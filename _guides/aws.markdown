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


# AWS Security

* [FedRamp Compliance](http://d0.awsstatic.com/whitepapers/aws-architecture-and-security-recommendations-for-fedramp-compliance.pdf)

## Distribute Credentials or sensitive data on boot

Ref:

* [Old Post of 2009, but well done](http://shlomoswidler.com/2009/08/how-to-keep-your-aws-credentials-on-ec2.html), I think it's written before instances profiles.


Don't use `User-data`:

* Any user account able to open a socket on an EC2 instance can see the user-data by getting the URL http://169.254.169.254/latest/user-data . This is exploitable if a web application running in EC2 does not validate input before visiting a user-supplied URL. Accessing the user-data URL is particularly problematic if you use the user-data to pass in the secret unencrypted into the instance – one quick wget (or curl) command by any user and your secret is compromised. And, there is no way to clear the user-data – once it is set at launch time, it is visible for the entire life of the instance.



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

* [TODO](http://docs.aws.amazon.com/IAM/latest/UserGuide/PermissionsAndPolicies.html)
* [List of policies common errors](http://blogs.aws.amazon.com/security/post/Tx1LYOT2FQML4UG/Back-to-School-Understanding-the-IAM-Policy-Grammar)

A policy can be attached to:

* a group, a user
* a resource

Each policy have a `principal` which is the Identity to which the policy apply. The `Principal` element is unnecessary in an IAM policy attached directly to an Identity, because the principal is by default the entity that the IAM policy is attached to. It can be a IAM user, federated user, or assumed-role user), AWS account, AWS service, or other principal entity.

[AWS reference; Principal](http://docs.aws.amazon.com/IAM/latest/UserGuide/AccessPolicyLanguage_ElementDescriptions.html#Principal)

Pricipal examples:

~~~
"Principal": {
        "AWS": ["arn:aws:iam::111122223333:user/Alice",
                "arn:aws:iam::111122223333:root"]
      },
~~~

### Policy Version

Ref: http://docs.aws.amazon.com/IAM/latest/UserGuide/AccessPolicyLanguage_ElementDescriptions.html#Version

The only allowed values are these:

* `2012-10-17` This is the current version of the policy language, and you should use this version number for all policies.
* `2008-10-17` This was an earlier version of the policy language. You might see this version on existing policies. Do not use this version for any new policies or any existing policies that you are updating.

### S3 Policies

Ref:

* [S3 Resource doc](http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)
* [S3 Actions doc](http://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html)
* [ Grant access to user-specific folders in an Amazon S3 bucket](http://blogs.aws.amazon.com/security/post/Tx1P2T3LFXXCNB5/Writing-IAM-policies-Grant-access-to-user-specific-folders-in-an-Amazon-S3-bucke) 

~~~
{
      "Effect": "Allow",
      "Action": [
        "s3:ListAllMyBuckets",
        "s3:GetBucketLocation"
      ],
      "Resource": "arn:aws:s3:::*"
    },
    {
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::BUCKET-NAME",
      "Condition": {"StringLike": {"s3:prefix": [
        "",
        "home/",
        "home/${aws:username}/"
      ]}}
    },
    {
      "Effect": "Allow",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::BUCKET-NAME/home/${aws:username}",
        "arn:aws:s3:::BUCKET-NAME/home/${aws:username}/*"
      ]
    }
~~~

#### IAM Policy Simulator

[Simulator URL](https://policysim.aws.amazon.com/home/index.jsp?#)

* Select "Mode: new policy" from the dropdown menù
* Insert the PolicyDocument, ex:

~~~
{
  "Version" : "2012-10-17",
  "Statement": [ {
    "Effect": "Allow",
    "Action": ["s3:ListBucket","s3:GetObject","s3:GetObjectVersion"],
    "Resource": "arn:aws:s3:::testnicolaprovaa-21.aaa/*"
  } ]
}
~~~

* Set the resource you want to test in `Simulation Test`
* Set the service and the api you want to test
* Run the simulation

#### Test S3 with FOG


~~~
require 'fog'

path_style param solve ssl issues, see : http://stackoverflow.com/questions/18340551/amazon-s3-hostname-does-not-match-the-server-certificate-opensslsslsslerr

connection = Fog::Storage.new({
  :provider => 'AWS',
  :use_iam_profile => true,
  :region => "eu-west-1",
  :path_style => true  
})

connection.directories.get("testnicolaprovaa-21.aaa").files.each{ |f| puts f.key }
~~~


### S3: IAM Policies VS Bucket Policies VS S3 ACL

Ref: http://blogs.aws.amazon.com/security/post/TxPOJBY6FE360K/IAM-policies-and-Bucket-Policies-and-ACLs-Oh-My-Controlling-Access-to-S3-Resourc

If you’re unsure of which to use, consider which audit question is most important to you:

* If you’re more interested in “What can this user do in AWS?” then IAM policies are probably the way to go. You can easily answer this by looking up an IAM user and then examining their IAM policies to see what rights they have.
* If you’re more interested in “Who can access this S3 bucket?” then S3 bucket policies will likely suit you better. You can easily answer this by looking up a bucket and examining the bucket policy.
* If you want to manage permissions on individual objects within a bucket, S3 ACLs enable you to apply policies on the objects themselves, whereas bucket policies can only be applied at the bucket level.


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

## How to Keep Your AWS Credentials on an EC2 Instance Securely: Instance Profile and Roles

* https://aws.amazon.com/blogs/aws/iam-roles-for-ec2-instances-simplified-secure-access-to-aws-service-apis-from-ec2/
* http://shlomoswidler.com/2009/08/how-to-keep-your-aws-credentials-on-ec2.html

Basically EC2 will provide some local URL that the instance can use to retrieve credentials that are rotate periodically.

Ref: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html#instancedata-dynamic-data-retrieval

### Example Ruby Carrierwave setup

Ref: http://www.spacevatican.org/2012/6/25/iam-roles/

config/initializers/carrierwave.rb:

~~~
CarrierWave.configure do |config|
  config.storage = :fog
  config.fog_credentials = {
    :provider              => 'AWS',
    :aws_access_key_id     => ENV['AWS_ACCESS_KEY_ID'],
    :aws_secret_access_key => ENV['AWS_SECRET_ACCESS_KEY'],
    :region                => ENV['AWS_REGION'],
  }
  config.fog_directory = ENV['AWS_BUCKET']
end

See https://github.com/carrierwaveuploader/carrierwave#testing-with-carrierwave

if Rails.env.test?
  CarrierWave.configure do |config|
    config.storage = :file
    config.enable_processing = false
  end
en
~~~


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

# CloudWatch

## New Relic Plugin for AWS

* [Plugin Home Page](https://rpm.newrelic.com/accounts/1013453/plugins/directory/58)
* It's available also as chef cookbook, we integrate it into our deploy machine


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

#### Name Type

http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html

* For some resources, you can specify a custom name.
* By default, AWS CloudFormation generates a unique physical ID to name a resource.
* Resource names must be unique across all of your active stacks.
* You can't perform an update that causes a custom-named resource to be replaced.


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

* the intrinsic function `Fn::FindInMap`, it works like a Case statement or lookup table.
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
* http://cloudacademy.com/blog/understanding-nested-cloudformation-stacks/
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

`aws cloudformation update-stack --stack-policy-during-update-body file://stack_policy_tmp.json`

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

* [keep a snapshot when the entire stack is deleted](http://blogs.aws.amazon.com/application-management/post/Tx2W35XGG70IIQI/Delete-Your-Stacks-But-Keep-Your-Data)
* [Back and restore](http://blog.jasonantman.com/2014/12/aws-cloudformation-and-rds-snapshots/)

**WARNING** If you make a change to one of the DBInstance properties that requires a resource replacement to take effect, the RDS instance will be replaced with a new one, and **all of the data and automatic snapshots from the old one will be DELETED!!!**:

**Best Practice*** if you set `DBInstanceIdentifier` you cannot do updates that require this resource to be replaced. If you wanto to avoid any possibility that the DB is replaced give it a name

*  automatic snapshots (the daily ones created by RDS) are tied to the instance;
*  if the instance is replaced by CloudFormation, you lose all automatic (backup) snapshots with it.

Update a stack (built using a RDS snapshot), without losing data:

~~~
$ aws cloudformation update-stack --stack-name mystack --template-body file:///home/myuser/cloudformation_template.json --parameters ParameterKey=DBSnapshotIdentifier,UsePreviousValue=true
~~~

Load a RDS snapshot into an existing stack (that isn’t already using this snapshot):

~~~
$ aws cloudformation update-stack --stack-name mystack --template-body file:///home/myuser/cloudformation_template.json --parameters ParameterKey=DBSnapshotIdentifier,ParameterValue='my-snapshot-identifier'
~~~

Load a RDS snapshot into an existing stack again (i.e. restore from the same snapshot a second time; this one is a kludge):

~~~
$ # re-create the RDS instance with a blank DB (DBName)
$ aws cloudformation update-stack --stack-name mystack --template-body file:///home/myuser/cloudformation_template.json --parameters ParameterKey=DBSnapshotIdentifier,ParameterValue=''
$ # then load the snapshot again
$ aws cloudformation update-stack --stack-name mystack --template-body file:///home/myuser/cloudformation_template.json --parameters ParameterKey=DBSnapshotIdentifier,ParameterValue='my-snapshot-identifier'
~~~


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

## CloudFormation and OpsWorks

[AWS::OpsWorks::Stack Resource Type](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html)

# AWS support for docker

see _guides/docker.markdown

# VPC (Virtual Private Cloud)

* [Short video intro](http://aws.amazon.com/training/intro_series/)
* [AWS VPC DOC](http://aws.amazon.com/vpc/)
* [VPC limits](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Appendix_Limits.html)

Amazon VPC lets you provision a logically isolated section of the Amazon Web Services (AWS) Cloud where you can launch AWS resources in a virtual network that you define. 


Your AWS resources are automatically provisioned in a ready-to-use default VPC that was created for you.

NOTE: the ADDICTIVE AWS account supports only VPC (not EC2 Classic)

## Topology

* a `VPC` has 1 `region`
* a `subnet` has 1 `route table`
* a `subnet` has 1 `availablity zone`
* `route table` has N `subnet`

### Topology best practices

When creating separate subnets for ELB, EC2 and RDS instances, each tier should have at least 2 subnets across availability zones.

For this example, we created subnets using zones us-east1b and us-east-1d. These subnets are called “private subnets” because the instances we launch are not accessible from the Internet. In other words, these instances don’t have a public IP unless you assign an EIP.

* App Tier: 10.0.1.0/24(zone-b), 10.0.2.0/24(zone-d)
* ELB: 10.0.51.0/24(zone-b), 10.0.52.0/24(zone-d)
* Database (RDS): 10.0.11.0/24(zone-b), 10.0.12.0/24(zone-d)

best practices:

* create separate route tables for each tier.
* Always choose the same availability zones for all tiers.


ELB: 

* For an Internet-facing load balancer to be connected to the Internet, the load balancer must reside in a subnet that is connected to the Internet using the Internet gateway.
* The application instances behind the load balancer do not need to be in the same subnet as the load balancer.

## Subnet


NOTE: Cidr notation: http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing  ( For example, in IPv4, a prefix size of /29 gives: 2^(32-29) = 2^3 = 8 addresses.)

Public VS private VS VPN-only, depends from the subnet's route table:

* If a subnet's traffic is routed to an Internet gateway, the subnet is known as a public subnet.
* If a subnet doesn't have a route to the Internet gateway, the subnet is known as a private subnet.
* If a subnet doesn't have a route to the Internet gateway, but has its traffic routed to a virtual private gateway, the subnet is known as a VPN-only subnet.



## Gateway

### Internet gateway

An Internet gateway is a horizontally scaled, redundant, and highly available VPC component that allows communication between instances in your VPC and the Internet. 

The iternet gateway is used by:

* the route table
* NAT instances

### Private Gateway

## Security

* at instance level: `security groups`
* at subnet level: `ACLs` 


## VPN

TODO

# RDS

## RDS and VPC

* Your VPC must have at least 1 subnet in at least 2 of the Availability Zones in the region where you want to deploy your DB instance.
* Your VPC must have a `DB subnet group` that you create

# ELB - Elastic Load Balancer

Elastic Load Balancing automatically distributes incoming web traffic across multiple EC2 instances.

Common Listener configurations: http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/using-elb-listenerconfig-quickref.html

## ELB in a VPC

## Registering / Deregistering Instances

* you MUST add ALL the subnets of the instances you want to connect to your ELB.
* Register instances: ELB use the IP address associated with an instance to drive traffic to it.

* restart instances: if you restart an instance in VPN it's private IP doen't change (TODO:and it's public IP??? ), so you don't need to reregister it but reregister reduce the time the ELB took to detect the recovered instance.


## Best practiecs for Web server behind an ELB


## ELB Cross-Zone load balancing

* http://aws.amazon.com/about-aws/whats-new/2013/11/06/elastic-load-balancing-adds-cross-zone-load-balancing/

When `Cross-Zone load balancing` is OFF:

* Incoming traffic is load balanced equally across all Availability Zones enabled for your load balancer, so it is important to have approximately equivalent numbers of instances in each zone.
* For example, if I have 4 instances (a1, a2, a3, a4) in zone us-east-1a and a single instance d1 in us-east-1d behind an ELB, d1 would get nearly 50% of the traffic.


When `Cross-Zone load balancing` is ON:

* incoming traffic is routed evenly across all back-end instances, **regardless of the Availability Zone**.
* For example, if I have 4 instances (a1, a2, a3, a4) in zone us-east-1a and a single instance d1 in us-east-1d behind an ELB, d1 would get nearly 20% of the traffic.
* http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/TerminologyandKeyConcepts.html#request-routing


http://stackoverflow.com/questions/11424481/aws-elastic-load-balancer-and-multiple-availability-zones

## ELB and Autoscaling groups

If you have associated your Auto Scaling group with a load balancer, you can use the load balancer health check to determine the health state of instances in your Auto Scaling group.

REF: http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/TerminologyandKeyConcepts.html#healthcheck

## Connection Draining

If connection draining is enabled, when an instance is deregisted, existing connection will be kept open for a configurable amount of time.

## Monitoring and Log

REF:

* http://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/elb-monitor-logs.html


# Autoscaling

[AWS Doc](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/WhatIsAutoScaling.html)

Auto Scaling Components:

* Groups
* Launch configurations
* Scaling plans

* a group has 1 launch configuration

* Auto Scaling groups can scale across multiple Availability Zones within a region.
  * Auto Scaling attempts to distribute instances evenly between the Availability Zones
  * For each instance that Auto Scaling launches in a VPC, it selects a subnet from the Availability Zone at random.
* Auto Scaling groups cannot span multiple regions.
* For Auto Scaling groups in a VPC, the EC2 instances are launched in subnets.

## Group

Is a collection of EC2 instances that share similar characteristics and are treated as a logical grouping for the purposes of instance scaling and management.

Params:

* a name
* launch configuration
* minimum number of instances
* and maximum number of instances.

To update the lauch config:

* create a new launch config
* update the group
* new instances are launched using the new configuration parameters, but existing instances are not affected (terminate them you want to update also existing one).

## Launch Configurations

Your group uses a launch configuration as a template for its EC2 instances:

* the AMI ID,
* instance type,
* key pair,
* security groups,
* block device mapping for your instances.

You can't modify a launch configuration after you've created it.

## Health

An Autoscaling Group can check the health of EC2 instances using:

* EC2 instance status checks (default).
  * If the instance status is any state other than `running` or if the system status is `impaired`, Auto Scaling considers the instance to be unhealthy and launches a replacement.
* ELB metrics (default if)

Note: also the ELB check the health of EC2 instances registered with the ELB

## Planning Autoscaling Groups

### Scaling Plan

You can have different scaling strategies:

* none: just keep a fixed number of instances
* manual: manually enter maximum, minimum, or desired capacity. At any time, you can manually change the size of an existing Auto Scaling group
* scheduled
* on demand

### Cooldowns

[DOC](http://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/Cooldown.html)

* Use case: give time to new/old instances to launch or terminate before reevaluate the group status and take new actions.
* The Auto Scaling `cooldown period` is a configurable setting that determines when Auto Scaling should suspend any scaling activities related to a specific Auto Scaling group.
* It start when any scaling activity happen
* default: 300 seconds


Lifecycle Hooks:

* The cooldown period for the Auto Scaling group does not begin until after the instance moves out of the wait state.

### Termination Policy

[Doc](http://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/AutoScalingBehavior.InstanceTermination.html)

When the group must scale in, the `termination policy` is applied to select which instances should be terminated.

Auto Scaling currently supports the following custom termination policies:

* `Default` Auto Scaling uses its default termination policy (see doc for a full description):
  * ensure that your network architecture spans Availability Zones evenly
  * try remove instance oldest launch configuration.
  * try to remove first instances are closest to the next billing hour

* `OldestInstance` Auto Scaling terminates the oldest instance in the group. This option is useful when you're upgrading the instances in the Auto Scaling group to a new EC2 instance type, and want to eventually replace instances with older instances with newer ones.

* `NewestInstance` Auto Scaling terminates the newest instance in the group. This policy is useful when you're testing a new launch configuration but don't want to keep it in production.

* `OldestLaunchConfiguration` Auto Scaling terminates instances that have the oldest launch configuration. This policy is useful when you're updating a group and phasing out the instances from a previous configuration.

* `ClosestToNextInstanceHour` Auto Scaling terminates instances that are closest to the next billing hour. This policy helps you maximize the use of your instances and manage costs.



### ELB: Load Balancing a Group

[Doc](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/US_SetUpASLBApp.html)

* an Auto Scaling group can register to N ELB.
* ELB send metrics in real time to CloudWatch

### Autoscaling and VPC

[Doc](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/autoscalingsubnets.html)

TODO

# Route 53

## Registar

In order for Route 53 DNS to become active for your application you need to tell your domain registrar (GoDaddy, DNSimple, NameCheap, 1&1 etc…) to use your hosted zone’s Route 53 nameservers.

## Redirect Naked/root domain to www

ref:

* [AWS Doc](http://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html)
* https://devcenter.heroku.com/articles/route-53

Route 53 supports Alias records which use Amazon S3 static websites to dynamically resolve naked domains to their www counterparts using a 301 redirect. E.g. example.com to www.example.com.

name the bucket the exact same as the hosted zone. E.e. the hosted zone example.com and a bucket named example.com.

click the “properties tab” and open the “Static Website Hosting” section.
Click “Redirect all requests to another host name”, www.example.com will be pre-filled. If it is not, enter www.example.com here.

Save the redirect settings, then open your Route 53 hosted zone for example.com.
Create a new record set, leave the name blank, select A type. Turn alias to yes and select example.com from the S3 Website Endpoints section of the Alias Target dropdown.

# S3

## Access Control to S3 Buckets 

REF:

* http://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html
* [How S3 authorize a request](http://docs.aws.amazon.com/AmazonS3/latest/dev/how-s3-evaluates-access-control.html)

By default, all Amazon S3 resources—buckets, objects, and related subresources are private.

* You can associate an access policy with a resource (bucket and object) or a user.

http://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-overview.html#access-control-resources-manage-permissions-basics


### Using User or Bucket Policy

Access policy language:

* [AWS DOC](http://docs.aws.amazon.com/AmazonS3/latest/dev/access-policy-language-overview.html)
* can specify: 
  * resources
  * actions
  * effect: Allow/Deny
  * principal: specifies the user, account, service, or other entity that is allowed or denied access to a resource (not required for a policy attached to users, groups, roles)
  * permissions: s3:GetObject, s3:PutObject, etc ( [AWS Ref](http://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html) )
  * conditions [AWS ref](http://docs.aws.amazon.com/AmazonS3/latest/dev/amazon-s3-policy-keys.html)

Policy can be attached to:

* bucket: [Example](http://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html)
  * Note: You attach S3 bucket policies at the bucket level (i.e. you can’t attach a bucket policy to an S3 object), but the permissions specified in the bucket policy apply to all the objects in the bucket.
  * Note: includes a “Principal” element, which lists the principals that bucket policy controls access for.
* users: [Example](http://docs.aws.amazon.com/AmazonS3/latest/dev/example-policies-s3.html)

Sample bucket policy:

~~~
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": ["arn:aws:iam::111122223333:user/Alice",
                "arn:aws:iam::111122223333:root"]
      },
      "Action": "s3:*",
      "Resource": ["arn:aws:s3:::my_bucket",
                   "arn:aws:s3:::my_bucket/*"]
    }
  ]
}
~~~

### Using S3 ACL

REF: [AWS Doc](http://docs.aws.amazon.com/AmazonS3/latest/dev/S3_ACLs_UsingACLs.html)

As a general rule, AWS recommends using S3 bucket policies or IAM policies for access control. S3 ACLs is a legacy access control mechanism that predates IAM. However, if you already use S3 ACLs and you find them sufficient, there is no need to change.

An S3 ACL is a sub-resource that’s attached to every S3 bucket and object. It defines which AWS accounts or groups are granted access and the type of access. When you create a bucket or an object, Amazon S3 creates a default ACL that grants the resource owner full control over the resource.


* Canned ACL: http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl

### How does authorization work with multiple access control mechanisms?

Whenever an AWS principal issues a request to S3, the authorization decision depends on the union of all the IAM policies, S3 bucket policies, and S3 ACLs that apply.

In accordance with the principle of least-privilege, decisions default to DENY and an explicit DENY always trumps an ALLOW. For example, if an IAM policy grants access to an object, the S3 bucket policies denies access to that object, and there is no S3 ACL, then access will be denied. Similarly, if no method specifies an ALLOW, then the request will be denied by default. Only if no method specifies a DENY and one or more methods specify an ALLOW will the request will be allowed.

### Guidelines: When to use IAM User policies vs. S3 Bucket policies VS ACL

Use IAM policies if:

* You need to control access to AWS services other than S3. IAM policies will be easier to manage since you can centrally manage all of your permissions in IAM instead of spreading them between IAM and S3.
* You have numerous S3 buckets each with different permissions requirements. IAM policies will be easier to manage since you don’t have to define a large number of S3 bucket policies and can instead rely on fewer, more detailed IAM policies.
* You prefer to keep access control policies in the IAM environment.

Use S3 bucket policies if:

* You want a simple way to grant cross-account access to your S3 environment, without using IAM roles.
* Your IAM policies bump up against the size limit (up to 2 kb for users, 5 kb for groups, and 10 kb for roles). S3 supports bucket policies of up 20 kb.
* You prefer to keep access control policies in the S3 environment.

If you’re still unsure of which to use, consider which audit question is most important to you:

* If you’re more interested in “What can this user do in AWS?” then IAM policies are probably the way to go. You can easily answer this by looking up an IAM user and then examining their IAM policies to see what rights they have.
* If you’re more interested in “Who can access this S3 bucket?” then S3 bucket policies will likely suit you better. You can easily answer this by looking up a bucket and examining the bucket policy.

Whichever you method you choose, we recommend staying as consistent as possible. Auditing permissions becomes more challenging as the number of IAM policies and S3 bucket policies grows.

## Hosting a public Static Website

REF: [AWS doc](http://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html)

For naked domain redirect see [here]({{ site.url }}/guides/aws.html#redirect-nakedroot-domain-to-www)

The website is then available at the region-specific website endpoint of the bucket:

`<bucket-name>.s3-website-<AWS-region>.amazonaws.com`

* Permission required for a public website using bucket policies [AWS Ref](http://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteAccessPermissionsReqd.html)

~~~
{
  "Version":"2012-10-17",
  "Statement":[{
	"Sid":"PublicReadGetObject",
        "Effect":"Allow",
	  "Principal": "*",
      "Action":["s3:GetObject"],
      "Resource":["arn:aws:s3:::example-bucket/*"
      ]
    }
  ]
}
~~~



Cloudfomation tempate example:

* see the `addictive-api-cloudformation` git repo
* `aws cloudformation create-stack  --profile=pt --capabilities CAPABILITY_IAM --stack-name  PitchTargetAlphaS3Frontend20150531 --template-body file://pitchtarget_template_s3_static_website_only.json --parameters ParameterKey=S3BucketName,ParameterValue=alpha.pitchtarget.com` 


### Create a Bucket Policy for a deploy user


## Hosting a private website with basic auth

* Use `http://www.s3auth.com/`

To create a user:

`htpasswd -nbs my_user my_password > .htpasswd`

To append a user: 

`htpasswd -nbs my_user my_password >> .htpasswd`


### Example

For example to deploy the Ember app on  `alpha.pitchtarget.com`:
 
* `aws cloudformation create-stack  --profile=pt --capabilities CAPABILITY_IAM --stack-name  PitchTargetAlphaS3Frontend20150531 --template-body file://pitchtarget_template_s3_static_website_only.json --parameters ParameterKey=S3BucketName,ParameterValue=alpha.pitchtarget.com`
* Create the `alpha` CNAME on the DNS with value: `alpha.pitchtarget.com.s3-website-eu-west-1.amazonaws.com`. You can read the CNAME value from the stack output.

WARNING: the bucket name must match the virtual host, see [here](http://docs.aws.amazon.com/AmazonS3/latest/dev/VirtualHosting.html#VirtualHostingCustomURLs) for more details.

TODO: capire bene le policy da mettere



# EC2

TODO: is it possible to use cfn-hup to update users and groups ?

## Metadata

* http://blog.domenech.org/2012/10/aws-ec2-instance-metadata.html
* http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html

[cfn-hup doc](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-hup.html)

cfn-hup helper is a daemon that detects changes in resource metadata and runs user-specified actions when a change is detected.

## Cloud-init


Add users: http://cloudinit.readthedocs.org/en/latest/topics/examples.html#including-users-and-groups

# Elastic Beanstalk


* See `eb config` to manage multimple env easly


## Docker Multi Container

### Save Container Log in volumes

* In this example 2 volumes are created and then mounted.
* The mounting points depends on the container, you should map the proper directory
* `/var/app/current` is always available on docker multicontainer host
  * `/var/app/current/nginx` and `/var/app/current/webapp` are automatically created if doesn't exists.


~~~
{
  "volumes": [
    {
      "name": "nginx",
      "host": {
        "sourcePath": "/var/app/current/nginx"
      }
    },
    {
      "name": "webapp",
      "host": {
        "sourcePath": "/var/app/current/webapp"
      }
    } 
  ],
  "containerDefinitions": [
    {
      "mountPoints": [
        {
          "sourceVolume": "nginx",
          "containerPath": "/var/log/nginx/"
        },
        {
          "sourceVolume": "webapp",
          "containerPath": "/home/app/webapp/log"
        }
      ]
    }
  ]
}
~~~




## EB CLI 3 and AWS CLI

Credentials:

* http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-configuration.html#eb-cli3-credentials
* The EB CLI uses the same credentials storage as the AWS CLI and AWS SDKs.
* NOTE: you can use also the `--profile` option

Getting Started:

* http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-getting-started.html
* `eb init myapp -l pitch-target -p "Multi-container Docker" --profile=pt`: create myapp with platform docker 
* `eb create my-env`: create a new env


### eb init command

When you run `eb init` it will create `.elasticbeanstalk/config.yml` 

~~~
branch-defaults:
  default:
    environment: dev-env
global:
  application_name: test_eb
  default_ec2_keyname: pitch-target
  default_platform: Docker 1.6.0
  default_region: null
  profile: pt
  sc: null
~~~

You can choose if you want to configure you local directory to interact with an existing app or create a new one.

### eb config 

To easly recreate a copy of an environment. You can save the configuration from an environment updload them to another:

* `eb config save <OLD_ENV> --cfg old_config`
* `eb create --cfg old_config <NEW_ENV>`

NOTE: to see a list of all available EB Stacks 

* `aws elasticbeanstalk list-available-solution-stacks --profile=pt`

#### Clone and modify an old_config to create a new env

* get it locally: `eb config get <old_config>` will save it into `.elasticbeanstalk/saved_configs/prova-sc.cfg.yml`
* rename it (keeping the extension `cfg.yml`): `cp .elasticbeanstalk/saved_configs/old_config.cfg.yml .elasticbeanstalk/saved_configs/prova-sc.cfg.yml `
* Do your changes
* put it online: `eb config put prova-sc` 


#### List configurations

To List configurations: `eb config list`



Note: Configurations for a given region are stored into this S3 bucket `elasticbeanstalk-eu-west-1-470031436598/resources/templates`

#### Copy configurations to another APP

If you want to copy a configuration from an application to another, you can save it locally and then copy the saved_configs dir:

* `cp -r EXISTING_APP/.elasticbeanstalk/saved_configs NEW_APP/.elasticbeanstalk/`
* `cd NEW_APP`
* `eb config put my_config` 

### eb create

`eb create --cfg production --version 5914 addictive-api-prod`

### EB Docker multi container (ECS)

`eb init myapp -l pitch-target -p "Multi-container Docker" --profile=pt`: create myapp with platform docker 

Example App: https://github.com/awslabs/eb-docker-nginx-proxy

`Dockerfile and Dockerrun.aws.json are both missing, abort deployment`

* When you create a "Multi-container Docker" EB env, EB will create a cluster
* When you deploy a new version of the app into an environment a new Task Definition is created into the ECS cluster and task are restarted.


`Dockerrun.aws.json` :

* describes the containers to deploy
* data volumes to create on the host instance for the containers to mount
* zipped up with additional source code in a single archive
* Source code that is archived with a Dockerrun.aws.json is deployed to container instances and accessible in the `/var/app/current/` directory

EB role is `aws-elasticbeanstalk-ec2-role`, you need to attach this policy once http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_docker_ecstutorial.html#create_deploy_docker_ecstutorial_role

#### Container Env

To add container env variables, use `.ebextensions/XX_YYYYY.config` :

~~~
option_settings:  
  - option_name: MY_VAR
    value: INCREDIBLEMOLK
~~~

if you log to the ecs console you will see that the variable is avalilable into the container.

### Get/set Environment variables

* `eb ` 
* `eb printenv  aaa-env`
* `eb setenv PIPPO=a PLUTO=b -e aaa-env`



#### Containers Log

Capire come sono organizzati in `/var/log/containers`

#### Container command

http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customize-containers-ec2.html#customize-containers-format-container_commands

#### ALL OPTION Settings

http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html

#### Private Docker Registry

* https://www.youtube.com/watch?v=pLw6MLqwmew&feature=youtu.be

* To use a private repository hosted by a third-party registry, you must provide a JSON file called `.dockercfg` with information required to authenticate with the repository.

* Run `docker login` from your workstation for dockerhub or run `docker login server_name` for other registries
* Upload `~/.dockercfg` to a private S3 bucket
  * create bucket `pt-eb-docker-private-registry-credentials`
  * create folder `breezeight`
  * upload the file with `Use Server Side Encryption`
* the S3 bucket must be hosted in the same region as the environment that is using it.
* Allow `s3:GetObject` on  `arn:aws:s3:::pt-eb-docker-private-registry-credentials/breezeight/dockercfg` to the EB instance profile `aws-elasticbeanstalk-ec2-role` (this is the default role, you could use a different one)

~~~
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Stmt1432493167000",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::pt-eb-docker-private-registry-credentials/breezeight/dockercfg"
            ]
        }
    ]
}
~~~

* Declare the .dockercfg file in the Dockerrun.aws.json file. Make sure that the .dockercfg file contains a valid Amazon S3 bucket and Amazon EC2 key pair. `Dockerrun.aws.json` example snippet:

~~~
{
  "AWSEBDockerrunVersion": 2,
  "authentication": {
    "bucket": "pt-eb-docker-private-registry-credentials",
    "key": "breezeight/.dockercfg"
  },
  "volumes": [
    {
      "name": "php-app",
      "host": {
        "sourcePath": "/var/app/current/php-app"
      }
    },
    {
      "name": "nginx-proxy-conf",
      "host": {
        "sourcePath": "/var/app/current/proxy/conf.d"
      }
    }  
  ],
  "containerDefinitions": [
    {
      "name": "addictive-api-production",
      "image": "breezeight/addictive-api-production:latest",
      "memory": 128,
      "essential": true
    }
  ]
}
~~~

TIP: to test policies: `aws s3 cp s3://pt-eb-docker-private-registry-credentials/breezeight/dockercfg .`


### EB ssh

`eb ssh` to quickly ssh into one of the machine

## Ebextension

Misc Notes: 

* When you run a container_command, the application is already inflated into `/var/app/staging/`
* the current working dir is `/var/app/staging/`
* the user is `root` 
* the environment has all the variable defined for the EB environment.


### Example: define a script

* create scripts/test.sh
* `chmod +x script/test.sh`
* run it .ebextensions/01_migrations.config 

~~~
container_commands:
  rails_migration:
    command: >
      scripts/test.sh  
    leader_only: true
~~~

NOTE: `>` is a yaml trick to merge line with spaces.

### ebextension to define resources like CloudFormation

ELB uses the same configuration management and resource setup as the CloudFormation service. see here : http://www.delarre.net/posts/elasticbeanstalk-vpc-fun/

You can use the ebextension directory to define resources with the same syntax of Cloudformation. Here http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customize-environment-resources-elasticache.html

In your extension file you can reference resources create by EB, the list is here: http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-resources.html

WARNING: if you set configuration from the web console those values will override those in the ebextension dir

example `.ebextensions/02_load_balancer.config` :


~~~
"Resources" : {
  "AWSEBLoadBalancerSecurityGroup": {
    "Type" : "AWS::EC2::SecurityGroup",
    "Properties" : {
      "GroupDescription" : "Enable 80 inbound and 8080 outbound",
      "VpcId": "vpc-un1que1d",
      "SecurityGroupIngress" : [ {
        "IpProtocol" : "tcp",
        "FromPort" : "80",
        "ToPort" : "80",
        "CidrIp" : "0.0.0.0/0"
      }],
      "SecurityGroupEgress": [ {
        "IpProtocol" : "tcp",
        "FromPort" : "8080",
        "ToPort" : "8080",
        "CidrIp" : "0.0.0.0/0"
      } ]
    }
  },
  "AWSEBLoadBalancer" : {
    "Type" : "AWS::ElasticLoadBalancing::LoadBalancer",
    "Properties" : {
      "Subnets": ["subnet-un1que1d2"],
      "Listeners" : [ {
        "LoadBalancerPort" : "80",
        "InstancePort" : "8080",
        "Protocol" : "HTTP"
      } ]
    }
  }
}
~~~

## Hooks

**WARNING** this is an undocumented feature, it's useful more for debug, it could change in the future.

* `/opt/elasticbeanstalk/hooks`: hooks directory
* https://forums.aws.amazon.com/thread.jspa?threadID=137136

### Undocumented Snipped found reading the hooks source code

* `/opt/elasticbeanstalk/bin/get-config container -k ecs_task_arn_file`: 

## EB Worker Tier

* [AWS DOC](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features-managing-env-tiers.html)

### Periodic Task - Cron

`cron.yaml`


### Rails Migration on Docker Multi Container

#### Parse the Dockerrun.aws.json and docker run a container from the addictive-api image

**HACK**this is a trick to run migration from the rails image defined in your Dockerrun.aws.json.


**NOTE**: actually this is the best solution

.ebextensions/01_migrations.config:

~~~
container_commands:
  rails_migration:
    command: >
      scripts/migrate_database.sh
    leader_only: true
~~~

In `scripts/migrate_database.sh` you must set your task definition name into `CONTAINER_DEFINITION_NAME`:

~~~
#!/bin/bash

env > scripts/env

#Your rails container definition
CONTAINER_DEFINITION_NAME=addictive-api-production

S3_BUCKET=`cat Dockerrun.aws.json | jq -r .authentication.bucket`
S3_KEY=`cat Dockerrun.aws.json | jq -r .authentication.key`
DOCKER_IMAGE=`cat Dockerrun.aws.json | jq .containerDefinitions | jq ".[] | select(.name | contains(\"$CONTAINER_DEFINITION_NAME\"))" | jq -r .image` 

aws s3 cp s3://$S3_BUCKET/$S3_KEY ~/.dockercfg 
docker ps > /tmp/docker_ps
docker run --rm --env-file=scripts/env $DOCKER_IMAGE bundle exec rake db:migrate:status > /tmp/migration_status

~~~

#### Use Docker exec

**ISSUES** DO NOT USE IT:

* "Command" run before the application and web server are set up and the application version file is extracted. So we are running migration from the previous app version
* it doesn't work on a new instance


**HACK**

I cannot manage to run a command on specific container... I fall back on this hack using `.ebextensions/01_migration.config`:

~~~
commands:
  rails_migration:
    command: docker exec `docker ps|grep addictive-api-prod|awk -F" " '{print $1}'` bundle exec rake db:migrate 
    leader_only: true

~~~

Basically we grep the name of the containter we want to use to exec the migration rake task.

**WARNING** : this could broke if EB will change the naming convention...

## EB Agent Debug and internals

### Debug ebextensions

When a script in ebextensions fails you can check the `/var/log/eb-activity.log` log.

log lines are tagged, for example the script `/opt/elasticbeanstalk/hooks/appdeploy/pre/01unzip.sh` will be tagged with `CMD-AppDeploy/AppDeployStage0/AppDeployPreHook/01unzip.sh`


Execution order:

* CMD-Startup/StartupStage1/AppDeployEnactHook/02update-credentials.sh
* 


# ECS

* [Components of ECS](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)

ECS is a container management service

## cloud formation and ECS

### ECS default cloudformation template

The ECS getting started created an example cloudformation stack. It is a good starting point to create other stacks

To download this default cluster template:

`aws cloudformation --profile=pt get-template --stack-name EC2ContainerService-default-4e359b92-83d2-4528-943d-f8e458d1428e`

These template can work with an existing VPC o it can create a new one:

* if you don't provide a `VpcId` the `CreateVpcResources` condition is true. A VPC will be created with 2 public subnet `PubSubnetAz1` and `PubSubnetAz2` in zones A and B, associated with the `RouteViaIgw` RouteTable. A new gateway `InternetGateway` is created and use by the `PublibRouteViaIgw` Route of the `RouteViaIgw` RouteTable.


CreateElasticLoadBalancer

* the autoscaling lauch configuration use the `EcsClusterName` param, set the `ecs.config` and 


EcsInstanceAsg :

* VPCZoneIdentifier (list of subnet identifiers).... what is the best strategy to manage AvailabilityZones ??? Mi sembra che questo template sia vincolato ad usare 2 zone e faccia l'assunzione che le subnet debbano essere nelle zone A e B



Params:

* KeyName pitch-target
* SourceCidr 0.0.0.0/0
* IamRoleInstanceProfile ecsInstanceRole

### ECS pitchtarget cloudformation template

Difference from the default:

* works only with an existing VPC (I want to simplify the template and I refactored out the VPC definition), Elb and EC2 security groups are params
* The ECS cluster name is required and don't have a default

TODO: require a private docker registry


## Private Registry

* [How to store registry credentials on S3](https://aws.amazon.com/blogs/aws/ec2-container-service-ecs-update-access-private-docker-repos-mount-volumes-in-containers/)
* [ECS doc for private registry](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/private-auth.html)

### Create a private registry with s3 backend

http://romain.dorgueil.net/blog/en/docker/2014/12/21/docker-registry-amazon-s3-storage-backend.html

## Agent introspection

ssh -i ~/.ssh/pitch-target.pem ec2-user@<HOST>


## IAM Roles and policies for ECS

http://docs.aws.amazon.com/AmazonECS/latest/developerguide/IAM_policies.html

I created:

* `ecsInstanceRole` role with `AmazonEC2ContainerServiceforEC2Role` managed policy that allow the instance's agent to register with the cluster and do basic administration.
* `ecs-service-role` role with `AmazonEC2ContainerServiceRole` managed policy that allow a service to register and derigister instances from a ELB.

## Task Definition Management


Deregister a task: `aws ecs deregister-task-definition --task-definition console-sample-app-static  --profile=pt`

## Describe clusters, tasks, services



## Scheduling tasks

TODO:

* Algorithm: What is the scheduling algorithm of default Amazon ECS scheduler? 
 * The ECS " run-task " call uses random placement to schedule your tasks.
 * [REF: aws ecs forum](https://forums.aws.amazon.com/thread.jspa?messageID=603806&#603806)


### Service

~~~
{
    "cluster": "", 
    "serviceName": "", 
    "taskDefinition": "", 
    "loadBalancers": [
        {
            "loadBalancerName": "", 
            "containerName": "", 
            "containerPort": 0
        }
    ], 
    "desiredCount": 0, 
    "clientToken": "", 
    "role": ""
}
~~~

You can specify the following parameters in a service definition.

cluster
The short name or full Amazon Resource Name (ARN) of the cluster on which to run your service on. If you do not specify a cluster, the default cluster is assumed.

serviceName
The name of your service. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.

taskDefinition
The family and revision (family:revision) or full Amazon Resource Name (ARN) of the task definition that you want to run in your service.

loadBalancers
A list of load balancer objects to use with your service. Currently you are limited to one load balancer per service.

loadBalancerName
The name of the load balancer.

containerName
The name of the container (as it appears in a container definition) to associate with the load balancer.

containerPort
The port on the container to associate with the load balancer.

desiredCount
The number of instantiations of the specified task definition to place and keep running on your cluster.

clientToken
Unique, case-sensitive identifier you provide to ensure the idempotency of the request. Up to 32 ASCII characters are allowed.

role
The name or full Amazon Resource Name (ARN) of the IAM role that allows your Amazon ECS container agent to make calls to your load balancer on your behalf. This parameter is only required if you are using a load balancer with your service.

#### Update a Service

* https://forums.aws.amazon.com/thread.jspa?messageID=613494&#613494
* http://blogs.aws.amazon.com/application-management/post/Tx32RHFZHXY6ME1/Set-up-a-build-pipeline-with-Jenkins-and-Amazon-ECS

TODO READ THIS DISCUSSION and THE JENKINS BLOG POST: https://forums.aws.amazon.com/thread.jspa?threadID=179271&tstart=0


Service Deployment [Doc](http://docs.aws.amazon.com/cli/latest/reference/ecs/describe-services.html)

The status of the deployment can be:

* `PRIMARY` (for the most recent deployment)
* `ACTIVE` (for previous deployments that still have tasks running, but are being replaced with the PRIMARY deployment)
* `INACTIVE` (for deployments that have been completely replaced).

#### Service ELB

* ELB: currently supports a fixed relationship between the load balancer port and the container instance port. (it is not possible to map the load balancer port 80 to port 3030 on one container instance and port 4040 on another container instance.)
* All of the containers that are launched in a single task definition are always placed on the same container instance. If the container definition exposes multiple ports you can add multiple listener ports to the load balancer.
* There is a limit of one load balancer per service.

TODO: 

* is the ELB check different from the container check (sse the essential param of the task definition)? 
* How many task with the same task-definition can run in a single container instance? 
* VPC and SUbnet: how to use them ?
  * select at least two subnets in different Availability Zones. Your selected subnets must at least include any subnet that your container instances reside in.



### Health check of container

* If a task in a service becomes unhealthy or unresponsive, the task is killed and restarted.
* This process continues until your service reaches the number of desired running tasks.

TODO:

* Which kind of check does it performe?
*

### Running Task

## Autoscaling ECS containers

TODO: https://forums.aws.amazon.com/thread.jspa?threadID=179401&tstart=0  or read the use of LAMBDA in the ecs blog

## Rails deploy

TODO:

* TEST a rails app with a docker image and an ELB
* Use AWS ruby sdk and rake to run a deploy
* How to run migrations? 
 * run migration from a CI server
 * detect pending migration from the healtcheck
* How do we update an image?
* build image with jenkins: https://blogs.aws.amazon.com/application-management/post/Tx32RHFZHXY6ME1/Set-up-a-build-pipeline-with-Jenkins-and-Amazon-ECS

Registry:

* We could try to use DockerHUB which has 1 private repo for free. The cons is the highest latency when a new machine need to download an image.
* Next step is to use learn how to setup a private repo.


NOTE: a service must have role `ecs-service-role` to interact with the ELB


Problemi riscontrati:



* We cannot update a service with a task that expose a port if we don't have at least 1 free instance to start the rollout:

~~~
{
    "services": [
        {
            "status": "ACTIVE", 
            "taskDefinition": "arn:aws:ecs:eu-west-1:470031436598:task-definition/console-sample-app-static:3", 
            "pendingCount": 0, 
            "loadBalancers": [], 
            "desiredCount": 3, 
            "serviceName": "80", 
            "clusterArn": "arn:aws:ecs:eu-west-1:470031436598:cluster/default", 
            "serviceArn": "arn:aws:ecs:eu-west-1:470031436598:service/80", 
            "deployments": [
                {
                    "status": "PRIMARY", 
                    "pendingCount": 0, 
                    "createdAt": 1429297790.558, 
                    "desiredCount": 3, 
                    "taskDefinition": "arn:aws:ecs:eu-west-1:470031436598:task-definition/console-sample-app-static:3", 
                    "updatedAt": 1429297790.558, 
                    "id": "ecs-svc/9223370607556985249", 
                    "runningCount": 0
                }, 
                {
                    "status": "ACTIVE", 
                    "pendingCount": 0, 
                    "createdAt": 1429296258.008, 
                    "desiredCount": 3, 
                    "taskDefinition": "arn:aws:ecs:eu-west-1:470031436598:task-definition/console-sample-app-static:1", 
                    "updatedAt": 1429297790.557, 
                    "id": "ecs-svc/9223370607558517799", 
                    "runningCount": 3
                }
            ], 
            "events": [
                {
                    "message": "(service 80) was unable to place a task because the resources could not be found.", 
                    "id": "f13b250b-ed9a-4c9f-a56f-9e4824bb8bf0", 
                    "createdAt": 1429297822.914
                }, 
                {
                    "message": "(service 80) has reached a steady state.", 
                    "id": "805efa67-04d0-42c4-a10c-790bfb0a05cc", 
                    "createdAt": 1429297789.821
                }, 

~~~

The only way to solve these issue is to add a container-image or reduce by 1 the number of 
IDEA: detect if a task-definition has a port: this means it can have only a task per container-instace (we could use these info to better schedule)


# MISC

ECS + JENKINS : http://blogs.aws.amazon.com/application-management/post/Tx32RHFZHXY6ME1/Set-up-a-build-pipeline-with-Jenkins-and-Amazon-ECS

### Use CoreOS

https://coreos.com/docs/running-coreos/cloud-providers/ecs/
https://gist.github.com/kgorskowski/3793ea745a1dd370e17e

### Deploy mesos on ECS

* 1 command: http://sebgoa.blogspot.it/2015/03/1-command-to-mesos-with-docker-compose.html
* 7 commnads: https://medium.com/@gargar454/deploy-a-mesos-cluster-with-7-commands-using-docker-57951e020586


### Future IDEAS for ECS

* Nice post with a lot of feature requests
