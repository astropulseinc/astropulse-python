"""The package version follows the API version it was generated from."""

from __future__ import annotations

from pathlib import Path

import pytest

from astropulse import __api_version__, __version__
from release_version import (
    check_tag,
    package_version,
    parse,
    with_changelog_entry,
)

ROOT = Path(__file__).resolve().parent.parent


def test_the_committed_version_is_for_the_committed_api() -> None:
    assert parse(__version__)[:3] == parse(package_version(__api_version__, "0"))[:3]


def test_the_changelog_has_an_entry_for_this_version() -> None:
    assert f"\n## {__version__}\n" in (ROOT / "CHANGELOG.md").read_text()


def test_a_new_api_version_becomes_the_package_version() -> None:
    assert package_version("v1.0.6", "1.0.5") == "1.0.6"
    assert package_version("v1.0.6", "1.0.5.post2") == "1.0.6"
    assert package_version("1.1.0", "1.0.5") == "1.1.0"


def test_a_fix_release_survives_regeneration_for_the_same_api() -> None:
    assert package_version("v1.0.5", "1.0.5") == "1.0.5"
    assert package_version("v1.0.5", "1.0.5.post1") == "1.0.5.post1"


@pytest.mark.parametrize("api_version", ["v1.0", "v1.0.5-rc1", "1.0.5\n__x__ = 1", "latest"])
def test_an_unexpected_api_version_is_refused(api_version: str) -> None:
    with pytest.raises(SystemExit):
        package_version(api_version, "1.0.5")


@pytest.mark.parametrize("version", ["1.0.5.dev1", "1.0.5rc1", "v1.0.5", "1.0.5.post"])
def test_only_release_versions_parse(version: str) -> None:
    with pytest.raises(SystemExit):
        parse(version)


def test_post_releases_sort_after_their_base() -> None:
    assert parse("1.0.5") < parse("1.0.5.post1") < parse("1.0.5.post10") < parse("1.0.6")


def test_a_changelog_entry_is_added_once_above_the_newest() -> None:
    changelog = "# Changelog\n\nIntro.\n\n## 1.0.5\n\nFirst.\n"
    updated = with_changelog_entry(changelog, "1.0.6", "v1.0.6")
    assert updated == (
        "# Changelog\n\nIntro.\n\n## 1.0.6\n\nGenerated from API v1.0.6.\n\n## 1.0.5\n\nFirst.\n"
    )
    assert with_changelog_entry(updated, "1.0.6", "v1.0.6") == updated


def test_a_tag_must_match_and_be_newer() -> None:
    check_tag("v1.0.6", "1.0.6", ["v1.0.5", "v1.0.5.post1", "not-a-release"])
    check_tag("v1.0.5", "1.0.5", [])
    with pytest.raises(SystemExit):
        check_tag("v1.0.6", "1.0.5", [])
    with pytest.raises(SystemExit):
        check_tag("v1.0.5", "1.0.5", ["v1.0.5.post1"])
    with pytest.raises(SystemExit):
        check_tag("v1.0.5", "1.0.5", ["v1.0.5"])
