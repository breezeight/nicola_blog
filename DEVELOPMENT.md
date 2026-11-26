# Development Guide

This documentation site is built with [MkDocs](https://www.mkdocs.org/) and the [Material](https://squidfunk.github.io/mkdocs-material/) theme. Python dependencies are managed with [uv](https://docs.astral.sh/uv/), and common tasks run through [just](https://github.com/casey/just).

## Prerequisites

- Python 3.12+
- uv
- just (optional, for convenience commands)

## Setup

```bash
just install   # same as: uv sync
```

## Running the Site

```bash
just serve              # http://127.0.0.1:8000
just serve 8080         # custom port
just serve-external     # listen on 0.0.0.0:8001 (reachable from other devices)
just dev                # uv sync + run macros + serve
```

## Building and Validating

```bash
just build          # uv run mkdocs build --clean
just check          # build and show warnings
just check-strict   # build with --strict (fails on warnings, e.g. broken links)
just build-serve    # build, then serve the production build on port 8001
just clean          # remove site/
```

Run `just check-strict` before committing larger changes to catch broken links and nav entries pointing to moved files.

## Available Just Commands

The root `justfile` imports `justfile.mkdocs`, which holds the MkDocs recipes. Run `just` with no arguments to list them all.

| Command | What it does |
|---------|--------------|
| `just install` | Install Python dependencies (`uv sync`) |
| `just serve [port]` | Start the development server |
| `just serve-external` | Start the server on all interfaces |
| `just build` | Build the site into `site/` |
| `just build-serve` | Build and serve the production build |
| `just check` / `just check-strict` | Validate the build |
| `just update` | Upgrade dependencies (`uv sync --upgrade`) |
| `just deps` | Show installed Python packages |
| `just clean` | Remove build artifacts |
| `just macros` | Run `main.py` |
| `just dev [port]` | Install, run macros and serve |
| `just deploy` | Deploy to GitHub Pages (`mkdocs gh-deploy`) |

## Configuration

- **`mkdocs.yml`** — site configuration, theme, Markdown extensions, plugins and the `nav` tree. When you move or rename a page, update its `nav` entry too.
- **`.mkdocsignore`** — legacy files excluded from the build.
- **`pyproject.toml`** / **`uv.lock`** — Python dependencies.

Enabled plugins:

- `search`
- `tags` — tags from page front matter, listed on [docs/tags.md](docs/tags.md)
- `gh-admonitions` — renders GitHub-style alerts (`> [!NOTE]`, `> [!WARNING]`, …) as Material admonitions
- `macros` — loads macros from `main.py`

## Macros

`main.py` defines macros available in any Markdown page:

- `link_with_abstract("path/to/page.md")` — renders a link to a page with the title and abstract from its front matter. The path is relative to the page that calls the macro.
- `github_code_ref(repo_path, start_line, end_line, language)` — embeds a code reference from a GitHub repository.

Example:

```markdown
- {{ link_with_abstract("dev/kubernetes/k8s-registry-auth-howto.md") }}
```

## Tags

Add tags in the page front matter:

```yaml
---
tags:
  - content/howto
  - tech/kubernetes
---
```

Tagged pages are listed on the [Tags](docs/tags.md) page.

## Project Structure

```
.
├── docs/                 # Documentation source (Markdown)
│   ├── dev/              # Technical notes, grouped by topic (aws/, kubernetes/, nix/, ...)
│   ├── nicola-routines/  # Personal routines system
│   ├── images/           # Images
│   ├── stylesheets/      # extra.css
│   ├── index.md          # Home page
│   └── tags.md           # Tags index
├── .cursor/rules/        # Cursor rules (content guidelines, MkDocs conventions)
├── main.py               # MkDocs macros
├── mkdocs.yml            # MkDocs configuration
├── justfile              # Entry point, imports justfile.mkdocs
├── justfile.mkdocs       # MkDocs recipes
├── pyproject.toml        # Python dependencies
└── site/                 # Generated site (build output)
```

## Contributing Content

Follow the content guidelines listed in [CONTENT.md](CONTENT.md). In short:

1. Classify each page using the Diátaxis framework (tutorial, how-to, reference, explanation) and name it accordingly (for example `*-howto.md`, `*-explanation.md`).
2. Use GitHub Flavored Markdown and GitHub-style alerts.
3. Add the page to `nav` in `mkdocs.yml` when it should appear in the navigation.
4. Preview with `just serve` and validate with `just check-strict`.

## Deployment

```bash
just deploy
```

This runs `mkdocs gh-deploy`, which builds the site and pushes it to the `gh-pages` branch.
