from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(
        text: str,
        chunk_size: int=800,
        chunk_overlap: int=100
):
    """
    Splits text into smaller chunks useing chunks.

    :param text: Raw extracted text from the PDF
    :param chunk_size: Max Characters per chunk
    :param chunk_overlap: Overlapping characters between chunks
    :return: List of text chunks
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = splitter.split_text(text)
    return chunks
