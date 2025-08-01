from langchain.text_splitter import CharacterTextSplitter

def chunk_text(pdf_file):
    text_splitter = CharacterTextSplitter(
        separator="\n\n=====",
        chunk_size=1000, #1000 characters per chunk
        chunk_overlap=200, #200 characters overlap
        length_function=len,
        is_separator_regex=True
    )
    file_section = text_splitter.split_text(pdf_file)
    chunks = []
    regular_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000, 
        chunk_overlap=100,
        length_function=len
    )
    for section in file_section:
        if "File:" in section:
            # Split the section into chunks
            section_chunks = regular_splitter.split_text(section)
            chunks.extend(section_chunks)
            
    return chunks