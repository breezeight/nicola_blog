

## On Boarding

### Stay updated


- Projects Activity of all members: Top Left Menu > Activity  (All Projects or a specific project)

- Top Right Menu > All My Activity 


#### Notifications


### Meeting

#### HOWTO schedule a meeting

#### HOWTO create a meeting agenda

Select the issue > Meetings Tab> Add to meeting


#### Milestones Overview

#### Calendar integration (Google Calendar)

TODO:
- Milestones Overview
- Calendar integration (Google Calendar)


### Log Time

#### HOWTO get an overview of PERSONAL time spent 

User Menù (top right) > My Page > My Spent Time Widget

#### HOWTO log time on an issue

- Select the issue > Estimate and time > Spent time
- Alternatively, you can add the time spent column to the issue list view and log time from there.

## Projects Hierarchy

A hierarchy in OpenProject defines parent–child relationships between projects and their related configurations. It determines how settings, data, and permissions propagate from parent projects to subprojects.

Elements Supporting Inheritance:

| Element                        | Inheritance Behavior                                                                    | Configuration Scope                                    |
| ------------------------------ | --------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **Project Structure**          | Projects can have multiple nested subprojects forming a tree.                           | Controlled by project creation (parent–child linkage). |
| **Work Package Types**         | Subprojects inherit available work package types from their parent if configured.       | In *Administration → Work package types*.              |
| **Custom Fields**              | Custom fields can be applied globally or restricted to specific project hierarchies.    | In *Administration → Custom fields*.                   |
| **Versions (Shared Versions)** | Versions can be shared across a hierarchy if “Share with project hierarchy” is enabled. | In *Project Settings → Versions*.                      |


Elements Not Inherited:

- Memberships and Permissions: Users and roles do not automatically propagate. Each project manages its own memberships.
- Budgets, Workflows, and Queries: These remain project-specific unless configured separately.

Best Practices

- Use parent projects as templates for subprojects to maintain consistency.
- Limit shared configurations to reduce confusion.

### HOWTO Enable Inheritance:

- Work Package Types: `Administration → Work package types → Edit → Assign to project hierarchy`
- Custom Fields: `Administration → Custom fields → Apply to selected projects (and subprojects)`
- Shared Versions: `Project Settings → Versions → Sharing → With project hierarchy`

### HOWTO view all projects in the hierarchy

To see all projects, you need to go to the HOME page (top left menù).

### Howto share versions between projects



### Assignable Users

- Assignable users are only those who are project members with the “Assign work packages” permission.
- Memberships don’t inherit between parent and subprojects. Users in a parent project aren’t assignable in its subprojects, and users in a subproject aren’t assignable in the parent unless added to both. Membership and permissions are project-specific.



### Overview of All Projects Milestones

HOME page (top left menù) > Gantt Charts > "Milestones"


## Meetings

## Cost Management

### Budget
https://www.openproject.org/docs/user-guide/budgets/

#### Budget Overview

[Epic: New dashboard with widgets for projects, portfolios and programs in the "Overview"](https://community.openproject.org/projects/design-system/work_packages/65846/relations)
[Figma](https://www.figma.com/design/kjzHe0qOLme1LXCjLoTBFV/Overview-and-Dashboard?node-id=585-21108&p=f&t=h9TYNkJ2FjTQJKMT-0)


### Time and Cost Reports

- https://www.openproject.org/docs/user-guide/time-and-costs/reporting/
- https://www.youtube.com/watch?v=2B_CXZRsZxI


Required modules:
- Time Tracking
- Cost Reports

### Remaining work

ISSUE: https://community.openproject.org/projects/stream-time-and-costs/work_packages/22800/activity



### User Rate

- Every user have a default rate set in the user profile.
- User Rate can be set per project and the rate can change in time.



#### HOWTO set user rate

User Menù (top right) > Administration > Users > <SELECT USER> > Rate History




## Examples

### The OpenProject itself

https://community.openproject.org/projects