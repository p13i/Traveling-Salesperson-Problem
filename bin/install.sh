#!/usr/bin/env bash

source ./bin/utils.sh

# Executed once in a virtual environment

# Make sure mypy isn't listed in the requirements because not all versions of
# Python support it
if grep --quiet mypy requirements.txt; then
    echo 'mypy should not be in requirements.txt. Please fix it before continuing.'
    exit 1
else
    echo 'mypy does not exist in requirements.txt as expected.'
fi

# Install the requirements
pip install -r requirements.txt

# Source: https://stackoverflow.com/a/38520618
py_version=$(python -c "import sys; print('{0[0]}.{0[1]}'.format(sys.version_info))")

# If mypy is supported,
if [[ $(version_at_least ${py_version} '3.4') == true ]]; then
    pip install flake8-mypy==17.3.3 mypy==0.700 mypy-extensions==0.4.1 typed-ast==1.3.1
else
    echo 'mypy not supported in this Python version. Skipping install.';
fi
