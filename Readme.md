# 🤖 NoteBot AI


### Intelligent PDF Study Assistant using RAG + Conversational AI

---

## 🚀 Live Demo

🔗 https://genai-pdf-assistant-cjibutvbnxpzvhh4xaxqvw.streamlit.app/

## 💻 GitHub Repository

🔗 https://github.com/Suupratik/genai-pdf-assistant

---

## 📌 Overview

**NoteBot AI** is a **Generative AI-powered application** that transforms static PDF documents into an **interactive, conversational study assistant**.

It uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant document context and combines it with a **Large Language Model (LLM)** to generate accurate, explainable, and context-aware answers.

This system is designed to enhance:

* 📚 Learning efficiency
* 🧠 Concept understanding
* 📄 Document exploration

---

## ✨ Key Features

### 📄 Document Processing

* Upload **single or multiple PDFs**
* Multi-page text extraction
* Structured document understanding

---

### 🧠 RAG-Based Question Answering

* Ask questions in natural language
* Retrieves relevant chunks using **FAISS**
* Generates answers grounded in document context
* Adjustable **Top-K retrieval control**

---

### 📚 Study Assistant Capabilities

* 📑 **Summarization**
  → Generates structured summaries for quick revision

* 📌 **Important Points Extraction**
  → Identifies key exam-relevant concepts

* 📝 **Notes Generator**
  → Creates clean, structured study notes

* ❓ **MCQ Generator**
  → Produces practice questions with answers and explanations

* 🧒 **Explain Like Beginner**
  → Simplifies complex topics

---

### 💬 General AI Chatbot

* Works **independently of PDFs**
* Handles general queries and concept explanations
* Adjustable **temperature (creativity control)**

---

### 🔁 Conversational Memory

* Enables **follow-up questioning**
* Uses previous outputs for deeper understanding
* Supports multi-step learning interaction

---

### 📊 Transparency & Retrieval

* Displays **source document chunks**
* Shows **page numbers** for traceability
* Improves trust in generated responses

---

### 🛡️ Smart Guardrails

* Detects unfair queries like:

  * "paper leak"
  * "exact question"
* Responds ethically to prevent misuse

---

## 🧠 System Architecture (RAG Pipeline)

```
PDF Upload
   ↓
Text Extraction (PyPDF2)
   ↓
Chunking (Text Splitter)
   ↓
Embeddings (HuggingFace)
   ↓
Vector Storage (FAISS)
   ↓
User Query
   ↓
Similarity Search (Top-K)
   ↓
Context + Memory Injection
   ↓
LLM Processing (GROQ)
   ↓
Final Answer
```

---

## 🧰 Tech Stack

| Component       | Technology     |
| --------------- | -------------- |
| Language        | Python 🐍      |
| UI              | Streamlit 🎨   |
| LLM             | GROQ API ⚡     |
| Embeddings      | HuggingFace 🤖 |
| Vector Database | FAISS 📊       |
| PDF Processing  | PyPDF2 📄      |

---

## 📁 Project Structure

```
genai-pdf-assistant/
│
├── app.py                # Main application
├── requirements.txt     # Dependencies
├── README.md            # Documentation
├── .gitignore
├── .streamlit/
│   └── config.toml      # UI & system config
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Suupratik/genai-pdf-assistant.git
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

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

### 5️⃣ Run Application

```bash
streamlit run app.py
```

---

## ☁️ Deployment

Deployed using **Streamlit Community Cloud**

### Steps:

1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Add secret:

```
GROQ_API_KEY = "your_api_key"
```

4. Deploy 🚀

---

## 🧠 Concepts Implemented

* Retrieval-Augmented Generation (RAG)
* Large Language Models (LLMs)
* Prompt Engineering
* Semantic Search
* Vector Databases (FAISS)
* Embeddings
* Conversational Memory

---

## 🔮 Future Enhancements

* 📌 Highlight answers directly in PDF
* 📊 Confidence scoring
* 📄 Multi-document comparison
* 🌐 Multilingual support
* 📱 Mobile UI optimization

---


## 👨‍💻 Author

**Supratik Mitra**
B.Tech CSE (AI & ML)

---

## ⭐ Support

If you found this project useful:

* ⭐ Star the repository
* 🔗 Share with others

---

## 🎯 Final Note

This project demonstrates how **Generative AI + Retrieval Systems + Conversational Interfaces** can transform static documents into intelligent, interactive knowledge systems, enabling faster and deeper learning.