---
layout: post
title: "Fleet"
date: 2014-03-15 15:19:49 +0100
comments: true
categories: 
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# Fleet
FLEET is a layer on top of systemd, the well-known init system. Fleet basically lets you manage your services on any server in your cluster transparently, and gives you some convenient tools to inspect the state of your services.
http://coreos.com/docs/launching-containers/launching/launching-containers-fleet/
http://coreos.com/using-coreos/clustering/

https://github.com/coreos/fleet

Can Deploy containers on machines matching specific metadata
Fleet architecture: https://github.com/coreos/fleet/blob/master/Documentation/architecture.md Each fleet daemon running in a cluster fulfills both roles. An Engine primarily makes scheduling decisions while an Agent executes jobs.

Scheduling doc:
https://github.com/coreos/fleet/blob/master/Documentation/scheduling.md

brew install fleetctl



fleetctl submit hello.service
fleetctl submit examples/*
fleetctl start hello.service
fleetctl stop hello.service
fleetctl list-units
fleetctl status hello.service
fleetctl destroy hello.service
fleetctl cat examples/hello.service


# Fleet metadata:
sudo mkdir /etc/fleet
sudo vim /etc/fleet/fleet.conf ->  metadata="region=us-west,az=us-west-1,role=api"
sudo systemctl restart fleet.service

debug:
journalctl -f

May 20 19:15:46 ip-172-31-40-20 fleet[689]: I0520 19:15:46.332731 00689 event.go:29] CommandLoadJob(myapp_all.service): publishing JobOffer
May 20 19:15:46 ip-172-31-40-20 fleet[689]: I0520 19:15:46.425527 00689 event.go:21] EventJobOffered(myapp_all.service): verifying ability to run Job
May 20 19:15:46 ip-172-31-40-20 fleet[689]: I0520 19:15:46.426389 00689 agent.go:419] Job(myapp_all.service) has requirements: map[ConditionMachineMetadata:[rolw=api]]
May 20 19:15:46 ip-172-31-40-20 fleet[689]: I0520 19:15:46.427261 00689 agent.go:424] Unable to run Job(myapp_all.service), local Machine metadata insufficient
May 20 19:15:46 ip-172-31-40-20 fleet[689]: I0520 19:15:46.428097 00689 event.go:37] EventJobOffered(myapp_all.service): not all criteria met, not bidding

In this example there was a typo in the metadata rolw=api 



# AUTOSCALING COREOS
https://groups.google.com/forum/#!searchin/coreos-dev/autoscaling/coreos-dev/6_EN4MJUJjM/P1K9o3DLm7UJ


# journalctl  --  Read Logs
http://coreos.com/docs/cluster-management/debugging/reading-the-system-log/

journalctl
journalctl -u apache.service

tail:
journalctl -f
journalctl -u apache.service -f

since boot
journalctl --boot

read from remote:
fleetctl --tunnel 10.10.10.10 journal apache.service
fleetctl --tunnel 10.10.10.10 journal -f apache.service



TODO : cos'è CONFD?   Confd can watch certain keys in etcd, and update the related configuration files as soon as the key changes.


ssh -i ~/.ssh/pitch-target.pem core@ec2-54-76-1-62.eu-west-1.compute.amazonaws.com 


fllet is build on top of systemd and uses systemd file




TODO CAPIRE SE è UN BUG ANCORA PRESENTE Note: at the time of writing there is a bug in CoreOS that causes your EC2 instance’s disk space to not be properly resized after booting. The workaround is to run this command on each of the EC2 instances in your fleet, via SSH:
sudo btrfs filesystem resize 1:max /


TODO:
more about orchestration http://continuousdelivery.uglyduckling.nl/docker/coreos-as-an-orchestration-layer-for-docker/






