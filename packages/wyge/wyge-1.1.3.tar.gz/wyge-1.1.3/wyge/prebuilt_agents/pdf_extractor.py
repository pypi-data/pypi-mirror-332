import tempfile
import os
import fitz  # PyMuPDF
import camelot
import numpy as np
from PIL import Image
import io
from PyPDF2 import PdfReader
import pdfplumber
import contextlib
import pandas as pd

class PDFExtractor:
    def __init__(self, file_path: str, page_range: tuple = None):
        self.file_path = file_path
        self.page_range = page_range
        # Initialize PDF document only when needed
        self._pdf_document = None
        
    @property
    def pdf_document(self):
        """Lazy loading of PDF document"""
        if self._pdf_document is None:
            self._pdf_document = fitz.open(self.file_path)
        return self._pdf_document
        
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        
    def close(self):
        """Explicitly close the PDF document"""
        if hasattr(self, '_pdf_document') and self._pdf_document:
            try:
                self._pdf_document.close()
                self._pdf_document = None
            except Exception:
                pass
                
    def __del__(self):
        """Backup method to ensure resources are freed"""
        self.close()
        
    def _get_page_range(self, total_pages):
        """Get normalized page range with 0-based indexing"""
        if self.page_range and len(self.page_range) >= 2:
            start_page = max(0, self.page_range[0] - 1)  # Convert to 0-based index
            end_page = min(total_pages, self.page_range[1])
            return start_page, end_page
        else:
            return 0, total_pages
    
    def _get_page_range_1_based(self, total_pages):
        """Get normalized page range with 1-based indexing (for camelot)"""
        if self.page_range and len(self.page_range) >= 2:
            start_page = max(1, self.page_range[0])  # Keep as 1-based index
            end_page = min(total_pages, self.page_range[1])
            return start_page, end_page
        else:
            return 1, total_pages
        
    def extract_text(self):
        """Extract text content using PyPDF2"""
        text_content = []
        
        try:
            reader = PdfReader(self.file_path)
            text = ""
            total_pages = len(reader.pages)
            start_page, end_page = self._get_page_range(total_pages)
            
            for i, page in enumerate(reader.pages):
                if start_page <= i < end_page:
                    extracted_text = page.extract_text()
                    if extracted_text:  # Only add non-empty text
                        text += extracted_text + "\n"
            
            # Only add if we have actual content
            if text.strip():
                text_content.append({
                    'content': text,
                    'metadata': {
                        'source': self.file_path,
                        'page_range': self.page_range
                    }
                })
        except Exception as e:
            raise Exception(f"Error extracting text content: {str(e)}")
        
        return text_content
        
    def extract_images(self):
        """Extract images using PyMuPDF"""
        image_content = []
        
        try:
            total_pages = len(self.pdf_document)
            start_page, end_page = self._get_page_range(total_pages)
            
            for page_num in range(start_page, end_page):
                page = self.pdf_document[page_num]
                image_list = page.get_images(full=True)
                
                for img_index, img in enumerate(image_list):
                    try:
                        xref = img[0]
                        base_image = self.pdf_document.extract_image(xref)
                        image_bytes = base_image["image"]
                        
                        # Convert to PIL Image for validation and processing
                        with Image.open(io.BytesIO(image_bytes)) as image:
                            # Skip tiny images (often artifacts)
                            if image.width < 50 or image.height < 50:
                                continue
                                
                            # Convert PIL Image to bytes
                            img_byte_arr = io.BytesIO()
                            image.save(img_byte_arr, format=image.format if image.format else 'PNG')
                            img_format = image.format if image.format else 'PNG'
                            img_size = image.size
                            
                        image_content.append({
                            'content': img_byte_arr.getvalue(),
                            'metadata': {
                                'page_number': page_num + 1,
                                'image_index': img_index,
                                'format': img_format,
                                'size': img_size
                            }
                        })
                    except Exception as e:
                        print(f"Warning: Error extracting image {img_index} on page {page_num + 1}: {str(e)}")
        except Exception as e:
            raise Exception(f"Error extracting images: {str(e)}")
            
        return image_content
        
    def extract_tables(self, table_flavor="auto"):
        """Extract tables using the specified method"""
        table_content = []

        try:
            # Get page range with 1-based indexing for camelot
            with pdfplumber.open(self.file_path) as pdf:
                total_pages = len(pdf.pages)
            
            start_page, end_page = self._get_page_range_1_based(total_pages)
            page_str = ','.join(str(i) for i in range(start_page, end_page + 1))
            
            # Only use camelot-lattice if selected or auto
            if table_flavor in ["auto", "lattice"]:
                try:
                    tables_lattice = camelot.read_pdf(
                        self.file_path, 
                        pages=page_str, 
                        flavor='lattice',
                        suppress_stdout=True
                    )
                    print(len(tables_lattice))
                    print(tables_lattice)
                    for i, table in enumerate(tables_lattice):
                        if len(table.df) > 1: #table.accuracy > 40 and 
                            df = table.df.replace('', np.nan).dropna(how='all').fillna('')
                            if not df.empty and df.shape[0] > 1 and df.shape[1] > 1:
                                unique_values_by_col = [df[col].nunique() for col in df.columns]
                                col_variation = np.std(unique_values_by_col)
                                if col_variation > 0.1:
                                    table_content.append({
                                        'content': df.to_dict(orient='records'),
                                        'metadata': {
                                            'page_number': table.page,
                                            'table_index': i,
                                            'accuracy': table.accuracy,
                                            'method': 'camelot-lattice'
                                        }
                                    })
                except Exception as e:
                    print(f"Warning: Camelot lattice extraction error: {str(e)}")
            
            # Only use camelot-stream if selected or auto
            if table_flavor in ["auto", "stream"]:
                try:
                    tables_stream = camelot.read_pdf(
                        self.file_path, 
                        pages=page_str, 
                        flavor='stream',
                        suppress_stdout=True
                    )
                    
                    for i, table in enumerate(tables_stream):
                        if table.accuracy > 90 and len(table.df) > 1:
                            df = table.df.replace('', np.nan).dropna(how='all').fillna('')
                            if not df.empty and df.shape[0] > 2 and df.shape[1] > 2:
                                is_duplicate = False
                                for existing in table_content:
                                    if existing['metadata']['page_number'] == table.page:
                                        existing_df = pd.DataFrame(existing['content'])
                                        if (abs(len(df) - len(existing_df)) <= 2 or
                                            (df.values == existing_df.values).mean() > 0.7):
                                            is_duplicate = True
                                            break
                                
                                if not is_duplicate:
                                    avg_word_count = df.map(lambda x: len(str(x).split())).mean().mean()
                                    if avg_word_count < 15:
                                        table_content.append({
                                            'content': df.to_dict(orient='records'),
                                            'metadata': {
                                                'page_number': table.page,
                                                'table_index': i,
                                                'accuracy': table.accuracy,
                                                'method': 'camelot-stream'
                                            }
                                        })
                except Exception as e:
                    print(f"Warning: Camelot stream extraction error: {str(e)}")
            
            # Only use pdfplumber if selected or auto
            if table_flavor in ["auto", "pdfplumber"]:
                with pdfplumber.open(self.file_path) as pdf:
                    start_page, end_page = self._get_page_range(total_pages)  # 0-based for pdfplumber
                    
                    for page_num in range(start_page, end_page):
                        page = pdf.pages[page_num]
                        tables = page.extract_tables(table_settings={
                            "vertical_strategy": "lines_strict", 
                            "horizontal_strategy": "lines_strict",
                            "intersection_tolerance": 5,
                            "min_words_vertical": 3,
                            "min_words_horizontal": 3
                        })
                        
                        for idx, table in enumerate(tables):
                            if table and len(table) >= 3:
                                rows = []
                                for row in table:
                                    if row and sum(1 for cell in row if cell and cell.strip()) > 1:
                                        rows.append(row)
                                
                                if rows and len(rows) >= 3:
                                    df = pd.DataFrame(rows)
                                    if all(str(x).strip() for x in df.iloc[0]):
                                        df.columns = df.iloc[0]
                                        df = df.iloc[1:].reset_index(drop=True)
                                    df = df.replace('', np.nan).dropna(how='all', axis=1).dropna(how='all').fillna('')
                                    if not df.empty and df.shape[0] >= 3 and df.shape[1] >= 2:
                                        avg_chars_per_row = df.map(lambda x: len(str(x))).mean(axis=1)
                                        row_variation = avg_chars_per_row.std() / avg_chars_per_row.mean()
                                        avg_words = df.map(lambda x: len(str(x).split())).mean().mean()
                                        if row_variation < 0.5 and avg_words < 12:
                                            table_content.append({
                                                'content': df.to_dict(orient='records'),
                                                'metadata': {
                                                    'page_number': page_num + 1,
                                                    'table_index': idx,
                                                    'method': 'pdfplumber'
                                                }
                                            })
        except Exception as e:
            raise Exception(f"Error extracting tables: {str(e)}")

        return table_content

@contextlib.contextmanager
def temporary_file(content, suffix=None):
    """Context manager for handling temporary files safely"""
    temp_file = None
    try:
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
        temp_file.write(content)
        temp_file.close()
        yield temp_file.name
    finally:
        if temp_file and os.path.exists(temp_file.name):
            try:
                os.remove(temp_file.name)
            except Exception as e:
                print(f"Warning: Could not remove temporary file: {str(e)}")

def process_pdf(file_path, page_range=None, extract_text=True, extract_images=True, extract_tables=True, table_flavor="auto"):
    """Process PDF file and return extracted content"""
    # Validate PDF file before processing
    try:
        with open(file_path, 'rb') as f:
            if not f.read(4).startswith(b'%PDF'):
                raise ValueError("The file does not appear to be a valid PDF.")
    except Exception as e:
        raise Exception(f"Error validating PDF file: {str(e)}")
    
    content = {'text': [], 'images': [], 'tables': []}
    
    with PDFExtractor(file_path, page_range) as extractor:
        if extract_text:
            content['text'] = extractor.extract_text()
        if extract_images:
            content['images'] = extractor.extract_images()
        if extract_tables:
            content['tables'] = extractor.extract_tables(table_flavor=table_flavor)
    
    return content