.DEFAULT_GOAL := help

# The API document this package is generated from. The platform serves it as
# the public OpenAPI document, the same for every caller; this repository only
# fetches it, over a public URL with no credential, and never the internal
# document.
SPEC_URL ?= https://api.astropulse.io/api/v1/openapi
SPEC := spec/openapi.yaml
# The files this repository owns. Everything else under src/astropulse is
# written by scripts/generate.sh and is the generator's business to format.
HANDWRITTEN := src/astropulse/_client.py src/astropulse/_errors.py \
	src/astropulse/__init__.py src/astropulse/_version.py tests examples
VENV := .venv
PYTHON := $(VENV)/bin/python

.PHONY: help
help: ## Show this help
	@grep -hE '^[a-z-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN{FS=":.*?## "}{printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

$(PYTHON):
	python3 -m venv $(VENV)

.PHONY: install
install: $(PYTHON) ## Install the package and the dev tools into .venv
	$(PYTHON) -m pip install -q --upgrade pip
	# --group reads [dependency-groups] in pyproject.toml, so the tools are
	# declared in one place rather than listed again here.
	$(PYTHON) -m pip install -q -e '.[examples]' --group dev

.PHONY: sync
sync: ## Fetch the published API document, writing $(SPEC) only when it moved
	@./scripts/sync-spec.sh "$(SPEC_URL)" "$(SPEC)"

.PHONY: generate
generate: ## Regenerate the client and the reference docs from spec/openapi.yaml
	./scripts/generate.sh $(abspath $(SPEC))

.PHONY: test
test: install ## Run the tests
	$(PYTHON) -m pytest -q

.PHONY: lint
lint: install ## Check style
	$(VENV)/bin/ruff check .
	$(VENV)/bin/ruff format --check $(HANDWRITTEN)

.PHONY: typecheck
typecheck: install ## Check types
	$(VENV)/bin/mypy

.PHONY: check
check: test lint typecheck ## Everything CI runs

.PHONY: build
build: install ## Build the wheel and the sdist
	$(PYTHON) -m pip install -q build
	$(PYTHON) -m build

.PHONY: clean
clean: ## Remove build output and caches
	rm -rf dist build .pytest_cache .mypy_cache .ruff_cache
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
