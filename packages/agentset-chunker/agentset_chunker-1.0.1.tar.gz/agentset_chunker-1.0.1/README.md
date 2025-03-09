# Agentset Chunker: Document Chunking and Processing


Agentset Chunker is a versatile tool designed to process and chunk various types of documents, making it easier to manage, analyze, and utilize their content. This repository is created for Retrieval-Augmented Generation (RAG) systems, allowing you to chunk your files efficiently for RAG systems. It supports a wide range of document formats, including text files, PDFs, DOCX files, HTML, and more. The core functionality of this project is to break down documents into smaller, manageable chunks, which can then be used for tasks like information retrieval, summarization, and data extraction.

## Key Features

*   **Document Chunking:** Breaks down documents into smaller, meaningful chunks based on configurable strategies.
*   **Multi-Format Support:** Handles a variety of document types, including:
    *   **Text:** TXT, Markdown (MD), JSON
    *   **Office:** PDF, DOCX, DOC
    *   **Web:** HTML, HTM
*   **URL Handling:** Can process documents directly from URLs.
*   **Configurable Chunking:** Offers flexible chunking strategies (e.g., by title, basic) with adjustable chunk size and overlap.
*   **Extensible:** Designed for future expansion to include more file types and processing techniques.

## How It Works

The Agentset Chunker project operates through the following key components:

1. **Chunker Function (`chunker.py`):**
    *   The core of the system, responsible for parsing and chunking documents.
    *   It determines the file type based on its extension or URL.
    *   It dispatches the document to the appropriate chunk (e.g., PDF chunk, DOCX chunk).
    *   It applies the selected chunking strategy and options.
    *   **Strategies:**
        *   `Strategy.BY_TITLE`: Chunks based on titles or headings in the document (if available).
        *   `Strategy.BASIC`: Chunks based on a simple character count with overlap.
    *   **Options:**
        *   `ocr_force`: Option for using OCR (Optical Character Recognition).
        *   `max_characters`: Maximum number of characters per chunk.
        *   `overlap`: Number of characters overlapping between chunks.

2. **Chunking Modules (`chunking/`)**
    *  There are separate modules for each file type:
        * `pdf.py` : Chunks PDF files.
        * `docx.py`: Chunks DOCX files.
        * `doc.py`: Chunks DOC files.
        * `txt.py`: Chunks TXT files.
        * `md.py`: Chunks MD files.
        * `json.py`: Chunks JSON files.
        * `html.py`: Chunks HTML and HTM files.
    *   Each module handles the specific parsing and chunking logic for its file type.

3. **Connector (`connector/`)**
    *   Handles downloading files from URLs to temporary local storage.
    *   Manages any necessary HTTP requests.

4. **Document Representation (`langchain-core/documents/base.py`):**
    *   Uses the `langchain_core.documents.Document` class to represent each chunk.
    *   Each `Document` has `page_content` (the text of the chunk) and `metadata` (additional information).


## Getting Started

### Prerequisites

Before you can use Agentset Chunker, you need to have the following installed:

*   **Python:** 3.12 or higher.
*   **pip:** Python package manager.
*   **System Dependencies:**
    *   **[Poppler](https://poppler.freedesktop.org/):** For PDF processing.
    *   **[LibreOffice](https://www.libreoffice.org/discover/libreoffice/):** For DOC and DOCX processing.
    *   **[Pandoc](https://pandoc.org/):** For markdown processing.
    *   **[Tesseract OCR](https://github.com/tesseract-ocr/tesseract):** For Optical Character Recognition (OCR).
        *   Note: Installation instructions for these dependencies vary by operating system. Please refer to the individual project's documentation for guidance.
* **python dependencies**:
    * run `uv pip install -r pyproject.toml`

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/agentset-ai/agentset-chunker.git
    cd agentset-chunker
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Linux/macOS
    .venv\Scripts\activate  # On Windows
    ```

3.  **Install Dependencies:**
    ```bash
    pip install .
    ```
    If you use `uv` you can run : `uv pip install .`.

### Usage

### Example
```python
import json

from agentset_chunker import chunker, Strategy

with open('./chunked.json', 'w') as file:
    res = chunker(
        "https://site.com/example.pdf",
        strategy=Strategy.BY_TITLE)
    file.write(json.dumps([c.__dict__ for c in res]))
```

## File Types

### Supported File Types

*   **HTML:** `htm`, `html`
*   **Text:** `pdf`, `docx`, `doc`, `text`, `md`, `json`

### Planned Support

*   **Image Types**
*   **Video Types**

## To-Do

- [ ] Add Image support
- [ ] Add video support
- [ ] Expand Chunking Strategies: Implement more advanced chunking strategies (e.g., semantic chunking).
- [ ] Improve Error Handling: Add more specific error handling for different types of issues.
- [ ] Add tests: write unit test for the code.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
