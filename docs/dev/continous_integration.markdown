---
layout: post
title: "Continous Integration"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["CI"]
---


# Shippable

## Yml Config File

* validator: http://yaml-online-parser.appspot.com/
* languages doc: http://docs.shippable.com/languages/
* samples: https://github.com/shippableSamples

Caching:
* https://github.com/Shippable/support/issues/533
* cache: true
* To reset the cache include a keyword in your commit message - [reset_minion] 
* example: https://github.com/shippableSamples/sample-ruby-mysql-cache/blob/master/shippable.yml
* http://blog.shippable.com/faster-builds-with-cached-containers
* http://blog.shippable.com/container-caching




## Docker

* http://blog.shippable.com/docker-image-creation-tagging-traceability
* http://docs.shippable.com/docker_registries/#push-images-to-docker-hub


## Bitbucket integration

Deployment Key: Shippable will add a deployment key to a connected repository




# Bamboo

Reference:

* [BambooCloud Official Doc](https://confluence.atlassian.com/bamboocloud)

TODO:

* build in automatico per il feature branch -> Paolini sa come fare

## Intro: Project, Plan, Job, Task

https://confluence.atlassian.com/bamboocloud/working-with-bamboo-cloud-737184556.html

* Plan: a sequence of stages (one by default)
* Stage: a sequence of tasks
* Job: 

* A plan can have more than a repository


### Tasks

#### Script task

* DASH issue: When you run from file Bamboo uses `/bin/sh` which in Ubuntu is `/bin/dash`, this bypass also the `#!/bin/bash` syntax. Instead when you use the "inline" option the behavior is different, the best practice is to use the inline option:

~~~bash
#!/bin/bash
docker/build_images.sh -p
~~~

* NON TTY bash issue: don't use docker `-i -t` becouse the bash runned by bamboo is not in TTY mode, otherwise you will get an error `` 
  

## Build Directory on the agent

`/home/bamboo/bamboo-agent-home/xml-data/build-dir`

## JIRA integration

* Show build status into a JIRA issue: https://confluence.atlassian.com/bamboocloud/using-plan-branches-737183873.html#Usingplanbranches-IntegratingbrancheswithJIRA

## Bitbucket integration

Build trigger: Add the Bamboo hook to your repository in Bitbucket. No further action is necessary on your local repository. Each push of new commits in to Bitbucket will trigger the build based on your configuration. 

* https://confluence.atlassian.com/bamboocloud/repository-triggers-the-build-when-changes-are-committed-737183942.html
* https://confluence.atlassian.com/display/BAMKB/Bitbucket+Commits+do+not+Trigger+Builds+in+Bamboo+Cloud

## SSH Keys for deploy

https://answers.atlassian.com/questions/279335/access-shared-credentials-from-shell-script-task

We install private keys used for this purpose on our instances via Bamboo instance configuration. In the instance startup script we add a method to dump the key to a file on the instance. This is then used during the build flow. It would be better to have access to the shared credentials in Bamboo ... maybe in the future they'll add this?? :)

## Shared Credentials

NOTE:

## Elastic Bamboo: AWS integration

**WARNING** :

* you should use a dedicated AWS account (you can use consolidated billing if you want)

### Access your instance with ssh

Ref:

* https://confluence.atlassian.com/bamboocloud/generating-your-aws-private-key-file-and-certificate-file-737184428.html

Bamboo generate an EC2 keypair, you cab get the private key from: Elastic Instances -> "view" your instance, download `/data/jirastudio/bamboo/home/xml-data/configuration/elasticbamboo.pk`. Then `mv ~/Downloads/elasticbamboo.pk ~/.ssh/` and `chmod 600 ~/.ssh/elasticbamboo.pk`

### Use AWS instances roles

* Create a role from the AWS console, AWS will create also an instance profile with the same name of the role: http://docs.aws.amazon.com/codedeploy/latest/userguide/how-to-create-iam-instance-profile.html#getting-started-create-ec2-role-console.
* From the Bamboo instance configuration set the instance profile.


### LIST of AWS ami

The official list is here: https://confluence.atlassian.com/display/BAMKB/List+of+Atlassian+AMI+IDs
But as stated in the comments the most updated list can be found browsing this directory: 
https://maven.atlassian.com/content/repositories/atlassian-public/com/atlassian/bamboo/atlassian-bamboo-elastic-image/

As september 2015 the most recent list is:
https://maven.atlassian.com/content/repositories/atlassian-public/com/atlassian/bamboo/atlassian-bamboo-elastic-image/4.7/atlassian-bamboo-elastic-image-4.7.ami

If you want to run on a T2 machine you need an HVM image, actually it's available only in virginia us-east-1:

~~~
cat atlassian-bamboo-elastic-image-4.7.ami |grep HVM.Ubuntu
image.US_EAST_1.EBS.x86_64.linux.HVM.Ubuntu=ami-eb5b8080
~~~

### Use Packer to create a T2 micro image [NOT WORKING]

* Create AMI with Packer: https://developer.atlassian.com/blog/2015/07/bamboo-packer/
* ansible intro: https://wiredcraft.com/blog/getting-started-with-ansible-in-5-minutes/

To use the free tier t2.micro we need an AMI that support the virtualization type 'hvm'. To use the easiest AWS packer build 


we start from the ami that bamboo propose from the its console (7 sept 2015 is: ami-02fbae75)

We removed credential 
`AWS_PROFILE=bamboo packer build bamboo-docker-update.json`

        "ami_virtualization_type": "hvm",


Here a link to an HVM image is provided: https://jira.atlassian.com/browse/BAM-12121
To get early access to the image, you can directly hit the artefact url. You can use later versions (newer than 4.3) of images too, but please remember that some of them may be private if there was no official Cloud release for them):
https://maven.atlassian.com/content/repositories/atlassian-public/com/atlassian/bamboo/atlassian-bamboo-elastic-image/4.4/atlassian-bamboo-elastic-image-4.4.ami

us-east-1 is Virginia

Watch this: https://jira.atlassian.com/browse/BAM-16190


MY IMAGES:
eu-west-1: ami-5febca28
us-east-1: ami-8397fbe6





# Jenkins

# TODO

* jobs
* workspaces: Disposable directory on Node used as a working directory for building. It is preserved on best effort bases after build completion.
* artifacts
* ssh key authentication 

## Glossary

* https://wiki.jenkins-ci.org/display/JENKINS/Terminology


## INTRO

Safari online guide: https://www.safaribooksonline.com/library/view/jenkins-the-definitive/9781449311155/ch05.html




## Security

https://wiki.jenkins-ci.org/display/JENKINS/Quick+and+Simple+Security

If have problem and look you out: https://wiki.jenkins-ci.org/display/JENKINS/Disable+security

### Cli security

Go to your profile -> Configure: add your public key ( ~/.ssh/id_rsa.pub by default)


## Install common plugins

~~~
java -jar jenkins-cli.jar -s http://localhost:8080 install-plugin git

~~~

## Jenkins Best practices

https://wiki.jenkins-ci.org/display/JENKINS/Jenkins+Best+Practices

Docker clean-up: http://blog.cloudbees.com/2015/08/jenkins-docker-gc.html

## Secure connection between Jenkins and Bitbucket

TODO: https://issues.jenkins-ci.org/browse/JENKINS-28632

* http://felixleong.com/blog/2012/02/hooking-bitbucket-up-with-jenkins
* https://wiki.jenkins-ci.org/display/JENKINS/BitBucket+Plugin
* Source code: https://github.com/jenkinsci/bitbucket-plugin

Atlassian doc:

* https://blog.bitbucket.org/2015/06/24/the-new-bitbucket-webhooks/
* https://confluence.atlassian.com/bitbucket/event-payloads-740262817.html

**TODO** : capire quando sicuro è il plugin bitbucket

Configuration:

* Install bitbucket plugin: `java -jar jenkins-cli.jar -s http://localhost:8080 install-plugin bitbucket`
* Setup bitbucket webhook: `http://1a14c906.ngrok.io/bitbucket-hook/`
* IMPORTANT: to avoid 500 error add the trailing `/`
* IMPORTANT: you must setup the trigger on your repo otherwise

If everythig is fine you should see this log:

~~~
INFO: Processing new Webhooks payload
INFO: Triggering BitBucket job <YOUR JOB NAME>
~~~



TIP: Use ngrok to test locally a webhook

* start jenkins locally
* Start ngrok tunnel: ngrok http 8080
* https://dashboard.ngrok.com/
* Go to http://localhost:4040/   and after you received a wekhook you can replay it from here to easly debug issues. NOTE you must reply the call which payload starts with:


~~~
{
    "push": {
        "changes": [
            {
~~~


TODO: 

* Is it possible to build all feature branches?
* Is it possible to access ENV variables?




### Resolve Troubles

Error 500: https://confluence.atlassian.com/display/BBKB/Webhooks+return+error+code+500+with+Jenkins

## Workflow Jobs

* http://jenkins-ci.org/content/workflow-plugin-10
* Home: https://github.com/jenkinsci/workflow-plugin
* https://www.cloudbees.com/sites/default/files/2014-0618-Boston-Jesse_Glick-Workflow.pdf

Tutorials:

* http://udaypal.com/2015-04-08-continuous-delivery-using-jenkins-workflow/
* http://udaypal.com/jenkins-workflow-getting-started/

Workflows are a new type of jobs that can easly describe a pipeline of build steps using a Groovy script.


Jenkins Workflow was built from ground up to provide users a way to address all the above limitations and support features such as

* Single Job - Entire CD Pipeline in a single workflow (or job)
* Complex logic - Support complex logic like for-loops, if-then-else, try-catch, fork-join etc…
* Survive restarts - While the workflow is running
* Human approval/input - Integrated human interaction into the workflow
* Allocate resources - Dynamically allocate slaves and workspaces
* Versioning - Supports checking workflow into version control system
* Checkpoints - CloudBees feature to be able to resume from a safe point
* Visualization - Stage view of workflow




Install the workflow plugin: `java -jar jenkins-cli.jar -s http://localhost:8080 install-plugin workflow-aggregator`

Your whole workflow is a single Groovy script using an embedded DSL, possibly quite short and legible; there is no need to jump between multiple job configuration screens to see what is going on. 

A key feature of a workflow execution is that it's suspendable.

TIP: 

* use the script generator to get basic snippets of steps
* Check each step status and output: enter the job and click the left menu "workflow steps"

### Steps documentation

* https://github.com/jenkinsci/workflow-plugin/blob/master/basic-steps/CORE-STEPS.md
* https://github.com/jenkinsci/workflow-plugin/blob/master/COMPATIBILITY.md

* `node` allocate a jenkins node. By default the node is master but you can specify the label of slaves.
* `stage` : https://github.com/jenkinsci/workflow-plugin/blob/master/TUTORIAL.md#stages
  * A concurrency of one is useful to let you lock a singleton resource, such as deployment to a single target server. Only one build will deploy at a given time: the newest which passed all previous stages.
  * A finite concurrency ≥1 can also be used to prevent slow build stages such as integration tests from overloading the system.
* `input` https://github.com/jenkinsci/workflow-plugin/blob/master/TUTORIAL.md#pausing-flyweight-vs-heavyweight-executors

### Build when a change is pushed to Bitbucket

* Install the bitbucket plugin
* from "build triggers" enable "Build when a change is pushed to BitBucket"

## Jenkins CLI

* REF: https://wiki.jenkins-ci.org/display/JENKINS/Jenkins+CLI

To download the cli: http://localhost:8080/cli/

To run: `java -jar jenkins-cli.jar -s http://localhost:8080/ help`

List plugins: `java -jar jenkins-cli.jar -s http://localhost:8080/ list-pligins`

Install plugins: ` java -jar jenkins-cli.jar -s http://localhost:8080 install-plugin <PLUGIN-ID>`

* You can find the plugin id on the plugin page, for example the workflow plugin has id `workflow-aggregator`: https://wiki.jenkins-ci.org/display/JENKINS/Workflow+Plugin
* After install use the soft restart: `java -jar jenkins-cli.jar -s http://localhost:8080/ safe-restart`

## Jenkins Logger Level

https://wiki.jenkins-ci.org/display/JENKINS/Logging 
