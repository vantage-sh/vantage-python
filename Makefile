.PHONY: install generate diff publish

install:
	python3 -m pip install -e ".[dev]"

generate:
	python3 autogen.py

diff: generate
	git diff --exit-code src/vantage

publish:
	python3 -m build
	twine upload dist/*
