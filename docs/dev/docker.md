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


# Related Documentation

* [Cheatsheet](https://github.com/wsargent/docker-cheat-sheet)
* [Docker Compose](dev/docker-compose.md)
* [Docker and Docker Compose arguments and environment variables](dev/docker-and-docker-compose-arg-env.md)

# HOWTO Docker Management

> [!NOTE]
> This section should be moved to a dedicated page.

## Garbage collection

https://github.com/zzrotdesign/docker-clean

https://github.com/rancher/sherdock

`docker run -d -v /var/lib/docker:/var/lib/docker -v /var/run/docker.sock:/var/run/docker.sock -p 8080:8080 rancher/sherdock`

## OSX Docker for MAC

ISSUE reduce qcow2 image (march 2017), Docker.qcow2 grows constantly:

* Ref: https://github.com/docker/for-mac/issues/371#issuecomment-265525709

```
docker rm -f $(docker ps -qa)
docker rmi -f $(docker images -q)
```
* restart docker

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

[Docker Internals: Networking](https://docs.google.com/document/d/1Q5LOZ2fm6nWgbaVBhjqjSZKrtwps91d34Jvmf7ui28o/edit?tab=t.0)


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

# Install and Tune Docker
On recent linux Docker is really easy to install but on OS like
windows and OSX it's a little bit harder and you need to use ONE classical virtual machine to run Linux and Docker.

## AWS

## OSX

### Under the Hood: Demystifying Docker For Mac

ref: https://collabnix.com/how-docker-for-mac-works-under-the-hood/
7TH MAY 2018

Docker For Mac:
* It runs on a LinuxKit VM and NOT on VirtualBox or VMware Fusion.
* LinuxKit is a framework for creating minimal Linux OS images purpose built for containers
* It embeds a hypervisor (based on xhyve), a Linux distribution which runs on LinuxKit and filesystem & network sharing that is much more Mac native.
* xhyve, a lightweight OS X virtualization solution https://github.com/machyve/xhyve

### HOWTO get a shell on The LinuxKit VM on OSX


https://gist.github.com/BretFisher/5e1a0c7bcca4c735e716abf62afad389
https://github.com/justincormack/nsenter1


`docker run -it --rm --privileged --pid=host justincormack/nsenter1`


WHY?
Here is one simple example: say you want to teach a few people about Docker networking and you want to show them how to inspect the default bridge network after starting two containers using ip addr show; the problem is if you are demonstrating with Docker for Mac, for example, your containers are not running on your host directly, but are running instead inside of a minimal Linux OS virtual machine specially built for running containers, i.e., LinuxKit. But being a lightweight environment, LinuxKit isn't running sshd, so how do you get access to a shell so you can run nsenter to inspect the namespaces for the process running as pid 1?

### Optimize Volumes Mounts

See: https://docs.docker.com/docker-for-mac/osxfs/#performance-issues-solutions-and-roadmap

to test how the volume is mounted you can inspect the container and check the `Mode` property of mounts:


```
"Mounts": [
    {
        "Type": "bind",
        "Source": "/Users/nicolabrisotto/SRC/betania/docker/tmp_builder_volumes/deps",
        "Destination": "/app/deps",
        "Mode": "delegated",
        "RW": true,
        "Propagation": "rprivate"
    },
```

### Cloudformation Template

https://docs.docker.com/docker-for-aws/#quickstart

usa DynamoDB per orchestrare info nel cluster:

```
get_primary_manager_ip()
{
    echo "Get Primary Manager IP"
    # query dynamodb and get the Ip for the primary manager.
    MANAGER=$(aws dynamodb get-item --region $REGION --table-name $DYNAMODB_TABLE --key '{"node_type":{"S": "primary_manager"}}')
    export MANAGER_IP=$(echo $MANAGER | jq -r '.Item.ip.S')
    echo "MANAGER_IP=$MANAGER_IP"
}
```


## Ubuntu 15.04

* To install: https://docs.docker.com/installation/ubuntulinux/
* To run the deamon with SystemD on boot  see: http://docs.docker.com/articles/systemd/ :
  * `sudo systemctl enable docker`

## OSX Docker Toolbox

Follow this Ref: http://docs.docker.com/installation/mac/

Next do:

* Add `eval "$(docker-machine env default)" ` to you bash profile to get the default machine connetion values available on each bash instance.
* add to `/etc/host`: 192.168.99.100  dockerhost , where the ip is the one returned by `docker-machine ip default`

Note:

* In an OS X installation, the docker daemon is running inside a Linux VM called `default`
* When you start the VM with docker-machine it is assigned an IP address.
* When you start a container, the ports on a container map to ports on the VM.
* when you start a container it automatically shares your /Users/username directory with the VM

Machine lets you create Docker hosts on your computer, on cloud providers, and inside your own data center. It works also with VirtualBox so it's a perfect replacement for Boot2Docker: it also configure directory sharing.


commands:

* `docker-machine start default`
* `docker-machine ssh default`
* `docker-machine stop default`
* `docker-machine inspect default`
* `docker-machine inspect ip`
* `docker-machine inspect env` :


# Docker components and Services
## Docker Registry

Docker-Registry is GO app that holds docker images: https://github.com/docker/docker-registry

A registry is, at its heart, a collection of repositories. In turn, a repository is collection of images. Users interact with the registry by pushing images to or pulling images from the registry.

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

#### Deploy a Registry

REF: https://docs.docker.com/registry/deploying/

`registry:2.0` image is for simple tests or debugging. Its configuration is unsuitable for most production instances.

#### Authentication

The registry service supports transport layer security (TLS) natively. You must configure it in your instance to make use of it. You can also use a proxy server such as Nginx and basic authentication to extend the security of a deployment.

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

### Official images from scratch: Ubuntu

* https://hub.docker.com/_/ubuntu/
* https://github.com/tianon/docker-brew-ubuntu-core/blob/3c355946fd5164da3f31063a5c5f249c826f7071/precise/Dockerfile


A base image starts from a special image:
https://hub.docker.com/_/scratch/

An explicitly empty image, especially for building images "FROM scratch".

As of Docker 1.5.0 (specifically, docker/docker#8827), FROM scratch is a no-op in the Dockerfile, and will not create an extra layer in your image (so a previously 2-layer image will be a 1-layer image instead).

Article about base image: https://docs.docker.com/engine/articles/baseimages/

### Official images: Language Stacks

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

# Dockerfile TIPS and BEST Practices

## Multistage

https://medium.com/@tonistiigi/advanced-multi-stage-build-patterns-6f741b852fae

## CHOWN optimization

It’s a common practice to set the owner of some files/folders via chown after copying the files. But with Docker this can unintentionally increase image size. See this fragment of a Dockerfile:

```
COPY . /dest-folder
RUN chown -R someuser:somegroup /dest-folder
```

This works, but the result are two layers with the same size (use docker history to see the size added by each layer).
Since Docker 17.09 there is a way to do the same things without wasting space:

```
COPY --chown=someuser:somegroup . /dest-folder
```

Just one layer, no size duplication. Read more about this here: https://blog.mornati.net/docker-images-and-chown/

# Basic Docker Guides and Articles

References:

* [CLI Commands reference](https://docs.docker.com/reference/commandline/cli)
* list of the [official Docker guides](https://docs.docker.com/userguide/)
* [list of official Docker articles](https://docs.docker.com/articles/basics/)
* [Cheatsheet](https://github.com/wsargent/docker-cheat-sheet)

## Path Cheatsheet

Docker-compose:

* Volume path are reletive to the first docker-compose file
* Docker file path is relative to the context

Dockerfile:

* COPY/ADD path are relative to the context

## Manage data in Docker

General intro https://docs.docker.com/storage/

By default all files created inside a container are stored on a writable container layer. Writing into a container’s writable layer requires a storage driver to manage the filesystem. The storage driver provides a union filesystem, using the Linux kernel. This extra abstraction reduces performance as compared to using data volumes, which write directly to the host filesystem.

Docker has other 3 options for containers to store files in the host machine, so that the files are persisted even after the container stops:

* volumes
* bind mounts
* tmpfs mount (Linux only)

No matter which type of mount you choose to use, the data looks the same from within the container.

A volume can is a directory that is located outside of the root filesystem of your container. This allows you to import this directory in other containers. You can also use volumes to mount directories from your host machine inside a container.

The main difference among volumes, bind mounts, and tmpfs mounts is: "where the data lives on the Docker host":

* Volumes are stored in a part of the host filesystem which is managed by Docker (/var/lib/docker/volumes/ on Linux). Non-Docker processes should not modify this part of the filesystem. Volumes are the best way to persist data in Docker.

* Bind mounts may be stored anywhere on the host system. They may even be important system files or directories. Non-Docker processes on the Docker host or a Docker container can modify them at any time.

* tmpfs mounts are stored in the host system’s memory only, and are never written to the host system’s filesystem.


NOTE: the use of volumes key and the `volume` type can generate confusion, they refer to different concepts.

Docker-compose has a short and long syntax to declare volumes, I prefer the long, which is more explicit:

https://docs.docker.com/compose/compose-file/#volumes

You can mount a host path as part of a definition for a single service, and there is no need to define it in the top level volumes key.

But, if you want to reuse a volume across multiple services, then define a named volume in the top-level volumes key.

### Data volumes

WARNING: this is an outdated trick

When you define a volume a directory of the docker host is mounted into a directory of a docker container.
When a Docker container is deleted, relaunching the image will start a fresh container without any of the changes made in the previously running container. In order to be able to save (persist) data and share data between containers, Docker came up with the concept of volumes.


You can define a data volume using:

* `VOLUME` in the Dockerfile
* `-v`, `--volume` option of docker run

If you don't specify which directory of the host you want to mount, docker will create one for you, usually into `/mnt/sda1/var/lib/docker/vfs/dir/`.
WARNING: Docker never automatically delete volumes when you remove a container, nor will it "garbage collect" volumes that are no longer referenced by a container. You could fill you disk space very quickly. Use `docker rm -v` to remove both the container and its volumes.

* `docker run -v /webapp` or `VOLUME /webapp`: will mount a randomly generated host directory into the `/webapp` dir (ex: `/mnt/sda1/var/lib/docker/vfs/dir/14119ff8f75bd5050ffd3c7fe37ee7ed1eb76513e9933208162cfc75788390f7`).

* `docker run -v /docker_host_dir:/webapp`: will mount the dockerhost `/docker_host_dir:` directory into the `/webapp` container directory. NOTE: you cannot use `VOLUME` to do this operation. 


To inspect an image's volumes:

```
docker inspect postgres | jq .[0].ContainerConfig.Volumes
{
  "/var/lib/postgresql/data": {}
}
```

### Volume Permissions and Ownership

REF:

* https://forums.docker.com/t/volume-not-writable-to-non-root-user-container/36103/2
* http://container-solutions.com/2014/12/understanding-volumes-docker/
* http://container42.com/2014/11/18/data-only-container-madness/

Often you will need to set the permissions and ownership on a volume or initialise the volume with some default data or configuration files. The key point to be aware of here is that anything after the VOLUME instruction in a Dockerfile will not be able to make changes to that volume e.g:

```
FROM debian:wheezy
RUN useradd foo
VOLUME /data
RUN touch /data/x
RUN chown -R foo:foo /data
```

Will not work as expected. We want the touch command to run in the image’s filesystem but it is actually running in the volume of a temporary container. The following will work:

```
FROM debian:wheezy
RUN useradd foo
RUN mkdir /data && touch /data/x
RUN chown -R foo:foo /data
VOLUME /data
```

Docker is clever enough to copy any files that exist in the image under the volume mount into the volume and set the ownership correctly. This won’t happen if you specify a host directory for the volume (so that host files aren’t accidentally overwritten).

If you can’t set permissions and ownership in a RUN command, you will have to do so using a CMD or ENTRYPOINT script that runs after container creation.

### How to clean up volumes

* https://github.com/chadoe/docker-cleanup-volumes
* `docker run -v $(which docker):/bin/docker -v /var/run/docker.sock:/var/run/docker.sock -v $(readlink -f /var/lib/docker):/var/lib/docker --rm martin/docker-cleanup-volumes --dry-run`

### Inspect Volumes of images and containers

* To list volumes of an image (ex: redis:2.8.20): `docker inspect redis:2.8.20 | jq '.[0].Config.Volumes'`

```
{
  "/data": {}
}
```

redis:2.8.20 Dockerfile with `VOLUME /data` command: https://github.com/docker-library/redis/blob/7d9f53256f8e13aa4dff2112145c69c22f8ce394/2.8/Dockerfile

* To list volumes mounted by a container:  `docker inspect addictiveapi_redis_1 | jq '.[0].Mounts'`

```
[
  {
    "Source": "/mnt/sda1/var/lib/docker/volumes/515a65e7fc61c330622025a5de1602145164841de31cdc2f705eaf2fdbc76b66/_data",
    "Destination": "/data",
    "Mode": "rw",
    "RW": true
  }
]
```

Source is the directory in the host, destination the directory in the container.

To list volumes from other containers: `docker inspect addictiveapi_redis_1 | jq '.[0].HostConfig.Binds'`


### Use Cases

* development: we can mount our source code inside the container and see our application at work as we change the source code.
* database: we can use the volume as data directory for the database, this will by-pass the COW filesystem and will increase performance.


## CONTAINERS

Cheatsheet:

* `docker ps` - Lists containers.
* `docker logs` - Shows us the standard output of a container.
* `docker stop` - Stops running containers.

https://docs.docker.com/articles/basics/#controlling-containers

### RUN: run a commando into a container

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

#### Run multiple commands

To run multiple commands in docker, use `/bin/bash -c` and semicolon ;

Example: `docker run image /bin/bash -c "cd /path/to/somewhere; python a.py"`



#### Environment variables

REF: https://docs.docker.com/userguide/dockerlinks/#environment-variables

You can set env variables when you run a container using:

* the ENV commands in the source container's Dockerfile
* the `-e`, `--env` and `--env-file` options on the docker run command when the source container is started
* Order of these three flags, the --env-file are processed first, and then -e, --env flags.

Example:

~~~
cat ./env.list
TEST_FOO=BAR
$ sudo docker run --env TEST_FOO="This is a test" --env-file ./env.list busybox env | grep TEST_FOO
TEST_FOO=This is a test
~~~

NOTE:

* Docker creates several environment variables when you link containers. Docker automatically creates environment variables in the target container based on the `--link` parameters.
* Warning: It is important to understand that all environment variables originating from Docker within a container are made available to any container that links to it. This could have serious security implications if sensitive data is stored in them.


TODO: capire bene come funziona questa naming convention delle variabili

#### multiplatform support

Docker : https://stackoverflow.com/questions/67458621/how-to-run-amd64-docker-images-on-arm64-host-platform


```bash
docker run --rm -ti --platform linux/arm/v7 ubuntu:latest uname -m
# armv7l

docker run --rm -ti --platform linux/amd64 ubuntu:latest uname -m
# x86_64
```
Docker compose: ....

### CMD vs ENTRYPOINT vs RUN


http://stackoverflow.com/questions/21553353/what-is-the-difference-between-cmd-and-entrypoint-in-a-dockerfile



https://aboullaite.me/dockerfile-run-vs-cmd-vs-entrypoint/

Short version:

* RUN executes the command(s) that you give in a new layer and creates a new image. This is mainly used for installing a new package.
* CMD is the default command to be run by the entrypoint. It sets default command and/or parameters, however, we can overwrite those commands or pass in and bypass the default parameters from the command line when docker runs
* ENTRYPOINT is the program to run the given command. It is used when yo want to run a container as an executable with `docker run` (but you can override it with --entrypoint).


Note that [CMD instruction](https://docs.docker.com/engine/reference/builder/#cmd) has three forms:

* `CMD ["executable","param1","param2"]` (exec form, this is the preferred form)
* `CMD ["param1","param2"]` (as default parameters to ENTRYPOINT)
* `CMD command param1 param2` (shell form)


The command is optional because the person who created the IMAGE may have already provided a default COMMAND using the Dockerfile CMD instruction. As the operator (the person running a container from the image), you can override that CMD instruction just by specifying a new COMMAND.

If the image also specifies an ENTRYPOINT then the CMD or COMMAND get appended as arguments to the ENTRYPOINT.

The ENTRYPOINT of an image is similar to a COMMAND because it specifies what executable to run when the container starts, but it is (purposely) more difficult to override. The ENTRYPOINT gives a container its default nature or behavior, so that when you set an ENTRYPOINT you can run the container as if it were that binary, complete with default options, and you can pass in more options via the COMMAND. But, sometimes an operator may want to run something else inside the container, so you can override the default ENTRYPOINT at runtime by using a string to specify the new ENTRYPOINT.

####  Shell vs. Exec

All three instructions RUN, CMD and ENTRYPOINT support two different forms:

* the shell form: `/bin/sh -c < instruction > < command >`
* the exec form: ` ` 

You may run into problems with the shell form if you're building a minimal image which doesn't even include a shell binary. When Docker is constructing the command to be run it doesn't check to see if the shell is available inside the container.

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

To set the user use `docker exec -u user_name`

### Remove stopped containers

REF: http://blog.stefanxo.com/2014/02/clean-up-after-docker/

* `docker rm <container>` 
* `docker rm $(docker ps -a -q)`  remove all stopped containers
  * `-q, --quiet=false`           Only display numeric IDs


### Remove unused images

`docker rmi $(docker images | grep "^<none>" | awk '{print $3}')`

## NETWORKING

refs:

* [Docker neworking Official Doc](https://docs.docker.com/network/)
* [Linking Container Together](http://docs.docker.com/userguide/dockerlinks/)
* [Docker Networking Explained](https://codability.in/docker-networking-explained/)

When Docker starts with the default configuration:

* it creates a virtual interface named `docker0` on the host machine, a virtual Ethernet bridge that automatically forwards packets between any other network interfaces that are attached to it.
* randomly chooses an address and subnet from the private range
* For each container Docker assign an internal network and an IP address
* Docker manages the DNS configuration mounting these files:

~~~
$$ mount
...
/dev/disk/by-uuid/1fec...ebdf on /etc/hostname type ext4 ...
/dev/disk/by-uuid/1fec...ebdf on /etc/hosts type ext4 ...
/dev/disk/by-uuid/1fec...ebdf on /etc/resolv.conf type ext4 ...
...
~~~

### Primer on Linux Networking: Linux Network Namespaces, Virtual Ethernet Devices, Linux Bridges, NAT and IPtables

#### Linux Network Namespaces
Any installation of Linux has a single set of network interfaces and routing table entries. You can modify the routing table entries add or delete policies using iptables, but that doesn’t fundamentally change the fact that the set of network interfaces and routing tables/entries are shared across the entire OS. With network namespaces, you can have different and separate instances of network interfaces and routing tables that operate independent of each other.

* create a network namespace `ip netns add <new namespace>`
* list all the available name spaces: `ip netns list`

To make use of these namespaces, we need to connect it to physical network devices and interfaces.

Assign a physical interface to a network namespace: `ip link set dev <device> netns <namespace>`

OR.... [TODO] connect a network namespace to the physical network, we can simply use a bridge. (More on that later)

NOTE: These commands mentioned above are just for your understanding, and to create and manage robust namespaces is an extremely difficult task, but this entire configuration becomes almost transparent when working with docker.

Each Docker container has its own network stack, using the Linux network namespace, where a new network namespace for each container is instantiated and cannot be seen from outside the container or from other containers.

#### Virtual Ethernet Devices

A virtual ethernet device or veth is a Linux networking interface that acts as a connecting wire between two network namespaces. A veth is a full duplex link that has a single interface in each namespace. Traffic in one interface is directed out the other interface. Docker network drivers utilize veths to provide explicit connections between namespaces when Docker networks are created. When a container is attached to a Docker network, one end of the veth is placed inside the container (usually seen as the ethX interface) while the other is attached to the Docker network.

#### Linux Bridges



### Communication between containers --link option

WARNING: DEPRECATED, use Embedded DNS server in user-defined networks

### Embedded DNS server in user-defined networks

https://docs.docker.com/engine/userguide/networking/configure-dns/

As of Docker 1.10, the docker daemon implements an embedded DNS server which provides built-in service discovery for any container created with a valid name or net-alias

### Binding container ports to the host -P and -p flags

[Docker DOC](https://docs.docker.com/articles/networking/#binding-container-ports-to-the-host)

`-P` or `--publish-all=true` flag:

* When that container is created with the -P flag it automatically maps any network ports mentioned in the `EXPOSE` line to a random high port from the range 49153 to 65535 on the Docker host.

`sudo docker run -d -P training/webapp python app.py` :

~~~
 sudo docker ps nostalgic_morse
CONTAINER ID  IMAGE                   COMMAND       CREATED        STATUS        PORTS                    NAMES
bc533791f3f5  training/webapp:latest  python app.py 5 seconds ago  Up 2 seconds  0.0.0.0:49155->5000/tcp  nostalgic_morse
~~~

`-p IP:host_port:container_port` or `-p HOST_PORT:CONTAINER_PORT` flags to :

* When you use the `-p flag` you can specify which interface/port map from the host to a container port

* `sudo docker run -d -p 5000:5000 training/webapp python app.py` :  bind a container's ports to a specific docker host port
* you can also specify a binding to a specific interface, for example only to the localhost: `sudo docker run -d -p 127.0.0.1:5000:5000 training/webapp python app.py`
* to bind port 5000 of the container to a dynamic port but only on the localhost: `sudo docker run -d -p 127.0.0.1::5000 training/webapp python app.py`
* You can also bind UDP ports by adding a trailing /udp : `sudo docker run -d -p 127.0.0.1:5000:5000/udp training/webapp python app.py`

### docker port

`docker port`: showed us the current port bindings

### TODO

capire se pipeworks ha ancora senso o meno
https://github.com/jpetazzo/pipework

Docker-user ›
container needs to know daemon's dynamically selected port from -p, and hosts 'public' ip address
https://groups.google.com/forum/#!topic/docker-user/KUbcMt1lARE


## Inspect containers or images

Basic command: `docker inspect [OPTIONS] CONTAINER|IMAGE [CONTAINER|IMAGE...]`

To find mounted volumes:

~~~
docker inspect 0ce31ad91a37 | jq .[0].Volumes
{
  "/var/lib/postgresql/data": "/mnt/sda1/var/lib/docker/vfs/dir/be36286d41c305d323dcd1abb450f5c1954fcf88cff0011644018ae5a40f4680"
}
~~~

In the above example the docker host directory is mounted into the `/var/lib/postgresql/data` container directory.


## Sharing of Resources

* https://goldmann.pl/blog/2014/09/11/resource-management-in-docker/

CPU A few things to remember:

* a CPU share is just a number — it’s not related to the CPU speed
* By default new containers have 1024 shares
* On an idle host a container with low shares will still be able to use 100% of the CPU
* You can pin a container to specific core, if you want

## IMAGES

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

### Build multi-arch images with BuildX

https://docs.docker.com/desktop/multi-arch/#build-multi-arch-images-with-buildx

### Info

* [`docker history`](http://docs.docker.io/reference/commandline/cli/#history) shows history of image.
* [`docker tag`](http://docs.docker.io/reference/commandline/cli/#tag) tags an image to a name (local or registry).

Docker image ids are [sensitive information](https://medium.com/@quayio/your-docker-image-ids-are-secrets-and-its-time-you-treated-them-that-way-f55e9f14c1a4) and should not be exposed to the outside world.  Treat them like passwords.

### Build

Ref: https://docs.docker.com/reference/builder/

context of the build:

* is the directory you pass as argument to docker build
* you can exclude files and directories by adding a `.dockerignore` file to the directory.

#### [JOB] Debug a failed build step

Every single build step of the docker build process is done in a container that is still accessible after a build step failure.

Usecase: a build could that takes several hours, so rewinding prior to the failed command and running it again takes a long time and is not very helpful.

The solution is:

* find the id of last container that failed: `docker ps -l -q`, return `3aac236d8281`
* commit the image: `docker commit 3aac236d8281`, return `sha256:c4dfce3f18eea752e16e19b1f638faf8c666d3fa900bf0b567ee03433dc049b4`
* to run a bash `docker run -it c4dfce3f18eea752e16e19b1f638faf8c666d3fa900bf0b567ee03433dc049b4 bash`
* to rerun the build step command: `docker run -it c4dfce3f18eea752e16e19b1f638faf8c666d3fa900bf0b567ee03433dc049b4`
* To cleanup `docker rmi c4dfce3f18eea752e16e19b1f638faf8c666d3fa900bf0b567ee03433dc049b4`, and before delete all the containers

NOTE: If you tried to start the failed container again it would run the command that failed again, and you'd be back where you started. By creating an image you can start a container with a different start command.

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

### Tagging strategies for images

* The problem is well descibed here: https://github.com/docker/docker/issues/13928


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

## Manage secrets

* Secrets: write-up best practices, do's and don'ts, roadmap https://github.com/docker/docker/issues/13490


TODO: docker and Vault:

* https://github.com/hashicorp/vault/issues/164
* https://github.com/hashicorp/vault/issues/165

Idea for deploy keys:

* create and then destroy an ssh key
* https://confluence.atlassian.com/display/BITBUCKET/deploy-keys+Resource#deploy-keysResource-POSTanewkey

Docket: https://github.com/defunctzombie/docket

Docker ssh forward: https://gist.github.com/d11wtq/8699521


# ELIXIR PHOENIX


# EMBER




# RAILS: Docker, docker-compose, docker-swarm

VEDERE con calma questi:

* https://github.com/finnlabs/rails-docker Parte da docker-passenger, risolve il problema della chiave ssh per repo privati usando questa soluzione:  http://simonrobson.net/2014/10/14/private-git-repos-on-docker-images.html
* http://bradgessler.com/articles/docker-bundler/  Make bundler fast again in Docker Compose

Anche questa è una buona lettura che riassume il workflow con rails e compose: http://blog.carbonfive.com/2015/03/17/docker-rails-docker-compose-together-in-your-development-workflow/

dovrei mettere `prepare_docker_build.sh` preso da rails-docker in uno step precedente la build dell'immagine

TODO: docker-compose for development and for production
TODO production:

* update to rails 4.2 and active jobs
* update to active jobs
* docker-compose:
  * postgres
  * come passare le variabili d'ambiente?? Come usare `/etc/hosts` ?

Draft:

~~~
FROM phusion/passenger-ruby22

RUN rm /etc/nginx/sites-enabled/default  # NGINX
ADD docker/passenger/addictive-api-nginx.conf /etc/nginx/sites-enabled/addictive-api-nginx.conf

RUN bundle config --global frozen 1 # configure bundler to throw errors if the Gemfile has been modified since Gemfile.lock

RUN mkdir -p /srv/www/addictive-api
WORKDIR /srv/www/addictive-api

COPY Gemfile /srv/www/addictive-api/
COPY Gemfile.lock /srv/www/addictive-api/
RUN bundle install

COPY . /srv/www/addictive-api/
~~~

NOTE: bundler will still connect to rubygems.org to check whether a platform-specific gem exists for any of the gems in vendor/cache. So the only problem that could happen is with private native gems.

## RAILS and docker-composer

TODO: https://blog.metova.com/containerize-your-development-environment-using-docker



* You will need to re-run the docker-compose build command every time you change the Dockerfile or Gemfile.
* developing with Docker added very little overhead to the development process. In fact, most commands that you would run for Rails simply needed to be prepended with a docker-compose run web

common commands:

* bundle install:	docker-compose run web bundle install
* rails s : docker-compose run web rails s
* rspec spec/path/to/spec.rb :	docker-compose run web rspec spec/path/to/spec.rb
* RAILS_ENV=test rake db:create : 	docker-compose run -e RAILS_ENV=test web rake db:create
* tail -f log/development.log :	docker-compose run web tail -f log/development.log


Database volume: ????
Code volume: ????

TODO: documentare il perchè esiste docker/environments/production.conf: comunica ad nginx di propagare le variabili d'ambiente...  come potrei fare a tenerlo aggiornato in modo smart????

To use byebug see here: http://blog.carbonfive.com/2015/03/17/docker-rails-docker-compose-together-in-your-development-workflow/

### FAQ

* When closing a container with a rails app, rails doesn't delete /tmp/pids/server.pid: https://github.com/docker/compose/issues/1393

## Orats: dockerized app generator

It's a really simple project that generate an opinionated Rails app customize for Docker.

TODO: capire perchè non si poteva usare semplicemente un template di Rails

* https://nickjanetakis.com/blog/dockerize-a-rails-5-postgres-redis-sidekiq-action-cable-app-with-docker-compose
* https://github.com/nickjj/orats

## Create Images with BuildRoot

TODO

* http://slides.com/aukewillem/minimal-docker#/

Cons

* Makefile are not so easy to manage and debug
* not so mainstream

Pro

* Very simple workflow
* You can recycle the buildroot expertice in the embedded world

## Links

* github.com/OrangeTux/minimal-docker-python-setup
* github.com/AdvancedClimateSystems/docker-buildroot
* blog.docker.com/2013/06/create-light-weight-docker-containers-buildroot/
* hub.docker.com/r/advancedclimatesystems/python/
* buildroot.uclibc.org/downloads/manual/manual.html

##

* Example: http://michaelcoyote.github.io/2015/08/02/lean-container-tricks/

## User BUILDROOT from a DOCKER IMAGE

SEE "_guide/embedded_distro.markdown"

## Example: minimal Nginx-uWSGI-Flask-Redis stack

https://github.com/OrangeTux/minimal-docker-python-setup


## Passenger Image

* http://phusion.github.io/baseimage-docker
* https://github.com/phusion/baseimage-docker
* https://groups.google.com/forum/#!forum/passenger-docker


KEY POINT: this images solves the PID 1 zombie reaping problem: https://blog.phusion.nl/2015/01/20/docker-and-the-pid-1-zombie-reaping-problem/

It implements a minimal (6 MB RAM) multiprocess image based on `baseimage-docker` that provide:

* `/sbin/my_init` reaps orphaned child processes correctly, and responds to SIGTERM correctly. This way your container won't become filled with zombie processes, and docker stop will work correctly.
* `syslog-ng`
* `cron`
* `SSH server`
* `logrotate`
* `runit` Used for service supervision and management.
* `setuser` A custom tool for running a command as another user. Easier to use than su, has a smaller attack vector than sudo, and unlike chpst this tool sets $HOME correctly. Available as /sbin/setuser.

### Cheatsheet


* docker run --rm -t -i phusion/baseimage:<VERSION> /sbin/my_init -- bash -l
* docker exec --rm -t -i phusion/baseimage:<VERSION> /sbin/my_init -- bash -l
* additional daemon: https://github.com/phusion/baseimage-docker#adding-additional-daemons


### baseimage-docker how it's build

See below how the image is build

* its `FROM ubuntu:14.04` 
* `make build`  
* `image/Dockerfile`

* The Dockerfile will do the setup of the basic services above.
* the `runit` dir contains all the runit script for basic services, `config` all the configurations.

### passenger-docker how it's build

If you run for example `make build_ruby22` the image is build locally.
It will copy the whole `image` dir and set the ruby22 variable, then build the `image/Dockerfile`

~~~
build_ruby22:
	rm -rf ruby22_image
	cp -pR image ruby22_image
	echo ruby22=1 >> ruby22_image/buildconfig
	echo final=1 >> ruby22_image/buildconfig
	docker build -t $(NAME)-ruby22:$(VERSION) --rm ruby22_image
~~~

Basically the `image/install.sh` script is entry point that make all the work and runs a sequence of scripts. 

`image/enable_repos.sh` :

* add brightbox ppa for ruby
* add other ppa for redis, openJDK, etc
* apt-get update

`image/prepare.sh`:  Create `app` user and group for the web app

`image/utilities.sh`:  install build-essential and git

`image/rubyX.Y.sh` (note: you can enable the installation of other sw redis, memcache, etc):

* install ruby from brigtbox
* use ubuntu `update-alternatives` to set the default ruby, rake, gems, etc
* install rake and bundler

`image/ruby-finalize.sh`:

* install with apt-get dependencies for common gems (psql, etc)
* use `ruby-switch` to set default system-wide interpreter for your Debian system

`image/nginx-passenger.sh`

* `apt-get install -y nginx-extras passenger` 
* set `image/config/nginx.conf`
* ?????? 30_presetup_nginx.sh
* nginx_main_d_default.conf ???????? do something with the environment
* `runit/nginx-log-forwarder /etc/service/nginx-log-forwarder/run` enable the nginx log forwarder


`image/finalize.sh` : cleanup apt-get cache and remove build scripts

### Running scripts at startup

https://github.com/phusion/baseimage-docker#running-scripts-during-container-startup

### Adding additional daemons

https://github.com/phusion/baseimage-docker#adding-additional-daemons

#### Sidekiq example



### Env variables

https://github.com/phusion/baseimage-docker#environment-variables

### Configuring and managing Nginx

Ref: https://github.com/phusion/passenger-docker#configuring-nginx

By default nginx is disabled, to enable it add `RUN rm -f /etc/service/nginx/down` 

The nginx file from `image/config/nginx.conf` will be copied to `/etc/nginx/nginx.conf` and will include with glob three directory:

~~~
include /etc/nginx/main.d/*.conf;

http {
  ...
  include /etc/nginx/conf.d/*.conf;
	include /etc/nginx/sites-enabled/*;
  ...
}
~~~

* `site-enabled` for application definition (server)
* `main.d` to override or

From your Dockerfile you can add file to those directories to change the NGINX config

### Finnlabs rails-docker based on passenger-docker, Addictive-api example

[Home Page](https://github.com/finnlabs/rails-docker)

Finnlabs derived this image from the phusion passenger image, for addictive-api I use a similar approach

The app is installed into `/home/app`

NOTE: This image solves the problem of using private git repository for gems becouse it package them.





# Common images and workflows

## Pitchtarget

The postgres image will use the default image volume, this means that it will bypass the COW filesystem and will store it in the

## Mongodb

https://hub.docker.com/r/library/mongo/

mkdir -p deployment/seed

Compose snippet `docker-compose.dev.yml`:

```
version: '2'

services:
  mongo:
    image: mongo:2.4.11
    volumes:
    - mongo-data:/data/db
    - ./deployment/seed:/data/seed

volumes:
  mongo-data:
```

We create a named volume "mongo-data" to persist


`docker-compose -f docker-compose.dev.yml run --rm mongo  mongorestore -h mongo -d storage_padova_push /data/seed/storage_padova_push`



## Rabbitmq


## Postgres


### Official postgres image on dockerhub

It's a quite simple image that install Postgres and run a simple script as entrypoint:

https://github.com/docker-library/postgres/blob/a82c28e1c407ef5ddfc2a6014dac87bcc4955a26/9.4/docker-entrypoint.sh

For local developmnet if you leave the `POSTGRES_PASSWORD` and `POSTGRES_USERNAME` empty the database will accept connection without password and a default ROLE postgres is created :

* add "host all all 0.0.0.0/0 trust" into "$PGDATA/pg_hba.conf"
* to connect: psql -h db -U postgres


### Other Postgres alternative

https://davidamick.wordpress.com/2014/07/19/docker-postgresql-workflow/


# Docker Cloud

Tutum is now Docker Cloud. Docker Cloud is a new service by Docker that implements all features previously offered by Tutum plus integration with Docker Hub Registry service and the common Docker ID credentials.

Ref:

* https://github.com/docker/dockercloud-cli
* brew install docker-cloud
* https://cloud.docker.com


Scan images for security issues: https://docs.docker.com/docker-cloud/builds/image-scan/

Services are logical groups of containers from the same image.

Stack: https://stackfiles.io

Create a stack: `docker-cloud stack create -f docker-cloud.yml`

[Stack yaml reference](https://docs.docker.com/docker-cloud/feature-reference/stack-yaml-reference/)

NOTE: there is still no multiusers but they are working on it https://forums.docker.com/t/multiple-users-access-to-docker-cloud/11596

## Docker Cloud Azure

Vedi guida su DevOps Pitchtarget:

https://docs.google.com/document/d/10rmKZYHvImmiKDrH9ydQtfqVnlWLdwlgYuXb2YM5194/edit#

## Docker Cloud CLI


# Docker Swarm

TODO:

* https://github.com/docker/swarm

Docker Swarm is native clustering for Docker. It turns a pool of Docker hosts into a single, virtual host.

## Docker Swarm on Azure

*

* https://ahmetalpbalkan.com/blog/docker-swarm-azure/

* ACS preview: https://azure.microsoft.com/en-us/blog/azure-container-service-preview/

# Docker Machine

REF:

* https://docs.docker.com/machine/
* https://github.com/docker/machine

Machine makes it really easy to create Docker hosts on your cloud providers and inside your own data center:

* It creates servers (it has integration with Azure, AWS, ...)
* installs Docker on them
* then configures the Docker client to talk to them (TLS config).

Docker Machine can also provision Swarm clusters. This can be used with any driver and will be secured with TLS.


Cheatsheet:

* docker-machine env default

## Docker Machine import/export machines

This is still an open issue: https://github.com/docker/machine/issues/23



## Docker Machine on Azure

[Docker Machine on Azure](azure.md#azure-and-docker-machine)

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
