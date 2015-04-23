---
layout: post
title: "Monit"
date: 2014-03-16 19:59:15 +0100
comments: true
categories: 
---
# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}


# References

* [Monit Doc](http://mmonit.com/monit/documentation/monit.html)
* [Digital Ocean Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-monit)

# Intro

What monit can do:

* start/stop process
* send alert (email)
* monitor CPU/RAM
* monitor network connections
* run periodic script for check


# Cheatsheet

* `monit status` displays monit’s details
* By default, it is set up to check that services are running every 2 minutes and stores its log file in `/var/log/monit.log`
  * These settings can be altered at the beginning of the configuration file in the `set daemon` and set `logfile` lines respectively.

# Chef Cookbook 

see my chef guide
