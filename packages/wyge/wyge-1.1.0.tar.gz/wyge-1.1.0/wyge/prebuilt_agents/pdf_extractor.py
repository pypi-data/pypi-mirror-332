import streamlit as st
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
            st.error(f"Error extracting text content: {str(e)}")
        
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
                                
                            # Convert PIL Image to bytes for Streamlit
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
                        st.warning(f"Error extracting image {img_index} on page {page_num + 1}: {str(e)}")
        except Exception as e:
            st.error(f"Error extracting images: {str(e)}")
            
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
                    st.warning(f"Camelot lattice extraction error: {str(e)}")
            
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
                    st.warning(f"Camelot stream extraction error: {str(e)}")
            
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
            st.error(f"Error extracting tables: {str(e)}")

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
                st.warning(f"Could not remove temporary file: {str(e)}")

def main():
    st.title("PDF Content Extractor")
    
    # File upload
    uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])
    
    if uploaded_file:
        # Validate PDF file before processing
        try:
            # Check if the uploaded file is a valid PDF
            pdf_bytes = uploaded_file.getvalue()
            if not pdf_bytes.startswith(b'%PDF'):
                st.error("The uploaded file does not appear to be a valid PDF.")
                return
        except Exception as e:  
            st.error(f"Error validating PDF file: {str(e)}")
            return
            
        # Process the file in a context manager to ensure cleanup
        with temporary_file(pdf_bytes, suffix='.pdf') as file_path:
            try:
                # Get total pages
                with fitz.open(file_path) as pdf:
                    total_pages = len(pdf)
                
                # Page range selection
                st.write(f"Total pages: {total_pages}")
                col1, col2 = st.columns(2)
                with col1:
                    start_page = st.number_input("Start Page", min_value=1, max_value=total_pages, value=1)
                with col2:
                    end_page = st.number_input("End Page", min_value=start_page, max_value=total_pages, value=min(total_pages, start_page))
                
                # Add extraction options
                st.subheader("Extraction Options")
                col1, col2, col3 = st.columns(3)
                with col1:
                    extract_text = st.checkbox("Extract Text", value=True)
                with col2:
                    extract_images = st.checkbox("Extract Images", value=True)
                with col3:
                    extract_tables = st.checkbox("Extract Tables", value=True)
                
                # Table extraction advanced options
                if extract_tables:
                    with st.expander("Table Extraction Options"):
                        table_flavor = st.radio(
                            "Table Extraction Method", 
                            ["auto", "lattice", "stream", "pdfplumber"],
                            help="'auto' tries all methods. 'lattice' works best for tables with borders. 'stream' works better for tables without clear borders."
                        )
                else:
                    table_flavor = "auto"
                    
                # Add confirmation button to wait for user input
                extract_button = st.button("Extract Content")
                
                if extract_button:
                    # Initialize extractor with page range
                    page_range = (start_page, end_page) if start_page <= end_page else None
                    
                    with PDFExtractor(file_path, page_range) as extractor:
                        content = {'text': [], 'images': [], 'tables': []}
                        
                        # Extract content based on user selection
                        with st.spinner("Extracting content from PDF..."):
                            if extract_text:
                                content['text'] = extractor.extract_text()
                            if extract_images:
                                content['images'] = extractor.extract_images()
                            if extract_tables:
                                content['tables'] = extractor.extract_tables(table_flavor=table_flavor)
                        
                        # Display extracted content
                        st.subheader("Extracted Content")
                        
                        # Text content
                        if extract_text and content['text']:
                            st.write("### Text Content")
                            for item in content['text']:
                                st.text_area("Text", item['content'], height=300)
                                with st.expander("Text Metadata"):
                                    st.write(item['metadata'])
                                st.markdown("---")
                        elif extract_text:
                            st.info("No text content was extracted.")
                        
                        # Image content
                        if extract_images and content['images']:
                            st.write("### Images")
                            # Create grid layout for images
                            cols = st.columns(3)
                            for i, item in enumerate(content['images']):
                                with cols[i % 3]:
                                    st.image(item['content'], caption=f"Page {item['metadata']['page_number']}, Image {item['metadata']['image_index'] + 1}")
                                    with st.expander("Image Metadata"):
                                        st.write(item['metadata'])
                        elif extract_images:
                            st.info("No images were extracted.")
                        
                        # Table content
                        if extract_tables and content['tables']:
                            st.write("### Tables")
                            for idx, item in enumerate(content['tables']):
                                st.write(f"Table {idx+1} from page {item['metadata']['page_number']} (Method: {item['metadata'].get('method', 'unknown')})")
                                
                                # Create a proper DataFrame from the content
                                if item['content']:
                                    df = pd.DataFrame(item['content'])
                                    
                                    # Offer download option
                                    csv = df.to_csv(index=False).encode('utf-8')
                                    excel = io.BytesIO()
                                    df.to_excel(excel, index=False, engine='openpyxl')
                                    excel.seek(0)
                                    
                                    col1, col2 = st.columns(2)
                                    with col1:
                                        st.download_button(
                                            label=f"Download Table {idx+1} as CSV",
                                            data=csv,
                                            file_name=f"table_{item['metadata']['page_number']}_{idx+1}.csv",
                                            mime="text/csv"
                                        )
                                    with col2:
                                        st.download_button(
                                            label=f"Download Table {idx+1} as Excel",
                                            data=excel,
                                            file_name=f"table_{item['metadata']['page_number']}_{idx+1}.xlsx",
                                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                                        )
                                    
                                    st.dataframe(df)
                                else:
                                    st.info("Table structure detected but no data extracted.")
                                
                                with st.expander("Table Metadata"):
                                    st.write(item['metadata'])
                                st.markdown("---")
                        elif extract_tables:
                            st.info("No tables were detected.")
                
            except Exception as e:
                st.error(f"Error processing PDF: {str(e)}")
    
if __name__ == "__main__":
    main()