.PHONY: format test lint check

target := rabbit_todo/

format:
	black $(target)
	isort $(target)

test:
	pytest tests/ -v

lint:
	pylint $(target)

check:
	mypy
	pflake8 $(target)
	pylint $(target)

all: format check test
