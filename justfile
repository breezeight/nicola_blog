# Justfile for Nicola's Blog MkDocs project with uv

# Default recipe - show available commands
default:
    @just --list

# Install dependencies
install:
    uv sync

# Start development server
serve port="8000":
    uv run mkdocs serve --dev-addr=127.0.0.1:{{port}}

# Start development server on all interfaces (for external access)
serve-external:
    uv run mkdocs serve --dev-addr=0.0.0.0:8001

# Build the documentation site
build:
    uv run mkdocs build --clean

# Build and serve (useful for testing production build)
build-serve:
    uv run mkdocs build --clean
    uv run mkdocs serve --dev-addr=127.0.0.1:8001

# Update dependencies to latest versions
update:
    uv sync --upgrade

# Show dependency information
deps:
    uv pip list

# Clean build artifacts
clean:
    rm -rf site/

# Format and validate configuration (non-strict)
check:
    uv run mkdocs build

# Strict validation (shows all warnings and errors)
check-strict:
    uv run mkdocs build --strict

# Deploy to GitHub Pages (if configured)
deploy:
    uv run mkdocs gh-deploy

# Run macros to generate dynamic content
macros:
    uv run python main.py

# Full development workflow: install, generate macros, and serve
dev port="8000":
    uv sync
    uv run python main.py
    uv run mkdocs serve --dev-addr=127.0.0.1:{{port}}
