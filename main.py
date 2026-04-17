from dotenv import load_dotenv
import os
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from datetime import datetime
import gradio as gr

# Environment variables
load_dotenv()

# Agent Tools
def get_date():
    """Get the current date"""
    return datetime.now().strftime("%m-%d-%Y")

# System prompt for the model
system_prompt = """
You are a helpful assistant. 
Answer all user queries in a kind manner.
Use the get_date tool ONLY when the user is explicitly asking about today's date.
"""

# Create and configure the agent
llm = ChatOllama(model="qwen3:8b")
agent = create_agent(
    model=llm,
    tools=[get_date],
    system_prompt=system_prompt
)

# Chat content
def chat(message, history):
    response = agent.invoke({"messages":[{"role": "user", "content": message}]})
    last_response = response['messages'][-1].content
    return last_response

# Set up Gradio with a title and chat interface
with gr.Blocks() as demo:
    gr.Markdown('# AI Chatbot')
    gr.ChatInterface(fn=chat)


demo.launch()