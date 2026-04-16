from dotenv import load_dotenv
import os
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from datetime import datetime

# Environment variables
load_dotenv()

# Tools
def get_date():
    """Get the current date"""
    return datetime.now().strftime("%m-%d-%Y")

# System prompt for the model
system_prompt = """
You are a helpful assistant.
Use the get_date tool if the user is asking about today's date.
"""
# User query
user_query = input("Enter a query: ")

# Create and configure the agent
llm = ChatOllama(model="qwen3:8b")
agent = create_agent(model=llm, tools=[get_date], system_prompt=system_prompt)
response = agent.invoke({"messages":[{"role": "user", "content": user_query}]})

# Print the models response
print(response['messages'][-1].content)