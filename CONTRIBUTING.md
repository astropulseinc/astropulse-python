# Contributing

## Setup

```bash
make check          # creates .venv, then runs the tests, style and types
```

## What is generated, and what is not

The API surface is generated from the platform's public OpenAPI document, which lives in
`spec/openapi.yaml`. `make sync` fetches the published document from
<https://api.astropulse.io/api/v1/openapi> and `make generate` runs openapi-generator
(v7.24.0, pinned, in Docker) over it, writing `src/astropulse/_generated/` and the reference
under `docs/`. Never hand-edit either: change the API, regenerate, and review the result as a
contract change.

Two of the generator's templates are overridden in `templates/python/`, so that an enum value
the API adds later parses instead of raising. Each is upstream's file for the pinned version
with one change, described at its top: re-copy and re-apply them when the version changes.

The hand-written layer is small and stays that way: `_client.py` (the client, its retry and
timeout policy, and `wait_until_serving`), `_errors.py`, `__init__.py` and `_version.py`, plus the
tests and examples. Everything else, `models.py` included, is written by `scripts/generate.sh`.

## An API change reaches this repository like this

1. The API changes, and its own CI refuses the change if it would break existing callers.
2. The new document is published at <https://api.astropulse.io/api/v1/openapi>.
3. The regeneration workflow runs `make sync generate check` and opens a PR titled
   "Sync platform <version>". Review it as a contract change: the diff is the API's diff. A
   weekly run backs this up, so a missed release shows up as a PR rather than as an SDK that
   quietly describes last month's API.

## Versions and releases

The package version is the API version it was generated from: API v1.0.5 gives 1.0.5.
`make generate` sets `src/astropulse/_version.py` and adds a `CHANGELOG.md` entry for it, so a
regeneration PR carries its own version. A fix to this package alone, against the same API, is a
post release: set `__version__` to `1.0.5.post1` by hand and add a `## 1.0.5.post1` entry to
`CHANGELOG.md`. The tests fail if the version does not match the API version or has no
changelog entry.

Releases need no manual step. When a PR that changes `__version__` merges to main, the tag
workflow tags `v<version>`, and the release workflow checks that tag, runs `make check`, builds,
publishes to PyPI through Trusted Publishing (no token is stored here, and PyPI records an
attestation of the build), and creates the GitHub release. A merge that does not change the
version releases nothing. The tag is created with a GitHub App token (repository secrets
`RELEASE_APP_CLIENT_ID` and `RELEASE_APP_PRIVATE_KEY`), because a tag created with the built-in
token does not start the release workflow.
