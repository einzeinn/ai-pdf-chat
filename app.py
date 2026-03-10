import streamlit as st

from pdf_loader import load_pdf
from vector_store import create_vector_store
from chat_engine import ask_question


st.title("AI Chat With PDF")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF uploaded successfully")

    documents = load_pdf("temp.pdf")
    vector_store = create_vector_store(documents)

    question = st.text_input("Ask a question about the PDF")

    if question:
        answer, sources = ask_question(vector_store, question)
        st.write("Answer:")
        st.write(answer)

        st.write("Sources:")
        for source in sources:
            st.write(f"Page: {source.get('page', 'Unknown')}")