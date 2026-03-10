from langchain_ollama import ChatOllama

def ask_question(vector_store, question):

    docs = vector_store.similarity_search(question, k=3)

    context = ""
    sources = []

    for doc in docs:
        context += doc.page_content + "\n"
        sources.append(doc.metadata)

    llm = ChatOllama(
        model="llama3",
        temperature=0
    )

    prompt = f"""
Gunakan konteks berikut untuk menjawab pertanyaan.

Konteks:
{context}

Pertanyaan:
{question}

Jawaban:
"""

    response = llm.invoke(prompt)

    return response.content, sources