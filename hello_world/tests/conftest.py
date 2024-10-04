"""
Fixtures to reuse.
"""

import sys

pytest_plugins = [
    # "tests.unit. ...
]

MIN_SIGNED_64_BIT = ~sys.maxsize  # -9223372036854775808
MAX_UNSIGNED_64_BIT = sys.maxsize  # 9223372036854775808
