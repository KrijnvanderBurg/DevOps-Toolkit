"""
Fixtures to reuse.
"""

import json
import tempfile
from collections.abc import Generator
from typing import Any

import pytest


@pytest.fixture
def temp_json_file() -> Generator[str, Any, None]:
    """
    Creates a temporary JSON file with predefined data and yields its file path.

    The function writes a dictionary `{"key": "value"}` to a temporary file with a `.json` suffix,
    yields the file path, and deletes the file after use.

    Yields:
        str: The path to the temporary JSON file.

    Cleanup:
        The temporary file is removed after the generator is exhausted.
    """
    data = {"key": "value"}
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".json", delete=False) as tmp:
        json.dump(data, tmp)
        tmp.flush()
        yield tmp.name
