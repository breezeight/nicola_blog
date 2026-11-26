---
title: "Nicola's Routines Personas Reference"
abstract: >
  Reference document defining all personas in Nicola's routines system, including 
  activation triggers, context boundaries, routines, and entry points for each persona.
type: reference
---

# Nicola's Routines Personas Reference

## 📘 Purpose & Scope

This document provides a complete reference of all personas in Nicola's routines system. Each persona entry includes activation triggers, context boundaries, associated routines, entry points, and priority levels.

## Persona Reference

### Nicola-CEO

**Persona ID**: CEO  
**Full Name**: Nicola-CEO  
**Primary Context**: Addictive company operations, strategic decisions, company oversight

**Activation Triggers**:
- Work hours (typically 09:00-18:00 on workdays)
- Calendar events indicating company meetings
- Email notifications from work-related sources
- Task notifications from company projects
- Manual activation for strategic work

**Routines**: See [Nicola's Routines](nicola-routines.md): Reference document listing all routines organized by persona, frequency, and entry point, with complete metadata including priority, estimated time, dependencies, and outcomes. for CEO persona routines

**Entry Points**: See [Nicola's Routines Entry Points Catalog](nicola-routines-entry-points.md): Reference catalog of all entry points in Nicola's routines system, organized by type, with trigger conditions, associated personas, and triggered routines. for CEO persona entry points

**Priority Level**: High

**Context Boundaries**:
- Active during work hours
- Active during company meetings and strategic sessions
- Active when handling company-related communications
- Inactive during personal time (unless manually activated)
- Inactive during yoga practice (unless urgent)

**Sub-Personas**: None currently defined

**Integration Points**:
- Google Calendar for meeting scheduling
- Email system for company communications
- OpenProject for company task management
- Company communication tools (Slack, Teams, etc.)

**Notes**:
- This persona takes precedence over other personas during work hours
- Strategic routines prioritize long-term company goals
- Decision-support routines help with strategic thinking
- Time optimization routines maximize CEO effectiveness

### Nicola-PM

**Persona ID**: PM  
**Full Name**: Nicola-PM  
**Primary Context**: Project management, project coordination, planning, execution

**Activation Triggers**:
- Working on specific projects (Project X, etc.)
- Project standups and meetings
- Task notifications from project management tools
- Calendar events indicating project meetings
- Manual activation for project work

**Routines**: See [Nicola's Routines](nicola-routines.md): Reference document listing all routines organized by persona, frequency, and entry point, with complete metadata including priority, estimated time, dependencies, and outcomes. for PM persona routines

**Entry Points**: See [Nicola's Routines Entry Points Catalog](nicola-routines-entry-points.md): Reference catalog of all entry points in Nicola's routines system, organized by type, with trigger conditions, associated personas, and triggered routines. for PM persona entry points

**Priority Level**: Medium

**Context Boundaries**:
- Active during project work sessions
- Active during project meetings and standups
- Active when handling project-related tasks
- Can be active simultaneously with CEO persona
- Inactive when not working on projects

**Sub-Personas**: 
- PM-ProjectX: Specific to Project X
- PM-ProjectY: Specific to Project Y (if applicable)

**Integration Points**:
- OpenProject for project task management
- Project management tools (Jira, Trello, etc.)
- Calendar for project meetings
- Communication tools for project coordination

**Notes**:
- This persona focuses on project-specific context
- Routines emphasize coordination and planning
- Can coexist with CEO persona for strategic project work
- Project-specific sub-personas allow project-specific routines

### Nicola-Personal

**Persona ID**: Personal  
**Full Name**: Nicola-Personal  
**Primary Context**: Personal life, relationships, self-care, personal development

**Activation Triggers**:
- Personal time (evenings, weekends, personal calendar events)
- Personal calendar events and reminders
- Personal relationships and self-care activities
- Time-based triggers for personal routines
- Manual activation for personal activities

**Routines**: See [Nicola's Routines](nicola-routines.md): Reference document listing all routines organized by persona, frequency, and entry point, with complete metadata including priority, estimated time, dependencies, and outcomes. for Personal persona routines

**Entry Points**: See [Nicola's Routines Entry Points Catalog](nicola-routines-entry-points.md): Reference catalog of all entry points in Nicola's routines system, organized by type, with trigger conditions, associated personas, and triggered routines. for Personal persona entry points

**Priority Level**: Medium

**Context Boundaries**:
- Active during personal time (evenings, weekends)
- Active during personal calendar events
- Active for personal relationships and self-care
- Inactive during work hours (unless personal emergency)
- Can coexist with Yoga Teacher persona

**Sub-Personas**: None currently defined

**Integration Points**:
- Personal calendar for personal events
- Personal task management (if separate from work)
- Personal communication tools
- Health and fitness tracking

**Notes**:
- This persona maintains work-life balance
- Routines prioritize wellbeing and personal growth
- Personal routines support relationships and self-care
- Can activate during work breaks for personal activities

### Nicola-YogaTeacher

**Persona ID**: Yoga  
**Full Name**: Nicola-YogaTeacher  
**Primary Context**: Yoga practice, teaching, learning, mindfulness

**Activation Triggers**:
- Scheduled yoga practice times
- Calendar events indicating yoga sessions
- Yoga-related learning and teaching activities
- Manual activation for practice
- Time-based triggers for regular practice

**Routines**: See [Nicola's Routines](nicola-routines.md): Reference document listing all routines organized by persona, frequency, and entry point, with complete metadata including priority, estimated time, dependencies, and outcomes. for Yoga Teacher persona routines

**Entry Points**: See [Nicola's Routines Entry Points Catalog](nicola-routines-entry-points.md): Reference catalog of all entry points in Nicola's routines system, organized by type, with trigger conditions, associated personas, and triggered routines. for Yoga Teacher persona entry points

**Priority Level**: Low

**Context Boundaries**:
- Active during scheduled practice times
- Active during yoga teaching sessions
- Active for yoga learning and study
- Can coexist with Personal persona
- Inactive during work hours (unless scheduled break)

**Sub-Personas**: None currently defined

**Integration Points**:
- Calendar for practice scheduling
- Yoga apps and tracking tools
- Learning resources (books, videos, courses)
- Teaching tools and resources

**Notes**:
- This persona emphasizes presence and mindfulness
- Routines prioritize practice over teaching
- Teaching routines support teaching activities
- Learning routines support continuous improvement

## Persona Activation Matrix

| Time/Context | CEO | PM | Personal | Yoga Teacher |
|--------------|-----|----|---------|--------------|
| Work Hours (09:00-18:00) | ✅ Active | ✅ Active (if project work) | ❌ Inactive | ❌ Inactive |
| Morning (07:00-09:00) | ⚠️ Can activate | ❌ Inactive | ✅ Active | ✅ Active (if scheduled) |
| Evening (18:00-22:00) | ⚠️ Can activate (if urgent) | ⚠️ Can activate (if project work) | ✅ Active | ✅ Active (if scheduled) |
| Weekend | ⚠️ Can activate (if urgent) | ⚠️ Can activate (if project work) | ✅ Active | ✅ Active (if scheduled) |
| Personal Calendar Event | ❌ Inactive | ❌ Inactive | ✅ Active | ⚠️ Can activate (if yoga-related) |
| Company Meeting | ✅ Active | ⚠️ Can activate (if project-related) | ❌ Inactive | ❌ Inactive |
| Project Meeting | ⚠️ Can activate (if strategic) | ✅ Active | ❌ Inactive | ❌ Inactive |
| Yoga Practice Time | ❌ Inactive | ❌ Inactive | ⚠️ Can coexist | ✅ Active |
| Manual Activation | ✅ Can activate | ✅ Can activate | ✅ Can activate | ✅ Can activate |

**Legend**:
- ✅ Active: Persona is typically active in this context
- ⚠️ Can activate: Persona can activate but not typical
- ❌ Inactive: Persona is typically inactive in this context

## Persona Priority Resolution

When multiple personas could activate routines:

1. **CEO Persona** takes precedence during work hours
2. **PM Persona** activates for project-specific contexts
3. **Personal Persona** activates during personal time
4. **Yoga Teacher Persona** activates during scheduled practice times
5. **Manual Activation** can override automatic priority rules

**Conflict Examples**:
- Work hours + Personal calendar event → CEO persona takes precedence (unless personal emergency)
- Project meeting + Yoga practice time → PM persona takes precedence (unless yoga is scheduled break)
- Weekend + Urgent work → CEO persona can activate (manual override)

## Persona Relationships

**Coexistence Rules**:
- CEO and PM personas can coexist during strategic project work
- Personal and Yoga Teacher personas can coexist during personal practice time
- CEO persona typically excludes Personal persona during work hours
- PM persona can coexist with CEO persona for project coordination

**Context Switching**:
- Automatic switching based on entry point triggers
- Manual switching via explicit activation
- Switching preserves context and state
- Switching logs for debugging and analysis

## Persona Metadata

| Persona | Priority | Typical Activation | Typical Duration | Frequency |
|---------|----------|-------------------|------------------|-----------|
| CEO | High | Work hours | 8-10 hours/day | Daily (workdays) |
| PM | Medium | Project work | 2-4 hours/day | Daily (when projects active) |
| Personal | Medium | Personal time | 4-6 hours/day | Daily |
| Yoga Teacher | Low | Scheduled practice | 1-2 hours/day | Daily (when scheduled) |

## References

- [Nicola's Routines System Architecture](nicola-routines-architecture.md): Architectural design document explaining the persona/agent model, entry point system, and overall architecture of Nicola's routines system for managing different life roles. - System architecture including persona model
- [Nicola's Routines](nicola-routines.md): Reference document listing all routines organized by persona, frequency, and entry point, with complete metadata including priority, estimated time, dependencies, and outcomes. - Routines organized by persona
- [Nicola's Routines Entry Points Catalog](nicola-routines-entry-points.md): Reference catalog of all entry points in Nicola's routines system, organized by type, with trigger conditions, associated personas, and triggered routines. - Entry points organized by persona
- [Nicola's Routines Core Principles](nicola-routines-principles.md): Core principles that guide routine definition and execution, ensuring consistency, effectiveness, and alignment with personal and professional goals. - Persona-specific principles
- [How to Activate a Persona](nicola-routines-howto-activate-persona.md): Step-by-step guide for activating personas in Nicola's routines system, including automatic and manual activation, context switching, and multi-persona handling. - How to activate personas
