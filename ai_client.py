#uses config.API_KEY and config.MODEL_NAME to make requests to the AI model and get responses back.
'''import config
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()                              # 1. load .env file
api_key = os.getenv("GEMINI_API_KEY")     # 2. get the key
genai.configure(api_key=api_key)          # 3. now configure
model = genai.GenerativeModel("gemini-1.5-flash")  # 4. create model

history = [{"role": "system", "content": config.SYSTEM_PROMPT}]


def askai(user_input):
    history.append({"role": "user", "content": user_input})
    response = model.generate_content(
    [msg["content"] for msg in history],
    generation_config={"max_output_tokens": config.MAX_TOKENS})
    response_text = response.text
    history.append({"role": "assistant", "content": response_text})
    return response_text
'''
# ai_client.py - Handles all communication with the Groq AI

from groq import Groq
from dotenv import load_dotenv
#from google import genai
import os
import config

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
#client = genai.Client(api_key=api_key)
client = Groq(api_key=api_key)

history = [
    {"role": "system", "content": config.SYSTEM_PROMPT},
    {"role": "assistant", "content": "Understood. I am JARVIS."}
]

def askai(user_input):
    history.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=history,
    max_tokens=config.MAX_TOKENS)
    
    response_text = response.choices[0].message.content
    history.append({"role": "assistant", "content": response_text})
    return response_text