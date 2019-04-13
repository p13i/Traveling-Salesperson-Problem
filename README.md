# Traveling Salesperson Problem - Solutions in Python

https://api.travis-ci.org/p13i/Traveling-Salesman-Problem.svg?branch=master

## Installation with `pip`

```bash
pip install gt-tsp
```

## Developer installation

```bash
git clone https://github.com/p13i/Traveling-Salesperson-Problem.git gt-tsp
cd gt-tsp
python3 -m venv venv
source venv/bin/activate
bash ./bin/install.sh
```

## Testing

Care has been taken to develop unit tests and ensure this code follows PEP8 conventions and type checking. Use `flake8` for coding style and type checking. Type checking with `mypy` is only supported in Python 3.5+ so please install that version before continuing.

```bash
bash ./bin/test.sh
```

## Publishing

```bash
python setup.py sdist
python setup.py sdist upload
```
