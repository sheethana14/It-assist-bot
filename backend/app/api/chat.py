from fastapi import APIRouter, HTTPException 
from httpx import request
from pydantic import BaseModel

from app.services.embeddings import generate_embeddings
from app.services.vector_store import search_index

router = APIRouter()

class ChatRequest(BaseModel):
    question: str
    top_k : int = 5

class ChatResponse(BaseModel):
    question: str
    retrieved_chunks: list[str]

@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    """
    Accept a user question, genrate embedding for the question,
    performs a simmilarity search,
    returns the most relevant chunks.
"""
    if not request.question.strip():
       raise HTTPException(status_code=400, detail="question cannot be empty")


    query_embedding =generate_embeddings([request.question])[0]

    results = search_index(query_embedding, top_k=request.top_k)
    return ChatResponse(
        question=request.question,
        retrieved_chunks=results
)