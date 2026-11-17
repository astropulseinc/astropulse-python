"""The package version, derived from the API version it was generated from.

1.0.5 is generated from API v1.0.5. A fix to this package alone, against the
same API, is 1.0.5.post1 (PEP 440). Only these two forms are released.

    release_version.py sync     # after generation: set _version.py, add a CHANGELOG entry
    release_version.py current  # print the package version, checked
    release_version.py tag v1.0.5 [tags...]  # check a tag against the version and releases
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from api_version import read_api_version

ROOT = Path(__file__).resolve().parent.parent
VERSION_FILE = ROOT / "src" / "astropulse" / "_version.py"
CHANGELOG = ROOT / "CHANGELOG.md"
SPEC = ROOT / "spec" / "openapi.yaml"

API_VERSION = re.compile(r"v?(\d+)\.(\d+)\.(\d+)")
PACKAGE_VERSION = re.compile(r"(\d+)\.(\d+)\.(\d+)(?:\.post(\d+))?")


def parse(version: str) -> tuple[int, int, int, int]:
    """Return a released package version as a sortable tuple, or refuse it."""
    match = PACKAGE_VERSION.fullmatch(version)
    if not match:
        raise SystemExit(f"{version!r} is not a release version (1.2.3 or 1.2.3.postN)")
    major, minor, patch, post = match.groups()
    return int(major), int(minor), int(patch), int(post or 0)


def base_of_api(api_version: str) -> str:
    """Return the package version an API version maps to: v1.0.5 -> 1.0.5."""
    match = API_VERSION.fullmatch(api_version)
    if not match:
        raise SystemExit(f"API version {api_version!r} is not v1.2.3; refusing to derive a version")
    return ".".join(match.groups())


def package_version(api_version: str, current: str) -> str:
    """The version to ship: the current one while it is for this API, else the API's."""
    base = base_of_api(api_version)
    if PACKAGE_VERSION.fullmatch(current) and parse(current)[:3] == parse(base)[:3]:
        return current
    return base


def read_version(text: str) -> str:
    match = re.search(r'^__version__ = "([^"]+)"$', text, re.M)
    if not match:
        raise SystemExit("_version.py has no __version__")
    return match.group(1)


def with_changelog_entry(changelog: str, version: str, api_version: str) -> str:
    """Add a section for ``version`` above the newest one, unless it has one."""
    if re.search(rf"^## {re.escape(version)}$", changelog, re.M):
        return changelog
    entry = f"## {version}\n\nGenerated from API {api_version}.\n\n"
    head, sep, rest = changelog.partition("\n## ")
    if not sep:
        return changelog.rstrip("\n") + "\n\n" + entry.rstrip("\n") + "\n"
    return head + "\n" + entry + "## " + rest


def check_tag(tag: str, version: str, existing: list[str]) -> None:
    """A tag must name this version and be newer than every release tag."""
    if tag != f"v{version}":
        raise SystemExit(f"tag {tag} does not match the package version {version}")
    released = [parse(t[1:]) for t in existing if PACKAGE_VERSION.fullmatch(t[1:])]
    if released and parse(version) <= max(released):
        raise SystemExit(f"{version} is not newer than every released version")


def main(argv: list[str]) -> None:
    command = argv[0] if argv else ""
    current = read_version(VERSION_FILE.read_text())
    if command == "sync":
        api_version = read_api_version(SPEC.read_text())
        version = package_version(api_version, current)
        if version != current:
            VERSION_FILE.write_text(f'__version__ = "{version}"\n')
        CHANGELOG.write_text(with_changelog_entry(CHANGELOG.read_text(), version, api_version))
        print(f"package version {version} (API {api_version})")
    elif command == "current":
        parse(current)
        print(current)
    elif command == "tag" and len(argv) >= 2:
        parse(current)
        check_tag(argv[1], current, [t for t in argv[2:] if t != argv[1]])
        print(f"{argv[1]} matches the package version")
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
