"# Agentic_Claims_Assistant" 
# 🤖 Agentic Claims Processing Assistant

This project is an **Agentic GenAI-powered Streamlit app** that allows users to upload insurance claim PDFs and interact with them through natural language. It supports claim summarization, question answering (QA), and raw document inspection using LangChain Agents and Tools.

---

## 🚀 Features

- 📄 Upload claim documents (PDF format)
- 🔎 Ask natural questions like "What is the claim amount?"
- 🧠 Agentic flow: LLM selects appropriate tools (QA, summarizer, reader)
- 🧰 Built using LangChain Tools + GPT-4
- 🖥️ Clean Streamlit UI

---

## 🛠️ Tech Stack

| Component       | Description                              |
|----------------|------------------------------------------|
| **Streamlit**   | Web interface for the assistant          |
| **LangChain**   | Agent and Tools framework                |
| **FAISS**       | Vector store for semantic search         |
| **OpenAI GPT-4**| LLM used for reasoning and responses     |
| **PyPDFLoader** | PDF ingestion and text extraction        |

---

## 🧩 Architecture

```mermaid
graph TD
    A[User Uploads PDF] --> B[PDF Loader (PyPDFLoader)]
    B --> C[Chunking & Embeddings (OpenAIEmbeddings)]
    C --> D[FAISS Vector Store]
    D --> E[RetrieverQA Tool]
    B --> F[Raw Reader Tool]
    B --> G[Summarizer Tool]
    H[User Asks Question] --> I[Agent (Zero-Shot ReAct)]
    I --> |Tool Selection| E
    I --> |Tool Selection| F
    I --> |Tool Selection| G
    E --> J[Response]
    F --> J
    G --> J
    J --> K[Streamlit Output]
