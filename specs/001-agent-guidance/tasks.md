# Tasks: Agent Guidance and Skills

**Input**: Design documents from `specs/001-agent-guidance/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: No automated test tasks (not requested). Validation is `just check-strict`, `grep`
checks and the manual scenarios in quickstart.md.

## Phase 1: Setup

- [X] T001 Create folders `guidelines/content/` and `guidelines/site/` (plan.md, Project Structure)

## Phase 2: Foundational

No blocking prerequisites beyond Setup.

## Phase 3: User Story 1 - Any agent follows the same content rules (P1) 🎯 MVP

**Goal**: rules live in `guidelines/`, Cursor keeps working through pointers, every agent is
directed to them.

**Independent Test**: quickstart.md §1–3.

- [X] T002 [US1] `git mv` each rule to its new path per the mapping in data-model.md (Content rule.path), e.g. `.cursor/rules/content-guidelines-diataxis.mdc` → `guidelines/content/diataxis.md`, and strip Cursor front matter from the moved files
- [X] T003 [US1] Fix cross-references inside `guidelines/**/*.md`: replace `mdc:.cursor/rules/...` links with relative links to the new files and remove references to the non-existent `content-guidelines-master.mdc` (research.md R3)
- [X] T004 [P] [US1] Retitle `guidelines/site/zensical.md` and `guidelines/site/theme-customization.md` for Zensical; mark the `custom_dir`/overrides section of theme-customization as not yet verified with Zensical (research.md R3)
- [X] T005 [US1] Recreate Cursor pointer rules in `.cursor/rules/*.mdc` with the original front matter (`description`, `globs`, `alwaysApply`) and an `@guidelines/...` reference (data-model.md Content rule.cursor pointer; research.md R2); convert `content-guidelines-general.md` to a proper `.mdc` with `globs: docs/**/*.md`; keep `nicola-routines/RULE.md` as pointer
- [X] T006 [P] [US1] Delete `.cursor/rules/clickup-integration.mdc` and `.cursor/clickup-config.json` (FR-011)
- [X] T007 [P] [US1] Replace the three `mdc:` links in `docs/index.md` (lines ~142–144) with GitHub links to `guidelines/content/...` (research.md R4)
- [X] T008 [US1] Rewrite `CONTENT.md` as the single index: every file in `guidelines/` listed once with an accurate one-line summary and scope (data-model.md Content rule.title, Content rule.scope, Content rule.summary); linking described as plain Markdown links
- [X] T009 [US1] Update the project structure tree and rule references in `DEVELOPMENT.md` (`.cursor/rules/` → `guidelines/` + Cursor pointers)
- [X] T010 [US1] Add a "Project guidance" section to `AGENTS.md` pointing to `.specify/memory/constitution.md`, `CONTENT.md`, `DEVELOPMENT.md` and `guidelines/`
- [X] T011 [US1] Run `just check-strict` and the `grep` check from quickstart.md §1; fix any reference left

**Checkpoint**: US1 complete; commit "docs: move agent rules to guidelines/ with Cursor pointers".

## Phase 4: User Story 2 - Create a personal learning task (P2)

**Goal**: `clickup-learning-task` skill shared by Claude Code and Codex.

**Independent Test**: quickstart.md §4–5.

- [X] T012 [US2] Write `.agents/skills/clickup-learning-task/SKILL.md` in English implementing contracts/clickup-learning-task.md (trigger, flow, status changes, description template, error cases) with list facts from research.md R7 and field rules from data-model.md (Learning task.name, Learning task.🎯 Motivation, Learning task.description, Learning task.status, Learning task.Main Area, Learning task.Impact/Reach/Planning/Deadline/priority/start date/due date, Learning task.RICE Index), including the field meanings (Deadline = hard deadline; start → due = execution window)
- [X] T013 [US2] Create the relative symlink `.claude/skills/clickup-learning-task` → `../../.agents/skills/clickup-learning-task` (data-model.md Skill.claude link; research.md R5)
- [X] T014 [US2] Verify Claude Code lists the skill in a fresh session (`claude -p`); if symlinks are not followed, apply the R5 fallback (copy + `just sync-skills` recipe in `justfile.zensical`)

**Checkpoint**: commit "feat: add clickup-learning-task skill for Claude Code and Codex".

## Phase 5: User Story 3 - Set up a new machine or agent (P3)

**Goal**: one place documents MCP servers and skills.

**Independent Test**: quickstart.md §4, §6.

- [X] T015 [US3] Extend "Project guidance" in `AGENTS.md` with skill locations (`.agents/skills/` source, `.claude/skills/` symlinks, `speckit-*` managed by Spec Kit) and the MCP server table (data-model.md MCP server entry.name, .endpoint, .purpose, .used by, .boundary): ClickUp = personal, Linear = Addictive work, never mixed
- [X] T016 [US3] Add "AI agents setup" to `DEVELOPMENT.md`: connect ClickUp in Claude Code (claude.ai connector or `/mcp`) and Codex (`codex mcp add clickup --url https://mcp.clickup.com/mcp`, `codex mcp login clickup`), and how to add a skill (research.md R5, R6)

## Phase 6: User Story 4 - Constitution covers content classification (P3)

- [X] T017 [US4] Amend `.specify/memory/constitution.md` to v1.1.0: add principle VI (Diátaxis: every page is one of tutorial, how-to, reference, explanation, see `guidelines/content/diataxis.md`), replace `.cursor/rules/` with `guidelines/` in Governance, update Last Amended date and remove the Sync Impact Report comment before commit

## Phase 7: Polish

- [ ] T018 Run quickstart.md §1–7 that can be checked locally; record results; `just check-strict`
- [ ] T019 Commit remaining changes (README, specs, AGENTS, DEVELOPMENT, constitution) and push `spec-kit-setup`

## Dependencies

- T001 → T002 → T003/T004 → T005 → T008–T011
- T006, T007 independent of T003–T005
- US2 (T012–T014) independent of US1, but T015 references the skill
- T017 after T002 (cites new path)
- T018–T019 last

## Parallel examples

- US1: T004, T006, T007 together after T002.
- US2 and US4 can proceed in parallel with US1's documentation tasks (T008–T010).

## Implementation strategy

MVP = US1 (rules visible to every agent). Then US2 (skill), US3 (setup docs), US4 (constitution),
committing at each checkpoint.
