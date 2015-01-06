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

* make a guide for TLS
* make a guide for docker host
  * app for aws:reinvent demo by Nathan Le Claire https://github.com/nathanleclaire/awsapp
  * Proposal: Host management https://github.com/docker/docker/issues/8681
  * Proposal: Container groups https://github.com/docker/docker/issues/8637
  * as of Nov 22 2014 you need this docker branch to test docker host https://github.com/nathanleclaire/docker
* make a guide for panamax, see here a
    [draft]({{site.url}}/guides/panamax.html)

# Docker intro

WHY DOCKER IS USEFUL: Really good intro to docker from an usage point of view: http://www.infoq.com/articles/docker-containers/

http://docs.docker.io/introduction/understanding-docker/

Docker is a platform for developers and sysadmins to develop, ship, and run applications. Docker lets you quickly assemble applications from components and eliminates the friction that can come when shipping code. Docker lets you get your code tested and deployed into production as fast as possible.

Docker provides a way to run almost any application securely isolated into a container. The isolation and security allows you to run many containers simultaneously on your host. The lightweight nature of containers, which run without the extra overload of a hypervisor, means you can get more out of your hardware.

Docker uses a client-server architecture. The Docker client talks to the Docker daemon, which does the heavy lifting of building, running, and distributing your Docker containers.

Docker consists of:

* `Docker Engine` which major components are:
  * `Docker containers`:    You can consider Docker containers the run portion of the Docker framework.
  * `Docker images`:   You can consider Docker images to be the build portion of the Docker framework.
  * `Docker registries`:   You can consider Docker registries the share portion of the Docker framework.
  * `Docker daemon`: creates, builds and manages containers (takes
    advantage of some neat Linux kernel and operating system features,
    like namespaces and cgroups)
  * `Docker client`: is the commandline tool you use to send command to
    one or more
* `Docker Hub`: a SaaS service for sharing and managing application
    stacks. [DockerHub homepage](https://hub.docker.com/).

(Highlevel point of view)
http://www.docker.io/learn_more/
At page 21,22 there are a lot of examples

Shipping container cargo methaphore: separation of concerns, the developer can package the container, the sysadmin ship it
see also "Gabriel Monroy" comment here https://groups.google.com/forum/#!topic/docker-user/NF86nnPMZ6k

# Intro how docker works

See the [official doc](https://docs.docker.com/introduction/understanding-docker/#so-how-does-docker-work
) for a light intro to:

* How does a Docker Image work?
* How does a Docker registry work?
* How does a container work?
* What happens when you run a container?

# Docker Underlying technology

* Namespaces
* Control groups (cgroups)
* Union file systems
* Container format

These technologies composes the building blocks of docker containers and
images.

## Container

Docker combines these components (namespaces, cgroups, UFS) into a wrapper we call a container
format. The default container format is called `libcontainer`.

You can think about containers as a process in a box. The box contains everything the process might need, so it has the filesystem, system libraries, shell and such, but by default none of it is started or run.

Once you start a process in Docker from an Image, Docker fetches the image and its Parent Image, and repeats the process until it reaches the Base Image. Then the Union File System adds a read-write layer on top. That read-write layer, plus the information about its Parent Image and some additional information like its unique id, networking configuration, and resource limits is called a container.

When a container is running, the idea of a “container” also includes a tree of processes running on the CPU, isolated from the other processes running on the host.

You can start, stop, and restart a container. The processes restart from scratch (their memory state is not preserved in a container), but the file system is just as it was when the container was stopped.

Each container has a unique ID which is more or less analogous to a git commit hash.

### Pid system within a container

container's primary process has `PID 1`, a lot of docker's commands
interact directly with this process (stop, kill, start, etc...)

## Images

[What is a Docker Image](http://docs.docker.io/en/latest/terms/image/)

* In Docker terminology, a read-only Layer is called an image. An image never changes.
* All images are identified by a 64 hexadecimal digit string
* An image that has no parent is a `base image`
* Each image may depend on one more image which forms the layer beneath it. We sometimes say that the lower image is the parent of the upper image.
* Using the `Public/Private registry` you can share images
* Docker stores downloaded images on the `Docker host`.

NB: Docker HUB is more than a Docker Index, it has its [registry
](https://registry.hub.docker.com/), but it add other sevices to manage
the community.

[Docker Guide to Images]https://docs.docker.com/userguide/dockerimages/
covers:
* Managing and working with images locally on your Docker host;
* Creating basic images;
* Uploading images to [Docker Hub](https://hub.docker.com/).

### Layers
http://docs.docker.io/en/latest/terms/layer/
When Docker mounts the rootfs, it starts read-only, as in a traditional Linux boot, but then, instead of changing the file system to read-write mode, it takes advantage of a union mount to add a read-write file system over the read-only file system. In fact there may be multiple read-only file systems stacked on top of each other. We think of each one of these file systems as a layer.

# Install Docker
On recent linux Docker is really easy to install but on OS like
windows and OSX it's a little bit harder and you need to use ONE classical virtual machine to run Linux and Docker.

## Install Fig

* pip uninstall fig
* pip install fig

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

~~~bash
$ ls /Users/nicolabrisotto/fig_django_test
django-12factor-docker
$ docker run -v /Users/nicolabrisotto/fig_django_test/:/pippo ubuntu:trusty  ls pippo
django-12factor-docker
~~~


This mount problem is caused by the limited capabilities of the current
version of docker (1.3). It support only [data volumes](https://docs.docker.com/userguide/dockervolumes/) mounted from the host running the docker deamon.

But Boot2docker execute the docker client on OSX and the docker deamon in VirtualBox.

Boot2Docker 1.3 solve this problem with a trick:

* Share the directory between OSX and VBox
  * [VBox shared folders](https://www.virtualbox.org/manual/ch04.html#sharedfolders)
`sharedfolder  add <uuid|vmname> --name <name> --hostpath <hostpath> [--transient] [--readonly] [--automount]`
* Share the same directory from the VBox vm and the docker container
* Follow a naming convention to mount the OSX `/Users` directory in the
    same path on the VBox virtual machine

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


# Docker Guides and Articles
[CLI Commands reference](https://docs.docker.com/reference/commandline/cli)


Here there is a list of the [official Docker
guides](https://docs.docker.com/userguide/) and the [list of official
Docker articles](https://docs.docker.com/articles/basics/)

Here I will collect some integration to those guides and reference to
other third parties guides.

## Managing Data in Containers (Volumes)

[Docekr guide: Managing Data in Containers ](https://docs.docker.com/userguide/dockervolumes/)

There are two primary ways you can manage data in Docker.

* Data volumes
* Data volume containers

Use-cases:

* development: we can mount our source code inside the container and see our application at work as we change the source code.
* database

## Controlling containers

https://docs.docker.com/articles/basics/#controlling-containers


## Docker CLI Commands

[The docker command line reference documentation](https://docs.docker.com/reference/commandline/cli/)

## Run

When an operator executes `docker run`, he starts a process with:

* its own file system
* its own networking
* its own isolated process tree.


This process is the only process run, so when it completes the container is fully stopped.

[Docker RUN reference](https://docs.docker.com/reference/run/), see here
for:

* Detached vs Foreground
  * Detached (-d)
  * Foreground
* Container Identification
* Name (--name)
* PID Equivalent
* Network Settings
* Clean Up (--rm)
* Runtime Constraints on CPU and Memory
* Runtime Privilege, Linux Capabilities, and LXC Configuration

The command docker run takes a minimum of two arguments. An image name, and the command you want to execute within that image.

The image defines defaults but `docker run` **can** override those default:

* `CMD` (Default Command or Options)
* `ENTRYPOINT` (Default Command to Execute at Runtime)
* `EXPOSE` (Incoming Ports)
* `ENV` (Environment Variables)
* `VOLUME` (Shared Filesystems)
* `USER`
* `WORKDIR`

Four of the Dockerfile commands **cannot** be overridden at runtime:

* `FROM`
* `MAINTAINER`
* `RUN`
* `ADD`

#### CMD vs ENTRYPOINT

http://stackoverflow.com/questions/21553353/what-is-the-difference-between-cmd-and-entrypoint-in-a-dockerfile

`sudo docker run [OPTIONS] IMAGE[:TAG] [COMMAND] [ARG...]`

The command is optional because the person who created the IMAGE may have already provided a default COMMAND using the Dockerfile CMD instruction. As the operator (the person running a container from the image), you can override that CMD instruction just by specifying a new COMMAND.

If the image also specifies an ENTRYPOINT then the CMD or COMMAND get appended as arguments to the ENTRYPOINT.

The ENTRYPOINT of an image is similar to a COMMAND because it specifies what executable to run when the container starts, but it is (purposely) more difficult to override. The ENTRYPOINT gives a container its default nature or behavior, so that when you set an ENTRYPOINT you can run the container as if it were that binary, complete with default options, and you can pass in more options via the COMMAND. But, sometimes an operator may want to run something else inside the container, so you can override the default ENTRYPOINT at runtime by using a string to specify the new ENTRYPOINT.



### Start

[Attach command Docker
reference]()

### Stop / Kill

* [Stop command Docker
    reference](https://docs.docker.com/reference/commandline/cli/#stop)
  * send `SIGTERM` and then `SIGKILL` after a grace period.
* [Kill command Docker
reference](
https://docs.docker.com/reference/commandline/cli/#kill)
  * with kill you can send any signal.

You can use this two commands to send signals to the main process of a
container no matter if you are attached to it.

### Attach

[Attach command Docker
reference](https://docs.docker.com/reference/commandline/cli/#attach)

TODO: capire se alla fine questo comando è utile solo per collegarsi via
bash al container o anceh per altro

## How Docker integrates with the Boot and Root Filesystems of a guest

http://docs.docker.io/en/latest/terms/filesystem/

## Docker Registry

Docker-Registry is a simple Python app that holds docker images: https://github.com/docker/docker-registry

You can upload or download images to and from it with `push` and `pull` commands.

Every installation of docker can store images locally and then push them to a registry.

The registry has the following characteristics:

* It stores the images and the graph for a set of repositories
* It does not have user accounts data
* It has no notion of user accounts or authorization
* It delegates authentication and authorization to the Docker Hub Auth service using tokens
* It supports different storage backends (S3, cloud files, local FS)
* It doesn't have a local database

By default docker tools use a public installation of a docker registry hosted at Docker.com
[Docker Public Index](https://registry.hub.docker.com/). But you can use other registries. See here to create your own private repository: http://blog.docker.io/2013/07/how-to-use-your-own-registry/

NOTE: the docker hub is a separate project that allow to search, share and collaborate with other. 

Docker registry [SPEC](https://docs.docker.com/reference/api/hub_registry_spec/)

### How does Image's tag works?
A lot of command accept tags
You can group your images together using names and tags, and then upload them to Share Images via Repositories.
http://docs.docker.io/reference/commandline/cli/#tag

### Private registry on Azure
http://azure.microsoft.com/blog/2014/11/11/deploying-your-own-private-docker-registry-on-azure/
http://azure.microsoft.com/blog/tag/docker/

## Docker Hub

* [Docker guide: Working with Docker Hub](https://docs.docker.com/userguide/dockerrepos/)
* [Intro to DockerHub](https://docs.docker.com/userguide/dockerhub/)

Docker HUB is a SaaS that provide you:

* Docker image hosting.
* A public Docker Registry with more than 15000 images
* User authentication, team collaboration.
* Automated image builds and work-flow tools such as build triggers and web hooks.
* Integration with GitHub and BitBucket.
* ...

### Repository

REF: [Official Docker doc about repositories](http://docs.docker.com/docker-hub/repos/)

What is a `repository` on Docker Hub? Essentialy it's a layer on top of a the docker registry that enables a set of collaboration and integration feature on a set of images:

* A web page at "https://registry.hub.docker.com/u/<username>/<repo_name>/" with a description and other info.
* Stats (numer of download, etc)
* Bookmarks
* Automatic builds
* Webhooks
* Collaborators and their role

Each repository has an image and how many image tag you want.


### Docker Official images: Docker Library

REF:

* http://stackoverflow.com/questions/24609139/what-are-the-differences-between-dockerfile-and-stackbrew-users-on-docker-hub
* https://docs.docker.com/articles/dockerfile_best-practices/
* https://docs.docker.com/docker-hub/official_repos/


Docker and its network of partners maintain a set of official images.

All the repositories of these images are listed here https://registry.hub.docker.com/repos/stackbrew/?s=stars

This images are built using `bashbrew` or `stackbrew`. Stackbrew is a web-application that performs continuous building of the docker standard library [repo](https://github.com/docker-library/official-images/tree/master/stackbrew).

The [docker-library](https://github.com/docker-library) github organization contains most of the repo used by this automated build system:

* [official images library](https://github.com/docker-library/official-images/tree/master/library) is a directory on manifest file, one for each official image.
* each manifest points to a separate git repository with a set of Dockerfile, most of them are under this organization (ex rails: https://github.com/docker-library/rails)
* [doc for each image](https://github.com/docker-library/docs) 


#### How to find the Dockerfile of an official image


Go to the library dir: https://github.com/docker-library/official-images/tree/master/library

Open the manifest, for example the Postgres manifest is https://github.com/docker-library/official-images/blob/master/library/postgres

~~~
.....

9.3.5: git://github.com/docker-library/postgres@c9d9f4c1a0d33a161fefda666f041ef0dc4dc9f8 9.3
9.3: git://github.com/docker-library/postgres@c9d9f4c1a0d33a161fefda666f041ef0dc4dc9f8 9.3

9.4.0: git://github.com/docker-library/postgres@c9d9f4c1a0d33a161fefda666f041ef0dc4dc9f8 9.4
9.4: git://github.com/docker-library/postgres@c9d9f4c1a0d33a161fefda666f041ef0dc4dc9f8 9.4
9: git://github.com/docker-library/postgres@c9d9f4c1a0d33a161fefda666f041ef0dc4dc9f8 9.4
latest: git://github.com/docker-library/postgres@c9d9f4c1a0d33a161fefda666f041ef0dc4dc9f8 9.4
~~~

The format of each line is `<docker-tag>: <git-url>@<git-tag-or-commit-id> <dockerfile-dir>`:

* Generated image will be tagged as `<docker-tag>`
* Optionally, if `<dockerfile-dir>` is present:
  * Stackbrew will look for the Dockerfile inside the specified subdirectory instead of at the root 
  * `<dockerfile-dir>` will be used as the "context" for the build).

This mean that to find the postgres:9.4 image Dockerfile you must go here: https://github.com/docker-library/postgres/blob/master/9.4/Dockerfile

#### Language Stacks

Language stacks are a set of official images designed to make easy:

* to find a particular version following this image tagging convention: tag with the version of the language you will find in the image. ie: `docker pull java:8u40`
* decouple your code from the stack using [ONBUILD](https://docs.docker.com/reference/builder/#onbuild)
* you’ll see that most of the language stacks are based on the buildpack-deps image, a collection of common build dependencies including development header packages. 

For more details see this blog post: [See the announcement on the blog](http://blog.docker.com/2014/09/docker-hub-official-repos-announcing-language-stacks/)

### Automated builds: Github and Bitbucket integration

http://docs.docker.com/docker-hub/builds/

## Networking

Docker neworking 
http://docs.docker.io/use/networking/

capire se pipeworks ha ancora senso o meno
https://github.com/jpetazzo/pipework

Docker-user ›
container needs to know daemon's dynamically selected port from -p, and hosts 'public' ip address
https://groups.google.com/forum/#!topic/docker-user/KUbcMt1lARE

### PORT FORWARDING on Boot2Docker
The last update of may 2014 (you must init again the VM) will create an host adpter and this make easy to connect locally to ports exposed by docker.
To get the VM host adpter address:
boot2docker ssh ip addr show dev eth1


## Execute an interactive bash

* `docker run --rm -i -t ubuntu:14.04 /bin/bash`
  * `--rm` Automatically remove the container when it exits (incompatible with -d)

## Cleanup containers and images

http://blog.stefanxo.com/2014/02/clean-up-after-docker/

## Starting a long-running worker process

https://docs.docker.com/articles/basics/#starting-a-long-running-worker-process

## Listing containers

https://docs.docker.com/articles/basics/#listing-containers


### See details of the last container started

* `docker ps -l`

## SEARCH

Container repo:
https://index.docker.io/
Usage: docker search TERM
Search the docker index for images

## PULL - COMMAND

Download an existing container:
docker pull learn/tutorial

When you pull you'll see that Docker has downloaded a number of layers. In Docker all images (except the base image) are made up of several cumulative layers.

A group of special, trusted images such as the ubuntu base image can be retrieved by just their name <repository>.
For images from the central index, the name you specify is constructed as <username>/<repository>

## BUILD IMAGES from DOCKERFILE
http://docs.docker.io/reference/builder/
A Dockerfile is a simple text file consisting of instructions on how to build the image from a base image.
Executing docker build will run your steps and commit them along the way, giving you a final image.

Dockerfile  VS other build tools
https://groups.google.com/forum/#!topic/docker-user/3pcVXU4hgko

## LIST Docker host images

docker images




## WAIT UNTIL a CONTAINER STOPS
http://docs.docker.io/reference/commandline/cli/#wait
docker wait [OPTIONS] NAME

MAKE MODIFICATION INTO THE CONTAINER
Next we are going to install a simple program (ping) in the container. The image is based upon ubuntu, so you can run the command apt-get install -y ping in the container.
Note that even though the container stops right after a command completes, the changes are not forgotten.  
docker version 
docker run learn/tutorial apt-get install -y ping 

## CREATE IMAGES : COMMIT CHANGES (LAYERS)
http://docs.docker.io/reference/commandline/cli/#commit
docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]

With Docker, the process of saving the state is called committing. Commit basically saves the difference between the old image and the new state. The result is a new image. 

## RUN FROM OTHER IMAGES
Now you have basically setup a complete, self contained environment with the 'ping' program installed.Your image can now be run on any host that runs Docker.Lets run this image on this machine:

docker run learn/ping ping google.com
Note that normally you can use Ctrl-C to disconnect. The container will keep running.  

## CHECK RUNNING IMAGES
You now have a running container. Let's see what is going on.Using docker ps we can see a list of all running containers, and using docker inspect we can see all sorts of useful information about this container. 
docker inspect <container id> 
You can see the ip-address, status and other information. 

## PUSH IMAGES
TODO

Move images and container without a registry (export/import  save/load)

A Docker image and its entire history can be saved to a tarball and loaded back again. This will preserve the history of the image:
# save the image to a tarball
docker save <IMAGE NAME> > /home/save.tar
# load it back
docker load <IMAGE NAME> < /home/save.tar


Trick to flatten the image story:
ID=$(docker run -d image-name /bin/bash)
docker export $ID | docker import – flat-image-name

If you want to save it for backup you can use gzip to compress the image.
ID=$(docker run -d image-name /bin/bash)
(docker export $ID | gzip -c > image.tgz)
gzip -dc image.tgz | docker import - flat-image-name


refs:
http://blog.intercityup.com/downsizing-docker-containers/
http://tuhrig.de/flatten-a-docker-container-or-image/


## DOCKER DIFF
TODO

## REMOVE IMAGES / CONTAINERS
sudo docker rmi <image_name>
docker rm <container>

remove stopped containers:
docker rm $(docker ps -a -q)

In the process of running docker I had accumulated several images that are not tagged. To remove these I use this command:
 docker ps -q -a | xargs docker rm

# Fig tool

## For development

* [fig.yml doc](http://www.fig.sh/yml.html)

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

