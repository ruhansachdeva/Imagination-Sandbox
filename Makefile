.DEFAULT_GOAL := help
PYTHON ?= python3

.PHONY: help run test lint clean

help: ## Show this help
	@grep -E '^[a-z-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-8s\033[0m %s\n", $$1, $$2}'

run: ## Run the project entry point
	$(PYTHON) main.py

test: ## Run the test suite
	$(PYTHON) -m unittest discover -s tests -v

clean: ## Remove caches and build artefacts
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	rm -rf .pytest_cache .mypy_cache .ruff_cache build dist *.egg-info
