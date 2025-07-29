import streamlit as st
import extract_pdf as pdf
import chunk_text as text_chunker
import vector_store as vector_db
import conversation_chain as conversation_chain
from dotenv import load_dotenv

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
    st.title("Document Analysis App")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    prompt = st.chat_input("Ask something")
    if prompt:
        with st.chat_message("user"):
            st.write(prompt)

    with st.sidebar:
        st.title("Upload PDF Files")
        
        uploaded_files = st.file_uploader(
            "Choose a pdf file", accept_multiple_files=True, type=["pdf"]
        )

        if len(uploaded_files)== 0:
            st.warning("Please upload at least two pdf files.")
        elif len(uploaded_files) == 1:
            st.warning("Please upload one more pdf file.")
        elif len(uploaded_files) > 2:
            st.warning("You can only upload up to two pdf files.")

        submit_button = st.button(label="Submit", disabled=len(uploaded_files) != 2)
                  

        if submit_button:
            with st.spinner("Processing..."):
                for uploaded_file in uploaded_files:
                    if uploaded_file is not None:
                        #extract text from the PDF file
                        extract_text = pdf.extract_text_from_pdf(uploaded_file)
                        #get chunked text
                        chunk_text = text_chunker.chunk_text(extract_text)
                        #get vector store
                        vectorstore = vector_db.get_vectorstore(chunk_text)
                        #create conversation chain
                        st.session_state.conversation = conversation_chain.get_conversation_chain(vectorstore)
            st.success("Files processed successfully!")

if __name__ == "__main__":
    main()