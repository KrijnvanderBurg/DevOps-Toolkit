import pytest
import json
import tempfile
import os

"""
Fixtures to reuse.
"""

@pytest.fixture
def temp_json_file():
    data = {"key": "value"}
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.json', delete=False) as tmp:
        json.dump(data, tmp)
        tmp.flush()
        yield tmp.name
    os.remove(tmp.name)