# Agent Instructions

These instructions apply to every coding agent working in this repository (Claude Code, Codex,
Cursor).

## Project guidance

Read these before changing anything:

| File | What it governs |
|---|---|
| [.specify/memory/constitution.md](.specify/memory/constitution.md) | Non-negotiable principles. Wins over everything else |
| [CONTENT.md](CONTENT.md) | Index of the content rules in [guidelines/](guidelines/). Read the rules that apply before writing or editing a page in `docs/` |
| [DEVELOPMENT.md](DEVELOPMENT.md) | Tooling, build, checks, deployment, agent setup |

- Changes to tooling, CI, deployment or site structure go through Spec Kit
  (`speckit-specify` → `speckit-plan` → `speckit-tasks` → `speckit-implement`). Content edits do not.
- `just check-strict` must pass before committing changes to `docs/`, `mkdocs.yml` or `main.py`.

## Skills

| Skill | Purpose | Uses |
|---|---|---|
| `clickup-learning-task` | Create or update personal learning tasks in ClickUp list "Nicola Learning" | ClickUp |
| `speckit-*` | Spec-driven development workflow (constitution, specify, plan, tasks, implement, …) | — |

- Source of project skills: `.agents/skills/<name>/SKILL.md` (read by Codex).
- Claude Code reads `.claude/skills/`, where project skills are symlinks to `.agents/skills/`.
- `speckit-*` skills are installed and updated by Spec Kit, separately in both folders; do not edit
  them by hand.

## MCP servers

| Server | Endpoint | Purpose | Used by | Boundary |
|---|---|---|---|---|
| ClickUp | `https://mcp.clickup.com/mcp` | Nicola's **personal** area: learning tasks and other personal tasks | `clickup-learning-task` | Personal only. Never put Addictive work here |
| Linear | `https://mcp.linear.app/mcp` | **Addictive** company work | — | Company only. Never put personal tasks here |

The two trackers are never mixed. If a request does not say which area it belongs to, ask.
How to connect the servers: [DEVELOPMENT.md § AI Agents Setup](DEVELOPMENT.md#ai-agents-setup).

## Session completion

**When ending a work session**, complete the steps below. Work is not complete until `git push` succeeds.

**Workflow:**

1. **File follow-ups** — Note anything that needs a later pass (issues, todos, or your tracker of choice).
2. **Run quality gates** (if code or tooling changed) — Tests, linters, builds as applicable.
3. **PUSH TO REMOTE**:
   ```bash
   git pull --rebase
   git push
   git status  # should show "up to date with origin"
   ```
4. **Clean up** — Clear stashes, prune remote branches if you use that workflow.
5. **Verify** — Changes committed and pushed.
6. **Hand off** — Short context for the next session if someone else continues the work.

**Rules:**

- Do not stop before `git push` when the goal was to land work on the remote.
- If push fails, fix and retry until it succeeds or you have a deliberate reason to stop.
