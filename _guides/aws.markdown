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

delete certificate:


~~~
aws --profile=pt iam  delete-server-certificate --server-certificate-name "fungostudios.com_STAR"
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

### NEW DEFINITIVE SOLUTION

Now aws cli support multiple profiles, the doc is [here](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-multiple-profiles).

**TODO**: sinceramente non ho ben capito quale file serve... se metto le
credenziali solo in `~/.aws/credentials` non me le trova da awscli ... le ho messe
in  `~/.aws/config` e adesso le becca.... boh!! cmq metterle in
`~/.aws/config` fa funzionare la cli

The following example shows a credentials file with two profiles `~/.aws/credentials`:

~~~json
[default]
aws_access_key_id=AKIAIOSFODNN7EXAMPLE
aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

[user2]
aws_access_key_id=AKIAI44QH8DHBEXAMPLE
aws_secret_access_key=je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY
~~~

To set default region and output for each profile `~/.aws/config`:

~~~
[default]
region=us-west-1
output=json

[profile user2]
region=us-east-1
output=text
~~~

example:

~~~
aws ec2 describe-instances --profile user2
~~~


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

# ECS: EC2 Container Service

Doc: https://aws.amazon.com/ecs/
Guide: http://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html
API: http://docs.aws.amazon.com/AmazonECS/latest/APIReference/Welcome.html






## Preview version

* Intro: http://aws.amazon.com/blogs/aws/ec2-container-service-in-action/?sc_ichannel=ha&sc_ipage=homepage&sc_icountry=en&sc_isegment=c&sc_iplace=hero1&sc_icampaigntype=product_launch&sc_icampaign=ha_en_ECS_Launch&sc_icategory=none&sc_idetail=ha_en_281_1&sc_icontent=ha_281&



### Boot via cloud formation

NOTE: the template below don't create the ECS Cluster, you must create
it manually because Cloudformation still not support the ECS resource.

/Users/nicolabrisotto/.local/lib/aws/bin/aws ecs create-cluster --cluster-name TestCluster --profile pt --region us-east-1

~~~
aws cloudformation create-stack --stack-name TestEC2Container --template-body https://s3.amazonaws.com/amazon-ecs-cloudformation/Amazon_ECS_Quickstart.template --parameters ParameterKey=ClusterName,ParameterValue=TestCluster ParameterKey=KeyName,ParameterValue="pt_virginia" ParameterKey=InstanceType,ParameterValue=t2.micro --region us-east-1 --profile pt
~~~

### JOIN the cluster from an EC2 instance

When you boot the ami you must add the cluster name to
`/etc/ecs/ecs.config`, for example with cloudformation you can use
`UserData`:

~~~json
    "ContainerInstance" : {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "IamInstanceProfile" : { "Ref" : "ECSIamInstanceProfile" },
        "ImageId" : { "Fn::FindInMap" : [ "AWSRegionArch2AMI", { "Ref" : "AWS::Region" },
                          { "Fn::FindInMap" : [ "AWSInstanceType2Arch", { "Ref" : "InstanceType" }, "Arch" ] } ] },
        "InstanceType"   : { "Ref" : "InstanceType" },
        "SecurityGroups" : [ {"Ref" : "ECSQuickstartSecurityGroup"} ],
        "KeyName"        : { "Ref" : "KeyName" },
        "UserData"       : { "Fn::Base64" : { "Fn::Join" : ["", [
             "#!/bin/bash -xe\n",
             "echo ECS_CLUSTER=", { "Ref" : "ClusterName" },
             " >> /etc/ecs/ecs.config\n"
        ]]}}
      }
    },
~~~

When the ecs service of the instance boots it will join the cluster

/Users/nicolabrisotto/.local/lib/aws/bin/aws ecs list-container-instances --cluster TestCluster  --region us-east-1 --profile pt


### Docker Agent

The ecs docker agent runs as a docker container

* `/etc/ecs/ecs-init` is the script that start the agent the script
* `/etc/ecs/ecs.config`
* this is the command that runs the agent: `docker run --name ecs-agent -v /var/run/docker.sock:/var/run/docker.sock -v /var/log/ecs:/log -p 127.0.0.1:51678:51678 --env-file /etc/ecs/ecs.config -e ECS_LOGFILE=/log/ecs-agent.log amazon/amazon-ecs-agent:latest`
* `/var/log/ecs/ecs-agent.log` is the log


# SES


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

### Parameters type

NOTE: use parameter type as much as possible, this will prevent most of the errors in a early stage of the creation procedure: http://blogs.aws.amazon.com/application-management/post/Tx3DV2UYG9SC38G/Using-the-New-CloudFormation-Parameter-Types


### Resources and Resource properties

* [AWS: definition of a resource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resources-section-structure.html)
* [AWS Resource Types Reference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html)
* [Resource Property Types Reference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-product-property-reference.html)

A resource have:

* `Logical ID`: The logical ID must be alphanumeric (A-Za-z0-9) and unique within the template.
* `Resource type`
* `Properties` 

~~~
"Resources" : {
    "Logical ID" : {
        "Type" : "Resource type",
        "Properties" : {
            Set of properties
        }
    }
}
~~~

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

### Conditions

http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/conditions-section-structure.html

Example:

~~~json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description" : "Condition Example",
  "Parameters" : {
    "CreateRoleParam": {
      "Default": "false",
      "Description" : "Create Database",
      "Type": "String",
      "AllowedValues" : [ "true", "false" ],
      "ConstraintDescription" : "must be either true or false."
    }
  },
  "Conditions" : {
    "CreateRoleCondition" : {"Fn::Equals" : [{"Ref" : "CreateRoleParam"}, "true"]}
  },
  "Resources": {
    "OpsWorksInstanceRole": {
      "Type": "AWS::IAM::Role",
      "Condition" : "CreateRoleCondition",
      "Properties": {
        "AssumeRolePolicyDocument": {
          "Statement": [
            {
              "Effect": "Allow",
              "Principal": {
                "Service": [
                  "ec2.amazonaws.com"
                ]
              },
              "Action": [
                "sts:AssumeRole"
              ]
            }
          ]
        },
        "Path": "/"
      }
    }
  }
}
~~~

To test: `aws cloudformation --profile=pt create-stack --stack-name "test2" --template-body file://prova_conditional.json --parameters ParameterKey=CreateRoleParam,ParameterValue=true --capabilities CAPABILITY_IAM`

### Capabilities

### Nested Stacks

* [AWS blog post jan 2015 about ](http://blogs.aws.amazon.com/application-management/post/Tx1T9JYQOS8AB9I/Use-Nested-Stacks-to-Create-Reusable-Templates-and-Support-Role-Specialization)
* http://www.rightbrainnetworks.com/blog/cloudformation-zen-nested-stacks/
* http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html
* http://blog.mikebabineau.com/2014/05/05/cloudformation-nested-stacks-gotcha/

### How to execute code on EC2 instances

* [AWS CloudFormation and Cloud-Init](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-waitcondition-article.html)
* [CloudFormation Helper Scripts Reference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-helper-scripts-reference.html)

## Stack Policy

* [AWS DOC](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html)

`stack policies` take the form of JSON documents which prohibit or permit various operations to specific or general resources within the existing CloudFormation stack (they are not used in stack creation, only during updates).


* After you set a stack policy, all resources in the stack are protected by default
* You can define only one stack policy per stack
* a single policy protects multiple resources

Reference:

~~~json
{
  "Statement" : [
    {
      "Effect" : "<Deny_or_Allow>",
      "Action" : "update_actions",
      "Principal" : "*",
      "Resource" : "LogicalResourceId/ <resource_logical_ID> ",
      "Condition" : {        #Optional
        "<StringEquals_or_StringLike>" : {
          "ResourceType" : [resource_type, ...]
        }
      }
    }
  ]
}
~~~


Example `--stack-policy-body file://stack_policy.json` :

~~~json 
{
  "Statement" : [
    {
      "Effect" : "Deny",
      "Action" : "Update:*",
      "Principal": "*",
      "Resource" : "LogicalResourceId/DBInstance"
    },
    {
      "Effect" : "Allow",
      "Action" : "Update:*",
      "Principal": "*",
      "Resource" : "*"
    }
  ]
}
~~~

### Updating Protected Resources

You can update protected resources by lifting their protections with a temporary policy (You must have permission to the AWS CloudFormation SetStackPolicy action).

The override policy should specify an Allow for the protected resources that you want to update. The override policy is a temporary policy that is applied only during this update.

* If you want to update protected resources, specify a temporary overriding stack policy during this update.
* If you do not specify a stack policy, the current policy that is associated with the stack will be used.
* You can specify either the stack-policy-during-update-body or the stack-policy-during-update-url parameter, but not both.

`aws cloudformation update-stack --stack-policy-during-update-url file://stack_policy_tmp.json`

### Revove Stack Policies

you must update the stack with this policy:

~~~json
{
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : "Update:*",
      "Principal": "*",
      "Resource" : "*"
    }
  ]
}
~~~

## Update resources

Some test:

* change `DBClass` do not destroy the RDS instance, it enter into the "modifying" state. TODO: capire se i dati e gli snapshot vengono toccati.

## Backup and restore RDS snapshots

* [](http://blogs.aws.amazon.com/application-management/post/Tx2W35XGG70IIQI/Delete-Your-Stacks-But-Keep-Your-Data)

## AWS CLI for CloudFormation

[Doc](http://docs.aws.amazon.com/cli/latest/reference/cloudformation/index.html)

NOTE: use parameter type as much as possible, this will prevent most of the errors in a early stage of the creation procedure: http://blogs.aws.amazon.com/application-management/post/Tx3DV2UYG9SC38G/Using-the-New-CloudFormation-Parameter-Types

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

### Common Errors

####  Value of property SecurityGroupIds must be of type List of String

If SecGroup is a param of type list you should use `"SecurityGroupIds": { "Ref" : "SecGroup" }` instead of `"SecurityGroupIds": [{ "Ref" : "SecGroup" }]`.

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

## CloudFormation and RDS snapshots

http://blog.jasonantman.com/2014/12/aws-cloudformation-and-rds-snapshots/

## CloudFormation and OpsWorks

[AWS::OpsWorks::Stack Resource Type](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html)

# AWS support for docker

see _guides/docker.markdown



# Route 53

## Registar

In order for Route 53 DNS to become active for your application you need to tell your domain registrar (GoDaddy, DNSimple, NameCheap, 1&1 etc…) to use your hosted zone’s Route 53 nameservers.

## Redirect Naked/root domain to www

ref: https://devcenter.heroku.com/articles/route-53

Route 53 supports Alias records which use Amazon S3 static websites to dynamically resolve naked domains to their www counterparts using a 301 redirect. E.g. example.com to www.example.com.

name the bucket the exact same as the hosted zone. E.e. the hosted zone example.com and a bucket named example.com.

click the “properties tab” and open the “Static Website Hosting” section.
Click “Redirect all requests to another host name”, www.example.com will be pre-filled. If it is not, enter www.example.com here.

Save the redirect settings, then open your Route 53 hosted zone for example.com.
Create a new record set, leave the name blank, select A type. Turn alias to yes and select example.com from the S3 Website Endpoints section of the Alias Target dropdown.
