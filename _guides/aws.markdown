---
layout: post
title: "aws"
date: 2014-03-16 20:48:22 +0100
comments: true
categories: 
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

This is a short internal guide to the AWS service we use most.

# IAM

Main concepts:

* _group_ : is a collection of users, when a user belong to a group has
all the group's permission
* _user_ : A IAM user is really just an identity with associated permission (can be people or application). A users is provided with credentials to uniquely identify themselves to AWS. 
* _security credential_ : each user can have different credentials (IAM—passwords, access keys, certificates, and MFA...). To create a new credential users need to be authorized.
* _permission_ : a permission authorizes or denies a user to perform any AWS actions or to access any AWS resources.
* _roles_ : A role lets you define a set of permissions to access the resources that a user or service needs, but the permissions are not attached to an IAM user or group. Instead, at run time, applications or AWS services (like Amazon EC2) can programmatically assume a role. When a role is assumed, AWS returns temporary security credentials that the user or application can use to make programmatic requests to AWS. Consequently, you don't have to share long-term security credentials (for example, by creating an IAM user) for each entity that requires access to a resource.
* _instance profiles_ : An instance profile is a container for an IAM role. Instance profiles are used to pass role information to an Amazon EC2 instance when the instance starts. 


refs:

* [aws doc users and groups](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_WorkingWithGroupsAndUsers.html)
* [aws doc credential management](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingLogins.html)
* [Doc: Roles](http://docs.aws.amazon.com/IAM/latest/UserGuide/WorkingWithRoles.html)
* [Doc: Instance Profiles](http://docs.aws.amazon.com/IAM/latest/UserGuide/instance-profiles.html)
* [Istance Profile use with EC2](http://docs.aws.amazon.com/IAM/latest/UserGuide/role-usecase-ec2app.html)


Our guidelines are:

* Create one user for each employee
* Assign policy only to groups (this will make your life easier when we
need to add the same policy to another user)
* Do NOT assign policies to a user. Create a new group and assign the
use to that group
* Password Policy: 16 chars, users cannot change pwd, require numbers,
special chars, uppercase char
* Do NOT create access key if not needed.
* Force MFA authentication at least on every production resource [How To](http://stackoverflow.com/questions/21917197/how-to-enforce-iam-users-to-use-multi-factor-authentication-to-use-the-console).
* Rotate credentials every 90 days (TODO write how to enforce)


These are ours main groups:

* _admin_ : Need permission to create and manage AMIs, instances, snapshots, volumes, security groups, and so on. The group has permission to use all the Amazon EC2 actions.

* _developers_ : need the ability to work with instances only. The group can call DescribeInstances, RunInstances, StopInstances, StartInstances, and TerminateInstances.

* _managers_ : not be able to perform any EC2 actions except listing the Amazon EC2 resources currently available. Has access to the billing info.

## IAM practical scenarios
* See [here](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_WorkingWithGroupsAndUsers.html) "Scenarios for Creating IAM Users"

Note:

* EC2 uses SSH keys and security groups to control who has access to specific Amazon EC2 instances. There's no method in the IAM system to allow or deny access to a specific instance.
* OpsWorks can help with the upload of SSH keys and is connected with
the IAM system
* for some use case the temporary token system is better suited than IAM

## IAM Policies

[TODO](http://docs.aws.amazon.com/IAM/latest/UserGuide/PermissionsAndPolicies.html)

## SLAM Providers

[TODO](http://docs.aws.amazon.com/IAM/latest/UserGuide/idp-managing-identityproviders.html)

## Log IAM Access with CloudTrial

[TODO](http://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html)

## IAM Server Certificates

IAM manage also all certificates you upload to AWS, ELB
ElasticBeastalk and other service use them.



to use EB_FAST_DEPLOY and add the certificate to EB use the "Arn" variables:

`aws iam list-server-certificates` :

~~~json
{
    "ServerCertificateMetadataList": [
        {
            "Path": "/", 
            "Arn": "arn:aws:iam::389793176040:server-certificate/fungostudios.com_STAR", 
            "ServerCertificateId": "ASCAI5PYADG6GB5TYNYZQ", 
            "ServerCertificateName": "fungostudios.com_STAR", 
            "UploadDate": "2012-08-24T16:17:52Z"
        }, 
~~~

~~~bash
LoadBalancerHTTPSPort=443
SSLCertificateId="arn:aws:iam::389793176040:server-certificate/fungostudios.com_STAR"
EnvironmentType=LoadBalanced
~~~

upload certificate:

~~~
aws iam upload-server-certificate --server-certificate-name certificate_object_name --certificate-body file://public_key_certificate_file --private-key file://privatekey.pem --certificate-chain file://certificate_chain_file
~~~

ref: [aws doc server certificates](http://docs.aws.amazon.com/IAM/latest/UserGuide/ManagingServerCerts.html)

## How to Keep Your AWS Credentials on an EC2 Instance Securely
http://shlomoswidler.com/2009/08/how-to-keep-your-aws-credentials-on-ec2.html

## How to Keep Your AWS Credentials on an laptop Securely

TODO: Why should we keep them in a laptop ?


## references

* [AWS best practices](http://docs.aws.amazon.com/IAM/latest/UserGuide/IAMBestPractices.html)
* [AWS use cases](http://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_UseCases.html#UseCase_EC2): EC2 and S3

# AWS Cli

The AWS Command Line Interface is a unified tool to manage your AWS services [reference](http://docs.aws.amazon.com/cli/latest/reference/).

NB: some service endpoint is available only in some region(OpsWorks only us-east-1 as of march 2014).

## Configuration and credentials for multiple accounts 

### Solution A: work by dirs
* add to bashrc AWS_CONFIG_FILE=.aws/config, this will override the
aws-cli config search path
* create a .aws/config for each project you work on
* execute all your aws command from the project dir

### Solution B: load credential with a bash function

see [here](http://mitchellhashimoto.tumblr.com/post/3505121069/flexible-aws-credentials)

Pros:
* keep all your credential in one place

Improvement:
* we could encrypt the credential dir

## Bash Commands Autocomplete

Quick install OSX:

~~~bash
brew install bash-completion
add to .bashrc:
if [ -f $(brew --prefix)/etc/bash_completion ]; then
  . $(brew --prefix)/etc/bash_completion
fi

echo "complete -C aws_completer aws" > /usr/local/etc/bash_completion.d/aws
~~~


Are you curious? How does it works?

* `aws_completer` is a command installed with the aws-cli
* `complete -C aws_completer aws` means: invoke the aws_completer
command when you double TAB.

Refs:

* [debian guide](http://www.debian-administration.org/article/316/An_introduction_to_bash_completion_part_1)
* [tldb.org](http://www.tldp.org/LDP/abs/html/tabexpansion.html)

# OpsWorks

[see this post](/guides/opsworks-introduction.html)


# CloudFormation


## Intro

* [Doc: Intro](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/CHAP_Intro.html)
* [Reinvent 2013: DMG201 - Zero to Sixty: AWS CloudFormation] (https://www.youtube.com/watch?v=-0ELfN-kb7g)

## How to write templates

* [Doc: template anatomy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html)
* [Doc: Template References](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-reference.html)


Templates have six major sections. Template structure and sections:

~~~json
{

    "AWSTemplateFormatVersion" : "version date",

    "Description" : "Valid JSON strings up to 4K",

    "Parameters" : {
        set of parameters
    },

    "Mappings" : {
            set of mappings
            },

    "Conditions" : {
            set of conditions
            },

    "Resources" : {
        set of resources
     },

    "Outputs" : {
        set of outputs
    }
}
~~~

Examples:

* [Template Snippets](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/CHAP_TemplateQuickRef.html)
* [Full Examples](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/example-templates.html)


### Resources and Resource properties

* [AWS Resource Types Reference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html)
* [Resource Property Types Reference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-product-property-reference.html)

NB: Every resource must have a Type key but properties doesn't require
it, for example this snippet has an error

~~~ json
  "Resources": {

    "AddictiveTestStack": {
      "Type": "AWS::OpsWorks::Stack",
      "Properties": {
        "ConfigurationManager": {
          "Type": "AWS::OpsWorks::StackConfigurationManager", # ERROR!
          "Properties": {
            "Name": "Chef",
            "Version": "11.10"
          }
        }
      }
    },
~~~

the right version is:

~~~ json
        "ConfigurationManager": {
          "Name": "Chef",
          "Version": "11.10"
        }
~~~


TIPS: to escape string for json format use the irb console

### Resource Dependency

[DependsOn attribute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html)

### Functions

[Intrinsic funtion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html) are built-in functions:

* Fn::Base64
* Condition Functions
* Fn::FindInMap
* Fn::GetAtt returns the value of an attribute from a resource in the template.
* Fn::GetAZs
* Fn::Join
* Fn::Select
* Ref

### Mapping

~~~json
"Mappings" : {
    "Mapping01 logical name" : {
        "Key01" : {
            "Value" : "Value01"
            "..."   : "..."
        },
        "Key02" : {
            "Value" : [ "Value02", "Value04"] 
        },
        "Key03" : {
            "Value" : "Value03"
        }
    }
}
~~~

* the intrinsic function _Fn::FindInMap_, it works like a Case statement or lookup table.
* Each mapping has a logical name unique within the template

### Pseudo Parameters

Parameters that are predefined by AWS CloudFormation.

[DOC](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/pseudo-parameter-reference.html):

* AWS::Region
* AWS::AccountId
* AWS::StackId
* AWS::StackName
* ...


### How to execute code on EC2 instances

* [AWS CloudFormation and Cloud-Init](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-waitcondition-article.html)
* [CloudFormation Helper Scripts Reference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-helper-scripts-reference.html)

## AWS CLI for CloudFormation

[Doc](http://docs.aws.amazon.com/cli/latest/reference/cloudformation/index.html)

~~~bash
aws cloudformation get-template --stack-name myteststack
aws cloudformation validate-template --template-body file://OpsWorks.json

aws cloudformation create-stack --stack-name "test" --template-body file://addictive_template.json
aws cloudformation create-stack --stack-name TestStack --template-body file:///home/local/MyTemplate.template --parameters ParameterKey=InstanceType,ParameterValue=m1.large

aws cloudformation describe-stack-events --stack-name "testConfigurationManagerOk"
aws cloudformation delete-stack --stack-name "test"

aws cloudformation update-stack --stack-name "testConfigurationManagerOk" --template-body file://addictive_template.json

aws cloudformation get-template --stack-name "testConfigurationManagerOk"
aws cloudformation list-stacks --stack-status-filter UPDATE_COMPLETE
~~~

To read the output parameters ??? What command should I use?
 

## Template validation

[Template validation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-validate-template.html)

~~~bash
aws cloudformation validate-template --template-body file://OpsWorks.json
~~~

## CloudFormer

If you already have AWS resources running, AWS provide a CloudFormer tool that lets you create a template from your existing resources. This allows you to capture and redeploy applications you already have running.

Launch it from the CloudFormation Console.


## Stack versioning and updates

[Doc](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html)

You modify stack resources by submitting an updated template or by submitting updated input parameters. When you submit an update, AWS CloudFormation updates resources based on differences between what you submit and the stack's current template. Resources that have not changed run without disruption during the update process. Resources that are updated could be interrupted or replaced, depending on the resources and properties that are being updated.

If you like you can keep the template versioned with source code but
using it to update an existing stack could be dangerous because the
running stack may have been updated.

The best practice to avoid unexpected resources updates is use `aws cloudformation get-template` to get the current stack and updated it.

TIPS: install json-diff if you want to check difference : `npm install -g json-diff`


## CloudFormation and OpsWorks

[AWS::OpsWorks::Stack Resource Type](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html)
