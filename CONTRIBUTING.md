# Contributing

## Development

```bash
python -m venv .venv
. .venv/Scripts/activate
pip install -e .[dev]
pytest
```

## Guidelines

- keep new abstractions grounded in verifiable environments
- prefer simple, explicit data structures over clever indirection
- mark paper-grounded claims separately from extensions
- add tests for any new blueprint or rendering logic

## Pull Requests

- explain which RL stage or environment pattern the change affects
- include tests for code changes
- update docs if architecture or reward logic changes
