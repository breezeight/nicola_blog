---
layout: post
title: "Packer and Vagrant"
date: 2014-03-15 15:19:49 +0100
comments: true
categories: 
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# Quick links

vagrant boxes:

* [Official Ubuntu 14.04](https://cloud-images.ubuntu.com/vagrant/trusty/current/)
* [Bento Project by OpsCode](https://github.com/opscode/bento): Bento is a project that encapsulates Packer templates for building Vagrant baseboxes, used by Opscode to test Chef. 

# Testing VM performances

brew install iozone

Examples: https://www.thegeekstuff.com/2011/05/iozone-examples/




# Packer VS Vagrant

First off, Packer does not require or even encourage Vagrant usage. Packer stands on its own as a useful tool for its own purposes: namely, building machine images for whatever environment you require.

However, Packer is very useful alongside Vagrant, if you want. Packer can create Vagrant boxes. So if you wanted Vagrant boxes, then Packer can do this for you. This is the ONLY way Packer helps you use Vagrant. It does not REPLACE any part of Vagrant.

So why would you want to create Vagrant boxes? Tons of reasons, but here are the most common:

* You want a custom OS or custom prepared box. You're generally tied to publicly available boxes (such as the ones I make). With Packer, you can create your own custom box that has your own OS installed in some specific way. This is useful if you want to match what runs in production more closely.

* You want to pre-run provisioners so that `vagrant up` is faster. With Packer, you can run Chef/Puppet/etc. beforehand and bake it into an image, essentially getting rid of the provision time when doing a `vagrant up`. This can speed things up drastically. A lot of bigger companies do this sort of thing because running provisioning is pretty heavy.

* You want to create Vagrant boxes that are as close as possible to production, so you generate both boxes and AMIs (for production, or any other type) at the same time with Packer.

Vagrant has the `vagrant package` command, but this only works for VirtualBox. None of the other providers currently really support the `package` functionality. Also, this requires a source box to begin with. Packer can solve this base box step. Additionally, I plan on supporting packaging up pre-existing running environments with Packer, and this will replace the `vagrant package` functionality.

In fact, it is very likely in the future that Vagrant installers will also ship with Packer in them to handle this functionality.

Ref: [Mitchell Hashimoto response](https://groups.google.com/forum/#!msg/packer-tool/4lB4OqhILF8/NPoMYeew0sEJ)
Ref: [Stack Overflow](http://stackoverflow.com/questions/17733063/vagrant-vs-packer-whats-the-difference)

# Packer

## Install and Update on OSX

To install packer:

~~~bash
brew tap homebrew/binary
brew install packer
~~~

To update packer:

~~~bash
brew remove packer
brew uninstal packer
brew install packer
~~~

## What is packer?
Packer is a tool for creating identical machine images for multiple platforms from a single source configuration.
Mitchell Hashimoto, the creator of Vagrant, launched Packer in mid 2013,
it will superseed any other tool or Vagrant plugin tailored to base box
creation.

[This blog post](http://blog.codeship.io/2013/11/07/building-vagrant-machines-with-packer.html) is a good introduction to the whole Packer Workflow.
Here I want to describe the main concepts and some practical use cases.

## Main Concepts

**Commands**
are sub-commands for the packer program that perform some job. An example command is "build", which is invoked as packer build. Packer ships with a set of commands out of the box in order to define its command-line interface.

**Builds**
Build is the core process of Packer. During this process Packer reads the configuration from a Template, use one or more Builder to create machine and use a provisioner to configure the machine and eventually produce one or more Artifact. Each build is a single task that eventually produces an image for a single platform. Multiple builds run in parallel.

**Artifact**
are the results of a single build, and are usually a set of IDs or files to represent a machine image. Every builder produces a single artifact. As an example, in the case of the Amazon EC2 builder, the artifact is a set of AMI IDs (one per region). For the VMware builder, the artifact is a directory of files comprising the created virtual machine.

**Provisioners**
are components of Packer that install and configure software within a running machine (shell scripts, Chef, Puppet, etc.),  prior to that machine being turned into a static image. 

**Builders**
are components of Packer that are able to create a machine image for a single platform (ex: AWS builder create an AMI creating a new EC2 instance or creating a new one). Builders read in some configuration and use that to run and generate a machine image. A builder is invoked as part of a build in order to create the actual resulting images. Example builders include VirtualBox, VMware, and Amazon EC2.

**Templates**
are JSON or [HCL](https://www.packer.io/docs/templates/hcl_templates) files which define one or more builds by configuring the various components of Packer. [Documentation](http://www.packer.io/docs/templates/introduction.html)

**Data Sources**
are components of Packer that fetch data from outside Packer and make it available to use within the template. Example of data sources include Amazon AMI, and Amazon Secrets Manager.

**Post-processors**
are components of Packer that take the result of a builder or another post-processor and process that to create a new artifact.

Ref: [Packer terminology documentation](http://www.packer.io/docs/basics/terminology.html)

## Packer Commands (CLI)

All interaction with Packer is done via the `packer` tool.
[Documentation](http://www.packer.io/docs/command-line/introduction.html)

Most common command are:

* Build a template : `packer build ubuntu_basic.json`
* Build only a builder : `packer build -only=virtualbox-iso ubuntu_basic.json`
* Print human readable template description : `packer inspect template.json`

## Packer Templates

https://www.packer.io/docs/templates

A Template consists of a series of declarations and commands for Packer to follow. 

* Packer is transitioning to a new template configuration format that uses HCL2 -- the same configuration language used by Terraform and HashiCorp's other products. From version 1.7.0, HCL2 becomes officially the preferred way to write Packer configuration(s).

[HCL2 Full doc](https://www.packer.io/docs/templates/hcl_templates)
[HCL2 Quick Intro](https://www.packer.io/guides/hcl)


NOTE: Note: that the file can be named anything, since Packer loads all files ending in .pkr.hcl in a directory. If you split your configuration across multiple files, use packer build <command line flags> <source directory> to initiate a build.

## Use Case: create a Generic Vagrant Box
Creating a base box is actually **provider-specific**.

This means that depending on if you're using VirtualBox, VMware, AWS, etc. the process for creating a base box is different. Usually each provider has different additions like VirtualBox or VMWare.

But each base box typically should have a bare minimum set of software for Vagrant to function.
As an example, a Linux box should be provisioned with the following:

* Package manager
* SSH
* SSH user so Vagrant can connect (with properly configured keys)
* Perhaps Chef, Puppet, etc. but not strictly required. (Vagrant can
install them later if needed by the provisioning step)

Packer has a [Vagrant post processor](http://www.packer.io/docs/post-processors/vagrant.html) that can create a Vagrant Box from many builder artifacts and is used also to create the official Vagrant Boxes.

Ref: [Creating a Vagrant Box](http://docs.vagrantup.com/v2/boxes/base.html)

### Create an Ubuntu Vagrant box for the Vagrant VirtualBox Provider

The [Ariya blog post](http://ariya.ofilabs.com/2013/11/using-packer-to-create-vagrant-boxes.html) uses the
[Virtualbox-iso builder](http://www.packer.io/docs/builders/virtualbox-iso.html). This builder will install VirtualBox additions by default.

Aryia on CentOS uses kickstart while on Ubuntu uses preseeding to setup the the machine, the VirtualBox builder `http_directory` option is used to publish via http the required configurations. The `boot_command` specifies the keys to type when the virtual machine is first booted in order to start the OS installer. This command is typed after boot_wait, which gives the virtual machine some time to actually load the ISO. As documented above, the boot_command is an array of strings. The strings are all typed in sequence. It is an array only to improve readability within the template. The boot command is "typed" character for character over a VNC connection to the machine, simulating a human actually typing the keyboard.

There are variable that you can use with the syntax `{{ variable_name }}` within the boot command:
  
* HTTPIP and HTTPPort
* Name


~~~json
    "boot_command": [
      "<esc><esc><enter><wait>",
      "/install/vmlinuz noapic preseed/url=http://{{ .HTTPIP }}:{{ .HTTPPort }}/ubuntu-12.04-amd64/preseed.cfg ",
      "debian-installer=en_US auto locale=en_US kbd-chooser/method=us ",
      "hostname={{ .Name }} ",
      "fb=false debconf/frontend=noninteractive ",
      "keyboard-configuration/modelcode=SKIP keyboard-configuration/layout=USA keyboard-configuration/variant=USA console-setup/ask_detect=false ",
      "initrd=/install/initrd.gz -- <enter>"
    ],

    "http_directory": "http",
~~~

The [shell provisioner](http://www.packer.io/docs/provisioners/shell.html) is used to provision the vagrant minimun requirements.

~~~json
  "provisioners": [{
    "type": "shell",
    "execute_command": "echo 'vagrant' | {{.Vars}} sudo -S -E bash '{{.Path}}'",
    "scripts": [
      "scripts/vagrant.sh",
      "scripts/vboxguest.sh",
      "scripts/compact.sh"
    ]
  }]
~~~

NB: images will be cached, see the subdirectory packer_cache, so that any subsequent build does not trigger a full download again.

COMMON ISSUES: the ubuntu image may dissapear when they update the minor version, we must replace the url and the SHA1

To build the box clone the [repo](https://bitbucket.org/ariya/packer-vagrant-linux) and run `packer build ubuntu-12.04-amd64.json`

### Create a Vagrant box from an Ubuntu Image to test OpsWorks
This usecase is basically the same but it provision also the the opsworks agent(see the opsworks.sh script)

Ref: [vagrant-opsworks](https://github.com/wwestenbrink/vagrant-opsworks)
Ref: [OpsWorks under the hood](http://www.slideshare.net/AmazonWebServices/aws-opsworks-under-the-hood-dmg304-aws-reinvent-2013)


~~~json
{
    "builders": [
        {
            "vm_name": "ubuntu1204-opsworks",
            "type": "virtualbox-iso",
            "guest_os_type": "Ubuntu_64",
            "http_directory": "preseed",
            "iso_url": "http://releases.ubuntu.com/12.04/ubuntu-12.04.4-server-amd64.iso",
            "iso_checksum": "b802bb065df98c0530d782eb94778c2da19e10d6",
            "iso_checksum_type": "sha1",
            "ssh_username": "vagrant",
            "ssh_password": "vagrant",
            "ssh_wait_timeout": "10000s",
            "boot_command": [
                "<esc><esc><enter><wait>",
                "/install/vmlinuz noapic ",
                "preseed/url=http://{{ .HTTPIP }}:{{ .HTTPPort }}/preseed.cfg ",
                "debian-installer=en_US auto locale=en_US kbd-chooser/method=us ",
                "hostname={{ .Name }} ",
                "fb=false debconf/frontend=noninteractive ",
                "keyboard-configuration/modelcode=SKIP keyboard-configuration/layout=USA ",
                "keyboard-configuration/variant=USA console-setup/ask_detect=false ",
                "initrd=/install/initrd.gz -- <enter>"
            ],
            "shutdown_command": "echo 'vagrant'|sudo -S shutdown -P now",
            "disk_size": 10140,
            "vboxmanage": [
                ["modifyvm", "{{.Name}}", "--memory", "512"],
                ["modifyvm", "{{.Name}}", "--cpus", "1"]
            ]
        },
        ....
    ],
    "provisioners": [
        {
            "type": "file",
            "source": "provision",
            "destination": "/tmp"
        },
        {
            "type": "shell",
            "inline": [
                "cd /tmp && chmod -R +x provision/"
            ]
        },
        {
            "type": "shell",
            "inline": [
                "cd /tmp/provision",
                "./base.sh",
                "./opsworks.sh",
                "./vmtools.sh",
                "./vagrant.sh",
                "./cleanup.sh"
            ],
            "execute_command": "echo 'vagrant'|{{.Vars}} sudo -E -S bash '{{.Path}}'"
        }
    ],
    "post-processors": [{
        "type": "vagrant",
        "output": "{{.Provider}}/ubuntu1204-opsworks.box"
    }]
}
~~~
##  Use Case: create an AWS AMI

Coming soon
http://www.packer.io/docs/builders/amazon-chroot.html


# Vagrant

## Vagrantfile

NOTE: all relative path in the Vagrantfile are relative to the
Vagrantfile's parent directory

[Vagrant file documentation](https://docs.vagrantup.com/v2/vagrantfile/machine_settings.html)

To set the virtualbox provisioner machine name:

~~~
config.vm.provider :virtualbox do |vb|
    vb.name = "my_machine"
  end
~~~

### Storage

https://www.virtualbox.org/manual/ch08.html#vboxmanage-storageattach
storageattach attaches/modifies/removes a storage medium connected to a storage controller that was previously added with the storagectl command

This example attach a vdi disk image

~~~
imagesDisk = "#{ENV['PMX_VAR_DIR']}/images.vdi" || 'images.vdi'
vb.customize ['storageattach', :id, '--storagectl', 'IDE Controller', '--port', 1, '--device', 0, '--type', 'hdd', '--medium', imagesDisk]
~~~

https://www.virtualbox.org/manual/ch08.html#vboxmanage-storagectl

### Shared Folders

config.vm.synced_folder
https://docs.vagrantup.com/v2/synced-folders/

If you have vbox addition the easiest way to mount and share a dir is:

~~~
    config.vm.synced_folder "/Users/nicolabrisotto/tmp", "/Users/nicolabrisotto/tmp"
~~~

## Plugins

**WARNING**

* [Vagrant-berkshelf could be deprecated and replaced by TestKitchen](https://sethvargo.com/the-future-of-vagrant-berkshelf/)


## Providers

WARNING: You need to use Vagrant boxes compatible with the provider you are using https://app.vagrantup.com/boxes/search?order=desc&page=0&provider=parallels&sort=created

### Parallels

https://parallels.github.io/vagrant-parallels/docs/

WARNING: You need to use Vagrant boxes compatible with the provider you are using https://app.vagrantup.com/boxes/search?order=desc&page=0&provider=parallels&sort=created


### VirtualBox

* official doc: http://docs.vagrantup.com/v2/virtualbox/configuration.html
* tutorial: http://kvz.io/blog/2013/01/16/vagrant-tip-keep-virtualbox-guest-additions-in-sync/
* [vagrant-vbguest](https://github.com/dotless-de/vagrant-vbguest) is a Vagrant plugin which automatically installs the host's VirtualBox Guest Additions on the guest system.
* `vagrant plugin install vagrant-vbguest`






### Docker

[Docker Provisioner](http://docs.vagrantup.com/v2/docker/index.html)

## Provisioner

* vagrant up --provision
* vagrant provision

### Chef Zero

[Vagrant chef zero plugin](https://github.com/andrewgross/vagrant-chef-zero)


I've done some test with this Vagrantfile 

~~~
# -*- mode: ruby -*-
# vi: set ft=ruby :

#requires:
# vagrant plugin install vagrant-chef-zero
# vagrant plugin install vagrant-berkshelf
# vagrant plugin install vagrant-omnibus


# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.
  #config.vm.box = "opscode-ubuntu-12.04"
  #config.vm.box_url = "http://opscode-vm-bento.s3.amazonaws.com/vagrant/virtualbox/opscode_ubuntu-12.04_chef-provisionerless.box"

  config.vm.provider :virtualbox do |vb|
    vb.name = "PitchtargetCookbooks"
  end

  config.vm.box = "canonical-ubuntu-14.04"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

  config.vm.network :forwarded_port, guest: 4567, host: 4567

  #CHEF
  config.omnibus.chef_version = :latest
  config.berkshelf.enabled = true
  config.chef_zero.enabled = false

  config.vm.provision :chef_client do |chef|
    #chef.cookbooks_path = ["cookbooks", "site-cookbooks"]
    #chef.add_recipe "addictive-devel-box-cookbook::default"
  end
end
~~~

but I still get this error:

~~~
chef client provisioner:
* Chef server URL must be populated.
* Validation key path must be valid path to your chef server validation key.
~~~

[Issue on github](https://github.com/berkshelf/vagrant-berkshelf/issues/14)


### Chef Solo

Using Berkshelf is realy easy to provision a VM with chef solo

install vagrant plugins:

* vagrant plugin install vagrant-berkshelf
* vagrant plugin install vagrant-omnibus

use a box without a provisioner for example:

~~~
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "opscode-ubuntu-12.04"
  config.vm.box_url = "http://opscode-vm-bento.s3.amazonaws.com/vagrant/virtualbox/opscode_ubuntu-12.04_chef-provisionerless.box"

  config.vm.network :forwarded_port, guest: 4567, host: 4567

  #CHEF
  config.omnibus.chef_version = "11.10.0"
  config.berkshelf.enabled = true

  #
  config.vm.provision "chef_solo" do |chef|
    chef.cookbooks_path = ["cookbooks", "site-cookbooks"]
    chef.add_recipe "nodejs::npm"
    chef.add_recipe "addictive-devel-box-cookbook::default"
  end
end
~~~


Add dependent coobooks with Berkshelf and the plugin will vendor them
for you if you add Berksfile in the same dir of you Vagrantfile.
Example of a Berksfile:

~~~
source "https://api.berkshelf.com"

cookbook 'nodejs'
cookbook 'npm'
cookbook 'addictive-devel-box-cookbook', path: 'addictive-devel-box-cookbook'
~~~

An easy way to add a local application cookbook is `berks cookbook addictive-devel-box-cookbook` and `cookbook 'addictive-devel-box-cookbook', path: 'addictive-devel-box-cookbook'`

NB: the application cookbook is also a nice pattern to override node
attributes: see Application Pattern in the guide [Develop and Test Chef Cookbooks](/guides/chef-cookbooks-develop-and-test.html)

Example to set the npm attribute of the nodejs cookbook:

~~~
node.set['nodejs']['npm']= "1.4.10"
~~~


To debug you can run from the VM the command: 
~~~bash
/opt/chef/embedded/bin/ruby /usr/bin/chef-solo  -c /tmp/vagrant-chef-1/solo.rb -j /tmp/vagrant-chef-1/dna.json
~~~

# UTM

https://getutm.app/

## [JOB] Start from a snapshot

https://github.com/utmapp/UTM/pull/3893

Short demo of the feature options

https://www.youtube.com/watch?v=XdqdCxRbsec&ab_channel=EugeneCheah


## [JOB] Setup Ubuntu 22.04 x86 with qemu emulation on apple M1

- Download Ubuntu Server for x86
- Open UTM
- Create a new VM => Emulation => ....


## [JOB] Setup Ubuntu 22.04 x86 with Rosetta virtualizaion on apple M1

- Download Ubuntu Server for x86
- Open UTM
- Create a new VM => Virtualization => check "apple virtualization" => check => Enable Rosetta

NON MI FUNZIONA!!

# Multipass - Canonical

* DOC: https://multipass.run/docs/mac-tutorial
* Discussion: https://discourse.ubuntu.com/c/multipass/21/none


## TODO

* Multipass alias: https://discourse.ubuntu.com/t/how-to-use-instance-command-aliases/24128

* build images with Packer, could it be useful? https://discourse.ubuntu.com/t/how-to-build-multipass-images-with-packer/12361/12



## Why Multipass?

* https://discourse.ubuntu.com/t/beta-release-multipass/2696 
*  is a service that manages virtual machine instances running Ubuntu. It uses images from [cloud-images](http://cloud-images.ubuntu.com/), the same images you will use 


## MISC cmds

multipass commands:

* `find` : Lists available images

* `delete breezy-liger`: delete the instance named breezy-liger
* `purge`: Purge all deleted instances permanently

* `info <instance>`: display instance's info (State, IPv4, Release, Image hash, Load, Disk usage, Memory usage, Mounts)
* `info --all`: print all
* `shell <instance>`: Open a shell on a running instance
* `start/stop/suspend`: Start instances, Stop running instances, Suspend running instances
* `transfer`: transfer files between the host and instances

## Which Tecnology does multipass uses?

https://multipass.run/docs/set-up-the-driver 

You can check which driver you are using with `multipass get local.driver`

At the time of writing (2023-03):
* On MacOS, 
  * By default, Multipass on macOS uses hyperkit driver for the Intel macOS and the qemu driver for the M1 macOS. However, an alternative option is to use VirtualBox.
  * https://multipass.run/docs/set-up-the-driver#heading--macos-use-virtualbox
* Linux: qemu or lxd driver (depending on the architecture). However, if you want more control over your VMs after they are launched, you can also use the experimental libvirt driver. 
* Windows: By default, Multipass on Windows uses the hyperv driver. However, if you want to (or have to), you can change the hypervisor that Multipass uses to VirtualBox.




## Primary Instance

In Multipass, an instance with the name primary is privileged.  `primary` is a special instance:
- your host $HOME is mounted automaticcaly into the VM `~/Home/` directory
- For example, it is the default argument of multipass shell. In two terminal instances, check multipass shell primary and multipass shell. Both commands should give the same result.


`multipass launch lts --name ltsInstance --mem 2G --disk 10G --cpus 2`

## Manage Instances (create/modify)

https://multipass.run/docs/create-an-instance

    multipass launch kinetic --name helpful-duck --cpus 1 --disk 5G --mem 4G


Custom networking: https://multipass.run/docs/create-an-instance#heading--create-an-instance-with-multiple-network-interfaces

### Add Network Interface

https://multipass.run/docs/additional-networks 


## cloud-init + Multipass

Doc:
* https://ubuntu.com/blog/using-cloud-init-with-multipass

Logs: `sudo cat /var/log/cloud-init*`



Multipass can also make use of cloud-init to customize an instance during launch.

    multipass launch -n my-test-vm --cloud-init cloud-config.yaml

*  multipass only supports YAML cloud-config files. Multipass will validate the YAML syntax of the cloud-config file before attempting to start the VM! 
Multipass uses cloud-init to pass in vendor-data to setup the VM for access by the user. If the user overrides any of the required keys (e.g. packages, ssh_authorized_keys, users, etc.) in his or her user-data then multipass will merge its own data so that the end-user will not lose access to the system.

If interested, a user can examine the executed user-data and vendor-data by looking at the files in /var/lib/cloud/instances/.

### Examples

https://aaronmsft.com/posts/multipass/

#### Nix




## Networking | HUGE TOPIC

Con la 1.9 dovrebbero aver risolto: https://discourse.ubuntu.com/t/multipass-on-apple-silicon/27367/4

## Mount | CAN BE SLOW

* https://discourse.ubuntu.com/t/mount-i-o-slow-how-to-improve-performance/18479/6
* https://multipass.run/docs/improve-mount-performance


* Within instance to mounted directory:     37558 KB/s
  * ex: iozone -a  -s 1024

* On instance filesystem:                   966404 KB/s
  * ex: multipass exec primary -d "/home/ubuntu" -- iozone -a  -s 1024

* On host filesystem (mounted directory):   3103163 KB/s
  * ex: multipass exec primary -d "/home/ubuntu/Home" -- iozone -a  -s 1024

## exec

`multipass exec -- cmd --my-option`: execute `cmd` into the instance 

By default it mounts the `pwd` of the host into the 

To override this behaviour use: `-n, --no-map-working-directory`: Do not map the host execution path to a mounted path


The -- separator is required if you want to pass options to the command being run. Options to the exec command itself must be specified before --.

it is possible to specify on which instance directory the command must be executed. For that, there are three options. The first one is `-d <dir>`, which tells Multipass that the command must be executed in the folder `<dir>`. For example:

```bash
$ multipass exec arriving-pipefish --working-directory /home -- ls -a
.  ..  ubuntu
```

The ls -la command showed the contents of the /home directory, because it was executed from there.


multipass exec primary -n ls




You can pipe standard input and output to/from the command:  `multipass exec primary -- lsb_release -a | grep ^Codename:`


## Multipass and cloud-init

https://gitlab.com/addictivedev/knowledge/examples-and-wiki/-/wikis/Multipass

