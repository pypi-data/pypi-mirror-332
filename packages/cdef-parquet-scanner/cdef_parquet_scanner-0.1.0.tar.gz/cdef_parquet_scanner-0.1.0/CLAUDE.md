# CDEF Parquet Scanner Guidelines

## Commands
- Run main script: `python schema.py <directory_path> [output_file]`
- Run single test: `pytest tests/<test_file>.py::test_<function_name> -v`
- Run all tests: `pytest`
- Format code: `black .`
- Lint code: `flake8`
- Type check: `mypy .`

## Code Style
- Use PEP 8 style guide
- Imports: standard library first, third-party modules (pyarrow) second
- Line length: 88 chars (Black default)
- Docstrings: use triple-quoted strings with clear descriptions
- Type hints: prefer explicit types for function parameters and return values
- Error handling: use try/except blocks with specific exceptions
- Naming: snake_case for functions/variables, PascalCase for classes
- Functions should be focused and do one thing well
- Comments should explain "why", not "what"