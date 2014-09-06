---
layout: post
title: "azure"
date: 2014-03-30 14:55:42 +0200
comments: true
categories: 
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

This is a short internal guide to the AWS service we use most.


# References

Azure WebSite scenari di utilizzo:
http://blogs.msdn.com/b/vitolo/archive/2012/11/28/windows-azure-web-sites-scenari-di-utilizzo.aspx

Training Material:
* Intro https://github.com/WindowsAzure-TrainingKit/PRESENTATION-WindowsAzureVirtualMachines
* All http://windowsazure-trainingkit.github.io/presentations.htm

Certificati SSL:
http://www.linkedin.com/groupAnswers?viewQuestionAndAnswers=&discussionID=211624566&gid=4079784&trk=eml-anet_dig-b_nd-pst_ttle-cn&ut=289aB_KkZHXlA1

Intro alla Virtual Machine
http://blogs.msdn.com/b/vitolo/archive/2012/10/17/alcuni-consigli-sulle-virtual-machine-in-windows-azure.aspx

AMPQ:
http://www.linkedin.com/groupAnswers?viewQuestionAndAnswers=&discussionID=211767746&gid=4079784&tra=eml-anet_dig-b_nd-pst_ttle-cn&ut=2qsOdRl4BJXlA1


# Main Concepts

* _Azure Subscription_ is a billing container
* _Region_ is where the hardware that physically runs your code lives
* _Storage Account_
* _Affinity Group_  is a name you can use to tie together resource on the same region for performace reason. All services within an affinity group will be located in the same data center. An affinity group is required in order to create a virtual network. [doc](http://msdn.microsoft.com/en-us/library/windowsazure/jj156209.aspx)
* _Account Storage_  http://www.windowsazure.com/en-us/documentation/articles/storage-whatis-account/
* _Virtual Network_ http://msdn.microsoft.com/en-us/library/windowsazure/jj156007.aspx

# Remote desktop with Windows Server

Image: Windows 8.1 Enterprise 

Jenkins on Windows Azure
Before we can create a Virtual Machine with a remote desktop we must create a FungoStudios Virtual Network as required by
http://msdn.microsoft.com/en-us/library/dn520828.aspx
Name: FungoStudios
Affinity Group: FungoStudiosCI


"remote desktop connection" is an OSX app

Azure [Remote desktop on windows](http://msdn.microsoft.com/en-us/library/windowsazure/dn535788.aspx)
Azure [Remote desktop on OSX](http://stackoverflow.com/questions/13248955/cant-rdp-to-azure-on-mac-os-x)




http://taylorcowanonline.com/?p=260

http://blogs.msdn.com/b/gongcheng/archive/2013/04/16/jenkins-on-windows-azure-the-missing-manual-master.aspx
http://blogs.msdn.com/b/gongcheng/archive/2013/04/16/jenkins-on-windows-azure-the-missing-manual-slave.aspx



# Commnad line tools: xplat-cli

To install the cli go [here](http://www.windowsazure.com/en-us/documentation/articles/xplat-cli/)
To get started, just type `azure` in a new Terminal window.

Command Reference is available on [github readme](https://github.com/WindowsAzure/azure-sdk-tools-xplat) and [azure website](
http://www.windowsazure.com/en-us/documentation/articles/command-line-tools/=).

To download your credential use from command line:
azure account download

~~~
azure account list
info:    Executing command account list
data:    Name      Id                                    Current
data:    --------  ------------------------------------  -------
data:    BizSpark  XXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX      false
data:    BizSpark  XXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX      true
~~~


NB: all BizSpark accounts have the same name. To understand the which account you are using by id go to the "portal -> setting" and check the id

to switch account:

~~~
azure account set XXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
~~~


## Affinity Group

create:
azure account affinity-group create placecommander --location "West Europe"

list:
azure account affinity-group list

show:
account affinity-group show [options] <name>


## Virtual Machine management

To create a VM with ssh key:

To create an azure image The recommended approach is to first create a digital certificate and then provide its public key when you create the VM.
For a useful overview, see Creating secure Linux VMs in Azure with SSH key pairs.


generate keys:
~~~
openssl req -x509 -nodes -days 365 -newkey rsa:2048  -keyout example1.key -out example1.pem
chmod 600 example.key
~~~

create the machine:

~~~
azure vm create --subscription "fb90212e-9706-4e31-8737-0d4842ab4179" --vm-size "small"  --ssh 22 --ssh-cert ./example1.pem --no-ssh-password --affinity-group placecommander "pc-frontend" b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-12_04_3-LTS-amd64-server-20140130-en-us-30GB ubuntu
ssh -i example1.key ubuntu@pc-frontend.cloudapp.net
~~~

get the DNS name and ssh into the machine

~~~
azure vm show pc-frontend
ssh -i ~/.ssh/placecommander_azure.key ubuntu@pc-frontend.cloudapp.net
~~~


To open a port
http://research.microsoft.com/en-us/projects/azure/windows-azure-for-linux-and-mac-users.pdf
azure vm endpoint create -multiple exampleVM1 80 80

Azure and Chef

http://docs.opscode.com/plugin_knife_azure.html

# BizSpark Tips and Tricks

## To use all 8 accounts
https://touch.www.linkedin.com/?sessionid=1074838991011840&trk=eml-b2_anet_digest-null-12-null&rs=false&dl=no#postdetail/g-4079784-S-5814368660738838531

Ciao a tutti, il modo migliore al momento per far comunicare VM di uno stesso dominio applicativo "spalmate", come dice Alessandro, su più sottoscrizioni per ottimizzare l'utilizzo dell'offerta BizSpark è di abilitare endpoint pubblici sulle macchine (http://is.gd/ZCNsCg) specificando delle Access Control Lists (http://is.gd/Cs1OQ3) per garantire la sicurezza delle macchine. Attraverso quegli endpoint è poi possibile instaurare la comunicazione secondo le modalità che si ritengono necessarie (es.: VPN, WebServices, ...)


NB: there is an issue with the loadbalancer, how should we add instances to a single load balancer???


