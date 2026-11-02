import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": "Bearer " + os.getenv("GROQ_API_KEY"),
    "Content-Type": "application/json"}
body = {"model": os.getenv("GROQ_MODEL"),
        "messages": [{"role": "user",
                      "content": "Explain APIs to a beginner."}]}
r = requests.post(url, headers=headers, json=body)
print(r.status_code)
