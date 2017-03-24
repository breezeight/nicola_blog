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

## NGINX

SEE google drive https://docs.google.com/document/d/1HHwCwIMdyZoMuUfOJizxA3mjASdNJK07LEtjMu5oUfY/edit#



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

