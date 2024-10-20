---
layout: post
title: "azure"
date: 2014-03-30 14:55:42 +0200
comments: true
categories: "DevOps"
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

## Networking

### Affinity group

### Virtual Networks

* _Virtual Network_ http://msdn.microsoft.com/en-us/library/windowsazure/jj156007.aspx

### VPN

### Endpoints

### CLOUD SERVICE
A cloud service is a container for one or more virtual machines you create. You can create a cloud service for a single virtual machine, or you can load balance multiple virtual machines by placing them in the same cloud service.


### VIRTUAL MACHINE LOCATIONS
Choose the region, affinity group, or virtual network in which you want to deploy the virtual machine.
Affinity groups
Virtual networks


### VIRTUAL MACHINE AVAILABILITY SETS
An availability set is a group of virtual machines that are deployed across fault domains and update domains. An availability set makes sure that your application is not affected by single points of failure, like the network switch or the power unit of a rack of servers.



### Load Balanced Virtual Machines

http://azure.microsoft.com/en-us/documentation/articles/virtual-machines-load-balance/

# Azure Resource Manager

* Authoring Azure Resource Manager templates: https://azure.microsoft.com/en-us/documentation/articles/resource-group-authoring-templates/#variables
* Use the CLI: https://azure.microsoft.com/en-us/documentation/articles/xplat-cli-azure-resource-manager/

* azure config mode arm
* azure location list


**WARNING** : to use from the CLI you cannot use a publishsettings to authenticate see: https://azure.microsoft.com/en-us/documentation/articles/xplat-cli-connect/
You need only to do `azure login` and follow the instructions.

## Template syntax

https://alexandrebrisebois.wordpress.com/2015/06/03/use-the-azure-resource-manager-copy-operation-to-deploy-duplicates/

Copy: https://azure.microsoft.com/en-us/documentation/articles/resource-group-create-multiple/

## Cli 

* To show output: `azure group deployment show "testRG" "testDeploy"`
* `azure group create "testSwarm" "North Europe" -f azuredeploy.json -d "testDeploySwarm" -e azuredeploy.parameters.json`
* `azure resource list "testRG"`
* `azure resource show "testRG" "MyUbuntuVM" Microsoft.Compute/virtualMachines -o "2015-06-15"`
* `azure group log show testSwarm --all`

* New deploy `https://azure.microsoft.com/en-us/documentation/articles/resource-group-template-deploy/`


https://azure.microsoft.com/en-us/documentation/articles/xplat-cli-azure-resource-manager/


# Remote desktop with Windows Server

!!!! USE the NEW Microsoft Remote Desktop for OSX, it works for sure with Windows 7 N:
https://itunes.apple.com/us/app/microsoft-remote-desktop/id715768417


## Old

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

# Azure Deployment: Classic VS Resource Manager

Azure has two different deployment models for creating and working with resources: Resource Manager and classic. This article covers using both models, but Microsoft recommends that most new deployments use the Resource Manager model.

https://azure.microsoft.com/en-us/documentation/articles/resource-manager-deployment-model/

* To use the Resource Manager model from CLI: `azure config mode arm`

Benefitof Resource Manager: added the concept of the resource group, template, tags, etc.





# How Azure subscriptions are associated with Azure Active Directory

https://azure.microsoft.com/en-us/documentation/articles/active-directory-how-subscriptions-associated-directory/

Multiple subscriptions can trust the same directory, but a subscription trusts only one directory. 

From https://manage.windowsazure.com -> "Impostazioni" you can change the active directory and add coadmin

# Azure Extensions

https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-extensions-features/

# Docker

## Azure Docker extension

see here https://github.com/Azure/azure-docker-extension/blob/master/README.md for:

* Using Docker Extension in ARM templates

If you are using CoreOS Docker is already installed: https://github.com/Azure/azure-docker-extension/blob/master/pkg/driver/coreos.go


Note about core os extension driver:
https://github.com/Azure/azure-docker-extension/blob/master/pkg/driver/coreos.go


## Azure and Docker-machine 

* [Azure Doc](https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-docker-machine/)

Prerequisites:

* See the guide above to create `mycert.pem`
* NOTE: 

To create a machine:

~~~
docker-machine -D create -d azure --azure-subscription-id="c34c63c0-7d8b-4ce1-9217-4b7a65c12ff9" --azure-subscription-cert=mycert.pem machine-name2

INFO[0006] Creating Azure machine...                    
DEBU[0024] Generating certificate for Azure...          
DEBU[0024] executing: /usr/bin/ssh-keygen ssh-keygen -t rsa -N  -f /Users/nicolabrisotto/.docker/machine/machines/machine-name2/id_rsa
 
Generating public/private rsa key pair.
Your identification has been saved in /Users/nicolabrisotto/.docker/machine/machines/machine-name2/id_rsa.
Your public key has been saved in /Users/nicolabrisotto/.docker/machine/machines/machine-name2/id_rsa.pub.
DEBU[0025] Adding Linux provisioning...                 
DEBU[0025] Authorizing ports...                         
DEBU[0025] added Docker endpoint (port 2376) to configuration 
DEBU[0025] Creating VM...   
~~~

To point your Docker client at it, run this in your shell:

~~~
$(docker-machine env machine-name2) 
~~~

## Azure Container Service 

* https://azure.microsoft.com/en-gb/documentation/videos/connect-2015-getting-started-developing-with-docker-and-azure-container-service/ at minutes 6:00


# Commnad line tools: xplat-cli

To install the cli go [here](http://www.windowsazure.com/en-us/documentation/articles/xplat-cli/): npm install azure-cli -g
To get started, just type `azure` in a new Terminal window.

Command Reference is available on [github readme](https://github.com/WindowsAzure/azure-sdk-tools-xplat) and [azure website](http://www.windowsazure.com/en-us/documentation/articles/command-line-tools/=).

To download your credential use from command line (this example is for the user bizspark2):

* I keep all account data here `~/.azure_accounts/addictive/bizspark2`
* login into the account from your default browser
* azure account download
* `mv ~/Downloads/sub2-4-15-2015-credentials.publishsettings ~/AZURE_ACCOUNTS/ADDICTIVE/bizspark2`
* `azure account import ~/AZURE_ACCOUNTS/ADDICTIVE/bizspark2/sub2-4-15-2015-credentials.publishsettings`
* Now you MUST remove the `~/AZURE_ACCOUNTS/ADDICTIVE/bizspark2/sub2-4-15-2015-credentials.publishsettings`, you don't need it, it's only a security risk.


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

# Azure Container Service

https://azure.microsoft.com/en-us/documentation/articles/container-service-intro/

1) Deploy an Azure Container Service cluster:
* https://azure.microsoft.com/en-us/documentation/articles/container-service-deployment/
* NEW from template -> Azure Container

2) Connect to an Azure Container Service cluster:
* https://azure.microsoft.com/en-us/documentation/articles/container-service-connect/

## Test cluster
AzureContainerTest  user:pt  sshkey /Users/nicolabrisotto/.ssh/azure_container_test
DNS: ptdev

Agent: 3
Master: 3

ENABLE TUNNEL:
ssh -i ~/.ssh/azure_container_test -L 2375:localhost:2375 -N pt@ptdevmgmt.northeurope.cloudapp.azure.com -p 2200
export DOCKER_HOST=:2375



# Azureml - Azure Machine Learnign Studio

**** Andare su subscriptions e selezionare "bizpark1pitchtarget" ****

## Create a workspace

From the azure management portal: https://manage.windowsazure.com

https://azure.microsoft.com/en-us/documentation/articles/machine-learning-create-workspace/

## Users Management

azure management portal -> Enter the workspace -> Settings

NB: to create work user:

* Go to azure manage portal, subscription bizpark1pitchtarget
* Active Directory
* users: add user


# BizSpark Tips and Tricks

## To use all 8 accounts
https://touch.www.linkedin.com/?sessionid=1074838991011840&trk=eml-b2_anet_digest-null-12-null&rs=false&dl=no#postdetail/g-4079784-S-5814368660738838531

Ciao a tutti, il modo migliore al momento per far comunicare VM di uno stesso dominio applicativo "spalmate", come dice Alessandro, su più sottoscrizioni per ottimizzare l'utilizzo dell'offerta BizSpark è di abilitare endpoint pubblici sulle macchine (http://is.gd/ZCNsCg) specificando delle Access Control Lists (http://is.gd/Cs1OQ3) per garantire la sicurezza delle macchine. Attraverso quegli endpoint è poi possibile instaurare la comunicazione secondo le modalità che si ritengono necessarie (es.: VPN, WebServices, ...)


NB: there is an issue with the loadbalancer, how should we add instances to a single load balancer???


