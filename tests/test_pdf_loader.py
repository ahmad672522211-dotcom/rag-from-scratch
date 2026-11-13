from src.ingestion.pdf_loader import load_pdf


def test_load_pdf():
    pages = load_pdf("data/sample.pdf")

    assert len(pages) > 0
    assert "text" in pages[0]
    assert "page" in pages[0]
    assert isinstance(pages[0]["text"], str)
