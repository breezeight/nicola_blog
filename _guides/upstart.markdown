---
layout: post
title: "Upstart"
date: 2014-03-16 19:59:15 +0100
comments: true
categories: 
---
# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

REF:

* http://www.jamescoyle.net/tag/upstart
* https://www.digitalocean.com/community/tutorials/the-upstart-event-system-what-it-is-and-how-to-use-it

* `service  --status-all`
* `service opsworks-agent status`


The AWS OpsWorks agent is running as PID 28270


~~~
 [ + ]  acpid
 [ + ]  apparmor
 [ ? ]  apport
 [ + ]  atd
 [ - ]  autofs
 [ ? ]  console-setup
 [ + ]  cron
 [ ? ]  cryptdisks
 [ ? ]  cryptdisks-early
 [ - ]  dbus
 [ ? ]  dns-clean
 [ + ]  friendly-recovery
 [ - ]  grub-common
 [ ? ]  irqbalance
 [ ? ]  killprocs
 [ ? ]  kmod
 [ + ]  monit
 [ ? ]  networking
 [ + ]  nginx
 [ + ]  ntp
 [ ? ]  ondemand
 [ ? ]  open-vm-tools
 [ ? ]  opsworks-agent
 [ ? ]  pppd-dns
 [ - ]  procps
 [ ? ]  rc.local
 [ + ]  resolvconf
 [ + ]  rpcbind
 [ - ]  rsync
 [ + ]  rsyslog
 [ ? ]  screen-cleanup
 [ ? ]  sendsigs
 [ - ]  ssh
 [ - ]  sudo
 [ + ]  udev
 [ ? ]  umountfs
 [ ? ]  umountnfs.sh
 [ ? ]  umountroot
 [ - ]  unattended-upgrades
 [ - ]  urandom
~~~
