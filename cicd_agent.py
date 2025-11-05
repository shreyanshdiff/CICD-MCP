import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

# 🧩 Load environment variables from .env file
load_dotenv()

# ✅ Ensure GROQ_API_KEY is present
if not os.getenv("GROQ_API_KEY"):
    raise ValueError("❌ Missing GROQ_API_KEY! Please add it to your .env file.")

# 🧠 Base prompt template
prompt_template = """
You are an AI DevOps optimization assistant.
You analyze Jenkins logs and pipeline configurations to find bottlenecks,
failures, and optimization opportunities like caching, parallelization, or build order.

Jenkins Logs:
{logs}

Pipeline Config:
{pipeline}

{chat_history}

User Question:
{user_input}

Your helpful and detailed response:
"""

def create_agent():
    """Creates a conversational DevOps optimization agent using Groq."""
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",  # ✅ Updated model, available in Groq
        temperature=0.2
    )

    # 🧠 Memory for conversation
    memory = ConversationBufferMemory(
        memory_key="chat_history", input_key="user_input"
    )

    # Prompt template
    prompt = PromptTemplate(
        input_variables=["logs", "pipeline", "user_input", "chat_history"],
        template=prompt_template
    )

    # LLM Chain setup
    chain = LLMChain(llm=llm, prompt=prompt, memory=memory, verbose=False)
    return chain


def analyze_ci_cd(logs, pipeline):
    """Run a one-shot analysis without chat."""
    chain = create_agent()
    return chain.run(logs=logs, pipeline=pipeline, user_input="Give me an overall analysis.")


def interactive_chat(logs, pipeline):
    """Start a conversational CLI chat session with the DevOps assistant."""
    chain = create_agent()
    print("\n You can now chat with the AI about your Jenkins logs and pipeline.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "q"]:
            print(" Goodbye!")
            break

        response = chain.run(logs=logs, pipeline=pipeline, user_input=user_input)
        print(f"\n AI: {response}\n")
