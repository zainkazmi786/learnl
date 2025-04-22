import requests
import os
from dotenv import load_dotenv
import json

# Load environment variables from .env
load_dotenv()

# Set these manually or pull from environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama3-8b-8192"  # or "mixtral-8x7b-32768", etc.

# Simple test message
messages = [
    {"role": "user", "content": "What is the command to list all files including hidden ones in Linux?"}
]

# Check key and model
if not GROQ_API_KEY:
    print("❌ GROQ_API_KEY is not set in your .env file.")
    exit(1)

if not GROQ_MODEL:
    print("❌ GROQ_MODEL is not defined.")
    exit(1)

# Prepare request
headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": GROQ_MODEL,
    "messages": messages,
    "temperature": 0.2
}

print("🔍 Testing Groq API request...\n")
print("➡️ Request Payload:")
print(json.dumps(payload, indent=2))

try:
    response = requests.post(GROQ_API_URL, headers=headers, json=payload)
    print(f"\n⬅️ Status Code: {response.status_code}")

    try:
        response_json = response.json()
        print("📦 Response JSON:")
        print(json.dumps(response_json, indent=2))

        if response.status_code == 200:
            content = response_json['choices'][0]['message']['content']
            print("\n✅ Extracted LLM Response:")
            print(content)
        else:
            print("❌ API returned an error:")
            print(response_json)

    except ValueError:
        print("❌ Failed to decode JSON:")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"❌ Request failed: {e}")
