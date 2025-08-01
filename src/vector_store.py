from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def get_vectorstore(pdf_file):
    embeddings = HuggingFaceEmbeddings(
        model_name="intfloat/e5-large-v2",
        model_kwargs={'device': 'cpu'},
        # improve similarity search by normalizing embeddings
        encode_kwargs={'normalize_embeddings': True} 
    )
    vectorstore = FAISS.from_texts(texts=pdf_file, embedding=embeddings)
    return vectorstore