from src.embeddings.embeddings import EmbeddingModel


def test_embedding_generation():
    model = EmbeddingModel()

    texts = [
        "Modern Physics",
        "Introduction to Modern Physics"
    ]

    vectors = model.encode(texts)

    assert vectors.shape == (2, 384)
    assert vectors.dtype == "float32"


def test_similar_texts():
    model = EmbeddingModel()

    vectors = model.encode([
        "Modern Physics",
        "Introduction to Modern Physics"
    ])

    similarity = float(vectors[0] @ vectors[1])

    assert similarity > 0.5
