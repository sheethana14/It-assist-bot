from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_answer(question: str, context_chunks: list[str]) -> str:
    """
    Generate an answer useing retrieved context.
    
    """
    context_text = "\n\n".join(context_chunks)
    prompt = f"""
You are an internal IT assistant.

Answer the question ONLY using the provided context.
If the answer is not found in the context, say:
"I could not find this information in the provided documents.


context : {context_text}

question : {question}

Answer :
"""
    response = client.chat.completions.create(
        model="gbt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful IT Assistant"},
            {"role": "user", "content" : prompt}
        ],
        temperature= 0
    )

    return response.choices[0].message.content.strip()