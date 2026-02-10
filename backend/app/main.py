from fastapi import FastAPI

app = FastAPI(title = " IT Assist Bot ")

@app.get("/")
def read_root():
    return {" message": " Welcome to IT Assist Bot!"}
