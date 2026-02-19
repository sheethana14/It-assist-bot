from sentence_transformers import SentenceTransformer
from typing import List

model = SentenceTransformer ("all-MiniLM-L6-V2")

def generate_embeddings(text_chunks: List[str]) -> List[List[float]]:
    """
   convert test chunks into vector embedding.
   :param text_chunks: List of text chunks
    :return: List of embedding vectors

    """
    embeddings = model.encode(text_chunks, 
    convert_to_numpy= True
    )
    return embeddings.tolist()