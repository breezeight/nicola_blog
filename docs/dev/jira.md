---
layout: post
title: "JIRA"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["Management"]
---

# References:

* For any technical issues, please [visit our support center](https://www.atlassian.com/company/contact?_ga=1.188973099.1485114379.1460647216)
* If you would like to request a new feature, please visit our [public-facing instance of JIRA](https://jira.atlassian.com/secure/Dashboard.jspa?_ga=1.76589205.1485114379.1460647216)
* To report a bug, head to [atlassian.com/contact](http://www.atlassian.com/contact?_ga=1.73974674.1485114379.1460647216)
* [Atlassian Answers](https://answers.atlassian.com/questions/topics?_ga=1.182161191.1485114379.1460647216)
  * Have any open questions about how to use a product, set up a workflow, or integrate with another product or language? Please visit Atlassian Answers where you will find questions submitted and answered by the user community, ecosystem developers, and Atlassian staff.
* [Twitter](https://twitter.com/Atlassian)
* [LinkedIn](https://www.linkedin.com/company/atlassian)
* [Facebook](https://www.facebook.com/AtlassianSoftware/)

# Project and Board configuration

* https://answers.atlassian.com/questions/259012/best-practices-for-projects-vs-epics
* 

# JIRA Service Desk

* http://blogs.atlassian.com/2016/10/extend-jira-service-desk-customer-support-new-capabilities/
* http://blogs.atlassian.com/2016/09/5-ways-small-business-use-help-desk/
* http://blogs.atlassian.com/2016/09/4-ways-boost-customer-service-technology/
* 
# Add ON

## JIRA Automation

https://marketplace.atlassian.com/plugins/com.codebarrel.addons.automation/cloud/overview



# Permission and Security

JIRA best practices:

* Only Project Roles are assigned to the Permission Scheme. Users and groups are not included in this phase.
* Assign Project Roles to the users or groups through the project administration page.
* REF: https://confluence.atlassian.com/display/JIRAKB/JIRA+Permissions+made+Simple


Ref:

* Overview: https://confluence.atlassian.com/jirasoftwarecloud/permissions-overview-764478244.html
* Doc https://confluence.atlassian.com/adminjiracloud/managing-project-permissions-776636362.html#Managingprojectpermissions-permission_schemes

## Permission schema

Permission schema is a config that:

* Grant project permission to users, groups, roles (e.g. who can see the project's issues, create, edit and assign them)
* Is associated to 1..N Projects
* From each project you can edit the schema but it will impact all the other project usiging it
* Project Admin - Permissions
  * Debug tool: Permission helper: you can check

Permission can be granted to:


## Groups VS Roles

tl;dr : use only roles in permission and notification schema

REF: https://www.safaribooksonline.com/library/view/practical-jira-administration/9781449309701/ch01.html


Project roles are somewhat similar to groups, the main difference being that group membership is global whereas project role membership is project-specific.

Why?

* you don't need system administration rights to add someone to a project (roles member are a project level setting)
* when you use groups they are shared between project and could be hard to manage when you need to customize a single project.
* Unlike groups, which have the same membership throughout your application, project roles have specific members for each project. 
* Ref: http://stackoverflow.com/questions/3632191/when-and-how-should-one-use-project-roles-instead-of-groups-within-jira


## Roles

Roles can be:

* Application Roles: very general, they can distinguish only if you are a logged user in a given JIRA app.
* Project Roles: more specific, you can add users or groups to a role

To add roles (NB: a role it's a global settings): JIRA Administration - System - Project Roles

To add users to a project role: Enter the project administration - Users and Roles - Add users to a role

NB: Roles could have a default set of users added when you create a project.


Doc:

* https://confluence.atlassian.com/adminjiracloud/managing-project-roles-776636382.html
* https://confluence.atlassian.com/jirasoftwarecloud/managing-project-role-memberships-764478255.html




## Tools

* scheme comparison tools (Administration→Scheme Tools).
* permission helper


# Organize JIRA issues

* http://blogs.atlassian.com/2013/11/organize-jira-issues-subcomponents/


EPIC: Can shown:

* # of issues
* # of completed issues
* estimated time

# JQL

* http://blogs.atlassian.com/2013/02/jql-the-most-flexible-way-to-search-jira-3-of-4/

## Subscription to JQL query via email

http://blogs.atlassian.com/2013/02/jql-the-most-flexible-way-to-search-jira-3-of-4/

# Business Board

Refs:

* http://blogs.atlassian.com/2016/09/jira-core-means-business-introducing-boards-and-mobile-apps/

3 quick ways to filter your tasks on the board by:

* Assigned to me (That’s you!)
* Due this week (Your team needs to work on these now!)
* Keyword ( Type one in and check out the results)

Use for marketing:

http://blogs.atlassian.com/2016/09/organize-your-marketing-campaign-with-jira-core/

# Scrum board

Consigli per le dashboard agile:

* https://confluence.atlassian.com/jiracore/blog/2015/08/5-steps-to-a-killer-jira-dashboard
* https://confluence.atlassian.com/jirasoftware/blog/2015/08/the-7-secrets-of-a-beautiful-agile-dashboard

## Configuration

* add "due date" to every screen : "project config" - "screen config" 
* add fields to the 


Board configuration:

* Issue detail View

## Quick Filters

TIPS: http://blogs.atlassian.com/2013/07/greenhopper-tip-of-the-month-quick-filter-agility/

Quick filters + Epics : Quick filters also work with filtering by epics and versions. Combining all three filter mechanisms give you a very powerful data visualization tool to manage your projects.

Management tip for easy quick filter refactor:

* Create a system shared filter: https://enerlife.atlassian.net/secure/admin/filters/ViewSharedFilters.jspa
* JQL: filter = "name of the filter"


## Board configuration Example

Scrum:

* Configure - Estimation: Estimation statistic = Original Time Estimate; Time Tracking = Remaining Estimate and Time Tracking

Ref:

* [Board estimation](https://confluence.atlassian.com/agile/jira-agile-user-s-guide/configuring-a-board/configuring-estimation-and-tracking)
* Issue subtask don't sum up : https://jira.atlassian.com/browse/GHS-9167
  * workaround: https://jira.atlassian.com/browse/GHS-9167?focusedCommentId=828570&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-828570 


Velocity report:

https://jira.atlassian.com/browse/GHS-8776

# Estimation and Time Tracking

Doc: https://pitchtarget.atlassian.net/secure/ShowTimeTrackingHelp.jspa?decorator=popup#TimeTracking

* Original Estimate
* Remaining Estimate

Sprint report: The values for each issue's Estimate are recorded at the time the sprint is started. Changing the Estimate value afterwards will not be reflected in the Sprint Report.

Configure Board - Estimate:
https://confluence.atlassian.com/jirasoftwarecloud/configuring-estimation-and-tracking-764478030.html
The type of Estimation Statistic you select affects the units that are used by the Estimate field, which appears at the right of each issue in the Backlog:

## Swimlines

Pro and Cons:...

## Reports

## Sub-Task VS Epic VS checklist with markdown

Use Checklist:

* PRO: easy and fast to write
* PRO: don't clutter the backlog
* CONS: cannot be assigned to different assegnee
* CONS: cannot use the time estimate

Use Subtask:

* PRO: don't clutter the backlog
* CONS: the original time estimate of subtasks don't sum up in their parent issue (instead this happens with stories)
* ISSUE: https://jira.atlassian.com/browse/GHS-9167
* IDEA: we could use estimates only at the issue level and block it at the subtask level (Proj Settings - Issue Type - Subtask - Fields: remove time tracking)

Use Epic and avoid subtasks (basically we exclude on level)

* PRO: issue time estimate will sum up in the epic time estimate and make easier to track how the time is spent.
* CONS: the backlog will be cluttered by task that could be instead be less visible as sub-tasks. 

### Sprint report

https://confluence.atlassian.com/agile/jira-agile-user-s-guide/using-a-board/using-reports/viewing-the-sprint-report

* The values for each issue's Estimate are recorded at the time the sprint is started. Changing the Estimate value afterwards will not be reflected in the Sprint Report.

## Rank

Rank ASC


# Notification

TIPS:

* Debug: From "project settings -> Notifications -> Notification Helper" you can debug why a notification is sent or not sent to a specific user


# Priority

http://blogs.atlassian.com/2014/06/organizing-issues-priority-optimize-delivery/

* Failure to be crisp about the definition of priority makes work more confusing to get done.

Priority VS Rank in scrum board

Oriority field gives a bucketed grouping of relative priority: You can then query those buckets using issue search or the various dashboard gadgets.


# Versions

# Assign issue to groups

https://confluence.atlassian.com/jira/how-do-i-assign-issues-to-multiple-users-207489749.html



# Github and Bitbucket Connector

Github:

* https://help.github.com/articles/integrating-jira-with-your-projects/
* 
    


# JIRA Projects Examples

## BitBucket Server

https://jira.atlassian.com/projects/BSERV?selectedItem=com.atlassian.jira.jira-projects-plugin:components-page


## Jenkins

How the Jenkins 2.x brainstorming is managed:

* They create a page on confluence: https://wiki.jenkins-ci.org/display/JENKINS/Jenkins+2.0
* To collect those feedbacks in a manageable way, we have prepared a number of ["2.0 planning tickets"](https://issues.jenkins-ci.org/issues/?jql=labels%3D2.0%20AND%20(%20status%20%3D%20open%20or%20status%20%3D%20%22In%20Progress%22)), divided under several themes called "epic tickets" in JIRA. This page and its children walk you through the main parts of those epics and details, and takes you to the actual tickets.
* https://issues.jenkins-ci.org/browse/JENKINS-31152?jql=issuetype%20%3D%20Epic%20AND%20status%20%3D%20Open%20AND%20labels%20%3D%202.0



# MISC Free Plugins

## Recurring Tasks

Free plugin:
https://marketplace.atlassian.com/plugins/com.gebsun.atlassian.rtasks/cloud/overview

## Gantt

https://marketplace.atlassian.com/plugins/eu.wisoft.gantt-ondemand/cloud/overview


## Slack

https://marketplace.atlassian.com/plugins/eu.wisoft.slack.jira/cloud/overview

## Epic Sum Up

https://marketplace.atlassian.com/plugins/aptis.plugins.epicSumUpFree/cloud/overview

https://answers.atlassian.com/questions/32519842/how-do-i-use-epic-sum-up
