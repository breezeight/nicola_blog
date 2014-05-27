---
layout: post
title: "dokku"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["chef", "docker", "paas"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# Dokku
This post will describe how **Dokku 0.23** works and how you could deploy it
with chef-dokku both on Azure and OpsWorks

References:

* [Dokku Github]()
* [Dokku Troubleshooting](https://github.com/progrium/dokku/wiki/Troubleshooting)
* [Dokku cookbook](https://github.com/pitchtarget/chef-dokku)
* [How dokku works](http://off-the-stack.moorman.nu/2013-11-23-how-dokku-works.html)
* [Dokku on OpsWork deploy](http://jonnybgod.ghost.io/using-dokku-with-aws-opsworks/)
* [Use grunt to trigger opsworks deployment](http://jonnybgod.ghost.io/use-grunt-to-trigger-opsworks-deployment/)

## Cheat Sheet

Get help:

~~~
ssh -i ~/.vagrant.d/insecure_private_key  dokku@10.0.0.2 help
~~~

Create an app:

~~~bash
git remote add dokku dokku@progriumapp.com:<MY_APP_NAME>
git push dokku <LOCAL_BRANCH>:master  #ONLY MASTER IS SUPPORTED
~~~

## Dokku components

Docker, Buildstep, [ssh-command](https://github.com/progrium/sshcommand), [pluginhook](https://github.com/progrium/pluginhook), ssh, git, nginx


### Component: sshcommand
Dokku is a really simple paas, it doesn't have a client for your workstation like Heroku. Dokku uses the ssh authorized_keys to run only a restricted set of commands directly on the server hosting dokku. The sshcommand make easy the management of users with restricted access.

Dokku gives to the dokku user the permission to execute only the dokku command:
`sshcommand create dokku /usr/local/bin/dokku`

This will add the configuration to  `/home/dokku/.ssh/authorized_keys`:

~~~
command="FINGERPRINT=dd:3b:b8:2e:85:04:06:e9:ab:ff:a8:0a:c0:04:6e:d6 NAME=vagrant `cat /home/dokku/.sshcommand` $SSH_ORIGINAL_COMMAND",no-agent-forwarding,no-user-rc,no-X11-forwarding,no-port-forwarding ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ== vagrant insecure public key
~~~

See here more details about how ssh restric which commands you can run http://binblog.info/2008/10/20/openssh-going-flexible-with-forced-commands/

To manage commands and user authorized to run those command dokku uses https://github.com/progrium/sshcommand it  

When you need to interact with dokku simply use ssh, example:

~~~
ssh  dokku@host help
ssh -i ~/.vagrant.d/insecure_private_key  dokku@10.0.0.2 help  #the command for the base chef-dokku deploy 
~~~

[This post](http://off-the-stack.moorman.nu/2013-11-23-how-dokku-works.html) explain really well how the sshcommand is used by Dokku.


### Pluginhook

[Pluginhook Homepage](https://github.com/progrium/pluginhook)
pluginhook is a commandline tool that allow to run multiple script hooks
by name. Hook are installed into subdir and all scripts with a given
name are executed. The pluginhook command simply loops through all plugin directories found in the path defined by the environment variable PLUGIN_PATH and passes the same arguments to any hook scripts by that name. This means installing a plugin is as simple as putting it in your PLUGIN_PATH. 

You can use 2 mode:

* broadcast: pluginhook post-commit $REV $USER
* pipe: echo "hello world" | pluginhook text

Dokku use pluginhook into the dokku executable to create hooks.


~~~bash

  build)
    APP="$2"; IMAGE="dokku/$APP"; CACHE_DIR="$DOKKU_ROOT/$APP/cache"
    id=$(cat | docker run -i -a stdin progrium/buildstep /bin/bash -c "mkdir -p /app && tar -xC /app")
    test $(docker wait $id) -eq 0
    docker commit $id $IMAGE > /dev/null
    [[ -d $CACHE_DIR ]] || mkdir $CACHE_DIR
    pluginhook pre-build $APP
    id=$(docker run -d -v $CACHE_DIR:/cache $IMAGE /build/builder)
    docker attach $id
    test $(docker wait $id) -eq 0
    docker commit $id $IMAGE > /dev/null
    pluginhook post-build $APP  ########## HOCK
    ;;

  release)
    APP="$2"; IMAGE="dokku/$APP"
    pluginhook pre-release $APP
    if [[ -f "$DOKKU_ROOT/$APP/ENV" ]]; then
      id=$(cat "$DOKKU_ROOT/$APP/ENV" | docker run -i -a stdin $IMAGE /bin/bash -c "mkdir -p /app/.profile.d && cat > /app/.profile.d/app-env.sh")
      test $(docker wait $id) -eq 0
      docker commit $id $IMAGE > /dev/null
    fi
    pluginhook post-release $APP   ########## HOCK
    ;;

  deploy)
    APP="$2"; IMAGE="dokku/$APP"
    pluginhook pre-deploy $APP   ########## HOCK
~~~



NB: It use the "command" convention instead


### Git

Dokku use git to create a tar of you source code and pipe it into build
step. Dokku use sshcommand to wrap the git-receive-pack and implements
it's workflow around the git lifecycle:

* When a new app is pushed to Dokku a new bare git repository is created
and a pre-receive hook is installed
* When the pre-receive hook is triggered it invoke `git archive` to exports the pushed application as tar archive to stdout and feed this to `dokku receive`.

~~~bash
case "$1" in
  receive)
    APP="$2"; IMAGE="app/$APP"
    echo "-----> Building $APP ..."
    cat | dokku build $APP $IMAGE
    echo "-----> Releasing $APP ..."
    dokku release $APP $IMAGE
    echo "-----> Deploying $APP ..."
    dokku deploy $APP $IMAGE
    echo "-----> Cleaning up ..."
    dokku cleanup
    echo "=====> Application deployed:"
    echo "       $(dokku url $APP)"
    echo
    ;;
~~~


[This post](http://off-the-stack.moorman.nu/2013-11-23-how-dokku-works.html) shows you all details


### Buildstep

[Homepage](https://github.com/progrium/buildstep).

Buildstep is the component that create a docker image using a base
image, a build pack and you application code.

~~~bash
FROM ubuntu:quantal
MAINTAINER progrium "progrium@gmail.com"

RUN mkdir /build
ADD ./stack/ /build
RUN LC_ALL=C DEBIAN_FRONTEND=noninteractive /build/prepare
RUN rm -rf /var/lib/apt/lists/*
RUN apt-get clean
~~~



Dokku use the git-receive plugin hook to 


https://www.andrewmunsell.com/blog/dokku-tutorial-digital-ocean

Provide a script to boot the app

Procfile should be something related to the Buildpack... 



is This an alternative to Progrium Buildstep, is it a fork?
https://index.docker.io/u/tutum/buildstep/

### Bash and GO

Dokku is mostly bash based and makes heavy use of [pipes](http://www.gnu.org/software/bash/manual/html_node/Pipelines.html). To be safe the pipefail option is enable on most of the pipe: `set -o pipefail`. If pipefail is enabled, the pipeline’s return status is the value of the last (rightmost) command to exit with a non-zero status, or zero if all commands exit successfully.


# Plugins:

## Postgres
* [Postgres](https://github.com/Kloadut/dokku-pg-plugin)

The plugin install create an image using a Dockerfile:

~~~bash
git clone https://github.com/Kloadut/dokku-pg-dockerfiles /tmp/dokku-pg-dockerfiles
docker build -q=true -t kloadut/postgresql /tmp/dokku-pg-dockerfiles
rm -rf /tmp/dokku-pg-dockerfiles
~~~

https://github.com/Kloadut/dokku-pg-plugin/blob/master/commands


# Dokku Cookbooks
The dokku-chef cookbook uses the [docker cookbook](https://github.com/bflad/chef-docker/) and has a well documented [Readme](https://github.com/fgrehm/chef-dokku).

Install/update basic dokku:

* **bootstrap recipe** : it will install the full dokku platform. When
sync attributes are true (default) the dokku command and all its
dependencies are updated pluginhooks. It includes th **buildstack recipe** : install a buildstack image on docker (by default use a prebuild image of buildstep). If you set default['dokku']['buildstack']['use_prebuilt'] = false   it will use the dockerfile at buildstep master git branch instead of the prebuild image. Include also **install recipe** : Clone the Dokku repository at revision ['dokku']['git_revision'] and install /usr/local/bin/dokku and default plugins (https://github.com/progrium/dokku/tree/master/plugins) into default['dokku']['plugin_path']= "/var/lib/dokku/plugins"

When the deploy is done you need apps, new admins and additional plugins:

* **plugins recipe** install any additional plugin listed into [:dokku][:plugins], ex: postgresql
* **apps recipe** create new applications and their envs
* **ssh\_keys recipe** : add new ssh keys for the dokku user


# Dokku on Opsworks

Use the deploy event on opswork
https://github.com/imoglobe/opsworks-cookbooks/blob/master/dokku_deploy/recipes/default.rb


# TODO

* How should we monitor containers?
* FIX: https://github.com/progrium/dokku/issues/402
* READ rails deploy: https://gist.github.com/linjunpop/6247236
* env plugins for dokku:
* Zero Downtime with dokku: https://labnotes.org/zero-downtime-deploy-with-dokku/
* User Env https://github.com/musicglue/dokku-user-env-compile
* https://www.andrewmunsell.com/blog/dokku-tutorial-digital-ocean


# Dokku Pull Request

* [Zero down-time deploy and server checks](https://github.com/progrium/dokku/pull/562)
* 
