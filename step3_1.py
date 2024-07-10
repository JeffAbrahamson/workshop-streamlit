import os

from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_openai import ChatOpenAI

db = SQLDatabase.from_uri("sqlite:///power-generation.sqlite")
llm = ChatOpenAI(
    model="gpt-3.5-turbo", temperature=0, api_key=os.getenv("OPENAI_API_KEY")
)
agent_executor = create_sql_agent(
    llm, db=db, agent_type="openai-tools", verbose=True
)

agent_executor.invoke(
    "How many countries are there in the power generation table"
)
agent_executor.invoke("How many rows are there in the power generation table")
