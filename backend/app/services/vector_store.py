import os
import faiss
import numpy as np
from typing import List
import pickle

index_PATH = "vector_store/faisss.index"
METADATA_PATH ="vector_store/metadata.pkl"

EMBEDDING_DIMENTION = 1538

index = faiss.IndexFlatL2(EMBEDDING_DIMENTION)

stored_chunks = []

if os.path.exists(index_PATH):
    index =faiss.read_index(index_PATH)
    with open(METADATA_PATH,"rb") as f:
        metadata_store = pickle.load(f)

else:
    index = faiss.IndexFlatL2(EMBEDDING_DIMENTION)
    metadata_store = []

def add_to_index(embedding, chunks, filename):
    global metadata_store

    vectors = np.array(embedding).astype('float32')
    index.add(vectors)

    for chunk in chunks:
        metadata_store.append({
            "text": chunk,
            "source": filename
        })

    faiss.write_index(index, index_PATH)
    with open(METADATA_PATH, "wb") as f:
        pickle.dump(metadata_store, f)

def search_index(query_embedding, top_k=3):
    query_vector = np.array(query_embedding).astype('float32')
    distances, indices =index.search(query_vector,top_k)

    results = []
    for idex in indices[0]:
        if idex < len(metadata_store):
            results.append(metadata_store[idex]["text"])
        return results