"# Agentic_Claims_Assistant" 
# 🛡️ Agentic RAG Insurance Assistant

An AI-powered, agentic insurance assistant built using **LangGraph**, **LangChain**, and **Streamlit**. This application can intelligently answer complex insurance-related queries by orchestrating document retrieval (RAG), agent reasoning, and input/output guardrails.

---

## 🚀 Features

- ✅ Agentic Reasoning using **LangGraph** state machine
- 🔎 Retrieval-Augmented Generation (RAG) over 4 insurance policies
- 🛡️ Guardrails on both **user input** and **AI output**
- 🎛️ Interactive frontend via **Streamlit**
- 📄 Multi-policy support (e.g., maternity, critical illness, exclusions)

---

## 🧠 How It Works

```mermaid
graph TD;
    A[User Query via Streamlit] --> B[Input Guardrails]
    B --> C[LangGraph Agent]
    C --> D{Should use RAG?}
    D -->|Yes| E[RAG Tool]
    D -->|No| F[LLM Reasoning]
    E --> G[Context Fused Response]
    F --> G
    G --> H[Output Guardrails]
    H --> I[Final Answer to Streamlit]
