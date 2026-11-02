import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": "Bearer " + os.getenv("GROQ_API_KEY"),
    "Content-Type": "application/json"
}
body = {
    "model": os.getenv("GROQ_MODEL", "llama3-8b-8192"),
    "messages": [{"role": "user", "content": "Explain APIs to a beginner."}]
}

# 1. Define 'r' by sending the request
r = requests.post(url, headers=headers, json=body)

# 2. Fix: Added parentheses () to r.json()
data = r.json()

answer = data["choices"][0]["message"]["content"]
print(answer)

tokens = data["usage"]["total_tokens"]
print(tokens)
