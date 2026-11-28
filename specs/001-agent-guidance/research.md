# Research: Agent Guidance and Skills

All findings verified in the repository or with local CLIs on 2026-11-27.

## R1. Tool-neutral location for content rules

- **Decision**: plain Markdown files in a top-level `guidelines/` folder, grouped as
  `guidelines/content/` (rules for writing pages) and `guidelines/site/` (rules for the site
  tooling). File names drop the `content-guidelines-` prefix and the `.mdc` extension.
- **Rationale**: every agent can read plain Markdown; a top-level folder is outside `docs/`, so the
  rules are not published on the site and do not affect the strict build; short names make
  `CONTENT.md` easier to scan.
- **Alternatives considered**:
  - Keep `.cursor/rules/` as the source and point other agents at it: keeps a tool-specific folder
    as source of truth (violates FR-001).
  - `docs/guidelines/`: rules would be published as site pages and need front matter and nav.
  - `.agents/guidelines/`: hidden folder, unexpected for humans.

## R2. Keeping Cursor's behaviour (FR-002)

- **Decision**: each `.cursor/rules/*.mdc` stays as a thin pointer: the original front matter
  (`description`, `globs`, `alwaysApply`) plus a body that references the moved file with
  Cursor's `@path` file reference (e.g. `@guidelines/content/diataxis.md`).
- **Rationale**: scope and triggers live in the front matter, which only Cursor understands; the
  `@` reference makes Cursor include the shared file, so content is not duplicated.
- **Alternatives considered**: symlinks `.mdc → .md` (lose the Cursor front matter); copying content
  (two sources drift).
- **Note**: `content-guidelines-general.md` has non-standard front matter (`glob`, `auto-attach`) and
  a `.md` extension, so Cursor likely never applied it. Its pointer becomes a proper `.mdc` with
  `globs: docs/**/*.md`.

## R3. Obsolete or broken rules

- `mkdocs-theme-customization.mdc`: `mkdocs.yml` still declares `theme: name: material`, which
  Zensical renders with its Material-compatible theme, and `docs/stylesheets/extra.css` (257 lines)
  still uses `md-*` classes. **Decision**: keep, rename to `guidelines/site/theme-customization.md`,
  retitle for Zensical, and mark the `custom_dir`/overrides section as not yet verified with
  Zensical (no `overrides/` folder exists today).
- `mkdocs.mdc` (uv/just workflow): still accurate after the Zensical migration. **Decision**: move
  to `guidelines/site/zensical.md`.
- References to `content-guidelines-master.mdc` in two rules: found during implementation to be the
  former name of the cross-language rule (titled "Master Rules"). **Decision**: point them to
  `cross-language.md`.
- Found during implementation: three more Cursor rules in `docs/.cursor/rules/`
  (`ansible-notes.mdc`, `dev-notes.mdc`, and `dev-notes-index.mdc`, which only contained "dsadsa").
  **Decision**: move the first two to `guidelines/content/` with pointers in `.cursor/rules/`;
  delete the empty one.
- `clickup-integration.mdc` and `.cursor/clickup-config.json`: point at list "Nicola Nix Config".
  **Decision**: delete (FR-011); replaced by the `clickup-learning-task` skill.

## R4. References to moved rules

`grep` found references in: `CONTENT.md`, `DEVELOPMENT.md` (project structure tree),
`docs/index.md` (3 `mdc:` links, lines 142–144), `.cursor/rules/*` (cross-references between
rules), `.specify/memory/constitution.md` (Governance). **Decision**: update all of them.
`docs/index.md` is published, and pages cannot link outside `docs/`, so its three links point to the
files on GitHub (`https://github.com/breezeight/nik-kh/blob/develop/guidelines/...`).

## R5. One skill source for Claude Code and Codex

- **Decision**: source at `.agents/skills/<name>/SKILL.md` (Codex's project skill folder); Claude
  Code sees it through a relative symlink `.claude/skills/<name> → ../../.agents/skills/<name>`.
- **Rationale**: one file to edit; git stores symlinks; both folders are already used by Spec Kit.
- **Verified 2026-11-28**: a fresh `claude -p` session lists the symlinked skill, and
  `codex exec` lists it from `.agents/skills/`. The fallback (copy + `just sync-skills`) is not
  needed.
- Spec Kit skills (`speckit-*`) stay as Spec Kit installs them (separate copies per agent).

## R6. MCP setup per agent

- **Claude Code**: ClickUp is a claude.ai connector (`https://mcp.clickup.com/mcp`, OAuth). Connect
  in claude.ai Settings → Connectors, or `/mcp` in Claude Code (needed again when a session starts
  unauthenticated).
- **Codex** (`codex-cli 0.166.0`): `codex mcp add clickup --url https://mcp.clickup.com/mcp`, then
  `codex mcp login clickup` (OAuth). Not configured yet on this machine.
- **Linear**: listed for the usage boundary only; not used by any skill in this feature.

## R7. ClickUp list facts (for the skill)

List `901519460495` "Nicola Learning", workspace `2194902`, space "Nicola Personal".
Statuses: `backlog` (default), `todo`, `on-hold`, `wip`, `Closed`. Custom fields: 🎯 Motivation
(short text), Main Area (dropdown), Impact (dropdown 3/2/1/0.5/0.25), Reach (number), Planning
(dropdown 1d/7d/30d), Deadline (date), RICE Index (formula). 100+ tasks: duplicate search must page
through all results and include closed tasks.
