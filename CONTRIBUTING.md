# Contributing

## Setup

```bash
make check          # creates .venv, then runs the tests, style and types
```

## What is generated, and what is not

The API surface is generated from the platform's public OpenAPI document, which lives in
`spec/openapi.yaml`. `make sync` fetches the published document from
<https://astropulse.io/docs/openapi/openapi.yaml> and `make generate` runs openapi-generator
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
2. The new document is published at <https://astropulse.io/docs/openapi/openapi.yaml>.
3. `make sync generate check` here, opened as a PR. Review it as a contract change: the diff
   is the API's diff. The regeneration workflow does exactly this on a schedule, so a missed
   release shows up as a PR rather than as an SDK that quietly describes last month's API.

Maintainers working on an API change that has not shipped yet can regenerate from a platform
checkout instead of the published document: `make sdk-python` there does the round trip.

## Releasing

Releases are tag-driven, and PyPI authenticates through Trusted Publishing, so no token is
stored in this repository.

1. Bump `__version__` in `src/astropulse/_version.py`. That is the only copy: the package version
   is read from it at build time, and the release workflow refuses a tag that disagrees with it.
2. Merge that PR.
3. Tag it: `git tag v0.1.0 && git push origin v0.1.0`.

The release workflow refuses to publish when the tag and the packaged version disagree.

Versioning is semver and independent of the API version: an additive API change is a minor
release here, and anything that breaks a caller of this package is a major one.
