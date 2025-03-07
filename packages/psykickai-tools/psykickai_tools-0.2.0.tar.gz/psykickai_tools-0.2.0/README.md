# psykickai-tools

A collection of reusable Python tools and utilities (logging, etc.) designed to streamline project setup and provide out-of-the-box functionality for common development needs.

![PyPI version](https://img.shields.io/pypi/v/psykickai-tools) ![Python versions](https://img.shields.io/pypi/pyversions/psykickai-tools) ![Build Status](https://img.shields.io/github/workflow/status/psykick-21/psykickai-tools/CI)

## Installation

You can install the package using pip:

```bash
pip install psykickai-tools
```

## Development Setup

To set up a development environment, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/psykick-21/psykickai-tools.git
   cd psykickai-tools
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the development dependencies:**
   ```bash
   pip install -e .[dev]
   ```

4. **Run tests to ensure everything is working:**
   ```bash
   pytest
   ```

## Available Functionalities

### Logger

The logger provides a pre-configured logging system with both console and file output. It offers:
- Console output for INFO level and above with a concise format showing time, level, and message
- Daily rotating file logs with detailed format including file path and line numbers
- Debug level logging in files for comprehensive debugging
- Automatic log directory creation

#### Example Usage

```python
from psykickai_tools.utils import logger

# Different logging levels
logger.debug("Detailed debug information")  # Only appears in log file
logger.info("General information")          # Appears in both console and file
logger.warning("Warning message")           # Appears in both console and file
logger.error("Error message")              # Appears in both console and file
logger.critical("Critical error")          # Appears in both console and file
```

Console output will show:
```
14:30:45 | INFO     | General information
14:30:45 | WARNING  | Warning message
```

Log file (`logs/app_YYYYMMDD.log`) will contain:
```
2024-01-27 14:30:45 | DEBUG    | /path/to/your/file.py:10 | Detailed debug information
2024-01-27 14:30:45 | INFO     | /path/to/your/file.py:11 | General information
2024-01-27 14:30:45 | WARNING  | /path/to/your/file.py:12 | Warning message
```

### IO Operations

The IO module provides safe and convenient file operations with proper error handling and logging. It includes functions for:
- Reading file content with UTF-8 encoding
- Writing content to files (with automatic directory creation)
- Appending content to files (with optional newline handling)

#### Example Usage

```python
from psykickai_tools.io import read_file_content, write_file_content, append_file_content

# Read content from a file
content = read_file_content("/path/to/file.txt")

# Write content to a file (creates directories if they don't exist)
write_file_content("/path/to/new/file.txt", "Hello, World!")

# Append content to a file
append_file_content("/path/to/file.txt", "New content", add_newline=True)
```

Key Features:
- Automatic directory creation for write and append operations
- UTF-8 encoding for all operations
- Comprehensive error handling with detailed error messages
- Integrated logging for debugging and monitoring
- Smart newline handling for append operations
- Type hints and complete documentation

Example Error Handling:
```python
try:
    content = read_file_content("/path/to/nonexistent/file.txt")
except FileNotFoundError:
    print("File does not exist")
except PermissionError:
    print("Permission denied")
except IOError as e:
    print(f"IO Error: {e}")
```

### Web Operations

The web module provides utilities for interacting with various web services and APIs. Currently, it includes:

#### Webpage Content Loader

The WebpageLoader class provides a robust way to load and parse content from web pages. It supports loading single or multiple URLs simultaneously, with metadata extraction and content parsing.

```python
from psykickai_tools.web import WebpageLoader

# Load a single webpage
loader = WebpageLoader("https://example.com")
loader.load()
documents = loader.get_documents()  # Get content as formatted strings
print(documents[0])  # Print the content of the webpage

# Load multiple webpages
urls = [
    "https://example.com/page1",
    "https://example.com/page2"
]
loader = WebpageLoader(urls)
loader.load()

# Get structured content with metadata
structured_docs = loader.get_documents(as_string=False)
for doc in structured_docs:
    print(f"Title: {doc.metadata.browser_title}")
    print(f"Language: {doc.metadata.language}")
    print(f"Content lines: {len(doc.content_lines)}")
```

Key Features:
- Load single or multiple webpages in sequence
- Extract metadata including title, language, section numbers, and meta tags
- Clean content extraction with automatic script and style removal
- Configurable parser type (HTML or XML)
- Comprehensive error handling for failed requests
- Detailed logging for debugging and monitoring
- Type hints and complete documentation

Example Error Handling:
```python
loader = WebpageLoader("https://nonexistent-site.com")
loader.load()
documents = loader.get_documents()
if documents and documents[0].startswith("Error:"):
    print("Failed to load webpage:", documents[0])
```

#### YouTube Transcript Extraction

Extract transcripts from YouTube videos with optional timestamp information.

```python
from psykickai_tools.web import fetch_transcript

# Get plain text transcript
url = "https://www.youtube.com/watch?v=your_video_id"
transcript = fetch_transcript(url)
print(transcript)  # Prints the full transcript as a single string

# Get transcript with timestamps
transcript_with_time = fetch_transcript(url, with_timestamp=True)
for segment in transcript_with_time:
    print(f"[{segment['start']}s] {segment['text']}")
```

Key Features:
- Extract transcripts from any YouTube video URL
- Option to get timestamps with transcript segments
- Comprehensive error handling for invalid URLs or unavailable transcripts
- Integrated logging for debugging and monitoring
- Type hints and complete documentation

Example Error Handling:
```python
try:
    transcript = fetch_transcript("https://www.youtube.com/watch?v=invalid_id")
except ValueError as e:
    print(f"Error: {e}")  # Will show detailed error message
```

Note: This functionality requires the `youtube-transcript-api` package, which is automatically installed with this library.

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.