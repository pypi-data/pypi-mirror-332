Learn PyPI package

## About

I want to create a PyPI package. Therefore, I need to answer some questions:

- How is a PyPI package structured?
- How is it tested (Unit)? What about static analysis and code style?
- How is it built and published to [PyPI](https://pypi.org)?
- How is it integrated with GitHub Actions?

## Structure
- `src` directory contains source files.
- `tests` directory contains test files
- `pyproject.toml` is a configuration file, to define build system requirements, project metadata, and other settings.

## Code style
- `black` package for code formatting.
- `isort` package for sorting imports. 
- `flake8` package for code linting.

> I consider they are in the category with ESLint and Prettier, but for Python only.

## Testing
- `pytest` package for unit testing.

## Commands

```bash
pip install poetry

poetry install

poetry run pytest

poetry build

poetry config pypi-token.pypi pypi-api-token-here

peotry publish
```
