---
layout: post
title: "SystemD"
date: 2014-03-15 15:19:49 +0100
comments: true
categories: 
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# SYSTEMD
systemctl is your interface to systemd, the init system used in CoreOS. 
Units can be, for example, services (.service), mount points (.mount), devices (.device) or sockets (.socket).

CoreOS use systemd to manage service, every service is a Docker container.
systemctl provide:
sudo systemctl status custom-registry.service
sudo systemctl list-units | grep .service
sudo systemctl start apache.service
sudo systemctl stop apache.service
sudo systemctl kill apache.service
sudo systemctl restart apache.service
sudo systemctl daemon-reload     #If you're restarting a service after you changed its service file

http://coreos.com/docs/launching-containers/launching/overview-of-systemctl/
Systemd doc: https://coreos.com/docs/launching-containers/launching/getting-started-with-systemd/
systemctl  

Refs:
https://wiki.archlinux.org/index.php/systemd

# From Upstart to SystemD

https://wiki.ubuntu.com/SystemdForUpstartUsers
