---
description: "Beads task tracking workflow and session completion protocol for AI agents"
globs: ["**/*"]
alwaysApply: true
---

# Beads Task Tracking Workflow

This project uses **bd** (beads) for issue tracking. All AI agents MUST follow these rules when working in this codebase.

## Quick Reference Commands

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --status in_progress  # Claim work
bd close <id>         # Complete work
bd sync               # Sync with git
```

## Session Completion Protocol (MANDATORY)

**CRITICAL: Work is NOT complete until `git push` succeeds.**

When ending a work session, you MUST complete ALL steps below:

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **PUSH TO REMOTE** - This is MANDATORY:
   ```bash
   git pull --rebase
   bd sync
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** - Clear stashes, prune remote branches
6. **Verify** - All changes committed AND pushed
7. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- Work is NOT complete until `git push` succeeds
- NEVER stop before pushing - that leaves work stranded locally
- NEVER say "ready to push when you are" - YOU must push
- If push fails, resolve and retry until it succeeds

## Beads Workflow Integration

This project uses [beads_viewer](https://github.com/Dicklesworthstone/beads_viewer) for issue tracking. Issues are stored in `.beads/` and tracked in git.

### Essential Commands

```bash
# CLI commands for agents (use these instead of TUI)
bd ready              # Show issues ready to work (no blockers)
bd list --status=open # All open issues
bd show <id>          # Full issue details with dependencies
bd create --title="..." --type=task --priority=2
bd update <id> --status=in_progress
bd close <id> --reason="Completed"
bd close <id1> <id2>  # Close multiple issues at once
bd sync               # Commit and push changes
```

### Standard Workflow Pattern

1. **Start**: Run `bd ready` to find actionable work
2. **Claim**: Use `bd update <id> --status=in_progress`
3. **Work**: Implement the task
4. **Complete**: Use `bd close <id>`
5. **Sync**: Always run `bd sync` at session end

### Key Concepts

- **Dependencies**: Issues can block other issues. `bd ready` shows only unblocked work.
- **Priority**: P0=critical, P1=high, P2=medium, P3=low, P4=backlog (use numbers, not words)
- **Types**: task, bug, feature, epic, question, docs
- **Blocking**: `bd dep add <issue> <depends-on>` to add dependencies

### Session Protocol Checklist

**Before ending any session, run this checklist:**

```bash
git status              # Check what changed
git add <files>         # Stage code changes
bd sync                 # Commit beads changes
git commit -m "..."     # Commit code
bd sync                 # Commit any new beads changes
git push                # Push to remote
```

### Best Practices

- Check `bd ready` at session start to find available work
- Update status as you work (in_progress → closed)
- Create new issues with `bd create` when you discover tasks
- Use descriptive titles and set appropriate priority/type
- Always `bd sync` before ending session

### Using npm Scripts

If your project has npm scripts configured, you can use:

```bash
npm run bd:ready        # Equivalent to: bd ready
npm run bd:sync         # Equivalent to: bd sync
npm run bdui            # Launch monitoring UI
```

### Integration with AI Agents

For AI coding assistants, Beads provides structured output:

```bash
# Get JSON output for programmatic use
bd ready --json
bd show <id> --json
bd list --json

# Use with beads_viewer for graph analytics
bv ready --json         # Tasks with graph metrics
bv insights             # Analytics dashboard
```

## Agent Behavior Rules

1. **Always check for available work** using `bd ready` at session start
2. **Claim tasks explicitly** using `bd update <id> --status=in_progress` before starting work
3. **Create issues** for discovered work using `bd create` with appropriate type and priority
4. **Close completed tasks** using `bd close <id>` with a reason
5. **Sync regularly** using `bd sync` to keep issues in sync with git
6. **Never skip git push** - session completion requires successful push to remote
