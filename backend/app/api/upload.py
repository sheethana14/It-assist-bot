from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import shutil
import uuid 

from app.services.pdf_loader import extract_text_from_pdf
from app.services.chunker import chunk_text

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile =File(...)):

    if  file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="only PDF file are allowed")
    
    unique_id = uuid.uuid4()
    file_extension = os.path.splitext(file.filename)[1]
    unique_filename = f"{unique_id}{file_extension}"

    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail="File upload failed")
    

    try:
        extract_text = extract_text_from_pdf(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"failed to extract: {str(e)}")
    
    chunks = chunk_text(extract_text)

    return{
        "message": "PDF file uploaded sucessfully",
        "filename": unique_filename,
        "text_preview": extract_text[:500],
        "total_chunks": len(chunks),
        "sample_chunk": chunks[0] if chunks else "No content"
    }
    
    

