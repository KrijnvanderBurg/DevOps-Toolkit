"""
Unit tests for file utility functions.
"""

import tempfile
from pathlib import Path

from hello_world.utils.file import create_file


def test_create_file() -> None:
    """
    Test create_file utility.
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file_path = Path(temp_dir) / "test_file.txt"
        test_content = "Hello, World!"

        # Test creating a new file
        create_file(test_file_path, test_content)

        # Verify the file was created
        assert test_file_path.exists()

        # Verify the content is correct
        with test_file_path.open("r", encoding="utf-8") as f:
            assert f.read() == test_content
