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
