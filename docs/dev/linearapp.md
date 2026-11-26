# Linear App

view Triage di tutti i projects
CONS: non puoi vedere le draft nelle views
NOTA: le draft, vanno attivate => customize sidebar 


I filter filtrano solo ulteriormente la view già settata, vanno in AND rispetto ai default, se vuoi cambiare i default vain in edit

Team equivalgono ad areee di projects

Progetti possono essere cross team

Le triage issue possono non essere in un progetto

Hanno un triage agent

issue belongs to 1 team
issue can belong 0-1 project

un project ha 1-N team



## issue associations to teams and projects and milestones

In Linear, issues have two key associations:                                                                                                                                
  1. Team - every issue belongs to exactly one team (e.g., ADA-1 belongs to AD-CC)                                                                                            
  2. Project - an issue can optionally be assigned to a project                                                                                                               
                                                                                                                                                               5             
  When a project spans multiple teams:                                                                                                                                        
  - Issues from Team A can be added to the project                                                                                                                            
  - Issues from Team B can be added to the same project                                                                                                                       
  - Both issues can then be assigned to the same milestone within that project                                                                                                
                                                                                                                                                                              
  Example:                                                                                                                                                                    
  - Project "Strategy Ops Agents" spans Team AD-CC and Team AD-Backend                                                                                                        
  - Milestone "M1: Foundation" exists in that project                                                                                                                         
  - Issue ADA-5 (from AD-CC) can be assigned to M1                                                                                                                            
  - Issue ADB-10 (from AD-Backend) can also be assigned to M1                                                                                                                 
  - Both issues now share the same milestone, despite belonging to different teams                                                                                            
                                                                                                                                                                              
  "Accessible" means: issues from any participating team can be organized into the project's milestones. The milestone acts as a shared container across teams within that    
  project's scope.   



# Cycles

https://linear.app/docs/use-cycles


## Cycle calendars
Keep up with your Linear cycles in your preferred calendar application by visiting your team's Cycles page, click on the overflow menu on a cycle, and hover over Subscribe to cycle calendar. Choose to add to Google Calendar, copy a feed URL, or download the calendar as an .ics file.

## Cycle capacity
On the Cycles view, cycles that have not yet started will display a capacity dial that shows an estimate on whether your team will be likely to complete all the issues added to the cycle.

Capacity is calculated from the velocity of the previous three completed cycles, i.e. the number of issues or estimate points completed in these cycles. If the team has not completed any cycles previously, capacity will be roughly estimated from the number of members in the team.

## Cycle Scope

The scope of a cycle is the sum of the story points of all issues assigned to the cycle.