---
description: "Nicola's routines system architecture and management rules"
globs: ["docs/nicola-routines/**/*.md"]
alwaysApply: true
---

# Nicola's Routines System Rules

This rule file defines the architecture and management rules for Nicola's routines system. All AI agents and users working with routines MUST follow these rules.

## Persona/Agent Activation

### When to Activate a Persona

**CEO Persona (Nicola-CEO)**:
- Activate during work hours (typically 09:00-18:00 on workdays)
- Activate when calendar events indicate company meetings
- Activate when email notifications are work-related
- Activate when task notifications are from company projects
- Priority: High

**PM Persona (Nicola-PM)**:
- Activate when working on specific projects (Project X, etc.)
- Activate during project standups and meetings
- Activate when task notifications are project-specific
- Activate when project management tools send notifications
- Priority: Medium

**Personal Persona (Nicola-Personal)**:
- Activate during personal time (evenings, weekends, personal calendar events)
- Activate for personal calendar events and reminders
- Activate for personal relationships and self-care activities
- Activate when entry points indicate personal context
- Priority: Medium

**Yoga Teacher Persona (Nicola-YogaTeacher)**:
- Activate during scheduled yoga practice times
- Activate when calendar events indicate yoga sessions
- Activate for yoga-related learning and teaching activities
- Activate when manually triggered for practice
- Priority: Low

### Context Switching

**Automatic Context Switching**:
- Personas switch automatically based on entry point triggers
- Calendar events trigger persona activation based on event context
- Time-based entry points activate personas based on time of day
- Notification-based entry points activate personas based on notification source

**Manual Context Switching**:
- User can manually activate any persona
- Manual activation overrides automatic priority rules
- Manual activation persists until explicitly changed or entry point triggers different persona

**Multi-Persona Scenarios**:
- Multiple personas can be active simultaneously
- Priority rules determine which routines execute when conflicts occur
- Personas with higher priority take precedence
- Routines from multiple personas can execute in parallel if no conflicts

### Persona Priority Rules

**Priority Hierarchy**:
1. **High Priority**: CEO Persona
2. **Medium Priority**: PM Persona, Personal Persona
3. **Low Priority**: Yoga Teacher Persona

**Conflict Resolution**:
- When multiple personas could activate routines, higher priority persona takes precedence
- During work hours, CEO persona routines execute before PM persona routines
- During personal time, Personal persona routines execute before work personas
- Manual activation can override automatic priority rules
- Yoga Teacher persona routines execute when explicitly scheduled, regardless of other personas

## Routine Definition Rules

### Routine Structure Requirements

**Required Fields**:
- **ID**: Unique identifier (e.g., R001, R002)
- **Name**: Human-readable name
- **Persona**: One or more personas this routine belongs to
- **Entry Points**: One or more entry points that trigger this routine
- **Steps**: List of actionable steps
- **Frequency**: Daily, Weekly, Monthly, Yearly, or On-Demand
- **Estimated Time**: Expected duration
- **Priority**: High, Medium, or Low
- **Dependencies**: Other routines this depends on (if any)
- **Outcomes**: Measurable outcomes or success criteria

**Optional Fields**:
- **Category**: Routine category (e.g., Health, Work, Personal)
- **Tags**: Additional tags for filtering and organization
- **Conditions**: Conditional logic for execution
- **Variations**: Different versions for different contexts

**Format Requirements**:
- Routines must be documented in `nicola-routines.md` reference document
- Each routine must have complete metadata
- Routines must follow naming conventions (descriptive, consistent)
- Routines must include cross-references to related documents

### Routine Categorization

**By Persona**:
- Routines are primarily categorized by persona
- Each routine belongs to one or more personas
- Persona determines routine context and activation

**By Frequency**:
- **Daily**: Routines that execute every day
- **Weekly**: Routines that execute weekly (specific day or flexible)
- **Monthly**: Routines that execute monthly
- **Yearly**: Routines that execute yearly
- **On-Demand**: Routines that execute when triggered

**By Type**:
- **Preparation**: Routines that prepare for activities
- **Execution**: Routines that execute activities
- **Review**: Routines that review and reflect
- **Maintenance**: Routines that maintain systems or habits

**By Priority**:
- **High**: Critical routines that must execute
- **Medium**: Important routines that should execute
- **Low**: Optional routines that can be skipped

### Entry Point Assignment

**Assignment Rules**:
- Each routine must have at least one entry point
- Entry points must be defined in `nicola-routines-entry-points.md`
- Entry points must match routine persona(s)
- Entry points must be appropriate for routine frequency

**Entry Point Types**:
- **Time-based**: For scheduled routines (daily, weekly, etc.)
- **Calendar-based**: For calendar-triggered routines
- **Notification-based**: For notification-triggered routines
- **Event-based**: For event-triggered routines
- **Manual**: For user-initiated routines
- **System**: For system-triggered routines

**Assignment Process**:
1. Identify routine trigger conditions
2. Find or create appropriate entry point
3. Assign entry point to routine
4. Document entry point in catalog
5. Update routine metadata

## Routine Execution Rules

### Execution Order

**Dependency-Based Ordering**:
- Routines execute in dependency order
- Routines with no dependencies can execute immediately
- Routines with dependencies wait for dependencies to complete
- Parallel execution allowed when no dependencies conflict

**Priority-Based Ordering**:
- High-priority routines execute before low-priority routines
- Persona priority determines routine priority when conflicts occur
- Manual activation can override priority ordering

**Time-Based Ordering**:
- Routines execute based on entry point trigger time
- Time-based entry points trigger at specified times
- Calendar-based entry points trigger based on calendar event time

### Entry Point Handling

**Trigger Detection**:
- Entry points continuously monitor for trigger conditions
- When trigger detected, entry point router identifies associated routines
- Persona system determines which personas should be active
- Routines matching entry point and active personas are selected

**Notification Processing**:
- Notification-based entry points parse notification content
- Notification content determines which routines to trigger
- Notification source determines which persona to activate
- Notification priority determines routine execution priority

**Conditional Logic**:
- Entry points can have conditional logic (if-then conditions)
- Conditions evaluate before routine execution
- Routines execute only if conditions are met
- Failed conditions log reason and skip routine

### Failure Handling

**Failure Types**:
- **Routine Failure**: Routine step fails or errors
- **Dependency Failure**: Required dependency fails or unavailable
- **Entry Point Failure**: Entry point fails to trigger
- **Persona Conflict**: Multiple personas conflict

**Failure Handling Rules**:
- Failed routines don't block other routines
- Failed routines log errors with context
- Failed routines notify user if critical
- Failed routines can retry based on retry logic
- Failed routines can skip remaining steps if configured

**Recovery Process**:
1. Log failure with context and error details
2. Determine if retry is appropriate
3. If retry, schedule retry with backoff
4. If no retry, mark routine as failed
5. Notify user if routine is critical
6. Continue with other routines

## Routine Review and Update Rules

### Review Schedule

**Regular Reviews**:
- **Weekly Review**: Review daily and weekly routines
- **Monthly Review**: Review monthly routines and overall system
- **Quarterly Review**: Review yearly routines and system architecture
- **Ad-Hoc Review**: Review when issues or changes occur

**Review Process**:
1. Evaluate routine effectiveness against outcomes
2. Check routine usage and execution frequency
3. Assess routine dependencies and relationships
4. Review routine priority and categorization
5. Identify improvements and optimizations
6. Update routine documentation

### Update Process

**Change Request**:
- Identify need for change (effectiveness, new requirement, etc.)
- Document change request with rationale
- Assess impact on related routines and personas
- Get approval if change affects multiple routines or personas

**Update Steps**:
1. Update routine definition in reference document
2. Update entry point configuration if needed
3. Update persona assignments if needed
4. Update dependencies if needed
5. Test routine execution
6. Update all related documentation
7. Notify stakeholders if significant change

**Version Control**:
- Routine changes are tracked in git
- Significant changes require commit messages explaining rationale
- Routine versions can be tagged for major changes
- Routine history maintained in git history

### Documentation Updates

**Required Updates**:
- Update `nicola-routines.md` when routines change
- Update `nicola-routines-entry-points.md` when entry points change
- Update `nicola-routines-personas.md` when personas change
- Update cross-references when relationships change

**Update Frequency**:
- Update immediately when routines are added or removed
- Update immediately when routine metadata changes
- Update during regular reviews
- Update when architecture or principles change

## LLM Agent Rules

### When Working with Routines

**AI agents MUST**:
1. Follow persona activation rules when suggesting routines
2. Respect routine dependencies when executing routines
3. Apply priority rules when conflicts occur
4. Use entry point abstraction when referencing triggers
5. Preserve context across routine executions
6. Handle failures gracefully
7. Update documentation when routines change

**AI agents MUST NOT**:
1. Create routines without proper persona assignment
2. Create routines without entry point assignment
3. Ignore routine dependencies
4. Override priority rules without explicit user request
5. Skip documentation updates
6. Create routines that conflict with existing routines

### When Defining Routines

**AI agents MUST**:
1. Identify appropriate persona(s) for routine
2. Define clear entry points
3. Set explicit dependencies
4. Define measurable outcomes
5. Make routines atomic and composable
6. Set appropriate priority
7. Document routine completely

### When Executing Routines

**AI agents MUST**:
1. Check persona activation before executing
2. Resolve conflicts using priority rules
3. Handle failures gracefully
4. Preserve context across executions
5. Provide observable execution status
6. Adapt execution to current conditions

## References

- {{ link_with_abstract("docs/nicola-routines/nicola-routines-architecture.md") }} - System architecture
- {{ link_with_abstract("docs/nicola-routines/nicola-routines-principles.md") }} - Core principles
- {{ link_with_abstract("docs/nicola-routines/nicola-routines.md") }} - Routine reference
- {{ link_with_abstract("docs/nicola-routines/nicola-routines-personas.md") }} - Persona definitions
- {{ link_with_abstract("docs/nicola-routines/nicola-routines-entry-points.md") }} - Entry point catalog
