---
layout: post
title: "Runit"
date: 2014-03-16 19:59:15 +0100
comments: true
categories: 
---
# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}


# References

* http://kchard.github.io/runit-quickstart/

# Intro

runit is a cross-platform Unix init scheme with service supervision, a replacement for sysvinit, and other init scheme

The design of runit takes a very "Unixy" approach by breaking down functionality into several small utilities each responsible for a single task.

The core runit utilities are `runsvdir`, `runsv`, `chpst`, `svlogd`, and `sv`.

# Run a service

Most linux distributions should have a runit package available in their repositories, for example debian/ubuntu has a runit package that don't replace the init system.

`/usr/bin/runsvdir -P /etc/service` :  

* this command is watching the /etc/service directory for files used to configure a monitored service.
* A monitored service is configured by adding a subdirecotry to /etc/service with a `run` script in it
* When runsvdir finds a new service configuration, it starts a new `runsv` process to manage the service.

# Manually Managing Services: runsv and sv

Finally, let's take a look at the `sv` utility. sv is used to manually manage your services.

* To check the status of the example service run: `sv status example`
* To stop the example service run: `sv stop example`
  * NOTE: Once you stop a service with sv, it will not be restarted automatically until you explicitly restart it.

* To start the service again run: `sv start example`
* To stop and then start a service run: `sv restart example`

`sv man` page to see additional options.


`runsv` is started by `runsvdir` for each service [ see runsv man page for details](http://smarden.org/runit/runsv.8.html). For each service it will search for:

* `<service_name>/run` script
* `<service_name>/down` script
* `<service_name>/finish` script
* `<service_name>/down` file (it can be empty) : if this file exists runsv will not attempt to start the service

NOTE: If ./run or ./finish exit immediately, runsv waits a second before starting ./finish or restarting ./run.


# Log

svlogd

When runsvdir notices a monitor configuration in a new directory under /etc/service, it looks for a sub directory named log. If it finds one it starts a new runsv process that will execute and monitor the run script in the log directory.

# Cheatsheet

# Chef Cookbook 

