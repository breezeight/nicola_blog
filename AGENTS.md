## Task Management with Beads

This project uses **bd** (beads) for issue tracking.

> **Source of Truth:** Complete workflow rules are in `.cursor/rules/beads-workflow/RULE.md` and are automatically applied in Cursor IDE.

For More Information, see:

- **Complete workflow rules**: `.cursor/rules/beads-workflow/RULE.md` (automatically applied in Cursor IDE)
- **Decision rationale**: `.cursor/rules/beads-workflow-explanation/RULE.md`
- **Beads documentation**: https://github.com/steveyegge/beads

## Landing the Plane (Session Completion)

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until `git push` succeeds.

**MANDATORY WORKFLOW:**

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
