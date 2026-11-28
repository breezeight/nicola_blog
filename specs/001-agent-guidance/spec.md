# Feature Specification: Agent Guidance and Skills

**Feature Branch**: `spec-kit-setup` (spec directory `001-agent-guidance`)

**Created**: 2026-11-27

**Status**: Draft

**Input**: User description: "Make the repository's guidance usable by every coding agent (Claude
Code, Codex, Cursor) from one source of truth: move content rules out of the Cursor-only folder,
make CONTENT.md the single index, document skills and MCP servers in AGENTS.md and
DEVELOPMENT.md, add a shared skill that creates personal learning tasks in ClickUp, remove the
obsolete Cursor ClickUp config, and add Diátaxis to the constitution."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Any agent follows the same content rules (Priority: P1)

The owner asks Claude Code, Codex or Cursor to write or edit a documentation page. Whichever agent
is used, it finds and applies the same content rules (Diátaxis classification, page structure,
linking, routines) without the owner having to point at them.

**Why this priority**: today the rules are visible only to Cursor; Claude and Codex silently ignore
them, so pages written with them drift from the guidelines.

**Independent Test**: start a fresh Claude Code or Codex session, ask "which rules apply when I
write a language reference page?", and check the agent cites the rule files without being told
where they are.

**Acceptance Scenarios**:

1. **Given** a fresh agent session in the repository, **When** the agent reads its entry
   instructions, **Then** it is directed to the constitution, the content-rule index and the
   development guide.
2. **Given** the content-rule index, **When** the owner follows each entry, **Then** every entry
   resolves to an existing rule file and every rule file is listed exactly once.
3. **Given** Cursor, **When** a page under `docs/` is edited, **Then** Cursor still applies the
   rules it applied before the move.

---

### User Story 2 - Create a personal learning task from a conversation (Priority: P2)

While studying a topic or writing a page, the owner asks the agent to create a learning task. The
agent prepares the task, shows a preview, checks for an existing task on the same topic, and
creates it in the personal learning list only after confirmation. The same behaviour is available
in Claude Code and Codex.

**Why this priority**: it is the first concrete use of shared skills and of the ClickUp connection,
but the repository is usable without it.

**Independent Test**: in Claude Code and in Codex, ask "create a learning task for Go generics";
verify a preview appears, nothing is created before confirmation, and after confirmation exactly
one task appears in the learning list with the agreed fields.

**Acceptance Scenarios**:

1. **Given** the owner asks for a learning task, **When** the agent prepares it, **Then** it shows
   name, description and fields and waits for confirmation before creating anything.
2. **Given** a task with a similar topic already exists in the list, **When** the owner asks for a
   new one, **Then** the agent shows the existing task and offers to update it instead.
3. **Given** a request for a work-related (company) task, **When** the agent evaluates it, **Then**
   it declines to put it in the personal list and points to the company tracker.
4. **Given** a request for a personal task that is not about learning, **When** the agent
   evaluates it, **Then** it asks which list to use.
5. **Given** the agent notices an unfinished topic while editing docs, **When** no task was
   requested, **Then** it may suggest a task but does not create one.

---

### User Story 3 - Set up a new machine or agent (Priority: P3)

The owner sets up the repository on a new machine, or tries a new agent. A single section tells
which external services (MCP servers) must be connected, what each is for, where skills live and
how to add a new one.

**Why this priority**: setup happens rarely, but without documentation the knowledge lives only in
past conversations.

**Independent Test**: following only the development guide, connect the required services in a
new agent session and confirm the learning-task skill is listed.

**Acceptance Scenarios**:

1. **Given** the agent instructions, **When** the owner reads the services table, **Then** each
   service shows its purpose, the skill that uses it, and its usage boundary (personal vs.
   company).
2. **Given** the development guide, **When** the owner adds a new skill following it, **Then** the
   skill is available in both Claude Code and Codex from a single source file.

---

### User Story 4 - Constitution covers content classification (Priority: P3)

Plans and reviews check new pages against the Diátaxis classification, because it is a
constitutional principle and not only a style guide.

**Independent Test**: read the constitution and find a principle requiring every page to be one
Diátaxis type; version is 1.1.0.

**Acceptance Scenarios**:

1. **Given** the amended constitution, **When** a plan adds documentation pages, **Then** the plan's
   constitution check includes the Diátaxis principle.

### Edge Cases

- A rule file referenced by other files (README, index pages, other rules) is moved: every
  reference must be updated, and the strict site build must stay green.
- The ClickUp connection is not authenticated in the current session: the skill must say so and
  stop, not fall back to another tracker.
- The learning list is renamed or moved in ClickUp: the skill identifies it by ID, and the guide
  explains how to change it.
- A rule file is obsolete (refers to tools no longer used): it is updated or removed, never left
  listed as current.
- An agent that does not support skills or symlinks: the rules remain readable as plain files
  through the index.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Content rules MUST live in a single location readable by every supported agent; no
  rule may exist only in a tool-specific folder.
- **FR-002**: Cursor MUST keep applying the rules it applies today (same scopes and triggers).
- **FR-003**: `CONTENT.md` MUST be the single index of content rules, listing every rule once with
  an accurate one-line description; the description of linking MUST reflect plain Markdown links.
- **FR-004**: `README.md` MUST be a short orientation page: a "Just cloned this repo?" table
  mapping goals to the file to read, and a "What's where" table describing the main files and
  folders. It MUST link to `CONTENT.md` instead of repeating its list, and MUST no longer contain
  the TODOs about migrating tasks between ClickUp and Linear.
- **FR-005**: Rules describing tools no longer in use (e.g. theme customization for Material for
  MkDocs) MUST be updated to the current tooling or removed.
- **FR-006**: `AGENTS.md` MUST contain a "Project guidance" section pointing to the constitution,
  `CONTENT.md`, `DEVELOPMENT.md`, the skill locations, and a table of required MCP servers with
  purpose, using skill, and usage boundary.
- **FR-007**: The usage boundary MUST state: ClickUp is for the owner's personal area; Linear is
  for Addictive company work; the two are never mixed.
- **FR-008**: `DEVELOPMENT.md` MUST explain how to connect the MCP servers in Claude Code and in
  Codex, and how to add a skill so both agents see it from one source.
- **FR-009**: Project skills MUST have one source file each, shared by Claude Code and Codex;
  Spec Kit-managed skills are left as Spec Kit installs them.
- **FR-010**: A skill named `clickup-learning-task`, written in English, MUST create personal
  learning tasks in ClickUp list `901519460495` following these rules:
  - only on explicit request; the agent may propose a task but never create one unprompted;
  - always show a preview and wait for confirmation;
  - search the list for a similar task first and offer to update it;
  - task name is the topic only;
  - the "why" (1–2 lines) goes in the **🎯 Motivation** field; the description contains external
    resources, related knowledge-base page as repository path and site URL
    (`https://nik-kh.pages.dev/...`), and expected output;
  - status is the list default (`backlog`) at creation; afterwards status changes can be made
    both by the owner in ClickUp and by the agent on the owner's request (with confirmation);
  - **Main Area** is proposed by the agent from the topic and related page and shown in the
    preview; if no existing option fits, the agent may propose a new option following the
    existing naming (`area/topic`, lowercase, e.g. `programming/go`); the option is added to the
    field only after the owner confirms it, otherwise the field stays empty;
  - for **Impact**, **Reach**, **Planning**, **Deadline**, priority, start date and due date the
    agent asks the owner whether to fill them; when the conversation suggests a value it may
    propose it, marked as a suggestion, but never sets a value the owner has not confirmed;
    **RICE Index** is a formula and never set;
  - field meanings recorded in the skill: **Deadline**, when set, is a hard deadline by which the
    task must be completed; **start date → due date** is the planned execution time range;
  - no back-link from documentation pages to the task, unless decided case by case with the owner;
  - all task content in English;
  - non-learning personal tasks: ask which list; company tasks: refuse and point to Linear.
- **FR-011**: The obsolete Cursor ClickUp configuration (`.cursor/clickup-config.json`, list
  "Nicola Nix Config", and `.cursor/rules/clickup-integration.mdc`) MUST be removed.
- **FR-012**: The constitution MUST gain a Diátaxis principle and be versioned 1.1.0.
- **FR-013**: The strict site build MUST pass after all changes.

### Key Entities

- **Content rule**: a guideline document with a scope (all pages, a folder, a language) and a
  short description; listed once in the index.
- **Skill**: an instruction package with a name, a trigger description and steps; one source,
  visible to several agents.
- **MCP server entry**: a connected external service with name, purpose, using skill, and usage
  boundary.
- **Learning task**: a ClickUp task in the learning list with topic, description sections, status,
  and agreed custom fields.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of rule files are listed in `CONTENT.md`, and 0 rule files exist only in a
  tool-specific folder.
- **SC-002**: In a fresh session, both Claude Code and Codex name the applicable content rules for
  a docs edit without being told where they are.
- **SC-003**: Creating a learning task takes one request plus one confirmation, and produces
  exactly one task (0 duplicates) in the learning list.
- **SC-004**: 0 tasks are created without explicit confirmation across the acceptance scenarios.
- **SC-005**: A new machine can be set up for agents by following one documentation section, with
  no knowledge from past conversations.
- **SC-006**: The strict site build reports 0 warnings.

## Assumptions

- The ClickUp connection is the claude.ai connector (OAuth, owner's account); Codex connects to the
  same ClickUp MCP endpoint with its own login.
- The learning list ("Nicola Learning", space "Nicola Personal") was inspected on 2026-11-27:
  statuses backlog/todo/on-hold/wip/Closed; custom fields Motivation, Main Area, Impact, Reach,
  Planning, Deadline, RICE Index. It holds 100+ tasks, so duplicate search covers all pages,
  including closed tasks. Existing task names are not renamed to English.
- Cursor support for rules from a non-default folder (e.g. via pointer files or links) is decided in
  the plan; the requirement is only that Cursor's behaviour is unchanged.
- The owner's other projects and the global Cursor MCP configuration are out of scope.
- Linear is not connected in this repository's sessions; the skill only refers to it, it does not
  use it.
- All work stays on branch `spec-kit-setup`.
