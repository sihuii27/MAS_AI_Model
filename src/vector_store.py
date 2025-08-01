from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document

def get_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="intfloat/e5-large-v2",
        model_kwargs={'device': 'cpu'},
        # improve similarity search by normalizing embeddings
        encode_kwargs={'normalize_embeddings': True} 
    )
    vectorstore = FAISS.from_documents(chunks, embedding=embeddings)
    return vectorstore