---
layout: post
title: "Develop and Test Chef Cookbooks"
date: 2014-03-10 10:08:28 +0100
comments: true
published: false
categories: [chef, "test-kitchen"] 
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# Getting started for monkeys: create an application cookbook

This guide will introduce you to cookbook development, a basic knowledge
of chef is required. This first paragraph is a quick getting started
that makes you ready in 15 minutes. The [Cookbook development](#cookbook-developement) paragraph will discuss each
step.

Fist start with and new gemset and this Gemfile to be sure you will not
have conflicts or compatibility issues.

~~~ruby
source 'https://rubygems.org'

group :integration do
  #gem 'foodcritic', '~> 3.0.0'
  gem 'foodcritic', :git => 'https://github.com/AudaxHealthInc/foodcritic.git',  :branch => 'relax_nokogiri' # fork of 3.0.3 to fix dependency issue
  gem 'thor-foodcritic', '~> 1.1.0'
  gem 'berkshelf', '~> 2.0.14'
  gem 'test-kitchen', '~> 1.2.1'
  gem 'kitchen-vagrant', '~> 0.14.0'
end
~~~

~~~
rvm --create --versions-conf use  ruby-2.1.0@mycookcook_dev_env
bundle install
~~~

Finally you need to install this VirtualBox and Vagrant, tested versions
are:

* VirtualBox 4.3.6
* Vagrant [1.5.3](https://dl.bintray.com/mitchellh/vagrant/vagrant_1.5.3.dmg)
* vagrant-berkshelf  2.0.0.rc3

~~~
vagrant plugin install vagrant-berkshelf --plugin-version 2.0.0.rc3
vagrant plugin install vagrant-omnibus
~~~

set the Thorfile:

~~~
# encoding: utf-8

require 'bundler'
require 'bundler/setup'
require 'berkshelf/thor'

begin
  require 'kitchen/thor_tasks'
  Kitchen::ThorTasks.new
rescue LoadError
  puts ">>>>> Kitchen gem not loaded, omitting tasks" unless ENV['CI']
end

begin
  require 'thor/foodcritic'
  ThorFoodCritic::Tasks.new
rescue LoadError
  puts ">>>>> thor-foodcritic gem not loaded, omitting tasks" unless ENV['CI']
end
~~~

Create the application cookbook with berkshelf and install the vagrant
plugin for berkshelf



set .kitchen.yml to:

~~~yaml
---
driver:
  name: vagrant

provisioner:
  name: chef_zero

platforms:
  - name: ubuntu-12.04
    driver:
      box: opscode_ubuntu-12.04_chef-provisionerless
      box_url: http://opscode-vm-bento.s3.amazonaws.com/vagrant/virtualbox/opscode_ubuntu-12.04_chef-provisionerless.box

suites:
  - name: default
    run_list:
      - recipe[test-cookbook::default]
      attributes:
~~~

Set ubuntu as vagrant box into the Vagrantfile:

~~~
  config.vm.box = "opscode_ubuntu-12.04_chef-provisionerless"
  config.vm.box_url = "http://opscode-vm-bento.s3.amazonaws.com/vagrant/virtualbox/opscode_ubuntu-12.04_chef-provisionerless.box"
~~~

NB: "http://opscode-vm-bento.s3.amazonaws.com/vagrant/virtualbox/opscode_ubuntu-12.04_chef-provisionerless.box has addition for virtualbox 4.3.8 OSX host

smoking test to check if the kitchen can boot the virtual machine:
`kitchen converge`

~~~bash
name             'test-cookbook'
maintainer       'YOUR_NAME'
maintainer_email 'YOUR_EMAIL'
license          'All rights reserved'
description      'Installs/Configures test-cookbook'
long_description IO.read(File.join(File.dirname(__FILE__), 'README.md'))
version          '0.1.0'

%w{ postgresql }.each do |dep|
  depends dep
end

~~~

check if you cookbook are uploaded into your instance at: `/tmp/kitchen/cookbooks`

Add your fist test in `test/integration/default/my_first_test.rb`

# Foodcritic

[Homepage](http://acrmp.github.io/foodcritic/)
http://dracoater.blogspot.it/2013/09/testing-chef-cookbooks-part-1-foodcritic.html

# Test Kitchen

Test Kitchen is designed to:

* automate the testing process of chef cookbooks (not infrastucture! see )
* plug into a CI server workflow
* execute on one or more platforms (ubuntu, centos, etc) and cloud providers (AWS, Digital
  Ocean, etc) in isolation, ensuring that no prior state exists.
* support any testing frameworks are already supported out of the box including Bats, shUnit2, RSpec, Serverspec, with others being created weekly.
* support cookbook dependency resolver like Berkshelf and Librarian-Chef

Test Kitchen has a simple workflow that stresses speed but optimizes for the freshness of your code executing on the remote systems between tests. It has a static, declarative configuration in a .kitchen.yml file at the root of your project.

Platforms are supported by a plugin architecture.

Resources:

* [Book](http://shop.oreilly.com/product/0636920020042.do)
* [Kitchen HomePage](http://kitchen.ci/)
* [Kitchen Drivers](https://rubygems.org/search?utf8=%E2%9C%93&amp;query=kitchen-)
* [Kitchen Busser Plugins](https://rubygems.org/search?utf8=%E2%9C%93&amp;query=busser-)

## TODO

* Chefspec
* Serverspec
* Guard:  https://github.com/test-kitchen/guard-kitchen
* Busser: https://github.com/test-kitchen/busser-serverspec 

* IDEA: Use `kitchen converge` to provision an application container,
  save it as image, run `kitchen verify` if everything is ok push the
container in production. 


## Setup a project with Test Kitchen: Init and basic concept
This is the [official getting started](http://kitchen.ci/docs/getting-started/creating-cookbook)
Here there a is a summary.

`kitchen init --driver=kitchen-vagrant` will create a
basic `.kitchen.yml`

~~~yaml
driver:
  name: vagrant

provisioner:
  name: chef_zero

platforms:
  - name: ubuntu-13.04
  - name: centos-6.5

suites:
  - name: client
    run_list:
      - recipe[postgresql::client]
  - name: server
    run_list:
      - recipe[postgresql::server]
~~~

* `driver`: the component that is responsible for creating a machine that we'll use to test our cookbook. Each Driver is implemented in a separate plugin gem `kitchen-<platform_name>`
* `provisioner`: This tells Test Kitchen how to run Chef, to apply the code in our cookbook to the machine under test ( `chef-solo`, `chef-zero`, etc).
* `provisioner`: 
* `platforms`: This is a list of operation systems on which we want to run our code. Note that the operating system's version, architecture, cloud environment, etc. might be relevant to what Test Kitchen considers a **Platform**.
* `suites`: This section defines what we want to test.  It includes the Chef run-list and any node attribute setups that we want run on each **Platform** above. For example, we might want to test the MySQL client cookbook code seperately from the server cookbook code for maximum isolation.
* `instance` A Test Kitchen Instance is a pairwise combination of a Suite and a Platform as laid out in your .kitchen.yml file. Test Kitchen has auto-named your only instance by combining the Suite name ("default") and the Platform name ("ubuntu-12.04") into a form that is safe for DNS and hostname records, namely "default-ubuntu-1204".

## Write Test: busser and the suites stanza

Busser is the component that helps facilitate testing on your instances,
it's a ruby gem.
Busser has a plugin based architecture (busser-bats, etc).

To create a test suite you need to create:

* An entry in the suite stanza of .kitchen.yml
* One (or more? ) input file for the busser plugin you are using

input file must be created following this naming convention:

* test/integration: Test Kitchen will look for tests to run under this directory. It allows you to put unit or other tests in test/unit, spec, acceptance, or wherever without mixing them up. This is configurable, if desired.
* < suite name > : This corresponds exactly to the Suite name we set up in the .kitchen.yml file. If we had a suite called "server-only", then you would put tests for the server only suite under test/integration/server-only.
* < busser plugin > : This tells Test Kitchen (and Busser) which Busser runner plugin needs to be installed on the remote instance. For example the bats directory name will cause Busser to install busser-bats from RubyGems.

~~~bash
mkdir test/integration/< suite name >/< busser plugin >
~~~

~~~yaml
---
driver:
  name: vagrant

provisioner:
  name: chef_solo

platforms:
  - name: ubuntu-12.04
    driver:
      box: opscode-ubuntu-12.04
      box_url: https://opscode-vm-bento.s3.amazonaws.com/vagrant/opscode_ubuntu-12.04_provisionerless.box

suites:
  - name: < suite name >
    run_list:
      - recipe[git::default]
    attributes:
~~~

 

A Suite is a Chef run_list and attribute hash that will be used in a convergence action Your test will be runned after the provising step.
NB: also a platform in the platforms stanza can define a run_list, this
list will be merged with the suite run_list and can affect you test!

`kitchen verify INSTANCE` freshly uploading all your tests files and execute test????

`kitchen test` is a shortcut that  run this actions in sequence: destroy,
  converge, setup, verify, destroy. It is useful for CI server.
with the `--destroy' flag you can change the behavior of the last destroy step:

* passing: instances passing verify will be destroyed afterwards.
* always: instances will always be destroyed afterwards.
* never: instances will never be destroyed afterwards. 




Parameters:

    options (Hash) (defaults to: {}) —

    configuration for a new suite

Options Hash (options):

    :name (String) —

    logical name of this suit (Required)
    :run_list (String) —

    Array of Chef run_list items (Required)
    :attributes (Hash) —

    Array of names of excluded platforms
    :data_bags_path (String) —

    path to data bags
    :roles_path (String) —

    path to roles
    :encrypted_data_bag_secret_key_path (String) —

    path to secret key file

### Configure DataBags and Attributes of a suite

TODO: HOW TO DATA BAGS


### Exclude a Platform from a suite
Use the excludes attribute of a suite, in this example we exclude the
centos-6.4 platform from the "server" suite 

~~~yaml
platforms:
  - name: ubuntu-12.04
  - name: ubuntu-10.04
  - name: centos-6.4

suites:
  - name: server
    run_list:
      - recipe[git::server]
    attributes:
    excludes:
      - centos-6.4
~~~



### ChefSpec Busser Plugin
https://github.com/sethvargo/chefspec


### ServerSpec Busser Plugin

* [ServerSpec Home](http://serverspec.org)
* [ServerSpec Reference](http://serverspec.org/resource_types.html)
* [ServerSpec Tutorial](http://dustinrcollins.com/chef-integration-testing-with-serverspec)
* [Example Specs](https://github.com/dustinmm80/serverspec-example/tree/master/test/integration/mongorabbit/serverspec)


### Example Git Server

First we need to define acceptance criteria:

* A process is listening on port 9418 (the default Git daemon port).
* A service is running called "git-daemon". This name is arbitrary but shouldn't surprise anyone using this cookbook.

## Cookbook dependency management with Berkshelf

If you have a Berksfile in your project directory Test Kitchen will use Berkshelf to resolve dependencies.

Install the berkshelf gem and create a basic Berksfile:

~~~ruby
site :opscode

metadata
~~~

add the cookbook you depend on to the metadata.rb file (ex: the runit cookbook):

~~~
name "git"
version "0.1.0"

depends "runit", "~> 1.4.0"
~~~

## Driver

### Vagrant and Test Kitchen command reference

[Here](https://github.com/test-kitchen/kitchen-vagrant) you can find the kitchen-vagrant drive documentation.


| Vagrant command                           | Test Kitchen command          |                                          |
| ----------------------------------------- |:-----------------------------:| ----------------------------------------:|
| `vagrant ssh [vm-name]`                   | `kitchen login INSTANCE`      | Log in to one machine                    |
| `vagrant destroy [vm-name]`               | `kitchen destroy INSTANCE`    | Destroy machine                          |
| `vagrant up [vm-name]` --no-provision     | `kitchen converge INSTANCE`   | Create a machine without provisioning it |

Test Kitchen only commands:

* `kitchen verify INSTANCE` : 
* `kitchen setup INSTANCE`: this action is responsible for installing the Busser RubyGem and any test runner plugins required.
* `kitchen test INSTANCE` : run this actions in sequence destroy,
  converge, setup, verify, destroy
* `kitchen list` : list all instances
* `kitchen diagnose` : print

When you use the kitchen-vagrant driver the converge action will save
the vagrant status in the `.kitchen` directory:

~~~bash
.kitchen
├── default-centos-64.yml
├── default-ubuntu-1204.yml
└── kitchen-vagrant
    ├── default-centos-64
    │   └── Vagrantfile
    └── default-ubuntu-1204
        └── Vagrantfile
~~~

The vagrant driver can be configured on a global stanza or per platform:

~~~
TODO
~~~



## Provisioner

[List of available provisioner on master](https://github.com/test-kitchen/test-kitchen/tree/master/lib/kitchen/provisioner)

### Chef-Solo
It's the default it works out of the box.

### Chef-Zero
TODO : http://blog.nistu.de/2013/09/21/getting-started-with-test-kitchen

gem 'chef-zero'

provisioner: chef_zero

## Examples: cookbooks using Test Kitchen

* [cookbook mysql](https://github.com/opscode-cookbooks/mysql)
* [cookbook nginx](https://github.com/opscode-cookbooks/nginx)
* [cookbook chef-server](https://github.com/opscode-cookbooks/chef-server)
* [cookbook runit](https://github.com/hw-cookbooks/runit)


# Leibniz
Test Kitchen was *not* designed for acceptance testing of infrastructure stacks.
Instead [Leibniz](http://leibniz.cc/) is simple utility which provides 
the ability to launch infrastructure using Test Kitchen


# Cookbook Developement

When you develop a cookbook follow a pattern:
* Application pattern (The berkshelf way)
* Library cookbook pattern (https://www.youtube.com/watch?v=hYt0E84kYUI
minute 28:00)
* Wrapper cookbook pattern (https://www.youtube.com/watch?v=hYt0E84kYUI
minute 29:40)


## Application Cookbook Pattern (The Berkshelf Way)

First you must follow this [getting stared](#getting-started-for-monkeys-create-an-application-cookbook) to create a basic setup.

This pattern is opinionated, it doesn't use roles because they are not
versioned with the cookbook itself, here you can learn more about the
question:

* [The berkshelf way](https://www.youtube.com/watch?v=hYt0E84kYUI) at
minute 25:00
* A proposed solution [Role are not evil](http://www.getchef.com/blog/2013/11/19/chef-roles-arent-evil/)


The main reference of this paragraph are:

* [The berkshelf way](https://www.youtube.com/watch?v=hYt0E84kYUI)
* [Test MyFace example app with test-kitchen](http://misheska.com/blog/2013/08/06/getting-started-writing-chef-cookbooks-the-berkshelf-way-part3/)
* [add Mysql to MyFace](http://misheska.com/blog/2013/06/23/getting-started-writing-chef-cookbooks-the-berkshelf-way-part2/)
* [MyFace Application Cookbook tutorial](http://vialstudios.com/guide-authoring-cookbooks.html) : will show how to create and debug a
* http://alluvium.com/blog/2013/05/03/the-application-cookbook-pattern-berkshelf-and-team-chef-workflow/

The key priciple of this cookbook pattern are:
* It’s a solid best practice to separate your **applications components into their own recipes** and avoid the use of roles.
* Use a Vagrantfile and the default recipe to quickly boot your app
(vagrant up and you should have your app running)
* Use test-kitchen to test your cookbook


It’s easier to develop and test components when they are separate. This is a good time to bring up the Single Responsibility Principle (SRP).
Each recipe should do the job of installing or configuring a single component - nothing more, nothing less.
Enables you to distribute components across different nodes without including unnecessary components.

The Vagrant file is configured to provision the VM with chef_solo and
the default recipe. The vagrant-berkshelf plugin will manage the
cookbook vendoring and make them available to chef-solo, saving you a
lot of truble (NB: on production you have to manage those step by your
onw!). The omnibus plugin install chef on the provisioned machine.


For example we refactored the placecommander application cookbook. In
the previous version eve

~~~
recipes/
default.rb
frontend.rb
memcache.rb
postgres.rb
redis.rb # install the redis server configured for
workers.rb
~~~

The defaul recipe will include all the needed component:

~~~
include_recipe 'placecommander::frontend'
include_recipe 'placecommander::workers'
include_recipe 'placecommander::memcache'
include_recipe 'placecommander::redis'
include_recipe 'placecommander::postgres'
~~~

The redis configuration is created with a file template:
templates/default/zips.conf.erb




All placecommander node attributes are scoped within the placecommander key, this is usefull to avoid clash of attributes on node with more than an application and also on OpsWorks global stack json:

~~~
default[:placecommander][:backup_redis][:bucket_name]
~~~

This approach cannot be used with the FungoStudios cookbook and backup
cookbook because they look for variables here:

~~~json
{
  "backup": {
    "user": "ubuntu",
    "group": "ubuntu",
    "dependencies": [["fog", "1.4.0"]]
  },
  "rvm": {
    "default_ruby": "1.9.3"
  },
  "backup_redis": {
    "bucket_name": "backup-redis-dolcetti"
  },
  "run_list":["recipe[rvm::gem_package]", "recipe[backup]", "recipe[backup_redis]"]  ->>>##### Questo l'ho spostato nella recipe di redis
}



{
  "redis": {
    "config_dir": "/etc/redis",
    "data_dir": "/var/lib/redis",
    "log_dir": "/var/log/redis",
    "user": "redis",
    "port": 6379,
    "bind_address": "127.0.0.1",
    "remove_build_essential": true,
    "remove_wget": true,
    "start_server": true,
    "include_files": ["/etc/redis/zips.conf"],
    "version": "2.6.12"
  },
  "run_list":["recipe[install_redis]"]
}

~~~

The placecommander::redis recipe contains also the backup configuration, this is a design choice, it make easy to deploy the redis component without worries.
To backup redis we use the backup cookbook.


Opsworks deploy scenario:



TODO:
* how should we document that an attribute is required ? For example the
AWS key of the redis backup is required and we also need a way to
validate it..
* how should we verify our backup ?
* togliere le chiavi di accesso dai parametri di default
* REDIS address: ho

Best practice:
* The application cookbook should document how to distribute different
component on a multi node architecture and how to deploy on a single
instance.

### Check List

Always run thor `foodcritic:lint` before commit

## Cookbook deployment
Finally when the cookbook is ready we can deploy it with chef-solo,
chef-server or aws opsworks.

TODO: explain how to deploy on different scenarios
TODO: azure scenario
TODO: Vagrant scenario
TODO: Opsworks scenario
TODO: integration test with test kitchen




# CHANGELOG and VERSIONS
This guide is based on:

* Test Kitchen version 1.2.1

