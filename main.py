import uuid
from dotenv import load_dotenv
import os
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from datetime import datetime
import gradio as gr
from langgraph.checkpoint.sqlite import SqliteSaver, sqlite3
from langchain_tavily import TavilySearch

# Load Environment variable
load_dotenv()


# Agent Tools
def get_date():
    """Get the current date"""
    return datetime.now().strftime("%m-%d-%Y")

search_tool = TavilySearch()

# System prompt for the model
system_prompt = """
You are a helpful assistant. 
Answer all user queries in a kind manner.
Use the get_date tool ONLY when the user is explicitly asking about today's date.
Use the search_tool for answering questions that require up to date information.
"""

# Establish an sqlite3 connection
conn = sqlite3.connect("chatbot_memory.db", check_same_thread=False)
checkpointer = SqliteSaver(conn)

# Create and configure the agent
llm = ChatOllama(model="qwen3:8b")
agent = create_agent(
    model=llm,
    tools=[get_date, search_tool],
    system_prompt=system_prompt, checkpointer=checkpointer
)

# Chat content
def chat(message, history, thread_id):
    config = {"configurable": {"thread_id": thread_id}}
    response = agent.invoke(
        {"messages": [{"role": "user", "content": message}]},
        config
    )
    last_response = response['messages'][-1].content
    return last_response

# Set up Gradio with a title and chat interface
with gr.Blocks() as demo:
    gr.Markdown("# AI Chatbot")
    thread_id = gr.State(value=lambda: str(uuid.uuid4()))
    gr.ChatInterface(fn=chat, additional_inputs=[thread_id])

demo.launch()