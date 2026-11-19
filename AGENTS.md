# AGENTS.md

How to work in this repository, for people and coding agents. This is the official Python SDK for
the AstroPulse Platform API (`astropulse` on PyPI). Most of it is generated from the platform's
OpenAPI document, and a small hand-written layer sits on top. [CONTRIBUTING.md](CONTRIBUTING.md)
covers the same process for people. When the two disagree, fix whichever one is wrong.

## Commands

```bash
make check      # creates .venv, then runs pytest, ruff (lint + format) and mypy --strict
make sync       # fetch the published API document into spec/openapi.yaml
make generate   # regenerate _generated/, models.py and docs/ from the spec (needs Docker)
make build      # wheel + sdist
```

Run `make check` before every commit; CI runs the same targets. CI's `generated` job also fails
when the committed generated code differs from what the spec and templates produce.

## Who owns which files

| Path                                                              | Owner                            |
| ----------------------------------------------------------------- | -------------------------------- |
| `spec/openapi.yaml`                                               | `make sync`                      |
| `src/astropulse/_generated/`, `src/astropulse/models.py`, `docs/` | `make generate`: never edit      |
| `templates/python/*.mustache`                                     | hand-written generator overrides |
| `src/astropulse/{_client,_errors,__init__,_version}.py`           | hand-written                     |
| `scripts/`, `tests/`, `examples/`, `.github/`                     | hand-written                     |

- **Never edit generated files by hand.** To change generated code, either change the API
  upstream and run `make sync generate`, or change a template and run `make generate`.
- **Decide whose bug it is.** If a real response doesn't parse, the spec is wrong: fix the API
  document upstream. If the generated plumbing is wrong for us (timeouts, errors, enums), fix it
  with a template override. Only behaviour callers would otherwise write themselves belongs in
  the hand-written layer.
- The generator (openapi-generator) is pinned in `scripts/generate.sh` and runs in Docker. Never
  upgrade it as a side effect of other work.
- After `make generate`, the diff must contain only what your change explains. Anything else
  means the spec moved or a template is wrong. Find out which before you commit.

## Changing a template

Each override is upstream's template at the pinned version, plus the change that the
`{{! ... }}` header at the top of the file describes.

1. Start from upstream's file at the pinned tag, never from memory:
   `https://raw.githubusercontent.com/OpenAPITools/openapi-generator/<VERSION>/modules/openapi-generator/src/main/resources/python/<name>.mustache`
2. Make the smallest change that works. Put any logic in a hand-written module and call it from
   the template; `_errors.connection_error` is the model to follow. Template code is neither
   type-checked nor unit-tested.
3. Describe the change in the header. Update the notes in `scripts/generate.sh` and the template
   paragraph in CONTRIBUTING to match.
4. Run `make generate`. Commit the template together with the regenerated files, and only those.

Generated code imports the hand-written modules while the package is still importing. Those
modules must not import `_generated` at run time; put such imports under `if TYPE_CHECKING:`.

## The public surface

- **The API document is the interface.** Don't wrap, rename or re-shape generated methods and
  models. A caller should be able to read the API reference and know the Python call.
- **What is public:** `astropulse.__all__` and `astropulse.models`. Everything else is private,
  and new modules start with an underscore. Make something public only when callers need it,
  because every public name has to be supported from then on. Add it to `__all__` in its
  commented group and to the README.
- **Runtime behaviour is the contract.** Assume callers depend on every public name, base
  class, default, keyword argument and exception type. Never remove or rename one; add the new
  one beside it. A change in which exception is raised is a user-visible change and goes in the
  changelog.
- **The API may add enum values at any time.** They must parse (`model_enum` and `model_generic`
  make sure of this). Never add code that rejects a value it does not know.
- **Don't re-validate what the API validates.** Let the server reject bad input, and surface its
  `code` and `trace_id`. Check only what the API cannot report, such as a missing key.

## Errors

The hierarchy:

- `AstroPulseError` is the root.
- The API's refusals are `ApiException`, with one subclass per status, carrying `.data.code` and
  `.data.trace_id`.
- A request that gets no answer raises `ApiConnectionError`; if it ran out of time,
  `ApiTimeoutError`.
- Waiting for a deploy raises `DeploymentFailed` or `WaitTimeout`.

Rules for raising:

- **Raise an SDK error when the SDK or the platform failed:** a status, the transport, waiting,
  or setup the SDK resolves itself (no API key found). It derives from `AstroPulseError`.
- **Raise the builtin when the caller made a programming mistake.** Arguments that conflict or
  are out of range raise plain `TypeError` or `ValueError`, exactly as any Python library would.
  `except AstroPulseError` must never hide a bug.
- **Keep the old base when an error changes type.** If it replaces one raised before, it also
  derives from that one, so existing `except` clauses still catch it. For example,
  `WaitTimeout(AstroPulseError, TimeoutError)`.
- When you convert an exception, write `raise New(...) from error`.
- Write one message per check, saying what was wrong and what to do: `"No API key. Pass
  api_key=..., or set ASTROPULSE_API_KEY."`
- Never branch on the text of an exception. Use its type or `.data.code`.
- Keep the API key out of messages, logs and reprs.

## Python style

- Support Python 3.10 to 3.14. Begin modules with `from __future__ import annotations`, and write
  `X | None`, not `Optional[X]`.
- Type everything: mypy runs in strict mode over `src/astropulse`, `scripts`, `tests` and
  `examples`. Avoid `Any` and `# type: ignore`. If one is unavoidable, give the error code
  (`# type: ignore[arg-type]`).
- `ruff` with a line length of 100 is the only linter and formatter. Generated files are
  excluded from it on purpose; keep them excluded.
- Make optional and behaviour arguments keyword-only (`*`). Defaults are module constants
  (`DEFAULT_TIMEOUT`), so callers and tests can name them.
- Runtime dependencies are only those in `pyproject.toml`. A new one needs a reason in the PR.
- Every public class and function has a docstring in plain sentences: the first line says what
  it does, the rest says why it works that way. Follow the markup already in the file. Write no
  comment by default; write one only for a non-obvious *why*, never to say *what* the code does.

## Tests

- Tests use `pytest` in `tests/`, and each test's name is a sentence:
  `test_a_refused_connection_is_a_connection_error_not_a_timeout`.
- **Fail before, pass after.** Every fix or behaviour change comes with a test that fails without
  it. Cover the negative branch too.
- **Test through the public API** (`from astropulse import ...`). Reach into a private module only
  for a helper that module owns.
- **No network access.** Use `monkeypatch`, small fakes, or a local socket on `127.0.0.1` for
  transport behaviour. The whole suite runs in seconds.
- **Pin each promise.** A kept base class, an accepted unknown enum value, a re-export: each gets
  a test that asserts it.
- **Tripwire tests.** Hand-written code that lists something derived from generated code (like
  the exception exports in `test_errors.py`) gets a test that fails when regeneration changes one
  side without the other. Its message says what to update.
- `examples/` are real programs: they are type-checked and imported by `tests/test_examples.py`.
  Keep them short, and runnable with only `ASTROPULSE_API_KEY` set.

## Versions and releases

- `__version__` is the API version the code was generated from: API v1.0.6 gives `1.0.6`.
  `make generate` sets it and adds the `CHANGELOG.md` entry.
- A fix to this package alone, against the same API, is a post release. Set `1.0.6.post1` by
  hand and add a `## 1.0.6.post1` changelog entry; the tests check the two agree.
- **Never bump the version unless asked.** Merging a version change to `main` tags it and
  publishes it to PyPI automatically. A merge without one releases nothing.

## Git and pull requests

- Never push to `main`. Branch from a fresh main:
  `git fetch origin && git checkout -b <branch> origin/main`.
- Before pushing to an existing branch, check that its PR has not merged
  (`gh pr list --head <branch> --json state`). If it has, start a new branch.
- **Every PR resolves an issue.** File the issue first, and put `Fixes #<n>` in the PR body. Scope
  the PR so that merging it closes the issue completely, and keep it to one logical change.
- Commit subjects and PR titles are plain sentences about what changes for the user ("Enums carry
  their labels and meanings from the API document"), not `feat:` prefixes.
- The PR body says what was wrong, what changed, what stays compatible, and how you verified it
  (`make check`, plus `make generate` and its diff when generated code moved). Update the body
  when later commits change the scope.
- Review a regeneration PR ("Sync platform vX.Y.Z") as an API contract change: its diff is the
  API's diff.

## Before you finish

- [ ] `make check` passes.
- [ ] If the spec or a template changed, `make generate` was run and every generated change is
      explained.
- [ ] New public names are in `__all__` and in the README, and the tests assert any compatibility
      promise.
- [ ] Docs describing what you changed (README, CONTRIBUTING, docstrings, `generate.sh` notes)
      still match the code.
