"""Read the API document's ``info.version`` for scripts/generate.sh.

Kept out of generate.sh so it can be unit-tested. The version is read from the
document text with a line regex rather than a YAML parser to avoid a parser
dependency in the generate step; because the spec is written by a YAML dumper,
a bare-numeric or date-like version comes through quoted (``'1.0'``), so the
surrounding quotes are stripped to record the value itself.
"""

from __future__ import annotations

import re
import sys


def read_api_version(spec_text: str) -> str:
    """Return ``info.version`` from an OpenAPI document's text, unquoted."""
    match = re.search(r"^  version: (.+)$", spec_text, re.M)
    if not match:
        raise SystemExit("the document has no info.version to record")
    return _unquote(match.group(1).strip())


def _unquote(value: str) -> str:
    """Strip one layer of matching surrounding single or double quotes."""
    if len(value) >= 2 and value[0] in "\"'" and value[-1] == value[0]:
        return value[1:-1]
    return value


if __name__ == "__main__":
    print(read_api_version(open(sys.argv[1]).read()))
