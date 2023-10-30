.PHONY: format

format:
	black . && isort .

test:
	pytest tests/ -v

lint:
	pylint rabbit_todo
