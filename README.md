# 🤖 AI Agent Chat

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com)
[![LangGraph](https://img.shields.io/badge/LangGraph-FF6B6B?style=for-the-badge)](https://langchain-ai.github.io/langgraph/)
[![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![Gradio](https://img.shields.io/badge/Gradio-F97316?style=for-the-badge&logo=gradio&logoColor=white)](https://gradio.app)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)
[![License](https://img.shields.io/badge/License-MIT-00ff41?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-30363d?style=for-the-badge)]()

</div>

> A local-first conversational AI agent powered by Ollama, LangChain, and LangGraph — with persistent per-thread memory, live web search, and a browser-based chat UI.

Runs a locally-hosted `qwen3:8b` model through LangChain's agent framework, wires in Tavily web search and a date tool, persists conversation state in SQLite, and exposes it all through a Gradio chat interface. Each session gets its own thread ID so the agent remembers context across turns without leaking memory between users.

---

## ⚡ Features

- **Runs models locally** via Ollama — no cloud API keys needed for inference
- **Persists conversations** in a SQLite database using LangGraph's `SqliteSaver` checkpointer
- **Isolates sessions** with per-user UUID thread IDs so chat histories stay scoped
- **Searches the web** through Tavily when the agent detects a query needs current information
- **Fetches today's date** via a built-in tool for time-sensitive questions
- **Serves a browser UI** through Gradio's `ChatInterface` with zero frontend code
- **Follows a system prompt** that governs tool use policy and response tone

---

## 🔧 Requirements

- Python `3.11+`
- [Ollama](https://ollama.com) installed locally with the `qwen3:8b` model pulled
- A Tavily API key ([tavily.com](https://tavily.com))

```plaintext
langchain
google-genai
langchain-google-genai
ollama
langchain-ollama
langchain-community
gradio
langgraph
langgraph-checkpoint-sqlite
python-dotenv
```

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/Kat0x0Ace/ai-agent-chat.git
cd ai-agent-chat

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Pull the local model
ollama pull qwen3:8b
```

Create an `.env` file in the project root:

```plaintext
TAVILY_API_KEY=your_tavily_api_key_here
```

---

## 🚀 Usage

```bash
# Make sure Ollama is running in the background
ollama serve

# Launch the chat app
python main.py
```

Gradio prints a local URL (typically `http://127.0.0.1:7860`) — open it in your browser and start chatting.

---

## 🧩 Agent Tools

| Tool | Purpose | Trigger |
|---|---|---|
| `get_date` | Returns today's date in `MM-DD-YYYY` format | User explicitly asks about the current date |
| `search_tool` | Tavily web search for real-time information | Queries requiring up-to-date data |

---

## 🔍 Example Output

```bash
python main.py
```

```plaintext
* Running on local URL:  http://127.0.0.1:7860
* To create a public link, set `share=True` in `launch()`.
```

Sample conversation:

```plaintext
User: What's today's date?
Agent: Today's date is 04-21-2026.

User: Who won the last F1 Grand Prix?
Agent: [searches via Tavily] ...returns current race results.
```

<img width="3134" height="1650" alt="image" src="https://github.com/user-attachments/assets/dbfcd39a-6e16-4925-8579-3e41fb7c0bc4" />

---

## 📁 Project Structure

```plaintext
ai-agent-chat/
├── main.py              # Agent setup, tools, Gradio UI, event loop
├── requirements.txt     # Python dependencies
├── .env                 # TAVILY_API_KEY
├── chatbot_memory.db    # Auto-generated SQLite checkpoint store
└── README.md
```

---

## ⚙️ How It Works

**Step 1 — Model & Tool Registration**
`ChatOllama` loads the local `qwen3:8b` model. Two tools are registered with the agent: `get_date` (a plain Python function) and `TavilySearch` (web search). A system prompt defines when each tool should fire.

**Step 2 — Memory & Agent Assembly**
`sqlite3` opens a connection to `chatbot_memory.db` and wraps it in LangGraph's `SqliteSaver` checkpointer. `create_agent()` stitches the model, tools, system prompt, and checkpointer into a single ReAct-style agent that persists state between invocations.

**Step 3 — Per-Session Threading & UI**
Gradio's `gr.State` generates a fresh UUID per browser session, passed into the agent as a `thread_id` in its config. The checkpointer scopes memory to that thread, so each user gets an isolated conversation history. `gr.ChatInterface` handles rendering, message dispatch, and history display with no custom frontend code.

---

<div align="center">

## 👤 Author

[![GitHub](https://img.shields.io/badge/GitHub-🧡Kat0x0Ace-181717?style=for-the-badge&logo=github)](https://github.com/Kat0x0Ace)

![footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer)

</div>
