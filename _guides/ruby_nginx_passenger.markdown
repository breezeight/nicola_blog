---
layout: post
title: "Ruby: Testing webservices"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["ruby", "nginx"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# References


# Nginx

Nginx is a reverse proxy first and HTTP server second!

How To install: http://wiki.nginx.org/GettingStarted
How to configure: http://blog.martinfjordvald.com/2010/07/nginx-primer/


Misc:

* http://jeroenbourgois.be/nginx-alongside-apache-on-osx-snow-leopard/
* http://phrogz.net/nginx-as-reverse-proxy-cache-for-thin

## Configuration

understanding-the-nginx-configuration-inheritance-model
nginx configuration file is an inheriting-hierarchy  

There are 6 possible contexts in nginx, here in top to bottom order:

* Global.
* Http.
* Server.
* If.
* Location.
  * Nested Location.
  * If in location.
  * limit_except.


Directives :

* server_name : instruct nginx to use this server block when the HOST header matches the value
* root : defines what to use as root when looking for files.

## Tuning

http://blog.martinfjordvald.com/2011/04/optimizing-nginx-for-high-traffic-loads/


## Scripting with MRuby

https://github.com/matsumoto-r/ngx_mruby/wiki/Class-and-Method
https://github.com/matsumoto-r/ngx_mruby/wiki/Use-Case


# Nginx + Ruby 

## Passenger + Nginx

https://www.phusionpassenger.com/documentation/Users%20guide%20Nginx.html



## Unicorn + Passenger

Hello world tutorial Nginx + Unicorn
http://velenux.wordpress.com/2012/01/10/running-sinatra-and-other-rack-apps-on-nginx-unicorn/


Common issues with Unicorn

502 bad gateway
http://stackoverflow.com/questions/9951134/unicorn-request-queuing
http://robert-reiz.com/2012/04/23/bad-gateway-with-nginx-unicorn/

