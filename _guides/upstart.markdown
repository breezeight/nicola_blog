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

# Create an UpStart service

* Upstart scripts are located in `/etc/init/` directory with a `.conf` extension.
* The scripts are called ‘System Jobs’ and run using sudo privileges.
 
    
Just like system jobs we also have ‘User Jobs’ that are located at `$HOME/.init/` directory

An Upstart script is a combination of:

* states: Currently upstart supports 10 states(waiting, starting, pre-start, spawned, post-start, running, pre-stop, stopping, killed and post-stop..)
  * [Doc](http://upstart.ubuntu.com/cookbook/#job-states)
* events

## Stanzas and Configuration



# CLI tools

`initctl` allows a system administrator to communicate and interact with the Upstart init(8) daemon.


# Examples

## Node.js

Here is a simple upstart script which starts node.js server whenever system boots.


~~~
# /etc/init/nodejs.conf
 
description "node.js server"
author      "Siva Gollapalli"
 
# used to be: start on startup
# until we found some mounts weren't ready yet while booting:
#start on started mountall
# If network interface is wireless
start on (local-filesystems and net-device-up IFACE=wlan0)
# If network interface is Ethernet uncomment below line and comment above line
#start on (local-filesystems and net-device-up IFACE=eth0)
 
stop on shutdown
 
# Automatically Respawn:
respawn
respawn limit 99 5
 
script
    # Not sure why $HOME is needed, but we found that it is:
    export HOME="/home/siva/work/myproject"
 
    exec /usr/local/bin/node $HOME/node/notify.js 13002 >> /var/log/node.log 2>&1
end script
 
post-start script
   # Optionally put a script here that will notify you node has (re)started
   # /root/bin/hoptoad.sh "node.js has started!"
end script
~~~
