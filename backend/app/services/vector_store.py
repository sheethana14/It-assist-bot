import os
import faiss
import numpy as np
import pickle
from typing import List

# Define paths for the FAISS index and metadata store
INDEX_PATH = "vector_store/faiss.index"
METADATA_PATH = "vector_store/metadata.pkl"

# Embedding dimension for the SentenceTransformer model (all-MiniLM-L6-V2)
EMBEDDING_DIMENSION = 384

# Initialize or load the FAISS index and metadata store
if os.path.exists(INDEX_PATH) and os.path.exists(METADATA_PATH):
    index = faiss.read_index(INDEX_PATH)
    with open(METADATA_PATH, "rb") as f:
        metadata_store = pickle.load(f)
else:
    index = faiss.IndexFlatL2(EMBEDDING_DIMENSION)
    metadata_store = []


def add_to_index(embeddings,chunks,filename):

    """Add embeddings and their corresponding text chunks to the FAISS index.

    Args:
        embeddings: List of embedding vectors (each a list of floats).
        chunks: List of text chunks that correspond to the embeddings.
        filename: Source filename for the chunks (used for metadata).
    """
    global metadata_store, index
    vectors = np.array(embeddings).astype("float32")
    index.add(vectors)

    for chunk in chunks:
        metadata_store.append({"text": chunk, "source": filename})

    os.makedirs(os.path.dirname(INDEX_PATH),exist_ok=True)

    faiss.write_index(index, INDEX_PATH)
    with open(METADATA_PATH, "wb") as f:
        pickle.dump(metadata_store, f)


def search_index(query_embedding: List[float], top_k: int = 3) -> List[str]:
    """Search the FAISS index for the most similar chunks.

    Args:
        query_embedding: Embedding vector for the query.
        top_k: Number of top results to return.

    Returns:
        List of text chunks that are most similar to the query.
    """
    query_vector = np.array([query_embedding]).astype("float32")
    distances, indices = index.search(query_vector, top_k)
    results = []
    for idx in indices[0]:
        if idx < len(metadata_store):
            results.append(metadata_store[idx]["text"])
    return results