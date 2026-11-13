import re


def clean_text(text: str) -> str:
    """
    Clean extracted PDF text.
    """

    text = text.replace("\u00a0", " ")

    text = re.sub(r"[ \t]+", " ", text)

    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()
