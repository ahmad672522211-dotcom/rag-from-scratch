from src.ingestion.text_cleaner import clean_text


def test_clean_text():
    raw_text = "Modern    Physics\n\n\nUNIT-01"

    cleaned = clean_text(raw_text)

    assert "Modern Physics" in cleaned
    assert "\n\n\n" not in cleaned
    assert cleaned == cleaned.strip()
