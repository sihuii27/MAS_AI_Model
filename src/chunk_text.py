from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import re

def chunk_text(pdf_text):
    chunks = []
    
    # split files using regex
    file_sections = re.split(r"\n+===== File: (.*?) =====\n+", pdf_text)
    
    # file_sections split into file names and content
    for i in range(1, len(file_sections), 2):
        file_name = file_sections[i].strip()
        content = file_sections[i + 1].strip()
        
        # split content into chunks using RecursiveCharacterTextSplitter
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=150,
            length_function=len,
            separators=["\n\n", "\n", ".", " ", ""]
        )
        
        section_chunks = splitter.split_text(content)
        # create document objects for each chunk
        for j, chunk in enumerate(section_chunks):
            chunks.append(Document(page_content=chunk, metadata={"file_name": file_name, "chunk": j}))
    
    return chunks
