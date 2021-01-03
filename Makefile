.PHONY: install coverage

all:
	@echo "Available: install, coverage"

coverage:
	coverage erase
	coverage run --source . test.py
	coverage report
	coverage html

install:
	pip install -e .
