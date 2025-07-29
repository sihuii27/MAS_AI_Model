from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def get_vectorstore(pdf_file):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore = FAISS.from_texts(texts=pdf_file, embedding=embeddings)
    return vectorstore