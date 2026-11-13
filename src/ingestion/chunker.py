def create_chunks(
    pages: list[dict],
    chunk_size: int = 200,
    overlap: int = 30
) -> list[dict]:
    """
    Divide page text into smaller overlapping chunks.
    """

    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be non-negative and smaller than chunk_size")

    chunks = []

    for page_data in pages:
        words = page_data["text"].split()
        start = 0

        while start < len(words):
            end = start + chunk_size
            chunk_words = words[start:end]

            chunks.append({
                "page": page_data["page"],
                "text": " ".join(chunk_words)
            })

            start += chunk_size - overlap

    return chunks
