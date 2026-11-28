# Quickstart: validate Agent Guidance and Skills

## Prerequisites

- Repository on branch `spec-kit-setup`, `just install` done.
- ClickUp connected in Claude Code (`/mcp` → claude.ai ClickUp) and, for Codex,
  `codex mcp add clickup --url https://mcp.clickup.com/mcp && codex mcp login clickup`.

## 1. Rules are in one place (US1, SC-001)

```bash
ls guidelines/content guidelines/site
grep -rn '\.cursor/rules' --exclude-dir={.git,site,.venv,specs} . | grep -v '^./.cursor/'   # expect no output
```

Every file in `guidelines/` appears once in `CONTENT.md`; every `CONTENT.md` link resolves.

## 2. Cursor pointers

Each `.cursor/rules/*.mdc` has front matter and an `@guidelines/...` reference to an existing file.
Open a `docs/dev/**` page in Cursor and check the rules panel lists the same rules as before.

## 3. Agents find the rules (SC-002)

Fresh session in Claude Code and in Codex: ask "Which rules apply when I write a language
reference page?". Expected: the answer cites `CONTENT.md` and `guidelines/content/...`.

## 4. Skill visible in both agents (US3, R5)

```bash
ls -l .claude/skills/clickup-learning-task      # symlink to ../../.agents/skills/clickup-learning-task
claude -p "List the names of the skills available in this project."   # includes clickup-learning-task
```

In Codex, `$clickup-learning-task` is offered.

## 5. Learning task flow (US2, SC-003, SC-004)

Ask: "Create a learning task for <a new topic>". Expect a preview table with every field listed
in the [ClickUp contract](contracts/clickup-learning-task.md) and the full description below it.
Check that the table distinguishes blank, unavailable, and calculated fields where applicable.
After you say "yes", verify exactly one task appears in Nicola Learning with status
`backlog`. Ask again for the same topic: the agent finds the existing task and offers to
update it. Ask for an Addictive work task: the agent declines and points to Linear.
Delete the test task afterwards.

## 6. Docs and constitution

- `README.md` has "Just cloned this repo?" and "What's where"; no ClickUp/Linear migration TODOs.
- `AGENTS.md` has "Project guidance" with the MCP table; `DEVELOPMENT.md` has "AI agents setup".
- Constitution version 1.1.0 with a Diátaxis principle.

## 7. Build

```bash
just check-strict   # 0 warnings
```
