from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain #allow chatting with the vector store
from langchain_groq import ChatGroq
import os 

def get_conversation_chain(vectorstore):
    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile",
        temperature=0.1,
    )
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory,
    )
    return conversation_chain