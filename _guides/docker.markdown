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


# TODO

# Install Docker
On recent linux Docker is really easy to install but on OS like
windows and OSX it's a little bit harder and you need to use ONE classical virtual machine to run Linux and Docker.

## boot2docker

### OSX


Note: if you are upgrading from boot2docker 0.9.1 or before, please create a new VM using:

~~~bash
boot2docker delete; boot2docker download; boot2docker up.
~~~

This will delete your persistent data, but will also ensure that you have the latest VirtualBox configuration.



### Mount Volumes issues
Problem: The current version of docker (1.2) support only [data volumes](https://docs.docker.com/userguide/dockervolumes/) mounted from the host running the docker deamon. Boot2docker uses runs the docker client on OSX and the deamon in VirtualBox.

Problem: To mount a volume from OSX into a container you need two steps:

* Share the directory between OSX and VBox
* Share the same directory from the VBox vm and the docker container

Current solution (not upstream), to mount the /Users directory into the
boot2docker-vm:

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


# Docker

## Volumes

[volumes](https://docs.docker.com/userguide/dockervolumes/) 

There are two primary ways you can manage data in Docker.

* Data volumes
* Data volume containers

Use-cases:

* development: we can mount our source code inside the container and see our application at work as we change the source code.
* database

# DockerHub

## Language Stacks

[See the announcement on the blog](http://blog.docker.com/2014/09/docker-hub-official-repos-announcing-language-stacks/)

## Stackbrew

Stackbrew is a web-application that performs continuous building of the docker standard library [repo](https://github.com/docker-library/official-images/tree/master/stackbrew).

http://stackoverflow.com/questions/24609139/what-are-the-differences-between-dockerfile-and-stackbrew-users-on-docker-hub


# Deployment solutions

* [Centurion by Newrelic](https://github.com/newrelic/centurion)

