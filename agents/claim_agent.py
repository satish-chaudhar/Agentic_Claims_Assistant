from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from agents.tools import get_retrieval_tool, get_claim_classification_tool

def create_claim_agent(filepath):
    tools = [
        get_retrieval_tool(filepath),
        get_claim_classification_tool(),
    ]

    llm = ChatOpenAI(temperature=0, model="gpt-4")

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    return agent
