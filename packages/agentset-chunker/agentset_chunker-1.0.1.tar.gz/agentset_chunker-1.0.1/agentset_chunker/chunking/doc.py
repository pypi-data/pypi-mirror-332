from langchain_core.documents import Document

from unstructured.chunking.title import chunk_by_title
from unstructured.chunking.basic import chunk_elements
from unstructured.partition.doc import partition_doc
from unstructured.partition.utils.constants import PartitionStrategy

from agentset_chunker.base import ChunkerOptions
from agentset_chunker._common import Strategy


def doc(file_path:str, opt:ChunkerOptions)->list[Document] | None:
    """
    Processes a DOC file and chunks its content based on the provided options.

    Args:
        file_path (str): The path to the file to be processed.
        opt (ChunkerOptions): The options for chunking the file.

    Returns:
        list[Document] | None: A list of Document objects containing the chunked content, or None if no chunks are created.
    """

    partition_strategy = PartitionStrategy.OCR_ONLY if opt.force_ocr else  PartitionStrategy.AUTO
    elements = partition_doc(filename=file_path, strategy=partition_strategy)

    if opt.strategy == Strategy.BASIC:
        chunks = chunk_by_title(elements, max_characters=opt.max_characters, overlap=opt.overlap)
    elif opt.strategy == Strategy.BY_TITLE:
        chunks = chunk_elements(elements, max_characters=opt.max_characters, overlap=opt.overlap)
    else:
        chunks = None

    if chunks is None:
        return None

    return [Document(page_content=c.text, metadata=c.metadata.to_dict()) for c in chunks]
