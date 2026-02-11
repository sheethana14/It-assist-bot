from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import shutil
import uuid 

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile =File(...)):

    if  file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="only PDF file are allowed")
    
    file_extension = os.path.splitext(file.filename)[1]
    if file_extension.lower() != ".pdf":
        raise HTTPException(status_code=400, detail="Invalid file extension")
    
    unique_filename = f"{uuid.uuid4()}{file_extension}"
    file_path =os.path.join(UPLOAD_DIR, unique_filename)

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail="File upload failed")
    
    return{
        "message": "PDF file uploaded sucessfully",
        "file_path":file.filename,
        "saved_as": unique_filename
    }

