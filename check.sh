#!/usr/bin/env bash

function div {
  echo "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
  echo "$1"
}

div "Running shellcheck against this file..."
shellcheck check.sh

div "Running mdl to check markdown in README..."
mdl README.md

div "Running black..."
black --line-length=79 ./*.py

div "Running pylint..."
pylint ./*.py

div "Running mypy..."
mypy ./*.py

div "Running pyflakes..."
pyflakes ./*py

div "Running pycodestyle..."
pycodestyle ./*.py

div "Running pydocstyle..."
pydocstyle ./*.py

div "Running bandit..."
bandit -s B101 ./*.py

div "Running pytest..."
python3 -m pytest ./*.py

