from fastapi import FastAPI
from app.api.upload import router as upload_router
from app.api.chat import router as chat_router


from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title = " IT Assist Bot ")


app.add_middleware(CORSMiddleware,
                   allow_origins=["http://localhost:5173","http://localhost:3000", "*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                )

app.include_router(upload_router,prefix="/api",tags=["Upload"]
)
app.include_router(chat_router,prefix="/api", tags=["Chat"])


@app.get("/")
def read_root():
    return {" message": " Welcome to IT Assist Bot!"}
