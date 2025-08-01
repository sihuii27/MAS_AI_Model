import streamlit as st
import extract_pdf as pdf
import chunk_text as text_chunker
import vector_store as vector_db
import conversation_chain as conversation_chain
from dotenv import load_dotenv

st.set_page_config(page_title="Document Analysis", layout="wide")

def handle_response(prompt):
    if st.session_state.conversation:
        with st.chat_message("user"):
            st.write(prompt)
        #add user message to session state
        st.session_state.messages.append({"role": "user", "content": prompt})
        response = st.session_state.conversation({"question": prompt+ "Be detailed and cite evidence where possible. Provide answers that are in the source documents. Unless the question is not related to the documents."})
        answer = response["answer"]
        with st.chat_message("assistant"):
            st.write(answer)
        #add assistant response to session state
        st.session_state.messages.append({"role": "assistant", "content": response["answer"]})
        
    else:
        st.error("Please upload PDF files to start the conversation.")
        
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        min-width: 550px; 
        max-width: 550px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def main():
    load_dotenv()
    st.title("PDF Document Analysis")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    prompt = st.chat_input("Ask something")
    if prompt:
        handle_response(prompt)

    with st.sidebar:
        st.title("Upload PDF Files")
        
        uploaded_files = st.file_uploader(
            "Choose a pdf file", accept_multiple_files=True, type=["pdf"]
        )

        if len(uploaded_files)== 0:
            st.warning("Please upload at least one pdf file.")

        submit_button = st.button(label="Submit", disabled=len(uploaded_files) != 2)
       

        if submit_button:
            with st.spinner("Processing..."):
                if uploaded_files is not None:
                    #extract text from the PDF file
                    extract_text = pdf.extract_text_from_pdf(uploaded_files)
                    #get chunked text
                    chunk_text = text_chunker.chunk_text(extract_text)
                    st.write("Chunked Text:", chunk_text)
                    #get vector store
                    vectorstore = vector_db.get_vectorstore(chunk_text)
                    #create conversation chain
                    st.session_state.conversation = conversation_chain.get_conversation_chain(vectorstore)
                    st.session_state.messages = []
            st.success("Files processed successfully!")
            

if __name__ == "__main__":
    main()