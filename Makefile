install:
	uv pip install -r requirements.txt

lint:
	ruff check .

test:
	pytest -v tests/

test-coverage:
	python3 -m pytest --cov=gendiff --cov-report xml tests/

check: lint test