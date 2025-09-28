# Package Management Rules

## ALWAYS use `uv` for Python package management
- Use `uv run` prefix for all Python commands (e.g., `uv run mkdocs build`)
- Use `uv add` to add dependencies instead of `pip install`
- Use `uv sync` to install dependencies from pyproject.toml
- Use `uv lock` to update lock file

## MkDocs Commands
- Build: `uv run mkdocs build`
- Serve: `uv run mkdocs serve`
- Deploy: `uv run mkdocs gh-deploy`

## Development Workflow
1. Use `uv sync` to ensure dependencies are installed
2. Use `uv run mkdocs serve` for local development
3. Use `uv run mkdocs build` to test builds
4. All Python scripts should be run with `uv run` prefix

## Project Structure
- Main documentation in `docs/` directory
- MkDocs configuration in `mkdocs.yml`
- Python dependencies in `pyproject.toml`
- Main Python script: `main.py` (for macros)

## Regex Documentation
- File `docs/regex.md` contains regex patterns that may look like markdown links
- These are intentionally formatted as code blocks to avoid MkDocs warnings
- Do not modify the markdown linting disable comment at the top of regex.md
