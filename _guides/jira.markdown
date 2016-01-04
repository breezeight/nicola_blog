---
layout: post
title: "JIRA"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["Management"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}


# References:

# Project and Board configuration

* https://answers.atlassian.com/questions/259012/best-practices-for-projects-vs-epics
* 

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



