import streamlit as st
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os
import random

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from groq import Groq

# =======================
# LOAD ENV
# =======================
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

# =======================
# UI
# =======================
st.set_page_config(page_title="NoteBot AI", page_icon="🤖", layout="wide")

st.title("🤖 NoteBot AI – Smart Study Assistant")
st.caption("RAG + Chatbot + Study Intelligence")

# =======================
# SESSION
# =======================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "last_output" not in st.session_state:
    st.session_state.last_output = ""

# =======================
# SAFETY
# =======================
def detect_unfair_query(query):
    keywords = ["paper leak", "exact question", "predict exact"]
    return any(k in query.lower() for k in keywords)

def savage_reply():
    return random.choice([
        "Go study 😄 no shortcuts!",
        "Not happening 😂",
        "Focus on concepts 😉"
    ])

# =======================
# SIDEBAR
# =======================
with st.sidebar:

    files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)

    k = st.slider("Accuracy (Top-K)", 1, 10, 5)
    temperature = st.slider("Creativity", 0.0, 1.0, 0.7)
    use_memory = st.checkbox("Chat with Generated Content", value=True)

    study_mode = st.selectbox(
        "Mode",
        [
            "Ask Question",
            "Summarize",
            "Important Points",
            "Notes",
            "MCQ Test",
            "Explain Simple",
            "General Chatbot"
        ]
    )

    if st.button("Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

    if st.button("Reset App"):
        st.session_state.chat_history = []
        st.session_state.vector_store = None
        st.session_state.last_output = ""

# =======================
# PROCESS PDF
# =======================
if files and st.session_state.vector_store is None:

    documents = []

    for file in files:
        pdf = PdfReader(file)
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                documents.append({"text": text, "page": i + 1})

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

    chunks = []
    metadatas = []

    for doc in documents:
        split_texts = splitter.split_text(doc["text"])
        for chunk in split_texts:
            chunks.append(chunk)
            metadatas.append({"page": doc["page"]})

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    st.session_state.vector_store = FAISS.from_texts(
        chunks,
        embeddings,
        metadatas=metadatas
    )

    st.success("PDF Processed!")

# =======================
# INPUT
# =======================
query = None

if study_mode in ["Ask Question", "General Chatbot"]:
    query = st.chat_input("Ask anything...")
else:
    if st.button("Run"):
        query = "RUN"

# =======================
# GENERAL CHATBOT
# =======================
if study_mode == "General Chatbot" and query:

    st.session_state.chat_history.append(("user", query))

    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            temperature=temperature,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": query}
            ]
        )

    answer = response.choices[0].message.content

    st.session_state.chat_history.append(("bot", answer))
    st.session_state.last_output = answer

# =======================
# MAIN RAG LOGIC
# =======================
elif (query or study_mode != "Ask Question") and st.session_state.vector_store:

    if study_mode == "Ask Question":

        if detect_unfair_query(query):
            answer = savage_reply()
            st.session_state.chat_history.append(("bot", answer))
        else:
            st.session_state.chat_history.append(("user", query))

    docs = st.session_state.vector_store.similarity_search(
        query if query else "summary", k=max(k, 5)
    )

    context = "\n\n".join([d.page_content for d in docs])
    extra_context = st.session_state.last_output if use_memory else ""

    # =======================
    # PROMPTS
    # =======================
    if study_mode == "Summarize":
        prompt = f"""
Give a structured summary with headings.

{context}
"""

    elif study_mode == "Important Points":
        prompt = f"""
Extract exam-important key points.

{context}
"""

    elif study_mode == "Notes":
        prompt = f"""
Create exam notes including:
- Definitions
- Key concepts
- Bullet points

{context}
"""

    elif study_mode == "MCQ Test":
        prompt = f"""
Generate 5 MCQs with:
- Question
- Options A/B/C/D
- Correct answer
- Explanation

{context}
"""

    elif study_mode == "Explain Simple":
        prompt = f"""
Explain like teaching a beginner.

{context}
"""

    else:
        prompt = f"""
You are a smart academic assistant.

Use:
- PDF context
- Previous generated output

Previous Output:
{extra_context}

Context:
{context}

Question:
{query}

Answer clearly and structured.
"""

    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            temperature=temperature,
            messages=[{"role": "user", "content": prompt}]
        )

    answer = response.choices[0].message.content

    st.session_state.chat_history.append(("bot", answer))
    st.session_state.last_output = answer

    # SOURCE DISPLAY
    with st.expander("📄 Sources"):
        for d in docs[:3]:
            st.write(f"📍 Page {d.metadata['page']}")
            st.write(d.page_content[:300])

# =======================
# DISPLAY CHAT (CORRECT ORDER)
# =======================
for role, msg in st.session_state.chat_history:
    if role == "user":
        st.markdown(f'<div style="text-align:right; margin:10px;"><b>🧑 {msg}</b></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="text-align:left; margin:10px;">🤖 {msg}</div>', unsafe_allow_html=True)