import faiss
import numpy as np
from typing import List

EMBEDDING_DIMENTION = 384

index = faiss.IndexFlatL2(EMBEDDING_DIMENTION)

stored_chunks = []

def add_to_index(embedding:List[List[float]], chunks: List[str]):
    """
    Add embeddings and corrsponding chunks to faiss index.
    """
    vectors = np.array(embedding).astype("float32")
    index.add(vectors)
    stored_chunks.extend(chunks)

def search_index(query_embedding: List[float], top_k: int=3):
    """
    Search FAISS index and return top_k relevant chunks.
    """
    query_vector = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_vector, top_k)

    results =[]
    for idx in indices[0]:
        if idx < len(stored_chunks):
            results.append(stored_chunks[idx])
    return results
