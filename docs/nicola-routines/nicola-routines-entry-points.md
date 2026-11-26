---
title: "Nicola's Routines Entry Points Catalog"
abstract: >
  Reference catalog of all entry points in Nicola's routines system, organized by type, 
  with trigger conditions, associated personas, and triggered routines.
type: reference
---

# Nicola's Routines Entry Points Catalog

## 📘 Purpose & Scope

This document provides a complete catalog of all entry points in Nicola's routines system. Entry points are triggers that initiate routines. Each entry point entry includes ID, name, type, trigger condition, associated personas, and triggered routines.

## Entry Point Schema

**Required Fields**:
- **ID**: Unique identifier (e.g., T001, C001, N001)
- **Name**: Human-readable name
- **Type**: Entry point category (Time, Calendar, Notification, Event, Manual, System)
- **Trigger**: Specific condition that activates entry point
- **Persona**: Which persona(s) this entry point activates
- **Routines**: Which routines this entry point triggers
- **Status**: Active, Inactive, or Deprecated

**Optional Fields**:
- **Conditional Logic**: Optional if-then conditions
- **Frequency**: How often this entry point triggers
- **Timezone**: Timezone handling (if time-based)
- **Integration**: External system integration details

## Time-Based Entry Points

| ID | Name | Trigger | Persona | Routines | Status |
|----|------|--------|---------|----------|--------|
| T001 | Morning Routine Trigger | 07:00 daily | Personal | Morning routine | Active |
| T002 | Work Day Start | 09:00 workdays | CEO | Work day start routine | Active |
| T003 | Lunch Break | 12:30 workdays | Personal, CEO | Lunch routine | Active |
| T004 | Work Day End | 18:00 workdays | CEO | Work day end routine | Active |
| T005 | Evening Routine Trigger | 21:00 daily | Personal | Evening routine | Active |
| T006 | Weekly Review | Sunday 09:00 | Personal, CEO, PM | Weekly review routine | Active |
| T007 | Monthly Review | 1st of month 09:00 | Personal, CEO | Monthly review routine | Active |
| T008 | Yearly Review | January 1st 10:00 | Personal, CEO | Yearly review routine | Active |

## Calendar-Based Entry Points

| ID | Name | Trigger | Persona | Routines | Status |
|----|------|--------|---------|----------|--------|
| C001 | Meeting Reminder | 15 minutes before calendar event | CEO, PM | Meeting preparation routine | Active |
| C002 | Company Meeting | Calendar event with "Company" tag | CEO | Company meeting routine | Active |
| C003 | Project Meeting | Calendar event with "Project" tag | PM | Project meeting routine | Active |
| C004 | Personal Event | Calendar event with "Personal" tag | Personal | Personal event routine | Active |
| C005 | Yoga Practice Scheduled | Calendar event with "Yoga" tag | Yoga Teacher | Yoga practice routine | Active |
| C006 | Standup Meeting | Calendar event with "Standup" tag | PM | Standup preparation routine | Active |
| C007 | Strategic Review | Calendar event with "Strategic" tag | CEO | Strategic review routine | Active |

## Notification-Based Entry Points

| ID | Name | Trigger | Persona | Routines | Status |
|----|------|--------|---------|----------|--------|
| N001 | Task Assigned | OpenProject task assignment notification | PM, CEO | Task review routine | Active |
| N002 | Task Status Changed | OpenProject task status change notification | PM | Task status review routine | Active |
| N003 | High Priority Task | OpenProject high-priority task notification | CEO, PM | High-priority task routine | Active |
| N004 | Email Received | Email notification from work domain | CEO | Email review routine | Active |
| N005 | Urgent Email | Email marked as urgent | CEO | Urgent email routine | Active |
| N006 | Project Notification | Project management tool notification | PM | Project notification routine | Active |
| N007 | Calendar Invite | Calendar invitation received | CEO, PM, Personal | Calendar invite routine | Active |

## Event-Based Entry Points

| ID | Name | Trigger | Persona | Routines | Status |
|----|------|--------|---------|----------|--------|
| E001 | Email from Specific Sender | Email received from predefined sender list | CEO | Specific sender routine | Active |
| E002 | Task Deadline Approaching | Task deadline within 24 hours | PM, CEO | Deadline reminder routine | Active |
| E003 | Task Overdue | Task past deadline | PM, CEO | Overdue task routine | Active |
| E004 | Project Milestone Reached | Project milestone completion event | PM | Milestone celebration routine | Active |
| E005 | Weekly Goal Achieved | Weekly goal completion event | Personal | Goal achievement routine | Active |

## Manual Entry Points

| ID | Name | Trigger | Persona | Routines | Status |
|----|------|--------|---------|----------|--------|
| M001 | Start Morning Routine | User explicitly activates | Personal | Morning routine | Active |
| M002 | Begin Work Day | User explicitly activates | CEO | Work day start routine | Active |
| M003 | Start Yoga Practice | User explicitly activates | Yoga Teacher | Yoga practice routine | Active |
| M004 | Begin Weekly Review | User explicitly activates | Personal, CEO, PM | Weekly review routine | Active |
| M005 | Emergency Override | User explicitly activates any persona | All | Emergency routine | Active |
| M006 | Activate CEO Persona | User explicitly activates | CEO | CEO activation routine | Active |
| M007 | Activate PM Persona | User explicitly activates | PM | PM activation routine | Active |
| M008 | Activate Personal Persona | User explicitly activates | Personal | Personal activation routine | Active |
| M009 | Activate Yoga Teacher Persona | User explicitly activates | Yoga Teacher | Yoga Teacher activation routine | Active |

## System Entry Points

| ID | Name | Trigger | Persona | Routines | Status |
|----|------|--------|---------|----------|--------|
| S001 | Computer Startup | System startup event | CEO, Personal | Startup routine | Active |
| S002 | App Launch | Specific app launch event | CEO, PM | App-specific routine | Active |
| S003 | System Notification | OS-level system notification | All | System notification routine | Active |
| S004 | Network Connected | Network connection established | CEO, PM | Network connection routine | Active |
| S005 | Low Battery Warning | System low battery warning | All | Battery warning routine | Active |

## Entry Points by Persona

### CEO Persona Entry Points

**Time-Based**: T002, T003, T004, T006, T007, T008  
**Calendar-Based**: C001, C002, C007  
**Notification-Based**: N001, N003, N004, N005, N007  
**Event-Based**: E001, E002, E003  
**Manual**: M002, M005, M006  
**System**: S001, S002, S003, S004, S005

### PM Persona Entry Points

**Time-Based**: T006  
**Calendar-Based**: C001, C003, C006  
**Notification-Based**: N001, N002, N003, N006, N007  
**Event-Based**: E002, E003, E004  
**Manual**: M004, M005, M007  
**System**: S001, S002, S003, S004, S005

### Personal Persona Entry Points

**Time-Based**: T001, T003, T005, T006, T007, T008  
**Calendar-Based**: C004  
**Notification-Based**: N007  
**Event-Based**: E005  
**Manual**: M001, M004, M005, M008  
**System**: S001, S003, S005

### Yoga Teacher Persona Entry Points

**Time-Based**: T001 (if scheduled)  
**Calendar-Based**: C005  
**Manual**: M003, M005, M009  
**System**: S003, S005

## Entry Points by Type Summary

| Type | Count | Active | Inactive | Deprecated |
|------|-------|--------|----------|------------|
| Time-Based | 8 | 8 | 0 | 0 |
| Calendar-Based | 7 | 7 | 0 | 0 |
| Notification-Based | 7 | 7 | 0 | 0 |
| Event-Based | 5 | 5 | 0 | 0 |
| Manual | 9 | 9 | 0 | 0 |
| System | 5 | 5 | 0 | 0 |
| **Total** | **41** | **41** | **0** | **0** |

## Entry Point Integration Details

### Calendar Integration

**System**: Google Calendar  
**Integration Method**: Calendar API monitoring  
**Update Frequency**: Real-time  
**Supported Event Types**: Meetings, Reminders, All-day events

### Task Management Integration

**System**: OpenProject  
**Integration Method**: Webhook notifications  
**Update Frequency**: Real-time  
**Supported Event Types**: Task assignment, Status changes, Comments

### Email Integration

**System**: Email client (varies)  
**Integration Method**: Email API or IMAP monitoring  
**Update Frequency**: Polling (every 5 minutes)  
**Supported Event Types**: New email, Urgent email, Specific sender

### System Integration

**System**: Operating System (macOS)  
**Integration Method**: System events and notifications  
**Update Frequency**: Real-time  
**Supported Event Types**: Startup, App launch, System notifications

## Entry Point Conditional Logic

Some entry points have conditional logic that determines when they trigger:

**C001 - Meeting Reminder**:
- IF calendar event has "Company" tag THEN activate CEO persona
- IF calendar event has "Project" tag THEN activate PM persona
- IF calendar event has "Personal" tag THEN activate Personal persona

**N001 - Task Assigned**:
- IF task priority is "High" THEN activate CEO persona
- IF task priority is "Normal" THEN activate PM persona
- IF task is from company project THEN activate CEO persona

**T001 - Morning Routine**:
- IF weekday THEN include work preparation steps
- IF weekend THEN include personal activities only
- IF yoga scheduled THEN activate Yoga Teacher persona

## Entry Point Status Management

**Active**: Entry point is currently active and monitoring for triggers  
**Inactive**: Entry point is temporarily disabled (can be reactivated)  
**Deprecated**: Entry point is no longer used (kept for historical reference)

**Status Change Process**:
1. Update entry point status in this catalog
2. Update associated routines if needed
3. Update persona definitions if needed
4. Document reason for status change
5. Update cross-references

## References

- {{ link_with_abstract("nicola-routines-architecture.md") }} - System architecture including entry point system
- {{ link_with_abstract("nicola-routines.md") }} - Routines organized by entry point
- {{ link_with_abstract("nicola-routines-personas.md") }} - Personas organized by entry point
- {{ link_with_abstract("nicola-routines-howto-configure-entry-point.md") }} - How to configure entry points
