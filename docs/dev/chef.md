---
layout: post
title: "chef"
date: 2014-03-16 19:59:15 +0100
comments: true
categories:
---
# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# Chef Intro


## Chef Main Concepts

chef client




* [Opscode Intro to Chef Server](http://gettingstartedwithchef.com/introducing-chef-server.html)
* [Chef Antipattern](http://www.getchef.com/blog/chefconf-talks/beginning-chef-antipatterns-julian-dunn/?__hstc=153815783.048d0d0a3f1e4720305d2b1f1091e434.1393768736811.1396000075578.1396039585392.12&__hssc=153815783.1.1396039585392&__hsfp=4176093744)
* [Chef Shelf Intro](http://www.slideshare.net/JulianDunn/an-introduction-to-shef-the-chef-shell)


## Chef Public and Private Keys

[Chef Doc](http://docs.opscode.com/chef_private_keys.html)

Where should we store keys?
When we download a started kit two keys are provided: username.pem and
organization-validator.pem

organization-validator.pem is required to bootstrap a new node. Should
we distribute it to every workstation that need to bootstrap a node?

The username.pem is personal and should not be shared among users.


## Install Chef Server

http://leopard.in.ua/2013/02/17/chef-server-getting-started-part-1/

## Install Chef on workstation

ref:
* [Official Opscode doc](https://learnchef.opscode.com/quickstart/workstation-setup/)


### Setup a chef-repo to manage multiple organizations

We will adopt a multi organizations approach using rvm.
Every organization have a repository where roles, cookbooks, nodes are stored see the [doc](http://docs.opscode.com/essentials_repository.html).
We create this repository from the new chef starter kit and we store a knife.rb that will read the configuration from the enviroment. To load env variables we use rvm. To work with chef on a given organization you must chdir into this repository and run knife from there.


To setup a new organization sign up for a free Hosted Enterprise Chef account and download the Starter Kit or Alternatively if already signed up and you lost the starter kit. Login and navigate to preview.opscode.com/organizations, Select your organization in the middle of the page. Click the "Starter Kit" link on the left.
The started kit replaces the old procedure of cloning the chef-repo from opscode github.
WARNING: the starter kit is a sensible data, it contains your pem keys into the .chef directory, do NOT SHARE PEM keys.
TODO: how to setup your own chef server

uncompress the zip into ~/CHEF_ORGANIZATIONS/your-organization
cd  ~/CHEF_ORGANIZATIONS/your-organization
git init
rm -rf roles/starter.rb cookbooks/starter

git add * .chef/knife.rb .gitignore

Lock the ruby version, setup an isolated gemset and lock gems.
rvm --create --versions-conf use ruby-2.1.0@your-organization

append env variables into: .versions.conf

~~~
ruby=ruby-2.1.0
ruby-gemset=fungostudios-chef-repo
#ruby-gem-install=bundler rake
#ruby-bundle-install=true
env-CHEF_USERNAME=opscode_pc
env-CHEF_ORGNAME=placecommander
env-AWS_ACCESS_KEY_ID=replace
env-AWS_SECRET_ACCESS_KEY=replace
env-RACKSPACE_USERNAME=replace
env-RACKSPACE_API_KEY=replace


# Chef Provisioning for orchestration

NB: Chef Metal has been renamed from chef-metal to chef-provisioning
since [version 0.15](https://github.com/opscode/chef-provisioning/blob/v0.15/CHANGELOG.md)

Intro: https://www.getchef.com/blog/2014/11/12/chef-provisioning-infrastructure-as-code/

Chef provisioning drivers for:

* [Aws](https://github.com/opscode/chef-provisioning-aws)
* [Fog](https://github.com/opscode/chef-provisioning-fog)
* [Azure](https://github.com/opscode/chef-provisioning-azure)
* [Docker](https://github.com/opscode/chef-provisioning-docker)
* [Vagrant](https://github.com/opscode/chef-provisioning-vagrant)

If you are working with chefDK you need to install this driver, ex: `chef gem install chef-provisioning-docker`

~~~
Sto testando qua:  /devel/SRC/DOCKER/CHEF_PROVISIONING
CHEF_DRIVER=docker chef-client -z docker_ubuntu_image.rb
~~~


Known issue "Could not find the file /etc/chef/client.pem in container" : https://github.com/opscode/chef-provisioning-docker/issues/13

# Chef Init

PID1 for your Chef containers

https://github.com/opscode/chef-init

## Test Clusters with Test Kitchen

Chef Provisioning also works with Test Kitchen, allowing you to test
entire clusters.
The repository for the kitchen-metal gem is https://github.com/doubt72/kitchen-metal.

env-AZURE_SUBSCRIPTION_ID=replace   #azure

env-AZURE_MGMT_CERT=replace
evn-AZURE_API_HOST_NAME=replace

env-AWS_ACCESS_KEY_ID=replace       #aws
env-AWS_SECRET_ACCESS_KEY=replace
~~~

cp .versions.conf .versions.conf_sample
echo ".versions.conf" >> .gitignore



We copy version into .versions.conf.sample because we will use the rvm support for loading env variables when you chdir and some of them are user dependent.
EX: You can add the ORGNAME env variable adding this line: env-ORGNAME=variable_value

Gemfile:

~~~ruby
source 'https://rubygems.org'

gem 'chef', '11.10.4'
gem 'berkshelf', '~> 2.0'

gem 'knife-ec2'       #AWS

gem 'knife-azure'     #azure
gem 'knife-windows
~~~


bundle install
git add Gemfile Gemfile.lock


Change the .berkshelf/config.json config removing the chef key so it will read the knife config we just created

~~~json
{
  "vagrant": {
    "vm": {
      "box": "opscode-ubuntu-12.04-i386",
      "box_url": "https://opscode-vm.s3.amazonaws.com/vagrant/opscode_ubuntu-12.04-i386_provisionerless.box",
      "provision": "chef_client"
    }
  }
}
~~~

backup your pem:

~~~
cd .chef
gpg -c placecommander-validator.pem
gpg -c opscode_pc.pem
mkdir -p ~/Dropbox/FunGoStudiosWallet/CHEF_ORGANIZATIONS/placecommander
mv *.gpg ~/Dropbox/FunGoStudiosWallet/CHEF_ORGANIZATIONS/placecommander
~~~

If you use azure:
https://github.com/opscode/knife-azure

### Setup Other workstations

Draft:
* install rvm
* clone the org repo
* cp .versions.conf_sample .versions.conf
* setup your variable and pem keys
* install ruby if needed and the gemset ()
* bundle install

### Setup knife-azure
This plugin v1.2.2 has issues with ruby 2.x , it works with ruby 1.9.x
but it require this ugly patch because the LOAD_PATH of the gem is
broken:

~~~
/Users/nicolabrisotto/.rvm/gems/ruby-1.9.3-p429@fungostudios-chef-repo/gems/knife-azure-1.2.2/lib/chef/knife/azure_server_create.rb
$:.unshift "/Users/nicolabrisotto/.rvm/gems/ruby-1.9.3-p429@fungostudios-chef-repo/gems/knife-azure-1.2.2/lib"
~~~

another issue that happens is “ nested asn1 error” ?





# Chef Server Tasks

## Bootstrap a node

WARNING: do not bootstrap **Azure** nodes with knife bootstrap but use
the knife-azure plugin, it will store additional attributes like the
public ip of the virtual machine

knife bootstrap -i ~/.ssh/placecommander_azure.key  -x ubuntu pc-frontend.cloudapp.net --sudo


~~~
knife bootstrap -i ~/.ssh/placecommander_azure.key  -x ubuntu pc-frontend.cloudapp.net --sudo
Bootstrapping Chef on pc-frontend.cloudapp.net
pc-frontend.cloudapp.net Starting Chef Client, version 11.10.4
pc-frontend.cloudapp.net Creating a new client identity for pc-frontend.pc-frontend.a5.internal.cloudapp.net using the validator key.
.....
~~~

Now the pc-frontend.cloudapp.net is bootstrapped:

* chef-client is installed
* a new client identity is generated using the validator.pem (see knife
client list)
* a new node is created: pc-frontend.pc-frontend.a5.internal.cloudapp.net

To keep your configuration on revision controll you can download the
json representation of the node and save it into the nodes directory.

~~~
knife node show -F json pc-frontend.pc-frontend.a5.internal.cloudapp.net > nodes/pc-frontend.pc-frontend.a5.internal.cloudapp.net.json
~~~
NB: the json filename is a convention we use the same value of "name"
jsonkey.

When we need to update the node we should not go to the webui but
instead edit the local file and upload it to the server:

~~~bash
vi noded/pc-frontend.pc-frontend.a5.internal.cloudapp.net.json
git add noded/pc-frontend.pc-frontend.a5.internal.cloudapp.net.json &&
git commit -m "..."
knife node from file nodes/pc-frontend.pc-frontend.a5.internal.cloudapp.net.json
Updated Node pc-frontend.pc-frontend.a5.internal.cloudapp.net!
~~~
or to update all nodes in one command:

~~~
knife node from file nodes/*.json
~~~

This is node example:

~~~json
{
   "name": "the_node_name",
   "chef_environment": "_default",
   "json_class": "Chef::Node",
   "automatic": {
   },
   "normal": {
   },
   "chef_type": "node",
   "default": {
   },
   "override": {
   },
   "run_list": [

   ]
}
~~~

## Bootstrap an node on Azure

~~~
knife azure server create -N MyNewNode --azure-vm-size Small -I b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-12_04_3-LTS-amd64-server-20140130-en-us-30GB -m "West Europe" --identity-file ~/.ssh/placecommander_azure_rsa --ssh-user ubuntu
~~~

## Role management

Discussions about chef roles:

* [15 Sep 2014 opscode mailing list](http://lists.opscode.com/sympa/arc/chef/2014-09/msg00144.html)


To create a role called "example_role" create a file
roles/example_role.json

~~~json
{
  "name": "example_role",
  "chef_type": "role",
  "json_class": "Chef::Role",
  "description": "The base role for Chef Server",
  "default_attributes": {
    "chef-server": {
      "api_fqdn": "10.33.33.33",
      "configuration": {
        "chef-server-webui": {
          "enable": true,
          "web_ui_admin_user_name": "admin",
          "web_ui_admin_default_password": "password"
        },
        "nginx": {
          "url": "http://10.33.33.33",
          "enable_non_ssl": true
        },
        "bookshelf": {
          "url": "http://10.33.33.33"
        }
      }
    }
  },
  "run_list": [
    "recipe[chef-server]"
  ]
}
~~~


to upload or update roles on server

~~~
knife role from file roles/*.json
~~~


## Destroy a node

If you are using azure you can delete both the virtual machine and the
chef node with one command:

knife azure server delete MyNewNode --purge

## Run chef client on nodes



On azure you must user `-a` option to get the proper public ip:

~~~
knife ssh -i ~/.ssh/placecommander_azure_rsa -a "azure.public_ip" --ssh-user ubuntu 'name:MyNewNode' 'sudo chef-client'
~~~


# Chef events and execution order

REF: http://frankmitchell.org/2013/02/chef-events/

* Chef executes resources in the order they appear in a recipe.

## Notify Resources

# Attributes

Ref:

* https://www.chef.io/blog/2013/02/05/chef-11-in-depth-attributes-changes/
* https://docs.chef.io/attributes.html

One of the most annoying concept of chef is understanding how to read and write attributes.

An attribute is a specific detail about a node, such as an IP address, a host name, a list of loaded kernel modules, the version(s) of available programming languages that are available, and so on.An attribute may be unique to a specific node or it can be identical across every node in the organization.

Attributes are most commonly set:

* from a cookbook, by using Knife
* or are retrieved by Ohai from each node prior to every chef-client run.

All attributes are indexed for search on the Chef server. Good candidates for attributes include:

* any cross-platform abstraction for an application, such as the path to a configuration files
* default values for tunable settings, such as the amount of memory assigned to a process or the number of workers to spawn
* anything that may need to be persisted in node data between chef-client runs.


## Attributes API

Chef 11 NOTE:

* since chef 11 read and write have been separated syntactically.
* node.default.an_attribute("value") is removed
* order of evaluation: attributes are evaluated in order based on your run list and cookbooks’ dependencies; all of a cookbook’s dependencies appear before it in the final sort order, but the overall order is otherwise controlled by the run list
* https://www.chef.io/blog/2013/02/05/chef-11-in-depth-attributes-changes/


* you must specify which precedence level you want to write to when setting attributes;
* When reading attributes, a merged view of the components is generated.merged attributes are made read-only


* All files in the `attributes/` folder are loaded in order during the start of the Chef Client run, except the `the default.rb` will always be loaded first.


For attributes debug, see: https://www.chef.io/blog/2013/02/05/chef-11-in-depth-attributes-changes/

Attributes are provided to the chef-client from the following locations:

* Nodes (collected by Ohai at the start of each chef-client run)
* Attribute files (in cookbooks)
* Recipes (in cookbooks)
* Environments
* Roles

Api syntax:

* In attributes files the `node` object can be implicit 
* you can use both `node.default["apache"]["dir"] = "/etc/apache2"` and `default["apache"]["dir"] = "/etc/apache2"`


Attributes definition can have different level of priority, based on the type. [See here for a full list of types](https://docs.chef.io/attributes.html#attribute-types):

* `default`
* `normal`
* `set` is an alias of `normal` 
* override
* ...

Write api `node.<TYPE>["foo"]["bar"] = "my value"`:

~~~ruby
node.default["apache"]["dir"] = "/etc/apache2
~~~


Read api:

~~~ruby
file "/tmp/something" do
  ....
  content node["bluepill"]["bin"]
end
~~~

Attributes precedence https://docs.chef.io/attributes.html#attribute-precedence :

* A default attribute located in a cookbook attribute file
* A default attribute located in a recipe
* A default attribute located in an environment
* A default attribute located in role
* A force_default attribute located in a cookbook attribute file
* A force_default attribute located in a recipe
* A normal attribute located in a cookbook attribute file
* A normal attribute located in a recipe
* An override attribute located in a cookbook attribute file
* An override attribute located in a recipe
* An override attribute located in a role
* An override attribute located in an environment
* A force_override attribute located in a cookbook attribute file
* A force_override attribute located in a recipe
* An automatic attribute identified by Ohai at the start of the chef-client run

## Derived attributes



## Attributes in Vagrant

TODO: documentare da qualche parte un parallelo tra un vagrant file con
chef-solo e un node.json, qua c'è un bell'esempio https://gist.github.com/halcyonCorsair/3644826

~~~
  config.vm.provision :chef_solo do |chef|
    chef.json = {
      mysql: {
        server_root_password: 'rootpass',
        server_debian_password: 'debpass',
        server_repl_password: 'replpass'
      }
    }

    chef.run_list = [
        "recipe[placecommander::default]"
    ]
  end
~~~

node.json

~~~json
{
  "mysql": {
    "server_root_password": "rootpass",
    "server_repl_password": "debpass",
    "server_debian_password": "replpass"
  },
  "run_list": [
    "recipe[placecommander::default]"
 ]
}
~~~

# Application Deployment
Every project has its own requirement. Usually most of the deployment
techniques fit in one of this two categories:

* Pull model: the machine periodically poll for new updates
* Push model: the deploy is triggered by an external tool (capistrano
uses this by default)

The push model is good approach when you want to minimize the version
switch duration. But it has a problem when you work in an autoscaling
environment: how do you deploy on a new machine when it boots?

IDEA: I like the push model, the push machine could work as a semaphore,
if a new deploy is in progress, no new machine are admitted into the
pool, when the deploy completes new machine are admitted.

ref:
* [Food Fight Show](http://foodfightshow.org/2013/01/application-deployment.html)

# Application Cookbook Developement

see [Develop and Test Chef Cookbooks](/blog/2014/03/10/develop-and-test-chef-cookbooks/)

# Chef resources

* [Resources doc](http://docs.opscode.com/chef/resources.html)
* [Resource source code](https://github.com/opscode/chef/tree/master/lib/chef/resource)
* [Provider source code](https://github.com/opscode/chef/tree/master/lib/chef/provider)


# Deploy Rails application

ref:

* http://www.concreteinteractive.com/how-to-deploy-a-rails-application-anywhere-with-chef/
*
* https://github.com/poise/application_ruby
* https://github.com/poise/application


TODO:

* https://github.com/yourabi/chef-puma

## Application Cookbook < 4.1.6

NOTE: NOAH KANTROWITZ started in jan 2015 a major refactor of the Application cookbook, see below.

The application cookbook is designed to work with sub-resources.

REF:

* http://nathenharvey.com/blog/2012/12/14/learning-chef-part-3/

TODO:

* review this commit that add a sinatra test app using serverspec https://github.com/poise/application_ruby/commit/a044ed74ae87538d37701fabb07ceacb891dec05


## Design notes

There are a lot of different ways to install Ruby on your server and each of them has pros and cons.  In this example we choose to build Ruby from source, but here are some options and our opinions on their merits:

* RVM/rbenv system-wide or user install. While these tools are really great for development environments because they allow you to manage multiple Ruby installations they are not that great on server side. Both RVM/rbenv require you to setup your shell environment in some ways to be able to manage Rubies for you. That’s simple to do on your development machine – just customize the shell you use. However on server side you run processes as different users and they can be invoked from different scripts. For example you have monit/runit or just init.d script that runs your app server that’s usually started as root, then you have tasks invoked by cron by a different user and then you probably have your deploy user running tasks like db:migrate. You need to make sure everything is RVM/rbenv aware.
* apt/yum package – installs Ruby system-wide. Packages are usually pretty old so you cannot use latest Ruby versions. It’s possible to have multiple rubies but you can only change Ruby version system wide.
* build from source code yourself – this option has the same problems as package installation but lets you install latest Ruby versions.

### NOAH KANTROWITZ and Andrea Campi redesign of the application Cookbook

* https://coderanger.net/application-cookbooks/
* https://github.com/poise/application_ruby
* https://github.com/poise/application
* http://www.slideshare.net/coderanger/reusable-cookbook-patterns
* ChefConf 2014: Noah Kantrowitz, ["Poise: Reusable Cookbook Patterns"](https://www.youtube.com/watch?v=vVsSAKtgOYs)

NOTE: `v4.1.6` is the last version of the application cookbook without the halite gem.

* The application_ruby cookbook depends on the application cookbook.

Internals:

* The application cookbook is writter as a gems that generate a cookbook using halite: 
  * https://github.com/coderanger/halite
  * https://github.com/poise/poise


* Define the BundleInstall resource

Poise provides:

* https://github.com/poise/poise#notifying-block
* https://github.com/poise/poise#include-recipe
* Lazy inizializer https://github.com/poise/poise#lazy-initializers
* Option collector https://github.com/poise/poise#option-collector
* Subresources (see the chef 2014 video)
* Resource DSL like LWRP
  * `actions` and `default_action` are just like in LWRPs, though default_action is rarely needed as the first action becomes the default.
  * `attribute` is also available just like in LWRPs, but with some enhancements noted below.  


#### Poise Cookbook 

* [The poise cookbook](https://github.com/poise/poise)

The poise cookbook is a set of libraries for writing reusable cookbooks. It providers helpers for common patterns and a standard structure to make it easier to create flexible cookbooks using HWRP.

Rather than LWRPs, Poise promotes the idea of using normal, or "heavy weight" resources, while including helpers to reduce much of boilerplate needed for this.

The chef ecosystem use "Fork", "cookbook wrapper" and "reqind" to allow cookbook extensibility
, Poise introduces a new strategy; **inheritance**. Resources are classes so the Poise filosophy is to inherite.

NOTE: The downside of this approach is that we **cannot use LWRP** because LWRP are defined using the DSL, instead HWRP uses pure ruby code.

Poise makes heavy use of mixins in order to load:

~~~ruby
class Chef
  class Resource::MyApp < Resource
    include Poise
    ...
  end

  class Provider::MyApp < Provider
    include Poise
    ...
  end
~~~


TODO:

* `notifying_block`
* `converge_by`
* Berkshelf extension : http://23.92.17.78/github/RiotGames/berkshelf/Berkshelf/Berksfile#extension-instance_method<F4>
*



# Resources most used by PITCHTARGET

* [deploy](http://docs.opscode.com/resource_deploy.html)
* [ruby block](http://docs.opscode.com/chef/resources.html#ruby-block)
* [service](http://docs.opscode.com/chef/resources.html#service)
* [remote_file](http://docs.opscode.com/resource_remote_file.html) used to transfer a file from a remote location using file specificity

## Users, Groups and SSH keys management

https://www.chef.io/blog/2014/07/10/managing-users-and-ssh-keys-in-a-hybrid-world/

## Monit

NOTE: each time a cookbook must send a notification to a service like monit, you need to make that resource available, the easiest and safest way to do it is to add it with action `:nothing`:

~~~
service 'monit' do
  action :nothing
end
~~~

Examples:

* [Opsworks NodeJS example](https://github.com/aws/opsworks-cookbooks/blob/release-chef-11.10/deploy/definitions/opsworks_nodejs.rb#L5)
* [Gitlab monit example](https://gitlab.com/gitlab-com/cookbook-gitlab-opsworks/blob/master/gitlab/recipes/deploy.rb)

### Monit Cookbook

It looks that Monit-ng is more advanced than this cookbook:

* https://supermarket.chef.io/cookbooks/monit


define :opsworks_nodejs

### Monit-ng Cookbook

* https://github.com/bbg-cookbooks/monit-ng
* https://supermarket.chef.io/cookbooks/monit-ng

### Implementation

* use testkitchen
* use serverspec
* in `libraries` there is there is the `monit_check` resource implementation
* The core of this cookbook is the `monit_check` resource.
* A pool of recipes manage different kinds of monit installations
* A poll of recipes offers some defaul for most common services (sshd, etc...)


## Service


## Backup Cookbook

This cookbook install and configure the Backup Ruby Gem. Here you can
find a [gem overview](http://meskyanichi.github.io/backup/v4/).
The backup\_model resource will schedeul with cron the execution of a
backup and the define a Backup model to be used. On the gem website you can find how to create a Backup::Model.
The `definition` attribute accept is the ruby code that define a
Backup::Model.


* [community page](http://community.opscode.com/cookbooks/backup)


The `definition` attribute accept is the ruby code that define a
Backup::Model.


* [community page](http://community.opscode.com/cookbooks/backup)

## Apt

https://github.com/opscode-cookbooks/apt

Setup PPA and install package:

~~~
apt_repository 'ruby-brightbox' do
  uri          'http://ppa.launchpad.net/brightbox/ruby-ng/ubuntu'
  distribution node['lsb']['codename']
  components   ['main']
  keyserver    'keyserver.ubuntu.com'
  key          'C3173AA6'
  deb_src      true
end

package "ruby2.2"
~~~


## gem_package resource

Ref: [Chef doc](https://docs.chef.io/resource_gem_package.html)

~~~
## Install the Bundler Gem:
gem_package "bundler" do
  options "--no-ri --no-rdoc"
end
~~~

# Ruby
## Ruby from source

* [Ruby build Cookbook](https://supermarket.chef.io/cookbooks/ruby_build) with LWRP resources, used also by gitlab

## Ruby from brightbox

* https://launchpad.net/~brightbox/+archive/ubuntu/ruby-ng
* https://github.com/phusion/passenger-docker/blob/master/image/enable_repos.sh


# Customizing Chef

**BEST REFERENCE** : /Volumes/ArchiveDisk/Archive/Misc/ebook/Customizing_Chef.pdf

* http://tech.yipit.com/2013/05/09/advanced-chef-writing-heavy-weight-resource-providers-hwrp/

## Definition : code reuse

* http://docs.chef.io/definitions.html
* http://stackoverflow.com/questions/21120495/chaining-grouping-resources-in-chef

* A definition is code that is reused across recipes, similar to a compile-time macro.
* A definition is then used in one (or more) recipes as if it were a resource.
* The definition will be replaced by all the resources that are specified within the definition.

## Custom Resources and Provider: LWRP or HWRP

REF: /Volumes/ArchiveDisk/Archive/Misc/ebook/Customizing_Chef.pdf

Every resource and provider you use in your recipies are instance of classes inherited from Chef::Provider and Chef::Resource.
Chef has two mechanism to create those classes:

* Add ruby code in you cookbook `libraries` directory
* Use the LWRP DSL language. Files into `providers` and `resources` directory are interpreted as LWRP definitions.

Cookbook example that mix both approaches:

~~~
libraries/
    my_resource.rb # use pure ruby code
    my_provider.rb # use pure ruby code
providers/
    my_lwrp_provider.rb # LWRP
resources/
    my_lwrp_resource.rb #LWRP
recipes/
    default.rb
metadata.rb
~~~

[This post](http://tech.yipit.com/2013/05/09/advanced-chef-writing-heavy-weight-resource-providers-hwrp/) show how to implement the same resource using these two mechanasism.

The final result is the same you can choose the mechanism that best fit your need, generally LWRP is easier to implement instead pure ruby code is more flexible.

* The [LWRP naming convention](http://docs.opscode.com/lwrp_custom.html#file-locations) is described here.
* The [LWRP resource DLS doc](http://docs.opscode.com/lwrp_custom_resource.html)
* The [LWRP provider DLS doc](http://docs.opscode.com/lwrp_custom_provider.html)


Other refs:
* [Intro exampe](http://dougireton.com/blog/2012/12/31/creating-an-lwrp/)
* [Tutorial: how to test LWRP](http://neethack.com/2013/10/understand-chef-lwrp-heavy-version/)

### HWRP Cheatsheat


* set_or_return  https://github.com/chef/chef/blob/master/lib/chef/mixin/params_validate.rb#L84
* `new_resource.updated_by_last_action(true)` when an action update a resource



# Tools

Chef development Kit:
* http://www.getchef.com/blog/2014/04/15/chef-development-kit/
* http://www.getchef.com/downloads/chef-dk/mac/

## chef tool
http://docs.opscode.com/ctl_chef.html

# Chef support for docker
See the docker guide: _guides/docker.markdown


