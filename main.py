import os
import streamlit as st
from dotenv import load_dotenv
from langchain.agents import Tool, initialize_agent, AgentType
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Streamlit UI
st.set_page_config(page_title="Agentic Claims Processing Assistant")
st.title("🤖 Agentic Claims Processing Assistant")

# File uploader
uploaded_file = st.file_uploader("📄 Upload a claim PDF", type=["pdf"])

if uploaded_file:
    os.makedirs("data", exist_ok=True)
    pdf_path = os.path.join("data", uploaded_file.name)
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.read())

    # PDF loader
    loader = PyPDFLoader(pdf_path)
    docs = loader.load_and_split()

    # Build vector store
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    retriever = vectorstore.as_retriever()

    # LLM
    llm = ChatOpenAI(model="gpt-4", temperature=0, openai_api_key=openai_api_key)

    # Tool 1: Document Reader
    def read_pdf(_: str) -> str:
        return "\n".join([doc.page_content for doc in docs])

    # Tool 2: QA from PDF
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    # Tool 3: Summarizer
    def summarize_claim(_: str) -> str:
        content = "\n".join([doc.page_content for doc in docs])
        prompt = (
            "You're an insurance claim assistant. Summarize the following claim document in 3 bullet points:\n"
            f"{content}"
        )
        return llm.invoke(prompt).content

    # Define tools
    tools = [
        Tool(
            name="DocumentReaderTool",
            func=read_pdf,
            description="Reads the full claim document and returns the raw text."
        ),
        Tool(
            name="PDFQATool",
            func=qa_chain.run,
            description="Answers specific questions about the uploaded claim PDF."
        ),
        Tool(
            name="SummarizerTool",
            func=summarize_claim,
            description="Summarizes the full claim document in 3 bullet points."
        ),
    ]

    # Initialize Agentic Flow (react agent)
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    # Input box for questions
    query = st.text_input("💬 Ask something about the claim:")
    if query:
        with st.spinner("🤖 Thinking..."):
            response = agent.run(query)
            st.success(response)
