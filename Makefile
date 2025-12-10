.PHONY: help install install-dev test clean format lint type-check all-checks demo docs

help:
	@echo "Agent-Toga Development Commands"
	@echo "================================"
	@echo ""
	@echo "Installation:"
	@echo "  make install        - Install package in editable mode"
	@echo "  make install-dev    - Install with development dependencies"
	@echo ""
	@echo "Testing:"
	@echo "  make test          - Run all tests"
	@echo "  make test-verbose  - Run tests with verbose output"
	@echo "  make coverage      - Run tests with coverage report"
	@echo ""
	@echo "Code Quality:"
	@echo "  make format        - Format code with black and isort"
	@echo "  make lint          - Run flake8 linter"
	@echo "  make type-check    - Run mypy type checker"
	@echo "  make all-checks    - Run all quality checks"
	@echo ""
	@echo "Demos:"
	@echo "  make demo          - Run personality demo"
	@echo "  make demo-security - Run security testing demo"
	@echo "  make demo-transform - Run transform quirk demo"
	@echo ""
	@echo "Maintenance:"
	@echo "  make clean         - Remove build artifacts and cache"
	@echo "  make docs          - Generate documentation"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"
	pip install -r requirements-dev.txt

test:
	python examples/test_toga.py

test-verbose:
	python examples/test_toga.py -v

test-pytest:
	pytest examples/test_toga.py -v

coverage:
	pytest examples/test_toga.py --cov=python --cov-report=html --cov-report=term

format:
	@echo "Formatting with black..."
	black python/ examples/ --line-length 100
	@echo "Sorting imports with isort..."
	isort python/ examples/ --profile black

lint:
	@echo "Running flake8..."
	flake8 python/ examples/ --max-line-length=100 --extend-ignore=E203,W503

type-check:
	@echo "Running mypy..."
	mypy python/

all-checks: format lint type-check test
	@echo "✓ All checks passed!"

demo:
	python examples/demo_toga.py

demo-security:
	python examples/security_testing_examples.py

demo-transform:
	python examples/transform_examples.py

demo-usage:
	python examples/usage_examples.py

clean:
	@echo "Cleaning build artifacts..."
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*~" -delete
	@echo "✓ Cleaned!"

docs:
	@echo "Documentation is in docs/ directory"
	@echo "View README.md for main documentation"

.DEFAULT_GOAL := help
