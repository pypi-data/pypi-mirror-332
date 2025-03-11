# pypi_test_ameynert

[![PyPI Release](https://badge.fury.io/py/pypi_test_ameynert.svg)](https://badge.fury.io/py/pypi_test_ameynert)[![CI](https://github.com/ameynert/pypi_test_ameynert/actions/workflows/python_package.yml/badge.svg?branch=main)](https://github.com/ameynert/pypi_test_ameynert/actions/workflows/python_package.yml?query=branch%3Amain)
[![Python Versions](https://img.shields.io/badge/python-3.11_|_3.12_|_3.13-blue)](https://github.com/ameynert/pypi_test_ameynert)
[![MyPy Checked](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://docs.astral.sh/ruff/)

...

## Recommended Installation

Install the Python package and dependency management tool [`poetry`](https://python-poetry.org/docs/#installation) using official documentation.
You must have Python 3.11 or greater available on your system path, which could be managed by [`mamba`](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html), [`pyenv`](https://github.com/pyenv/pyenv), or another package manager. 
Finally, install the dependencies of the project with:

```console
poetry install
```

To check successful installation, run:

```console
poetry run pypi_test_ameynert hello --name Fulcrum
```

## Installing into a Mamba Environment

Install the Python package and dependency management tool [`poetry`](https://python-poetry.org/docs/#installation) and the environment manager [`mamba`](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html) using official documentation.
Create and activate a virtual environment with Python 3.11 or greater:

```console
mamba create -n pypi_test_ameynert python=3.11
mamba activate pypi_test_ameynert
```

Then, because Poetry will auto-detect an activated environment, install the project with:

```console
poetry install
```

To check successful installation, run:

```console
pypi_test_ameynert hello --name Fulcrum
```

## Development and Testing

See the [contributing guide](./CONTRIBUTING.md) for more information.
