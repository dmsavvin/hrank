install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hrank --cov-report xml

lint:
	poetry run flake8 hrank

selfcheck:
	poetry check

check: selfcheck test lint

.PHONY: install test lint selfcheck check