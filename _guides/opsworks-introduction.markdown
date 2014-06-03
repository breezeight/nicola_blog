---
layout: post
title: "OpsWorks Introduction"
date: 2014-03-15 14:33:08 +0100
comments: true
categories: 
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

Test:
[Create a vagrant box](/blog/2014/03/15/packer_and_vagrant#create-a-vagrant-box-from-an-ubuntu-image-to-test-opsworks)

# Basic Concepts

Stack:

* The stack is the top-level AWS OpsWorks entity.
* It represents a set of instances that you want to manage collectively.

Layer:

* A layer is essentially a blueprint for an Amazon EC2 instance.
* Every stack has at least one and usually several layers.
* Instances can optionally be a member of multiple layers (but not all
layers are compatible).
* Layers support [Auto Healing](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-autohealing.html) of instances 

App:

* Some of AWS OpsWorks's layers support application servers.
* An AWS OpsWorks app represents code that you want to run on an application server.


# CloudFormation support for OpsWorks


OpsWorks Example:
https://s3.amazonaws.com/cloudformation-templates-us-east-1/OpsWorks.template

[Issue Berkshelf not supported, need manual activation](https://forums.aws.amazon.com/thread.jspa?messageID=544082)

# AWS OpsWorks CLI and API

Describe stacks:

~~~ bash
aws opsworks describe-stacks --region us-east-1
~~~


* Deploy http://docs.aws.amazon.com/opsworks/latest/APIReference/API_CreateDeployment.html



# Layer Customization
http://docs.aws.amazon.com/opsworks/latest/userguide/attributes.html
[HowTo](http://docs.aws.amazon.com/opsworks/latest/userguide/create-custom-deploy.html) app on a custom layer.

[AWS OpsWorks Under the Hood (DMG304) | AWS re:Invent 2013](https://www.youtube.com/watch?v=913oT6xV-Qk)

## Manage a git repo with custom cookbook

To manage cookbooks and their dependencies we use berkshelf via Thor
tasks. See the [addictive-cookbook](https://bitbucket.org/fungostudios/addictive-cookbook) as a good starting point.

To overwrite templates with used the second strategy from this [blog](https://sethvargo.com/using-amazon-opsworks-with-berkshelf/),

[this](https://bitbucket.org/fungostudios/addictive-cookbook/commits/3d40a5747d81e407e6123a893988df58c3fd53d3) and [this](https://bitbucket.org/fungostudios/addictive-cookbook/commits/b22c243f4bf9184e65200754f700a27221057be1) commits show how we handle overwritten templates

## Manage a git repo with custom cookbook with chef 11.10 which adds
Berkshelf support to Opsworks

[AWS doc about Berkshelf](http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook-chef11-10.html)

Include a Berksfile file in your cookbook repository's root directory that specifies which cookbooks to install.

* The built-in cookbooks are installed to /opt/aws/opsworks/current/cookbooks.
* If your custom cookbook repository contains cookbooks, they are installed to /opt/aws/opsworks/current/site-cookbooks.
* If you have enabled Berkshelf and your custom cookbook repository contains a Berksfile, the specified cookbooks are installed to /opt/aws/opsworks/current/berkshelf-cookbooks.

This not documented but there is a fourth directory that looks like the
merge of the previous three: /opt/aws/opsworks/current/merged-cookbooks/

## Override default templates
[Opsworks Custom Templates](http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook-template-override.html)

## Custom layer from default Rails Layer

ref: http://www.stefanwrobel.com/heroku-to-opsworks

The Rails Layer will add those recipies to the standard set of recipes:

* setup: unicorn::rails
* configure: rails::configure
* deploy: deploy::rails
* undeploy: deploy::rails-undeploy
* shutdown: nginx::stop

for each rails app of the stack 'unicorn::rails' will create opsworks_deploy_user, opsworks_deploy_dir and the unicorn script in this dir `deploy[:deploy_to]}/shared/scripts/unicorn`



'deploy:default' include the recipe 'dependencies:default'

Ruby:
On every instance, AWS OpsWorks installs a Ruby package for Chef recipes and the instance agent to use. If you add a Rails App Server layer to your stack, AWS OpsWorks installs a separate Ruby package on that layer's instances for the layer's apps to use. The packages are installed in different locations and aren't necessarily the same version. The details depend on which Chef version your stack is using.
http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook-ruby.html

The deploy::rails
opsworks_rails resurce dinamycally include the proper stack: `include_recipe node[:opsworks][:rails_stack][:recipe]`

~~~json
"rails_stack": {
  "name": "nginx_unicorn"
},
~~~

On restart webserver command this the runlist:

~~~json
["opsworks_stack_state_sync", "deploy::rails-restart", "test_suite", "opsworks_cleanup"]
~~~

The [deploy attribute](http://docs.aws.amazon.com/opsworks/latest/userguide/attributes-json-deploy.html)  attribute contains one or more attributes, one for each app that was deployed, named by the app's slug name.
A lot of recipes use the following syntax:

~~~ruby
node[:deploy].each do |application, deploy|
  # application is the slug name
  # deploy is the application hash
end
~~~

We use a custom Unicorn template to close and reopen the Redis connection on fork: `addictive-opsworks-cookbooks/unicorn/templates/default/unicorn.conf.erb `

**DONE** env manage the creation order, IDEA:  symlink_before_migrate( deploy[:symlink_before_migrate] )
Symlink the custom env:
~~~json
  "deploy": {
    "addictive_api": {
      "symlink_before_migrate": {
        "config/env": ".env"
      },
~~~


**TODO** bundle `"auto_bundle_on_deploy": true` on rails app type should
do the magic
~~~json
  "deploy": {
    "addictive_api": {
      "symlink_before_migrate": {
        "config/env": ".env"
      },
      "puma": {
        "logrotate": false
      },
      "auto_bundle_on_deploy": true,
~~~

**Database Adapter** Config
We need to set the database adapter
~~~json
  "deploy": {
    "addictive_api": {
      "symlink_before_migrate": {
        "config/env": ".env"
      },
      "puma": {
        "logrotate": false
      },
      "auto_bundle_on_deploy": true,
      "domains" : ["pippo"],
      "database": {
        "adapter": "pg"
        }
~~~
and add `postgresql::ruby` from the opscode cookbook to the configure postgres ruby gem

NB: If no database adapter specified it will default to mysql



**TODO** notification of restart, how does it works? ( `notifies :run, "execute[restart Rails app #{application}]"` in rails::configure)
**DONE** migration
from the deploy select migrate true

**TODO** puma
**TODO** worker

**TODO** Security
check the frontend machine security group is closed from outside
setup VPN to the VPC network

**TODO** SSL cert and Load Balancer
[Here]( http://docs.aws.amazon.com/opsworks/latest/userguide/workingsecurity-ssl.html#d0e9702
) to add SSL to instance's webserver, but we usually don't need this
feature because we add the certificate to the ELB and we use port 80
from ELB to instances.

**TODO** berkshelf etc/client/pem

**TODO** redis
free rediscloud

**TODO** mongo
free mongolab Ireland, missing backup

# Application Deployment on Custom Layers
By default OpsWorks will deploy application based on a match between the
layer type and the application type

As stated in the [doc](http://docs.aws.amazon.com/opsworks/latest/userguide/workinglayers-custom.html):AWS OpsWorks automatically deploys apps only to the built-in app server layers. To deploy apps to a custom layer's instances, you must implement custom recipes to handle the deploy operation and assign them to the layer's Deploy event.

the [Tomcat example](http://docs.aws.amazon.com/opsworks/latest/userguide/create-custom-deploy.html) of the doc define a custom deploy recipe that deploy every application:

~~~json
include_recipe 'deploy'

node[:deploy].each do |application, deploy|
  opsworks_deploy_dir do
    user deploy[:user]
    group deploy[:group]
    path deploy[:deploy_to]
  end

  opsworks_deploy do
    deploy_data deploy
    app application
  end
~~~



http://www.slideshare.net/AmazonWebServices/zero-to-sixty-aws-opsworks-dmg202-aws-reinvent-2013

The Custom JSON contains a keys for each app to be deployed on a layer
and the gittag
~~~json
{
  "app_name_1" : { "gittag" : "v1.2" };
  "app_name_2" : { "gittag" : "v3.5" };

~~~

* Get the instances by Layer ID
* Send the deploy command to those instances


To update the custom json
1. get the json from opsworks
2. update
3. upload to opsworks

TODO: possible issue is new instances booting


TODO: [blue green deploy](http://www.intelligrape.com/blog/2014/02/28/blue-green-deployment-with-aws-opsworks/)
TODO: [Kibana and logstash](http://devblog.springest.com/complete-logstash-stack-on-aws-opsworks-in-15-minutes/)
TODO: check the [artifact cookbook](https://github.com/RiotGames/artifact-cookbook)
TODO: check the [application cookbook](http://community.opscode.com/cookbooks/application)

# CI Integration

http://www.slideshare.net/AmazonWebServices/zero-to-sixty-aws-opsworks-dmg202-aws-reinvent-2013

# Users and IAM integration
You can import IAM users into opsworks. When ever you add ssh or sudo permission to a user the execute_recipes
command will execute the "ssh_users" recipe to update all stack instances.

TODO Opsworks create a set of new roles, should we care about them?

# GitLab Opsworks Cookbook

gitlab/attributes/default.rb

~~~ruby
# Databases
# Assumed defaults
# database: postgresql (option: mysql)
# environment: production (option: development)
default['gitlab']['external_database'] = false
default['gitlab']['database_adapter'] = "postgresql"
default['gitlab']['database_password'] = "datapass"
default['gitlab']['database_user'] = "git"
default['gitlab']['env'] = "production"
~~~

the gitlab:setup recipe 
# Setup chosen database
include_recipe "gitlab::database_#{gitlab['database_adapter']}"


# OpsWorks under the hood
ref: AWS OpsWorks Under the Hood (DMG304) | AWS re:Invent 2013 [video](https://www.youtube.com/watch?v=913oT6xV-Qk) and [slide](http://www.slideshare.net/AmazonWebServices/aws-opsworks-under-the-hood-dmg304-aws-reinvent-2013)

## Chef Server VS OpsWorks (with chef 11.10)

OpsWorks doesn't use chef-server but implements a custom server.

OpsWorks use an opswork-agent installed on each instance to talk with
the custom server. The opsworks-agent use the chef-client to execute a
chef-run. The chef-client is a small superset of the chef-solo tool
features, it periodically pools the chef-server and instantiate a
chef run when there is a new update. Opsworks-agent do the same with the Opsworks server.

The main difference between OpsWorks and Opscode ends when the chef-client is started. From that point onwards they behaves the same.

NOTE: previous version of the opsworks stack wraps chef-solo


Useful directories:

* /opt/aws/opsworks/ : directory with chef and opsworks binaries and
cookbooks
* /opt/aws/opsworks/current/bin/chef_command_wrapper.sh : a wrapper to
execute chef commands and save logs

**TODO** the OpsWorks team claim to use a push model but the opsworks-agent.process_command.log has tons of this log "Polling for command to process". I don't understand why this should not be a polling model...


When a command is executed by the opsworks-agent it will trigger a
chef-solo run

~~~bash
ps aux while the agent is executing chef-solo

aws      25924  0.0  0.0   4168   348 ?        S    15:33   0:00 /opt/aws/opsworks/current/bin/lockrun --wait --verbose --lockfile /var/lib/aws/opsworks/lockrun.lock -- env HOME=/root sudo /opt/aws/opsworks/current/bin/chef_solo_wrapper.sh -s /opt/aws/opsworks/current/bin/chef-solo -j /var/lib/aws/opsworks/chef/2014-03-16-15-33-33-01.json -c /opt/aws/opsworks/current/conf/solo.rb -L /var/lib/aws/opsworks/chef/2014-03-16-15-33-33-01.log 2>&1
root     25925  0.0  0.2  36096  1572 ?        S    15:33   0:00 sudo /opt/aws/opsworks/current/bin/chef_solo_wrapper.sh -s /opt/aws/opsworks/current/bin/chef-solo -j /var/lib/aws/opsworks/chef/2014-03-16-15-33-33-01.json -c /opt/aws/opsworks/current/conf/solo.rb -L /var/lib/aws/opsworks/chef/2014-03-16-15-33-33-01.log 2>&1
root     25926  0.0  0.2  11032  1476 ?        S    15:33   0:00 /bin/bash /opt/aws/opsworks/current/bin/chef_solo_wrapper.sh -s /opt/aws/opsworks/current/bin/chef-solo -j /var/lib/aws/opsworks/chef/2014-03-16-15-33-33-01.json -c /opt/aws/opsworks/current/conf/solo.rb -L /var/lib/aws/opsworks/chef/2014-03-16-15-33-33-01.log 2>&1
root     25930  0.0  0.1  11032   636 ?        S    15:33   0:00 /bin/bash /opt/aws/opsworks/current/bin/chef_solo_wrapper.sh -s /opt/aws/opsworks/current/bin/chef-solo -j /var/lib/aws/opsworks/chef/2014-03-16-15-33-33-01.json -c /opt/aws/opsworks/current/conf/solo.rb -L /var/lib/aws/opsworks/chef/2014-03-16-15-33-33-01.log 2>&1
root     25931 49.0  3.6  79420 21816 ?        R    15:33   0:00 ruby1.8 /opt/aws/opsworks/current/bin/chef-solo -j /var/lib/aws/opsworks/chef/2014-03-16-15-33-33-01.json -c /opt/aws/opsworks/current/conf/solo.rb
~~~

chef-solo is runned with this options:

* attributes file : -j /var/lib/aws/opsworks/chef/2014-03-16-15-28-20-01.json
* configuration file : -c /opt/aws/opsworks/current/conf/solo.rb

configuration file example:

~~~bash
require 'pathname'

Ohai::Config[:plugin_path] << "#{Pathname.new(__FILE__).realpath.dirname}/../plugins"
file_cache_path  "#{Pathname.new(__FILE__).realpath.dirname}/.."
cookbook_path    ["#{Pathname.new(__FILE__).realpath.dirname}/../cookbooks/","#{Pathname.new(__FILE__).realpath.dirname}/../site-cookbooks"]
log_level        :debug

%w{BUNDLE_GEMFILE GEM_HOME GEM_PATH RUBYLIB RUBYOPT}.each do |env|
  ENV[env] = nil
end

# make sure local REE is in path for Chef runs and not Agent stuff
ENV['PATH'] = "/usr/local/bin:/usr/local/sbin:#{ENV['PATH']}"

File.umask 022
~~~

The `/opt/aws/opsworks/current` dir contains both the opsworks (cookbook dir) and the
custom cookbooks (site-cookbooks dir).

attribute file example: /var/lib/aws/opsworks/chef/2014-03-16-11-04-04-01.json

~~~json
{
  "ssh_users": {
  },
  "opsworks": {
    "agent_version": "221",
    "activity": "configure",
    "valid_client_activities": [
      "reboot",
      "stop",
      "deploy",
      "setup",
      "configure",
      "update_dependencies",
      "install_dependencies",
      "update_custom_cookbooks",
      "execute_recipes"
    ],
    "sent_at": 1394966606,
    "deployment": null,
    "layers": {
      "addictive-api": {
        "name": "addictive-api",
        "id": "280016e7-9636-43c4-9609-892155db0205",
        "elb-load-balancers": [

        ],
        "instances": {
          "addictive-api2": {
            "public_dns_name": "ec2-54-72-92-117.eu-west-1.compute.amazonaws.com",
            "private_dns_name": "ip-172-31-24-122.eu-west-1.compute.internal",
            "backends": 2,
            "ip": "54.72.92.117",
            "private_ip": "172.31.24.122",
            "instance_type": "t1.micro",
            "status": "online",
            "id": "3554f1c2-52d4-45d3-b900-1b96b132cca6",
            "aws_instance_id": "i-bd90a7fc",
            "elastic_ip": null,
            "created_at": "2014-03-15T11:46:56+00:00",
            "booted_at": "2014-03-15T11:48:11+00:00",
            "region": "eu-west-1",
            "availability_zone": "eu-west-1a"
          },
          "addictive-api1": {
            "public_dns_name": "ec2-54-72-13-15.eu-west-1.compute.amazonaws.com",
            "private_dns_name": "ip-172-31-17-12.eu-west-1.compute.internal",
            "backends": 6,
            "ip": "54.72.13.15",
            "private_ip": "172.31.17.12",
            "instance_type": "m3.medium",
            "status": "online",
            "id": "5a38a023-93a3-48b2-a353-f0a4ba4755e6",
            "aws_instance_id": "i-3ea0967f",
            "elastic_ip": null,
            "created_at": "2014-03-16T10:37:28+00:00",
            "booted_at": "2014-03-16T10:38:40+00:00",
            "region": "eu-west-1",
            "availability_zone": "eu-west-1a"
          }
        }
      }
    },
    "applications": [
      {
        "name": "addictive-api",
        "slug_name": "addictive_api",
        "application_type": "rails"
      }
    ],
    "stack": {
      "name": "PitchTarget",
      "id": "4a048479-a67d-47d3-984f-415f4800d268",
      "vpc_id": "vpc-7df1e21f",
      "elb-load-balancers": [

      ]
    },
    "instance": {
      "id": "3554f1c2-52d4-45d3-b900-1b96b132cca6",
      "hostname": "addictive-api2",
      "instance_type": "t1.micro",
      "public_dns_name": "ec2-54-72-92-117.eu-west-1.compute.amazonaws.com",
      "private_dns_name": "ip-172-31-24-122.eu-west-1.compute.internal",
      "ip": "54.72.92.117",
      "private_ip": "172.31.24.122",
      "architecture": "x86_64",
      "layers": [
        "addictive-api"
      ],
      "backends": 2,
      "aws_instance_id": "i-bd90a7fc",
      "region": "eu-west-1",
      "availability_zone": "eu-west-1a",
      "subnet_id": "subnet-07647c65"
    },
    "ruby_version": "2.0.0",
    "ruby_stack": "ruby",
    "rails_stack": {
      "name": null
    }
  },
  "deploy": {
    "addictive_api": {
      "deploy_to": "/srv/www/addictive_api",
      "application": "addictive_api",
      "deploying_user": null,
      "domains": [
        "addictive_api"
      ],
      "application_type": "rails",
      "mounted_at": null,
      "rails_env": "production",
      "ssl_support": false,
      "ssl_certificate": null,
      "ssl_certificate_key": null,
      "ssl_certificate_ca": null,
      "document_root": "public",
      "restart_command": null,
      "sleep_before_restart": 0,
      "symlink_before_migrate": {
        "config/database.yml": "config/database.yml",
        "config/memcached.yml": "config/memcached.yml"
      },
      "symlinks": {
        "system": "public/system",
        "pids": "tmp/pids",
        "log": "log"
      },
      "database": {
        "host": null,
        "database": "addictive_api",
        "username": "root",
        "password": null,
        "reconnect": true
      },
      "memcached": {
        "host": null,
        "port": 11211
      },
      "migrate": false,
      "auto_bundle_on_deploy": true,
      "scm": {
        "scm_type": "git",
        "repository": "git@bitbucket.org:fungostudios/addictive-api.git",
        "revision": "develop",
        "ssh_key": "-----BEGIN RSA PRIVATE KEY-----\n .... \n-----END RSA PRIVATE KEY-----",
        "user": null,
        "password": null
      }
    }
  },
  "opsworks_custom_cookbooks": {
    "enabled": true,
    "scm": {
      "type": "git",
      "repository": "git@bitbucket.org:fungostudios/addictive-opsworks-cookbooks.git",
      "user": null,
      "password": null,
      "revision": "master",
      "ssh_key": "-----BEGIN RSA PRIVATE KEY-----\n ...... \n-----END RSA PRIVATE KEY-----"
    },
    "recipes": [
      "opsworks_ganglia::configure-client",
      "ssh_users",
      "agent_version",
      "opsworks_stack_state_sync",
      "test_suite",
      "opsworks_cleanup"
    ]
  },
  "recipes": [
    "opsworks_custom_cookbooks::load",
    "opsworks_custom_cookbooks::execute"
  ],
  "opsworks_rubygems": {
    "version": "2.2.1"
  },
  "opsworks_bundler": {
    "version": "1.5.1",
    "manage_package": null
  }
}
~~~


# Ubuntu OpsWorks Ami Internal

## opsworks-agent
This AMI has the opsworks-agent installed:
wget -O opsworks-agent.tgz https://opsworks-instance-agent.s3.amazonaws.com:443/214/opsworks-agent-installer.tgz

## Log

`/var/log/aws/opsworks` contains the opsworks-agent logs:

* **opsworks-agent.keep_alive.log**
: The agent will send a keep_alive message every minute to the opsworks server
and log here.

* **opsworks-agent.statistics.log**
: The agent will report the instance status(procs, memory, cpu, load) every minute to the opsworks server
and log here.

* **installer.log**
: agent install log, created at boot time. Useful to debug custom AMI.

* **updater.log**
: the agent checks every 10 minute if there are agent updated and log
here.

* **opsworks-agent.log**
: the agent logs here its start/stop lifecycle and chef run log uploads

* **opsworks-agent.process_command.log**
: the agent pools the server every minute to check if there are new
commands and logs here. It logs alse the chef solo execution time.

* **user-data.log**
: TODO



`/var/lib/aws/opsworks/chef` contains the chef run log:

* **YYYY-MM-DD-HH-MM-SS.log**
: TODO this should be a single chef run log

* **YYYY-MM-DD-HH-MM-SS.json**
: TODO this should be the attribute file




/var/lib/aws/opsworks/chef/2014-03-16-11-04-04-01.log

~~~bash
[2014-03-16T10:43:39+00:00] INFO: *** Chef 11.4.4 ***
[2014-03-16T10:43:42+00:00] DEBUG: Building node object for addictive-api2.localdomain
[2014-03-16T10:43:42+00:00] DEBUG: Extracting run list from JSON attributes provided on command line
[2014-03-16T10:43:42+00:00] INFO: Setting the run_list to ["opsworks_custom_cookbooks::load", "opsworks_custom_cookbooks::execute"] from JSON
[2014-03-16T10:43:42+00:00] DEBUG: Applying attributes from json file
[2014-03-16T10:43:42+00:00] DEBUG: Platform is ubuntu version 12.04
[2014-03-16T10:43:42+00:00] INFO: Run List is [recipe[opsworks_custom_cookbooks::load], recipe[opsworks_custom_cookbooks::execute]]
[2014-03-16T10:43:42+00:00] INFO: Run List expands to [opsworks_custom_cookbooks::load, opsworks_custom_cookbooks::execute]
[2014-03-16T10:43:42+00:00] INFO: Starting Chef Run for addictive-api2.localdomain
[2014-03-16T10:43:42+00:00] INFO: Running start handlers
[2014-03-16T10:43:42+00:00] INFO: Start handlers complete.
[2014-03-16T10:43:42+00:00] DEBUG: No chefignore file found at /opt/aws/opsworks/releases/20140306112110_221/cookbooks/chefignore no files will be ignored
[2014-03-16T10:43:43+00:00] DEBUG: No chefignore file found at /opt/aws/opsworks/releases/20140306112110_221/site-cookbooks/chefignore no files will be ignored
[2014-03-16T10:43:43+00:00] DEBUG: Cookbooks to compile: ["gem_support", "packages", "opsworks_bundler", "opsworks_rubygems", "ruby", "ruby_enterprise", "dependencies", "opsworks_commons", "scm_helper", :opsworks_custom_cookbooks]
[2014-03-16T10:43:43+00:00] DEBUG: Loading cookbook gem_support's library file: /opt/aws/opsworks/releases/20140306112110_221/cookbooks/gem_support/libraries/current_gem_version.rb
[2014-03-16T10:43:43+00:00] DEBUG: Loading cookbook packages's library file: /opt/aws/opsworks/releases/20140306112110_221/cookbooks/packages/libraries/packages.rb
[2014-03-16T10:43:43+00:00] DEBUG: Loading cookbook dependencies's library file: /opt/aws/opsworks/releases/20140306112110_221/cookbooks/dependencies/libraries/current_gem_version.rb
[2014-03-16T10:43:43+00:00] DEBUG: Loading cookbook opsworks_commons's library file: /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_commons/libraries/activesupport_blank.rb
[2014-03-16T10:43:43+00:00] DEBUG: Loading cookbook opsworks_commons's library file: /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_commons/libraries/monkey_patch_chefgem_resource.rb
[2014-03-16T10:43:43+00:00] DEBUG: Loading cookbook opsworks_commons's library file: /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_commons/libraries/monkey_patch_gem_package_resource.rb
[2014-03-16T10:43:43+00:00] DEBUG: Loading cookbook opsworks_commons's library file: /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_commons/libraries/monkey_patch_rubygems_provider.rb
[2014-03-16T10:43:43+00:00] DEBUG: Loading cookbook opsworks_commons's library file: /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_commons/libraries/shellout.rb
[2014-03-16T10:43:43+00:00] DEBUG: Loading cookbook scm_helper's library file: /opt/aws/opsworks/releases/20140306112110_221/cookbooks/scm_helper/libraries/archive.rb
[2014-03-16T10:43:43+00:00] DEBUG: Loading cookbook scm_helper's library file: /opt/aws/opsworks/releases/20140306112110_221/cookbooks/scm_helper/libraries/git.rb
[2014-03-16T10:43:43+00:00] DEBUG: Loading cookbook scm_helper's library file: /opt/aws/opsworks/releases/20140306112110_221/cookbooks/scm_helper/libraries/package.rb
[2014-03-16T10:43:43+00:00] DEBUG: Loading cookbook scm_helper's library file: /opt/aws/opsworks/releases/20140306112110_221/cookbooks/scm_helper/libraries/s3.rb
[2014-03-16T10:43:43+00:00] DEBUG: Loading cookbook scm_helper's library file: /opt/aws/opsworks/releases/20140306112110_221/cookbooks/scm_helper/libraries/svn.rb
[2014-03-16T10:43:43+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook packages's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/packages/attributes/customize.rb
[2014-03-16T10:43:43+00:00] DEBUG: Loading Attribute packages::customize
[2014-03-16T10:43:43+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook packages's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/packages/attributes/packages.rb
[2014-03-16T10:43:43+00:00] DEBUG: Loading Attribute packages::packages
[2014-03-16T10:43:43+00:00] DEBUG: I am not loading attribute file packages::customize, because I have already seen it.
[2014-03-16T10:43:43+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook opsworks_bundler's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_bundler/attributes/bundler.rb
[2014-03-16T10:43:43+00:00] DEBUG: Loading Attribute opsworks_bundler::bundler
[2014-03-16T10:43:43+00:00] DEBUG: Loading Attribute opsworks_bundler::customize
[2014-03-16T10:43:43+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook opsworks_bundler's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_bundler/attributes/customize.rb
[2014-03-16T10:43:43+00:00] DEBUG: I am not loading attribute file opsworks_bundler::customize, because I have already seen it.
[2014-03-16T10:43:43+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook opsworks_rubygems's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_rubygems/attributes/customize.rb
[2014-03-16T10:43:43+00:00] DEBUG: Loading Attribute opsworks_rubygems::customize
[2014-03-16T10:43:43+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook opsworks_rubygems's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_rubygems/attributes/rubygems.rb
[2014-03-16T10:43:43+00:00] DEBUG: Loading Attribute opsworks_rubygems::rubygems
[2014-03-16T10:43:43+00:00] DEBUG: Loading Attribute opsworks_initial_setup::default
[2014-03-16T10:43:43+00:00] DEBUG: Loading Attribute opsworks_initial_setup::customize
[2014-03-16T10:43:43+00:00] DEBUG: I am not loading attribute file opsworks_rubygems::customize, because I have already seen it.
[2014-03-16T10:43:43+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook ruby's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/ruby/attributes/customize.rb
[2014-03-16T10:43:43+00:00] DEBUG: Loading Attribute ruby::customize
[2014-03-16T10:43:43+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook ruby's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/ruby/attributes/ruby.rb
[2014-03-16T10:43:43+00:00] DEBUG: Loading Attribute ruby::ruby
[2014-03-16T10:43:43+00:00] DEBUG: I am not loading attribute file opsworks_initial_setup::default, because I have already seen it.
[2014-03-16T10:43:43+00:00] DEBUG: Loading Attribute opsworks_commons::default
[2014-03-16T10:43:43+00:00] DEBUG: Loading Attribute opsworks_commons::customize
[2014-03-16T10:43:43+00:00] DEBUG: I am not loading attribute file ruby::customize, because I have already seen it.
[2014-03-16T10:43:43+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook ruby_enterprise's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/ruby_enterprise/attributes/customize.rb
[2014-03-16T10:43:43+00:00] DEBUG: Loading Attribute ruby_enterprise::customize
[2014-03-16T10:43:43+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook ruby_enterprise's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/ruby_enterprise/attributes/ruby_enterprise.rb
[2014-03-16T10:43:43+00:00] DEBUG: Loading Attribute ruby_enterprise::ruby_enterprise
[2014-03-16T10:43:43+00:00] DEBUG: I am not loading attribute file opsworks_commons::default, because I have already seen it.
[2014-03-16T10:43:43+00:00] DEBUG: I am not loading attribute file opsworks_rubygems::rubygems, because I have already seen it.
[2014-03-16T10:43:43+00:00] DEBUG: I am not loading attribute file ruby_enterprise::customize, because I have already seen it.
[2014-03-16T10:43:43+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook dependencies's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/dependencies/attributes/default.rb
[2014-03-16T10:43:43+00:00] DEBUG: Loading Attribute dependencies::default
[2014-03-16T10:43:43+00:00] DEBUG: I am not loading attribute file ruby::ruby, because I have already seen it.
[2014-03-16T10:43:43+00:00] DEBUG: Loading Attribute dependencies::customize
[2014-03-16T10:43:43+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook dependencies's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/dependencies/attributes/customize.rb
[2014-03-16T10:43:43+00:00] DEBUG: I am not loading attribute file dependencies::customize, because I have already seen it.
[2014-03-16T10:43:43+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook opsworks_commons's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_commons/attributes/default.rb
[2014-03-16T10:43:43+00:00] DEBUG: I am not loading attribute file opsworks_commons::default, because I have already seen it.
[2014-03-16T10:43:43+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook opsworks_commons's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_commons/attributes/customize.rb
[2014-03-16T10:43:43+00:00] DEBUG: I am not loading attribute file opsworks_commons::customize, because I have already seen it.
[2014-03-16T10:43:43+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook opsworks_custom_cookbooks's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_custom_cookbooks/attributes/default.rb
[2014-03-16T10:43:43+00:00] DEBUG: Loading Attribute opsworks_custom_cookbooks::default
[2014-03-16T10:43:43+00:00] DEBUG: I am not loading attribute file opsworks_initial_setup::default, because I have already seen it.
[2014-03-16T10:43:43+00:00] DEBUG: Loading Attribute opsworks_custom_cookbooks::customize
[2014-03-16T10:43:43+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook opsworks_custom_cookbooks's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_custom_cookbooks/attributes/customize.rb
[2014-03-16T10:43:43+00:00] DEBUG: I am not loading attribute file opsworks_custom_cookbooks::customize, because I have already seen it.
[2014-03-16T10:43:43+00:00] DEBUG: Loading cookbook opsworks_commons's definitions from /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_commons/definitions/fallback.rb
[2014-03-16T10:43:43+00:00] DEBUG: Loading Recipe opsworks_custom_cookbooks::load via include_recipe
[2014-03-16T10:43:43+00:00] DEBUG: Found recipe load in cookbook opsworks_custom_cookbooks
[2014-03-16T10:43:43+00:00] DEBUG: Loading Recipe opsworks_custom_cookbooks::checkout via include_recipe
[2014-03-16T10:43:43+00:00] DEBUG: Found recipe checkout in cookbook opsworks_custom_cookbooks
[2014-03-16T10:43:43+00:00] DEBUG: Loading Recipe opsworks_custom_cookbooks::execute via include_recipe
[2014-03-16T10:43:43+00:00] DEBUG: Found recipe execute in cookbook opsworks_custom_cookbooks
[2014-03-16T10:43:43+00:00] INFO: OpsWorks Custom Run List: ["opsworks_ganglia::configure-client", "ssh_users", "agent_version", "opsworks_stack_state_sync", "test_suite", "opsworks_cleanup"]
[2014-03-16T10:43:43+00:00] DEBUG: Loading from cookbook_path: /opt/aws/opsworks/releases/20140306112110_221/cookbooks, /opt/aws/opsworks/releases/20140306112110_221/site-cookbooks
[2014-03-16T10:43:43+00:00] DEBUG: Converging node addictive-api2.localdomain
[2014-03-16T10:43:43+00:00] INFO: Processing package[git-core] action install (opsworks_custom_cookbooks::checkout line 9)
[2014-03-16T10:43:43+00:00] DEBUG: package[git-core] checking package status for git-core
[2014-03-16T10:43:44+00:00] DEBUG: package[git-core] current version is 1:1.7.9.5-1
[2014-03-16T10:43:44+00:00] DEBUG: package[git-core] candidate version is 1:1.7.9.5-1
[2014-03-16T10:43:44+00:00] DEBUG: package[git-core] is already installed - nothing to do
[2014-03-16T10:43:44+00:00] INFO: Processing directory[/root/.ssh] action create (opsworks_custom_cookbooks::checkout line 8)
[2014-03-16T10:43:44+00:00] INFO: Processing file[/root/.ssh/config] action touch (opsworks_custom_cookbooks::checkout line 16)
[2014-03-16T10:43:44+00:00] INFO: file[/root/.ssh/config] updated atime and mtime to Sun Mar 16 10:43:44 +0000 2014
[2014-03-16T10:43:44+00:00] INFO: Processing execute[echo 'StrictHostKeyChecking no' > /root/.ssh/config] action run (opsworks_custom_cookbooks::checkout line 23)
[2014-03-16T10:43:44+00:00] DEBUG: Skipping execute[echo 'StrictHostKeyChecking no' > /root/.ssh/config] due to not_if command `grep '^StrictHostKeyChecking no$' /root/.ssh/config`
[2014-03-16T10:43:44+00:00] INFO: Processing template[/root/.ssh/id_dsa] action create (opsworks_custom_cookbooks::checkout line 27)
[2014-03-16T10:43:44+00:00] DEBUG: Current content's checksum:  059c8e7fb62b641dd0a6a8c725d201b66bfaa421ce6b39efca7780fc633c469c
[2014-03-16T10:43:44+00:00] DEBUG: Rendered content's checksum: 059c8e7fb62b641dd0a6a8c725d201b66bfaa421ce6b39efca7780fc633c469c
[2014-03-16T10:43:44+00:00] DEBUG: template[/root/.ssh/id_dsa] content has not changed.
[2014-03-16T10:43:44+00:00] INFO: Processing git[Download Custom Cookbooks] action checkout (opsworks_custom_cookbooks::checkout line 29)
[2014-03-16T10:43:44+00:00] DEBUG: Skipping git[Download Custom Cookbooks] due to not_if ruby block
[2014-03-16T10:43:44+00:00] INFO: Processing ruby_block[Move single cookbook contents into appropriate subdirectory] action run (opsworks_custom_cookbooks::checkout line 64)
[2014-03-16T10:43:44+00:00] DEBUG: Skipping ruby_block[Move single cookbook contents into appropriate subdirectory] due to only_if ruby block
[2014-03-16T10:43:44+00:00] INFO: Processing execute[ensure correct permissions of custom cookbooks] action run (opsworks_custom_cookbooks::checkout line 80)
[2014-03-16T10:43:44+00:00] INFO: execute[ensure correct permissions of custom cookbooks] ran successfully
[2014-03-16T10:43:44+00:00] INFO: Processing ruby_block[Compile Custom OpsWorks Run List] action run (opsworks_custom_cookbooks::execute line 3)
[2014-03-16T10:43:44+00:00] DEBUG: No chefignore file found at /opt/aws/opsworks/releases/20140306112110_221/cookbooks/chefignore no files will be ignored
[2014-03-16T10:43:44+00:00] DEBUG: No chefignore file found at /opt/aws/opsworks/releases/20140306112110_221/site-cookbooks/chefignore no files will be ignored
[2014-03-16T10:43:44+00:00] INFO: New Run List expands to ["opsworks_ganglia::configure-client", "ssh_users", "agent_version", "opsworks_stack_state_sync", "test_suite", "opsworks_cleanup"]
[2014-03-16T10:43:44+00:00] DEBUG: Cookbooks to compile: [:opsworks_ganglia, "gem_support", "packages", "opsworks_bundler", "opsworks_rubygems", "ruby", "ruby_enterprise", "dependencies", "opsworks_commons", "opsworks_initial_setup", :ssh_users, :agent_version, :opsworks_stack_state_sync, :test_suite, :opsworks_cleanup]
[2014-03-16T10:43:44+00:00] DEBUG: Loading cookbook gem_support's library file: /opt/aws/opsworks/releases/20140306112110_221/cookbooks/gem_support/libraries/current_gem_version.rb
[2014-03-16T10:43:44+00:00] DEBUG: Loading cookbook packages's library file: /opt/aws/opsworks/releases/20140306112110_221/cookbooks/packages/libraries/packages.rb
[2014-03-16T10:43:44+00:00] DEBUG: Loading cookbook dependencies's library file: /opt/aws/opsworks/releases/20140306112110_221/cookbooks/dependencies/libraries/current_gem_version.rb
[2014-03-16T10:43:44+00:00] DEBUG: Loading cookbook opsworks_commons's library file: /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_commons/libraries/activesupport_blank.rb
/opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_commons/libraries/activesupport_blank.rb:92: warning: already initialized constant NON_WHITESPACE_REGEXP
[2014-03-16T10:43:44+00:00] DEBUG: Loading cookbook opsworks_commons's library file: /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_commons/libraries/monkey_patch_chefgem_resource.rb
[2014-03-16T10:43:44+00:00] DEBUG: Loading cookbook opsworks_commons's library file: /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_commons/libraries/monkey_patch_gem_package_resource.rb
[2014-03-16T10:43:44+00:00] DEBUG: Loading cookbook opsworks_commons's library file: /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_commons/libraries/monkey_patch_rubygems_provider.rb
[2014-03-16T10:43:44+00:00] DEBUG: Loading cookbook opsworks_commons's library file: /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_commons/libraries/shellout.rb
[2014-03-16T10:43:44+00:00] DEBUG: Loading cookbook ssh_users's library file: /opt/aws/opsworks/releases/20140306112110_221/cookbooks/ssh_users/libraries/user.rb
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook opsworks_ganglia's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_ganglia/attributes/default.rb
[2014-03-16T10:43:44+00:00] DEBUG: Loading Attribute opsworks_ganglia::default
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file opsworks_initial_setup::default, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Loading Attribute apache2::apache
[2014-03-16T10:43:44+00:00] DEBUG: Loading Attribute apache2::customize
[2014-03-16T10:43:44+00:00] DEBUG: Loading Attribute opsworks_ganglia::customize
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook opsworks_ganglia's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_ganglia/attributes/customize.rb
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file opsworks_ganglia::customize, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook packages's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/packages/attributes/customize.rb
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file packages::customize, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook packages's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/packages/attributes/packages.rb
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file packages::packages, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook opsworks_bundler's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_bundler/attributes/bundler.rb
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file opsworks_bundler::bundler, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook opsworks_bundler's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_bundler/attributes/customize.rb
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file opsworks_bundler::customize, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook opsworks_rubygems's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_rubygems/attributes/customize.rb
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file opsworks_rubygems::customize, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook opsworks_rubygems's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_rubygems/attributes/rubygems.rb
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file opsworks_rubygems::rubygems, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook ruby's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/ruby/attributes/customize.rb
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file ruby::customize, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook ruby's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/ruby/attributes/ruby.rb
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file ruby::ruby, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook ruby_enterprise's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/ruby_enterprise/attributes/customize.rb
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file ruby_enterprise::customize, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook ruby_enterprise's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/ruby_enterprise/attributes/ruby_enterprise.rb
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file ruby_enterprise::ruby_enterprise, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook dependencies's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/dependencies/attributes/default.rb
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file dependencies::default, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook dependencies's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/dependencies/attributes/customize.rb
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file dependencies::customize, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook opsworks_commons's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_commons/attributes/default.rb
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file opsworks_commons::default, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook opsworks_commons's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_commons/attributes/customize.rb
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file opsworks_commons::customize, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook opsworks_initial_setup's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_initial_setup/attributes/default.rb
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file opsworks_initial_setup::default, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook opsworks_initial_setup's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_initial_setup/attributes/customize.rb
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file opsworks_initial_setup::customize, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook ssh_users's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/ssh_users/attributes/default.rb
[2014-03-16T10:43:44+00:00] DEBUG: Loading Attribute ssh_users::default
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file opsworks_initial_setup::default, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Loading Attribute ssh_users::customize
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook ssh_users's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/ssh_users/attributes/customize.rb
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file ssh_users::customize, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook agent_version's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/agent_version/attributes/default.rb
[2014-03-16T10:43:44+00:00] DEBUG: Loading Attribute agent_version::default
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file opsworks_initial_setup::default, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Loading Attribute agent_version::customize
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook agent_version's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/agent_version/attributes/customize.rb
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file agent_version::customize, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook test_suite's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/test_suite/attributes/default.rb
[2014-03-16T10:43:44+00:00] DEBUG: Loading Attribute test_suite::default
[2014-03-16T10:43:44+00:00] DEBUG: Loading Attribute test_suite::customize
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook test_suite's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/test_suite/attributes/customize.rb
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file test_suite::customize, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook opsworks_cleanup's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_cleanup/attributes/default.rb
[2014-03-16T10:43:44+00:00] DEBUG: Loading Attribute opsworks_cleanup::default
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file opsworks_initial_setup::default, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Loading Attribute opsworks_cleanup::customize
[2014-03-16T10:43:44+00:00] DEBUG: Node addictive-api2.localdomain loading cookbook opsworks_cleanup's attribute file /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_cleanup/attributes/customize.rb
[2014-03-16T10:43:44+00:00] DEBUG: I am not loading attribute file opsworks_cleanup::customize, because I have already seen it.
[2014-03-16T10:43:44+00:00] DEBUG: Loading cookbook opsworks_commons's definitions from /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_commons/definitions/fallback.rb
[2014-03-16T10:43:44+00:00] INFO: Overriding duplicate definition fallback, new definition found in /opt/aws/opsworks/releases/20140306112110_221/cookbooks/opsworks_commons/definitions/fallback.rb
[2014-03-16T10:43:44+00:00] DEBUG: Loading Recipe opsworks_ganglia::configure-client via include_recipe
[2014-03-16T10:43:44+00:00] DEBUG: Found recipe configure-client in cookbook opsworks_ganglia
[2014-03-16T10:43:44+00:00] DEBUG: Loading Recipe ssh_users via include_recipe
[2014-03-16T10:43:44+00:00] DEBUG: Found recipe default in cookbook ssh_users
[2014-03-16T10:43:44+00:00] DEBUG: Loading Recipe agent_version via include_recipe
[2014-03-16T10:43:44+00:00] DEBUG: Found recipe default in cookbook agent_version
[2014-03-16T10:43:44+00:00] INFO: Updating agent TARGET_VERSION to 221
[2014-03-16T10:43:44+00:00] DEBUG: Loading Recipe opsworks_stack_state_sync via include_recipe
[2014-03-16T10:43:44+00:00] DEBUG: Found recipe default in cookbook opsworks_stack_state_sync
[2014-03-16T10:43:44+00:00] DEBUG: Loading Recipe opsworks_stack_state_sync::hosts via include_recipe
[2014-03-16T10:43:44+00:00] DEBUG: Found recipe hosts in cookbook opsworks_stack_state_sync
[2014-03-16T10:43:45+00:00] DEBUG: Loading Recipe opsworks_stack_state_sync::motd via include_recipe
[2014-03-16T10:43:45+00:00] DEBUG: Found recipe motd in cookbook opsworks_stack_state_sync
[2014-03-16T10:43:45+00:00] DEBUG: Loading Recipe test_suite via include_recipe
[2014-03-16T10:43:45+00:00] DEBUG: Found recipe default in cookbook test_suite
[2014-03-16T10:43:45+00:00] DEBUG: Loading Recipe opsworks_cleanup via include_recipe
[2014-03-16T10:43:45+00:00] DEBUG: Found recipe default in cookbook opsworks_cleanup
[2014-03-16T10:43:45+00:00] INFO: ruby_block[Compile Custom OpsWorks Run List] called
[2014-03-16T10:43:45+00:00] INFO: Processing service[gmond] action nothing (opsworks_ganglia::configure-client line 1)
[2014-03-16T10:43:45+00:00] DEBUG: service[gmond] falling back to process table inspection
[2014-03-16T10:43:45+00:00] DEBUG: service[gmond] attempting to match 'gmond' (/gmond/) against process list
[2014-03-16T10:43:45+00:00] DEBUG: service[gmond] running: true
[2014-03-16T10:43:45+00:00] DEBUG: Doing nothing for service[gmond]
[2014-03-16T10:43:45+00:00] INFO: Processing template[/etc/ganglia/gmond.conf] action create (opsworks_ganglia::configure-client line 21)
[2014-03-16T10:43:45+00:00] DEBUG: Current content's checksum:  4bc75791e5ca09307f2b2ff4180d7a00ef0a12319cebd2dffd17f951b4a3dc55
[2014-03-16T10:43:45+00:00] DEBUG: Rendered content's checksum: 4bc75791e5ca09307f2b2ff4180d7a00ef0a12319cebd2dffd17f951b4a3dc55
[2014-03-16T10:43:45+00:00] DEBUG: template[/etc/ganglia/gmond.conf] content has not changed.
[2014-03-16T10:43:45+00:00] INFO: Processing execute[Stop gmond if there is no monitoring master] action run (opsworks_ganglia::configure-client line 34)
15044
[2014-03-16T10:43:45+00:00] INFO: execute[Stop gmond if there is no monitoring master] ran successfully
[2014-03-16T10:43:45+00:00] INFO: Processing group[opsworks] action create (ssh_users::default line 1)
[2014-03-16T10:43:45+00:00] INFO: Processing template[/etc/sudoers] action create (ssh_users::default line 31)
[2014-03-16T10:43:45+00:00] DEBUG: Current content's checksum:  50f0eac71be219aa080d7d3028e85778e88d6726e5c74f18cd09623878a9b21f
[2014-03-16T10:43:45+00:00] DEBUG: Rendered content's checksum: 50f0eac71be219aa080d7d3028e85778e88d6726e5c74f18cd09623878a9b21f
[2014-03-16T10:43:45+00:00] DEBUG: template[/etc/sudoers] content has not changed.
[2014-03-16T10:43:45+00:00] INFO: Processing template[/var/lib/aws/opsworks/TARGET_VERSION] action create (agent_version::default line 1)
[2014-03-16T10:43:45+00:00] DEBUG: Current content's checksum:  67e9c3acebb154a282f326d4ff1951cd1f342e58e74d562b556b517da5e56132
[2014-03-16T10:43:45+00:00] DEBUG: Rendered content's checksum: 67e9c3acebb154a282f326d4ff1951cd1f342e58e74d562b556b517da5e56132
[2014-03-16T10:43:45+00:00] DEBUG: template[/var/lib/aws/opsworks/TARGET_VERSION] content has not changed.
[2014-03-16T10:43:45+00:00] INFO: Processing template[/etc/hosts] action create (opsworks_stack_state_sync::hosts line 3)
[2014-03-16T10:43:45+00:00] DEBUG: Current content's checksum:  e8794930b8d78b48cc69df48b8fa8c5aaf3f8dd1acfdc92d43f88babf8b58234
[2014-03-16T10:43:45+00:00] DEBUG: Rendered content's checksum: d540d86e846daeef1c6d803f4a87a5d2c19bb9168e4d2f2298019be4618dbd24
[2014-03-16T10:43:45+00:00] INFO: template[/etc/hosts] backed up to /var/chef/backup/etc/hosts.chef-20140316104345
[2014-03-16T10:43:45+00:00] INFO: template[/etc/hosts] updated content
[2014-03-16T10:43:45+00:00] INFO: template[/etc/hosts] mode changed to 644
[2014-03-16T10:43:45+00:00] INFO: Processing template[/etc/motd.opsworks-static] action create (opsworks_stack_state_sync::motd line 1)
[2014-03-16T10:43:45+00:00] DEBUG: Current content's checksum:  f1b6d1f38500660547b77547074bfba8ccb65b24c6311c8708a7a9c640cbde3a
[2014-03-16T10:43:45+00:00] DEBUG: Rendered content's checksum: f1b6d1f38500660547b77547074bfba8ccb65b24c6311c8708a7a9c640cbde3a
[2014-03-16T10:43:45+00:00] DEBUG: template[/etc/motd.opsworks-static] content has not changed.
[2014-03-16T10:43:45+00:00] INFO: Processing ruby_block[Remove temp directories] action run (opsworks_cleanup::default line 3)
[2014-03-16T10:43:45+00:00] INFO: ruby_block[Remove temp directories] called
[2014-03-16T10:43:45+00:00] INFO: Processing ruby_block[Clean up old chef log files] action run (opsworks_cleanup::default line 11)
[2014-03-16T10:43:45+00:00] INFO: Clean up: There are fewer than 10 logs - skipping cleanup
[2014-03-16T10:43:45+00:00] INFO: ruby_block[Clean up old chef log files] called
[2014-03-16T10:43:45+00:00] INFO: Chef Run complete in 2.980203 seconds
[2014-03-16T10:43:45+00:00] INFO: Running report handlers
[2014-03-16T10:43:45+00:00] INFO: Report handlers complete
[2014-03-16T10:43:45+00:00] DEBUG: Exiting
~~~









==> opsworks-agent.process_command.log <==
[2014-03-16 10:56:55]  INFO [opsworks-agent(839)]: process_command: Polling for command to process

==> opsworks-agent.statistics.log <==
[2014-03-16 10:57:10]  INFO [opsworks-agent(837)]: statistics: Calculating system statistics.
[2014-03-16 10:57:13]  INFO [opsworks-agent(837)]: statistics: Reported statistics data: {"stats":{"procs":81,"memory":{"used":330836,"free":95248,"buffers":35064,"total":604328,"swap":0,"cached":143180},"cpu":{"idle":99.93,"nice":0.0,"waitio":0.0,"user":0.0,"system":0.0,"steal":0.0},"collected_at":"2014-03-16T10:57:13Z","load":{"load_15":0.05,"load_1":0.0,"load_5":0.01}}}
[2014-03-16 10:57:13]  INFO [opsworks-agent(837)]: statistics: Reported statistics. (3.45263314247131 sec)

==> opsworks-agent.keep_alive.log <==
[2014-03-16 10:57:14]  INFO [opsworks-agent(825)]: keep_alive: Reporting keepalive. (0.595 sec)








# Chef Debug
~~~bash
\================================================================================
Error executing action `deploy` on resource 'deploy[/srv/www/addictive_api]'
\================================================================================
 
 
Chef::Exceptions::Exec
\----------------------
if [ -f Gemfile ]; then echo 'OpsWorks: Gemfile found - running migration with bundle exec' && /usr/local/bin/bundle exec /usr/local/bin/rake db:migrate; else echo 'OpsWorks: no Gemfile - running plain migrations' && /usr/local/bin/rake db:migrate; fi returned 1, expected 0
---- Begin output of if [ -f Gemfile ]; then echo 'OpsWorks: Gemfile found - running migration with bundle exec' && /usr/local/bin/bundle exec /usr/local/bin/rake db:migrate; else echo 'OpsWorks: no Gemfile - running plain migrations' && /usr/local/bin/rake db:migrate; fi ----
STDOUT: OpsWorks: Gemfile found - running migration with bundle execSTDERR: rake aborted!
Specified 'mysql' for database adapter, but the gem is not loaded. Add `gem 'mysql'` to your Gemfile.
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/activerecord-4.0.4/lib/active_record/connection_adapters/connection_specification.rb:58:in `rescue in resolve_hash_connection'
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/activerecord-4.0.4/lib/active_record/connection_adapters/connection_specification.rb:55:in `resolve_hash_connection'
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/activerecord-4.0.4/lib/active_record/connection_adapters/connection_specification.rb:46:in `resolve_string_connection'
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/activerecord-4.0.4/lib/active_record/connection_adapters/connection_specification.rb:30:in `spec'
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/activerecord-4.0.4/lib/active_record/connection_handling.rb:39:in `establish_connection'
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/activerecord-4.0.4/lib/active_record/railtie.rb:176:in `block (2 levels) in <class:Railtie>'
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/activesupport-4.0.4/lib/active_support/lazy_load_hooks.rb:38:in `instance_eval'
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/activesupport-4.0.4/lib/active_support/lazy_load_hooks.rb:38:in `execute_hook'
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/activesupport-4.0.4/lib/active_support/lazy_load_hooks.rb:28:in `block in on_load'
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/activesupport-4.0.4/lib/active_support/lazy_load_hooks.rb:27:in `each'
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/activesupport-4.0.4/lib/active_support/lazy_load_hooks.rb:27:in `on_load'
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/activerecord-4.0.4/lib/active_record/railtie.rb:174:in `block in <class:Railtie>'
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/railties-4.0.4/lib/rails/initializable.rb:30:in `instance_exec'
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/railties-4.0.4/lib/rails/initializable.rb:30:in `run'
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/railties-4.0.4/lib/rails/initializable.rb:55:in `block in run_initializers'
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/railties-4.0.4/lib/rails/initializable.rb:54:in `run_initializers'
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/railties-4.0.4/lib/rails/application.rb:215:in `initialize!'
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/railties-4.0.4/lib/rails/railtie/configurable.rb:30:in `method_missing'
/srv/www/addictive_api/releases/20140318100845/config/environment.rb:5:in `<top (required)>'
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/activesupport-4.0.4/lib/active_support/dependencies.rb:229:in `require'
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/activesupport-4.0.4/lib/active_support/dependencies.rb:229:in `block in require'
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/activesupport-4.0.4/lib/active_support/dependencies.rb:214:in `load_dependency'
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/activesupport-4.0.4/lib/active_support/dependencies.rb:229:in `require'
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/railties-4.0.4/lib/rails/application.rb:189:in `require_environment!'
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/railties-4.0.4/lib/rails/application.rb:250:in `block in run_tasks_blocks'
Tasks: TOP => db:migrate => environment
(See full trace by running task with --trace)
---- End output of if [ -f Gemfile ]; then echo 'OpsWorks: Gemfile found - running migration with bundle exec' && /usr/local/bin/bundle exec /usr/local/bin/rake db:migrate; else echo 'OpsWorks: no Gemfile - running plain migrations' && /usr/local/bin/rake db:migrate; fi ----
 
 
 
Resource Declaration:
---------------------
# In /opt/aws/opsworks/releases/20140306112110_221/cookbooks/deploy/definitions/opsworks_deploy.rb
 
65:     deploy deploy[:deploy_to] do
66:       provider Chef::Provider::Deploy.const_get(deploy[:chef_provider])
67:       if deploy[:keep_releases]
68:         keep_releases deploy[:keep_releases]
69:       end
70:       repository deploy[:scm][:repository]
 
 
 
Compiled Resource:
------------------
# Declared in /opt/aws/opsworks/releases/20140306112110_221/cookbooks/deploy/definitions/opsworks_deploy.rb:65:in `from_file'
 
deploy("/srv/www/addictive_api") do
repository_cache "cached-copy"
retries 0
migrate true
updated true
destination "/srv/www/addictive_api/shared/cached-copy"
cookbook_name :deploy
create_dirs_before_symlink ["tmp", "public", "config"]
before_migrate #<Proc:0x00007fc69b807c30@/opt/aws/opsworks/releases/20140306112110_221/cookbooks/deploy/definitions/opsworks_deploy.rb:99>
recipe_name "rails"
scm_provider Chef::Provider::Git
environment {"LC_ALL"=>"C", "RAILS_ENV"=>"production", "HOME"=>"/home/deploy", "RACK_ENV"=>"production", "RUBYOPT"=>""}
deploy_to "/srv/www/addictive_api"
revision "develop"
action [:deploy]
provider Chef::Provider::Deploy::Timestamped
keep_releases 5
purge_before_symlink ["log", "tmp/pids", "public/system"]
restart_command "sleep 0 && ../../shared/scripts/unicorn clean-restart"
migration_command "if [ -f Gemfile ]; then echo 'OpsWorks: Gemfile found - running migration with bundle exec' && /usr/local/bin/bundle exec /usr/local/bin/rake db:migrate; else echo 'OpsWorks: no Gemfile - running plain migrations' && /usr/local/bin/rake db:migrate; fi"
user "deploy"
enable_submodules true
current_path "/srv/www/addictive_api/current"
symlinks {"pids"=>"tmp/pids", "log"=>"log", "system"=>"public/system"}
params {:name=>nil, :app=>"addictive_api", :deploy_data=>{"rake"=>"/usr/local/bin/rake", "migrate"=>true, "action"=>"deploy", "auto_npm_install_on_deploy"=>true, "puma"=>{"logrotate"=>false}, "chef_provider"=>"Timestamped", "migrate_command"=>"if [ -f Gemfile ]; then echo 'OpsWorks: Gemfile found - running migration with bundle exec' && /usr/local/bin/bundle exec /usr/local/bin/rake db:migrate; else echo 'OpsWorks: no Gemfile - running plain migrations' && /usr/local/bin/rake db:migrate; fi", "shell"=>"/bin/bash", "home"=>"/home/deploy", "enable_submodules"=>true, "symlink_before_migrate"=>{"config/database.yml"=>"config/database.yml", "config/env"=>".env", "config/memcached.yml"=>"config/memcached.yml"}, "nodejs"=>{"restart_command"=>"monit restart node_web_app_addictive_api", "stop_command"=>"monit stop node_web_app_addictive_api"}, "current_path"=>"/srv/www/addictive_api/current", "user"=>"deploy", "deploying_user"=>"arn:aws:iam::470031436598:root", "application_type"=>"rails", "restart_command"=>nil, "keep_releases"=>5, "ignore_bundler_groups"=>["test", "development"], "ssl_certificate_ca"=>nil, "auto_bundle_on_deploy"=>true, "rails_env"=>"production", "delete_cached_copy"=>true, "ssl_support"=>false, "mounted_at"=>nil, "ssl_certificate_key"=>nil, "scm"=>{"password"=>nil, "revision"=>"develop", "scm_type"=>"git", "user"=>nil, "ssh_key"=>"----END RSA PRIVATE KEY-----", "repository"=>"git@bitbucket.org:fungostudios/addictive-api.git"}, "deploy_to"=>"/srv/www/addictive_api", "group"=>"www-data", "domains"=>["addictive_api", "pippo"], "document_root"=>"public", "application"=>"addictive_api", "stack"=>{"needs_reload"=>true}, "ssl_certificate"=>nil, "memcached"=>{"host"=>nil, "port"=>11211}, "absolute_document_root"=>"/srv/www/addictive_api/current/public/", "sleep_before_restart"=>0, "shallow_clone"=>false, "environment"=>{"RAILS_ENV"=>"production", "HOME"=>"/home/deploy", "RACK_ENV"=>"production", "RUBYOPT"=>""}, "symlinks"=>{"pids"=>"tmp/pids", "log"=>"log", "system"=>"public/system"}, "database"=>{"password"=>nil, "host"=>nil, "reconnect"=>true, "username"=>"root", "adapter"=>"pg", "database"=>"addictive_api"}}}
remote "origin"
retry_delay 2
repo "git@bitbucket.org:fungostudios/addictive-api.git"
updated_by_last_action true
shared_path "/srv/www/addictive_api/shared"
group "www-data"
symlink_before_migrate {"config/database.yml"=>"config/database.yml", "config/env"=>".env", "config/memcached.yml"=>"config/memcached.yml"}
end

~~~
