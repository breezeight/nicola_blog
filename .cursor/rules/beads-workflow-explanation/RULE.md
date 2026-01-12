---
description: "Explanation: Decision-making context and rationale for beads-workflow rule. Helps answer questions about why decisions were made and enables self-updates with user confirmation."
globs: [".cursor/rules/beads-workflow/RULE.md"]
alwaysApply: false
---

# Beads Workflow Rule - Explanation & Decision Context

This explanation document provides decision-making context and rationale for the beads-workflow rule. It applies ONLY to `.cursor/rules/beads-workflow/RULE.md` and helps answer questions about why certain decisions were made.

**Documentation Type**: Explanation (per Diataxis framework - understanding-oriented)

## Purpose

This explanation document serves three functions:
1. **Document decision rationale** - Explains why Beads was chosen and how the workflow rule was designed
2. **Answer questions** - Provides context when asked about rule decisions or alternatives
3. **Enable self-updates** - Allows the beads-workflow rule to be refactored/updated with user confirmation

## Why Beads? - Core Decision Rationale

### The Problem with Traditional Approaches

#### Markdown TODO Lists
- **No dependency tracking**: Can't express that Task B depends on Task A
- **No priority management**: Hard to see what's actually ready to work on
- **No status tracking**: Difficult to track what's in progress vs. completed
- **Merge conflicts**: Multiple people editing TODO.md causes conflicts
- **No history**: Can't see when tasks were created or completed
- **No structure**: Flat list doesn't show relationships between tasks
- **No easy way to create scenarios** in order to simulate the rescheduling of tasks and see the dependencies between tasks on git. 

#### External Issue Trackers (GitHub Issues, Jira, etc.)
- **Context switching**: Need to leave your editor/terminal
- **Not git-native**: Issues live outside your codebase
- **Overhead**: Requires authentication, web UI, separate workflow
- **Not portable**: Tied to specific platforms
- **No offline access**: Can't work without internet

### Why Beads Solves These Problems

Beads provides a **git-backed, dependency-aware graph** for managing tasks directly in your repository.

#### ✅ Git-Native
- **Issues stored in `.beads/`**: Versioned alongside your code
- **Branch-aware**: Issues can be created and managed in feature branches
- **Merge-friendly**: Hash-based IDs prevent conflicts
- **Full history**: Every change is tracked in git
- **Portable**: Works offline, no external dependencies

#### ✅ Dependency-Aware
- **Blocking relationships**: Task B can depend on Task A
- **Automatic ready detection**: `bd ready` shows only tasks with no blockers
- **Graph visualization**: See how tasks relate to each other
- **Epic support**: Organize tasks hierarchically

#### ✅ Agent-Optimized
- **JSON output**: Easy to parse and integrate with tools
- **CLI-first**: Perfect for automation and scripts
- **Structured data**: Tasks have priorities, statuses, descriptions
- **Auto-sync**: Keeps issues in sync with git automatically

#### ✅ Zero Infrastructure
- **No servers**: Everything is local
- **No authentication**: Uses your git credentials
- **No setup**: Just `bd init` and you're ready
- **Fast**: SQLite cache for quick queries

#### ✅ Developer-Friendly
- **Terminal workflow**: Stay in your terminal/editor
- **Simple commands**: `bd ready`, `bd create`, `bd close`
- **Clear priorities**: P0 (highest) to P4 (lowest)
- **Status tracking**: open → in_progress → done

## Benefits for Complex Projects

### 1. **Multi-Phase Development**

Projects with multiple phases and dependencies benefit from Beads:
- See which tasks are ready (no blockers)
- Understand dependencies between phases
- Track progress across phases

**Example:** A project with Phase 1 (Foundation), Phase 2 (Core Features), and Phase 3 (Integration) can express that Phase 2 depends on Phase 1, and Phase 3 depends on Phase 2.

### 2. **Component-Based Architecture**

When building multiple components that depend on a common interface or library, Beads allows you to:
- Express that all components depend on the interface definition
- See which components can be started once the interface is done
- Track progress across multiple similar tasks

**Example:** Building adapters for different APIs that all depend on a common adapter interface.

### 3. **Research & Evaluation**

Projects with research tasks and sequential dependencies benefit from:
- Ensuring research tasks are done in the right order
- Tracking decision points and their dependencies
- Documenting the research workflow

**Example:** Evaluating multiple technologies where each evaluation depends on the previous one's results.

### 4. **Long-Horizon Planning**

For projects with many tasks, Beads provides:
- Clear organization by epic/phase
- Priority-based filtering
- Dependency-aware task selection
- Progress tracking over time

## Comparison: Before vs. After

### Before (TODO.md)

```markdown
## Feature Development
- [ ] Define common interface
- [ ] Component A implementation
- [ ] Component B implementation
- [ ] Component C implementation
...
```

**Problems:**
- Can't see that components depend on the interface
- No way to filter "ready to work" tasks
- No status tracking
- Manual updates required

### After (Beads)

```bash
$ npm run bd:ready
📋 Ready work (10 issues with no blockers):
1. [● P0] Define common interface
2. [● P1] Component A implementation (depends on: interface)
3. [● P1] Component B implementation (depends on: interface)
...
```

**Benefits:**
- Clear dependencies shown
- Only ready tasks displayed
- Status automatically tracked
- Git-backed, always in sync

## Workflow Example

### Traditional Workflow
1. Open TODO.md
2. Find a task manually
3. Edit TODO.md to mark as in progress
4. Commit changes
5. Work on task
6. Edit TODO.md to mark as done
7. Commit changes

### Beads Workflow
1. `npm run bd:ready` - See what's available
2. `npx bd update <id> --status in_progress` - Claim task
3. Work on task
4. `npx bd close <id>` - Complete task
5. `npm run bd:sync` - Sync with git (automatic)

**Result:** Faster, clearer, less error-prone.

## Integration with Development Workflow

Beads integrates seamlessly with git workflows:

- **Feature branches**: Create issues in branches, merge with code
- **Pull requests**: Issues are part of the code review
- **CI/CD**: Can query issues programmatically
- **Documentation**: Issues serve as living documentation

## For AI Agents

Beads is particularly well-suited for AI coding assistants:

- **Structured output**: JSON format easy to parse
- **Dependency awareness**: Agents can understand task relationships
- **Ready detection**: Agents can find work without blockers
- **Status tracking**: Agents can update progress automatically
- **Git integration**: Changes are versioned automatically

## Rule Design Decisions

### Why "Session Completion Protocol" is Mandatory

**Decision**: Made git push mandatory in session completion workflow.

**Rationale**:
- Prevents work from being stranded locally
- Ensures all changes are backed up remotely
- Creates clear completion criteria for AI agents
- Aligns with git-native workflow philosophy

**Alternatives Considered**:
- Optional push (rejected - too easy to forget)
- Separate "sync" step (rejected - adds complexity)
- Auto-push (rejected - too risky, user should control when)

### Why Always Apply Glob Pattern

**Decision**: Set `alwaysApply: true` with glob `["**/*"]` in beads-workflow rule.

**Rationale**:
- Beads workflow applies to all code changes
- Task tracking is universal across all file types
- Ensures consistent behavior regardless of what files are being edited

**Alternatives Considered**:
- File-type specific globs (rejected - workflow is universal)
- Conditional application (rejected - adds complexity, reduces consistency)

### Why Explicit Task Claiming Required

**Decision**: Require `bd update <id> --status in_progress` before starting work.

**Rationale**:
- Prevents duplicate work on same task
- Creates clear audit trail
- Enables better progress tracking
- Supports dependency-aware workflow

**Alternatives Considered**:
- Implicit claiming (rejected - no visibility)
- Optional claiming (rejected - defeats purpose)

### Why JSON Output Emphasized

**Decision**: Emphasize `--json` flag for all bd commands.

**Rationale**:
- Enables programmatic agent use
- Supports automation and scripting
- Makes integration with tools easier
- Aligns with agent-optimized design

## Complementary Tools: beads_viewer and bdui

The Beads ecosystem includes two powerful complementary tools that enhance the core experience: **beads_viewer (bv)** for AI agents and **bdui** for human observers. Together, they create a complete agent-native infrastructure system.

### beads_viewer (bv): The AI Agent's Brain

**beads_viewer transforms task management into intelligent agent decision-making.** Rather than requiring agents to parse JSONL files or guess dependencies, bv provides a **graph-aware intelligence layer** that precomputes nine sophisticated metrics:

**Advanced Graph Analytics:**
- **PageRank** identifies which tasks have the highest influence across the dependency graph—telling agents where impact matters most
- **Betweenness Centrality** finds critical bottleneck tasks that many workflows depend on—single points of failure that block progress
- **HITS (Hyperlink-Induced Topic Search)** distinguishes between authority tasks (important to work on) and hub tasks (used to coordinate other work)
- **Critical Path Analysis** determines the dependency-driven timeline—revealing how delays cascade through your project
- **Closeness and Eigenvector Centrality** measure other dimensions of task importance

**Agent-Native Workflow:**
Instead of agents hallucinating what to do next, bv provides a **robot protocol** with structured commands:
- `bd ready` returns only actionable work with no blockers (eliminating impossible task attempts)
- `bd show <id>` gives complete dependency context
- `bd update <id>` and `bd close <id>` for status management
- All commands support `--json` output for programmatic agent use

**Six Visualization Views** serve different needs: list (quick scanning), Kanban (workflow status), graph (dependency visualization), insights (analytics), history (time-travel diffing), and flow (progress tracking).

This transforms agent behavior from reactive task completion into **strategic, dependency-aware planning.** Agents can reason about what truly needs doing next based on impact, not just what's first in a list.

### bdui: The Human Observer's Window

**bdui provides real-time visibility into agent work,** answering the critical question: "What are my AI agents doing right now?"

**Multiple Visualization Lenses:**
- **Kanban Board** shows the standard 4-column workflow (To-Do → Doing → Review → Done), letting stakeholders see at a glance where work sits
- **Tree View** displays epic and task hierarchies—the parent-child relationships agents are creating
- **Dependency Graph** reveals what's blocking what in visual form
- **Stats Dashboard** provides progress analytics and completion metrics

**Zero-Infrastructure Architecture:**
Unlike traditional project management tools, bdui works directly with the SQLite database—no authentication, no APIs, no cloud services. It watches the `.beads/` database in real-time and updates live as agents modify issues.

**Live Monitoring:**
As agents create, modify, and close tasks, bdui reflects these changes instantly. Teams see agent activity with zero delays, making it ideal for collaborative human oversight of autonomous workflows.

### Why You Need Both

The two tools solve different problems in agent-driven development:

| Dimension | beads_viewer | bdui |
|-----------|--------------|------|
| **Audience** | AI agents (decision-making) | Humans (oversight) |
| **Primary Value** | Graph intelligence for task prioritization | Real-time visibility and team alignment |
| **Metric Sophistication** | 9 advanced graph metrics | Workflow status and dependency view |
| **Use Case** | "What should I work on next?" | "What are agents doing right now?" |
| **Integration** | CLI + JSON output for agent scripts | Live database monitoring for stakeholders |

**In practice:**
- **Agents use beads_viewer** to answer "What's my highest-priority unblocked work?" by analyzing 9 graph metrics that reveal true task importance
- **Humans use bdui** to answer "Is the team making progress?" and "Who's blocked on what?" through real-time Kanban and dependency visualization

Together, they enable **agent-autonomous execution with human visibility**—agents move fast because they're working on genuinely critical tasks, and humans stay informed without micromanaging the workflow.

### Complementary Tools Rationale

**Decision**: Mentioned but not required in the workflow rule.

**Rationale**:
- Optional tools that enhance but don't replace core workflow
- Some projects may not need advanced analytics or human monitoring
- Keeps core rule focused on essential agent behavior

## Self-Update Protocol

When refactoring or updating `.cursor/rules/beads-workflow/RULE.md`, follow this protocol:

### 1. **Understand Current State**
- Read the current beads-workflow RULE.md
- Review this meta-rule for decision context
- Check if proposed changes conflict with established rationale

### 2. **Propose Changes**
- Explain what you want to change and why
- Reference relevant decision rationale above
- Show before/after if significant

### 3. **Request User Confirmation**
- **ALWAYS ask for explicit user confirmation** before modifying the rule
- Present the proposed changes clearly
- Explain the impact of changes
- Wait for user approval before proceeding

### 4. **Update Both Files**
- Update `.cursor/rules/beads-workflow/RULE.md` with approved changes
- Update this explanation document if decision rationale changes
- Maintain consistency between rule and rationale

### 5. **Verify**
- Check that updated rule still aligns with Beads philosophy
- Ensure no breaking changes to workflow
- Test that rule still applies correctly

## Answering Questions About the Rule

When asked about the beads-workflow rule:

1. **Reference this explanation document** for decision context
2. **Explain the "why"** behind decisions, not just the "what"
3. **Consider alternatives** that were rejected and why
4. **Maintain consistency** with established rationale

### Common Questions

**Q: Why is git push mandatory?**
A: Prevents work from being stranded locally and ensures all changes are backed up. See "Session Completion Protocol" rationale above.

**Q: Why always apply to all files?**
A: Beads workflow is universal - task tracking applies regardless of file type. See "Always Apply Glob Pattern" rationale above.

**Q: Why require explicit task claiming?**
A: Prevents duplicate work and creates clear audit trail. See "Explicit Task Claiming Required" rationale above.

**Q: Can I modify the rule?**
A: Yes, but follow the Self-Update Protocol above. Always request user confirmation before making changes.

## Conclusion

Beads provides a **modern, git-native approach** to task tracking that:
- ✅ Eliminates context switching
- ✅ Prevents merge conflicts
- ✅ Tracks dependencies automatically
- ✅ Integrates with git workflows
- ✅ Works offline
- ✅ Scales with project complexity

For projects with multiple phases, dependencies, and long-term planning, Beads is the ideal solution.

## Getting Started

See [AGENTS.md](../../AGENTS.md) for instructions on using Beads in this project.

**Quick commands:**
```bash
npm run bd:ready              # See available work
npx bd update <id> --status in_progress  # Start working
npx bd close <id>             # Complete task
npm run bd:sync              # Sync with git
```

## References

- [Beads GitHub](https://github.com/steveyegge/beads)
- [beads_viewer GitHub](https://github.com/Dicklesworthstone/beads_viewer)
- [beads-ui GitHub](https://github.com/mantoni/beads-ui)

## Version History

- **2026-01-11**: Initial rule creation
- **2026-01-11**: Converted to Cursor RULE.md format with explanation document
- **2026-01-11**: Consolidated BEADS_MOTIVATION.md content into this explanation document
