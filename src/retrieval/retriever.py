from src.embeddings.embeddings import EmbeddingModel
from src.retrieval.vector_store import VectorStore


class Retriever:
    def __init__(
        self,
        embedding_model: EmbeddingModel,
        vector_store: VectorStore
    ):
        self.embedding_model = embedding_model
        self.vector_store = vector_store

    def retrieve(self, query: str, top_k: int = 4) -> list[dict]:
        if not query.strip():
            raise ValueError("Query cannot be empty")

        query_embedding = self.embedding_model.encode([query])[0]

        results = self.vector_store.search(
            query_embedding,
            top_k=top_k
        )

        return results
