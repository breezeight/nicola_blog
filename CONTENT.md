# Content Guidelines

The single index of the rules for writing and maintaining this knowledge base. The rules live in
[guidelines/](guidelines/) as plain Markdown, so every agent (Claude Code, Codex, Cursor) and every
editor reads the same files. Cursor loads them through thin pointer rules in `.cursor/rules/`.

The non-negotiable principles are in the
[constitution](.specify/memory/constitution.md); these guidelines explain how to apply them.

## Writing pages

| Rule | Applies to | Summary |
|---|---|---|
| [Diátaxis](guidelines/content/diataxis.md) | All pages, mainly `docs/dev/` | Classify every page as tutorial, how-to, reference or explanation, and write it accordingly |
| [General](guidelines/content/general.md) | All pages | Folder layout, file naming, Markdown formatting |
| [Linking](guidelines/content/linking.md) | All pages, `main.py`, `mkdocs.yml` | Plain relative Markdown links; index entries as `[Title](page.md): abstract`; available macros |
| [Dev notes](guidelines/content/dev-notes.md) | `docs/dev/` | Code examples, commands and technical writing standards |

## Programming languages

| Rule | Applies to | Summary |
|---|---|---|
| [Language structure](guidelines/content/language-structure.md) | `*-index.md` language references | The standard 18-section structure of a language reference |
| [Cross-language](guidelines/content/cross-language.md) | Language references and the cross-language comparison | Coordinates the language rules; keeps comparison tables consistent |
| [TypeScript docs](guidelines/content/typescript-docs.md) | `docs/dev/javascript/` TypeScript pages | Structure and scope of the advanced TypeScript guide |

## Specific areas

| Rule | Applies to | Summary |
|---|---|---|
| [Ansible](guidelines/content/ansible.md) | `docs/dev/ansible*.md` | Main guide vs. tutorials and how to keep them in sync |
| [Routines](guidelines/content/routines.md) | `docs/nicola-routines/` | Architecture, personas and maintenance of Nicola's routines |

## Site tooling

| Rule | Applies to | Summary |
|---|---|---|
| [Zensical site](guidelines/site/zensical.md) | `mkdocs.yml`, `justfile*`, `pyproject.toml` | uv for packages, `just` for commands, Zensical workflow |
| [Theme customization](guidelines/site/theme-customization.md) | `docs/stylesheets/`, theme settings | CSS and JavaScript customization; theme overrides not yet verified with Zensical |

## Adding or changing a rule

1. Write it as a plain Markdown file in `guidelines/content/` or `guidelines/site/`.
2. Add one row to the right table above.
3. For Cursor, add `.cursor/rules/<name>.mdc` with the front matter (`description`, `globs`,
   `alwaysApply`) and a single line `@guidelines/<folder>/<file>.md`.
4. Run `just check-strict` if pages changed.
