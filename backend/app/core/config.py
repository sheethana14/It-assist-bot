import os
from dotenv import load_dotenv

load_dotenv()

class Setting:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")

settings = Setting()