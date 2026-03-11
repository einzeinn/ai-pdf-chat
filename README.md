# AI PDF Chat

AI PDF Chat is a simple application that allows users to ask questions about a PDF document using a local LLM.

The system converts the content of the PDF into vector embeddings and retrieves the most relevant context when answering a question.

## Features

* Upload a PDF file
* Convert PDF content into vector embeddings
* Retrieve relevant document context
* Answer questions using a local LLM

## Tech Stack

* Python
* Streamlit
* LangChain
* Ollama
* Llama3
* Sentence Transformers
* Chroma Vector Database

## Installation

Clone the repository:

```
git clone https://github.com/einzeinn/ai-pdf-chat.git
cd ai-pdf-chat
```

Create a virtual environment:

```
python -m venv venv
```

Activate the virtual environment.

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

## Running the Application

Make sure Ollama is installed and the Llama3 model is available.

Run the model:

```
ollama run llama3
```

Start the application:

```
streamlit run app.py
```

## How It Works

1. The user uploads a PDF file
2. The system reads the content of the PDF
3. The text is converted into embeddings
4. The embeddings are stored in a vector database
5. When the user asks a question, the system retrieves the most relevant context
6. The LLM generates an answer based on that context

## Future Improvements

* Support multiple PDFs
* Add chat history
* Improve the UI
* Support more LLM models

## Demo

![Screenshot 1](Screenshot 2026-03-11 214558.png)
*Step 1: Tampilan awal program*

![Screenshot 2](Screenshot 2026-03-11 214640.png)
*Step 2: Upload file PDF*

![Screenshot 3](Screenshot 2026-03-11 214734.png)
*Step 3: Model menjawab pertanyaan*
