#!/usr/bin/env bash
black --line-length=79 *.py
pylint *.py
mypy *.py
pyflakes *py
pycodestyle *.py
pydocstyle *.py
bandit *.py
python3 -m pytest *.py

