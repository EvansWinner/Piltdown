#!/usr/bin/env bash
black *.py
pylint *.py
mypy *.py
pycodestyle *.py
pydocstyle *.py
pytest *.py

