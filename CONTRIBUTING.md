# Contributing

Thanks for contributing.

Project repository: `https://github.com/mitkox/megacode`

## Development Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Run Checks

```bash
ruff check .
pytest
python -m py_compile audit.py
python audit.py --help
```

## Pull Request Guidelines

- Keep changes focused and minimal.
- Add/update tests for behavior changes.
- Update `README.md` when CLI behavior or defaults change.
- Keep `CHANGELOG.md` updated for notable user-facing changes.
- Avoid committing local audit output files.

## Commit Guidelines

- Use clear commit messages.
- Reference issues where relevant.
