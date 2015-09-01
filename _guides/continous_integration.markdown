---
layout: post
title: "Continous Integration"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["CI"]
---

# Jenkins

# TODO

* jobs
* workspaces: Disposable directory on Node used as a working directory for building. It is preserved on best effort bases after build completion.
* artifacts
* ssh key authentication 

## Glossary

* https://wiki.jenkins-ci.org/display/JENKINS/Terminology

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

TIP: Use ngrok to test locally a webhook

* start jenkins locally
* Start ngrok tunnel: ngrok http 8080
* https://dashboard.ngrok.com/
* Go to http://localhost:4040/   and after you received a wekhook you can replay it from here to easly debug issues.

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
