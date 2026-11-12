#!/usr/bin/env bash
# Generate the platform resource layer from the OpenAPI document.
#
# openapi-generator, pinned to the same version every AstroPulse SDK uses, so
# the SDKs stay consistent and no new tool enters the stack. Everything under
# src/astropulse/_generated is written by this script: never edit it,
# regenerate it.
set -euo pipefail

VERSION="v7.24.0"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SPEC="${1:-${ROOT}/spec/openapi.yaml}"

command -v docker >/dev/null || { echo "docker is required"; exit 1; }

rm -rf "${ROOT}/src/astropulse/_generated"
# templates/python overrides three of the generator's own templates. So that an
# enum value the API adds later parses instead of raising, model_enum keeps an
# unlisted value as a member carrying it, and model_generic does not check an
# inline enum field against the values listed; each is upstream's file for the
# version above with that one change. partial_header is a fixed header, so a new
# API version or description rewrites no file whose code is unchanged.
# Run as the caller, not as root: the container writes into the mounted
# repository, and files it leaves owned by root cannot be moved or removed
# afterwards. Docker Desktop hides this by remapping ownership; on Linux, and so
# in CI, the generate step fails with "Permission denied".
docker run --rm \
  --user "$(id -u):$(id -g)" \
  -v "${ROOT}:/local" -v "$(dirname "${SPEC}"):/spec" \
  "openapitools/openapi-generator-cli:${VERSION}" generate \
  -i "/spec/$(basename "${SPEC}")" \
  -g python \
  -t /local/templates/python \
  -o /local/.generated \
  --additional-properties=packageName=astropulse._generated,generateSourceCodeOnly=true \
  >/dev/null

mv "${ROOT}/.generated/astropulse/_generated" "${ROOT}/src/astropulse/_generated"
rm -rf "${ROOT}/.generated"

# The reference lives at docs/, not inside the package: it is for reading, not
# for shipping in the wheel. One page per resource and per model, generated
# from the same document as the code.
rm -rf "${ROOT}/docs"
mv "${ROOT}/src/astropulse/_generated/docs" "${ROOT}/docs"
rm -rf "${ROOT}/src/astropulse/_generated/test"

# The public `astropulse.models` re-exports every generated type. A star import
# with a computed __all__ is invisible to a type checker -- mypy --strict and
# pyright both refuse `from astropulse.models import ApplicationCreate`, which
# is the first line of the README -- so write the list out instead, in the
# redundant-alias form that marks an explicit re-export.
python3 - "${ROOT}" <<'PYTHON'
import pathlib, re, sys

root = pathlib.Path(sys.argv[1])
# Read the recorded API version through the unit-tested helper beside this script.
sys.path.insert(0, str(root / "scripts"))
from api_version import read_api_version

generated = (root / "src/astropulse/_generated/models/__init__.py").read_text()
imports = re.findall(r"^from (astropulse\._generated\.models\.\w+) import (\w+)$", generated, re.M)
if not imports:
    raise SystemExit("no generated models found to re-export")

lines = [
    '"""The request and response types, generated from the API document.',
    "",
    "    from astropulse.models import ApplicationCreate",
    "",
    "Every type here is generated, and so is this file: scripts/generate.sh writes",
    "it from the generated package so a type checker can see the re-exports.",
    "They are pydantic models, so ``from_dict`` builds one from the JSON shape the",
    "API documents, and ``to_dict`` gives it back.",
    '"""',
    "",
    "from __future__ import annotations",
    "",
]
for module, name in sorted(imports, key=lambda pair: pair[1]):
    relative = module.replace("astropulse._generated", "._generated")
    lines.append(f"from {relative} import {name} as {name}")
lines += ["", "__all__ = ["]
lines += [f'    "{name}",' for _, name in sorted(imports, key=lambda pair: pair[1])]
lines += ["]", ""]
(root / "src/astropulse/models.py").write_text("\n".join(lines))
print(f"re-exported {len(imports)} types from astropulse.models")

# The document's own version -- the platform build it was generated from. The
# package's version is its own (a client fix ships without an API change), so
# this is recorded rather than copied into it.
api_version = read_api_version((root / "spec/openapi.yaml").read_text())
(root / "src/astropulse/_api_version.py").write_text(
    '"""The API document this package was generated from. Written by '
    'scripts/generate.sh."""\n\n__api_version__ = "%s"\n' % api_version
)
print(f"generated from API document {api_version}")
PYTHON
echo "generated $(ls "${ROOT}/src/astropulse/_generated/api" | grep -c '_api.py') resource classes, $(ls "${ROOT}/src/astropulse/_generated/models" | wc -l | tr -d ' ') models, $(ls "${ROOT}/docs" | wc -l | tr -d ' ') reference pages"
