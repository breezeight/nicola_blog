# Data Model: Agent Guidance and Skills

## Content rule

| Attribute | Description |
|---|---|
| path | `guidelines/content/<name>.md` or `guidelines/site/<name>.md` |
| title | First heading of the file |
| scope | Which pages it applies to (all pages, `docs/dev/**`, language pages, `docs/nicola-routines/**`) |
| summary | One line, used in `CONTENT.md` |
| cursor pointer | `.cursor/rules/<original-name>.mdc` with front matter + `@path` |

Validation: listed exactly once in `CONTENT.md`; every `CONTENT.md` entry resolves to a file.

Mapping (old → new):

| Old (`.cursor/rules/`) | New |
|---|---|
| `content-guidelines-general.md` | `guidelines/content/general.md` |
| `content-guidelines-diataxis.mdc` | `guidelines/content/diataxis.md` |
| `content-guidelines-linking.mdc` | `guidelines/content/linking.md` |
| `content-guidelines-language-structure.mdc` | `guidelines/content/language-structure.md` |
| `content-guidelines-cross-language.mdc` | `guidelines/content/cross-language.md` |
| `content-guidelines-typescript-docs.mdc` | `guidelines/content/typescript-docs.md` |
| `nicola-routines/RULE.md` | `guidelines/content/routines.md` |
| `mkdocs.mdc` | `guidelines/site/zensical.md` |
| `mkdocs-theme-customization.mdc` | `guidelines/site/theme-customization.md` |
| `docs/.cursor/rules/ansible-notes.mdc` | `guidelines/content/ansible.md` |
| `docs/.cursor/rules/dev-notes.mdc` | `guidelines/content/dev-notes.md` |
| `docs/.cursor/rules/dev-notes-index.mdc` | deleted (empty) |
| `clickup-integration.mdc` | deleted (replaced by skill) |

## Skill

| Attribute | Description |
|---|---|
| name | kebab-case, equals folder name |
| description | Trigger text used by agents to decide when to load it |
| source | `.agents/skills/<name>/SKILL.md` |
| claude link | `.claude/skills/<name>` → `../../.agents/skills/<name>` |
| uses MCP | e.g. ClickUp |

## MCP server entry (AGENTS.md table)

| Attribute | Example |
|---|---|
| name | ClickUp |
| endpoint | `https://mcp.clickup.com/mcp` |
| purpose | Personal area: learning tasks |
| used by | `clickup-learning-task` |
| boundary | Personal only; Addictive work goes to Linear |

## Learning task (ClickUp)

| Field | Rule |
|---|---|
| list | `901519460495` (Nicola Learning) |
| name | Topic only, English |
| 🎯 Motivation | Why, 1–2 lines |
| description | Resources; knowledge-base page (repo path + `https://nik-kh.pages.dev/...`); expected output |
| status | List default (`backlog`) |
| Main Area | Proposed by agent from existing options; if none fits, agent may propose a new option (`area/topic`, lowercase), added only after the owner confirms; else empty |
| Impact, Reach, Planning, Deadline, priority, start date, due date | Agent asks whether to fill them; may suggest values the conversation implies, clearly marked as suggestions; sets only confirmed values |
| RICE Index | Never set (formula) |

Meanings: **Deadline** = hard deadline by which the task must be completed; **start date → due
date** = planned execution window.

State transitions (`backlog` → `todo` → `wip` → `Closed`, plus `on-hold`) can be managed by both
the owner in ClickUp and the agent. The agent changes a status when the owner asks (e.g. "mark Go
generics as wip", "close it"), showing the change and confirming before applying it like any other
update.
