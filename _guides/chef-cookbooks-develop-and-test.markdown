---
layout: post
title: "Chef cookbooks development and test"
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
  gem 'foodcritic', '~> 4.0'
  gem 'berkshelf', '~> 3.1'
  #gem 'thor-foodcritic', '~> 1.1.0'
  gem 'test-kitchen', '~> 1.2'
  gem 'kitchen-vagrant', '~> 0.14'
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

set the Rakefile

~~~
require 'foodcritic'
task :default => [:foodcritic]
FoodCritic::Rake::LintTask.new do |t|    ### the block can be omitted if don't have options to pass
  t.options = {:fail_tags => ['correctness']}
end
~~~


Create the application cookbook with berkshelf and copy.

~~~
berks cookbook prova ## optionally: --pattern=environment
~~~

The new cookbook will contains 


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

When you develop a cookbook follow a pattern

## Cookbook Debug

### Recipe Log
A recipe can write events to a log file and can cause exceptions using Chef::Log. The levels include debug, info, warn, error, and fatal. For example, to just capture information:

~~~
Chef::Log.info('some useful information')
~~~

Or to trigger a fatal exception:

~~~
Chef::Log.fatal!('something bad')
~~~

### Ruby Debugger

[Tutorial](http://mharrytemp.blogspot.it/2012/11/non-destructive-debugging-of-chef.html)


~~~
export PATH=/opt/chef/embedded/bin:$PATH
gem install debugger
rdebug  -- /usr/bin/chef-solo -c /tmp/vagrant-chef-1/solo.rb -j /tmp/vagrant-chef-1/dna.json
break  /tmp/vagrant-chef-1/chef-solo-1/cookbooks/nodejs/recipes/default.rb:20
~~~

### Opswork Debug Tips
see the opsworks guide

### Chef-Shell

[Chef Shell](http://docs.opscode.com/chef_shell.html)
[Intro on slideshare](http://www.slideshare.net/JulianDunn/an-introduction-to-shef-the-chef-shell)
[Getting Started](https://wiki.opscode.com/display/chef/Getting+Started+with+Shef) : describe how to use chef-shel as and irb console to define resources
[Chef-Shell TIPS](http://stevendanna.github.io/blog/2012/01/28/shef-debugging-tips-1/) : 

*WARNING* : I CANNOT FIND HOW TO LOAD AND DEBUG RECIPES IN SOLO MODE


Commands:

* help
* node.name
* node.run_list
* node.environment
* node.chef_environment  
* node.default : Default Attributes
* node.normal : Normal Attributes
* node.override : Override Attributes
* node.automatic : Automatic Attributes
* node.automatic.cpu
* node.automatic.memory
* node.automatic.fqdn

modes:

* Default prompt
* Attribute mode: attributes_mode
* Recipe mode : recipe_mode
* Run Chef


To debug a chef solo run like the one below:

~~~
/opt/chef/embedded/bin/ruby /usr/bin/chef-solo -c /tmp/vagrant-chef-1/solo.rb -j /tmp/vagrant-chef-1/dna.json
~~~

run chef-shell with the --solo option and the same -j and -c options:

~~~
sudo /opt/chef/embedded/bin/ruby /usr/bin/chef-shell --solo -c /tmp/vagrant-chef-1/solo.rb -j /tmp/vagrant-chef-1/dna.json
~~~

### Resource Error Log Example


~~~bash
Chef::Exceptions::Exec
\----------------------
if [ -f Gemfile ]; then echo 'OpsWorks: Gemfile found - running migration with bundle exec' && /usr/local/bin/bundle exec /usr/local/bin/rake db:migrate; else echo 'OpsWorks: no Gemfile - running plain migrations' && /usr/local/bin/rake db:migrate; fi returned 1, expected 0
---- Begin output of if [ -f Gemfile ]; then echo 'OpsWorks: Gemfile found - running migration with bundle exec' && /usr/local/bin/bundle exec /usr/local/bin/rake db:migrate; else echo 'OpsWorks: no Gemfile - running plain migrations' && /usr/local/bin/rake db:migrate; fi ----
STDOUT: OpsWorks: Gemfile found - running migration with bundle execSTDERR: rake aborted!
Specified 'mysql' for database adapter, but the gem is not loaded. Add `gem 'mysql'` to your Gemfile.
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/activerecord-4.0.4/lib/active_record/connection_adapters/connection_specification.rb:58:in `rescue in resolve_hash_connection'
/home/deploy/.bundler/addictive_api/ruby/2.1.0/gems/activerecord-4.0.4/lib/active_record/connection_adapters/connection_specification.rb:55:in `resolve_hash_connection'
......
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


## Common issues

### Resources from other cookbooks not found

You must add `depends "cookbook_name"` to make LWRP from cookbook_name avai


## Berkshelf
[Homepage](http://berkshelf.com/)
Manage a Cookbook or an Application's Cookbook dependencies. Berkshelf gives users the ability to shy away from their monolithic Chef repositories and treat cookbooks as software projects.


Berkshelf 3.x is the current version as of june 2014
http://misheska.com/blog/2013/06/16/getting-started-writing-chef-cookbooks-the-berkshelf-way/



https://github.com/berkshelf/berkshelf/blob/master/lib/berkshelf/berksfile.rb#L590


### Berksfile

Add the cookbook you need in the Berksfile file, example:

~~~json
source "https://api.berkshelf.com"

cookbook 'mysql'
cookbook 'npm', '~>0.1.5', :git => "https://github.com/balbeko/chef-npm.git"
cookbook 'addictive-devel-box-cookbook', path: 'addictive-devel-box-cookbook'
~~~

Note that:
* 'mysql' cookbook will be get from https://api.berkshelf.com
* 'npm' will honor the version but will download it from the git repo
* 'addictive-devel-box-cookbook' will be got from the local path


If you are working with a chef server you can upload cookbooks with this
command:

~~~
berks upload
git add Berksfile.lock
git commit
~~~

Q: What happens when you add a dependent cookbook both on the Berksfile and the metadata.rb?
A: Not sure but I think the Berksfile will override the metadata.rb
info, I suppose the best solution is use the metadata when you can. If
you need the Berksfile capability (group, path, git, etc) use the
Berksfile.
TODO: read this discussion
* https://github.com/berkshelf/berkshelf/issues/166
* https://github.com/sethvargo/community-zero


### Berksfile.lock

Is used to freeze the resolved cookbook depency graph. It is used by:

* berks vendor
* berks apply

for implmentation details see:

* https://github.com/berkshelf/berkshelf/blob/master/lib/berkshelf/berksfile.rb#L590
* https://github.com/berkshelf/berkshelf/blob/master/lib/berkshelf/berksfile.rb#L370


**Warning** : There is an issue with OpsWorks (stack version 11.10), you cannot add a
single cookbook with Berksfile.lock, see [this thread](https://forums.aws.amazon.com/thread.jspa?threadID=154020&tstart=0)


## The berkshelf VISION

The berkshelf vision is a set of recommandations, tools and patterns to
make working with chef easier. The Chef Conf 2013 talk by Jamie Winsor
is a good starting point to uderstand the basic concepts.

References:

* [Data Driven Cookbooks, No roles, less data_bags](https://www.youtube.com/watch?v=hYt0E84kYUI#t=21m20s)
* [Create a cookbook for every service or application you have, use pattern](https://www.youtube.com/watch?v=hYt0E84kYUI#t=17m00s)
  * work in vertical from the outside-in: whats is my futhest endpoint?
  service and applications
  * create a cookbook for every application or service you have
  * service/apps are made of components (app servers, cache servers,
  database servers, background workers, etc)
  * use pattern on the above structure
* [Application cookbook pattern, MyFace example](https://www.youtube.com/watch?v=hYt0E84kYUI#t=18m40s)
* [Environment cookbook pattern]()
  * the environment looks like a good pattern to apply with a chef server, not sure if 
  * [Make deployment part of your build process](http://www.slideee.com/slide/atmosphere-2014) slide 48

* Jamie winsor chefconf2013 [Library cookbook pattern](https://www.youtube.com/watch?v=hYt0E84kYUI#t=28m50s)
* Jamie winsor chefconf2013 [Wrapper cookbook pattern](https://www.youtube.com/watch?v=hYt0E84kYUI#t=29m38s)
* NB: the vagrant berkshelf plugin will be replaced by the test-kitchen
workflow (2014)
* Use [Short iteration loop](https://www.youtube.com/watch?v=hYt0E84kYUI#t=31m)


* Jamie winsor chefconf2014 [self contained release](https://www.youtube.com/watch?v=Dq_vGxd-jps#t=10m30s)

A self contained release is something that provide everything you need
to install the software:

  * Software artifact (ex: berkshelf-api.tar.gz)
  * Cookbook artifact (ex: berkshelf-cookbooks.tar.gz)
  * Installation | Update | Configuration Docs

You should produce this 3 thing, with those you can:

  * Build a new environment with a specific version
  * Upgrade pre-existing environments
  * Promote through logical environments (dev, stage, production)

Automation is dangerous unless:

* it is portable
* it is repeatable
* it is predictable

Artifacts should be available on an artifact server, for example:

* Github [releases](https://help.github.com/articles/creating-releases): provide organized release notes, as well as links to binary files or the source code.
* Sonatype's nexus
* Artifatory
* NIC: may s3 could make sense?

To build the software artifact:

* Bump version
* Compile with dependencies
* Test
* Package into an archive (myapp.tar.gz)

To build the cookbook artifact:

* the cookbook must follow the enviroment pattern
* the cookbook must share the same version of the code
* The cookbook should reside into the same repository of the code
because to make easier to share the same version of the code.
[Example](https://github.com/berkshelf/berkshelf-api/tree/master/cookbook)

TODO: how to read the version and compile it into the metadata.rb,
minute 20:00. 

* Jamie winsor chefconf2014: solve the distribution problem
[Blo](https://www.youtube.com/watch?v=Dq_vGxd-jps#t=26m30s):
  * **WARNING** it's an experimental 
  * blo is a super simple tool that replace some features of knife
  * blo install https://...../cookbooks.tar.gz
  * https://github.com/reset/berkflow



* A proposed solution to Winsor point of view about roles: [Role are not evil](http://www.getchef.com/blog/2013/11/19/chef-roles-arent-evil/)


The main reference of this paragraph are:

* [Test MyFace example app with test-kitchen](http://misheska.com/blog/2013/08/06/getting-started-writing-chef-cookbooks-the-berkshelf-way-part3/)
* [add Mysql to MyFace](http://misheska.com/blog/2013/06/23/getting-started-writing-chef-cookbooks-the-berkshelf-way-part2/)
* [MyFace Application Cookbook tutorial](http://vialstudios.com/guide-authoring-cookbooks.html) : will show how to create and debug a
* http://alluvium.com/blog/2013/05/03/the-application-cookbook-pattern-berkshelf-and-team-chef-workflow/



berks cookbook wrapper  --pattern wrapper
These cookbooks follow the naming convention {organization}-{wrapped_cookbook} or even sometimes {application}-{wrapped_cookbook}. So the postgresql cookbook for the company Vialstudios would be called vialstudios-postgresql.
Wrapper cookbooks depend on Application Cookbooks only. They do not depend on other Wrapper Cookbooks, Library Cookbooks, or Environment Cookbooks.



The Chef Environments that an Environment Cookbook manages should follow the naming convention {cookbook_name}-{environment_name} where {cookbook_name} matches that of the Environment Cookbook and {environment_name} is what you would have probably called this environment in the past. Something like dev, staging, preview, or production.


Berkshelf is not only a tool but also a set of best practices and
patterns.


metadata.rb is very important, it contains:

* name of the cookbook (it's optional but if you don't set it chef will
use the name of the cookbook directory, which can change on different
workstations)
* the version of the cookbook (follow [semver.org!](http://semver.org))
* supported OS
* coookbook you depends on


Application are made of component, ex:

* Loadbalancer
* Application server proxy
* Caching service
* Application server
* Background workers
* Database servers

Pattern:
1 cookbook  <-> 1 component

Map each component into a recipe

* The Application MyFace -> myface::default
* Load balancer  -> myface::load_balancer
* Application server proxy  -> myface::app_proxy
* Caching service  -> myface::cache_server
* Application server -> myface::app_server
* Background workers -> myface::worker_pool
* Database servers -> myface::database_server


Creat/Use DATADRIVEN Cookbooks:

* you can change the cookbook behavior using configurable values (attributes, encrypted data bags, data bags)
* helps to don't fork cookbooks and get out of sync with upstream


## Patterns

### ANTI Patterns


[see here](http://www.getchef.com/blog/2014/02/03/evolution-of-cookbook-development/)


* Composing URLs from multiple local variables or attributes
* Large conditional logic branches like case statements in recipes
* Not using definitions when it is best to do so
* Knowledge of how node run lists are composed for search, or searching for “role:some-server”
* Repeated resources across multiple orthogonal recipes
* Plaintext secrets in attributes or data bag items


### Application Cookbook Pattern (The Berkshelf Way)

First you must follow this [getting stared](#getting-started-for-monkeys-create-an-application-cookbook) to create a basic setup.

This pattern is opinionated, it doesn't use roles because they are not
versioned with the cookbook itself, here you can learn more about the
question:


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

