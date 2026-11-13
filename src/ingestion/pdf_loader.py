
import pymupdf
from pathlib import Path


def load_pdf(file_path: str) -> list[dict]:
    """
    Extract text from a PDF file page by page.

    Args:
        file_path: Path to the PDF document.

    Returns:
        A list of dictionaries containing page number and text.
    """

    pdf_path = Path(file_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {file_path}")

    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError("File must be a PDF.")

    extracted_pages = []

    with pymupdf.open(pdf_path) as document:

        for page_number, page in enumerate(document, start=1):

            text = page.get_text("text").strip()

            if text:
                extracted_pages.append({
                    "page": page_number,
                    "text": text
                })

    return extracted_pages
