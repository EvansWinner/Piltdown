#!/usr/bin/env bash
black --line-length=79 *.py
pylint *.py
mypy *.py
pycodestyle *.py
pydocstyle *.py
python3 -m pytest *.py

