---
layout: post
title: "Docker"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["docker"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}


# References:

* [Cheatsheet](https://github.com/wsargent/docker-cheat-sheet)

# TODO

# Install Docker
On recent linux Docker is really easy to install but on OS like
windows and OSX it's a little bit harder and you need to use ONE classical virtual machine to run Linux and Docker.

## boot2docker

### OSX


You can upgrade your existing Boot2Docker VM without data loss by running: `boot2docker upgrade`
This will delete your persistent data, but will also ensure that you have the latest VirtualBox configuration.


### Mount Volumes issues on OSX

Boot2docker 1.3 supports volumes mounting but with some limitation:

* limited to boot2docker’s virtualbox configuration
* cannot be managed dynamically, and only works for directories in **/Users**
* Expect this area to improve drastically in the next few releases.

`docker run -v /Users/bob/myapp/src:/src [...]` Will mount the directory /Users/bob/myapp/src from your Mac into the container.

$ ls /Users/nicolabrisotto/fig_django_test
django-12factor-docker
$ docker run -v /Users/nicolabrisotto/fig_django_test/:/pippo ubuntu:trusty  ls pippo
django-12factor-docker


There are still some limitations:






Problem: The current version of docker (1.2) support only [data volumes](https://docs.docker.com/userguide/dockervolumes/) mounted from the host running the docker deamon. Boot2docker execute the docker client on OSX and the docker deamon in VirtualBox.

Problem: To mount a volume from OSX into a container you need two steps:

* Share the directory between OSX and VBox
* Share the same directory from the VBox vm and the docker container

Current solution (not upstream), to mount the /Users directory into the
boot2docker-vm:

* Install from [here](http://boot2docker.io/)
* Download the boot2docker iso with VBox addition from [here](https://medium.com/boot2docker-lightweight-linux-for-docker/boot2docker-together-with-virtualbox-guest-additions-da1e3ab2465c) and copy it to `~/.boot2docker/boot2docker.iso`
* Recreate the boot2docker-vm:  `boot2docker destroy; boot2docker init`
* Create the VBox share: `VBoxManage sharedfolder add boot2docker-vm -name home -hostpath /Users`

If you want to create a custom share and automount it at boot, create a
new script like `/etc/rc.d/vbox-guest-additions-permanent-mount`

Ref:

* [VBox shared folders](https://www.virtualbox.org/manual/ch04.html#sharedfolders)
`sharedfolder  add <uuid|vmname> --name <name> --hostpath <hostpath> [--transient] [--readonly] [--automount]`

A temporary solution will be pushed upstream with boot2docker 1.3:

* see [here](https://github.com/boot2docker/boot2docker/pull/534) the
discussion
* [boot2docker 1.3 doc about vbox shares](https://github.com/boot2docker/boot2docker#virtualbox-guest-additions)

Docker is working on a new proposal that could solve the issue allowing
docker to mount [remote shared volumes](https://github.com/docker/docker/issues/7249)

### FIG issues
Fig relies heavly on volumes and variables. I need to understand how to
manage these issues on OSX.

With the current boot2docker 1.2 we need to map dirs in our home (ex:
~/figtest), but what does "." means in a fig.yml file??? This solution
is a trick that maps the Vbox host /Users dir the same VM dir, this way
you obtain a mirror of the /User dir.

* how could we write a 12 factor app that works with fig and AWS
Beanstalk??? 


TODO: read the make file of this project and implements it in FIG: https://github.com/ricardokirkner/django-12factor-docker



# Docker

## Volumes

[volumes](https://docs.docker.com/userguide/dockervolumes/) 

There are two primary ways you can manage data in Docker.

* Data volumes
* Data volume containers

Use-cases:

* development: we can mount our source code inside the container and see our application at work as we change the source code.
* database

# Fig tool

## For development

* [fig.yml doc](http://www.fig.sh/yml.html)

# DockerHub

## Language Stacks

[See the announcement on the blog](http://blog.docker.com/2014/09/docker-hub-official-repos-announcing-language-stacks/)

## Stackbrew

Stackbrew is a web-application that performs continuous building of the docker standard library [repo](https://github.com/docker-library/official-images/tree/master/stackbrew).

http://stackoverflow.com/questions/24609139/what-are-the-differences-between-dockerfile-and-stackbrew-users-on-docker-hub


# Deployment solutions

* [Centurion by Newrelic](https://github.com/newrelic/centurion)


# Chef support for docker


## Docker container

* [Webinar](https://www.getchef.com/blog/2014/09/10/webinar-recording-chef-for-containers/)
* [Documentation](http://docs.getchef.com/containers.html)
* [Docker Images](https://hub.docker.com/u/chef)

Feedback:

* http://github.com/opscode/chef-init
* http://github.com/opscode/knife-container

FAQ:

* Docker container scope do not include volumes mounting. For this task
you can use chef-metal or docker.
* At the moment (oct 2014) chef-server see a container as an host, there is no
support for clean-up. May be chef-metal can manage something for you.

# AWS support for docker

* [Oct 2014: Running Docker on AWS OpsWorks](http://blogs.aws.amazon.com/application-management/post/Tx2FPK7NJS5AQC5/Running-Docker-on-AWS-OpsWorks)


# Manage container clusters

## Apache Mesos and Marathon
* https://github.com/mesosphere/marathon
* https://github.com/thefactory/cloudformation-mesos

## Google Kubernetes
* kubernetes: https://github.com/GoogleCloudPlatform/kubernetes

