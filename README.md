# AI PDF Chat

AI PDF Chat adalah aplikasi sederhana untuk bertanya kepada file PDF menggunakan model LLM lokal.

Project ini menggunakan vector search untuk memahami isi dokumen dan kemudian menjawab pertanyaan berdasarkan konteks dari PDF tersebut.

## Features

* Upload file PDF
* Mengubah isi PDF menjadi embedding vector
* Mencari konteks yang relevan
* Menjawab pertanyaan menggunakan model LLM lokal

## Tech Stack

* Python
* Streamlit
* LangChain
* Ollama
* Llama3
* Sentence Transformers
* Chroma Vector Database

## Installation

Clone repository:

```
git clone https://github.com/einzeinn/ai-pdf-chat.git
cd ai-pdf-chat
```

Buat virtual environment:

```
python -m venv venv
```

Aktifkan virtual environment:

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

## Running The App

Pastikan Ollama sudah berjalan dan model Llama3 sudah terinstall.

```
ollama run llama3
```

Jalankan aplikasi:

```
streamlit run app.py
```

## How It Works

1. User upload file PDF
2. Sistem membaca isi PDF
3. Teks diubah menjadi embedding vector
4. Vector disimpan di vector database
5. Ketika user bertanya, sistem mencari konteks yang paling relevan
6. Model LLM menghasilkan jawaban berdasarkan konteks tersebut

## Future Improvements

* Multiple PDF support
* Chat history
* Better UI
* Support lebih banyak model
