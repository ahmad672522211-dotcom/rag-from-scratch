import numpy as np
from src.retrieval.retriever import Retriever


class FakeEmbeddingModel:
    def encode(self, texts):
        return np.array([[1.0, 0.0, 0.0]], dtype="float32")


class FakeVectorStore:
    def search(self, query_embedding, top_k=4):
        return [
            {"page": 1, "text": "Modern Physics", "score": 0.95}
        ]


def test_retriever_returns_relevant_chunks():
    retriever = Retriever(
        embedding_model=FakeEmbeddingModel(),
        vector_store=FakeVectorStore()
    )

    results = retriever.retrieve("What is Modern Physics?")

    assert len(results) == 1
    assert results[0]["text"] == "Modern Physics"
    assert results[0]["page"] == 1


def test_empty_query():
    retriever = Retriever(
        embedding_model=FakeEmbeddingModel(),
        vector_store=FakeVectorStore()
    )

    try:
        retriever.retrieve("   ")
        assert False
    except ValueError:
        assert True
