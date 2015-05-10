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

Read here installation instruction: http://docs.docker.com/installation/mac/

You can upgrade your existing Boot2Docker VM without data loss by running: `boot2docker upgrade`
This will delete your persistent data, but will also ensure that you have the latest VirtualBox configuration.

If you run a container with an exposed port: `docker run --rm -i -t -p 80:80 nginx`
then you should be able to access that Nginx server using the IP address reported by: `$ boot2docker ip`

### Filesystem resize

https://docs.docker.com/articles/b2d_volume_resize/

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

# Docker components and Services
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


### Private registries and docker login

* On Azure: http://azure.microsoft.com/blog/2014/11/11/deploying-your-own-private-docker-registry-on-azure/  and http://azure.microsoft.com/blog/tag/docker/
* Core OS Enterprise Registry behind the firewall: https://coreos.com/products/enterprise-registry/plans/
* Quay.io
* Private registry with NGINX: https://www.digitalocean.com/community/tutorials/how-to-set-up-a-private-docker-registry-on-ubuntu-14-04


See here also
http://www.activestate.com/blog/2014/01/deploying-your-own-private-docker-registry

* `docker login` can work with any website that support `basic auth`. After you login into your registry the auth token is stored here `~/.dockercfg`: `{"quay.io":{"auth":"XXXXXXXXXXXXXXXXXXXXXX","email":"nicolabrisotto@gmail.com"}}`

 
* see also: https://github.com/docker/docker-registry#authentication-options

See "working with images" to push/pull from a private registry.

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

### Repositories on DockerHub

REF: [Official Docker doc about repositories](http://docs.docker.com/docker-hub/repos/)

What is a `repository` on Docker Hub? Essentialy it's a layer on top of a the repository of the registry that enables a set of collaboration and integration features:

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


### How to find the Dockerfile of an official image


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

### Language Stacks

Language stacks are a set of official images designed to make easy:

* to find a particular version following this image tagging convention: tag with the version of the language you will find in the image. ie: `docker pull java:8u40`
* decouple your code from the stack using [ONBUILD](https://docs.docker.com/reference/builder/#onbuild), which adds to the image a trigger instruction to be executed at a later time, when the image is used as the base for another build.
* you’ll see that most of the language stacks are based on the buildpack-deps image, a collection of common build dependencies including development header packages. 

For more details see this blog post: [See the announcement on the blog](http://blog.docker.com/2014/09/docker-hub-official-repos-announcing-language-stacks/)

You can use `docker inspect` and `jq` to easly inspect ONBUILD triggers:

~~~
docker inspect ruby:2.2.2-onbuild|jq .[0].Config.OnBuild
[
  "COPY Gemfile /usr/src/app/",
  "COPY Gemfile.lock /usr/src/app/",
  "RUN bundle install",
  "COPY . /usr/src/app"
]

~~~

#### Ruby Language Stack

This stack make easy to dockerize a ruby application that use bundler.

* https://registry.hub.docker.com/_/ruby/
* Old Problem with caching ADD and how to make ti : http://ilikestuffblog.com/2014/01/06/how-to-skip-bundle-install-when-deploying-a-rails-app-to-docker/
  * It should be fixed in modern ruby language images:  https://github.com/docker-library/ruby/blob/master/2.2/onbuild/Dockerfile

The ruby language stack image is based on this images:

* `buildpack-deps:jessie` : https://registry.hub.docker.com/_/buildpack-deps/
  * is a debian jessie image with some basic tool (git, mercurial, curl, etc)

* `ruby:X.Y` : ex: https://github.com/docker-library/ruby/blob/master/2.2/Dockerfile
  * FROM buildpack-deps:jessie
  * install ruby from source, setup bundler 

* `ruby:X.Y-onbuild` : ex: https://github.com/docker-library/ruby/blob/master/2.2/onbuild/Dockerfile
  * FROM ruby:2.2
  * it configure bundler for production, copy the application code and run bundle install
  * If your Dockerfile is from this image each time you run `docker build` all the commands tagged `ONBUILD` from the `ruby:2.2.2-onbuild` image will be executed
  * the image copy the Gemfile before the application code, this will cache the bundle install command if the application code is changed but not the Gemfile( [see here for build caching](#docker-build-cache) )
  
`ruby:2.2.2-onbuild` Dockerfile:

~~~
FROM ruby:2.2.2

# configure bundler to throw errors if the Gemfile has been modified since Gemfile.lock
RUN bundle config --global frozen 1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ONBUILD COPY Gemfile /usr/src/app/
ONBUILD COPY Gemfile.lock /usr/src/app/
ONBUILD RUN bundle install

ONBUILD COPY . /usr/src/app
~~~

TODO: capire quale dovrebbe essere il workflow corretto sia con Docker-Compose che senza.
TODO: capire come funziona il caching dei comandi, come escluderlo etc

This image will check if the Gemfile was modified: https://github.com/docker-library/ruby/blob/master/2.2/onbuild/Dockerfile

You can use `docker inspect` and `jq` to easly inspect ONBUILD triggers:

~~~
docker inspect ruby:2.2.2-onbuild|jq .[0].Config.OnBuild
[
  "COPY Gemfile /usr/src/app/",
  "COPY Gemfile.lock /usr/src/app/",
  "RUN bundle install",
  "COPY . /usr/src/app"
]

~~~



### Automated builds: Github and Bitbucket integration

http://docs.docker.com/docker-hub/builds/



# Basic Docker Guides and Articles

References:

* [CLI Commands reference](https://docs.docker.com/reference/commandline/cli)
* list of the [official Docker guides](https://docs.docker.com/userguide/)
* [list of official Docker articles](https://docs.docker.com/articles/basics/)
* [Cheatsheet](https://github.com/wsargent/docker-cheat-sheet) 

## Volumes: Managing Data in Containers 

[Docekr guide: Managing Data in Containers ](https://docs.docker.com/userguide/dockervolumes/)

Nice article about volumes: http://crosbymichael.com/advanced-docker-volumes.html

So is a volume?

A volume can be a directory that is located outside of the root filesystem of your container. This allows you to import this directory in other containers. You can also use volumes to mount directories from your host machine inside a container.


There are two primary ways you can manage data in Docker.

* Data volumes
* Data volume containers

### Under the hood


### Use Cases

* development: we can mount our source code inside the container and see our application at work as we change the source code.
* database: we can use the volume as data directory for the database, this will by-pass the COW filesystem and will increase performance.


## Working with Containers

Cheatsheet:

* `docker ps` - Lists containers.
* `docker logs` - Shows us the standard output of a container.
* `docker stop` - Stops running containers.

https://docs.docker.com/articles/basics/#controlling-containers

### RUN a container

When an operator executes `docker run`, he starts a process with:

* its own file system
* its own networking
* its own isolated process tree.


This process is the only process run, so when it completes the container is fully stopped.

[Docker RUN reference](https://docs.docker.com/reference/run/), see here for:

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

When the image is built its `Dockerfile` defines a set of defaults

* `CMD` (Default Command or Options)
* `ENTRYPOINT` (Default Command to Execute at Runtime)
* `EXPOSE` (Incoming Ports)
* `ENV` (Environment Variables)
* `VOLUME` (Shared Filesystems)
* `USER`
* `WORKDIR`

but `docker run` **can** override those default or add new values:

* `CMD` is overridden by `docker run <your cmd>`
* `ENTRYPOINT` is overridden by  `docker run --entrypoint`
* `EXPOSE` can be overridden by  `docker run -p` 
* `ENV` can overridden by  `docker run -e`
* `VOLUME` can be overridden by  `docker run -v`

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

#### Starting a long-running worker process

https://docs.docker.com/articles/basics/#starting-a-long-running-worker-process


### Container lifecycle

* [`docker create`](http://docs.docker.io/reference/commandline/cli/#create) creates a container but does not start it.
* [`docker run`](http://docs.docker.io/reference/commandline/cli/#run) creates and starts a container in one operation.
* [`docker start`](http://docs.docker.io/reference/commandline/cli/#start) will start it again.
* [`docker restart`](http://docs.docker.io/reference/commandline/cli/#restart) restarts a container.
* [`docker rm`](http://docs.docker.io/reference/commandline/cli/#rm) deletes a container.
* [`docker attach`](http://docs.docker.io/reference/commandline/cli/#attach) will connect to a running container.
  * TODO: capire se alla fine questo comando è utile solo per collegarsi via bash al container o anceh per altro
* [`docker wait`](http://docs.docker.io/reference/commandline/cli/#wait) blocks until container stops.


* [`docker kill`](http://docs.docker.io/reference/commandline/cli/#kill) sends a `SIGKILL` to a container.
* [`docker stop`](http://docs.docker.io/reference/commandline/cli/#stop) send `SIGTERM` and then `SIGKILL` after a grace period.


You can use this two commands to send signals to the main process of a container no matter if you are attached to it.


If you want to run and then interact with a container, `docker start`, then spawn a shell as described in [Executing Commands](https://github.com/wsargent/docker-cheat-sheet/#executing-commands).

If you want a transient container, `docker run --rm` will remove the container after it stops.

If you want to run an interactive shell into an image, `docker run -t -i <myimage> <myshell>` to open a tty:

* `docker run --rm -i -t ubuntu:14.04 /bin/bash`
  * `--rm` Automatically remove the container when it exits (incompatible with -d)


If you want to map a directory on the host to a docker container, `docker run -v $HOSTDIR:$DOCKERDIR`.  Also see [Volumes](https://github.com/wsargent/docker-cheat-sheet/#volumes).

If you want to integrate a container with a [host process manager](http://docs.docker.io/use/host_integration/), start the daemon with `-r=false` then use `docker start -a`.

If you want to expose container ports through the host, see the [exposing ports](https://github.com/wsargent/docker-cheat-sheet#exposing-ports) section.

Restart policies on crashed docker instances are [covered here](http://container42.com/2014/09/30/docker-restart-policies/).

### Info

REF:  https://docs.docker.com/articles/basics/#listing-containers

* [`docker ps`](http://docs.docker.io/reference/commandline/cli/#ps) shows running containers.
* [`docker inspect`](http://docs.docker.io/reference/commandline/cli/#inspect) looks at all the info on a container (including IP address).
* [`docker logs`](http://docs.docker.io/reference/commandline/cli/#logs) gets logs from container.
* [`docker events`](http://docs.docker.io/reference/commandline/cli/#events) gets events from container.
* [`docker port`](http://docs.docker.io/reference/commandline/cli/#port) shows public facing port of container.
* [`docker top`](http://docs.docker.io/reference/commandline/cli/#top) shows running processes in container.
* [`docker diff`](http://docs.docker.io/reference/commandline/cli/#diff) shows changed files in the container's FS.

* `docker ps -a` shows running and stopped containers.
* `docker ps -l` Show only the latest created container, include non-running ones

### Import / Export

There doesn't seem to be a way to use docker directly to import files into a container's filesystem.  The closest thing is to mount a host file or directory as a data volume and copy it from inside the container.

* [`docker cp`](http://docs.docker.io/reference/commandline/cli/#cp) copies files or folders out of a container's filesystem.
* [`docker export`](http://docs.docker.io/reference/commandline/cli/#export) turns container filesystem into tarball.

### Executing Commands

* [`docker exec`](https://docs.docker.com/reference/commandline/cli/#exec) to execute a command in container.

To enter a running container, attach a new shell process to a running container called foo, use: `docker exec -it foo /bin/bash`.

### Remove containers 

REF: http://blog.stefanxo.com/2014/02/clean-up-after-docker/

* `docker rm <container>` 
* `docker rm $(docker ps -a -q)`  remove all stopped containers
  * `-q, --quiet=false`           Only display numeric IDs


## Networking

refs:

* [Docker neworking](http://docs.docker.io/use/networking/)


### -P flag

When that container was created, the -P flag was used to automatically map any network ports inside it to a random high port from the range 49153 to 65535 on our Docker host. 

`sudo docker run -d -P training/webapp python app.py` :

~~~
 sudo docker ps nostalgic_morse
CONTAINER ID  IMAGE                   COMMAND       CREATED        STATUS        PORTS                    NAMES
bc533791f3f5  training/webapp:latest  python app.py 5 seconds ago  Up 2 seconds  0.0.0.0:49155->5000/tcp  nostalgic_morse
~~~

### -p flag

* `sudo docker run -d -p 5000:5000 training/webapp python app.py` :  bind a container's ports to a specific docker host port 

* you can also specify a binding to a specific interface, for example only to the localhost: `sudo docker run -d -p 127.0.0.1:5000:5000 training/webapp python app.py`
* to bind port 5000 of the container to a dynamic port but only on the localhost: `sudo docker run -d -p 127.0.0.1::5000 training/webapp python app.py`
* You can also bind UDP ports by adding a trailing /udp : `sudo docker run -d -p 127.0.0.1:5000:5000/udp training/webapp python app.py`

### docker port

`docker port`: showed us the current port bindings



###

capire se pipeworks ha ancora senso o meno
https://github.com/jpetazzo/pipework

Docker-user ›
container needs to know daemon's dynamically selected port from -p, and hosts 'public' ip address
https://groups.google.com/forum/#!topic/docker-user/KUbcMt1lARE

### PORT FORWARDING on Boot2Docker
The last update of may 2014 (you must init again the VM) will create an host adpter and this make easy to connect locally to ports exposed by docker.
To get the VM host adpter address:
boot2docker ssh ip addr show dev eth1


## Working with images

Ref:

* [Docker doc: image definition](https://docs.docker.com/terms/image/)
* [Official Image Spec](https://github.com/docker/docker/blob/master/image/spec/v1.md)

* an `image` is a _read-only_ layer.
* An image never changes.
* All images are identified by a 64 hexadecimal digit string (internally a 256bit value).


An image that has no parent is a `base image`.


Images are just [templates for docker containers](https://docs.docker.com/introduction/understanding-docker/#how-does-a-docker-image-work).

### Lifecycle

* [`docker images`](http://docs.docker.io/reference/commandline/cli/#images) shows all images.
* [`docker import`](http://docs.docker.io/reference/commandline/cli/#import) creates an image from a tarball.
* [`docker build`](http://docs.docker.io/reference/commandline/cli/#build) creates image from Dockerfile.
* [`docker commit`](http://docs.docker.io/reference/commandline/cli/#commit) creates image from a container.
* [`docker rmi`](http://docs.docker.io/reference/commandline/cli/#rmi) removes an image.
* [`docker insert`](http://docs.docker.io/reference/commandline/cli/#insert) inserts a file from URL into image. (kind of odd, you'd think images would be immutable after create)
* [`docker load`](http://docs.docker.io/reference/commandline/cli/#load) loads an image from a tar archive as STDIN, including images and tags (as of 0.7).
* [`docker save`](http://docs.docker.io/reference/commandline/cli/#save) saves an image to a tar archive stream to STDOUT with all parent layers, tags & versions (as of 0.7).

### Info

* [`docker history`](http://docs.docker.io/reference/commandline/cli/#history) shows history of image.
* [`docker tag`](http://docs.docker.io/reference/commandline/cli/#tag) tags an image to a name (local or registry).

Docker image ids are [sensitive information](https://medium.com/@quayio/your-docker-image-ids-are-secrets-and-its-time-you-treated-them-that-way-f55e9f14c1a4) and should not be exposed to the outside world.  Treat them like passwords.

### Repository

A collection of tags grouped under a common prefix (the name component
before `:`). For example, in an image tagged with the name
`my-app:3.1.4`, `my-app` is the _Repository_
component of the name. Acceptable values for repository name are
implementation specific, but they SHOULD be limited to the set of
alphanumeric characters `[a-zA-z0-9]`, and punctuation
characters `[._-]`, however it MAY contain additional
`/` and `:` characters for organizational
purposes, with the last `:` character being interpreted
dividing the repository component of the name from the tag suffic
component.

### SEARCH images on the Docker Hub registry

* search online on [Docker Hub](https://hub.docker.com/)
* `docker search TERM` Search the Docker Hub index for images 

### Image ID and Image tags

A lot of command accept tags. You can group your images together using a basic name and tags. 

For example postgres uses:

* basic name: `postgres`
* tags: `9.2`, `9.3`, ... , `latest`
* ex: `postgres:9.2`

From the docker point of view every tagged image is totally different from the other, the tagging system is only a naming convention.

On Docker Hub every repository can host multiple tag.
http://docs.docker.io/reference/commandline/cli/#tag



**Tip** : We recommend you always use a specific tagged image, for example ubuntu:12.04. That way you always know exactly what variant of an image is being used.


IDs are globally unique but they may be accessible via different image
names, in different security contexts. So from a security point of view we
can't allow direct unqualified access to a given ID. (ref: https://github.com/docker/docker/pull/7262)

If you commit multiple times the same container with different tag names, it will produce images with different ids:

~~~bash
docker commit 4d0a2c78d7ab quay.io/breezeight/test:1.0
docker commit 4d0a2c78d7ab quay.io/breezeight/test:1.1
docker images
REPOSITORY                          TAG                  IMAGE ID            CREATED             VIRTUAL SIZE
quay.io/breezeight/test             1.1                  3db75a60921e        3 minutes ago       2.433 MB
quay.io/breezeight/test             1.0                  60fa11675848        4 minutes ago       2.433 MB
~~~

### PULL - COMMIT - PUSH - TAG

* `docker pull <username>/<repository>` Download an existing image from dockerhub.
* `docker pull <YOUR-DOMAIN>:8080/test-image` download from a private repository (docker detects the domain regexp).

A group of special, trusted images such as the ubuntu base image can be retrieved by just their name <repository>. For images from the central index, the name you specify is constructed as <username>/<repository>


* `docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]` creates image from a container.
* http://docs.docker.io/reference/commandline/cli/#commit

With Docker, the process of saving the state is called committing. Commit basically saves the difference between the old image and the new state. The result is a new image. 

Docker has an unusual mechanism for specifying which registry to push to. You have to tag an image with the private registry's location in order to push to it. Let's tag our image to our private registry:

* `docker tag [OPTIONS] IMAGE[:TAG] [REGISTRYHOST/][USERNAME/]NAME[:TAG]` Tag an image into a repository
* `docker tag test-image YOUR-DOMAIN:8080/test-image` 

NOTE: the `tag` command is different from an image tag.

Now we can push that image to our registry. This time we're using the tag name only:

* `docker push <YOUR-DOMAIN>:8080/test-image`

Note: you need to login before you can push, see here some example:https://www.digitalocean.com/community/tutorials/how-to-set-up-a-private-docker-registry-on-ubuntu-14-04

### BUILD IMAGES from DOCKERFILE

http://docs.docker.io/reference/builder/
A Dockerfile is a simple text file consisting of instructions on how to build the image from a base image.
Executing docker build will run your steps and commit them along the way, giving you a final image.

Dockerfile  VS other build tools
https://groups.google.com/forum/#!topic/docker-user/3pcVXU4hgko

* `docker build -t breezeight/test-kitchen-ubuntu .` 
* `docker build --no-cache=true -t pippolippo .` build without using cache


#### Docker Build cache

Ref:

* http://www.centurylinklabs.com/caching-docker-images/

Docker creates a commit for each line of instruction in Dockerfile. All these command are cached and subsequent invocations will be faster. The caching mechanism store the command to be executed and the image produced by the previous command.

When does the cache is invalidated ?:

* changing any instruction in a RUN 
* changing any file of a COPY/ADD instruction
*  If you cause cache invalidation at one instruction, subsequent instructions doesn’t use cache. This is inevitable because Dockerfile uses the image built by the previous instruction as a parent image to execute next instruction


Possible issues:

* Cache is used for non-idempotent instructions: If you run a command that has external dependencies, docker will not detect changes to those deps, you need to to force  `docker build --no-cache=true`. Ex: you use `apt-get update`, 3 months later, Ubuntu made some security updates to their repository, so you rebuild the image by using the same Dockerfile hoping your new image includes the security updates. However, this doesn’t pick up the updates.


### Save and load an image to a tarball

A Docker image and its entire history can be saved to a tarball and loaded back again. This will preserve the history of the image:

* `docker save <IMAGE NAME> > /home/save.tar`
* `docker load <IMAGE NAME> < /home/save.tar`

Usecase: Move images and container without a registry (export/import  save/load)

### Trick to flatten the image story

ID=$(docker run -d image-name /bin/bash)
docker export $ID | docker import – flat-image-name

If you want to save it for backup you can use gzip to compress the image.
ID=$(docker run -d image-name /bin/bash)
(docker export $ID | gzip -c > image.tgz)
gzip -dc image.tgz | docker import - flat-image-name


refs:
http://blog.intercityup.com/downsizing-docker-containers/
http://tuhrig.de/flatten-a-docker-container-or-image/


### DOCKER DIFF

TODO

### REMOVE IMAGES

* `docker rmi <image_name>` 

## Monitoring and Stats TODO

* `docker info` 
* `docker version`
* https://docs.docker.com/articles/runmetrics/ 

# Advanced Guides

## How Docker integrates with the Boot and Root Filesystems of a guest

http://docs.docker.io/en/latest/terms/filesystem/

##  How to create a base OS image

https://docs.docker.com/articles/baseimages/

## Security

* [Docker Secure Deployment Guidelines](https://github.com/GDSSecurity/Docker-Secure-Deployment-Guidelines)

# My images

## Pitchtarget

The postgres image will use the default image volume, this means that it will bypass the COW filesystem and will store it in the 

## Postgres

https://davidamick.wordpress.com/2014/07/19/docker-postgresql-workflow/

# Docker Swarm

TODO:

* https://github.com/docker/swarm

Docker Swarm is native clustering for Docker. It turns a pool of Docker hosts into a single, virtual host.



# Docker Machine

REF:

* https://docs.docker.com/machine/
* https://github.com/docker/machine

Machine makes it really easy to create Docker hosts on your cloud providers and inside your own data center:

* It creates servers (it has integration with Azure, AWS, ...)
* installs Docker on them
* then configures the Docker client to talk to them (TLS config).

Docker Machine can also provision Swarm clusters. This can be used with any driver and will be secured with TLS.

## Docker Machine on Azure

[Docker Machine on Azure]({{ site.url }}/guides/azure.html#azure-and-docker-machine)

# Docker Compose (ex Fig tool)

Install: If you install from pip you will get an SSL error. Use brew install docker-compose

Compose is great for:

* development environments
* staging servers
* CI server. 

We don't recommend that you use it in production yet (april the 18th).

TODO: 

* http://docs.docker.com/compose/install/
* http://blog.docker.com/2015/02/announcing-docker-compose/

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

