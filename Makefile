VERSION=$(shell grep version setup.py | cut -d= -f2 | sed 's/[",]//g')

.PHONY: install release coverage

all:
	@echo "Available: install, release, coverage"

coverage:
	coverage run --source . test.py
	coverage report

install:
	pip install -e .

release:
	git tag v$(VERSION)
	git push --tags origin master
	hub release create -m "Release v$(VERSION)" v$(VERSION)
