from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain #allow chatting with the vector store
from langchain.chat_models import ChatOpenAI

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory,
    )
    return conversation_chain