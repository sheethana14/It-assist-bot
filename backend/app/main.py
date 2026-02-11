from fastapi import FastAPI
from app.api.upload import router as upload_router

app = FastAPI(title = " IT Assist Bot ")

app.include_router(
    upload_router,
    prefix="/api",
    tags=["Upload"]
)

@app.get("/")
def read_root():
    return {" message": " Welcome to IT Assist Bot!"}
