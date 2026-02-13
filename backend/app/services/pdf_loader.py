from pypdf import PdfReader

def extract_text_from_pdf(file_path: str) -> str:
    """
    Extracts text from a pdf file.
    Returns the extracted text as a string.

    """
    reader = PdfReader(file_path)
    text_content = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            text_content.append(text.strip())
    return "\n".join(text_content)
