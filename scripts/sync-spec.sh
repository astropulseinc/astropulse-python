#!/usr/bin/env bash
# Fetch the platform's PUBLIC API document and, when its version differs from
# the committed spec, write it to the spec file. Pull-only: a public URL, no
# credential, and no read access to the platform's source.
#
# Usage: sync-spec.sh <url> <out>
#
# It prints a one-line decision and, under GitHub Actions, writes `status`
# (absent|unchanged|changed) and `version` to $GITHUB_OUTPUT, so the workflow
# regenerates only when the document actually moved.
set -euo pipefail

url="${1:?usage: sync-spec.sh <url> <out>}"
out="${2:?usage: sync-spec.sh <url> <out>}"

emit() { # key=value -> $GITHUB_OUTPUT when running under Actions
	if [ -n "${GITHUB_OUTPUT:-}" ]; then
		echo "$1" >>"$GITHUB_OUTPUT"
	fi
}

tmp="$(mktemp)"
trap 'rm -f "$tmp"' EXIT

# Until the release serves the document the route is absent; that is the
# expected state before launch, not a failure, so the run ends green.
if ! curl -fsSL "$url" -o "$tmp" 2>/dev/null; then
	echo "no published document yet"
	emit "status=absent"
	exit 0
fi

# Parse the fetched bytes once: confirm it is an OpenAPI document and read its
# version and operation count. A 200 that is not the document (an HTML error
# page, an empty body) fails here — red, and before anything is written — so a
# bad fetch never becomes the committed spec. A plain assignment lets `set -e`
# abort on that failure.
summary="$(python3 - "$tmp" <<'PY'
import sys, yaml
doc = yaml.safe_load(open(sys.argv[1]))
if not isinstance(doc, dict) or "version" not in (doc.get("info") or {}) or "paths" not in doc:
    sys.exit("fetched document is not an OpenAPI document")
ops = sum(1 for p in doc["paths"].values() for m in p if m in ("get", "post", "put", "patch", "delete"))
print(doc["info"]["version"], ops)
PY
)"
served="${summary%% *}"
ops="${summary##* }"

current=""
if [ -f "$out" ]; then
	current="$(python3 -c 'import sys,yaml; print(yaml.safe_load(open(sys.argv[1]))["info"]["version"])' "$out")"
fi

if [ "$served" = "$current" ]; then
	echo "version: $served (unchanged)"
	emit "status=unchanged"
	emit "version=$served"
	exit 0
fi

# The generator reads the YAML spec. Dump sorted and with unicode intact so the
# committed spec is deterministic regardless of the served key order and stays
# readable (JSON is a YAML subset, so one path handles the served JSON).
python3 -c 'import sys,yaml; yaml.safe_dump(yaml.safe_load(open(sys.argv[1])), open(sys.argv[2],"w"), sort_keys=True, allow_unicode=True)' "$tmp" "$out"

echo "version: $served operations: $ops"
emit "status=changed"
emit "version=$served"
