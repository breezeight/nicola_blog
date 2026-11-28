# nik-kh — Nicola's Knowledge Hub

Personal knowledge base built with [Zensical](https://zensical.org/) and published, behind
Cloudflare Access, at <https://nik-kh.pages.dev>.

## Just cloned this repo?

| I want to… | Go to |
|---|---|
| Run the site locally | `just install && just serve`, then open <http://localhost:8000>. Details in [DEVELOPMENT.md](DEVELOPMENT.md) |
| Write or edit a page | [CONTENT.md](CONTENT.md): the content rules (Diátaxis, structure, linking) |
| Work with an AI agent (Claude Code, Codex, Cursor) | [AGENTS.md](AGENTS.md): agent instructions, skills, MCP servers to connect |
| Change tooling, CI or deployment | [DEVELOPMENT.md](DEVELOPMENT.md), then a spec with Spec Kit (`/speckit-specify`) |
| Deploy | Push to `main`: GitHub Actions builds and deploys. See [DEVELOPMENT.md § Deployment](DEVELOPMENT.md#deployment) |

## What's where

| Path | Contents |
|---|---|
| [docs/](docs/) | The site content; [docs/index.md](docs/index.md) is the home page |
| [mkdocs.yml](mkdocs.yml) | Site configuration and navigation (read by Zensical) |
| [main.py](main.py) | Macros available in pages (`github_code_ref`) |
| [justfile](justfile) | Commands: `serve`, `build`, `check-strict`, `deploy`, … |
| [.specify/memory/constitution.md](.specify/memory/constitution.md) | Non-negotiable project principles |
| [specs/](specs/) | Spec Kit feature specs, plans and tasks |
| `.agents/skills/`, `.claude/skills/` | Agent skills (see [AGENTS.md](AGENTS.md)) |
| `.githooks/`, `.github/workflows/` | Pre-commit strict build and CI/deploy |

## Task tracking

Personal tasks (including learning) live in ClickUp; Addictive work lives in
[Linear](https://linear.app/addictivedev/settings/teams/NBP). The two are never mixed; see
[AGENTS.md](AGENTS.md).

## Editing tips

- Images and VS Code setup: [docs/dev/markdown-editing-tools.md](docs/dev/markdown-editing-tools.md).
- Moving a page and updating its links: [ad-internal-docs-cli](https://github.com/addictivedev/ad-internal-docs-cli);
  run `just check-strict` afterwards.
