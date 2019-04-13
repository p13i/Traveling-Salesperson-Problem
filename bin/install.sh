#!/usr/bin/env bash

# Executed once in a virtual environment

# Make sure mypy isn't listed in the requirements because not all versions of
# Python support it
if grep --quiet mypy requirements.txt; then
    echo 'mypy should not be in requirements.txt' & exit 1
else
    echo 'mypy does not exist in requirements.txt as expected.'
fi

# Install the requirements
pip install -r requirements.txt

# If mypy is supported,
if [[ ${SUPPORT_MYPY} ]]; then
    pip install flake8-mypy==17.3.3 mypy==0.700 mypy-extensions==0.4.1
else
    echo 'mypy not supported in this Python version. Skipping install.';
fi
