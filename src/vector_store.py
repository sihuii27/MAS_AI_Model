from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS

def get_vectorstore(pdf_file):
    embeddings = HuggingFaceInstructEmbeddings(model_name='hkunlp/instructor-large')
    vectorstore = FAISS.from_texts(texts=pdf_file, embedding=embeddings)
    return vectorstore