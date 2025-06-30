# 📄 Doc-AMA – Ask Me Anything from a PDF

Doc-AMA is a lightweight app that lets you upload a PDF and ask natural language questions about its content.
It combines local PDF parsing, semantic chunking, vector similarity search, and LLM-powered answers using **open-access models** like Windsurf or OpenRouter.

---

## 🌟 Features

- 🗂 Upload any PDF file and extract clean text
- 🔍 Chunk and embed the document using Sentence Transformers
- 🤖 Ask questions about the PDF — get smart, context-aware answers
- 💡 Uses retrieval-augmented generation (RAG) with FAISS or Chroma
- ⚙️ Switch between OpenRouter, Ollama, or other backends
- 🧱 Modular codebase (parser, embedder, retriever, LLM handler)

---

## 🧠 Why I Built This

I wanted to deeply understand how modern RAG (retrieval-augmented generation) works — how to go from unstructured documents to semantically meaningful answers powered by LLMs.
Doc-AMA is built to be clean, hackable, and open — and to help me grow beyond vibe coding into system-level thinking.

---

## 🧰 Tech Stack

| Layer | Tool |
|-------|------|
| 🧾 PDF Parsing | `PyMuPDF` (`fitz`) |
| 🧠 Embeddings | `sentence-transformers` (e.g., MiniLM) |
| 🔎 Vector Store | `FAISS` or `Chroma` |
| 💬 LLM Backend | `OpenRouter`, `Ollama`, or `Windsurf` |
| 🧑‍💻 UI | `Gradio` |
| 🔄 Deployment | Hugging Face Spaces |

---

## 🧪 Running Locally

### 1. Install dependencies (using [uv](https://github.com/astral-sh/uv))
```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### 2. Set required environment variables
Create a `.env` file in the project root (or export variables in your shell) with the following keys:

```bash
# OpenRouter (https://openrouter.ai)
OPENROUTER_API_KEY=sk-...

# Ollama (https://ollama.com) – only needed if you choose the Ollama backend
# For local Ollama use the default below
OLLAMA_BASE_URL=http://localhost:11434

# Windsurf (https://github.com/pygmalion-ai/windsurf) – optional
WINDSURF_BASE_URL=http://localhost:8000
```

You can mix-and-match providers at runtime via the **Settings** panel in the UI. If a backend is not configured, it will be hidden automatically.

### 3. Launch the app
```bash
python app.py
```
By default the Gradio interface will be available at <http://localhost:7860>.

---

## ⚙️ Configuration
Key settings live in `config.py` and can be tweaked without touching the core code. Notable options:

| Setting | Default | Description |
|---------|---------|-------------|
| `CHUNK_SIZE` | `1024` tokens | Maximum chunk size passed to the embedder |
| `VECTOR_DB` | `"faiss"` | Choose between `faiss` (in-memory) or `chroma` (persistent) |
| `EMBED_MODEL_NAME` | `"sentence-transformers/all-MiniLM-L6-v2"` | Hugging Face model used for embeddings |
| `MAX_CONTEXT_CHUNKS` | `5` | How many relevant chunks to stuff into the LLM prompt |

Changes are picked up on the next run.

---

## 📁 Project Structure
```text
docama/
├── app.py            # Gradio UI & orchestrator
├── config.py         # Central configuration
├── embedder.py       # Sentence-Transformers wrapper
├── llm.py            # Thin client for LLM backends (OpenRouter, Ollama, Windsurf)
├── parser.py         # PDF text extraction & chunking
├── retriever.py      # FAISS/Chroma similarity search
├── utils.py          # Helper functions
└── README.md         # You are here 🎉
```
The `src/docama` directory is reserved for packaging if you wish to `pip install` the project in the future.

---

## 🚀 Deployment
The easiest way to share Doc-AMA is via **Hugging Face Spaces**:
1. Push this repository to your HF account.
2. In the Space settings, choose the **Gradio** runtime.
3. Set the same environment variables as in the `.env` file (under *Variables & secrets*).
4. Click **Restart Space** – done!

For containerised deployments you can adapt the provided `Dockerfile` example (coming soon) or rely on services like Fly.io, Render.com, or AWS App Runner.

---

> *Built with <3 by [YOUR NAME] — happy hacking!*