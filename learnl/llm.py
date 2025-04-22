import requests
import os
import json
from dotenv import load_dotenv

# Load .env for GROQ_API_KEY
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama3-8b-8192"

def ask_llm(history, question):
    if not GROQ_API_KEY:
        return "❌ GROQ API key not found."

    if not GROQ_MODEL:
        return "❌ Model not set."

    prompt = build_prompt(history, question)

    if not prompt or not prompt.strip():
        return "❌ Prompt is empty."

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": GROQ_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return extract_commands(response.json())

    except requests.exceptions.RequestException:
        return "❌ API request failed."
    except Exception:
        return "❌ Unexpected error."

def build_prompt(history, question):
    history_str = "\n".join(history[-10:]).strip()
    if not history_str and not question.strip():
        return ""
    return f"""
You are a Linux shell assistant.

The user recently ran these commands:
{history_str}

Now they asked:
{question}

Reply ONLY with the correct Linux shell command(s) to solve the problem.
Do NOT include any explanations, descriptions, or extra text.
""".strip()

def extract_commands(response_json):
    try:
        content = response_json['choices'][0]['message']['content']
        lines = [line.strip() for line in content.splitlines() if line.strip()]
        return "\n".join(lines)
    except (KeyError, IndexError, TypeError):
        return "❌ Failed to parse response."
