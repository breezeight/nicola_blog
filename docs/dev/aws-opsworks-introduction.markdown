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

# TODO

Q: What happens on autoscaling? What applications are deployed ? Does AWS attempt to deploy every app and its layer's reponsability to select the proper one?
A: ????



# Basic Concepts

## Stack

* The stack is the top-level AWS OpsWorks entity.
* It represents a set of instances that you want to manage collectively.

## Layer

* A layer is essentially a blueprint for an Amazon EC2 instance with
similar behavior ( recipe/runlist, settings/attributes )
* Every stack has at least one and usually several layers.
* Instances can optionally be a member of multiple layers (but not all
layers are compatible).
* Similar to **Chef Role**
* Layers support [Auto Healing](http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-autohealing.html) of instances 

## App

* Some of AWS OpsWorks's layers support application servers.
* An AWS OpsWorks app represents code that you want to run on an application server.

## Deployment

# Lifecycle

[DOC](http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook-events.html)


A layer has a sequence of five lifecycle events, each of which has an associated set of recipes that are specific to the layer. When an event occurs on a layer's instance, AWS OpsWorks automatically runs the appropriate set of recipes.

* **Setup** occurs on a new instance after it successfully boots. AWS OpsWorks runs recipes that set the instance up according to its layer. For example, if the instance is a member of the Rails App Server layer, the Setup recipes install Apache, Ruby Enterprise Edition, Passenger and Ruby on Rails. **Setup includes Deploy** (it means that recipes associated to the deploy event will be appended to the run list during a setup event), which automatically deploys the appropriate recipes to a new instance after setup is complete.

* **Configure** occurs on all of the stack's instances when an instance enters or leaves the online state. For example, suppose that your stack has instances A, B, and C, and you start a new instance, D. After D has finished running its setup recipes, AWS OpsWorks triggers the Configure event on A, B, C, and D. If you subsequently stop A, AWS OpsWorks triggers the Configure event on B, C, and D. AWS OpsWorks responds to the Configure event by running each layer's Configure recipes, which update the instances' configuration to reflect the current set of online instances. The Configure event is therefore a good time to regenerate configuration files. For example, the HAProxy Configure recipes reconfigure the load balancer to accommodate any changes in the set of online application server instances.

* **Deploy** occurs when you run a Deploy command, typically to deploy an application to a set of application server instances. The instances run recipes that deploy the application and any related files from its repository to the layer's instances. For example, for a Rails Application Server instances, the Deploy recipes check out a specified Ruby application and tell Phusion Passenger to reload it. You can also run Deploy on other instances so they can, for example, update their configuration to accommodate the newly deployed app. Note that Setup includes Deploy; it runs the Deploy recipes after setup is complete to automatically deploy the appropriate recipes to a new instance.

* **Undeploy** occurs when you delete an app or run an Undeploy command to remove an app from a set of application server instances. The specified instances run recipes to remove all application versions and perform any required cleanup.

* **Shutdown** occurs after you direct AWS OpsWorks to shut an instance down but before the associated Amazon EC2 instance is actually terminated. AWS OpsWorks runs recipes to perform cleanup tasks such as shutting down services. AWS OpsWorks allows Shutdown recipes 45 seconds to perform their tasks, and then terminates the Amazon EC2 instance.

When an instance is booted opsworks will run the "setup" and the "configure" 

During the configure command the rails recipe will try to deploy existing apps

# API

## Opsworks API

[Opsworks API Doc](http://docs.aws.amazon.com/opsworks/latest/APIReference/Welcome.html)

## CloudFormation support for OpsWorks

WARNING: a lot of params are documented in the [Opsworks API Doc](http://docs.aws.amazon.com/opsworks/latest/APIReference/Welcome.html) not in the cloudformation doc.

OpsWorks Example:
https://s3.amazonaws.com/cloudformation-templates-us-east-1/OpsWorks.template

[Issue Berkshelf not supported, need manual activation](https://forums.aws.amazon.com/thread.jspa?messageID=544082)

##  Stack, Layers, App Attributes vs chef attributes

Stacks, layers, apps have attributes that you can set from console or API, they are NOT chef attributes. But they can affect the list of recipe and chef attributes, for example the RailsStack layer attribute can be used to include recipe for Apache+Passenger or instead for Nginx-Unicorn in a Rails App Layer.

NB: If you use a custom layer you
 

* [stack attributes](http://docs.aws.amazon.com/opsworks/latest/APIReference/API_CreateStack.html#opsworks-CreateStack-request-Attributes)

~~~json
            "Attributes": {
                "Color": "rgb(45, 114, 184)"
            }
~~~

* [app attributes](http://docs.aws.amazon.com/opsworks/latest/APIReference/API_CreateApp.html#opsworks-CreateApp-request-Attributes)

~~~json
            "Attributes": {
                "RailsEnv": "production", 
                "AutoBundleOnDeploy": "true", 
                "DocumentRoot": "public"
            }
~~~

* [layer attributes](http://docs.aws.amazon.com/opsworks/latest/APIReference/API_CreateLayer.html#opsworks-CreateLayer-request-Attributes)

~~~json
            "Attributes": {
                "JvmVersion": null, 
                "RailsStack": "apache_passenger", 
                "EnableHaproxyStats": null, 
                "MysqlRootPasswordUbiquitous": null, 
                "NodejsVersion": null, 
                "HaproxyHealthCheckUrl": null, 
                "GangliaPassword": null, 
                "Jvm": null, 
                "HaproxyHealthCheckMethod": null, 
                "RubyVersion": "2.0.0", 
                "HaproxyStatsPassword": null, 
                "MysqlRootPassword": null, 
                "JavaAppServer": null, 
                "MemcachedMemory": null, 
                "JavaAppServerVersion": null, 
                "BundlerVersion": "1.5.3", 
                "PassengerVersion": "4.0.42", 
                "ManageBundler": "true", 
                "HaproxyStatsUrl": null, 
                "HaproxyStatsUser": null, 
                "GangliaUser": null, 
                "JvmOptions": null, 
                "RubygemsVersion": "2.2.2", 
                "GangliaUrl": null
            }
~~~




## AWS OpsWorks CLI and API

Describe stacks:

~~~ bash
aws opsworks describe-layers --region us-east-1 --stack-id 3eb6cdbb-3501-4b21-be1f-dfddf0ef0d94
aws opsworks describe-stacks --region us-east-1 --stack-id 3eb6cdbb-3501-4b21-be1f-dfddf0ef0d94
aws opsworks describe-apps --region us-east-1 --stack-id 3eb6cdbb-3501-4b21-be1f-dfddf0ef0d94
~~~


* Deploy http://docs.aws.amazon.com/opsworks/latest/APIReference/API_CreateDeployment.html

# Auto-healing, load instances, and load balancer

Ref: http://serverfault.com/questions/568384/aws-opsworks-auto-healing-load-instances-and-load-balancer

Autohealing is a feature enabled on a layer basis, for which it applies to all EC2 instances that belong to one layer. The way it works is that if the AWS OpsWorks agent that is installed on every EC2 fails to establish communication with OpsWorks, that instance is terminated and replaced.

http://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-autohealing.html

The checks done by an Elastic Load Balancer are TCP/HTTP based, for which they test connectivity to specific ports, and the action performed by the ELB is that incoming traffic is routed to healthy instances in the layer the ELB is attached to until the unhealthy instance passes the ping test done by the ELB.

http://docs.aws.amazon.com/opsworks/latest/userguide/load-balancer.html

Load balanced instances are instances that are launched when load related triggers that you configure occur. For example you can configure a layer to add a new instance when incoming traffic for that layer makes online instances exceede CPU usage by 80%.

Q: Will an instance that is counted as unresponsive in the load balancer get replaced by the auto healing?
A:  if an instance is considered unhealthy by an ELB, it is not replaced.

## How to test what happens when auto h

This will broke the opsworks health check and the machine will be restarted:

* `mv /opt/aws/opsworks /opt/aws/opsworks_old`
* `service opsworks-agent restart` 

NOTE: the opsworks-agent is monitored by monit `/etc/monit/conf.d/opsworks-agent.monitrc` which restart the service is you try to turn it off from upstart 

# OpsWorks customization

## Security

By default OpsWorks associates the AWS OpsWorks built-in security groups with the stack's layers. These groups open a lot of ports like 80 and 22 to 0.0.0.0/0.

AWS OpsWorks provides a standard set of built-in security groups—one for each layer— which are associated with layers by default. Use OpsWorks security groups allows you to instead provide your own custom security groups. For more information on security groups, see Amazon EC2 Security Groups. Use OpsWorks security groups has the following settings:

* Yes - AWS OpsWorks automatically associates the appropriate built-in security group with each layer (default setting).You can associate additional security groups with a layer after you create it but you cannot delete the built-in security group.

* No - AWS OpsWorks does not associate built-in security groups with layers. You must create appropriate EC2 security groups and associate a security group with each layer that you create. However, you can still manually associate a built-in security group with a layer on creation; custom security groups are required only for those layers that need custom settings.

Cloudformation `AWS::OpsWorks::Stack` option : `UseOpsworksSecurityGroups` boolean


## Extending a Built-in Layer
### Using Chef Deployment Hooks

[Doc](http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook-extend-hooks.html)

Implement one or more Ruby applications and place them in your app's /deploy directory

NB: opsworks_deploy definition internally uses the OpsCode deploy which by default looks into the `deploy` dir, see the [Opscode doc](http://docs.opscode.com/resource_deploy.html#callbacks)

## Creating Custom Layers
http://docs.aws.amazon.com/opsworks/latest/userguide/attributes.html
[HowTo](http://docs.aws.amazon.com/opsworks/latest/userguide/create-custom-deploy.html) app on a custom layer.

[AWS OpsWorks Under the Hood (DMG304) | AWS re:Invent 2013](https://www.youtube.com/watch?v=913oT6xV-Qk)


## Manage a git repo with custom cookbook 

Opsworks support Berkshelf on stack >= 11.10

[AWS doc about Berkshelf](http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook-chef11-10.html)

You must turn on the berkshelf support from setting and include a Berksfile file in your cookbook repository's root directory that specifies which cookbooks to install.

* The built-in cookbooks are installed to `/opt/aws/opsworks/current/cookbooks`
* If your custom cookbook repository contains cookbooks, they are installed to `/opt/aws/opsworks/current/site-cookbooks`
* If you have enabled Berkshelf and your custom cookbook repository contains a Berksfile, the specified cookbooks are installed to `/opt/aws/opsworks/current/berkshelf-cookbooks`
* `/opt/aws/opsworks/current/merged-cookbooks/` : the final merge of the previous three dirs.

A very good idea is to use the environment pattern ( http://blog.vialstudios.com/the-environment-cookbook-pattern/ ) but I've found some problem on OpsWorks, see [this thread for details](https://forums.aws.amazon.com/thread.jspa?threadID=154020).

Actually the guideline is:

* create a structure like this from `addictive-cookbook`: https://bitbucket.org/pitchtarget/addictive-cookbook/src/a68567f2284602ce91e55fa9f0403ca0b8dd705a/README.md?at=master
* NOTE: you need to force cookbook update after they are added to Berksfile.lock. Ex: `berks update addictive-deploy`


* Use the `update_custom_cookbooks` command from the deployment section to update custom cookbooks 

## Override default templates
[Opsworks Custom Templates](http://docs.aws.amazon.com/opsworks/latest/userguide/workingcookbook-template-override.html)

## Rails Layer: Custom and default 

ref: http://www.stefanwrobel.com/heroku-to-opsworks

### Default rails layer

The Rails Layer will add those recipies to the standard set of recipes:

* setup: unicorn::rails
* configure: rails::configure
* deploy: deploy::rails
* undeploy: deploy::rails-undeploy
* shutdown: nginx::stop


#### deploy::rails recipe

~~~ ruby
node[:deploy].each do |application, deploy|

  if deploy[:application_type] != 'rails'
    Chef::Log.debug("Skipping deploy::rails application #{application} as it is not a Rails app")
    next
  end

  opsworks_deploy_dir do
    user deploy[:user]
    group deploy[:group]
    path deploy[:deploy_to]
  end

  opsworks_rails do
    deploy_data deploy
    app application
  end

  opsworks_deploy do
    deploy_data deploy
    app application
  end
end
~~~

This recipe try to deploy all appliction under the deploy key.




#### MISC

for each rails app of the stack 'unicorn::rails' will create opsworks_deploy_user, opsworks_deploy_dir and the unicorn script in this dir "deploy[:deploy_to]}/shared/scripts/unicorn"


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

# Fast debug with the opsworks-agent-cli

We can `opsworks-agent-cli` to run commands directly from an EC2 instance managed by OpsWorks:

* `sudo opsworks-agent-cli list_commands`
* `sudo opsworks-agent-cli run_command update_custom_cookbooks`
* `sudo opsworks-agent-cli run_command execute_recipes <recipe name>`

# Opsworks Cookbook release process 

This the git repo with all the official Opsworks cookbooks: `git@github.com:aws/opsworks-cookbooks.git`

For each chef version there is a branch:

~~~
  release-chef-0.9
  release-chef-11.10
  release-chef-11.4
~~~

When a new version is release they tag the version, if you run the `update_custom_cookbooks` command the last release is deployed.

## Simple strategy to run recipes on a single node

### Rails migration

From what I understand you want to chose one and only one instance to do something special during the deploy. And all instances should agree on which instance this is, right?

As all instances get the same information which nodes are available during the deploy, just create a simple algorithm to agree on which one is the special one, e.g. the first one when sorted by name:

~~~ruby
special_node = node[:opsworks][:layers]['my-layer'][:instances].keys.sort.first
 
if special_node[:hostname] == node[:opsworks][:instance][:hostname] # I'm the special node
  # do stuff, include recipe, etc
else
  # I'm not the special node, do something else
end
~~~

see [here for details](https://forums.aws.amazon.com/thread.jspa?threadID=153158&tstart=0)

### Cron Setup on single node

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


# Debug

/var/lib/aws/opsworks/cache/cookbooks/opsworks_berkshelf/providers/runner.rb

## Opsworks Logs


* `/var/log/aws/opsworks/opsworks-agent.keep_alive.log`
: The agent will send a keep_alive message every minute to the opsworks server
and log here.

* `/var/log/aws/opsworks/opsworks-agent.statistics.log`
: The agent will report the instance status(procs, memory, cpu, load) every minute to the opsworks server
and log here.

* `/var/log/aws/opsworks/installer.log`
: agent install log, created at boot time. Useful to debug custom AMI.

* `/var/log/aws/opsworks/updater.log`
: the agent checks every 10 minute if there are agent updated and log
here.

* `/var/log/aws/opsworks/opsworks-agent.log`
: the agent logs here its start/stop lifecycle and chef run log uploads

* `/var/log/aws/opsworks/opsworks-agent.process_command.log`
: the agent pools the server every minute to check if there are new
commands and logs here. It logs alse the chef solo execution time.

* `/var/log/aws/opsworks/user-data.log`
: TODO

* `/var/lib/aws/opsworks/chef/YYYY-MM-DD-HH-MM-SS.log`
: TODO this should be a single chef run log

* `/var/lib/aws/opsworks/chef/YYYY-MM-DD-HH-MM-SS.json`
: TODO this should be the attribute file



# OpsWorks under the hood
ref: AWS OpsWorks Under the Hood (DMG304) | AWS re:Invent 2013 [video](https://www.youtube.com/watch?v=913oT6xV-Qk) and [slide](http://www.slideshare.net/AmazonWebServices/aws-opsworks-under-the-hood-dmg304-aws-reinvent-2013)

## Chef Server VS OpsWorks (with chef 11.10)

OpsWorks doesn't use chef-server but implements a custom server.

Main differences are:

* Opsworks agent Chef Run are driven by events using a **push model** (see
note below), Chef Server use a periodical run (chef server Enterprise is
an exception, it has push jobs ).
* Opsworks don't have Environments, Encrypted data bag and search as
limited capabilities (see slide 30-40 [here](http://www.slideshare.net/jweiss/chefconf-2014-aws-opsworks-under-the-hood))

OpsWorks use an opswork-agent installed on each instance to talk with
the custom server. The opsworks-agent use the chef-client to execute a
chef-run. The chef-client is a small superset of the chef-solo tool
features, it periodically pools the chef-server and instantiate a
chef run when there is a new update. Opsworks-agent do the same with the Opsworks server.

The main difference between OpsWorks and Opscode ends when the chef-client is started. From that point onwards they behaves the same.

NOTE on push model: the OpsWorks team claim to use a push model but the opsworks-agent.process_command.log has tons of this log "Polling for command to process". It's not a real push model from the implementation point of view. But from an operation point of view you can think it as a push model with a max delay of minute (the actual opsworks polling cycle is 1 minute).

NOTE: previous version of the opsworks stack wraps chef-solo

## OpsWorks AMI and OpsWorks Agent Internals

We have done of hacking on the current version of Opsworks Agent to
understand ho it works (using `ps auxww` when the agent parse  )
Most of the commands execute a custom list of chef recipes, so it's easy
to understand what is going on.

This AMI has the opsworks-agent installed:
wget -O opsworks-agent.tgz https://opsworks-instance-agent.s3.amazonaws.com:443/214/opsworks-agent-installer.tgz


Useful directories:

* `/opt/aws/opsworks/` : directory with chef and opsworks binaries and
cookbooks
* `/opt/aws/opsworks/current/bin/chef_command_wrapper.sh` : a wrapper to
execute chef commands and save logs




When a command is executed by the opsworks-agent it will trigger a
chef-zero run

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


### update_custom_cookbooks Command 

This command will trigger the execution of a list of recipe (the -o
option override the run_list). This are the most intersting:

* opsworks_custom_cookbooks::update: download all cookbook into
different dirs.
* opsworks_custom_cookbooks::load: merge all cookbooks sources
* opsworks_berkshelf::install use `berks vendor` to install cookbooks
* [opsworks_custom_cookbooks](https://github.com/aws/opsworks-cookbooks/tree/release-chef-11.4/opsworks_custom_cookbooks)
* [opsworks_berkshelf](https://github.com/aws/opsworks-cookbooks/tree/master-chef-11.10/opsworks_berkshelf)


~~~bash
/opt/aws/opsworks/current/bin/lockrun --wait --verbose --lockfile /var/lib/aws/opsworks/lockrun.lock -- env HOME=/root sudo /opt/aws/opsworks/current/bin/chef_command_wrapper.sh -s /opt/aws/opsworks/current/bin/chef-client -j /var/lib/aws/opsworks/chef/2014-06-09-14-41-54-01.json -c /var/lib/aws/opsworks/client.rb -o opsworks_custom_cookbooks::update,opsworks_custom_cookbooks::load,opsworks_custom_cookbooks::execute -L /var/lib/aws/opsworks/chef/2014-06-09-14-41-54-01.log -A \n---\n 2>&1
~~~



### Log Example

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




#APPENDIX A: Deploy json example

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
        "elb-load-balancers": [],
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
