---
layout: post
title: "CoreOS"
date: 2014-03-15 15:19:49 +0100
comments: true
categories:
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# COREOS
CoreOS isn’t just another Linux distribution, its explicit goal is to support the creation and maintenance of multi-resource, distributed systems based on Docker containers

DOC: http://coreos.com/docs/

Tools you need to understand:
systemctl
fleetctl
journalctl

Very cool: cloudformation + kibana and elastic search: http://coreos.com/docs/running-coreos/cloud-providers/ec2/
http://marceldegraaf.net/2014/05/05/coreos-follow-up-sinatra-logstash-elasticsearch-kibana.html

BETA: https://coreos.com/blog/coreos-beta-release/

AWS
Create from template: http://coreos.com/docs/running-coreos/cloud-providers/ec2/
min 3 instances for a cluster
Capire http://coreos.com/docs/cluster-management/setup/etcd-cluster-discovery/
 https://discovery.etcd.io/e8ca77732330a70219e014ac283680db

ELB integration:
http://marceldegraaf.net/2014/04/24/experimenting-with-coreos-confd-etcd-fleet-and-cloudformation.html
http://marceldegraaf.net/2014/05/05/coreos-follow-up-sinatra-logstash-elasticsearch-kibana.html
https://raw.githubusercontent.com/marceldegraaf/blog-coreos-1/master/stack.json                -------------------------->>>>>>>>>>>>>>>>>>>>>>>>    RISPETTO a QUELLO UFFICIALE AGGIUNGE ELB

