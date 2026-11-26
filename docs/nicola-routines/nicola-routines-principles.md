---
title: "Nicola's Routines Core Principles"
abstract: >
  Core principles that guide routine definition and execution, ensuring consistency, 
  effectiveness, and alignment with personal and professional goals.
type: explanation
---

# Nicola's Routines Core Principles

## 📘 Purpose & Scope

This document explains the core principles that guide how routines are defined, executed, and maintained. These principles ensure routines remain effective, consistent, and aligned with personal and professional goals across all personas.

## Core Principles for Routine Definition

### Principle 1: Persona-Driven Organization

**Description**: Routines are organized by persona (role/context), not by frequency or type. Each routine belongs to one or more personas that define its context and purpose.

**Rationale**: 
- Ensures routines activate in appropriate contexts
- Prevents context confusion (e.g., work routines during personal time)
- Makes routine management more intuitive
- Aligns with how humans naturally think about roles

**Examples**:
- Morning routine belongs to "Personal" persona, not "Daily" category
- Meeting preparation belongs to "CEO" persona, triggered by calendar
- Yoga practice belongs to "Yoga Teacher" persona, not "Health" category

**Application**: When defining a routine, first identify which persona(s) it serves, then assign entry points and metadata.

### Principle 2: Entry Point Abstraction

**Description**: Entry points abstract away implementation details of triggers. Routines don't need to know about specific calendar systems, notification providers, or time management tools.

**Rationale**:
- Routines remain portable across different tools
- Changes to notification systems don't require routine changes
- Simplifies routine definition and maintenance
- Enables testing with different entry point implementations

**Examples**:
- Routine triggered by "calendar event" works with Google Calendar, Outlook, or any calendar
- Routine triggered by "task notification" works with OpenProject, Jira, or any task system
- Routine triggered by "time" works regardless of timezone or system clock

**Application**: Define entry points in terms of abstract triggers (calendar event, notification, time) rather than specific implementations (Google Calendar, Slack, system clock).

### Principle 3: Explicit Dependencies

**Description**: Routines explicitly declare dependencies on other routines, entry points, or conditions. Dependencies determine execution order and prevent conflicts.

**Rationale**:
- Ensures routines execute in correct order
- Prevents race conditions and conflicts
- Makes routine relationships explicit and understandable
- Enables parallel execution when dependencies allow

**Examples**:
- "Weekly review" depends on "Daily standup" completion
- "Meeting preparation" depends on calendar entry point
- "Yoga practice" depends on "Morning routine" completion

**Application**: When defining a routine, explicitly list all dependencies. Use dependency graphs to visualize routine relationships.

### Principle 4: Atomic and Composable

**Description**: Routines are atomic (single purpose) and composable (can be combined). Complex workflows are built from simple routines.

**Rationale**:
- Simplifies routine definition and understanding
- Enables reuse of routine components
- Makes routines easier to test and debug
- Allows flexible combination of routines

**Examples**:
- "Check email" is atomic; "Morning routine" composes multiple atomic routines
- "Prepare meeting agenda" is atomic; "Meeting preparation" composes multiple atomic routines
- "Review tasks" is atomic; "Weekly review" composes multiple atomic routines

**Application**: Break complex routines into atomic components. Compose complex workflows from atomic routines using dependencies.

### Principle 5: Measurable Outcomes

**Description**: Each routine has measurable outcomes or success criteria. Routines are evaluated based on whether they achieve their intended outcomes.

**Rationale**:
- Enables routine effectiveness evaluation
- Provides clear success criteria
- Supports routine optimization and improvement
- Makes routine value explicit

**Examples**:
- "Morning routine" outcome: "Ready for work day with clear priorities"
- "Meeting preparation" outcome: "Have agenda and context for meeting"
- "Yoga practice" outcome: "Completed practice session with focus and presence"

**Application**: Define measurable outcomes for each routine. Review routines regularly against their outcomes.

## Core Principles for Routine Execution

### Principle 1: Priority-Based Conflict Resolution

**Description**: When multiple routines could execute simultaneously, priority rules determine execution order. Persona priority and routine priority combine to resolve conflicts.

**Rationale**:
- Prevents routine conflicts and confusion
- Ensures important routines execute first
- Provides predictable execution behavior
- Supports multi-persona scenarios

**Examples**:
- CEO persona routines take priority during work hours
- Personal persona routines take priority during personal time
- High-priority routines execute before low-priority routines
- Manual activation can override automatic priority

**Application**: Define priority levels for personas and routines. Document priority resolution rules clearly.

### Principle 2: Graceful Failure Handling

**Description**: Routines handle failures gracefully. Failed routines don't block other routines, and failure recovery is explicit.

**Rationale**:
- Prevents cascade failures
- Maintains system resilience
- Provides clear failure recovery paths
- Enables routine debugging and improvement

**Examples**:
- If "Check email" fails, "Morning routine" continues with other steps
- If "Meeting preparation" fails, meeting still happens with basic preparation
- Failed routines log errors and notify user
- Recovery routines can retry or skip failed steps

**Application**: Define failure handling for each routine. Include retry logic, skip conditions, and error notifications.

### Principle 3: Context Preservation

**Description**: Routines preserve context across execution. Context includes persona state, routine history, and environmental conditions.

**Rationale**:
- Enables routine continuity across sessions
- Supports context-aware routine execution
- Maintains routine state and history
- Enables routine learning and adaptation

**Examples**:
- "Weekly review" remembers previous week's priorities
- "Meeting preparation" remembers previous meeting notes
- "Yoga practice" tracks practice history and progress
- Context persists across routine executions

**Application**: Design routines to preserve and use context. Store context in routine metadata and history.

### Principle 4: Observable Execution

**Description**: Routine execution is observable. Users can see routine status, progress, and outcomes in real-time.

**Rationale**:
- Provides transparency and trust
- Enables routine monitoring and debugging
- Supports routine optimization
- Improves user experience

**Examples**:
- Routine status visible in dashboard or notification
- Progress indicators show routine execution steps
- Completion notifications confirm routine success
- Execution logs enable debugging and analysis

**Application**: Design routines with observable execution. Include status updates, progress indicators, and completion notifications.

### Principle 5: Adaptive Execution

**Description**: Routines adapt to changing conditions. Execution adjusts based on context, time available, and current priorities.

**Rationale**:
- Handles real-world variability
- Optimizes routine execution for current conditions
- Prevents rigid routine adherence
- Improves routine effectiveness

**Examples**:
- "Morning routine" adapts to time available (full vs. abbreviated version)
- "Meeting preparation" adapts to meeting importance (detailed vs. quick prep)
- "Yoga practice" adapts to energy level (full practice vs. gentle practice)
- Routines skip or modify steps based on conditions

**Application**: Design routines with adaptive logic. Include conditional steps and time-based variations.

## Persona-Specific Principles

### CEO Persona Principles

**Focus**: Strategic thinking, company oversight, decision-making

**Principles**:
1. **Strategic Over Tactical**: Prioritize strategic routines over tactical ones
2. **Decision Support**: Routines support decision-making, not replace it
3. **Company Context**: Routines maintain company-wide perspective
4. **Time Efficiency**: Routines optimize CEO time for high-value activities

**Examples**:
- "Strategic review" routine focuses on big picture, not details
- "Meeting preparation" includes strategic context, not just agenda
- "Daily standup" provides company-wide visibility, not just project status

### PM Persona Principles

**Focus**: Project coordination, planning, execution

**Principles**:
1. **Project Focus**: Routines maintain project-specific context
2. **Coordination**: Routines support team coordination and communication
3. **Planning**: Routines emphasize planning and preparation
4. **Execution**: Routines support project execution and delivery

**Examples**:
- "Task review" routine focuses on project tasks, not general tasks
- "Standup preparation" includes project-specific context
- "Weekly review" emphasizes project progress and blockers

### Personal Persona Principles

**Focus**: Personal life, relationships, self-care

**Principles**:
1. **Balance**: Routines maintain work-life balance
2. **Wellbeing**: Routines prioritize health and wellbeing
3. **Relationships**: Routines support personal relationships
4. **Personal Growth**: Routines support personal development

**Examples**:
- "Morning routine" includes self-care, not just work preparation
- "Evening routine" supports relaxation and reflection
- "Weekly review" includes personal goals, not just work goals

### Yoga Teacher Persona Principles

**Focus**: Yoga practice, teaching, learning

**Principles**:
1. **Practice First**: Routines prioritize personal practice
2. **Teaching Support**: Routines support teaching activities
3. **Learning**: Routines include learning and study
4. **Presence**: Routines emphasize mindfulness and presence

**Examples**:
- "Yoga practice" routine focuses on personal practice, not just teaching
- "Teaching preparation" includes practice and study
- "Practice review" emphasizes learning and growth

## Principle Application Framework

### When Defining Routines

1. **Identify Persona**: Which persona(s) does this routine serve?
2. **Define Entry Points**: What triggers this routine?
3. **Set Dependencies**: What does this routine depend on?
4. **Define Outcomes**: What are the measurable outcomes?
5. **Make Atomic**: Can this be broken into smaller routines?
6. **Set Priority**: What priority level does this routine have?

### When Executing Routines

1. **Check Context**: Is the appropriate persona active?
2. **Resolve Conflicts**: Apply priority rules if conflicts exist
3. **Handle Failures**: Implement graceful failure handling
4. **Preserve Context**: Maintain context across execution
5. **Observe Execution**: Provide status and progress updates
6. **Adapt Execution**: Adjust based on current conditions

### When Reviewing Routines

1. **Measure Outcomes**: Did the routine achieve its outcomes?
2. **Evaluate Effectiveness**: Is the routine effective?
3. **Check Dependencies**: Are dependencies still valid?
4. **Assess Priority**: Is priority level still appropriate?
5. **Consider Adaptation**: Can the routine be improved?
6. **Update Documentation**: Keep documentation current

## References

- {{ link_with_abstract("nicola-routines-architecture.md") }} - System architecture that implements these principles
- {{ link_with_abstract("nicola-routines.md") }} - Reference document with routines following these principles
- {{ link_with_abstract("nicola-routines-personas.md") }} - Persona definitions with persona-specific principles
- {{ link_with_abstract("nicola-routines-howto-define-routine.md") }} - How to apply these principles when defining routines
- {{ link_with_abstract("nicola-routines-howto-review-routines.md") }} - How to review routines against these principles
