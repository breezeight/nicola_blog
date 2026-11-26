---
title: "How to Configure Entry Points"
abstract: >
  Step-by-step guide for configuring entry points in Nicola's routines system, including 
  notification system setup, trigger configuration, and integration with external systems.
type: howto
---

# How to Configure Entry Points

> [!NOTE]
> For entry point catalog and definitions, see {{ link_with_abstract("nicola-routines-entry-points.md") }}. For system architecture, see {{ link_with_abstract("nicola-routines-architecture.md") }}.

## 📘 Purpose & Scope

This guide provides step-by-step instructions for configuring entry points in Nicola's routines system. Entry points are triggers that initiate routines and integrate with external systems like calendars, notifications, and task management tools.

## Prerequisites

- Understanding of entry point system (see {{ link_with_abstract("nicola-routines-entry-points.md") }})
- Understanding of routine system (see {{ link_with_abstract("nicola-routines.md") }})
- Access to external systems (calendar, notifications, etc.)

## Step 1: Identify Entry Point Need

**Action**: Determine what entry point is needed.

**Questions to Answer**:
- What should trigger this entry point?
- Which persona(s) should this entry point activate?
- Which routine(s) should this entry point trigger?
- What type of entry point is this?

**Entry Point Types**:
- **Time-based**: Scheduled times
- **Calendar-based**: Calendar events
- **Notification-based**: Notifications
- **Event-based**: Specific events
- **Manual**: User activation
- **System**: System events

**Example**:
- Need: Trigger routine when task assigned
- Type: Notification-based
- Persona: PM
- Routine: Task review routine

**Verification**: You can clearly define the entry point need.

## Step 2: Check Existing Entry Points

**Action**: Check if suitable entry point already exists.

**Process**:
1. Review entry point catalog (see {{ link_with_abstract("nicola-routines-entry-points.md") }})
2. Search for similar entry points
3. Check if existing entry point can be reused
4. Determine if new entry point is needed

**Example**:
- Need: Trigger routine when task assigned
- Check: N001 (Task Assigned) already exists
- Decision: Can reuse N001 or create variant

**Verification**: You've checked existing entry points.

## Step 3: Define Entry Point Metadata

**Action**: Define entry point metadata.

**Required Metadata**:
- **ID**: Unique identifier (next available ID)
- **Name**: Human-readable name
- **Type**: Entry point category
- **Trigger**: Specific condition that activates entry point
- **Persona**: Which persona(s) this activates
- **Routines**: Which routines this triggers
- **Status**: Active, Inactive, or Deprecated

**Optional Metadata**:
- **Conditional Logic**: Optional if-then conditions
- **Frequency**: How often this triggers
- **Timezone**: Timezone handling
- **Integration**: External system integration details

**Example**:
- ID: N001
- Name: Task Assigned
- Type: Notification-based
- Trigger: OpenProject task assignment notification
- Persona: PM, CEO
- Routines: Task review routine
- Status: Active

**Verification**: Entry point metadata is defined.

## Step 4: Configure Time-Based Entry Points

**Action**: Configure entry points triggered by time.

**Process**:
1. Set trigger time (e.g., 07:00 daily)
2. Configure timezone handling
3. Set recurrence pattern (daily, weekly, etc.)
4. Configure conditional logic if needed

**Configuration Steps**:
1. Set time: Specify exact time (HH:MM format)
2. Set frequency: Daily, Weekly, Monthly, Yearly
3. Set days: Which days of week (if weekly)
4. Set timezone: Handle timezone conversions
5. Set conditions: Optional conditional logic

**Example**:
- Entry Point: T001 (Morning Routine Trigger)
- Time: 07:00
- Frequency: Daily
- Timezone: Local timezone
- Conditions: None

**Verification**: Time-based entry point is configured.

## Step 5: Configure Calendar-Based Entry Points

**Action**: Configure entry points triggered by calendar events.

**Process**:
1. Connect to calendar system (Google Calendar, etc.)
2. Configure event monitoring
3. Set trigger conditions (time before event, event tags, etc.)
4. Configure event filtering

**Configuration Steps**:
1. **Calendar Integration**: Connect to calendar API
2. **Event Monitoring**: Set up event monitoring
3. **Trigger Conditions**: Set when to trigger (e.g., 15min before)
4. **Event Filtering**: Filter events by tags, type, etc.
5. **Persona Mapping**: Map event types to personas

**Example**:
- Entry Point: C001 (Meeting Reminder)
- Calendar: Google Calendar
- Trigger: 15 minutes before calendar event
- Filter: Events with "Company" or "Project" tags
- Persona: CEO (Company), PM (Project)

**Verification**: Calendar-based entry point is configured.

## Step 6: Configure Notification-Based Entry Points

**Action**: Configure entry points triggered by notifications.

**Process**:
1. Connect to notification system (OpenProject, email, etc.)
2. Configure notification monitoring
3. Set trigger conditions (notification type, source, etc.)
4. Configure notification filtering

**Configuration Steps**:
1. **Notification Integration**: Connect to notification API
2. **Notification Monitoring**: Set up notification monitoring
3. **Trigger Conditions**: Set when to trigger
4. **Notification Filtering**: Filter notifications by type, source, etc.
5. **Persona Mapping**: Map notification types to personas

**Example**:
- Entry Point: N001 (Task Assigned)
- System: OpenProject
- Trigger: Task assignment notification
- Filter: All tasks
- Persona: PM (normal), CEO (high priority)

**Verification**: Notification-based entry point is configured.

## Step 7: Configure Event-Based Entry Points

**Action**: Configure entry points triggered by specific events.

**Process**:
1. Identify event source
2. Configure event monitoring
3. Set trigger conditions
4. Configure event filtering

**Configuration Steps**:
1. **Event Source**: Identify where events come from
2. **Event Monitoring**: Set up event monitoring
3. **Trigger Conditions**: Set when to trigger
4. **Event Filtering**: Filter events by criteria
5. **Persona Mapping**: Map event types to personas

**Example**:
- Entry Point: E001 (Email from Specific Sender)
- Source: Email system
- Trigger: Email received from predefined sender list
- Filter: Senders in list
- Persona: CEO

**Verification**: Event-based entry point is configured.

## Step 8: Configure Manual Entry Points

**Action**: Configure entry points triggered manually.

**Process**:
1. Define manual trigger mechanism
2. Configure activation command
3. Set persona activation
4. Configure routine triggering

**Configuration Steps**:
1. **Trigger Mechanism**: Define how user activates (command, button, etc.)
2. **Activation Command**: Set command or action
3. **Persona Activation**: Set which persona activates
4. **Routine Triggering**: Set which routines trigger

**Example**:
- Entry Point: M001 (Start Morning Routine)
- Trigger: User command "Start morning routine"
- Persona: Personal
- Routine: Morning routine

**Verification**: Manual entry point is configured.

## Step 9: Configure System Entry Points

**Action**: Configure entry points triggered by system events.

**Process**:
1. Identify system event source
2. Configure system event monitoring
3. Set trigger conditions
4. Configure event filtering

**Configuration Steps**:
1. **System Integration**: Connect to system events
2. **Event Monitoring**: Set up system event monitoring
3. **Trigger Conditions**: Set when to trigger
4. **Event Filtering**: Filter events by type
5. **Persona Mapping**: Map event types to personas

**Example**:
- Entry Point: S001 (Computer Startup)
- Source: Operating system
- Trigger: System startup event
- Filter: All startups
- Persona: CEO (work hours), Personal (personal time)

**Verification**: System entry point is configured.

## Step 10: Configure Conditional Logic

**Action**: Configure conditional logic for entry points.

**Process**:
1. Identify conditions needed
2. Define if-then logic
3. Configure condition evaluation
4. Set up conditional routing

**Conditional Logic Examples**:
- **Time-based**: IF weekday THEN activate CEO, IF weekend THEN activate Personal
- **Event-based**: IF high priority THEN activate CEO, IF normal THEN activate PM
- **Calendar-based**: IF Company tag THEN activate CEO, IF Project tag THEN activate PM

**Example**:
- Entry Point: C001 (Meeting Reminder)
- Condition: IF calendar event has "Company" tag THEN activate CEO persona
- Condition: IF calendar event has "Project" tag THEN activate PM persona
- Condition: IF calendar event has "Personal" tag THEN activate Personal persona

**Verification**: Conditional logic is configured.

## Step 11: Document Entry Point

**Action**: Add entry point to catalog.

**Process**:
1. Open entry point catalog (see {{ link_with_abstract("nicola-routines-entry-points.md") }})
2. Add entry point to appropriate type section
3. Add entry point to persona section
4. Update entry point statistics
5. Add integration details if needed

**Documentation Format**:
- Use table format for entry point listing
- Include all metadata
- Cross-reference related documents
- Follow existing documentation style

**Example**:
Add to Notification-Based Entry Points table:
```
| N001 | Task Assigned | OpenProject task assignment notification | PM, CEO | Task review routine | Active |
```

**Verification**: Entry point is documented in catalog.

## Step 12: Test Entry Point

**Action**: Verify entry point works correctly.

**Process**:
1. Trigger entry point (manually or wait for automatic trigger)
2. Verify persona activates
3. Verify routines trigger
4. Check for errors
5. Adjust configuration if needed

**Testing Checklist**:
- [ ] Entry point triggers correctly
- [ ] Persona activates as expected
- [ ] Routines trigger correctly
- [ ] Conditional logic works
- [ ] No errors occur
- [ ] Integration works properly

**Verification**: Entry point works correctly.

## Troubleshooting

### Entry Point Not Triggering

**Problem**: Entry point doesn't trigger when expected.

**Solutions**:
- Check trigger configuration
- Verify monitoring is active
- Check integration connection
- Verify conditions are met
- Test trigger manually

### Integration Not Working

**Problem**: External system integration fails.

**Solutions**:
- Check API credentials
- Verify API connection
- Check API permissions
- Review integration logs
- Test integration separately

### Conditional Logic Not Working

**Problem**: Conditional logic doesn't evaluate correctly.

**Solutions**:
- Review condition definitions
- Check condition evaluation logic
- Test conditions individually
- Verify condition syntax
- Check condition data

### Persona Not Activating

**Problem**: Entry point triggers but persona doesn't activate.

**Solutions**:
- Check persona mapping
- Verify persona is available
- Check priority rules
- Verify context boundaries
- Test persona activation separately

## References

- {{ link_with_abstract("nicola-routines-entry-points.md") }} - Entry point catalog
- {{ link_with_abstract("nicola-routines-architecture.md") }} - System architecture including entry point system
- {{ link_with_abstract("nicola-routines.md") }} - Routines organized by entry point
- {{ link_with_abstract("nicola-routines-personas.md") }} - Personas organized by entry point
