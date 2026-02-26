from urllib import response

from openai import BaseModel, OpenAI
from prompt_toolkit import prompt
from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

class ChatRequest(BaseModel):
    question: str
    top_k: int = 3
    history: list = []

def generate_answer(question, context_chunks, history=None) :
   history_text =""
   if history:
       for h in history:
          history_text += f"User: {h['question']}\nAssistant: {h['answer']}\n"

       context_text = "\n\n".join(context_chunks)
   
   prompt = f"""
You are an internal IT assistant.

Conversation History:
{history_text}

Context:
{context_text}

Current Question:
{question}

Answer clearly and based only on context.
"""

   response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
   return response.choices[0].message.content.strip()