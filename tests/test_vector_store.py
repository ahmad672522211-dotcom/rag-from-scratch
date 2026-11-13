import numpy as np
from src.retrieval.vector_store import VectorStore


def test_vector_store_add_and_search():
    store = VectorStore(dimension=3)

    embeddings = np.array([
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.9, 0.1, 0.0]
    ], dtype="float32")

    chunks = [
        {"page": 1, "text": "Physics"},
        {"page": 2, "text": "Chemistry"},
        {"page": 3, "text": "Modern Physics"}
    ]

    store.add(embeddings, chunks)

    results = store.search(
        np.array([1.0, 0.0, 0.0], dtype="float32"),
        top_k=2
    )

    assert len(results) == 2
    assert results[0]["text"] == "Physics"
    assert results[0]["score"] > 0.9


def test_empty_vector_store():
    store = VectorStore(dimension=3)

    results = store.search(
        np.array([1.0, 0.0, 0.0], dtype="float32")
    )

    assert results == []
