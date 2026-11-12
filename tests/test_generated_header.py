"""Generated files carry one fixed header, never the API version or description."""

from pathlib import Path

GENERATED = Path(__file__).resolve().parent.parent / "src" / "astropulse" / "_generated"
HEADER = "Generated from the AstroPulse API document by OpenAPI Generator."


def test_no_generated_file_carries_the_api_version() -> None:
    files = list(GENERATED.rglob("*.py"))
    assert len(files) > 100
    stamped = [
        str(p.relative_to(GENERATED))
        for p in files
        if "The version of the OpenAPI document" in p.read_text()
    ]
    assert stamped == []


def test_api_and_model_files_start_with_the_fixed_header() -> None:
    files = [
        p
        for kind in ("api", "models")
        for p in (GENERATED / kind).glob("*.py")
        if p.name != "__init__.py"
    ]
    assert len(files) > 100
    missing = [str(p.relative_to(GENERATED)) for p in files if HEADER not in p.read_text()[:400]]
    assert missing == []
