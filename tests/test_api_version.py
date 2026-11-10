"""The API-version read that scripts/generate.sh records."""

from __future__ import annotations

import pytest

from api_version import read_api_version


def test_quoted_version_comes_out_bare() -> None:
    # A YAML dumper quotes a bare-numeric or date-like version; the recorded
    # value is the version itself, not the quotes.
    assert read_api_version("info:\n  title: x\n  version: '1.0'\n") == "1.0"
    assert read_api_version('info:\n  title: x\n  version: "2024-11-05"\n') == "2024-11-05"


def test_plain_version_is_unchanged() -> None:
    assert read_api_version("info:\n  version: v0.0.178\n") == "v0.0.178"
    # Only a matching pair of surrounding quotes is stripped; a stray leading
    # quote is left as-is rather than over-stripped.
    assert read_api_version("info:\n  version: '1.0\n") == "'1.0"


def test_missing_version_is_an_error() -> None:
    with pytest.raises(SystemExit):
        read_api_version("info:\n  title: x\n")
