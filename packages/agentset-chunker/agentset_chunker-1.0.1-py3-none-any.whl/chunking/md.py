from langchain_core.documents import Document
from unstructured.chunking.title import chunk_by_title
from unstructured.chunking.basic import chunk_elements
from unstructured.partition.md import partition_md

from agentset_chunker.base import ChunkerOptions
from agentset_chunker._common import Strategy


def md(file_path:str, opt:ChunkerOptions)->list[Document] | None:
    """
    Processes a md file and chunks its content based on the provided options.

    Args:
        file_path (str): The path to the file to be processed.
        opt (ChunkerOptions): The options for chunking the file.

    Returns:
        list[Document] | None: A list of Document objects containing the chunked content, or None if no chunks are created.
    """
    elements = partition_md(filename=file_path)

    if opt.strategy == Strategy.BASIC:
        chunks = chunk_by_title(elements, max_characters=opt.max_characters, overlap=opt.overlap)
    elif opt.strategy == Strategy.BY_TITLE:
        chunks = chunk_elements(elements, max_characters=opt.max_characters, overlap=opt.overlap)
    else:
        chunks = None

    if chunks is None:
        return None

    return [Document(page_content=c.text, metadata=c.metadata.to_dict()) for c in chunks]
