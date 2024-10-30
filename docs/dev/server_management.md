---
layout: post
title: "Server Management"
date: 2014-07-02 20:48:22 +0100
comments: true
categories: 
---


[Process Supervision is Not Service Management](http://jtimberman.housepub.org/blog/2012/12/29/process-supervision-solved-problem/)


Looking around a lot of people are running graphite, collectd, statsd, cacti, zabbix, zenoss, monit or a number of other tools. I wanted something modern that would work with what we had. Collectd was what was running on Engine Yard so naturally started there.


collectd:

* C at core
* python for plugins




Sensu http://sensuapp.org/ :

* ruby


fluentd:

* ruby
* centralize log

logstash

* centralize log

# Init

## Intro

REF: 

* https://felipec.wordpress.com/2013/11/04/init/

What should an init system do? [Here](https://felipec.wordpress.com/2013/11/04/init/) the author describes some of the basic function of init using ruby.

* Mount the filesystem
* Automaticcaly start services managing dependencies
* Socket activation
* ....

## Monit

* [Monit guide](monit.md)

## Upstart

* [Upstar guide](upstart.md)


# Sidekiq Management

* http://librelist.com/browser//sidekiq/2012/11/15/redis-sidekiq-can-t-be-used-for-critical-jobs/#92b1d0027749e5ed76de1389095832df
* http://oldblog.antirez.com/post/redis-persistence-demystified.html

# AWS monitoring with DatadogHQ


## Setup

* Create a Iam user (and create the access key)and config as described here: http://docs.datadoghq.com/integrations/aws/
* Go to integrations and add the access key and secret.
