
# Docker-Compose

## Install

OSX: use the Docker App

## Intro

Docker Compose acts as a wrapper around Docker – it links your containers together and provides syntactic sugar around some complex container linking commands.
It can coordinate and spin up your entire application and dependencies with one command.

With Compose, you use a Compose file to configure your application’s services. Then, using a single command, you create and start all the services from your configuration.

A service definition contains configuration which will be applied to each container started for that service, much like passing command-line parameters to:

* `docker run`.
* `docker network create`
* `docker volume create`

Compose is great for:

* development environments
* staging servers
* CI server.

We don't recommend that you use it in production yet (april the 18th 2015).


## cheatsheet:

* `docker-compose up`
* `docker-compose stop`
* `docker-compose logs` : watch the logs of all our containers
* `service` : the main stanzas in th docker-compose.yml file (ex: web, db, redis)
* `docker-compose down`

A single service (“container”) out of a docker-compose.yaml file is rebuilt and restarted like this:

```
docker-compose build
docker-compose up -d  # runs containers, but returns immediately
# Oops, something needs to be changed
docker-compose stop web
# Make changes
docker-compose build web
docker-compose up -d --no-deps web
```
NOTE:  `--no-deps` don't restart services on which the service depends on

TODO: capire meglio quando server rifare una build: Quando cambiano i file di cui facciamo COPY/ADD ? Quando cambiamo ENV o file ENV ?
TODO: capire come forzare il pull delle immagini se usiamo latest tag



## Naming convention:

* the directory containing the `docker-compose.yml` file is used in the give a prefix to services and images
  * `-`, `_`, spaces, etc are removed (ex: addctive-api becomes addictiveapi)
  * you can ovverride this default behavior with the `-p` option
* name of the images that are built is: `<containingDIR>_<service_name>`
* name of the containers: `<containingDIR>_<service_name>_<incremental_number>`

ex: `addctive-api/docker-compose.yml` with a service named `web` creates a container named: `addictiveapi_web_1`


## Containers and Images lifecycle with compose

Images: http://stackoverflow.com/questions/32612650/how-to-get-docker-compose-to-always-start-fresh-images

Container lifecycle: when you use `docker-compose stop` and then `up`, docker compose will not recreate container but will use `docker start`. It uses docker labels to find the proper container

Labels in compose 1.5: ref: https://github.com/docker/compose/pull/1356/files

Docker compose adds labels to container

* LABEL_CONTAINER_NUMBER = 'com.docker.compose.container-number'
* LABEL_ONE_OFF = 'com.docker.compose.oneoff'
* LABEL_PROJECT = 'com.docker.compose.project'
* LABEL_SERVICE = 'com.docker.compose.service'
* LABEL_VERSION = 'com.docker.compose.version'

## Volumes lifecycle with compose

HOW to Remove a named volume with docker-compose?

* docker-compose down -v
* Ref: https://stackoverflow.com/questions/45511956/remove-a-named-volume-with-docker-compose


TODO: fare qualche test con la cancellazione e rigenerazione

https://github.com/docker/compose/issues/2308 :
https://github.com/docker/compose/issues/1882 :

* using an image that defines a volume
* in a docker-compose.yml that overrides that volume with a host volume
* after that project-folder is moved and re-upped
* the overridden volume's host path will still point to the previous path in the host fs
* while host-volumes that are only defined in docker-compose.yml are bound to the new project-folder


To see this behaviour start from this image that define `VOLUME /data`:

~~~
redis:
  image: redis:2.8.20
~~~

The container will be mounted:

~~~
    "Mounts": [
        {
            "Source": "/mnt/sda1/var/lib/docker/volumes/0b058454c02a4c75bc00e6ed72dedc375ed7be045d580c026d55a19df3007062/_data",
            "Destination": "/data",
            "Mode": "rw",
            "RW": true
        }
    ],
~~~

If you add a volume to the docker-compose file and then `docker-compose stop` and `docker-compose up`

~~~
redis:
  image: redis:2.8.20
  volumes:
    - .:/data
~~~


Now when you run docker-compose up you will get a warning:

WARNING: Service "redis" is using volume "/data" from the previous container. Host mapping "/private/tmp/prova_compose" has no effect. Remove the existing containers (with `docker-compose rm redis`) to use the host volume mapping.

That's why docker-compose is consevative and don't try to remove an existing volume from an existing container.

If you `docker-compose rm` and `docker-compose up` the existing container is removed and compose will create a new one which respect the configuration:

~~~
    "Mounts": [
        {
            "Source": "/private/tmp/prova_compose",
            "Destination": "/data",
            "Mode": "rw",
            "RW": true
        }
    ],
~~~

## Networking in Compose and Service discovery

https://docs.docker.com/compose/networking/

By default Compose sets up a single network for your app:

* Each container for a service joins the default network
* is reachable by other containers on that network,
* and discoverable by them at a hostname identical to the container name.

Note: Your app’s network is given a name based on the “project name”, which is based on the name of the directory it lives in.

NORE: links are required only if you want to create an alias https://docs.docker.com/compose/networking/#links

## docker-compose file reference

V2: https://docs.docker.com/compose/compose-file/compose-file-v2/

Volumes:

* For version 2 files, named volumes need to be specified with the top-level volumes key. When using version 1, the Docker Engine will create the named volume automatically if it doesn’t exist.

### Volumes

https://docs.docker.com/compose/compose-file/compose-file-v2/#/volume-configuration-reference

While it is possible to declare volumes on the fly as part of the service declaration, this section allows you to create named volumes that can be reused across multiple services (without relying on volumes_from), and are easily retrieved and inspected using the docker command line or API. See the [docker volume](https://docs.docker.com/engine/reference/commandline/volume_create/) subcommand documentation for more information.


### PORTS

* `ports` to expose ports to the host container

It's very similar to the docker commandline option `-p`

### LINKS

WARNING:

* The --link flag is a deprecated legacy feature of Docker. We recommend that you use user-defined networks and the embedded DNS server [ref](https://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/)
 One feature that user-defined networks do not support that you can do with --link is sharing environmental variables between containers. However, you can use other mechanisms such as volumes to share environment variables between containers in a more controlled way.

`links`

[Docker compose doc](https://docs.docker.com/compose/yml/#links)

## Open Issues

### 2 docker-compose.yml, same directory name - causes 'mixing' of services

Ref:

* GITHUB ISSUE 2 docker-compose.yml, same directory name - causes 'mixing' of services: https://github.com/docker/compose/issues/2120
* COMPOSE_PROJECT_NAME env variable: https://docs.docker.com/compose/reference/overview/#compose-project-name
* Proposal: make project-name persistent. https://github.com/docker/compose/issues/745


## FAQ

* every time you do a docker-compose run, Compose is spinning up entirely new containers for your code but only if the containers are not up already, in which case they are linked to that (running) container.This means that it’s possible that you’ve spun up multiple instances of your app without thinking about it – for example, you may have a web and db container already up from a docker-compose up command, and then in a separate terminal window you run a docker-compose run web rails c. That spins up another web container to execute the command, but then links that container with the pre-launched db container.

## Example

Ref V2 file, docker 1.12: https://www.linux.com/learn/introduction-docker-compose-tool-multi-container-applications

```
version: '2'
services:
 mysql:  
  image: mysql
  container_name: mysql
  ports:
   - "3306"
  environment:
   - MYSQL_ROOT_PASSWORD=root
   - MYSQL_DATABASE=ghost
   - MYSQL_USER=ghost
   - MYSQL_PASSWORD=password
 ghost:  
  build: ./ghost
  container_name: ghost
  depends_on:
    - mysql
  ports:
    - "80:2368"
```

This would be the equivalent of running the following `docker run` commands:

```
$ docker run -d --name mysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=ghost -e MYSQL_PASSWORD=password -e MYSQL_USER=ghost -p 3306 mysql
$ docker build -t myghost .
$ docker run -d --name ghost -p 80:2368 myghost
```

## Variable substitution

[https://docs.docker.com/compose/compose-file/compose-file-v3/\#variable-substitution](https://docs.docker.com/compose/compose-file/compose-file-v3/#variable-substitution)

Your configuration options can contain environment variables. Compose uses the variable values from the shell environment in which `docker compose` is run. For example, suppose the shell contains `POSTGRES_VERSION=9.3` and you supply this configuration:

```yaml
db:
 image: "postgres:${POSTGRES_VERSION}"
```

When you run `docker compose up` with this configuration, Compose looks for the `POSTGRES_VERSION` environment variable in the shell and substitutes its value in. For this example, Compose resolves the `image` to `postgres:9.3` before running the configuration if the shell has the `POSTGRES_VERSION` environment variable set to `9.3`.

If an environment variable is not set, Compose substitutes with an empty string. In the example above, if `POSTGRES_VERSION` is not set, the value for the `image` option is `postgres:`.

To fully understand how variable substitution can be applied in real cases, see [Docker Compose Environment Variables](https://docs.docker.com/compose/compose-file/compose-file-v3/#variable-substitution) for a deep dive into how env and arg variables work and can be used to achieve more complex configurations.

Both `$VARIABLE` and `${VARIABLE}` syntax are supported. Additionally when using the [2.1 file format](https://docs.docker.com/compose/compose-file/compose-versioning/#version-21), it is possible to provide inline default values using typical shell syntax:

* `${VARIABLE:-default}` evaluates to `default` if `VARIABLE` is **unset** or **empty** in the environment.  
* `${VARIABLE-default}` evaluates to `default` only if `VARIABLE` is **unset** in the environment.

Similarly, the following syntax allows you to specify **mandatory variables**:

* `${VARIABLE:?err}` exits with an error message containing `err` if `VARIABLE` is unset or empty in the environment.  
* `${VARIABLE?err}` exits with an error message containing `err` if `VARIABLE` is unset in the environment.

## Config subcommand: Verify Override and Anchor extension

Use the config subcommand to "compile" the final docker-compose file:  
`docker-compose -f base.yaml -f vol1.yaml -f vol2.yaml config`

See example here [https://stackoverflow.com/a/61178760](https://stackoverflow.com/a/61178760) 

## Yaml Anchor and Extension fields

YAML anchors and aliases provide a way to reuse configurations across different services in a `docker-compose.yml` file. This approach helps to reduce duplication and maintain a cleaner, more manageable configuration file, especially when you have multiple services with similar settings.

### Anchor Definition (`&`):

* An anchor, denoted by `&`, is used to create a named reference to a configuration block. You define an anchor by placing `&anchor_name` before the configuration you want to reuse, for example:

```yaml
x-defaults: &defaults
  restart: always
  environment:
    - ENV_VAR=example
```

### Alias Usage (`*`)

An alias, indicated by `*`, is used to insert the anchored configuration into another service.  By placing `<<: *anchor_name` in a service definition, Docker Compose merges the anchored configuration into that service.  Example:

```yaml
x-defaults: &defaults
  restart: always
  environment:
    - ENV_VAR=example

service1:
  <<: *defaults
  image: service1:latest
```

### Benefits of using anchors and aliases in Docker Compose:  
* **Reduce Redundancy**: Anchors and aliases eliminate the need to repeat common configurations across multiple services, making the file shorter and more readable.  
* **Ease of Maintenance**: Changes to the common configuration can be made in one place, automatically applying to all services using the anchor.  
* **Flexibility**: Specific configurations in each service can still override the shared settings from the anchor, allowing for customization alongside reuse.

A common example is to define a base service and then reuse that configuration in other services like workers.

```yaml
worker:
  <<: *worker
  command: ./bin/docker-worker-celery --with-scheduler
  restart: on-failure
  environment:
    DISABLE_SECURE_SSL_REDIRECT: 'true'
    IS_BEHIND_PROXY: 'true'
    DATABASE_URL: 'postgres://posthog:posthog@db:5432/posthog'
    CLICKHOUSE_HOST: 'clickhouse'
    CLICKHOUSE_DATABASE: 'posthog'
    CLICKHOUSE_SECURE: 'false'
    CLICKHOUSE_VERIFY: 'false'
    KAFKA_HOSTS: 'kafka'
    REDIS_URL: 'redis://redis:6379/'
    PGHOST: db
    PGUSER: posthog
    PGPASSWORD: posthog
    DEPLOYMENT: hobby
```

This approach is particularly useful for services that share a lot of common configuration but have slight differences. It makes the Docker Compose file more maintainable and easier to read by reducing duplication.

### Extension Fields: "x-"

Added in [version 3.4](https://docs.docker.com/compose/compose-file/compose-versioning/#version-34) file format.

It is possible to re-use configuration fragments using extension fields. Those special fields can be of any format as long as they are located at the root of your Compose file and their name start with the `x-` character sequence.

Note

Starting with the 3.7 format (for the 3.x series) and 2.4 format (for the 2.x series), extension fields are also allowed at the root of service, volume, network, config and secret definitions.

```yaml
version: "3.8"
x-custom:
  items:
    - a
    - b
  options:
    max-size: '12m'
  name: "custom"
```

The contents of those fields are ignored by Compose, but they can be inserted in your resource definitions using [YAML anchors](https://yaml.org/spec/1.2/spec.html#id2765878). For example, if you want several of your services to use the same logging configuration:

```yaml
logging:
  options:
    max-size: '12m'
    max-file: '5'
  driver: json-file
```

You may write your Compose file as follows:

```yaml
version: "3.8"
x-logging:
  &default-logging
  options:
    max-size: '12m'
    max-file: '5'
  driver: json-file
services:
  web:
    image: myapp/web:latest
    logging: *default-logging
  db:
    image: mysql:latest
    logging: *default-logging
```

It is also possible to partially override values in extension fields using the [YAML merge type](https://yaml.org/type/merge.html)

```yaml
version: "3.8"
x-volumes:
  &default-volume
  driver: foobar-storage
services:
  web:
    image: myapp/web:latest
    volumes: ["vol1", "vol2", "vol3"]
volumes:
  vol1: *default-volume
  vol2:
    << : *default-volume
    name: volume02
  vol3:
    << : *default-volume
    driver: default
    name: volume-local
```

## Secrets 

### Sops \+ secret key

Ref: 

* [https://beaglesecurity.com/blog/article/secrets-in-docker.html](https://beaglesecurity.com/blog/article/secrets-in-docker.html)  
* secrets configuration reference ⇒ [Compose file version 3 reference | Docker Docs](https://docs.docker.com/compose/compose-file/compose-file-v3/#secrets-configuration-reference) 