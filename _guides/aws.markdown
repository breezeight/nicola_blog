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

# References

* [YouTube recordings of AWS re:Invent 2017 sessions](https://gist.github.com/stevenringo/108922d042c4647f2e195a98e668108a)


# AWS Account Management

## Consolidated Billing

* http://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_from-consolidatedbilling.html
* http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html

With AWS Organization the master account pay the consolidated bill.

## AWS Organizations

* HOME: https://console.aws.amazon.com/organizations
* [DOC](http://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
* Announcement: https://aws.amazon.com/it/about-aws/whats-new/2017/02/aws-organizations-now-generally-available/

* Organizations helps simplify the billing for multiple accounts by enabling you to setup a single payment method for all the accounts in your organization through consolidated billing.
* You can create Service Control Policies (SCPs) that centrally control AWS service use across multiple AWS accounts.


To create an account from your parent org: http://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_access.html


AWS Organizations automatically creates a **root user** and an **IAM role named OrganizationAccountAccessRole** for the account (that you can optionally rename but don't do it).
To access the account as the root user for the first time, you must go through the process for **password recovery**.


## Reserved Instances

Ref:
https://financetrainingcourse.com/education/2017/07/the-aws-guide-that-will-make-you-switch-to-reserved-ec2-instances/


Some of the questions we had were:

* What is a Reserved Instance and how long will I have to commit for?
* How much will the Reserved Instances cost, compared to my On-Demand instance?
* When do I have to pay?
* Will I really save 60% if I use a Reserved Instances as claimed?
* What if my computing requirements change?
* How can I start using the Reserved Instances once I have purchased it?


Reserved Instance come as either:

* Standard or
* Convertible offering classes.

Market place: https://docs.aws.amazon.com/en_us/AWSEC2/latest/UserGuide/ri-market-general.html



# AWS Security

* [FedRamp Compliance](http://d0.awsstatic.com/whitepapers/aws-architecture-and-security-recommendations-for-fedramp-compliance.pdf)

## Distribute Credentials or sensitive data on boot

Ref:

* [Old Post of 2009, but well done](http://shlomoswidler.com/2009/08/how-to-keep-your-aws-credentials-on-ec2.html), I think it's written before instances profiles.

Don't use `User-data`:

* Any user account able to open a socket on an EC2 instance can see the user-data by getting the URL http://169.254.169.254/latest/user-data . This is exploitable if a web application running in EC2 does not validate input before visiting a user-supplied URL. Accessing the user-data URL is particularly problematic if you use the user-data to pass in the secret unencrypted into the instance – one quick wget (or curl) command by any user and your secret is compromised. And, there is no way to clear the user-data – once it is set at launch time, it is visible for the entire life of the instance.

# IAM

Refs:

* https://start.jcolemorrison.com/aws-iam-policies-in-a-nutshell/
* https://blog.schlomo.schapiro.org/2017/06/understanding-iam-roles-in-amazon-aws.html
* https://blog.schlomo.schapiro.org/2017/06/working-with-iam-roles-in-amazon-aws.html


The long, deep, dark of AWS documentation can sometimes overcomplicate concepts.

NOTE: The difficulty with policies isn't really the concept or the anatomy. Instead, it's the overwhelming number of possible actions, principals, resources and conditions that we can insert into them. Additionally the "context" of the policies (i.e. using them on an S3 bucket vs an IAM user) also changes what can be inserted into them.






## IAM Policies

* [TODO](http://docs.aws.amazon.com/IAM/latest/UserGuide/PermissionsAndPolicies.html)
* [List of policies common errors](http://blogs.aws.amazon.com/security/post/Tx1LYOT2FQML4UG/Back-to-School-Understanding-the-IAM-Policy-Grammar)

### Intro

What is an AWS IAM Policy? A set of rules that, under the correct conditions, define what actions the policy principal or holder can take to specified AWS resources.

That still sounds a bit stiff. How about: Who can do what to which resources. When do we care?

There we go. Let's break down the simple statement even more:

* *The "Who aka The Principal"*: "Who" is trying to do stuff? This can be a User, Groups of users and "roles.". The first two are self-explanatory. The last one is just allows us to let other things, like EC2 servers, become the "Who." (We can also allow for federated users to be the "who" but we won't dive into that.)

* *The "What"* :"What" actions can the "Who" take? Run EC2 instances? Put objects to S3? Put logs to cloud watch?

* *The "Which"*: "What" actions can the "Who" take on "Which" resources? So the "Who" can put and get objects to S3, but to which S3 buckets? All of them? Only ones in us-east-1?

* *The "When"* : When do we care? If the IP matches a certain range of IPs? If the date-time is before a particular day? If the AWS user's username includes the string "cheese"?

Let's translate our simple statement over to one that follows AWS's policy language now.

A Simple Policy Example:

```
{
  "Version": "2012-10-17",
  "Id": "some-unique-id",
  "Statement": {
    "Sid": "1",
    "Effect": "Allow",
    "Principal": {"AWS": "arn:aws:iam::111222333444:user/colonel"},
    "Action": [
      "s3:PutObject",
      "s3:Get*"
    ],
    "Resource": "arn:aws:s3:::kfc-bucket/*",
    "Condition": {
      "DateGreaterThan": {
        "aws:CurrentTime": "2017-02-28T00:00:00Z"
      }
    }
  }
}
```

* "Version" - There's only two verisons - 2012-10-17 and 2008-10-17. Always use the newest.

* "Id" (optional) - Suggested to be a uuid. Required by some services, but not by many. We won't use this property in our examples.*

* "Statement" - Remember: who can do what to which resources... and when. This is the meat of Policies. This can be one of those statements or an array of many.

Everything else is inside of a statement:

* "Sid" (optional) - an ID for each of the individual statements. Optional and isn't even exposed in the IAM API, so we won't do cover this.*

* "Effect" - Either Allow or Deny. If we used Deny in the above example, it would just flip the policy. We would deny the user colonel from getting and putting objects to the kfc-bucket. That would be sad.

* "Principal" - The "Who." In this example we specify the ARN, Amazon Resource Name (unique AWS id of a resource), of the IAM user colonel.

* "Action" - The "What." The two actions in our example are s3:PutObject and s3:Get*. They perform any action that begins with the characters Get (i.e. GetObject, GetBucket, etc) and put things to/from S3.

* "Resource" - The "Which." Which resource they can do "what" to, is anything in the bucket kfc-bucket.

* "Condition" - The conditions that must present for this policy to be relevant, is when the current date is greater than Feb 28, 2017 (when US East 1 went down).

* - ID and SID are required by some services. If so, it will be specified in the docs specific to that service, i.e. SQS and SNS.
Even though there are a number of properties, 99% of the time will be spent on "Principal", "Action", "Resource" and "Condition". Because of this, that will be our main focus.

### The Who aka the Principal

A policy can have a `principal` which is the identity to which the policy apply.

A policy can be attached to:

* a group, a user
* a resource

The `Principal` element is unnecessary with an IAM policy attached directly to an Identity, because the principal is by default the entity that the IAM policy is attached to. It can be a IAM user, federated user, or assumed-role user), AWS account, AWS service, or other principal entity.

[AWS reference; Principal](http://docs.aws.amazon.com/IAM/latest/UserGuide/AccessPolicyLanguage_ElementDescriptions.html#Principal)

For IAM Users and Roles, we just grab its ARN (found in the IAM console or returned in the CLI) and follow the format of:

```
"Principal": {"AWS": "<ARN OF YOUR IAM USER OR ROLE BUT NOT GROUPS>"}
```

So groups don't work. Kind of frustrating. I'm sure there's a good reason for it, but we'll talk about how to use policies on groups later on.

Pricipal examples:

~~~
"Principal": {
        "AWS": ["arn:aws:iam::111122223333:user/Alice",
                "arn:aws:iam::111122223333:root"]
      },
~~~

or AWS services:

```
"Principal": {
  "Service": "ec2.amazonaws.com"
}
```

This allows an AWS service as the Principal. In this case our "who" is the EC2 service. Anytime we want another AWS resource to do something for us independently, we need to give it permissions i.e. a EC2 server putting objects to S3.

Note: ec2.amazonaws.com is just AWS's "friendly" name to specify EC2 as a service.

NOW. HUGE Gotcha. If we're making and attaching policies to IAM users, groups and roles, the principal (or Who) isn't needed. That's because when you attach a policy to an IAM user for example, the policy assumes that the user who we've attached the policy to is the principal.

But... why is there a Principal field then? Even though the majority of our policies are attached to IAM users, groups and roles, they're also used in places without these assumptions. The most common ones are: S3 buckets, Glacier, SNS, SQS and AWS Role Trust Policies.

In fact, if you've done anything with S3, you've seen the infamous "Bucket Policy." Those are just policies! And they're the type where we need to specify the principal. The main difference on those is that the only resource or "which" that they care about is the bucket the policy is on.

Before we move on, I mentioned that groups can't be specified as principals. Well, as we just mentioned, the principal is implied on IAM users and groups. Therefore, if we wanted a group to be the principal, just attach a policy to the group and the principal will be assumed to be the group. I bring this up just in case you try and specify a group ARN an on an S3 bucket policy, it won't work.

### The "Who" Users vs The "Who" Resources

What's the difference between attaching a policy to an IAM user vs a resource like an S3 bucket?

The easiest way to explain the difference here is to use this analogy:

If the policy is attached to the user, group or role it's like a permission slip. If it's attached to the resource, it's like a VIP list.

If it's with the user, just imagine the user colonel walking around with a permission slip. He shows up to a resource, we'll call kfc-bucket, and requests objects. To determine permissions we look at the slip, and he gets the objects or doesn't. Since the slip is with the user, we don't need to know who it applies to, obviously it's for the user.

If it's with the resource, then imagine colonel walking around with nothing. Instead, the permission slip is on the kfc-bucket. When colonel shows up to the kfc-bucket, we check the permission slip on the bucket and that's where we determine if he gets the objects or not. Since the slip is with the resource, we need to know who is allowed in or not, therefore we need to specify the principals.



### IAM identities: how to specify the WHO

`IAM identities` are created to provide authentication for people and processes in your AWS account:

* _user_ : A IAM user is really just an identity with associated permission (can be people or application). A users is provided with credentials to uniquely identify themselves to AWS.
* _group_ : is a collection of users, when a user belong to a group has all the group's permission
* _roles_ : A role lets you define a set of permissions to access the resources that a user or service needs, but the permissions are not attached to an IAM user or group. Instead, at run time, applications or AWS services (like Amazon EC2) can programmatically assume a role. When a role is assumed, AWS returns temporary security credentials that the user or application can use to make programmatic requests to AWS. Consequently, you don't have to share long-term security credentials (for example, by creating an IAM user) for each entity that requires access to a resource.
* _Temporary credentials_ : are primarily used with IAM roles, but there are also other uses. You can request temporary credentials that have a more restricted set of permissions than your standard IAM user. This prevents you from accidentally performing tasks that are not permitted by the more restricted credentials. A benefit of temporary credentials is that they expire automatically after a set period of time. You have control over the duration that the credentials are valid.
* _Root Account_ :

Main concepts:

* _security credential_ : each user can have different credentials (IAM—passwords, access keys, certificates, and MFA...). To create a new credential users need to be authorized.
* _permission_ : a permission authorizes or denies a user to perform any AWS actions or to access any AWS resources.
* _instance profiles_ : An instance profile is a container for an IAM role. Instance profiles are used to pass role information to an Amazon EC2 instance when the instance starts.


refs:

* [aws doc users and groups](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_WorkingWithGroupsAndUsers.html)
* [aws doc credential management](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingLogins.html)
* [Doc: Roles](http://docs.aws.amazon.com/IAM/latest/UserGuide/WorkingWithRoles.html)
* [Doc: Instance Profiles](http://docs.aws.amazon.com/IAM/latest/UserGuide/instance-profiles.html)
* [Istance Profile use with EC2](http://docs.aws.amazon.com/IAM/latest/UserGuide/role-usecase-ec2app.html)

#### Best Practices

Our guidelines are:

* Create one user for each employee
* Assign policy only to groups (this will make your life easier when we need to add the same policy to another user)
* Do NOT assign policies to a user. Create a new group and assign the use to that group
* Password Policy: 16 chars, users cannot change pwd, require numbers, special chars, uppercase char
* Do NOT create access key if not needed.
* Force MFA authentication at least on every production resource [How To](http://stackoverflow.com/questions/21917197/how-to-enforce-iam-users-to-use-multi-factor-authentication-to-use-the-console). [Here](https://blog.stitchdata.com/role-playing-with-aws-c9eaebcc6c98#.xtcbko558). [Principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege).
* Rotate credentials every 90 days (TODO write how to enforce)

These are ours main groups:

* _admin_ : Need permission to create and manage AMIs, instances, snapshots, volumes, security groups, and so on. The group has permission to use all the Amazon EC2 actions.

* _developers_ : need the ability to work with instances only. The group can call DescribeInstances, RunInstances, StopInstances, StartInstances, and TerminateInstances.

* _managers_ : not be able to perform any EC2 actions except listing the Amazon EC2 resources currently available. Has access to the billing info.


AWS doc:
http://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html

#### Test and debug TIPS:

* As admin we could create a second key for each user and test locally using AWS_PROFILE

https://docs.aws.amazon.com/cli/latest/reference/iam/simulate-custom-policy.html
aws-vault exec -n idrostudi -- aws iam simulate-custom-policy

Intro: https://www.slideshare.net/AmazonWebServices/aws-reinvent-2016-how-to-automate-policy-validation-sec311


https://docs.aws.amazon.com/cli/latest/reference/iam/simulate-principal-policy.html#examples

aws-vault exec -n idrostudi -- aws iam simulate-principal-policy --policy-source-arn "arn:aws:iam::319646432438:group/idrostudi-ec2-compute-models-session-manager" --action-names "ssm:StartSession" --resource-arns "arn:aws:ec2:us-west-1:319646432438:instance/i-0ae63a6de081103e6"

--policy-source-arn  The Amazon Resource Name (ARN) of a user, group, or role whose policies you want to include in the simulation.


--resource-arns (list) A list of ARNs of AWS resources to include in the simulation. If this parameter is not provided, then the value defaults to * (all resources).


#### Users

* [full doc](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html)

User Management:

* [Permitting IAM Users to Change Their Own Passwords](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_enable-user-change.html)
* MFA
  * [MFA Protected API calls](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) additional security of requiring a user to be authenticated with AWS multi-factor authentication (MFA) before the user is allowed to perform particularly sensitive actions. [Principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege)

* [Credentials Report](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)
* [CodeCommit credentials](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_ssh-keys.html)


To create a user and send him a mail:
.....

#### Roles

* http://docs.aws.amazon.com/IAM/latest/UserGuide/WorkingWithRoles.html
* https://blog.schlomo.schapiro.org/2017/06/understanding-iam-roles-in-amazon-aws.html
* https://blog.schlomo.schapiro.org/2017/06/working-with-iam-roles-in-amazon-aws.html
* [Role terms and concepts](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html)


* A role is essentially a set of permissions that grant access to actions and resources in AWS
* Delegation is granting permission to someone that allows access to resources that you control.

Even though IAM users and groups imply a "who" on their permission policy, IAM roles do so only after we've specified the who via a "Trust Policy." Therefore, when creating a role we have to pass it these two separate policy documents:

* *Trust policy* : which specifies who is allowed to assume the role (the trusted entity, or principal; see the next term)
* *Permissions policy* : which defines what actions and resources the principal is allowed to use.

[Granting a user permissions to switch role](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_permissions-to-switch.html)

#### Users VS Roles

When use users:

- You need to access the AWS console or use the AWS cli from your workstation (NB: protect your keys with aws-vault or similar tools). with aws-cli you can still use the assume role feature to limit your stardard access permissions.
- You need to integrate with 3rd parties (ex: datadogs)


When user role:

- You're creating an application that runs on an Amazon Elastic Compute Cloud (Amazon EC2) instance and that application makes requests to AWS.
- You're creating an app that runs on a mobile phone and that makes requests to AWS.
- Users in your company are authenticated in your corporate network and want to be able to use AWS without having to sign in again—that is, you want to allow users to federate into AWS.


### IAM policy element reference

http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html

### IAM policy variables

http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html#policy-vars-intro

* For users of a group: `${aws:username}`

### Type of Policies

http://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html

You can create different types of policies:

* `Identity-based AWS Managed policies` – Standalone policies that you can attach to multiple users, groups, and roles in your AWS account. Managed policies apply only to identities (users, groups, and roles) - not resources. Are created and managed by AWS.
* `Identity-based Customer managed policies` – Managed policies that you create and manage in your AWS account. Using customer managed policies, you have more precise control over your policies than when using AWS managed policies.
* `Identity-based Inline policies` – Policies that you create and manage, and that are embedded directly into a single user, group, or role. Resource-based policies are another form of inline policy.
* `Resource-based Inline policies` policies that are embedded directly into a resource


* Generally speaking, the content of the policies is the same in all cases, each kind of policy defines a set of permissions using a common structure and a common syntax.

For example, the AWS managed policy called ReadOnlyAccess provides read-only access to all AWS services and resources. When AWS launches a new service, AWS will update the ReadOnlyAccess policy to add read-only permissions for the new service. The updated permissions are applied to all principal entities that the policy is attached to.

#### Policy type BEST practices

* Use Managed AWS policies for what everything that could be updated by AWS (ex: new services API, etc)
* Use Customer Managed when you need more control

arn:aws:iam::aws:policy/AdministratorAccess


#### [JOB] List and Get policies and who is attached

Get the full statement of policies: Go to IAM Console -> policies , you can filter for AWS managed policies

list:

* `aws --profile=pt iam list-policies`
* `aws --profile=pt iam list-policies --scope AWS| jq '.Policies[] | {name: .PolicyName, arn: .Arn}'` :
* `aws --profile=pt iam list-policies --scope AWS|grep PolicyName|awk '{print $2}'` : list of all AWS managed policies
* http://docs.aws.amazon.com/cli/latest/reference/iam/list-policies.html

list policy's versions:

* `aws --profile=pt iam list-policy-versions --policy-arn arn:aws:iam::aws:policy/AmazonRoute53FullAccess`



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

#### [JOB] Debug Policies with IAM Policy Simulator

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

#### [JOB] Test S3 with FOG


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

## AWS Services That Work with IAM

List of IAM permission types each service supports:

* Action-level permissions
* Resource-level permissions
* Resource-based permissions
* Tag-based permissions
* Temporary security credentials
* tips to help you write policies to control service access, and links to related information.

http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html

## IAM practical scenarios

* See [here](http://docs.aws.amazon.com/IAM/latest/UserGuide/Using_WorkingWithGroupsAndUsers.html) "Scenarios for Creating IAM Users"

Note:

* EC2 uses SSH keys and security groups to control who has access to specific Amazon EC2 instances. There's no method in the IAM system to allow or deny access to a specific instance.
* OpsWorks can help with the upload of SSH keys and is connected with
the IAM system
* for some use case the temporary token system is better suited than IAM

Billing:

* https://blogs.aws.amazon.com/security/post/Tx2154FGFDNMQNP/Enhanced-IAM-Capabilities-for-the-AWS-Billing-Console



Delegate Access to demo AWS account:

http://cloudsentry.evident.io/aws-security-best-practice-7-use-iam-roles-with-sts-assumerole/

## SLAM Providers

[TODO](http://docs.aws.amazon.com/IAM/latest/UserGuide/idp-managing-identityproviders.html)

## Log IAM Access with CloudTrial

[TODO](http://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html)

## IAM Server Certificates

IAM manage also all certificates you upload to AWS, ELB
ElasticBeastalk and other service use them.



to use EB_FAST_DEPLOY and add the certificate to EB use the "Arn" variables:

`aws iam list-server-certificates` :

~~~
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

~~~
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

Ref: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html#instancedata-dynamic-data-retrieva



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

https://blog.stitchdata.com/role-playing-with-aws-c9eaebcc6c98#.dyhio82dk

## references

* [AWS best practices](http://docs.aws.amazon.com/IAM/latest/UserGuide/IAMBestPractices.html)
* [AWS use cases](http://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_UseCases.html#UseCase_EC2): EC2 and S3

# AWS Cli

The AWS Command Line Interface is a unified tool to manage your AWS services [reference](http://docs.aws.amazon.com/cli/latest/reference/).

NB: some service endpoint is available only in some region(OpsWorks only us-east-1 as of march 2014).

AWS Cli as docker image:
* https://hub.docker.com/r/garland/aws-cli-docker/tags

Add this alias to your bash and you will run awscli as `aws_docker`, it will inject your current aws credentials

~~~
alias aws_docker="docker run \
  --env AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} \
  --env AWS_SECRET_ACCESS_KEY=${YOUR_SECRET_ACCESS} \
  --env AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION} \
  --env AWS_REGION=${AWS_REGION} \
  --env AWS_SESSION_TOKEN=${AWS_SESSION_TOKEN} \
  --env AWS_SECURITY_TOKEN=${AWS_SECURITY_TOKEN} \
  garland/aws-cli-docker:1.16.140 aws"
~~~

Really simple Dockerfile that install awscli into the Alpine Python image

~~~
FROM python:3.8.0a3-alpine3.9

# Versions: https://pypi.python.org/pypi/awscli#downloads
ENV AWS_CLI_VERSION 1.16.140

RUN apk --no-cache update && \
    apk --no-cache add ca-certificates groff less && \
    pip3 --no-cache-dir install awscli==${AWS_CLI_VERSION} && \
    rm -rf /var/cache/apk/*

WORKDIR /data
~~~

alias aws_docker="docker run garland/aws-cli-docker:1.16.140"

ISSUE with aws vault: "aws-vault doesn't work with aliases" https://github.com/99designs/aws-vault/issues/272

## Configuration and credentials for multiple accounts

### NEW DEFINITIVE SOLUTION WITH AWS VAULT

TODO: Assuming Roles and MFA https://github.com/99designs/aws-vault#assuming-roles


Example:

```
aws-vault exec pt aws ec2 describe-instances
```

AWS cli support multiple profiles, the doc is [here](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-multiple-profiles).

http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-config-files

The CLI stores credentials specified with aws configure in a local file named `credentials` in a folder named .aws in your home directory. We don't use it, instead we use `aws-vault`.



In order to separate credentials from less sensitive options, region and output format are stored in a separate file named `config` in the same folder.

To set default region and output for each profile `~/.aws/config`:

~~~
[default]
region=us-west-1
output=json

[profile user2]
region=us-east-1
output=text
~~~

To configure AWS-VAULT: https://github.com/99designs/aws-vault

```
aws-vault add <profile>
```





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


# API Gateway

## What is Amazon API Gateway?

https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html

Amazon API Gateway is an AWS service for creating, publishing, maintaining, monitoring, and securing REST, HTTP, and WebSocket APIs at any scale. API developers can create APIs that access AWS or other web services.

Main Features:

* Custom Domains https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html

### Choosing between HTTP APIs and REST APIs

Doc:https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html

HTTP APIs is a new flavor of API Gateway (REST API is the first released by AWS):
* Cheaper
* Less features but easier to manage in the most common use-cases
* REF: https://aws.amazon.com/blogs/compute/announcing-http-apis-for-amazon-api-gateway/




* HTTP API
  * Build low-latency and cost-effective REST APIs with built-in features such as OIDC and OAuth2, and native CORS support.
  * Works with the following: Lambda, HTTP backends

* REST API
  * Develop a REST API where you gain complete control over the request and response along with API management capabilities.
  * Works with the following: Lambda, HTTP, AWS Services

* REST API Private
  * Create a REST API that is only accessible from within a VPC.

## API Gateway V2

https://aws.amazon.com/blogs/compute/announcing-http-apis-for-amazon-api-gateway/


# AWS Severless

## Intro: Serverless world, applications, usecases

Serverless App are EVENT DRIVEN

### AWS Lambda VS AWS SAM

Reading the documentation you can get confused by these apparently similar 

* AWS::Lambda::Function
* AWS::Serverless::Function https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html

As stated here: 
https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-generated-resources-function.html
`AWS::Serverless::Function` is an higher level concept that generate many resources, depending on the the configuration, like for ex: 
AWS::Lambda::Alias, AWS::Lambda::Version AWS::Lambda::EventInvokeConfig, AWS::SNS::Topic

Generally speaking  AWS::Lambda::Function is just a part of the SAM Model.

SAM APP for AWS Educate: Let teacher run CloudFormation in all student AWS Educate Classroom Account.
* https://www.linkedin.com/pulse/how-use-managed-aws-educate-classroom-calendar-build-wong/
* Repo: git@github.com:wongcyrus/managed-aws-educate-classroom.git


### Awesome Lambda

10 AWS Lambda Use Cases to Start Your Serverless Journey : https://www.simform.com/serverless-examples-aws-lambda-use-cases/#website



Use Geonames to "reverse geocode" the Lat/Lon for each Hotel in the database and add "hierarchy" for that place: https://github.com/dwyl/lambda-taggable-geonames-indexer

## Tutorial: managed-aws-educate-classroom

### Overview del template

Code:
https://github.com/wongcyrus/managed-aws-educate-classroom/
Commit: a991d2cacf125a419a128e7b96c7c2cc7cbe0d4d

User guide: https://www.linkedin.com/pulse/how-use-managed-aws-educate-classroom-calendar-build-wong/

https://calendar.google.com/calendar/b/1?cid=dGVjaHN0YXRpb25wYWRvdmEuaXRfNDVoODFwNjBlN2g1azJkZjMzdm41dmw1dGdAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ


Main features:
* Manage all student AWS Educate Classroom Account through Google Calendar.
* Create CloudFormation stack in all student AWS Educate Classroom Account before the class.
* Delete CloudFormation stack in all student AWS Educate Classroom Account after the class.
* Start all EC2 instances inside CloudFormation stack in all student AWS Educate Classroom Account before the class.
* Stop all EC2 instances inside CloudFormation stack in all student AWS Educate Classroom Account after the class.
* Access all of your student's AWS Educate Classroom Account.



Wait until the deployment completion, click on “View CloudFormation Stack”.
Click on “Outputs” tab.
Note down the value of “ClassroomBucket” and “StudentRegistrationUrl”



TODO:
* capire a cosa servono questi parametri: BucketName, SesInboxTopic, TeacherCommandEmail, TeacherEmailDomains, StudentCommandEmail, StudentEmailDomains


TODO: capire come monitorare gli errori... 

Servizi AWS usati:
* SQS Amazon Simple Queue Service 
* SNS 
* SES
* SAM
* AWS Lambda
* sts:AssumeRole
* HTTP Api
* DynamoDB

Package NodeJS:
* Testing: mocha  https://mochajs.org/ , chai  https://www.chaijs.com/

### Resources Overview
 WebUI for student registration.
  HttpApi:
    Type: AWS::Serverless::HttpApi


  ClassroomBucket:
    Type: AWS::S3::Bucket

  StudentAccountTable: 
    Type: AWS::DynamoDB::Table

SNS subscriptions:
* SetupStudentAccountSubscription
* CreateClassroomSubscription
* DeleteClassroomSubscription
* DeleteClassroomCalendarEventsSubscription
* CreateClassroomCalendarEventsSubscription


Queues  
There is a queue for some action and the relative deadletterqueue

AWS::SQS::Queue
* SetupStudentAccountQueue:
* SetupStudentAccountDeadLetterQueue: 
* CreateClassroomQueue:
* CreateClassroomDeadLetterQueue: 
* DeleteClassroomQueue:
* DeleteClassroomDeadLetterQueue: 

Nested Application
  CalendarEventsApplication:
    Type: AWS::Serverless::Application


Usa i layer a occhio per esportare qualche funzioncina di utility:
* CommonLayer: Type: AWS::Serverless::LayerVersion
* https://github.com/wongcyrus/managed-aws-educate-classroom/blob/a991d2cacf125a419a128e7b96c7c2cc7cbe0d4d/template.yaml#L98


SetupStudentAccountFunction:
  * Type: AWS::Serverless::Function
  * https://github.com/wongcyrus/managed-aws-educate-classroom/blob/a991d2cacf125a419a128e7b96c7c2cc7cbe0d4d/template.yaml#L151
  * Events: SetupStudentAccountQueue 
TODO: capire chi inserisce gli eventi nella coda

StartInstanceFunction
  * Type: AWS::Serverless::Function 
  * Create and Start Classroom
  * https://github.com/wongcyrus/managed-aws-educate-classroom/blob/a991d2cacf125a419a128e7b96c7c2cc7cbe0d4d/template.yaml#L173
TODO: capire x' non è collegata a nessun evento...

CreateStudentStackFunction:
  * Type: AWS::Serverless::Function
  * https://github.com/wongcyrus/managed-aws-educate-classroom/blob/a991d2cacf125a419a128e7b96c7c2cc7cbe0d4d/template.yaml#L185

TODO:

capire come gestire SES e SNS
https://github.com/wongcyrus/managed-aws-educate-classroom/blob/a991d2cacf125a419a128e7b96c7c2cc7cbe0d4d/template.yaml#L118
  SetupStudentAccountSubscription:
    Type: 'AWS::SNS::Subscription'

### Students Registration

The Student's registration page is at root endpoint of our HTTP Gateway:
* https://feamlqbiuf.execute-api.us-east-1.amazonaws.com/?classroomName=ChangeToYourClassName&studentEmail=YourStudentEmailAddress
* `studentEmail` [OPTIONAL] prefill the email form field
* `ChangeToYourClassName` [REQUIRED] ..... 

The web-ui routing is configure in your SAM template `template.yml`: https://github.com/wongcyrus/managed-aws-educate-classroom/blob/a991d2cacf125a419a128e7b96c7c2cc7cbe0d4d/template.yaml#L402
* your lambda code: CodeUri: web-ui/
* The Event of `Type: HttpApi` will add a route to the HTTP Api Gateway `ApiId: !Ref HttpApi`: `Method: ANY` and `Path: /`


Lambda Code: https://github.com/wongcyrus/managed-aws-educate-classroom/blob/a991d2cacf125a419a128e7b96c7c2cc7cbe0d4d/setup-student-account/app.js

Note that the registration URL is added to the output section of the template and is composed with the `!Sub` function (sadly there isn't a return value for this value)

```
  StudentRegistrationUrl:
    Description: URL of your API endpoint
    Value: !Sub 'https://${HttpApi}.execute-api.${AWS::Region}.${AWS::URLSuffix}/?classroomName=ChangeToYourClassName'
```


### Nested Application: Calendar Trigger

https://github.com/wongcyrus/calendar-trigger

AWS SAM Apps to poll public calendar and publish event to SNS.

Outputs:
  CanlenderEventStartTopic:
    Value: !Ref CanlenderEventStartTopic
  CanlenderEventStopTopic:
    Value: !Ref CanlenderEventStopTopic


## AWS Lambda

https://aws.amazon.com/lambda/

Developer Documentation: https://docs.aws.amazon.com/lambda/latest/dg/welcome.html

console.aws.amazon.com/lambda

You can use AWS Lambda to run your code in response to events, such as changes to data in an Amazon S3 bucket or an Amazon DynamoDB table; to run your code in response to HTTP requests using Amazon API Gateway; or invoke your code using API calls made using AWS SDKs. With these capabilities, you can use Lambda to easily build data processing triggers for AWS services like Amazon S3 and Amazon DynamoDB, process streaming data stored in Kinesis, or create your own back end that operates at AWS scale, performance, and security.

Key points: 

* Administration: all the devops and security is offloaded (server and operating system maintenance, capacity provisioning and automatic scaling, code monitoring and logging). Lambda is a highly available service out of the box. 
* AWS Lambda executes your code only when needed and scales automatically, from a few requests per day to thousands per second. Usefull for apps with random load spikes.
* Lambda can run on edge location (TODO: check if this can reduce latency)
* Pricing: You pay only for the compute time you consume - there is no charge when your code is not running. Sometime is easier to estimate the cost with lambda than with complex system with many moving parts.

When should you use lambda? 

* when administration of the system is too expensive. Think about simple app with low volume
* when you need to create custom glue code between AWS services
* WARNING: latency can be an issue
* WARNING: working with zip file can be a mess... but may be framenworks like serverless can solve the problem (TODO)

### Lambda Cheatsheet

Function clean-up:
* Custom Roles
* log
* the function itself `aws lambda delete-function --function-name my-function`

### Lambda Getting Started - HelloWorld

Very simple example using the console and the online AWS editor: https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html
* Console Editor (embedded Cloud9)
* Test event
* monitoring tab

https://aws.amazon.com/getting-started/hands-on/run-serverless-code/

#### Concepts

https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-concepts.html

* `Function` a resource that you can invoke to run your code in AWS Lambda. Has code that processes events, and a runtime that passes requests and responses between Lambda and the function code.
* `Runtime` allow functions in different languages to run in the same base execution environment. 
* `Event`: An event is a JSON formatted document that contains data for a function to process. The Lambda runtime converts the event to an object and passes it to your function code. 
* `Concurrency`: Concurrency is the number of requests that your function is serving at any given time.
* `Trigger`: A trigger is a resource or configuration that invokes a Lambda function. This includes AWS services that can be configured to invoke a function, applications that you develop, and event source mappings.


For details on events from AWS services, see Using AWS Lambda with other services: https://docs.aws.amazon.com/lambda/latest/dg/lambda-services.html

#### Lambda Programming Model

https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-programmingmodel

This is a generic intro, for a detailed guide to a specific Language, see "Working with..." in the documentation. EX, nodejs: https://docs.aws.amazon.com/lambda/latest/dg/lambda-nodejs.html

All runtimes share a common programming model that defines the interface between your code and the runtime code.

You tell the runtime which method to run by defining a handler in the function configuration. Ex `template.yaml`:

```
Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function # More info about Function Resource: https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Properties:
      CodeUri: hello-world/
      Handler: app.lambdaHandler #### HANDLER #####
      Runtime: nodejs12.x
      Events:
        HelloWorld:
          Type: Api # More info about API Event Source: https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#api
          Properties:
            Path: /hello
            Method: get
```

`hello-world/app.js`:

```
exports.lambdaHandler = async (event, context) => {
    try {
        // const ret = await axios(url);
        response = {
            'statusCode': 200,
            'body': JSON.stringify({
                message: 'hello world',
                // location: ret.data.trim()
            })
        }
    } catch (err) {
        console.log(err);
        return err;
    }

    return response
};
```

The runtime passes in objects to the handler that contain:
* the invocation `event`
* the `context`, such as the function name and request ID.

Filesystem:
* Your function also has access to local storage in the `/tmp` directory.

LOGS: 
* The runtime captures logging output from your function and sends it to `Amazon CloudWatch Logs`.
* In addition to logging your function's output, the runtime also logs entries when execution starts and ends. This includes a report log with the request ID, billed duration, initialization duration, and other details. If your function throws an error, the runtime returns that error to the invoker.

Lifecycle:
* When the handler finishes processing the first event, the runtime sends it another.
* The function's class stays in memory, so clients and variables that are declared outside of the handler method in initialization code can be reused. (WARNING about how you use them!)
* Instances of your function that are serving requests remain active for a few hours before being recycled.

OPTIMIZATION: To save processing time on subsequent events, create reusable resources like AWS SDK clients during initialization. Once initialized, each instance of your function can process thousands of requests.

See X-Ray and Lambda monitoring to check how long does you initialization phase:
https://docs.aws.amazon.com/lambda/latest/dg/lambda-x-ray.html

SCALING:

* Lambda scales your function by running additional instances of it as demand increases, and by stopping instances as demand decreases. 
* Unless noted otherwise, incoming requests might be processed out of order or concurrently. 
* Store your application's state in other services, and don't rely on instances of your function being long lived. Use local storage and class-level objects to increase performance, but keep the size of your deployment package and the amount of data that you transfer onto the execution environment to a minimum.

#### Deployment Package

https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-package

It's a ZIP managed by the AWS CLI or AWS SAM CLI, or other integration tools.

#### Layers

https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-layers

Lambda layers are a distribution mechanism for libraries, custom runtimes, and other function dependencies. 

#### Scaling 

Docs:

* https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-scaling
* https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html

Your functions' concurrency is the number of instances that serve requests at a given time. 

Scaling:

* UP When your function is invoked more quickly than a single instance of your function can process events, Lambda scales up by running additional instances.
* DOWN When traffic subsides, inactive instances are frozen or stopped. You only pay for the time that your function is initializing or processing events.

TODO leggersi meglio come funziona....

#### Asynchronous invocation
https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-async

With asynchronous invocation, Lambda queues the event for processing and returns a response immediately. 

USE-CASEs:
* TODO rileggere questo anche se non so se centra... https://read.acloud.guru/save-time-and-money-with-aws-lambda-using-asynchronous-programming-3548ea65f751

#### Event Source Mapping

https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-eventsourcemapping

To process items from a stream or queue, you can create an event source mapping. An event source mapping is a resource in Lambda that reads items from an Amazon SQS queue, an Amazon Kinesis stream, or an Amazon DynamoDB stream, and sends them to your function in batches. 

NOTE: Each event contains hundreds or thousands of items.

#### Destination

https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-destinations

A destination is an AWS resource that receives invocation records for a function. For asynchronous invocation, you can configure Lambda to send invocation records to a queue, topic, function, or event bus. You can configure separate destinations for successful invocations and events that failed processing. The invocation record contains details about the event, the function's response, and the reason that the record was sent.


#### Function blueprints

https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-features.html#gettingstarted-features-blueprints

When you create a function in the Lambda console, you can choose to start from scratch, use a blueprint, or deploy an application from the AWS Serverless Application Repository.

#### Application templates

Application templates in the Lambda console include:

* code for one or more functions,
* an application template that defines functions and supporting AWS resources, 
* and an infrastructure template that defines an AWS CodePipeline pipeline. 

The pipeline has build and deploy stages that run every time you push changes to the included Git repository.

For more information, see Creating an application with continuous delivery in the Lambda console: https://docs.aws.amazon.com/lambda/latest/dg/applications-tutorial.html

#### CLI intro

https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-awscli.html

* Prerequisites
* Create the execution role
* Create the function
* List the Lambda functions in your account
* Retrieve a Lambda function
* Clean up

#### Other Tools

https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-tools.html

* AWS Command Line Interface
* AWS Serverless Application Model
* SAM CLI
* Code authoring tools

##### AWS Toolkit for Visual Studio Code 
* The AWS Toolkit for Visual Studio Code is an open source plug-in for the Visual Studio Code that makes it easier to create, debug, and deploy applications on Amazon Web Services: 
https://aws.amazon.com/visualstudiocode/

Issue with AWS VAULT:
https://github.com/99designs/aws-vault/issues/370

NON RISOLTO.... 
* VS Code issue with AWS VAULT and workaround: https://github.com/aws/aws-toolkit-vscode/issues/164#issuecomment-549940246
* https://github.com/99designs/aws-vault/blob/master/USAGE.md#using-credential-helper
* https://docs.aws.amazon.com/cli/latest/topic/config-vars.html#sourcing-credentials-from-external-processes
* then you need to solve also this issue "error when there is a config file but not a credentials file present"
* https://github.com/aws/aws-toolkit-vscode/issues/641


After you connect to AWS from VSCode you can use the inline commands above your lambda.

NOTE: it uses VS Code "Code lines" feature to add debug commands



#### Code Editor Intro (embedded Cloud9 for Lambda)

https://docs.aws.amazon.com/lambda/latest/dg/code-editor.html

### Lambda Limits

https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html

### Permissions

https://docs.aws.amazon.com/lambda/latest/dg/lambda-permissions.html

An AWS Lambda function's execution role grants it permission to access AWS services and resources. You provide this role when you create a function, and Lambda assumes the role when your function is invoked. 

There are managed policies for most common usecases: https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html#permissions-executionrole-features

**TODO**
* Boundaries
....


### Managing Functions

Doc: https://docs.aws.amazon.com/lambda/latest/dg/lambda-functions.html

#### Configuration console
https://docs.aws.amazon.com/lambda/latest/dg/configuration-console.html

#### Environment variables
Lambda has its own support to store ENV variable see https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html

Can we use the parameter store?

#### Concurrency
TODO
https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html

#### Versions and Alias

Lambda deploys can be versioned: https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html

You can create one or more aliases for your AWS Lambda function. A Lambda alias is like a pointer to a specific Lambda function version. Users can access the function version using the alias ARN:
https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html

* Aliases
* Layers
* Network
* Database
* Tags

#### Lambda Layers

Doc: https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html

Awesome Layers: https://github.com/mthenw/awesome-layers

You can configure your Lambda function to pull in additional code and content in the form of layers. A layer is a ZIP archive that contains libraries, a custom runtime, or other dependencies. With layers, you can use libraries in your function without needing to include them in your deployment package.

TODO: rileggere meglio a cosa servono e vantaggi/svantaggi

AWS Serverless Lambda Tutorial - How to use layers with AWS Lambda?
https://m.youtube.com/watch?v=zlOOCDnmBH8


## AWS Serverless Application Repository 

The AWS Serverless Application Repository is a managed repository for serverless applications.

Each application is packaged with an **AWS Serverless Application Model** (SAM) template that defines the AWS resources used. 

DOC: https://aws.amazon.com/serverless/serverlessrepo/

## SAM Model

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html

The AWS Serverless Application Model (AWS SAM) is an open-source framework that you can use to build serverless applications on AWS.
A serverless application is a combination of Lambda functions, event sources, and other resources that work together to perform tasks.

* AWS SAM template: describe the functions, APIs, permissions, configurations, and events that make up a serverless application. You use an AWS SAM template file to operate on a single, deployable, versioned entity that's your serverless application. It's an Extension of AWS CloudFormation.
* AWS SAM command line interface (AWS SAM CLI). Lets you locally build, test, and debug serverless applications that are defined by AWS SAM templates and deploy serverless applications to the AWS Cloud.

INSTALL CLI https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-mac.html

### Other Links

https://alexharv074.github.io/2019/03/02/introduction-to-sam-part-i-using-the-sam-cli.html
https://alexharv074.github.io/2019/03/02/introduction-to-sam-part-ii-template-and-architecture.html
https://alexharv074.github.io/2019/03/31/introduction-to-sam-part-iii-adding-a-proxy-endpoint-and-cors-configuration.html
https://alexharv074.github.io/2019/12/07/introduction-to-sam-part-iv-updates-to-sam-package-and-deploy-in-sam-cli-0.33.1.html

### SAM Cheatsheet


## SAM Hello world tutorial

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html


`sam init` init a sam app starting from a template. The example above use python but we can use nodejs

There are three especially important files:

* template.yaml: Contains the AWS SAM template that defines your application's AWS resources.
* hello-world/app.js: Contains your actual Lambda handler logic.
* hello-world/package.json:  Contains any NodeJS dependencies that the application requires, and is used for sam build.

`sam build` The sam build command builds any dependencies that your application has, and copies your application source code to folders under .aws-sam/build to be zipped and uploaded to Lambda.

```
.aws-sam/build/
├── HelloWorldFunction
│   ├── app.js
│   ├── node_modules
|   |   └── ....
│   └── package.json
└── template.yaml
```

The AWS SAM CLI comes with abstractions for a number of Lambda runtimes to build your dependencies, and copies the source code into staging folders so that everything is ready to be packaged and deployed.

`aws-vault exec -n nb -- sam deploy --guide`

NOTE: we use `-n` otherwise the Role creation fail, don't know why... probably something related to IAM capabilities.

## TODO tutorial basic

SPUNTI: https://medium.com/better-programming/how-to-build-your-first-serverless-api-with-awss-serverless-application-module-and-ci-cd-8ac67cbd8862



Sarebbe carino spiegare come creare una semplice API con NODEJS.

* Http API -> ci da l'URL delle nostre api. Se non lo creiamo explicitamente viene creato implicitamente con logicalID
* Un po' di esempi di API (magari partendo prima con del codice inline)

Come mappare un dominio? Magari in HTTPS ?

Come collegare un layer di authentication? Cognito?




## Alternatives - to Lambda and SAM

`Serverless framework` is an alternative framework that makes it easy to write event-driven functions for a myriad of providers, including AWS, Google Cloud, Kubeless and more.
* https://sanderknape.com/2018/02/comparing-aws-sam-with-serverless-framework/
* https://www.serverless.com/aws-lambda/


* https://epsagon.com/blog/serverless-open-source-frameworks-openfaas-knative-more/

## AWS SAM Specification

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification.html
This section provides details for the AWS SAM template sections, resources types, resource properties, data types, resource attributes, intrinsic functions, and API Gateway extensions that you can use in AWS SAM templates.

AWS SAM templates are an extension of AWS CloudFormation templates. 

### AWS SAM Template Anatomy

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy.html

The primary differences between AWS SAM templates and AWS CloudFormation templates are the following:

* `Transform declaration` identifies an AWS CloudFormation template as an AWS SAM template. SAM resources will generate one or more Cloudformation resources
  * Generated Resources https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-generated-resources.html
  * see Transform in the AWS CloudFormation User Guide: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-section-structure.html 


* `Globals section` The Globals section is unique to AWS SAM. It defines properties that are common to all your serverless functions and APIs. All these resources inherit the properties that are defined in the Globals section:
  * AWS::Serverless::Function
  * AWS::Serverless::Api
  * AWS::Serverless::SimpleTable
  * AWS::Serverless::HttpApi 

Currently, AWS SAM supports the following resources and properties in the Global section:
https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy-globals.html

* `Resources section` In AWS SAM templates the Resources section can contain a combination of AWS CloudFormation resources and AWS SAM resources (prefix `AWS::Serverless::`).

### AWS SAM Resource and Property Reference

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-resources-and-properties.html

* AWS::Serverless::Api
* AWS::Serverless::Application
* AWS::Serverless::Function
* AWS::Serverless::HttpApi
* AWS::Serverless::LayerVersion
* AWS::Serverless::SimpleTable

#### AWS::Serverless::HttpApi

When an AWS::Serverless::HttpApi is specified, AWS Serverless Application Model (AWS SAM) generates the `AWS::ApiGatewayV2::Api` AWS CloudFormation resource.

##### HttpApi Invoke URL

To call a deployed API, clients submit requests to the URL for the API Gateway service for API execution, known as execute-api.

The base URL for REST or HTTP APIs is in the following format:

```
https://{restapi_id}.execute-api.{region}.amazonaws.com/{stage_name}/
```

where `{restapi_id}` is the API identifier, `{region}` is the Region, and `{stage_name}` is the stage name of the API deployment(can be empty for the default).

If needed this URL can be added to the output section of the template and is composed with the `!Sub` function (sadly there isn't a return value for this value)

```yaml
Outputs:
  HttpApiUrl:
    Description: URL of your API endpoint
    Value:
      Fn::Sub: 'https://${HttpApi}.execute-api.${AWS::Region}.${AWS::URLSuffix}/${StageName}/'
  HttpApiId:
    Description: Api id of HttpApi
    Value:
      Ref: HttpApi
```

##### 

## Authoring Serverless SAM Applications

When you author a serverless application using AWS SAM, you construct an AWS SAM template to declare and configure the components of your application.

### Validating AWS SAM Template Files

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-validate.html

Run `sam validate` in the directory that contains your `template.yml`

### Building Applications with Dependencies
 
DOC: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-build.html

`sam build` compiles dependencies for Lambda functions:
* NodeJS: npm install for every package.json
* Python: `requirements.txt`

```
sam build
Building resource 'HelloWorldFunction'
Running NodejsNpmBuilder:NpmPack
Running NodejsNpmBuilder:CopyNpmrc
Running NodejsNpmBuilder:CopySource
Running NodejsNpmBuilder:NpmInstall
Running NodejsNpmBuilder:CleanUpNpmrc

Build Succeeded

Built Artifacts  : .aws-sam/build
Built Template   : .aws-sam/build/template.yaml

Commands you can use next
=========================
[*] Invoke Function: sam local invoke
[*] Deploy: sam deploy --guided
```

`sam build` The sam build command builds any dependencies that your application has, and copies your application source code to folders under .aws-sam/build to be zipped and uploaded to Lambda.

```
.aws-sam/build/
├── HelloWorldFunction
│   ├── app.js
│   ├── node_modules
|   |   └── ....
│   └── package.json
└── template.yaml
```


Use `sam build --use-container` for functions that need to be compiled on Amazon Linux (not this one though).  The build step will be executed in the Docker container.

TODO: capiere quali sono i casi in cui è necessario fare questo passaggio.... in generale mi sembra più safe lavorare nel docker container...

### Working with Layers

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-layers.html

* TODO capire come e quando usarli, sembra un po' un casino gestire le dipendenze....
* Layers and Docker can be used locally

### Nested Application

TODO 

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template-nested-applications.html

```yaml
Resources:
  applicationaliasname:
    Type: AWS::Serverless::Application
```

### Controlling Access to API Gateway APIs - Authorization

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-controlling-access-to-apis.html

TODO

* Lambda authorizers
* Amazon Cognito user pools.
* IAM permissions.
* API keys.
* Resource policies.

## Testing and Debugging Serverless Applications

With the SAM CLI, you can locally test and "step-through" debug your serverless applications before uploading your application to the AWS Cloud.

### Invoking Functions Locally

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-invoke.html

`sam local invoke [OPTIONS] [FUNCTION_IDENTIFIER]`

Where FUNCTION_IDENTIFIER in the example below is `HelloWorldFunction`

```yaml
Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function
```




# AWS Systems Manager

## AWS Session Manager to SSH into EC2 instances

Intro: https://cloudonaut.io/goodbye-ssh-use-aws-session-manager-instead/

Demo: https://www.youtube.com/watch?v=cUEFGKaZOyU

* How to create a web session
* How to audit logs

Doc: 

* https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html
* https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/session-manager.html

Cloudformation: https://github.com/samkeen/aws-ssm-session-manager-example

Session Manager provides secure and auditable instance management without the need to:

* open inbound ports,
* maintain bastion hosts,
* or manage SSH keys. Unfortunately, AWS deploys a single key pair for authenticating via SSH to each EC2 instances. As sharing keys between engineers is a no go, you need to find a way to distribute a key pair per engineer to your EC2 instances.

Main Benefit - Simple and More secure Authentication: 

* Comply with corporate policies that require controlled access to instances, strict security practices, and fully auditable logs with instance access details

* AWS Session Manager uses the Identity and Access Management (IAM) for authentication and authorization. Therefore, you can reuse IAM users or SSO with Azure AD, SAML, … to authenticate and authorize engineers when logging into EC2 instances as well. Multi-factor authentication (MFA) is built into IAM by default. Therefore, it is simple to require administrators to authenticate with a second factor - e.g., an OTP app - before establishing a remote session with an EC2 instance.

* One-click access to instances from the console and CLI

* Port forwarding. Redirect any port inside your remote instance to a local port on a client.


### Prerequisites: SSM Agent, EC2 Instance profile, AWS CLI 

What do you need to configure on your EC2 Instance:

1. SSM Agent must be installed on the instance (installed by defaul on recent AWS Linux images).
2. AWS Cli
For 1 and 2 see here https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-prerequisites.html
Install: https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html
To Test run `session-manager-plugin`
To connect `aws ssm start-session --target i-027b41574af5de383`

3. Every instance must have a specific role connected to the EC2 instance profile.
See here the doc: https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started-instance-profile.html

ADDICTIVE NOTE: We already have sone Cloudformation example with the required profile. EC2InstanceWithSecurityGroupSample.yaml


cloudformation example instance profile, ref : https://github.com/samkeen/aws-ssm-session-manager-example/blob/master/ssm-session-mgr-example.yaml#L103

The required IAM instance profile isn't attached to the instance:

```
  # By default, AWS Systems Manager doesn't have permission to perform actions on your instances.
  # You must grant access by using an AWS Identity and Access Management (IAM) instance profile.
  # https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-configuring-access-role.html
  Ec2InstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      Path: /
      Roles: [ !Ref Ec2InstanceRole ]
  Ec2InstanceRole:
    Type: AWS::IAM::Role
    Properties:
      ManagedPolicyArns:
        # ********** This is really the only adjustment we need to make to enable use of SSM Session Manager
        #            All the AWS::CloudFormation::Init and cloud init script work is setting up cloudwatch logs
        #            to give visibility to the SSM Agent actions.
        - arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforSSM
      AssumeRolePolicyDocument:
        Statement:
          - Effect: Allow
            Principal:
              Service: [ ec2.amazonaws.com ]
            Action:
              - sts:AssumeRole
      Path: /
```
### Using AWS Session Manager with Enhanced SSH and SCP Capability

https://www.tripwire.com/state-of-security/security-data-protection/cloud/aws-session-manager-enhanced-ssh-scp-capability/

### Session Manager: Give Access to User

At Addictive, to allow user to connect via session manger we create a group with this policy attached
https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-restrict-access-quickstart.html

[NOTE] The policy suggested in the example is restricted to a single region, we sligthly changed using `*` to glob every region:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ssm:StartSession"
            ],
            "Resource": [
                "arn:aws:ec2:*:319646432438:instance/i-0df23322e84e45313"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:DescribeSessions",
                "ssm:GetConnectionStatus",
                "ssm:DescribeInstanceProperties",
                "ec2:DescribeInstances"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:GetDocument"
            ],
            "Resource": [
                "arn:aws:ssm:*:319646432438:document/SSM-SessionManagerRunShell"
            ],
            "Condition": {
                "BoolIfExists": {
                    "ssm:SessionDocumentAccessCheck": "true"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:TerminateSession"
            ],
            "Resource": [
                "arn:aws:ssm:*:*:session/${aws:username}-*"
            ]
        }
    ]
}
```

# EC2

## 2020 approach to EC2 Instances Maintainence

https://cloudonaut.io/ec2-instances-2-0-time-to-update-your-toolbox/


Amazon Elastic Compute Cloud (EC2) has more than 13 years of public history and is one of the oldest AWS services. EC2 is a mature service that reinvented itself many times:

* From EC2 classic to Amazon VPC.
* From SSH access to AWS SSM Session Manager.
* From self-managed backup solution to AWS Backup.
* More powerful instance families.
* New pricing options.
* And much more.

## GP2 vs EBS AMI

https://stackoverflow.com/questions/51232230/amazon-ec2-ebs-vs-gp2-ami

## SecurityGroups VS SecurityGroupsIds

https://stackoverflow.com/questions/56676108/cloudformation-throws-value-for-parameter-groupid-is-invalid-the-value-cann

TL;DR: For a nondefault VPC, you must use security group IDs instead. Addictive always use NON DEFAULT VPC.

## Query the Latest AMI 

See the cloudformation section

## Metadata and User Data

* [EC2 AWS DOC](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html)
* https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html
* http://blog.domenech.org/2012/10/aws-ec2-instance-metadata.html
* http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html

User Data:

* User data can be in the form of parameters or user defined script executed when the instance is launched
* User data can be used for bootstrapping EC2 instance and helps answer: "the What should I do?"
* User data is executed only at the launch of the instance. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html

You can pass two types of user data to Amazon EC2:

* shell scripts. User data shell scripts must start with the `#!` characters and the path to the interpreter you want to read the script (commonly /bin/bash)
* cloud-init directives.  The `#cloud-config` line at the top is required in order to identify the commands as cloud-init directives.



Instance metadata and user data can be used for Self Configuration allowing EC2 instance answer the question Who am I ? What should I do ?

Instance metadata and user data can be accessed from within the instance itself

Data is not protected by cryptographic methods. Anyone who can access the instance can view its metadata and should not be used to any store sensitive data, such as passwords, as user data.

Both the metadata and user data is available from the IP address 169.254.169.254 and has the latest as well as previous versions available

Metadata and User data can be retrieved using simple curl or GET command and these requests are not billed


Instance metadata is divided into two categories

* Instance metadata: includes metadata about the instance such as instance id, ami id, hostname, ip address, role etc. Can be accessed from http://169.254.169.254/latest/meta-data/

* Dynamic data: is generated when the instances are launched such as instance identity documents, instance monitoring etc. Can be accessed from http://169.254.169.254/latest/dynamic/

Instance metadata can be used for managing and configuring instances

## CloudFormation Helper Scripts Reference: cfn-init, cfn-signal, cfn-hup

Ref:

* [AWS Doc](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-helper-scripts-reference.html)
* [cfn-hup doc](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-hup.html)
* https://acloud.guru/forums/aws-certified-devops-engineer-professional/discussion/-KGKD6rei-kp6QOv5ne-/whats-the-key-difference-between-cloud-init-and-cfn-init

AWS CloudFormation provides the following Python helper scripts that you can use to install software and start services on an Amazon EC2 instance that you create as part of your stack:

* `cfn-init`: Use to retrieve and interpret resource metadata, install packages, create files, and start services.
* `cfn-signal`: Use to signal with a CreationPolicy or WaitCondition, so you can synchronize other resources in the stack when the prerequisite resource or application is ready.
* `cfn-get-metadata`: Use to retrieve metadata for a resource or path to a specific key.
* `cfn-hup`: Use to check for updates to metadata and execute custom hooks when changes are detected.

To configure cfn-{init,hup} you need to create a configset into your Cloudformation AWS::CloudFormation::Init resource, see below.

Cloud-init VS cfn-init: `cfn-init` is customized version of `cloud-init` for AWS product.

AWS CloudFormation includes a set of helper scripts (cfn-init, cfn-signal, cfn-get-metadata, and cfn-hup) that are based on cloud-init. This is the information I can find from the cfn user guide.


Add users: http://cloudinit.readthedocs.org/en/latest/topics/examples.html#including-users-and-groups


`cfn-hup` helper is a daemon that detects changes in resource metadata and runs user-specified actions when a change is detected.

TODO: is it possible to use cfn-hup to update users and groups ?

### AWS::CloudFormation::Init and Config Sets

[AWS DOC](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-init.html#aws-resource-cloudformation-init-syntax)

The metadata is organized into config keys, which you can group into configsets.

You can specify a configset when you call cfn-init in your template.

If you don't specify a configset, cfn-init looks for a single config key named config.

OREDER NOTE: The cfn-init helper script processes these configuration sections in the following order: packages, groups, users, sources, files, commands, and then services. If you require a different order, separate your sections into different config keys, and then use a configset that specifies the order in which the config keys should be processed.

### Example: User-Data Script

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html#user-data-shell-scripts

This example shows a quite typical combination:

* cfn-init it called on the first boot from the userdata script
* Metadata are used to configure cfn-init using AWS::CloudFormation::Init
* cfn-hup is configured to allow future update when you update AWS::CloudFormation::Init

CloudFormation snippet, it the AWS::CloudFormation::Init type to include metadata on an Amazon EC2 instance for the cfn-init helper script.

```
    ECSLaunchConfiguration:
        Type: AWS::AutoScaling::LaunchConfiguration
        Properties:
            ImageId:  !Ref AmiId
            InstanceType: !Ref InstanceType
            SecurityGroups:
                - !Ref SecurityGroup
            IamInstanceProfile: !Ref ECSInstanceProfile
            UserData:
                "Fn::Base64": !Sub |
                    #!/bin/bash
                    yum install -y https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm
                    yum install -y aws-cfn-bootstrap hibagent
                    /opt/aws/bin/cfn-init -v --region ${AWS::Region} --stack ${AWS::StackName} --resource ECSLaunchConfiguration
                    /opt/aws/bin/cfn-signal -e $? --region ${AWS::Region} --stack ${AWS::StackName} --resource ECSAutoScalingGroup
                    /usr/bin/enable-ec2-spot-hibernation

        Metadata:
            AWS::CloudFormation::Init:
                config:
                    packages:
                        yum:
                            awslogs: []

                    commands:
                        01_add_instance_to_cluster:
                            command: !Sub echo ECS_CLUSTER=${ECSCluster} >> /etc/ecs/ecs.config
                    files:
                        "/etc/cfn/cfn-hup.conf":
                            mode: 000400
                            owner: root
                            group: root
                            content: !Sub |
                                [main]
                                stack=${AWS::StackId}
                                region=${AWS::Region}

                        "/etc/cfn/hooks.d/cfn-auto-reloader.conf":
                            content: !Sub |
                                [cfn-auto-reloader-hook]
                                triggers=post.update
                                path=Resources.ECSLaunchConfiguration.Metadata.AWS::CloudFormation::Init
                                action=/opt/aws/bin/cfn-init -v --region ${AWS::Region} --stack ${AWS::StackName} --resource ECSLaunchConfiguration

                        "/etc/awslogs/awscli.conf":
                            content: !Sub |
                                [plugins]
                                cwlogs = cwlogs
                                [default]
                                region = ${AWS::Region}

                        "/etc/awslogs/awslogs.conf":
                            content: !Sub |
                                [general]
                                state_file = /var/lib/awslogs/agent-state

                                [/var/log/dmesg]
                                file = /var/log/dmesg
                                log_group_name = ${ECSCluster}-/var/log/dmesg
                                log_stream_name = ${ECSCluster}

                                [/var/log/messages]
                                file = /var/log/messages
                                log_group_name = ${ECSCluster}-/var/log/messages
                                log_stream_name = ${ECSCluster}
                                datetime_format = %b %d %H:%M:%S

                                [/var/log/docker]
                                file = /var/log/docker
                                log_group_name = ${ECSCluster}-/var/log/docker
                                log_stream_name = ${ECSCluster}
                                datetime_format = %Y-%m-%dT%H:%M:%S.%f

                                [/var/log/ecs/ecs-init.log]
                                file = /var/log/ecs/ecs-init.log.*
                                log_group_name = ${ECSCluster}-/var/log/ecs/ecs-init.log
                                log_stream_name = ${ECSCluster}
                                datetime_format = %Y-%m-%dT%H:%M:%SZ

                                [/var/log/ecs/ecs-agent.log]
                                file = /var/log/ecs/ecs-agent.log.*
                                log_group_name = ${ECSCluster}-/var/log/ecs/ecs-agent.log
                                log_stream_name = ${ECSCluster}
                                datetime_format = %Y-%m-%dT%H:%M:%SZ

                                [/var/log/ecs/audit.log]
                                file = /var/log/ecs/audit.log.*
                                log_group_name = ${ECSCluster}-/var/log/ecs/audit.log
                                log_stream_name = ${ECSCluster}
                                datetime_format = %Y-%m-%dT%H:%M:%SZ

                    services:
                        sysvinit:
                            cfn-hup:
                                enabled: true
                                ensureRunning: true
                                files:
                                    - /etc/cfn/cfn-hup.conf
                                    - /etc/cfn/hooks.d/cfn-auto-reloader.conf
                            awslogs:
                                enabled: true
                                ensureRunning: true
                                files:
                                    - /etc/awslogs/awslogs.conf
                                    - /etc/awslogs/awscli.conf
```

The value of UserData is a script that will be executed only the first time that the Instance is started, it:

* Install aws-cfn-bootstrap
* execute `cfn-init` which will act accordingly to AWS::CloudFormation::Init

In the

### Debug issues with UserData

If you UserData script has some issue It could exit without sending signals.
When using CloudFormation you could get this error on AutoscalingGroup creation: `Received 1 FAILURE signal(s) out of 1. Unable to satisfy 100% MinSuccessfulInstancesPercent requirement`

See: https://stackoverflow.com/questions/42604753/aws-cloudformation-stack-fails-with-error-received-0-success-signals-out-of-1

cfn-init logs: `tail -f  /var/log/cfn-init.log`

## Amazon Linux Distribution

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-linux-ami-basics.html

[Amazon Linux FAQ](https://aws.amazon.com/amazon-linux-ami/faqs/)

To identify on which version you are running:

* `/etc/image-id` 
* `/etc/system-release`

yum is the package manager

For service management:

* chkconfig:
https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/s2-services-chkconfig

# AWS Systems Manager

## Parameter Store

https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-paramstore.html

AWS Systems Manager Parameter Store provides secure, hierarchical storage for configuration data management and secrets management

### Cloudformation with Parameter Store

AWS::SSM::Parameter::Value

https://aws.amazon.com/it/blogs/mt/integrating-aws-cloudformation-with-aws-systems-manager-parameter-store/




# OpsWorks

[see this post](/guides/opsworks-introduction.html)

# ECS: EC2 Container Service

Doc: https://aws.amazon.com/ecs/
Guide: http://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html
API: http://docs.aws.amazon.com/AmazonECS/latest/APIReference/Welcome.html


## ECR Container registry

Amazon ECR Lifecycle Policies:

* Lifecycle Policy Evaluation Rules https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html#lp_evaluation_rules
* A rule with a tagStatus value of any must have the highest value for rulePriority and be evaluated last.

NOTE: You should expect that after creating a lifecycle policy the affected images are expired within 24 hours.

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

PRODUTION NOTES:

* all new accounts in the Amazon SES sandbox, the followin restriction applies
* To GO INTO PRODUCTION you need to open a support case and it can take SAME DAY. If the limit is 200 mail per day it's faster to obtain.

* You can only send mail to verified email addresses and domains
* and more... see here https://docs.aws.amazon.com/ses/latest/DeveloperGuide/request-production-access.html

To get out the sandbox follow the instruction above

SES can be used with a SMTP interface, it's easy to make it compatible with most libraries.

## SES Cloudformation - CDK

https://binx.io/blog/2019/11/14/how-to-deploy-aws-ses-domain-identities-dkim-records-using-cloudformation/

TODO SES cdk

## What is Amazon SES?

Ref: https://docs.aws.amazon.com/ses/latest/DeveloperGuide/Welcome.html
Is an email platform that provides an easy, cost-effective way for you to send and receive email using your own email addresses and domains.

For example, you can:
* send marketing emails such as special offers,
* transactional emails such as order confirmations, 
* and other types of correspondence such as newsletters. 
* When you use Amazon SES to receive mail, you can develop software solutions such as email autoresponders, email unsubscribe systems, and applications that generate customer support tickets from incoming emails.

### Why use Amazon SES?

Building a large-scale email solution is often a complex and costly challenge for a business. You must deal with infrastructure challenges such as email server management, network configuration, and IP address reputation.

Additionally, many third-party email solutions require contract and price negotiations, as well as significant up-front costs.

Amazon SES (like SENDGRID, etc... ) eliminates these challenges and enables you to benefit from the years of experience and sophisticated email infrastructure Amazon.com has built to serve its own large-scale customer base.

PRO: Amazon SES can be fully setuped with CloudFormation making easy to reproduce similar configuration between different application. You can also leverege the IAM permission system.

### Amazon SES and other AWS services
https://docs.aws.amazon.com/ses/latest/DeveloperGuide/Welcome.html#ses-and-aws

* `SNS` Amazon Simple Notification Service (Amazon SNS) to notify you of your emails that bounced, produced a complaint, or were successfully delivered to the recipient's mail server. When you use Amazon SES to receive emails, your email content can be published to Amazon SNS topics.
* `Route 53` Although you can use Easy DKIM with any DNS provider, it is especially easy to set up when you manage your domain with Route 53
* `S3` Store emails you receive in Amazon Simple Storage Service (Amazon S3).
* `Lambda` Take action on your received emails by triggering AWS Lambda functions
* `KMS` Use AWS Key Management Service (AWS KMS) to optionally encrypt the mail you receive in your Amazon S3 bucket.


# SNS Simple Notification Service

Ref:

* Easy intro: https://tutorialsdojo.com/amazon-sns/
* Developer Guide: https://docs.aws.amazon.com/sns/latest/dg/welcome.html
* Doc: https://aws.amazon.com/sns/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc 


Amazon Simple Notification Service (SNS) is a highly available, durable, secure, fully managed pub/sub messaging service.

SNS is an event-driven computing hub that has native integration with a wide variety of AWS event sources (including EC2, S3, and RDS) and AWS event destinations (including SQS, and Lambda). Event-driven computing is a model in which subscriber services automatically perform work in response to events triggered by publisher services. It can automate workflows while decoupling the services that collectively and independently work to fulfil these workflows.

In Amazon SNS, there are two types of **clients—publishers** and subscribers—also referred to as **producers and consumers**.

Publishers: communicate asynchronously with subscribers by producing and sending a message to a topic, which is a logical access point and communication channel. 

Subscribers: (that is, web servers, email addresses, Amazon SQS queues, AWS Lambda functions) consume or receive the message or notification over one of the supported protocols (that is, Amazon SQS, HTTP/S, email, SMS, Lambda) when they are subscribed to the topic.

Security:  the owner create an SNS topic and control access to it by defining policies that determine which publishers and subscribers can communicate with the topic.

When a message is published on a topic, Amazon SNS matches the topic to a list of subscribers who have subscribed to that topic, and delivers the message to each of those subscribers. Each topic has a unique name that identifies the Amazon SNS endpoint for publishers to post messages and subscribers to register for notifications. Subscribers receive all messages published to the topics to which they subscribe, and all subscribers to a topic receive the same messages.



* Message filtering:
  allows a subscriber to create a filter policy, so that it only gets the notifications it is interested in.

* Message fanout:
  occurs when a message is sent to a topic and then replicated and pushed to multiple endpoints. Fanout provides asynchronous event notifications, which in turn allows for parallel processing.

* SNS mobile notifications (Push Notification, SMS, email):
 SNS allows you to easly fanout mobile push notifications to iOS, Android, Fire OS, Windows and Baidu-based devices. You can also use SNS to fanout text messages (SMS) to 200+ countries and fanout email messages (SMTP). DOC: https://docs.aws.amazon.com/sns/latest/dg/sns-user-notifications.html

* Application and system alerts: 
are notifications, triggered by predefined thresholds, sent to specified users by SMS and/or email.
</span></li><li style="font-weight: 400;"><b>Push email </b><span style="font-weight: 400;">and</span><b> text messaging</b><span style="font-weight: 400;"> are two ways to transmit messages to individuals or groups via email and/or SMS.</span></li><li style="font-weight: 400;"><span style="font-weight: 400;">SNS provides durable storage of all messages that it receives. When SNS receives your </span><i><span style="font-weight: 400;">Publish</span></i><span style="font-weight: 400;"> request, it stores multiple copies of your message to disk. Before SNS confirms to you that it received your request, it stores the message in multiple Availability Zones within your chosen AWS Region.</span></li><li style="font-weight: 400;"><span style="font-weight: 400;">SNS allows you to set a TTL (Time to Live) value for each message. When the TTL expires for a given message that was not delivered and read by an end user, the message is deleted. </span></li></ul>


AWS::SNS::Topic
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic.html#cfn-sns-topic-subscription

## Example: Email subscriber


Status: Pending confirmation

When 

## Example: SNS + Lambda filtering with Cloudformation

https://github.com/claudiobizzotto/aws-cloudformation-notifications/blob/master/cloudformation-notifications.yaml

# CloudWatch

## New Relic Plugin for AWS

* [Plugin Home Page](https://rpm.newrelic.com/accounts/1013453/plugins/directory/58)
* It's available also as chef cookbook, we integrate it into our deploy machine


# CloudFormation


## Intro

* [Doc: Intro](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/CHAP_Intro.html)
* [Reinvent 2013: DMG201 - Zero to Sixty: AWS CloudFormation] (https://www.youtube.com/watch?v=-0ELfN-kb7g)

## Common Cloudformation Use Cases

### EC2 Instance

#### EBS Block Storage or Ephemeral Drive

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-blockdevicemappings

`BlockDeviceMappings` is a property of an `AWS::EC2::Instance` resource. Is a list of `BlockDeviceMapping`.

`BlockDeviceMapping` is documented here:
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-mapping.html

NOTE: You can specify either `VirtualName` or `Ebs`, but not both.

When you specify EBS: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-template.html

```yaml
BlockDeviceMappings:
  - DeviceName: /dev/sdc
    Ebs:
      VolumeSize: 50
      VolumeType: gp2
      DeleteOnTermination: false
```

If you want to initialize the volume from a snapshot use `"SnapshotId": "snap-xxxxxxxx",`

```yaml
BlockDeviceMappings:
  - DeviceName: /dev/sdc
    Ebs:
      SnapshotId: snap-xxxxxxxx
      VolumeSize: 50
      VolumeType: gp2
      DeleteOnTermination: false
```

Examples (https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-mapping.html#aws-properties-ec2-blockdev-mapping--examples):

* Block Device Mapping with two EBS Volumes
* Block Device Mapping with an Ephemeral Drive
* Unmapping an AMI-defined Device


The EBS type 

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-template.html


#### Resize with Cloudformation a volume

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modify-volume.html



#### EC2 enable session manager

https://cloudonaut.io/goodbye-ssh-use-aws-session-manager-instead/

https://github.com/samkeen/aws-ssm-session-manager-example 

```
  # By default, AWS Systems Manager doesn't have permission to perform actions on your instances.
  # You must grant access by using an AWS Identity and Access Management (IAM) instance profile.
  # https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-configuring-access-role.html
  Ec2InstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      Path: /
      Roles: [ !Ref Ec2InstanceRole ]
  Ec2InstanceRole:
    Type: AWS::IAM::Role
    Properties:
      ManagedPolicyArns:
        # ********** This is really the only adjustment we need to make to enable use of SSM Session Manager
        #            All the AWS::CloudFormation::Init and cloud init script work is setting up cloudwatch logs
        #            to give visibility to the SSM Agent actions.
        - arn:aws:iam::aws:policy/service-role/AmazonEC2RoleforSSM
      AssumeRolePolicyDocument:
        Statement:
          - Effect: Allow
            Principal:
              Service: [ ec2.amazonaws.com ]
            Action:
              - sts:AssumeRole
      Path: /
```

### Managed IAM Policies

Yaml policy doc example:
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-iam.html#scenario-bucket-policy



### CloudFormation and OpsWorks

[AWS::OpsWorks::Stack Resource Type](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html)


## CloudFormation Designer

* Video Intro: ( 5min, utile): https://www.youtube.com/watch?v=EeduOlNkMyI
* Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.html
* https://ig.nore.me/2015/11/looking-at-cloudformation-designer/

Tips:

* `ctrl + space` to autocomplete
* `right click` for documentation, edit, duplicate
* CTRL+F: Search within currently open editor pane
* CTRL+\: Format the open pane
* CTRL+SHIFT+\: Strip all whitespace


WARNING: il renaming e i refresh non funzionanano benissimo, per aggiornare il nome di una risorsa:
  * usare la matitina
  * andare su template
  * premere il tasto "Refresh" in alto a DX

## How to write templates

* [Doc: template anatomy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html)
* [Doc: Template References](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-reference.html)


Templates have six major sections. Template structure and sections:

~~~
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

~~~
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

~~~
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

~~~
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



* Doc: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/conditions-section-structure.html

* Samples: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/conditions-sample-templates.html#d0e150834

Example:

~~~
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

### IAM Capabilities

You will need to specify special capability when you create a template with IAM resources
( AWS::IAM::AccessKey, AWS::IAM::Group, AWS::IAM::InstanceProfile, AWS::IAM::Policy, AWS::IAM::Role, AWS::IAM::User, and AWS::IAM::UserToGroupAddition.....)

* the `CAPABILITY_IAM`
* the `CAPABILITY_NAMED_IAM` flag if resources are named

ref: http://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStack.html


### Nested Stacks

* [AWS blog post jan 2015 about ](http://blogs.aws.amazon.com/application-management/post/Tx1T9JYQOS8AB9I/Use-Nested-Stacks-to-Create-Reusable-Templates-and-Support-Role-Specialization)
* http://cloudacademy.com/blog/understanding-nested-cloudformation-stacks/
* http://www.rightbrainnetworks.com/blog/cloudformation-zen-nested-stacks/
* http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html
* http://blog.mikebabineau.com/2014/05/05/cloudformation-nested-stacks-gotcha/

### How to execute code on EC2 instances

* [AWS CloudFormation and Cloud-Init](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-waitcondition-article.html)
* [CloudFormation Helper Scripts Reference](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-helper-scripts-reference.html)

### Merge list of security groups

In this example
https://stackoverflow.com/questions/23335802/add-an-unknown-sized-list-of-security-groups-to-an-ec2-instance/44289165#44289165 the value `SecurityGroupIds` of an `Ec2Instance` is obtained merging a ref to an internal SecurityGroup with a comma separated list of SecurityGroups provided as parameter.

Example: https://github.com/MoveInc/ecs-cloudformation-templates/blob/master/ECS-Cluster.template

### Query for the latest Amazon Linux AMI IDs using AWS Systems Manager Parameter Store

https://aws.amazon.com/blogs/compute/query-for-the-latest-amazon-linux-ami-ids-using-aws-systems-manager-parameter-store/

## Metadata

Metadata can be used for a number of things. The example commonly explained is the use of the AWS::CloudFormation::Init metadata type to provide data to cfn-init, which is a simple configuration management tool. This is not covered in the example, as the work that is being done is simple enough to be done through UserData.

See on the the EC2 chapter.

## Dependencies

A CreationPolicy can be used as a constraint to determine when a resource is counted as created. For example, this can be used with cfn-signal on an EC2 instance to ensure that the resource is not marked as CREATE_COMPLETE until all reasonable post-installation work has been done on an instance (for example, after all updates have been applied or certain software has been installed).

A dependency (defined with DependsOn) is a simple association to another resource that ties its creation with said parent. For example, the web server instances in the example do not start creation until the NAT instance is complete, as they are created in a private network and will not install properly unless they have internet access available to them.

## Stack Policy

* [AWS DOC](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html)

`stack policies` take the form of JSON documents which prohibit or permit various operations to specific or general resources within the existing CloudFormation stack (they are not used in stack creation, only during updates).


* After you set a stack policy, all resources in the stack are protected by default
* You can define only one stack policy per stack
* a single policy protects multiple resources

Reference:

~~~
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

~~~
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

### Changeset

https://aws.amazon.com/it/blogs/aws/new-change-sets-for-aws-cloudformation/

Used to

* preview the changes on stack updates,
* verify that they are in line with their expectations,
* and proceed with the update.
* use IAM to control access to specific CloudFormation functions such as UpdateStack, CreateChangeSet, DescribeChangeSet, and ExecuteChangeSet

You could allow a large group developers to create and preview change sets, and restrict execution to a smaller and more experienced group. With some additional automation, you could raise alerts or seek additional approvals for changes to key resources such as database servers or networks.

Example from cli


```
aws cloudformation create-change-set  --profile=pt --capabilities CAPABILITY_NAMED_IAM --stack-name AccountDefaultGroups --change-set-name prova --template-body file://account_default_groups.yml

aws cloudformation describe-change-set  --profile=pt --stack-name AccountDefaultGroups --change-set-name prova

aws cloudformation execute-change-set  --profile=pt --stack-name AccountDefaultGroups --change-set-name prova
```


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


## ARN Resource Format

Amazon Resource Names (ARNs) uniquely identify AWS resources.

The following are the general formats for ARNs; the specific components and values used depend on the AWS service.

* arn:partition:service:region:account-id:resource
* arn:partition:service:region:account-id:resourcetype/resource
* arn:partition:service:region:account-id:resourcetype:resource

REF for paths and resources: http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces

# AWS support for docker

see [docker](_guides/docker.markdown)

# VPC (Virtual Private Cloud)

## References

* [Short video intro](http://aws.amazon.com/training/intro_series/)
* [AWS VPC DOC](http://aws.amazon.com/vpc/)
* [VPC limits](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Appendix_Limits.html)
* Best Practices: https://blog.james.rcpt.to/2017/01/16/aws-zero-to-hero-in-a-few-hours/
* https://www.slideshare.net/gsilverm/aws-vpc-in

Videos AWS re:Invent 2016:

* BASIC Creating Your Virtual Data Center: VPC Fundamentals and Connectivity (NET201) https://www.youtube.com/watch?v=Ul2NsPNh9Ik   slides: https://www.slideshare.net/AmazonWebServices/aws-reinvent-2016-creating-your-virtual-data-center-vpc-fundamentals-and-connectivity-options-net201
  * 13:00 Internet GW and route table

* ADVANCED: From One to Many: Evolving VPC Design (ARC302) https://www.youtube.com/watch?v=3Gv47NASmU4


## Intro

http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html

A virtual private cloud (VPC) is a virtual network dedicated to your AWS account.

* It is logically isolated from other virtual networks in the AWS Cloud.
* You can launch your AWS resources, such as Amazon EC2 instances, into your VPC.
* it spans all the Availability Zones in the region.
* has a range of IPv4 addresses (CIDR)

NOTE: the ADDICTIVE AWS account supports only VPC (not EC2 Classic)

A VPC subnet is a part of your VPC that can contain resources that share a common subnet mask and that contain instances and resources that can normally only be accessed within that subnet except if you use an internet gateway to make them public.


Your VPC closely resembles a traditional network. You can configure your VPC; you can select its IP address range, create subnets, and configure route tables, network gateways, and security settings. You can connect instances in your VPC to the internet. You can connect your VPC to your own corporate data center, making the AWS cloud an extension of your data center. To protect the resources in each subnet, you can use multiple layers of security, including security groups and network access control lists


## EC2 instances and VPC

You can launch an instance into one of two platforms: EC2-Classic or EC2-VPC

You can use security groups to control who can access your instances. These are analogous to an inbound network firewall that enables you to specify the protocols, ports, and source IP ranges that are allowed to reach your instances. You can create multiple security groups and assign different rules to each group. You can then assign each instance to one or more security groups, and we use the rules to determine which traffic is allowed to reach the instance. You can configure a security group so that only specific IP addresses or specific security groups have access to the instance.


By launching your instances into a VPC you can:

* Assign static private IPv4 addresses to your instances that persist across starts and stops

* Assign multiple IPv4 addresses to your instances

* Define network interfaces, and attach one or more network interfaces to your instances

* Change security group membership for your instances while they're running

* Control the outbound traffic from your instances (egress filtering) in addition to controlling the inbound traffic to them (ingress filtering)

* Add an additional layer of access control to your instances in the form of network access control lists (ACL)

* Run your instances on single-tenant hardware

* Assign IPv6 addresses to your instances

### Elastic Network Interfaces

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html

An elastic network interface (referred to as a network interface in this documentation) is a logical networking component in a VPC that represents a virtual network card.

A network interface must be assigned to a VPC-Subnet and can include the following attributes:

* A primary private IPv4 address from the IPv4 address range of your VPC
* One or more secondary private IPv4 addresses from the IPv4 address range of your VPC
* One Elastic IP address (IPv4) per private IPv4 address
* One public IPv4 address
* One or more IPv6 addresses
* One or more security groups
* A MAC address
* A source/destination check flag

By default, each instance will have a primary network interface.

When you attach an ENI to an istance you will see a new network interface from your OS.


https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html

### EC2 Public IP

* An instance that's launched into EC2-Classic or a default VPC is automatically assigned a public IP address
* An instance that's launched into a nondefault VPC can be assigned a public IP address on launch.

Instances can fail or terminate for reasons outside of your control. If an instance fails and you launch a replacement instance, the replacement has a different public IP address than the original. However, if your application needs a static IP address, you can use an Elastic IP address.


## Topology

* a `VPC` has 1 `region`
* a `subnet` has 1 `route table`
* a `subnet` has 1 `availablity zone`
* `route table` has N `subnet`

### Topology best practices

* Choose a large CIDR, doesn't cost anything, gives you flexibility
* Don't allocate all your IP range at the beginning (you may need new subnet not planned)

example and a good starting point:

* VPC 172.31.0.0/16  (64k addresses)
* one subnet per availability zone 172.31.0.0/24, 172.31.1.0/24, 172.31.2.0/24 (251 addresses, some are reserved)


NOTE: RFC1918 suggest to use these ranges for private intranet: `10.0.0.0 - 10.255.255.255  (10/8 prefix)`, `172.16.0.0 - 172.31.255.255 (172.16/12 prefix)`, `192.168.0.0 - 192.168.255.255 (192.168/16 prefix)`


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

A subnet is closely related with Availability zones:

* Each subnet must reside entirely within one Availability Zone and cannot span zones.
* Each subnet has CIDR block, which is a subset of the VPC CIDR block.
* A subnet is a block of private IP addresses associated to a specific data center (aka Availability Zone).
* Instances deployed into this subnet will be automatically assigned a unique IP from that block.

NOTE: Cidr notation: http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing  ( For example, in IPv4, a prefix size of /29 gives: 2^(32-29) = 2^3 = 8 addresses.)

ROUTING:

* Each subnet MUST have ONE route table: http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Security.html


Public VS private VS VPN-only, depends from the subnet's route table:

* If a subnet's traffic is routed to an Internet gateway, the subnet is known as a public subnet.
* If a subnet doesn't have a route to the Internet gateway, the subnet is known as a private subnet.
* If a subnet doesn't have a route to the Internet gateway, but has its traffic routed to a virtual private gateway, the subnet is known as a VPN-only subnet.

NOTE: You can allow an instance in your VPC to initiate outbound connections to the Internet over IPv4 but prevent unsolicited inbound connections from the Internet using a network address translation (NAT) gateway or instance.

## Security

### Network ACLs / Security Groups

Reinvent 2016: https://youtu.be/Ul2NsPNh9Ik?t=931

DOC:

* http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html#SubnetSecurity
* http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Security.html


Security Groups are the most commonly used:

* used for INBOUND and OUTBOUND traffic
* are STATEFULL: if you allow to initiate the connection, the reply packet is allowed automatically.


* at instance level: `security groups`
* at subnet level: `ACLs` 

Network ACLs Ref: https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_ACLs.html



### VPC Flow log

Reinvent 2016: https://youtu.be/Ul2NsPNh9Ik?t=2757

* Visibility : dump of metadata of what you accept or reject

## VPC Peering

Reinvent 2016: https://youtu.be/Ul2NsPNh9Ik?t=1753

VPC Peering is 2 VPC with NON OVERLAPPING ip ranges that are almost merged.

A new gateway is created after peering, you need to Route traffic throgh it (called `pcx....`).

## Gateway

### Internet gateway

Cloudformation: `AWS::EC2::InternetGateway`

An Internet gateway is a horizontally scaled, redundant, and highly available VPC component that allows communication between instances in your VPC and the Internet.

The iternet gateway is used by:

* The route table
* NAT instances

### NAT Gateway

Cloudformation: `AWS::EC2::NatGateway`

https://aws.amazon.com/it/blogs/aws/new-managed-nat-network-address-translation-gateway-for-aws/

Reinvent 2016: https://youtu.be/Ul2NsPNh9Ik?t=1430

Use case: allow an instance in your VPC to initiate outbound connections to the Internet over IPv4 but prevent unsolicited inbound connections from the Internet using a network address translation (NAT) gateway or instance.

### VPC Endpoint for S3

* Reinvent 2016: https://youtu.be/Ul2NsPNh9Ik?t=2483
* https://blog.james.rcpt.to/2016/09/19/the-move-to-s3-endpoints/

Problem:

* your application data is on S3, if you take the DNS of your bucket it resolve to public routable IP address
* you need to add an Internet Gateway (on NAT gateway) into your VPC Subnet but you don't want if have a private network

Sol:

* `VPC Endpoint for S3` is a gateway specific for S3
* you can create S3 policy associated with a VPC or S3 endpoint


## DNS in a VPC

Reinvent 2016: https://youtu.be/Ul2NsPNh9Ik

Route53: Private Hosted zone


## Regions

VPCs can span availability zones but not regions. In order to interconnect regions, a [peer](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-peering.html) needs to be set up, or the VPCs need to be connected via other means, such as using a VPN.

## VPN and direct connect

TODO

Reinvent 2016: https://youtu.be/Ul2NsPNh9Ik?t=1843

Useful for Private DataCenters

## VPC and the other AWS services

Reinvent 2016: https://youtu.be/Ul2NsPNh9Ik?t=2182

There are several AWS services that can run inside a VPC: RDS, ALB, Elastic cache, Lambda, etc:

* you can use security groups to allow/deny
* DNS names works in your VPC

## How to access instances in a private network: Bastion Host or VPN

Use `pt-cloudformation-templates/linux-bastion.template`, for details see pt-cloudformation-templates/README.md

# RDS

## Migrate from OLD RDS

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html#Overview.RDSSecurityGroups.Compare

In the past we used `DB security groups` with some DB instances that are not in a VPC and on the EC2-Classic platform. Now at Addictive we use only VPC SecurityGroups, the same that we use for every EC2 instance:
* https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html#Overview.RDSSecurityGroups.VPCSec
* AWS::EC2::SecurityGroup

## RDS and VPC

Doc: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html#Overview.RDSSecurityGroups.VPCSec

COMMON SCENARIO: A common use of an RDS instance in a VPC is to share data with an application server running in an Amazon EC2 instance in the same VPC, which is accessed by a client application outside the VPC.

* Your VPC must have at least 1 subnet in at least 2 of the Availability Zones in the region where you want to deploy your DB instance.
* Your RDS instance must have a `DB subnet group`, it's a resource that list in which subnets RDS can create network interfaces.

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbsubnet-group.html

## RDS Postgres

### Postgis
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.html#Appendix.PostgreSQL.CommonDBATasks.PostGIS

### Dump and restore
Generic Postgres notes:
https://docs.google.com/document/d/1J7ggNpPIdU_frNM8k2qhiHVurCJfwTA0cfCHd7-916g/edit#heading=h.hur8f2l741zl

### Drop e and recreate a SCHEMA on RDS

  DROP SCHEMA public CASCADE;
  CREATE SCHEMA public AUTHORIZATION rds_superuser;

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

# ALB Application Load Balancer (ELB V2)

## ALB vs ELB

DOC: http://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html

Conceptually ALB has a lot in common with ELB. It’s a static endpoint that’s always up and will balance traffic based on it’s knowledge of healthy hosts.But ALB introduces two new key concepts:

* content-based routing:
* target groups:  

A single ALB can serve HTTP, HTTP/2 and websockets ( to up to 10 microservice backends ??? forse questa limitazione è stata rimossa).

ALB solves some problems of ELB:

* no longer need hacks for websockets and HTTP referrers
* no longer need multiple ELBs or internal service discovery software (ex: nginx, HAProxy, Consul, Kong, Kubernetes and Docker Swarm) in our microservice application stack to get traffic to our containers ( ELBs cost $18/month minimum, so the cost can really add up).
* EC2 Container Service (ECS) integration for managed container orchestration

## Intro

![ALB Architecture](aws/alb_component_architecture.png "ALB Architecture")

DOC: https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html#request-routing

A load balancer:

* serves as the single point of contact for clients.
* distributes incoming application traffic across multiple targets, such as EC2 instances, in multiple Availability Zones.
* monitors the health of its registered targets and ensures that it routes traffic only to healthy targets.
* You configure your load balancer to accept incoming traffic by specifying one or more listeners.

For the most common use cases you need to know:

* When you create an ALB you get the DNS address to connect to the target behind the ALB
* You can associate an SSL certificate to an ALB's Listener to terminate HTTPS traffic. You cannot pass through the HTTPS traffic but you can still connect to in HTTPS to the targets. see https://stackoverflow.com/questions/42027582/application-load-balancer-elbv2-ssl-pass-through
* To open a port you need to define a listener


AWS::ElasticLoadBalancingV2::LoadBalancer main properties:

* DNS Name: 
  * is assigned when you create the ALB, clients must connect to this address
  * Example: BTproduction-1905833798.eu-west-1.elb.amazonaws.com 
* SecurityGroups: security groups assigned to the load balancer.
  * every service or instance ALB will connect to, must accept connection from this sg.
* Subnets: subnets to associate with the load balancer. The subnets must be in different Availability Zones
* Connection Idle Timeout: an idle timeout that is triggered when no data is sent over the connection for a specified time period.
* https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.html#w2ab2c21c10d643c12
* Scheme: Specifies whether the load balancer is internal (routes requests to targets using private IP addresses) or Internet-facing (routes requests from clients over the Internet to targets in your public subnets).

By default the ALB does't accept connections. You must create a Listener for each Port/Protocol you want to use. A listener is a process that checks for connection requests, using the protocol and port that you configure. 

AWS::ElasticLoadBalancingV2::Listener:

* is associated to ONE ALB
* Has one or more rule. 
* *Rules* determine which requests are routed to a given action. If the action is a ForwardAction, the request is forwarded to a Target registered to one of Target Groups associated with the ForwardAction.
* For each lister a process in the ALB is created and it checks for connection requests, using the protocol and port that you configure. The rules that you define for a listener determine how the load balancer routes requests to the targets in one or more target groups.
* Support Protocols: HTTP, HTTPS and Ports: 1-65535
* DOC: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html

AWS::ElasticLoadBalancingV2::ListenerRule:

* Has ONE Listener
* When a listerer get a request, it process rules to define which requests an Elastic Load Balancing listener takes action on and the action that it takes.

AWS::ElasticLoadBalancingV2::TargetGroup:

* Define the HealthChecks to perform on targets
* Target groups are used to route requests to one or more registered targets when using a load balancer.
* Define default protocol and port for connection to the targets. Each target can ovverride the port to which it is listening; it's very usefull for ECS instances that could run multiple container on the same host, if the port would be fix it could cause conflicts between containers.

https://convox.com/blog/alb/

Routing Algorithm
With Application Load Balancers, the load balancer node that receives the request uses the following process:

Evaluates the listener rules in priority order to determine which rule to apply.

Selects a target from the target group for the rule action, using the routing algorithm configured for the target group. The default routing algorithm is round robin. Routing is performed independently for each target group, even when a target is registered with multiple target groups.

## ALB USE-CASE: Listener Rules and multi-site

How to use AWS Application Load Balancer to setup Multi-Site redirections?
https://medium.com/tensult/multiple-site-redirections-using-aws-application-load-balancer-35bc0d5da6ad


## ALB USE-CASE: Redirect HTTP to HTTPS

See "Redirect ALL HTTP traffic to HTTPS" here https://docs.google.com/document/d/1pPaupcCyc8Lg75Ok5SyxF-JuAtjKAOg56B86XnYnbwI/edit#heading=h.k3a3aksi4tu8


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

### Target Tracking

https://aws.amazon.com/about-aws/whats-new/2017/07/introducing-target-tracking-scaling-policies-for-auto-scaling

With target tracking, you select a load metric for your application, such as “Average CPU Utilization” or the new “Request Count Per Target” metric from Application Load Balancer, set the target value, and Auto Scaling adjusts the number of EC2 instances in your Auto Scaling group as needed to maintain that target. It acts like a home thermostat, automatically adjusting the system to keep the environment at your desired temperature. For example, you can configure target tracking to keep CPU utilization for your fleet of web servers at 50%. From there, Auto Scaling launches or terminates EC2 instances as required to keep the average CPU utilization at 50%

### RequestCountPerTarget CloudWatch Metric

https://aws.amazon.com/about-aws/whats-new/2017/07/application-load-balancer-adds-support-for-new-requestcountpertarget-cloudwatch-metric/

RequestCountPerTarget metric value indicates the average number of requests received by each target in a target group associated with an Application Load Balancer during a specified time period.

# Route53

## Record Set

### Alias Resource Record Set

It can be used only with AWS resources (ELB, CloudFront distribution, etc)

To use an Alias you need to configure the HostedZoneID, the config depends on the type of resource you are using, see below.


* Choosing Between Alias and Non-Alias Resource Record Sets http://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html
* CloudFormation ref: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html
* Hosted Zone ID for the alias doc:
  * http://docs.aws.amazon.com/Route53/latest/APIReference/CreateAliasRRSAPI.html
  * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html#cfn-route53-aliastarget-hostedzoneid


## Registar

In order for Route 53 DNS to become active for your application you need to tell your domain registrar (GoDaddy, DNSimple, NameCheap, 1&1 etc…) to use your hosted zone’s Route 53 nameservers.

How to Transfer a domain to AWS: https://www.youtube.com/watch?v=WWUoQ51jxII


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

# CloudFront

http://cloudacademy.com/blog/amazon-cloudfront-cdn/

## CDN TODO

* Ha senso pensare di caricare Ember da una CDN pubblic?
  * Files may be pre-cached: jQuery is ubiquitous on the web. There’s a high probability that someone visiting your pages has already visited a site using the Google CDN. Therefore, the file has already been cached by your browser and won’t need to be downloaded again.

https://www.sitepoint.com/7-reasons-not-to-use-a-cdn/
https://www.sitepoint.com/7-reasons-to-use-a-cdn/

## CDN Intro

A CDN is a set of servers distributed across the Internet to serve highly available, high performance content to end-users.

Example:

* a request for an image can routed 10 times within the United States before the image was retrieved, which is not an unusually large number of hops.
* If your user were in Europe, the request would be routed through even more networks to reach your server in Seattle.
* IMPACT: The number of networks and the distance that the request and the image must travel have a significant impact on the performance, reliability, and availability of the image.
* you can use `traceroute` to test

A CDN speeds up the distribution of your content by routing each user request to the edge location that can best serve your content. Typically, this is the CloudFront edge location that provides the lowest latency. This dramatically reduces the number of networks that your users' requests must pass through

Among other advantages, a CDN can:

* Offload traffic served directly from the content provider’s origin infrastructure.
* Help manage denial-of-service attacks by absorbing some of the traffic.
* Offer higher availability, lower network latency, and lower packet loss.
* Sometimes reduce your hosting costs.
* Handle increased numbers of concurrent users.

If there are advantages, there will be some negatives too:

* Lock-in dependency on a single CDN provider for support availability.
* Lock-in dependency on a single CDN provider for infrastructure availability.
* Not all CDN providers will have data centers in exactly the geographic locations you need them for each of your projects.

The CDN market has many active providers, including CloudFare, Akamai Technologies, and Limelight Networks.

## CDN Common Mistakes

http://www.yottaa.com/company/blog/networking-and-security/setting-configuring-content-delivery-network-cdn-architecture-experts-share-common-mistakes/

### Serving of duplicate content


Since your website will be serving content from two different domains, it is vital to tell Google that your main URL is the original and the CDN version is a copy. You can do this by adding a rel=“canonical” directive to the http headers of your site. This is an integral step to avoid duplicate content issues with Google and maintaining your rankings.

This issue can raise if both the origin and the CDN are public.

### Don't monitor for low cache hit rates

Not continually checking the logs for low cache hit rates or other types of errors is one of the biggest overlooked mistakes I find sites making. The initial set up is generally based on a few assumptions which, under realistic traffic patterns, do not hold up. Periodically checking those logs will help identify both issues as well as changes in your users’ behavior.

### limit yourself to a single subdomain and domain for your CDN

Don’t limit yourself to a single subdomain and domain for your CDN. Creating multiple aliases for your CDN can be utilized to load assets much faster. Browsers will synchronously load from a single CDN path, but will asynchronously load from multiple CDN paths. In other words, you could have c1.domain.com <http://c1.domain.com/> through c8.domain.com <http://c2.domain.com/> all pointing to the same folder, and then cycle through the subdomains when loading a page.

### Don't autopublish size and resolution modifications upon uploading the asset

Autopublish size and resolution modifications upon uploading the asset, saving yourself from on-the-fly asset production later that delays the user experience. This will ensure retina displays, mobile sizing, and other optimal image sizes are all preloaded so that the first user that visits on a different viewport will experience great performance. Waiting until the file is requested to determine the size and resolution is a huge time-waster.

### Don't use alternative paths

Ensure alternative paths can be loaded in the event that assets cannot be loaded due to an outage. The ability to migrate or enable and disable CDNs can save you some embarrassment in the event of a CDN service outage.

### Don't test the site after swithing

Not thoroughly testing the site after switching on the CDN. I’ve seen several examples of sites which have fallen over when the CDN is switched on, primarily due to the compression of the JS and CSS files, which then causes conflicts. Typically business will switch on a CDN, look at the home page and think that everything is okay; however, subpages such as product, checkout, and blog pages typically tend to be the ones that fall over. The simple solution is to have a blueprint of the website architecture (a sitemap) handy so that you can step through every page and check it thoroughly.

### Not verifying that your caching is caching

Is your CDN really caching? That’s a key question you should be asking, and to find out, you really need to dig into HTTP headers.

* `no-cache HTTP directives`: Many content management systems send no-cache HTTP directives when responding to a request. As a result, you may suddenly find your site is slower with a CDN than without. The reason is that many CDN providers simply honor whatever cache directives your server sends to them. If your server is sending no caching data or a no-cache directive, they may not cache your files.  Your sites will work fine, but you are not getting the benefits of using a CDN.

* recommend checking HTTP headers coming both from your origin servers and the CDN
* digg into the logs of your origin severs

* `The Vary: User-Agent header` : This directive causes the CDN to store different copies for different User-Agents. Given the large number of User-Agents in use today, this undermines the benefit of the CDN. If at all possible, remove this header or check to ensure that your CDN provider can filter it for you.

### Hurt SEO performances

content delivery network architecture – from an SEO perspective, and it can really hurt a site’s online traffic…”

Naming your URLS. Once your files are on your new CDN servers they will have a new URL, and lots of people miss this or don’t understand this. So let’s say our old CSS file was at yourcoolsite.com/css/main.css. Well now that you are using a CDN, your CSS file is located at a URL that might look like this: gem garbledeegoohey24374566fth/main.css. Obviously, this URL won’t do much for you in the way of SEO, so make sure you take your time during this crucial step and name your new URLs in an SEO-friendly or appropriate manner.

### Not setting up proper invalidation rules

When you are caching static content that will never change, this is a simple task. However, many companies use CDNs to increase the performance of changeable data. Most data these days come in chunks; if not all chunks invalidate at the same time, your users may experience what seems to be schizophrenic content.

### URL Canonicalization

Bandwidth is wasted when files are duplicated in different folders on a CDN. This is further compounded if the CDN is case sensitive, as most LINUX environments are. An additional canonicalization issue is where files are addressed using appended query-strings. All of this makes centrally managing information difficult, and worse, means content isn’t being cached correctly for users, contributing to reduced performance.

### Don't automate content upload

companies make when setting up and configuring their CDN architecture is not building, updating, and flushing the CDN into their automated deploy process. It’s often left as a manual step that is easily forgotten and can result in an application with display issues and inconsistencies.

### Not considering the level of effort and timeline for migrating their existing content onto the network

This can take days or even weeks depending on the volume of content the company has accumulated.

This can be mitigated by CDNs that will automatically pull from an origin server, but there’s a tradeoff there in that the first user to request a piece of content will incur the load time for a failed CDN request and pull from the origin server.

But remember to account time if you need to change URLs in your code (imgs, css, etc).

### SSL certificate Compatibility

CDNs are not always 100% compatible with SSL certificates. When setting up a CDN, developers should make sure that it is compatible with SSL certificates, even if they aren’t going to switch to HTTPS now. Some CDNs allow SSL, but only if the certificate is through them. Even for sites without shopping carts, security is important, and search engines are placing extra emphasis on it – so be prepared for the future.



## CloudFront Intro

CloudFront is a web service that speeds up distribution of your static and dynamic web content

When a user requests content that you're serving with CloudFront, the user is routed to the edge location that provides the lowest latency (time delay)

CloudFront requires you to define the server hosting the content you want CloudFront to deliver across the distributed network.
The origin server can be an S3 bucket or an HTTP server (either based in Amazon’s EC2 or locally in your own datacenter).



Origin:

*

Custom vs S3 Origin:

*

HTTPS

Cache Behaviour:

Attenzione a non fare caching dei Cookies

CNAME vs non CNAME:

Non CNAME:

* Cross origin CORS
* change URLs in the html code


Request and Response Behavior for Custom Origins:

http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#ResponseCustomCaching


List of values for Origin and for Cache Behavior Settings


Params for Web distribution: http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesErrorCachingMinTTL

## Distributions

## Web Distributions

### CNAME and Alias

In CloudFront, an alternate domain name, also known as a CNAME, lets you use your own domain name (for example, www.example.com) for links to your objects instead of using the domain name that CloudFront assigns to your distribution.

http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html

### SSL Certificates

To use your SSL certificate:

* you must specify a path using the `--path` option. The path must begin with /cloudfront and must include a trailing slash (for example, /cloudfront/test/ ).
* http://stackoverflow.com/questions/36059152/where-can-i-manage-uploaded-iam-user-ssl-certificates-in-aws/36062067
* http://docs.aws.amazon.com/cli/latest/reference/iam/upload-server-certificate.html

ISSUE: That certificate appears in the Custom SSL Certificate dropdown on new distribution page but it is DISABLED:

* It could take a few minutes for the certificate to propagate
* http://stackoverflow.com/questions/28609262/unable-to-select-custom-ssl-certificate-stored-in-aws-iam

# AWS Developer Tools

## CodeCommit

### Credentials and Permissions

[Managed Policies for AWS CodeCommit](http://docs.aws.amazon.com/codecommit/latest/userguide/access-permissions.html#access-permissions-managed-policies) :

For example, the following specifies the AWS CodeCommit repository named MyDemoRepo registered to the AWS account 111111111111 in the region us-east-2:

* arn:aws:codecommit:us-east-2:111111111111:MyDemoRepo
* arn:aws:codecommit:region:account:repo



Credential setup:

* CodeCommit has a dedicated set of SSH keys and https credentials, each user can configure them from the IAM console
* To create a key and setup you ssh/config follow the instruction [here](http://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-ssh-unixes.html#setting-up-ssh-unixes-keys)
* Note: AWS CodeCommit requires AWS KMS


To access a CodeCommit repo you need 2 set of permissions:

* Permission to access a repo
* Permission to autheticate with a repo

ref: http://docs.aws.amazon.com/codecommit/latest/userguide/access-permissions.html


Git Client setup:

* ref: http://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-ssh-unixes.html
* To give permission to a user to upload his ssh key attach to the user IAMUserSSHKeys and IAMReadOnlyAccess managed policies
* Setup ssh config
* Test `ssh git-codecommit.us-east-2.amazonaws.com` you should see this message: "You have successfully authenticated over SSH...."

NOTE: the IAMUserSSHKeys managed policy is restricted to a single resource

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iam:DeleteSSHPublicKey",
                "iam:GetSSHPublicKey",
                "iam:ListSSHPublicKeys",
                "iam:UpdateSSHPublicKey",
                "iam:UploadSSHPublicKey"
            ],
            "Resource": "arn:aws:iam::*:user/${aws:username}"
        }
    ]
}
```


## CodePipeline

CodePipeline is a Continuous Delivery service that enables you to orchestrate every step of your software delivery process in a workflow that consists of a series of stages and actions. These actions perform the steps of your software delivery process.


## CodeBuild

Cons:

* No native Bitbucket integration
* No Caching can slow down a lot your builds

Pros:

* Billed by minute of usage
* custom integration with SNS and Lambdas
* Are you still building JARs in your IDE?
* Are you looking to remove the need to setup a separate Jenkins environment to build artifacts?
* Do you want to reduce the amount of dedicated build infrastructure you maintain?
* Are you trying to move to a hosted Continuous Integration (CI) server but it’s difficult to get new services approved within your organization?
* your organization uncomfortable having a third party run their builds, but comfortable with running those builds in AWS


Note: can be used to replace the building component of Jenkins and other tools

## CodeDeploy



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

In accordance with the principle of least-privilege:

* decisions default to DENY and an explicit DENY always trumps an ALLOW.

For examples:

* if an IAM policy grants access to an object, the S3 bucket policies denies access to that object, and there is no S3 ACL, then access will be denied.
* if no method specifies an ALLOW, then the request will be denied by default. Only if no method specifies a DENY and one or more methods specify an ALLOW will the request will be allowed.

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

## [JOB] Debug policies with IAM Simulator

https://policysim.aws.amazon.com

EX to test a specific file in a bucket:

* Resource `arn:aws:s3:::people-production-s3/assets/FontAwesome.otf`
* Action `GetObject`



## [JOB] Protecting files on Amazon S3 through Rails app

https://www.newgenapps.com/blog/bid/211045/Protecting-images-on-Amazon-S3-through-Rails-app

## [JOB] Hosting a public Static Website

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


## [JOB] Hosting a private website with basic auth

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

# Elastic Beanstalk


* See `eb config` to manage multimple env easly

## Elastic Beanstalk Stack Release notes

https://aws.amazon.com/releasenotes/AWS-Elastic-Beanstalk

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
