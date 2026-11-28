# Implementation Plan: Agent Guidance and Skills

**Branch**: `spec-kit-setup` | **Date**: 2026-11-27 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/001-agent-guidance/spec.md`

## Summary

Move the content and site rules from `.cursor/rules/` to a tool-neutral `guidelines/` folder,
leaving thin Cursor pointer rules so Cursor behaves as before. Make `CONTENT.md` the single rule
index and `README.md` a short orientation page. Add agent-facing guidance (constitution, rules,
skills, MCP servers) to `AGENTS.md` and setup steps to `DEVELOPMENT.md`. Add a
`clickup-learning-task` skill with one source in `.agents/skills/` and a symlink for Claude Code.
Remove the obsolete Cursor ClickUp configuration and amend the constitution to v1.1.0 with a
Diátaxis principle.

## Technical Context

**Language/Version**: Markdown (rules, docs, skills); YAML front matter for Cursor rules and skills

**Primary Dependencies**: Zensical (strict build), Claude Code skills, Codex skills
(`codex-cli 0.166.0`), Cursor rules (`.mdc` with `@file` references), ClickUp MCP
(`https://mcp.clickup.com/mcp`)

**Storage**: Files in the repository; tasks in ClickUp list `901519460495`

**Testing**: `just check-strict` (0 warnings); `grep` checks for stale references; manual agent
checks in [quickstart.md](quickstart.md)

**Target Platform**: macOS developer machine; GitHub Actions for the build

**Project Type**: Documentation repository with agent configuration

**Performance Goals**: N/A

**Constraints**: Rules outside `docs/` (not published); no secrets in the repo; symlink support
for Claude Code skills to be verified (R5)

**Scale/Scope**: 9 rule files moved, 1 deleted, 1 skill added, 5 top-level docs updated

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Check | Result |
|---|---|---|
| I. Portable plain-Markdown content | Rules become plain `.md`; the three `mdc:` links in `docs/index.md` become normal links | Pass |
| II. Strict build always green | `just check-strict` after every step; `guidelines/` is outside `docs/` | Pass |
| III. Private by default | No secrets added; ClickUp/Codex use OAuth outside the repo; nothing deployed | Pass |
| IV. Reproducible, minimal tooling | No new dependencies; one optional fallback `just` recipe only if symlinks fail | Pass |
| V. Process proportional to change | Structure change handled through Spec Kit | Pass |

Post-design re-check: no violations; Complexity Tracking not needed.

## Project Structure

### Documentation (this feature)

```text
specs/001-agent-guidance/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/clickup-learning-task.md
├── checklists/requirements.md
└── tasks.md             # /speckit-tasks
```

### Source Code (repository root)

```text
guidelines/
├── content/
│   ├── general.md
│   ├── diataxis.md
│   ├── linking.md
│   ├── language-structure.md
│   ├── cross-language.md
│   ├── typescript-docs.md
│   └── routines.md
└── site/
    ├── zensical.md
    └── theme-customization.md

.cursor/rules/            # thin pointers: front matter + @guidelines/... (clickup rule deleted)
.cursor/clickup-config.json   # deleted

.agents/skills/clickup-learning-task/SKILL.md      # source
.claude/skills/clickup-learning-task -> ../../.agents/skills/clickup-learning-task

AGENTS.md          # + Project guidance, skills, MCP table
CONTENT.md         # single rule index
DEVELOPMENT.md     # + AI agents setup; structure tree updated
README.md          # orientation page (done)
docs/index.md      # rule links → GitHub URLs
.specify/memory/constitution.md   # v1.1.0, principle VI Diátaxis, guidance paths
```

**Structure Decision**: rules move to `guidelines/` (see [research.md](research.md) R1–R4); skill
layout per R5; MCP setup per R6; skill behaviour per
[contracts/clickup-learning-task.md](contracts/clickup-learning-task.md).

## Implementation order

1. `git mv` rules to `guidelines/`, fix internal cross-references and remove the
   `content-guidelines-master.mdc` references; retitle site rules for Zensical.
2. Recreate `.cursor/rules/*.mdc` as pointers; delete ClickUp rule and config.
3. Update `docs/index.md`, `CONTENT.md`, `DEVELOPMENT.md` tree; run `just check-strict`.
4. Write the skill and the symlink; verify in a fresh Claude Code session.
5. `AGENTS.md` and `DEVELOPMENT.md` sections.
6. Constitution v1.1.0.
7. Quickstart validation; commit per logical step.
