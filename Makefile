.PHONY: install publish

install:
	python3 autogen.py
	python3 -m pip install -e ".[dev]"

publish:
	python3 autogen.py
	python3 -m build
	twine upload dist/*
