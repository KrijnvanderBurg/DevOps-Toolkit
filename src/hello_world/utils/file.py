"""
Utility functions for file operations.

This module provides functions to create and manipulate files.
"""

from pathlib import Path


def create_file(file_path: Path, content: str) -> None:
    """
    Creates a file at the given Path and writes the provided content to it,
    only if the file does not already exist.

    Args:
        file_path (Path): The Path of the file to create.
        content (str): The content to write into the file.
    """

    if file_path.exists():
        print("File already exists.")
    else:
        with file_path.open("w", encoding="utf-8") as f:
            f.write(content)
