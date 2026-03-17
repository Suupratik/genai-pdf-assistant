import streamlit as st
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from groq import Groq

# =======================
# LOAD ENV
# =======================
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

# =======================
# UI
# =======================
st.set_page_config(page_title="NoteBot AI", page_icon="🤖", layout="wide")

st.markdown("""
<style>
.main { background-color: #0E1117; }
.chat-box {
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
    max-width: 75%;
}
.user {
    background-color: #1f77b4;
    color: white;
    margin-left: auto;
}
.bot {
    background-color: #262730;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 NoteBot AI (GROQ Powered)")
st.caption("FREE AI PDF Assistant")

# =======================
# SIDEBAR
# =======================
with st.sidebar:
    file = st.file_uploader("Upload PDF", type="pdf")

# =======================
# SESSION
# =======================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

# =======================
# PROCESS PDF
# =======================
if file and st.session_state.vector_store is None:

    with st.spinner("Processing PDF..."):
        pdf = PdfReader(file)
        text = ""
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )
        chunks = splitter.split_text(text)

        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        st.session_state.vector_store = FAISS.from_texts(chunks, embeddings)

    st.success("PDF Ready!")

# =======================
# CHAT
# =======================
query = st.chat_input("Ask your question...")

if query and st.session_state.vector_store:

    st.session_state.chat_history.append(("user", query))

    docs = st.session_state.vector_store.similarity_search(query)
    context = "\n\n".join(
    [d.page_content.strip().replace("\n", " ") for d in docs[:6]]
)

    prompt = f"""
You are a smart academic assistant.

Answer ONLY from the given context.

Rules:
- Do NOT add extra assumptions
- Do NOT generate unrelated text
- Keep answers clear and structured
- If answer is not present, say:
  "I don't know based on the document."

Context:
{context}

Question:
{query}

Answer:
"""

    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

    answer = response.choices[0].message.content
    st.session_state.chat_history.append(("bot", answer))

# =======================
# DISPLAY
# =======================
for role, msg in st.session_state.chat_history:
    if role == "user":
        st.markdown(f'<div class="chat-box user">{msg}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-box bot">{msg}</div>', unsafe_allow_html=True)