---
layout: post
title: "Ruby: NGINX and Passenger configuration"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["ruby", "nginx"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# References

* [Passenger Library](https://www.phusionpassenger.com/library/) : a comprehensive online resource about Ruby, Python and Node.js deployment, administration, scaling, high availability and more 

# Nginx

Nginx is a reverse proxy first and HTTP server second!

How To install: http://wiki.nginx.org/GettingStarted
How to configure: http://blog.martinfjordvald.com/2010/07/nginx-primer/


Misc:

* http://jeroenbourgois.be/nginx-alongside-apache-on-osx-snow-leopard/
* http://phrogz.net/nginx-as-reverse-proxy-cache-for-thin

## Configuration

Refs: 

* Nginx Intro: http://nginx.org/en/docs/beginners_guide.html
* Intro by DigitalOcean: https://www.digitalocean.com/community/tutorials/understanding-the-nginx-configuration-file-structure-and-configuration-contexts
* Reference of Nginx directives: http://nginx.org/en/docs/dirindex.html

* The configuration file is made of directives
* Context: directives with `{ ... }` blocks are contexts (server, http, etc). `main` is the the default context
* the main configuration file is that it appears to be organized in a tree-like structure, defined by nested directives.
* `#` for comments


By default, the configuration file is named `nginx.conf` (usually in /usr/local/nginx/conf, /etc/nginx, or /usr/local/etc/nginx)

nginx configuration file is an inheriting-hierarchy:

* if a directive is valid in multiple nested scopes, a declaration in a broader context will be passed on to any child contexts as default values.
* The children contexts can override these values at will. 




There are the possible contexts in nginx. This is list of the most common:

* `Global` : represents the broadest environment for Nginx configuration. It is used to configure details that affect the entire application on a basic level. While the directives in this section affect the lower contexts, many of these aren't inherited because they cannot be overridden in lower levels.
  * user and group to run the worker processes as
  * the number of workers
  * the file to save the main process's PID.
  * You can even define things like worker CPU affinity and the "niceness" of worker processes.
  * The default error file for the entire application can be set at this level (this can be overridden in more specific contexts).
  * ...

* `Http `: When configuring Nginx as a web server or reverse proxy, the "http" context will hold the majority of the configuration.
  * directives at this level control the defaults for every virtual server defined within.
  * configure compression (gzip and gzip_disable),
  * fine-tune the TCP keep alive settings (keepalive_disable, keepalive_requests, and keepalive_timeout),
  * the rules that Nginx will follow to try to optimize packets and system calls (sendfile, tcp_nodelay, and tcp_nopush). 


* `Events` : Nginx uses an event-based connection processing model, so the directives defined within this context determine how worker processes should handle connections
  * There can only be a single events context defined within the Nginx configuration.
  * select the connection processing technique to use, or to modify the way these methods are implemented. Usually, the connection processing method is automatically selected based on the most efficient choice that the platform has available. 
  * number of connections each worker can handle

* Server `http` : 
  * allows for multiple declarations, each of which can handle a specific subset of connections.
  * The directives in this context can override many of the directives that may be defined in the http context, including logging, the document root, compression, etc.
  * `listen`: The ip address / port combination that this server block is designed to respond to. If a request is made by a client that matches these values, this block will potentially be selected to handle the connection.
  * `server_name` : If there are multiple server blocks with listen directives of the same specificity that can handle the request, Nginx will parse the `Host` header of the request and match it against this directive.
  * `root` : defines what to use as root when looking for files.
  * configure files to try to respond to requests (try_files),
  * issue redirects and rewrites (return and rewrite)
  * and set arbitrary variables (set).

* If.
  * TODO

* `Location` : Location contexts share many relational qualities with server contexts
  * used to handle a certain type of client request, and each location is selected by virtue of matching the location definition against the client request through a selection algorithm.
  * location blocks further divide up the request handling within a server block by looking at the request URI.
  * Location blocks live within server contexts and, unlike server blocks, can be nested inside one another. 
  * Nested Location.
  * If in location.
  * limit_except.

~~~
server {
    # server context
    location /match/criteria {
        # first location context
    }
    location /other/criteria {
        # second location context
        location nested_match {
            # first nested location
        }
        location other_nested {
            # second nested location
        }
    }
}
~~~


* `upstream` : this context defines a named pool of servers that Nginx can then proxy requests to.

~~~
http {
    # http context
    upstream upstream_name {
        # upstream context
        server proxy_server1;
        server proxy_server2;
        . . .
    }

    server {
        # server context
    }
}
~~~




## Requests Life cycle

Client request will be handled according to the configuration defined in a single server context, so Nginx must decide which server context is most appropriate based on details of the request. 

## Monitoring

Monitoring an Nginx server

* http://tribily.com/node/157
* Loggly: https://www.loggly.com/docs/nginx-server-logs/ 

## Tuning

http://blog.martinfjordvald.com/2011/04/optimizing-nginx-for-high-traffic-loads/


## Scripting with MRuby

https://github.com/matsumoto-r/ngx_mruby/wiki/Class-and-Method
https://github.com/matsumoto-r/ngx_mruby/wiki/Use-Case


# Passenger 

## Integration Mode 

* Explanation of passenger integration modes: https://www.phusionpassenger.com/library/indepth/integration_modes.html:
  * standalone
  * with nginx
  * with apache
  * What is this? · What are the differences? · Which one should I use?



### Passenger Standalone

Passenger standalone uses the nginx core. Basically it will start an NGINX server to 

See here for an example: http://code.eklund.io/blog/2015/03/17/managing-rewrites-for-a-rails-app-on-heroku-with-nginx-plus-phusion-passenger/

remember to start the server with the ` --nginx-config-template` option, ex: `bundle exec passenger start -p 3000 --max-pool-size 3 --min-instances 2 --nginx-config-template config/nginx.conf.erb`

TIP: to check the compile nginx config:

~~~
ps aux|grep nginx
nginx: master process /Users/nicolabrisotto/.passenger/support-binaries/5.0.15/nginx-1.8.0 -c /var/folders/wm/2yx43zwx1js0404rrzx6pnf40000gn/T/passenger-standalone.e5r602/nginx.conf -p /var/folders/wm/2yx43zwx1js0404rrzx6pnf40000gn/T/passenger-standalone.e5r602

cat  /var/folders/wm/2yx43zwx1js0404rrzx6pnf40000gn/T/passenger-standalone.e5r602/nginx.conf
~~~

### Passenger + Nginx

Viewing overall server status report: https://www.phusionpassenger.com/library/admin/nginx/overall_status_report.html

## Debug Application Startup Problems

https://github.com/phusion/passenger/wiki/Debugging-application-startup-problems


# NGinx + Unicorn 

Hello world tutorial Nginx + Unicorn
http://velenux.wordpress.com/2012/01/10/running-sinatra-and-other-rack-apps-on-nginx-unicorn/


Common issues with Unicorn

502 bad gateway
http://stackoverflow.com/questions/9951134/unicorn-request-queuing
http://robert-reiz.com/2012/04/23/bad-gateway-with-nginx-unicorn/

