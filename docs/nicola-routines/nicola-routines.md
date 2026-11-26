---
title: "Nicola's Routines"
abstract: >
  Reference document listing all routines organized by persona, frequency, and entry point, 
  with complete metadata including priority, estimated time, dependencies, and outcomes.
type: reference
---

# Nicola's Routines

## 📘 Purpose & Scope

This document serves as a complete reference for all routines in Nicola's routines system. Routines are organized by [Nicola's Routines Personas Reference](nicola-routines-personas.md): Reference document defining all personas in Nicola's routines system, including activation triggers, context boundaries, routines, and entry points for each persona., frequency, and [Nicola's Routines Entry Points Catalog](nicola-routines-entry-points.md): Reference catalog of all entry points in Nicola's routines system, organized by type, with trigger conditions, associated personas, and triggered routines., with complete metadata including priority, estimated time, dependencies, and outcomes. For more context on the system design, see [Nicola's Routines System Architecture](nicola-routines-architecture.md): Architectural design document explaining the persona/agent model, entry point system, and overall architecture of Nicola's routines system for managing different life roles. and [Nicola's Routines Core Principles](nicola-routines-principles.md): Core principles that guide routine definition and execution, ensuring consistency, effectiveness, and alignment with personal and professional goals..

## Routine Metadata Schema

Each routine includes the following metadata:

- **ID**: Unique identifier (e.g., R001, R002)
- **Name**: Human-readable name
- **Persona**: One or more [Nicola's Routines Personas Reference](nicola-routines-personas.md): Reference document defining all personas in Nicola's routines system, including activation triggers, context boundaries, routines, and entry points for each persona. this routine belongs to
- **Entry Points**: One or more [Nicola's Routines Entry Points Catalog](nicola-routines-entry-points.md): Reference catalog of all entry points in Nicola's routines system, organized by type, with trigger conditions, associated personas, and triggered routines. that trigger this routine
- **Frequency**: Daily, Weekly, Monthly, Yearly, or On-Demand
- **Estimated Time**: Expected duration
- **Priority**: High, Medium, or Low
- **Dependencies**: Other routines this depends on (if any)
- **Outcomes**: Measurable outcomes or success criteria
- **Status**: Active, Inactive, or Deprecated

To define new routines, see [How to Define a Routine](nicola-routines-howto-define-routine.md): Step-by-step guide for defining new routines in Nicola's routines system, including persona assignment, entry point configuration, and metadata requirements..

## Routines by Persona

Routines are organized by [Nicola's Routines Personas Reference](nicola-routines-personas.md): Reference document defining all personas in Nicola's routines system, including activation triggers, context boundaries, routines, and entry points for each persona.. To activate a persona, see [How to Activate a Persona](nicola-routines-howto-activate-persona.md): Step-by-step guide for activating personas in Nicola's routines system, including automatic and manual activation, context switching, and multi-persona handling..

### CEO Persona Routines

#### Daily Routines

| ID    | Name               | Entry Point   | Time         | Priority | Dependencies | Status  |
| ----- | ------------------ | ------------- | ------------ | -------- | ------------ | ------- |
| R001  | Work Day Start     | T002, M002    | 09:00        | High     | None         | Active  |
| R002  | Email Review       | N004, N005    | On-demand    | High     | None         | Active  |
| R003  | Meeting Preparation | C001, C002    | 15min before | High     | None         | Active  |
| R004  | Strategic Review   | C007, M006    | On-demand    | High     | R001         | Active  |
| R005  | Work Day End       | T004          | 18:00        | Medium   | R001         | Active  |
| R006  | Lunch Break        | T003          | 12:30        | Medium   | None         | Active  |

**Outcomes**:
- R001: Ready for work day with clear priorities and context
- R002: Important emails reviewed and responded to
- R003: Prepared for meeting with agenda and context
- R004: Strategic decisions made with proper context
- R005: Work day concluded with tasks organized and next day prepared
- R006: Lunch break taken with proper nutrition and rest

#### Weekly Routines

| ID    | Name               | Entry Point | Time         | Priority | Dependencies | Status  |
| ----- | ------------------ | ----------- | ------------ | -------- | ------------ | ------- |
| R007  | Weekly Review      | T006, M004  | Sunday 09:00 | High     | R001-R006     | Active  |
| R008  | Strategic Planning | C007        | On-demand    | High     | R007         | Active  |

**Outcomes**:
- R007: Week reviewed with accomplishments and learnings documented
- R008: Strategic plans updated with current context

#### Monthly Routines

| ID    | Name                        | Entry Point | Time                | Priority | Dependencies | Status  |
| ----- | --------------------------- | ----------- | ------------------- | -------- | ------------ | ------- |
| R009  | Monthly Review              | T007        | 1st of month 09:00  | High     | R007         | Active  |
| R010  | Company Performance Review | C007        | Monthly             | High     | R009         | Active  |

**Outcomes**:
- R009: Month reviewed with key metrics and achievements
- R010: Company performance assessed with strategic adjustments

#### Yearly Routines

| ID    | Name               | Entry Point | Time               | Priority | Dependencies | Status  |
| ----- | ------------------ | ----------- | ------------------ | -------- | ------------ | ------- |
| R011  | Yearly Review      | T008        | January 1st 10:00  | High     | R009         | Active  |
| R012  | Strategic Planning | C007        | Yearly             | High     | R011         | Active  |

**Outcomes**:
- R011: Year reviewed with major accomplishments and learnings
- R012: Strategic direction set for upcoming year

### PM Persona Routines

#### Daily Routines

| ID    | Name                 | Entry Point | Time         | Priority | Dependencies | Status  |
| ----- | -------------------- | ----------- | ------------ | -------- | ------------ | ------- |
| R013  | Task Review          | N001, N002  | On-demand    | High     | None         | Active  |
| R014  | Standup Preparation  | C006        | 15min before | High     | R013         | Active  |
| R015  | Project Status Check | N006        | On-demand    | Medium   | R013         | Active  |
| R016  | Task Planning        | N001        | On-demand    | Medium   | R013         | Active  |

**Outcomes**:
- R013: Tasks reviewed with priorities and status updated
- R014: Standup prepared with updates and blockers identified
- R015: Project status assessed with risks identified
- R016: Tasks planned with dependencies and estimates

#### Weekly Routines

| ID    | Name                   | Entry Point | Time         | Priority | Dependencies | Status  |
| ----- | ---------------------- | ----------- | ------------ | -------- | ------------ | ------- |
| R017  | Weekly Project Review  | T006, M004  | Sunday 09:00 | High     | R013-R016    | Active  |
| R018  | Sprint Planning        | C003        | On-demand    | High     | R017         | Active  |

**Outcomes**:
- R017: Project progress reviewed with blockers and risks documented
- R018: Sprint planned with tasks and estimates

### Personal Persona Routines

#### Daily Routines

| ID    | Name            | Entry Point | Time      | Priority | Dependencies | Status  |
| ----- | --------------- | ----------- | --------- | -------- | ------------ | ------- |
| R019  | Morning Routine | T001, M001   | 07:00     | High     | None         | Active  |
| R020  | Evening Routine | T005        | 21:00     | Medium   | R019         | Active  |
| R021  | Personal Time   | C004        | On-demand | Medium   | None         | Active  |
| R022  | Self-Care       | T003, C004  | On-demand | Medium   | None         | Active  |

**Outcomes**:
- R019: Morning started with energy and clear mind
- R020: Evening concluded with reflection and preparation for next day
- R021: Personal time enjoyed with relationships and activities
- R022: Self-care maintained with health and wellbeing prioritized

#### Weekly Routines

| ID    | Name                    | Entry Point | Time         | Priority | Dependencies | Status  |
| ----- | ----------------------- | ----------- | ------------ | -------- | ------------ | ------- |
| R023  | Weekly Personal Review  | T006, M004  | Sunday 09:00 | Medium   | R019-R022    | Active  |
| R024  | Personal Goal Review    | E005        | On-demand    | Medium   | R023         | Active  |

**Outcomes**:
- R023: Personal week reviewed with accomplishments and learnings
- R024: Personal goals assessed with progress tracked

#### Monthly Routines

| ID    | Name                     | Entry Point | Time               | Priority | Dependencies | Status  |
| ----- | ------------------------ | ----------- | ------------------ | -------- | ------------ | ------- |
| R025  | Monthly Personal Review  | T007        | 1st of month 09:00 | Medium   | R023         | Active  |

**Outcomes**:
- R025: Personal month reviewed with growth and achievements documented

#### Yearly Routines

| ID    | Name                    | Entry Point | Time               | Priority | Dependencies | Status  |
| ----- | ----------------------- | ----------- | ------------------ | -------- | ------------ | ------- |
| R026  | Yearly Personal Review  | T008        | January 1st 10:00  | Medium   | R025         | Active  |

**Outcomes**:
- R026: Personal year reviewed with major life events and growth

### Yoga Teacher Persona Routines

#### Daily Routines

| ID    | Name                 | Entry Point      | Time           | Priority | Dependencies | Status  |
| ----- | -------------------- | ---------------- | -------------- | -------- | ------------ | ------- |
| R027  | Yoga Practice        | C005, M003, T001 | Scheduled      | Low      | None         | Active  |
| R028  | Teaching Preparation | C005             | Before teaching | Low      | R027         | Active  |
| R029  | Practice Review      | After R027       | After practice | Low      | R027         | Active  |

**Outcomes**:
- R027: Yoga practice completed with presence and focus
- R028: Teaching prepared with sequence and intention
- R029: Practice reviewed with learnings and adjustments

#### Weekly Routines

| ID    | Name                    | Entry Point | Time    | Priority | Dependencies | Status  |
| ----- | ----------------------- | ----------- | ------- | -------- | ------------ | ------- |
| R030  | Weekly Practice Review  | T006        | Sunday  | Low      | R027-R029    | Active  |

**Outcomes**:
- R030: Practice week reviewed with progress and insights

## Routines by Entry Point

For complete details on entry points, see [Nicola's Routines Entry Points Catalog](nicola-routines-entry-points.md): Reference catalog of all entry points in Nicola's routines system, organized by type, with trigger conditions, associated personas, and triggered routines.. To configure entry points, see [How to Configure Entry Points](nicola-routines-howto-configure-entry-point.md): Step-by-step guide for configuring entry points in Nicola's routines system, including notification system setup, trigger configuration, and integration with external systems..

### Time-Based Routines

**T001 - Morning Routine Trigger**: R019, R027 (if scheduled)  
**T002 - Work Day Start**: R001  
**T003 - Lunch Break**: R006, R022  
**T004 - Work Day End**: R005  
**T005 - Evening Routine Trigger**: R020  
**T006 - Weekly Review**: R007, R017, R023, R030  
**T007 - Monthly Review**: R009, R025  
**T008 - Yearly Review**: R011, R026

### Calendar-Based Routines

**C001 - Meeting Reminder**: R003, R014  
**C002 - Company Meeting**: R003  
**C003 - Project Meeting**: R018  
**C004 - Personal Event**: R021, R022  
**C005 - Yoga Practice Scheduled**: R027, R028  
**C006 - Standup Meeting**: R014  
**C007 - Strategic Review**: R004, R008, R010, R012

### Notification-Based Routines

**N001 - Task Assigned**: R013, R016  
**N002 - Task Status Changed**: R013  
**N003 - High Priority Task**: R013 (high priority)  
**N004 - Email Received**: R002  
**N005 - Urgent Email**: R002 (urgent)  
**N006 - Project Notification**: R015  
**N007 - Calendar Invite**: R003, R014, R021

### Event-Based Routines

**E001 - Email from Specific Sender**: R002 (specific handling)  
**E002 - Task Deadline Approaching**: R013 (deadline reminder)  
**E003 - Task Overdue**: R013 (overdue handling)  
**E004 - Project Milestone Reached**: R017 (milestone celebration)  
**E005 - Weekly Goal Achieved**: R024

### Manual Routines

**M001 - Start Morning Routine**: R019  
**M002 - Begin Work Day**: R001  
**M003 - Start Yoga Practice**: R027  
**M004 - Begin Weekly Review**: R007, R017, R023  
**M005 - Emergency Override**: All routines (override)  
**M006 - Activate CEO Persona**: R004  
**M007 - Activate PM Persona**: R013  
**M008 - Activate Personal Persona**: R019, R021  
**M009 - Activate Yoga Teacher Persona**: R027

### System Routines

**S001 - Computer Startup**: R001 (if work hours), R019 (if personal time)  
**S002 - App Launch**: R001 (if work app), R013 (if project app)  
**S003 - System Notification**: All routines (system notification handling)  
**S004 - Network Connected**: R001, R013  
**S005 - Low Battery Warning**: All routines (battery warning)

## Routines by Frequency

### Daily Routines

**CEO**: R001, R002, R003, R004, R005, R006  
**PM**: R013, R014, R015, R016  
**Personal**: R019, R020, R021, R022  
**Yoga Teacher**: R027, R028, R029

**Total Daily Routines**: 18

### Weekly Routines

**CEO**: R007, R008  
**PM**: R017, R018  
**Personal**: R023, R024  
**Yoga Teacher**: R030

**Total Weekly Routines**: 7

### Monthly Routines

**CEO**: R009, R010  
**Personal**: R025

**Total Monthly Routines**: 3

### Yearly Routines

**CEO**: R011, R012  
**Personal**: R026

**Total Yearly Routines**: 3

### On-Demand Routines

All routines can be triggered on-demand via manual entry points or conditional logic. See [How to Configure Entry Points](nicola-routines-howto-configure-entry-point.md): Step-by-step guide for configuring entry points in Nicola's routines system, including notification system setup, trigger configuration, and integration with external systems. for configuration details.

## Routine Dependencies

Understanding routine dependencies helps ensure proper execution order. For more on the rationale behind routine design, see [Nicola's Routines - Explanation](nicola-routines-explanation.md): Explanation of the rationale behind personal routines, workflow patterns, and the strategic thinking behind daily, weekly, monthly, and yearly habits..

### Dependency Graph

```
R001 (Work Day Start)
├── R004 (Strategic Review)
├── R005 (Work Day End)
└── R007 (Weekly Review)
    ├── R008 (Strategic Planning)
    ├── R009 (Monthly Review)
    │   ├── R010 (Company Performance Review)
    │   └── R011 (Yearly Review)
    │       └── R012 (Strategic Planning)
    └── R017 (Weekly Project Review)
        └── R018 (Sprint Planning)

R013 (Task Review)
├── R014 (Standup Preparation)
├── R015 (Project Status Check)
├── R016 (Task Planning)
└── R017 (Weekly Project Review)

R019 (Morning Routine)
├── R020 (Evening Routine)
└── R023 (Weekly Personal Review)
    ├── R024 (Personal Goal Review)
    └── R025 (Monthly Personal Review)
        └── R026 (Yearly Personal Review)

R027 (Yoga Practice)
├── R028 (Teaching Preparation)
├── R029 (Practice Review)
└── R030 (Weekly Practice Review)
```

## Routine Statistics

To review and update routines, see [How to Review and Update Routines](nicola-routines-howto-review-routines.md): Step-by-step guide for reviewing and updating routines in Nicola's routines system, including effectiveness evaluation, usage analysis, and change management..

| Persona     | Daily | Weekly | Monthly | Yearly | Total |
| ----------- | ----- | ------ | ------- | ------ | ----- |
| CEO         | 6     | 2      | 2       | 2      | 12    |
| PM          | 4     | 2      | 0       | 0      | 6     |
| Personal    | 4     | 2      | 1       | 1      | 8     |
| Yoga Teacher| 3     | 1      | 0       | 0      | 4     |
| **Total**   | **17**| **7**  | **3**   | **3**  | **30**|

## References

- [Nicola's Routines - Explanation](nicola-routines-explanation.md): Explanation of the rationale behind personal routines, workflow patterns, and the strategic thinking behind daily, weekly, monthly, and yearly habits. - Explanation: Routine rationale
- [Nicola's Routines System Architecture](nicola-routines-architecture.md): Architectural design document explaining the persona/agent model, entry point system, and overall architecture of Nicola's routines system for managing different life roles. - Explanation: System architecture
- [Nicola's Routines Core Principles](nicola-routines-principles.md): Core principles that guide routine definition and execution, ensuring consistency, effectiveness, and alignment with personal and professional goals. - Explanation: Core principles
- [Nicola's Routines Personas Reference](nicola-routines-personas.md): Reference document defining all personas in Nicola's routines system, including activation triggers, context boundaries, routines, and entry points for each persona. - Reference: Persona definitions
- [Nicola's Routines Entry Points Catalog](nicola-routines-entry-points.md): Reference catalog of all entry points in Nicola's routines system, organized by type, with trigger conditions, associated personas, and triggered routines. - Reference: Entry point catalog
- [How to Define a Routine](nicola-routines-howto-define-routine.md): Step-by-step guide for defining new routines in Nicola's routines system, including persona assignment, entry point configuration, and metadata requirements. - Howto: Define routines
- [How to Activate a Persona](nicola-routines-howto-activate-persona.md): Step-by-step guide for activating personas in Nicola's routines system, including automatic and manual activation, context switching, and multi-persona handling. - Howto: Activate personas
- [How to Configure Entry Points](nicola-routines-howto-configure-entry-point.md): Step-by-step guide for configuring entry points in Nicola's routines system, including notification system setup, trigger configuration, and integration with external systems. - Howto: Configure entry points
- [How to Review and Update Routines](nicola-routines-howto-review-routines.md): Step-by-step guide for reviewing and updating routines in Nicola's routines system, including effectiveness evaluation, usage analysis, and change management. - Howto: Review routines
