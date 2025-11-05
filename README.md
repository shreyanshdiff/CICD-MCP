
# 🚀 CI/CD Optimization Assistant (MCP + LangChain + Groq)

### 🧩 3-Line Overview

* An **AI-powered DevOps assistant** that analyzes Jenkins pipelines and logs to detect failures, bottlenecks, and performance issues.
* Built using **LangChain + Groq + FastAPI + FastMCP** for real-time CI/CD intelligence and conversational analysis.
* Enables **automated DevOps optimization** through LLM insights, caching suggestions, and build-time diagnostics.

---

## 🧠 Project Description

The **CI/CD Optimization Assistant** is a cutting-edge **AI DevOps agent** that streamlines your Jenkins pipeline diagnostics and optimization process.
It connects Groq’s **ultra-fast inference engine** with **LangChain’s LLM orchestration** to analyze logs, interpret failures, and propose improvements such as:

* **Parallelization** of build stages
* **Caching strategies** to reduce build time
* **Pipeline restructuring** for higher efficiency

This project also includes a **FastMCP server** (built with FastAPI) to simulate Jenkins log retrieval and test result analysis — allowing easy integration into MLOps or CI/CD environments.

---

## 🧱 Features

✅ **Conversational CI/CD Analysis** – Chat with the AI to debug Jenkins logs interactively
✅ **Groq-Powered LLM** – Uses `llama-3.3-70b-versatile` for lightning-fast inference
✅ **Memory-Aware Context** – Tracks conversation history for better DevOps insights
✅ **MCP Integration** – Deployable as a local MCP server to interface with build/test data
✅ **Secure Design** – Secrets handled via `.env` and `.gitignore` to ensure safe deployments

---

## 🧰 Tech Stack

| Component                  | Technology                           |
| -------------------------- | ------------------------------------ |
| **Language Model**         | Groq (Llama-3.3-70B-Versatile)       |
| **Frameworks**             | LangChain, FastAPI, FastMCP          |
| **Memory**                 | LangChain `ConversationBufferMemory` |
| **Environment Management** | Python-dotenv                        |
| **Runtime**                | Uvicorn                              |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/CI-CD-Optimization-Assistant.git
cd CI-CD-Optimization-Assistant
```

### 2️⃣ Create and Configure `.env`

```bash
GROQ_API_KEY=your_api_key_here
```

*(Make sure `.env` is listed in `.gitignore` to avoid committing secrets.)*

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the DevOps Analyzer

```bash
python main.py
```

This will:

* Run an initial **automated analysis** of sample Jenkins logs
* Start an **interactive chat** where you can ask questions about logs or pipeline performance

### 5️⃣ Run the MCP Server (Optional)

```bash
python mcp_server.py
```

Then visit:

```
http://localhost:8000
```

---

## 🧩 Example Output

```
🔍 Running initial CI/CD analysis...

🧾 AI Analysis:
Tests failed in stage 'Test'. Consider caching Docker layers and parallelizing test execution.
```

And in chat mode:

```
You: How can I reduce build time?
AI: Try enabling Docker layer caching and running 'pytest' tests in parallel using pytest-xdist.
```

---

## 📦 Folder Structure

```
.
├── langchain_agent/
│   ├── cicd_agent.py          # LangChain logic for analysis and chat
├── mcp_server.py              # FastAPI + FastMCP server
├── main.py                    # CLI interface and sample run
├── .env.example               # Example environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔐 Security Best Practices

* Never commit real API keys to GitHub — use `.env` and `.gitignore`.
* You can safely share `.env.example` for configuration guidance.
* GitHub push protection automatically blocks commits containing secrets.

---

## 🌟 Future Enhancements

* Integration with **real Jenkins REST APIs** for live log ingestion
* Add **Grafana dashboards** for build-time visualization
* Deployable as a **MCP microservice** in production pipelines

---

## 👤 Author

**Shreyansh Singh**
AI/ML & MLOps Developer
🔗 *Focused on scalable, intelligent, and automation-driven system design.*

---

