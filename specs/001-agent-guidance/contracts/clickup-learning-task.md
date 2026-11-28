# Contract: `clickup-learning-task` skill

## Trigger

- Explicit: `/clickup-learning-task` (Claude Code), `$clickup-learning-task` (Codex), or a request
  such as "create a learning task for X", "add X to my learning list".
- Never triggered to create a task on the agent's own initiative. The agent may *suggest* running
  it when it notices an unfinished topic.

## Inputs

| Input | Required | Source |
|---|---|---|
| topic | yes | user request |
| motivation | yes (asked if missing) | user / conversation |
| resources | no | user / conversation |
| related page | no | current file or topic → `docs/...md` |
| expected output | no (proposed by agent) | e.g. "Update docs/dev/go/go-index.md" |
| Impact, Reach, Planning, Deadline, priority, start/due date | no | agent asks whether to fill them; may suggest values implied by the conversation, marked as suggestions; only confirmed values are set |

## Flow

1. **Classify**: company work → stop, point to Linear. Personal non-learning → ask which list.
2. **Check connection**: ClickUp tools available? If not → tell the user to connect (`/mcp` or
   `codex mcp login clickup`) and stop. No fallback tracker.
3. **Duplicate search**: search list `901519460495` (all pages, closed included) for a similar
   topic. If found → show it and offer: update it / create anyway / cancel.
4. **Preview**: show a Markdown table headed **ClickUp task preview** with one row each for Task
   name, List, Status, 🎯 Motivation, Description, Main Area, Impact, Reach, Planning, Deadline,
   Priority, Start date, Due date, and RICE Index. Use **Blank** for fields that will be left
   empty, **Unavailable** for fields unavailable in ClickUp, and **Calculated by ClickUp** for
   RICE Index. Use **Shown in full below** in the Description row and show the full formatted
   description below the table. Then ask whether to fill
   Impact, Reach, Planning, Deadline, priority and start/due date, listing any values the
   conversation suggests as *suggested* (e.g. "Deadline: 2026-12-15 — suggested, you mentioned
   mid-December"). Unconfirmed suggestions are left empty.
5. **Confirm**: create or update only after explicit confirmation.
6. **Report**: the task as a Markdown link `[Topic](https://app.clickup.com/t/<id>)`.

## Status changes

The agent can move a learning task between the list statuses (`backlog`, `todo`, `on-hold`, `wip`,
`Closed`) when the user asks, e.g. "mark Go generics as wip" or "close it". It finds the task,
shows current → new status, and applies the change after confirmation. The owner can also change
statuses directly in ClickUp; the agent never changes a status on its own initiative.

## Output rules

- All text in English.
- Description template:

  ```markdown
  ## Resources
  - <link or reference>

  ## Knowledge base
  - Page: `docs/<path>.md` — https://nik-kh.pages.dev/<path>/

  ## Expected output
  - <what will exist when done>
  ```

- No edits to documentation pages (no back-link) unless agreed with the user for that task.

## Error cases

| Case | Behaviour |
|---|---|
| ClickUp not connected | Explain how to connect; stop |
| List not found (renamed/moved) | Report; ask the user; do not create elsewhere |
| Main Area has no fitting option | Propose a new option named like the existing ones (`area/topic`, lowercase, e.g. `programming/go`); add it to the field only after explicit confirmation (it changes the list for all tasks); if declined, leave empty |
| Create/update fails | Show the error; do not retry silently |
