from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

from app.services.embeddings import generate_embeddings
from app.services.vector_store import search_index
from app.services.llm import generate_answer

router = APIRouter()


class ChatRequest(BaseModel):
    question: str
    # top_k: int = 3
    # history: List[dict] = []


class ChatResponse(BaseModel):
    question: str
    answer: str


@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    """ 
    Handle chat requests and generate responses based on uploaded documents.
    """
    try:
        if not request.question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty")

        query_embedding = generate_embeddings([request.question])
        query_embedding = query_embedding[0]

        retrieved_chunks = search_index(query_embedding, top_k=3)       
       
        if not retrieved_chunks:
            return {
                "response": "No relevant Information found in the iploaded documnets.",
                "context": []      
            }

        return {
            "response": "here is the answer to your question based on the uploaded the documents.",
            "context": retrieved_chunks
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the chat request: {str(e)}")