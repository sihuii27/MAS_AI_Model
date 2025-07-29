from langchain.text_splitter import CharacterTextSplitter

def chunk_text(pdf_file):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000, #1000 characters per chunk
        chunk_overlap=200, #200 characters overlap
        length_function=len
    )
    chunks = text_splitter.split_text(pdf_file)
    return chunks