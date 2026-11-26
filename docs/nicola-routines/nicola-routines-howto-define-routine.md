---
title: "How to Define a Routine"
abstract: >
  Step-by-step guide for defining new routines in Nicola's routines system, including 
  persona assignment, entry point configuration, and metadata requirements.
type: howto
---

# How to Define a Routine

> [!NOTE]
> For context and rationale behind routine definition, see [Nicola's Routines Core Principles](nicola-routines-principles.md): Core principles that guide routine definition and execution, ensuring consistency, effectiveness, and alignment with personal and professional goals.. For system architecture, see [Nicola's Routines System Architecture](nicola-routines-architecture.md): Architectural design document explaining the persona/agent model, entry point system, and overall architecture of Nicola's routines system for managing different life roles..

## 📘 Purpose & Scope

This guide provides step-by-step instructions for defining a new routine in Nicola's routines system. Follow these steps to ensure routines are properly structured, documented, and integrated with the system.

## Prerequisites

- Understanding of persona model (see [Nicola's Routines Personas Reference](nicola-routines-personas.md): Reference document defining all personas in Nicola's routines system, including activation triggers, context boundaries, routines, and entry points for each persona.)
- Understanding of entry point system (see [Nicola's Routines Entry Points Catalog](nicola-routines-entry-points.md): Reference catalog of all entry points in Nicola's routines system, organized by type, with trigger conditions, associated personas, and triggered routines.)
- Access to routine reference document (see [Nicola's Routines](nicola-routines.md): Reference document listing all routines organized by persona, frequency, and entry point, with complete metadata including priority, estimated time, dependencies, and outcomes.)
- Understanding of core principles (see [Nicola's Routines Core Principles](nicola-routines-principles.md): Core principles that guide routine definition and execution, ensuring consistency, effectiveness, and alignment with personal and professional goals.)

## Step 1: Identify Routine Need

**Action**: Determine what routine is needed and why.

**Questions to Answer**:
- What problem does this routine solve?
- What outcome should this routine achieve?
- Who benefits from this routine?
- When should this routine execute?

**Example**:
- Problem: Need to prepare for meetings effectively
- Outcome: Arrive at meetings with agenda and context
- Beneficiary: CEO persona (Nicola-CEO)
- Timing: 15 minutes before calendar events

**Verification**: You can clearly articulate the routine's purpose and value.

## Step 2: Assign Persona(s)

**Action**: Determine which persona(s) this routine belongs to.

**Process**:
1. Review persona definitions in [Nicola's Routines Personas Reference](nicola-routines-personas.md): Reference document defining all personas in Nicola's routines system, including activation triggers, context boundaries, routines, and entry points for each persona.
2. Identify which persona's context this routine fits
3. Consider if routine belongs to multiple personas
4. Assign primary persona and any secondary personas

**Persona Options**:
- **CEO**: Company operations, strategic decisions
- **PM**: Project management, coordination
- **Personal**: Personal life, relationships, self-care
- **Yoga Teacher**: Yoga practice, teaching, learning

**Example**:
- Routine: Meeting preparation
- Primary Persona: CEO (for company meetings)
- Secondary Persona: PM (for project meetings)

**Verification**: Routine is assigned to appropriate persona(s).

## Step 3: Define Entry Points

**Action**: Identify what triggers this routine.

**Process**:
1. Review entry point catalog in [Nicola's Routines Entry Points Catalog](nicola-routines-entry-points.md): Reference catalog of all entry points in Nicola's routines system, organized by type, with trigger conditions, associated personas, and triggered routines.
2. Identify existing entry points that could trigger this routine
3. If no suitable entry point exists, plan to create new one (see [How to Configure Entry Points](nicola-routines-howto-configure-entry-point.md): Step-by-step guide for configuring entry points in Nicola's routines system, including notification system setup, trigger configuration, and integration with external systems.)
4. Assign entry point(s) to routine

**Entry Point Types**:
- **Time-based**: Scheduled times (e.g., 07:00 daily)
- **Calendar-based**: Calendar events (e.g., 15min before meeting)
- **Notification-based**: Notifications (e.g., task assigned)
- **Event-based**: Specific events (e.g., email received)
- **Manual**: User activation (e.g., "Start routine")
- **System**: System events (e.g., computer startup)

**Example**:
- Routine: Meeting preparation
- Entry Point: C001 (Meeting Reminder - 15 minutes before calendar event)
- Alternative: C002 (Company Meeting) or C003 (Project Meeting)

**Verification**: Routine has at least one entry point assigned.

## Step 4: Define Routine Steps

**Action**: Break down routine into actionable steps.

**Process**:
1. List all steps required to complete routine
2. Make steps atomic and specific
3. Order steps logically
4. Include verification steps
5. Consider error handling

**Step Guidelines**:
- Each step should be a single, clear action
- Steps should be executable without additional context
- Steps should be measurable (can verify completion)
- Steps should be ordered logically

**Example**:
- Routine: Meeting preparation
- Steps:
  1. Check calendar for meeting details
  2. Review meeting agenda (if available)
  3. Gather relevant documents and context
  4. Review previous meeting notes (if applicable)
  5. Prepare questions or talking points
  6. Set reminder for meeting time

**Verification**: Routine steps are clear, actionable, and complete.

## Step 5: Set Metadata

**Action**: Define routine metadata.

**Required Metadata**:
- **ID**: Unique identifier (next available ID from reference document)
- **Name**: Human-readable name
- **Frequency**: Daily, Weekly, Monthly, Yearly, or On-Demand
- **Estimated Time**: Expected duration
- **Priority**: High, Medium, or Low
- **Dependencies**: Other routines this depends on (if any)
- **Outcomes**: Measurable outcomes or success criteria

**Optional Metadata**:
- **Category**: Routine category (e.g., Health, Work, Personal)
- **Tags**: Additional tags for filtering
- **Conditions**: Conditional logic for execution
- **Variations**: Different versions for different contexts

**Example**:
- ID: R003
- Name: Meeting Preparation
- Frequency: On-Demand (triggered by calendar)
- Estimated Time: 15 minutes
- Priority: High
- Dependencies: None
- Outcomes: Arrive at meeting with agenda and context prepared

**Verification**: All required metadata is defined.

## Step 6: Define Dependencies

**Action**: Identify routine dependencies.

**Process**:
1. Review routine steps
2. Identify if routine depends on other routines
3. List dependencies explicitly
4. Consider dependency order

**Dependency Types**:
- **Prerequisite**: Must complete before this routine
- **Optional**: Can enhance this routine but not required
- **Parallel**: Can execute simultaneously

**Example**:
- Routine: Weekly Review
- Dependencies: R001-R006 (all daily routines must complete first)

**Verification**: Dependencies are identified and documented.

## Step 7: Define Outcomes

**Action**: Define measurable outcomes or success criteria.

**Process**:
1. Identify what success looks like
2. Define measurable criteria
3. Consider how to verify outcomes
4. Document outcomes clearly

**Outcome Guidelines**:
- Outcomes should be specific and measurable
- Outcomes should align with routine purpose
- Outcomes should be verifiable
- Outcomes should be achievable

**Example**:
- Routine: Meeting Preparation
- Outcome: Arrive at meeting with agenda reviewed, relevant documents gathered, and talking points prepared

**Verification**: Outcomes are defined and measurable.

## Step 8: Document Routine

**Action**: Add routine to reference document.

**Process**:
1. Open `nicola-routines.md` reference document
2. Add routine to appropriate persona section
3. Add routine to appropriate frequency section
4. Add routine to entry point section
5. Update routine statistics
6. Update dependency graph if needed

**Documentation Format**:
- Use table format for routine listing
- Include all metadata
- Cross-reference related documents
- Follow existing documentation style

**Example**:
Add to CEO Persona Daily Routines table:
```
| R003 | Meeting Preparation | C001, C002 | 15min before | High | None | Active |
```

**Verification**: Routine is documented in reference document.

## Step 9: Update Entry Points

**Action**: Update entry point catalog if needed.

**Process**:
1. Check if entry point already exists
2. If new entry point needed, create it (see [How to Configure Entry Points](nicola-routines-howto-configure-entry-point.md): Step-by-step guide for configuring entry points in Nicola's routines system, including notification system setup, trigger configuration, and integration with external systems.)
3. Update entry point catalog with routine reference
4. Update entry point by persona section

**Verification**: Entry points are updated with routine references.

## Step 10: Test Routine

**Action**: Verify routine works as expected.

**Process**:
1. Trigger routine via entry point
2. Execute routine steps
3. Verify outcomes are achieved
4. Check for errors or issues
5. Adjust routine if needed

**Testing Checklist**:
- [ ] Entry point triggers routine correctly
- [ ] Routine steps execute in order
- [ ] Dependencies are met
- [ ] Outcomes are achieved
- [ ] No errors occur
- [ ] Routine completes successfully

**Verification**: Routine executes successfully and achieves outcomes.

## Troubleshooting

### Routine Not Triggering

**Problem**: Routine doesn't trigger when entry point activates.

**Solutions**:
- Check entry point configuration
- Verify persona is active
- Check routine status (should be Active)
- Verify entry point assignment

### Routine Steps Not Clear

**Problem**: Routine steps are unclear or ambiguous.

**Solutions**:
- Break down steps into smaller actions
- Add more specific instructions
- Include examples or context
- Review with persona context

### Dependencies Not Met

**Problem**: Routine dependencies are not available.

**Solutions**:
- Verify dependency routines exist
- Check dependency routine status
- Adjust dependency requirements
- Consider making dependencies optional

### Outcomes Not Achieved

**Problem**: Routine doesn't achieve defined outcomes.

**Solutions**:
- Review routine steps
- Adjust step sequence
- Add missing steps
- Refine outcome definitions

## Next Steps

After defining a routine:

1. **Review Routine**: Schedule regular review (see [How to Review and Update Routines](nicola-routines-howto-review-routines.md): Step-by-step guide for reviewing and updating routines in Nicola's routines system, including effectiveness evaluation, usage analysis, and change management.)
2. **Monitor Execution**: Track routine execution and outcomes
3. **Gather Feedback**: Collect feedback on routine effectiveness
4. **Iterate**: Improve routine based on experience

## References

- [Nicola's Routines Core Principles](nicola-routines-principles.md): Core principles that guide routine definition and execution, ensuring consistency, effectiveness, and alignment with personal and professional goals. - Core principles for routine definition
- [Nicola's Routines System Architecture](nicola-routines-architecture.md): Architectural design document explaining the persona/agent model, entry point system, and overall architecture of Nicola's routines system for managing different life roles. - System architecture
- [Nicola's Routines](nicola-routines.md): Reference document listing all routines organized by persona, frequency, and entry point, with complete metadata including priority, estimated time, dependencies, and outcomes. - Routine reference document
- [Nicola's Routines Personas Reference](nicola-routines-personas.md): Reference document defining all personas in Nicola's routines system, including activation triggers, context boundaries, routines, and entry points for each persona. - Persona definitions
- [Nicola's Routines Entry Points Catalog](nicola-routines-entry-points.md): Reference catalog of all entry points in Nicola's routines system, organized by type, with trigger conditions, associated personas, and triggered routines. - Entry point catalog
- [How to Configure Entry Points](nicola-routines-howto-configure-entry-point.md): Step-by-step guide for configuring entry points in Nicola's routines system, including notification system setup, trigger configuration, and integration with external systems. - How to configure entry points
- [How to Review and Update Routines](nicola-routines-howto-review-routines.md): Step-by-step guide for reviewing and updating routines in Nicola's routines system, including effectiveness evaluation, usage analysis, and change management. - How to review routines
