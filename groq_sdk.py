# pip install groq
import os
from dotenv import load_dotenv
from groq import Groq
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
response = client.chat.completions.create(
    model=os.getenv("GROQ_MODEL"),
    messages=[{"role": "user", "content": "Explain APIs to a beginner."}])
print(response.choices[0].message.content)