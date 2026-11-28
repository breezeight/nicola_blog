---
name: clickup-learning-task
description: Create, update or change the status of Nicola's personal learning tasks in the ClickUp list "Nicola Learning". Use when the user asks to create a learning task, add a topic to study to the learning list, update a learning task, or mark one as backlog/todo/on-hold/wip/closed. Do not use for Addictive company work (that goes to Linear) or for personal tasks that are not about learning (ask which list).
---

# ClickUp learning task

Create and maintain tasks in Nicola's personal learning list in ClickUp, from Claude Code or Codex.
Everything you write in ClickUp (name, Motivation, description) is in **English**.

## Target

| Item | Value |
|---|---|
| Workspace | `2194902` |
| Space | Nicola Personal |
| List | **Nicola Learning**, id `901519460495` (https://app.clickup.com/2194902/v/li/901519460495) |
| Statuses | `backlog` (default for new tasks), `todo`, `on-hold`, `wip`, `Closed` |

If the list cannot be found (renamed, moved, no access), report it and ask. Never create the task
in another list.

## Ground rules

- **Explicit request only.** Create or change tasks only when the user asks. While working on
  something else you may *suggest* a learning task (e.g. an unfinished topic in the docs), but do
  not create it.
- **Always confirm.** Show a preview and wait for an explicit "yes" before any create, update,
  status change or new dropdown option.
- **Never guess values.** Optional fields are set only with values the user confirmed.
- **Personal vs. company.** Addictive work never goes to ClickUp: say it belongs to Linear and stop.
  A personal task that is not about learning: ask which ClickUp list to use.
- **No back-links in the docs.** Do not edit pages in `docs/` to link the task, unless the user
  agrees for that specific task.
- **ClickUp not connected?** If the ClickUp MCP tools are not available, tell the user how to
  connect (Claude Code: `/mcp` → *claude.ai ClickUp*; Codex: `codex mcp login clickup`) and stop.
  Do not fall back to another tracker.

## Fields

| Field | Type | Rule |
|---|---|---|
| Task name | — | The **topic only**, e.g. `Go generics`, `Elixir OTP supervision`. No prefixes like "Learn:" |
| 🎯 Motivation | short text | Why Nicola wants to learn it, 1–2 lines. Ask if the conversation does not make it clear |
| Description | Markdown | Template below: resources, knowledge-base page, expected output |
| Status | status | New tasks: list default (`backlog`). Changes only on request |
| Main Area | dropdown | Propose the best existing option (see below) |
| Impact | dropdown `3`, `2`, `1`, `0.5`, `0.25` | Ask whether to fill |
| Reach | number | Ask whether to fill |
| Planning | dropdown `1d`, `7d`, `30d` | Ask whether to fill; do not set it otherwise |
| Deadline | date | Ask whether to fill. **Meaning: a hard deadline by which the task must be completed** |
| Priority | native | Ask whether to fill |
| Start date → Due date | native | Ask whether to fill. **Meaning: the planned execution time range of the task** |
| RICE Index | formula | Never set; ClickUp computes it |

For the "ask whether to fill" fields: list them in one question after the preview. When the
conversation suggests a value, propose it marked as a suggestion and say why, e.g.
`Deadline: 2026-12-15 (suggested: you mentioned mid-December)`. Leave every unconfirmed field empty.

### Main Area

Existing options: `ai`, `dev/architecture`, `devops/aws`, `devops/linux`, `devops/nix`,
`devops/pulumi`, `devops/security`, `devops/terraform`, `management/project`,
`opensource-ecosystem`, `programming/js-ts`, `programming/python`, `programming/rust`.
Read the live options with the custom-fields tool before proposing, since they can change.

- Pick from the topic and the related page path (e.g. `docs/dev/python/...` → `programming/python`,
  `docs/dev/nix/...` → `devops/nix`, `docs/dev/ai/...` → `ai`).
- If nothing fits, you may propose a **new option** named like the existing ones (`area/topic`,
  lowercase, e.g. `programming/go`, `programming/elixir`). A new option changes the field for the
  whole list, so add it only after explicit confirmation. If declined, leave the field empty.

### Description template

```markdown
## Resources
- <link or reference, one per line>

## Knowledge base
- Page: `docs/<path>.md` — https://nik-kh.pages.dev/<path>/

## Expected output
- <what will exist when the task is done, e.g. "New section in docs/dev/go/go-index.md">
```

Omit a section only if it would be empty. The site URL is the page path without `docs/` and
`.md`, with a trailing slash (`docs/dev/go/go-index.md` → `https://nik-kh.pages.dev/dev/go/go-index/`).

## Create a task

1. **Classify** the request (learning / other personal / company), per the ground rules.
2. **Check for duplicates**: search the list for a similar topic, going through **all result pages**
   and **including closed tasks** (the list has 100+ tasks). If you find one, show it as a link and
   offer: update it, create a new one anyway, or cancel.
3. **Show the preview** under the heading **ClickUp task preview**. Use this Markdown table and
   include every row. Replace placeholders with the proposed values. Use **Blank** for a field
   that will be left empty, **Unavailable** for a field that is unavailable in ClickUp, and
   **Calculated by ClickUp** for the RICE Index.

   | Field | Proposed value |
   |---|---|
   | Task name | <topic> |
   | List | Nicola Learning |
   | Status | backlog |
   | 🎯 Motivation | <motivation> |
   | Description | Shown in full below |
   | Main Area | <proposed option> |
   | Impact | Blank |
   | Reach | Blank |
   | Planning | Blank |
   | Deadline | Blank |
   | Priority | Blank |
   | Start date | Blank |
   | Due date | Blank |
   | RICE Index | Calculated by ClickUp |

   Show the full formatted description below the table before asking for confirmation.
4. **Ask about optional fields** (Impact, Reach, Planning, Deadline, priority, start/due date), with
   suggestions where the conversation implies a value.
5. **Wait for confirmation**, then create the task with the confirmed values only.
6. **Report** the task as a Markdown link: `[Go generics](https://app.clickup.com/t/<id>)`.

## Update a task or change its status

The owner can change tasks and statuses directly in ClickUp; you can too, when asked.

1. Find the task in the list (ask if several match).
2. Show the change: `field: current → new` (e.g. `status: todo → wip`).
3. Apply it after confirmation and report the task link.

Never change a status on your own initiative. Do not rename existing tasks to English unless asked.

## Errors

| Case | What to do |
|---|---|
| ClickUp tools unavailable | Explain how to connect; stop |
| List not found | Report it; ask; do not create elsewhere |
| No fitting Main Area | Propose a new option (needs confirmation) or leave empty |
| Create/update fails | Show the error message; do not retry silently |
