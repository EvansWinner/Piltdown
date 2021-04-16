#!/usr/bin/env bash
function div {
  echo "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
  echo "$1"
}

div "Running shellcheck against this file..."
shellcheck check.sh


# div "Running mdl to check markdown..."
# mdl README.md

div "Running black..."
black --line-length=79 piltdown/*.py

div "Running pylint..."
pylint piltdown/*.py

div "Running mypy..."
mypy piltdown/*.py

div "Running pyflakes..."
pyflakes piltdown/*py

div "Running pycodestyle..."
pycodestyle piltdown/*.py

div "Running pydocstyle..."
pydocstyle piltdown/*.py

div "Running bandit..."
bandit -s B101 piltdown/*.py

# div "Running pytest..."
# python3 -m pytest piltdown/*.py

