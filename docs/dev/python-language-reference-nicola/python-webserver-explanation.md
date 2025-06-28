# WebServer

## How to choose a webserver for a Python app

Short answer: 
- for basic apps use and/or if you don't have a highly skilled team use  **Nginx \+ Gunicorn** ( Ref: [Which WSGI server should I use?. Gunicorn, uWSGI, or mod\_wsgi?](https://medium.com/django-deployment/which-wsgi-server-should-i-use-a70548da6a83)  by Django Deployment \- [Antonis Christofides](https://aptiko.medium.com/)). 
- Otherwise if you have time and skills to optimize your deploy you can evaluate other option (see the next section)

More in details these are the main points:

* Gunicorn will server http and can be used with a really well known nginx proxy configuration  (`nginx + proxy_pass`)   
* Other alternatives like uWSGI have many features that already exist in nginx or other parts of the stack, thus they are rarely needed but complicate the configuration and the documentation.   
* Gunicorn, on the other hand, does exactly what you want and no more. It is simple and works fine. So I recommend it unless in your particular case there is a compelling reason to use one of the others.  
* **Nginx** as a reverse proxy in front of Gunicorn or uWSGI is a common and recommended practice in deploying Django applications. This setup offers several benefits:
  * Great performance with **static files and Media Files**: Handling of Static and Media Files: Django is not optimized for serving static files (like CSS, JavaScript, and images), so Nginx can handle these efficiently. This offloads work from Gunicorn/uWSGI, allowing them to focus on running Python code.
  * Security: Nginx can act as a security layer, managing SSL/TLS termination and protecting against DDoS attacks and other common web threats.
  * **Load Balancing**: Nginx can distribute traffic across multiple instances of your application, improving load handling and redundancy.
  * **Caching**: It can cache content, reducing the load on your application servers and speeding up response times for your users.
  * **Better Handling of HTTP Requests**: Nginx can manage slow client network connections, freeing up application server resources.
* **Flexibility and Scalability**: This setup is scalable and can be adjusted as your application grows and your needs change.



### Another simple alternative: uwsgi with basic configuration

The reality is that if you avoid complex configuration also `uwsgi` is as simple as `gunicorn`.

The only thing you have to change to route requests to **gunicorn**:

```
location / {
    proxy_pass http://127.0.0.1:8000;
}
```

and to **uwsgi**:

```
location / {
    uwsgi_pass 127.0.0.1:8001;
}
```

### Intro to Advanced Configuration

Choosing the right web server and configuration is a quite complex task that require a lot of knowledge of the whole stack.  Read post like these to start understanding the topic:

* [https://blog.miguelgrinberg.com/post/ignore-all-web-performance-benchmarks-including-this-one](https://blog.miguelgrinberg.com/post/ignore-all-web-performance-benchmarks-including-this-one)  
* [https://ivan-site.com/2012/09/benchmark-uwsgi-vs-gunicorn-for-async-workers/](https://ivan-site.com/2012/09/benchmark-uwsgi-vs-gunicorn-for-async-workers/)

In these section we don't delve into details (for now :) ). Just keep in mind that details matter. Just to mention some example:

* the DB pooler can heavily change the results  
* Async/sync code performs very differently.  A request that involve a lot of I/O can perform well with asynchronous solution but the inverse could be true if the request is CPU intensive.

## Python Web Server Interfaces: WSGI and ASGI

In Python web development, two primary server interfaces facilitate communication between web servers and applications: 
- **WSGI** (Web Server Gateway Interface)
- **ASGI** (Asynchronous Server Gateway Interface)

WSGI, introduced in the early 2000s, standardizes the interaction between web servers and synchronous Python applications, ensuring compatibility across various frameworks and servers. However, with the advent of real-time web features and the need for handling numerous simultaneous connections, ASGI emerged as an evolution of WSGI. 

ASGI supports both synchronous and asynchronous applications, enabling efficient management of long-lived connections like WebSockets and enhancing performance in high-concurrency scenarios. Understanding the distinctions between WSGI and ASGI is crucial for developers aiming to build scalable and responsive web applications in Python.


### WSGI

WSGI, which stands for **Web Server Gateway Interface**, is a specification in Python that describes a standard interface between web servers and Python web applications or frameworks. It's a protocol that allows a web server to communicate with a web application written in Python. 

PEP 3333 describes the interface that a Python web application should implement to be compatible with a WSGI (Web Server Gateway Interface) web server. This specification defines how the web server communicates with the web application, essentially acting as a contract between the server and the application.

The main purpose of WSGI is to facilitate a standard way for Python applications to work with web servers, making it easier to develop and deploy web applications in Python.

The WSGI (Web Server Gateway Interface) specification is documented in PEP 3333 ([https://peps.python.org/pep-3333/](https://peps.python.org/pep-3333/)), it  includes examples of how to implement WSGI applications and servers, as well as the rationale behind certain decisions in the specification.

In more detail:

* **Application Interface**: PEP 3333 specifies that a Python web application must provide a callable object (such as a function, method, or an instance of a class) that the server will use to pass requests to the application and receive responses from it. This callable takes two arguments:
  1. the `environment` (a dictionary containing HTTP request information and WSGI-specific variables) and 
  2. a `start_response` function (used to begin the HTTP response). 

* **Server Responsibilities**: The PEP also outlines the responsibilities of the web server when interfacing with the application. This includes passing the correct environment variables, handling the HTTP requests and responses appropriately, and managing the lifecycle of the application.  

* Middleware Support: PEP 3333 enables the use of middleware components that sit between the server and application, capable of processing requests and responses as they pass through. Middleware components themselves conform to the WSGI interface, allowing them to be stacked or chained.

* **Compatibility and Flexibility**: The interface defined in PEP 3333 ensures that any WSGI-compliant web application can be run with any WSGI-compliant server, providing great flexibility and compatibility for Python web development.

PEP 3333 thus plays a crucial role in the Python web ecosystem, providing a standard that has enabled the growth and interoperability of numerous web frameworks and servers. This standardization is key to the wide-ranging compatibility seen in Python web applications and servers today.

#### Django WSGI

Official Doc: [https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/)

Django’s primary deployment platform is [WSGI](https://wsgi.readthedocs.io/en/latest/), the Python standard for web servers and applications.

When you create a new Django project with the [**startproject**](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-startproject) command, it will sets up a minimal default WSGI configuration for you by creating a `project_name/wsgi.py` file, which you can tweak as needed for your project:

```python
# project_name/wsgi.py
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings')
application = get_wsgi_application()
```

This file is used both by Django’s development server and in production WSGI deployments. Basicly you need to tell to your service to use the `application` callable in `project_name/wsgi.py`.

* PROD: WSGI servers obtain the path to the **application** callable from their configuration. For example uwsgi will use the `module` option to specify the path to the application callable: `module = project_name.wsgi:application`
* DEV: Django’s built-in server, namely the [**runserver**](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-runserver) command, reads it from the [WSGI_APPLICATION](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-WSGI_APPLICATION) setting. By default, it’s set to `project_name.wsgi.application`.

When the WSGI server loads your application, Django needs also to import the settings module — that’s where your entire application configuration is defined. Django uses the [DJANGO_SETTINGS_MODULE](https://docs.djangoproject.com/en/5.0/topics/settings/#envvar-DJANGO_SETTINGS_MODULE) environment variable to locate the appropriate settings module.

#### Custom WSGI web server Implementation Example [ADVANCED]

If you want to delve into the details of WSGI implementation:

* [https://betterprogramming.pub/writing-your-own-http-server-implementing-wsgi-97706588ac20](https://betterprogramming.pub/writing-your-own-http-server-implementing-wsgi-97706588ac20)

### ASGI



## Python Web Servers

### uWSGI

In the following section we will see how to configure uWSGI to serve a Django application in production using sane defaults that we use in Addictive.

For a complete reference see the [uWSGI Documentation](https://uwsgi-docs.readthedocs.io/en/latest/).

#### How to use env variable in an uWSGI ini file

Once the environment variable is set, uWSGI can access it directly. In your .ini file, you can reference this variable for any configuration setting. For example, in a Unix/Linux shell, you can export the variable:

```bash
export DJANGO_APP_NAME=myapp
```

To access the Variable in uWSGI:

```ini
[uwsgi]
module = $(APP_DJANGO_PROJECT_PACKAGE).wsgi:application
http-socket = :8000
env = DJANGO_SETTINGS_MODULE=$(APP_DJANGO_PROJECT_PACKAGE).settings
```

#### HOWTO Deploy Django with docker, nginx and uwsgi

Deploy Django with docker, nginx and uwsgi is a common way to deploy Django applications in production.

This is a basic example of how to configure uwsgi to serve a Django application in production using sane defaults that we use in Addictive.

In this setup:
- uwsgi serve the django application
- nginx is used as a reverse proxy to serve media and static files
- docker is used to containerize the application and the web server

Ref:

* See the section "uwsgi" and "Static and Media file" [https://github.com/addictivedev/ad-internals-poetry-docker-django](https://github.com/addictivedev/ad-internals-poetry-docker-django) for a reference example about usign nginx to serve media and static files.  
*  [https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django\_and\_nginx.html](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)

1. Install the **uwsgi** python package  
2. configure uwsgi

Uwsgi can be configured from command line or using an ini file, both are equivalent, at Addictive we prefer using ini file

At Addictive we usually deploy our services using docker containers and we populate the environment, this is a basic ***uwsgi.ini*** file that reads it's config from env variables:

```ini
[uwsgi]

# `chdir` changes the current working directory of the uWSGI process to the specified directory before loading the application.
# This is useful when your application needs to be executed in a specific directory context (for instance, if it accesses files using relative paths)
# Typically is the root of your repository
chdir = $(APP_DIR)

# the module configuration option is used to specify the WSGI callable that should be loaded and run by the uWSGI server.
# Format: The module option typically takes the form module_name:callable, where module_name is the Python module
# (e.g., a Python file without the .py extension), and callable is the name of the callable object within that module (often app or application).
# NOTE: mydjangoapp.wsgi uses the python syntax for module, the path is mydjangoapp/wsgi.py
module = $(APP_DJANGO_PROJECT_PACKAGE).wsgi:application

# The home option in uWSGI is used to set the Python virtual environment for your application. Our docker image doesn't use virtual env.
# home = /home/django/.virtualenvs/myenv

# a "plugin" refers to a modular component that extends the functionality of the uWSGI server.
plugin = python38

# NOTE: mydjangoapp.wsgi uses the python syntax for module, the path is mydjangoapp/wsgi.py

module = $(APP_DJANGO_PROJECT_PACKAGE).wsgi:application

# The home option in uWSGI is used to set the Python virtual environment for your application. Our docker image doesn't use virtual env.
# home = /home/django/.virtualenvs/myenv

# a "plugin" refers to a modular component that extends the functionality of the uWSGI server.
plugin = python38

# When master is set to 1 (or true), uWSGI runs a master process in addition to worker processes.
# The master process manages the worker processes, handling tasks like reloading, re-spawning, and load balancing.
# It's generally recommended to enable the master process for production deployments because it provides more control and robustness.
master = 1

# `processes` specifies how many worker processes uWSGI should spawn. Each worker process handles requests independently.
processes = 2

# `thread` defines how many threads each worker process should use.
thread = 3

pidfile=/tmp/project-master.pid

vacuum=True

max-requests=5000

#daemonize=/var/log/uwsgi/yourproject.log

#check-static=/app//public

uid = $(APP_UID)

gid = $(APP_GID)

chmod-socket = 666

# Setting file in the python import syntax, path is %(APP_DJANGO_PROJECT_PACKAGE)/%(APP_DJANGO_PROJECT_PACKAGE)/server.py
env = DJANGO_SETTINGS_MODULE=$(APP_DJANGO_PROJECT_PACKAGE).$(APP_DJANGO_PROJECT_PACKAGE).settings

# PYTHONPATH specifies additional directories where Python should look for modules and packages.
env = PYTHONPATH=YOURPATH:$PYTHONPATH

env = LANG=en_US.utf8

env = LC_ALL=en_US.UTF-8

env = LC_LANG=en_US.UTF-8

env = PYTHONIOENCODING=UTF-8

# lazy-apps
# by default, uWSGI runs in a mode where Python's Global Interpreter Lock (GIL) is not released,
# effectively disabling the ability of Python threads to run in parallel. It was enabled in the Irideos original config.

#enable-threads = true

# When you specify one or more files with touch-chain-reload, uWSGI monitors these files for modifications.
# If any of these files are 'touched' (i.e., their modification timestamps are updated), uWSGI will gracefully reload the application.
touch-chain-reload = /app/mydjangoapp/mydjangoapp/wsgi.py

# `vacuum` is used to ensure that all of the resources allocated by the server during its startup are cleaned up and released when it shuts down.
# This includes removing socket files, pidfiles, and other temporary files that uWSGI might have created during its operation.
vacuum = true

# `max-requests` controls the maximum number of requests a worker will process before being recycled (restarted).
max-requests = 200

# The harakiri option sets a timeout (in seconds) for requests.
# If a request takes longer than the specified time, the harakiri mode is triggered, and the worker processing that request will be killed and restarted.
harakiri = 120

# The chmod-socket option is particularly relevant when using Unix sockets (as opposed to TCP sockets).
# The 666 permission setting allows for read and write permissions for everyone. This needs to be set appropriately based on your security requirements.
# In many cases, a more restrictive setting like 660 might be preferable.
chmod-socket = 666

# The buffer-size option sets the size of the buffer uWSGI uses for each request.
# This is the maximum size of the headers your application can receive.
# If your application is expected to receive requests with large headers (like big cookies or tokens), you might need to increase this value.
# The size is specified in bytes, so 8192 means 8 KB.
buffer-size=8192

# The chmod-socket option is particularly relevant when using Unix sockets (as opposed to TCP sockets).
# The 666 permission setting allows for read and write permissions for everyone. This needs to be set appropriately based on your security requirements.
# In many cases, a more restrictive setting like 660 might be preferable.
chmod-socket = 666

# The `buffer-size` option sets the size of the buffer uWSGI uses for each request.
# This is the maximum size of the headers your application can receive.
# If your application is expected to receive requests with large headers (like big cookies or tokens), you might need to increase this value.
# The size is specified in bytes, so 8192 means 8 KB.
buffer-size=8192

## Clean write error (client close) ##

# This is the maximum size of the headers your application can receive.
# If your application is expected to receive requests with large headers (like big cookies or tokens), you might need to increase this value.
# The size is specified in bytes, so 8192 means 8 KB.
buffer-size=8192

## Clean write error (client close) ##

# `ignore-sigpipe = true` tells uWSGI to ignore SIGPIPE errors.
# A SIGPIPE error occurs when uWSGI tries to write to a socket that has been closed by the client.
# This can happen, for example, if a client disconnects unexpectedly.
# Ignoring SIGPIPE helps in keeping the uWSGI server stable in face of such client-side interruptions.
ignore-sigpipe = true

# `ignore-write-errors = true` Similar to ignore-sigpipe, this setting helps in handling cases where the client has closed the connection, and uWSGI attempts to write data to that connection.
ignore-write-errors = true

# `memory-report = true` enables the uWSGI stats server and specifies the Unix socket through which these stats can be accessed.
# Tools and monitoring systems can use this socket to fetch real-time metrics about the uWSGI server's performance and health.
memory-report = true

# `stats = /run/uwsgi/app/app/stat.sock` enables the uWSGI stats server and specifies the Unix socket through which these stats can be accessed.
# Tools and monitoring systems can use this socket to fetch real-time metrics about the uWSGI server's performance and health.
stats = /run/uwsgi/app/app/stat.sock

# `socket = /run/uwsgi/app/uwsgi.sock` enables the uWSGI stats server and specifies the Unix socket through which these stats can be accessed.
# Tools and monitoring systems can use this socket to fetch real-time metrics about the uWSGI server's performance and health.
socket = /run/uwsgi/app/uwsgi.sock

# `ignore-write-errors = true` Similar to ignore-sigpipe, this setting helps in handling cases where the client has closed the connection, and uWSGI attempts to write data to that connection.
ignore-write-errors = true

# `disable-write-exception = true`  By default, uWSGI raises exceptions when it encounters an error while sending data to a client. This option disables that behavior, which can be useful in ensuring that worker processes don't get terminated due to client-side issues.
disable-write-exception = true

# `stats = /run/uwsgi/app/app/stat.sock` enables the uWSGI stats server and specifies the Unix socket through which these stats can be accessed.
# Tools and monitoring systems can use this socket to fetch real-time metrics about the uWSGI server's performance and health.
stats = /run/uwsgi/app/app/stat.sock

# `socket = /run/uwsgi/app/uwsgi.sock` enables the uWSGI stats server and specifies the Unix socket through which these stats can be accessed.
# Tools and monitoring systems can use this socket to fetch real-time metrics about the uWSGI server's performance and health.
socket = /run/uwsgi/app/uwsgi.sock

`ignore-write-errors = true`

# disable-write-exception = true`  By default, uWSGI raises exceptions when it encounters an error while sending data to a client. This option disables that behavior, which can be useful in ensuring that worker processes don't get terminated due to client-side issues.

disable-write-exception = true

# Stats endpoint for monitoring
# When this option is enabled, uWSGI includes memory usage information in its logs and reports.
# This is valuable for monitoring and debugging, as it helps in understanding the memory footprint of your application.
memory-report = true

# `stats = /run/uwsgi/app/app/stat.sock` enables the uWSGI stats server and specifies the Unix socket through which these stats can be accessed.
# Tools and monitoring systems can use this socket to fetch real-time metrics about the uWSGI server's performance and health.
stats = /run/uwsgi/app/app/stat.sock

# Unix socket configuration
# When using Unix sockets, ensure that the permissions and ownership of the socket file allow the web server (e.g., Nginx or Apache) to communicate with uWSGI.
# The choice between TCP/IP and Unix sockets depends on your architecture and preferences.
# Unix sockets are generally faster and more secure as they don't involve network stack and are accessible only on the local machine.
stats = /run/uwsgi/app/app/stat.sock


`# Unix sockets are generally faster and more secure as they don't involve network stack and are accessible only on the local machine.`

`socket = /run/uwsgi/app/uwsgi.sock`


3. Configure nginx

```nginx
# mysite_nginx.conf
# the upstream component nginx needs to connect to
upstream django 
{
    server unix:///path/to/your/mysite/mysite.sock; # for a file socket
    server 127.0.0.1:8001; # for a web port socket (we'll use this first)
}

# configuration of the server
server {
    # the port your site will be served on
    listen      8000;
    # the domain name it will serve for
    server_name example.com; # substitute your machine's IP address or FQDN
    charset     utf-8;

    # max upload size
    client_max_body_size 75M;   # adjust to taste

    # Django media
    location /media  {
        alias /path/to/your/mysite/media;  # your Django project's media files - amend as required
    }
```

This conf file tells nginx to serve up media and static files from the filesystem, as well as handle requests that require Django’s intervention. 

4. Deploy static files

Before running nginx, you have to collect all Django static files in the static folder. First of all you have to edit mysite/settings.py adding:

STATIC\_ROOT \= os.path.join(BASE\_DIR, "static/")

and then run

python manage.py collectstatic

​​