all: lint test

test:
	pytest -v test.py

lint:
	black --diff .
	ruff check .
	pyright .
	
