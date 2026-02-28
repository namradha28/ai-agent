# 🤖 AI Agent Prototype (LLM + Tools + Memory)

A production-style AI Agent built using **FastAPI**, **Groq LLM (openai/gpt-oss-20b)**, custom tool routing, and conversation memory.

Deployed on Hugging Face Spaces.

---

## 🧠 Project Overview

This project demonstrates how to build a real AI Agent with:

- LLM-powered reasoning
- Tool execution capability
- Stateful conversation memory
- FastAPI backend
- Web-based chat interface
- Cloud deployment readiness

The agent intelligently routes user input to either:
- Custom tools (math, notes, weather)
- Or an LLM (Groq API)

---

## ✨ Features

- ✅ LLM Integration (Groq API)
- ✅ Model: `openai/gpt-oss-20b`
- ✅ Tool Calling (Manual routing logic)
- ✅ Conversation Memory (Chat History)
- ✅ FastAPI Backend
- ✅ Clean Web UI
- ✅ Hugging Face Deployment Ready
- ✅ Modular Architecture

---

## 🏗️ System Architecture

```
User
  ↓
Frontend (HTML/CSS)
  ↓
FastAPI Backend
  ↓
Agent Router
  ├── Math Tool
  ├── Weather Tool
  ├── Notes Tool
  └── LLM (Groq)
  ↓
Response
```

---

## 📂 Project Structure

```
ai-agent-prototype/
│
├── app.py              # FastAPI application
├── agent.py            # LLM logic + memory + routing
├── tools.py            # Custom tool functions
├── requirements.txt
├── templates/
│     └── index.html
├── static/
│     └── style.css
```

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Groq API
- openai/gpt-oss-20b
- Jinja2
- HTML / CSS
- Hugging Face Spaces

---

## 🔧 Implemented Tools

| Tool | Description |
|------|------------|
| calculate() | Evaluates math expressions |
| get_weather() | Returns mock weather data |
| save_note() | Saves key-value memory |
| get_note() | Retrieves stored notes |

---

## 🧠 Conversation Memory

The agent maintains session-based memory using:

```python
chat_history = [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
]
```

This enables:

- Context retention
- Follow-up understanding
- Multi-turn conversations

---

## ⚙️ Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/ai-agent-prototype.git
cd ai-agent-prototype
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Create `.env` File

```
GROQ_API_KEY=your_api_key_here
```

### 4️⃣ Start Server

```bash
uvicorn app:app --reload --port 8003
```

Open:

```
http://127.0.0.1:8003
```

---

## 🌍 Deployment (Hugging Face Spaces)

1. Create new Space (FastAPI or Blank)
2. Upload all project files (except `.env`)
3. Add environment variable:

```
GROQ_API_KEY=your_api_key
```

4. Restart the Space

---

## 📈 Future Enhancements

- Persistent database memory
- LLM-based tool selection
- Multi-step reasoning loop
- User authentication
- RAG integration
- Streaming responses
- Token management & optimization

---

## 🎯 Why This Project Is Valuable

This project demonstrates:

- LLM integration in real applications
- Agent design patterns
- Tool orchestration logic
- Backend engineering with FastAPI
- Deployment to production environment

It reflects real-world AI system design principles.

---

## 👩‍💻 Author

Namradha Mani  
AI • Data • Cloud • Full Stack Enthusiast

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
