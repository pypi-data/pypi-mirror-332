"""File operations module for AI agents.

This module provides core file operation functionalities that can be used by AI agents
for reading, writing, and appending content to files.

Can also be used as a standalone module for file operations.
"""

import os
from pathlib import Path
from typing import Union, Optional
from ..utils import logger

def read_file_content(file_path: Union[str, Path]) -> str:
    """Read content from a file.
    
    Args:
        file_path: Complete path to the file (including filename and extension)
        
    Returns:
        The content of the file as a string
        
    Raises:
        FileNotFoundError: If the file does not exist
        PermissionError: If the program lacks permission to read the file
        IOError: If there's an error reading the file
    """
    try:
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        logger.debug(f"Reading content from file: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        logger.debug(f"Successfully read {len(content)} characters from {file_path}")
        return content
    
    except PermissionError as e:
        logger.error(f"Permission denied while reading file: {file_path}")
        raise
    except IOError as e:
        logger.error(f"IO error while reading file {file_path}: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error while reading file {file_path}: {str(e)}")
        raise

def write_file_content(
    file_path: Union[str, Path],
    content: str,
    create_dirs: bool = True
) -> None:
    """Write content to a file, overwriting any existing content.
    
    Args:
        file_path: Complete path to the file (including filename and extension)
        content: Content to write to the file
        create_dirs: If True, create parent directories if they don't exist
        
    Raises:
        PermissionError: If the program lacks permission to write to the file
        IOError: If there's an error writing to the file
    """
    try:
        file_path = Path(file_path)
        if create_dirs:
            file_path.parent.mkdir(parents=True, exist_ok=True)
        
        logger.debug(f"Writing content to file: {file_path}")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        logger.debug(f"Successfully wrote {len(content)} characters to {file_path}")
    
    except PermissionError as e:
        logger.error(f"Permission denied while writing to file: {file_path}")
        raise
    except IOError as e:
        logger.error(f"IO error while writing to file {file_path}: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error while writing to file {file_path}: {str(e)}")
        raise

def append_file_content(
    file_path: Union[str, Path],
    content: str,
    create_dirs: bool = True,
    add_newline: bool = True
) -> None:
    """Append content to a file.
    
    Args:
        file_path: Complete path to the file (including filename and extension)
        content: Content to append to the file
        create_dirs: If True, create parent directories if they don't exist
        add_newline: If True, add a newline before appending the content if the file
                    doesn't end with one
        
    Raises:
        PermissionError: If the program lacks permission to write to the file
        IOError: If there's an error writing to the file
    """
    try:
        file_path = Path(file_path)
        if create_dirs:
            file_path.parent.mkdir(parents=True, exist_ok=True)
        
        logger.debug(f"Appending content to file: {file_path}")
        
        # Check if we need to add a newline
        needs_newline = False
        if add_newline and file_path.exists() and file_path.stat().st_size > 0:
            with open(file_path, 'r', encoding='utf-8') as file:
                file.seek(max(0, file.seek(0, 2) - 1))
                last_char = file.read(1)
                needs_newline = last_char != '\n'
        
        with open(file_path, 'a', encoding='utf-8') as file:
            if needs_newline:
                file.write('\n')
            file.write(content)
        
        logger.debug(f"Successfully appended {len(content)} characters to {file_path}")
    
    except PermissionError as e:
        logger.error(f"Permission denied while appending to file: {file_path}")
        raise
    except IOError as e:
        logger.error(f"IO error while appending to file {file_path}: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error while appending to file {file_path}: {str(e)}")
        raise 