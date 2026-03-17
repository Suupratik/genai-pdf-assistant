# 🤖 NoteBot AI — PDF Question Answering Assistant (RAG)

A **Generative AI-powered web application** that allows users to upload PDFs and ask questions.
Built using **Retrieval-Augmented Generation (RAG)**, this system retrieves relevant content from documents and generates accurate answers using an LLM.

---

## 📌 Overview

NoteBot AI is designed to simplify document understanding by enabling **interactive question-answering over PDFs**.
It combines **semantic search (FAISS)** with **LLM-based generation (GROQ)** to provide context-aware answers.

---

## ✨ Features

* 📄 Upload any PDF document
* 💬 Ask questions in natural language
* ⚡ Fast responses using GROQ LLM
* 🧠 Context-aware answers using RAG
* 📊 Semantic search with vector database (FAISS)
* 🎯 Clean chat-based UI (Streamlit)

---

## 🧠 How It Works (RAG Pipeline)

```
PDF Upload
   ↓
Text Extraction
   ↓
Chunking
   ↓
Embeddings (HuggingFace)
   ↓
Vector Storage (FAISS)
   ↓
User Query
   ↓
Similarity Search
   ↓
LLM (GROQ)
   ↓
Final Answer
```

---

## 🧰 Tech Stack

* **Python** 🐍
* **Streamlit** 🎨
* **FAISS** 📊 (Vector Database)
* **HuggingFace Embeddings** 🧠
* **GROQ API (LLM)** ⚡
* **PyPDF2** 📄

---

## 📁 Project Structure

```
genai-pdf-assistant/
│
├── app.py                # Main Streamlit app
├── requirements.txt     # Dependencies
├── .env                 # API key (not uploaded)
├── .streamlit/
│   └── config.toml      # UI config
├── README.md            # Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/genai-pdf-assistant.git
cd genai-pdf-assistant
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add API Key

Create `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

### 5️⃣ Run Application

```bash
streamlit run app.py
```

---

## ☁️ Deployment

Deployed using **Streamlit Community Cloud**:

* Connect GitHub repo
* Add API key in **Secrets**
* Deploy in one click

---

## 🔮 Future Improvements

* 📄 Multi-PDF support
* 🧠 Chat history memory
* 📊 Better document summarization
* 🎨 Advanced UI/UX enhancements
* 🔍 Highlight answers from document

---

## 🧠 Key Concepts Used

* Generative AI
* Large Language Models (LLMs)
* Prompt Engineering
* Embeddings
* Vector Databases (FAISS)
* Retrieval-Augmented Generation (RAG)

---

## 📌 Credits

* 👨‍💻 Developed by **Supratik Mitra**
* 💡 Guided by Generative AI Training Program

---

## ⭐ Support

If you found this project useful, give it a ⭐ on GitHub!
