from src.ingestion.chunker import create_chunks


def test_create_chunks():
    pages = [
        {
            "page": 1,
            "text": " ".join([f"word{i}" for i in range(450)])
        }
    ]

    chunks = create_chunks(pages, chunk_size=200, overlap=30)

    assert len(chunks) == 3
    assert chunks[0]["page"] == 1
    assert len(chunks[0]["text"].split()) == 200
    assert len(chunks[1]["text"].split()) == 200
    assert len(chunks[2]["text"].split()) == 110


def test_invalid_chunk_size():
    pages = [{"page": 1, "text": "Hello world"}]

    try:
        create_chunks(pages, chunk_size=0)
        assert False
    except ValueError:
        assert True
