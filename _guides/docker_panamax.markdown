---
layout: post
title: "Docker: Panamax"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["docker"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}


# References:

* Install [Panamax](http://panamax.io/get-panamax/)


# Intro


Local console: http://10.0.0.200:3000

From local console you can search the docker HUB registry.

Note: Each time you restart panamax the Vagrantfile will be
reevaluated.

# VBOX Sharing

Qua spiegano un po' di trick
http://blog.printf.net/articles/2014/08/25/experimenting-with-panamax/

We can add a mounted dir using the vbox addition, if both arguments are
the same the docker volume command will works (this is a small trick for
docker 1.3, in the future we will not need it):

~~~
    config.vm.synced_folder "/Users/nicolabrisotto/tmp", "/Users/nicolabrisotto/tmp"
~~~

# Vagrantfile
In osx il
/usr/local/Cellar/panamax/0.3.2/.panamax/Vagrantfile


~~~bash
# -*- mode: ruby -*-
# # vi: set ft=ruby :
imagesDisk = "#{ENV['PMX_VAR_DIR']}/images.vdi" || 'images.vdi'

Vagrant.configure("2") do |config|
    Vagrant.require_version ">= 1.6.0"
    config.vm.box = ENV['PMX_BASEBOX'] || "panamax-coreos-box"
    config.vm.box_url = ENV['PMX_BASEBOX_URL'] || "http://storage.core-os.net/coreos/amd64-usr/367.1.0/coreos_production_vagrant.box"
    config.vm.hostname = ENV['PMX_VM_NAME'] || "panamax-vm"

    config.vm.network "private_network", ip: ENV['PMX_VM_PRIVATE_IP'] || "10.0.0.200"

    config.vm.provider :virtualbox do |vb, override|
        vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
        vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
        vb.name = ENV['PMX_VM_NAME'] || "panamax-vm"
        vb.customize ["modifyvm", :id, "--memory", Integer(ENV['PMX_VM_MEMORY']||1536)]
        vb.customize ["modifyvm", :id, "--ioapic", "on"]
        vb.customize ["modifyvm", :id, "--cpus", Integer(ENV['PMX_VM_CPUS']||2)]
        vb.customize ['storageattach', :id, '--storagectl', 'IDE Controller', '--port', 1, '--device', 0, '--type', 'hdd', '--medium', imagesDisk]
    end
    config.vm.define :ENV['PMX_VM_NAME'] || "panamax-vm"

    # plugin conflict
    if Vagrant.has_plugin?("vagrant-vbguest") then
        config.vbguest.auto_update = false
    end
    config.vm.synced_folder ".", "/var/panamax", type: "rsync", rsync__exclude: "images*"
    #Docker Mount
    if ARGV[0] == "up" then
      config.vm.provision "shell", inline: "cd /var/panamax && ./create-docker-mount", keep_color: "true"
    end
    config.vm.provision "shell", inline: "sudo chmod +x /var/panamax/coreos", keep_color: "true"
    config.vm.provision "shell", inline: "cd /var/panamax && ./coreos $1 --$2 -pid=\"$3\"", args: "#{ENV['PMX_OPERATION'] || 'install'} #{ENV['PMX_IMAGE_TAG'] || 'stable'} #{ENV['PMX_PANAMAX_ID'] || 'not-set'}", keep_color: "true"
    config.vm.synced_folder ".", "/vagrant", disabled: true
    config.ssh.username = "core"
end
~~~



The `image.vdi` disk image is attached
~~~
imagesDisk = "#{ENV['PMX_VAR_DIR']}/images.vdi" || 'images.vdi'
vb.customize ['storageattach', :id, '--storagectl', 'IDE Controller', '--port', 1, '--device', 0, '--type', 'hdd', '--medium', imagesDisk]
~~~

The `/usr/local/Cellar/panamax/0.3.2/.panamax` directory is synced on
`panamax up` into the `/var/panamax` dir, see the [vagrant rsync
doc](https://docs.vagrantup.com/v2/synced-folders/rsync.html)
This will make panamax scripts available into the VM

~~~
    config.vm.synced_folder ".", "/var/panamax", type: "rsync", rsync__exclude: "images*"
~~~

Finally the provisioning step will use the panamax scripts to:

* 

~~~
    #Docker Mount
    if ARGV[0] == "up" then
      config.vm.provision "shell", inline: "cd /var/panamax && ./create-docker-mount", keep_color: "true"
    end
    config.vm.provision "shell", inline: "sudo chmod +x /var/panamax/coreos", keep_color: "true"
    config.vm.provision "shell", inline: "cd /var/panamax && ./coreos $1 --$2 -pid=\"$3\"", args: "#{ENV['PMX_OPERATION'] || 'install'} #{ENV['PMX_IMAGE_TAG'] || 'stable'} #{ENV['PMX_PANAMAX_ID'] || 'not-set'}", keep_color: "true"
    config.vm.synced_folder ".", "/vagrant", disabled: true
~~~

## create-docker-mount script

Does it us systemd ?

## Variables

il vagrant file ha una serie di variabili d'ambiente ad esempio:
`PMX_VM_CPUS`
