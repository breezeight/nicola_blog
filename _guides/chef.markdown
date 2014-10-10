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

#azure
env-AZURE_SUBSCRIPTION_ID=replace
env-AZURE_MGMT_CERT=replace
evn-AZURE_API_HOST_NAME=replace

#aws
env-AWS_ACCESS_KEY_ID=replace
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

#aws
gem 'knife-ec2'

#azure
gem 'knife-azure'
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


# Attributes
One of the most annoying concept of chef is understanding how to read
and write attributes.

An attribute is a specific detail about a node, such as an IP address, a host name, a list of loaded kernel modules, the version(s) of available programming languages that are available, and so on. An attribute may be unique to a specific node or it can be identical across every node in the organization. Attributes are most commonly set from a cookbook, by using Knife, or are retrieved by Ohai from each node prior to every chef-client run. All attributes are indexed for search on the Chef server. Good candidates for attributes include:

any cross-platform abstraction for an application, such as the path to a configuration files
default values for tunable settings, such as the amount of memory assigned to a process or the number of workers to spawn
anything that may need to be persisted in node data between chef-client runs.


NB: In attributes files the node object can be implicit, you can use
both `node.default["apache"]["dir"] = "/etc/apache2"` and `default["apache"]["dir"] = "/etc/apache2"`


~~~yaml
file "/tmp/something" do
  ....
  content node["bluepill"]["bin"]
end
~~~

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


# Resources most used by PITCHTARGET

* [deploy](http://docs.opscode.com/resource_deploy.html)
* [ruby block](http://docs.opscode.com/chef/resources.html#ruby-block)
* [service](http://docs.opscode.com/chef/resources.html#service)
* [remote_file](http://docs.opscode.com/resource_remote_file.html) used to transfer a file from a remote location using file specificity

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


# Custom Resources and Provider: LWRP or pure ruby code
Every resource and provider you use in your recipies are instance of
classes inherited from Chef::Provider and Chef::Resource.
Chef has two mechanism to create those classes:

* Add ruby code in you cookbook `libraries` directory
* Use the LWRP DSL language. Files into `providers` and `resources`
directory are interpreted as LWRP definitions.

~~~
#Cookbook example that mix both approaches
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

The final result is the same you can choose the mechanism that best fit
your need, generally LWRP is easier to implement instead pure ruby code
is more flexible.

* The [LWRP naming convention](http://docs.opscode.com/lwrp_custom.html#file-locations) is described here.
* The [LWRP resource DLS doc](http://docs.opscode.com/lwrp_custom_resource.html)
* The [LWRP provider DLS doc](http://docs.opscode.com/lwrp_custom_provider.html)


Other refs: 
* [Intro exampe](http://dougireton.com/blog/2012/12/31/creating-an-lwrp/)
* [Tutorial: how to test LWRP](http://neethack.com/2013/10/understand-chef-lwrp-heavy-version/)


# Tools

Chef development Kit:
* http://www.getchef.com/blog/2014/04/15/chef-development-kit/
* http://www.getchef.com/downloads/chef-dk/mac/

## chef tool
http://docs.opscode.com/ctl_chef.html

# Chef support for docker
See the docker guide: _guides/docker.markdown


