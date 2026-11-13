import faiss
import numpy as np


class VectorStore:
    def __init__(self, dimension: int):
        if dimension <= 0:
            raise ValueError("Dimension must be positive")

        self.dimension = dimension
        self.index = faiss.IndexFlatIP(dimension)
        self.chunks = []

    def add(self, embeddings: np.ndarray, chunks: list[dict]) -> None:
        embeddings = np.asarray(embeddings, dtype="float32")

        if embeddings.ndim != 2:
            raise ValueError("Embeddings must be a 2D array")

        if embeddings.shape[1] != self.dimension:
            raise ValueError("Embedding dimension mismatch")

        if len(embeddings) != len(chunks):
            raise ValueError("Embeddings and chunks count must match")

        if len(embeddings) == 0:
            return

        self.index.add(embeddings)
        self.chunks.extend(chunks)

    def search(
        self,
        query_embedding: np.ndarray,
        top_k: int = 4
    ) -> list[dict]:

        if top_k <= 0:
            raise ValueError("top_k must be positive")

        if self.index.ntotal == 0:
            return []

        query_embedding = np.asarray(
            query_embedding,
            dtype="float32"
        ).reshape(1, -1)

        if query_embedding.shape[1] != self.dimension:
            raise ValueError("Query embedding dimension mismatch")

        scores, indices = self.index.search(
            query_embedding,
            min(top_k, self.index.ntotal)
        )

        results = []

        for score, index in zip(scores[0], indices[0]):
            if index == -1:
                continue

            result = self.chunks[int(index)].copy()
            result["score"] = float(score)
            results.append(result)

        return results
