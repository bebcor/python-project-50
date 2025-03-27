install:
	pip3 install --user --break-system-packages -r requirements.txt

lint:
	python3 -m ruff check .

test:
	python3 -m pytest -v tests/

test-coverage:
	python3 -m pytest --cov=gendiff --cov-report xml tests/

check: lint test

.PHONY: install lint test test-coverage check