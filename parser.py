# parser.py

import fitz  # PyMuPDF
from typing import List


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract all text from a PDF file using PyMuPDF (fitz).
    """
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """
    Split text into overlapping chunks for embedding.

    chunk_size: number of characters per chunk
    overlap: number of characters to overlap between chunks
    """
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap  # slight overlap to preserve context
    return chunks


if __name__ == "__main__":
    from pathlib import Path

    sample_pdf = Path("data/uploads/sample.pdf")  # make sure the PDF exists
    if sample_pdf.exists():
        raw_text = extract_text_from_pdf(str(sample_pdf))
        print(f"✅ Extracted {len(raw_text)} characters from {sample_pdf.name}")

        chunks = chunk_text(raw_text)
        print(f"📚 Split into {len(chunks)} chunks (preview below):\n")
        print(chunks[0])
    else:
        print("⚠️ sample.pdf not found in data/uploads/")
