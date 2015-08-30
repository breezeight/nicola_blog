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

## Jenkins Bestpractices

https://wiki.jenkins-ci.org/display/JENKINS/Jenkins+Best+Practices

## Secure connection between Jenkins and Bitbucket

* http://felixleong.com/blog/2012/02/hooking-bitbucket-up-with-jenkins
* https://wiki.jenkins-ci.org/display/JENKINS/BitBucket+Plugin

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

Workflows are a new type of jobs that can easly describe a pipeline of build steps using a Groovy script.

Install the workflow plugin: `java -jar jenkins-cli.jar -s http://localhost:8080 install-plugin workflow-aggregator`

Your whole workflow is a single Groovy script using an embedded DSL, possibly quite short and legible; there is no need to jump between multiple job configuration screens to see what is going on. 

A key feature of a workflow execution is that it's suspendable.

TIP: 

* use the script generator to get basic snippets of steps
* Check each step status and output: enter the job and click the left menu "workflow steps"


## Jenkins CLI

* REF: https://wiki.jenkins-ci.org/display/JENKINS/Jenkins+CLI

To download the cli: http://localhost:8080/cli/

To run: `java -jar jenkins-cli.jar -s http://localhost:8080/ help`

List plugins: `java -jar jenkins-cli.jar -s http://localhost:8080/ list-pligins`

Install plugins: ` java -jar jenkins-cli.jar -s http://localhost:8080 install-plugin <PLUGIN-ID>`

* You can find the plugin id on the plugin page, for example the workflow plugin has id `workflow-aggregator`: https://wiki.jenkins-ci.org/display/JENKINS/Workflow+Plugin
* After install use the soft restart: `java -jar jenkins-cli.jar -s http://localhost:8080/ safe-restart`

###  
