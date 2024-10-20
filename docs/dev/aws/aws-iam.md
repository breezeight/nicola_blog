# AWS IAM #

# WIP

# What is IAM?

https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html


## AWS-VAULT LOGIN  get-federation-token 

Il processo è descritto qua: "Enabling Custom Identity Broker Access to the AWS Console" https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.html

Used by `aws-vault login`, see here https://github.com/99designs/aws-vault/blob/7aa76dcd9a4ce1fde5438241d9a074443302557d/cli/login.go#L143

Ref https://github.com/99designs/aws-vault#how-it-works

* aws-vault uses Amazon's STS service to generate temporary credentials via the `GetSessionToken` or `AssumeRole API` calls. These expire in a short period of time, so the risk of leaking credentials is reduced.

Controlla se la config 
https://github.com/99designs/aws-vault/blob/7aa76dcd9a4ce1fde5438241d9a074443302557d/cli/login.go#L94

NOTE: Only federation tokens or assume role tokens may be used for federated login (not session tokens)

`NewAssumeRoleWithWebIdentityProvider` returns a provider that generates credentials using AssumeRoleWithWebIdentity
* Code: https://github.com/99designs/aws-vault/blob/85ab787a6fa70a4e4a386cd6829260cb9730d33e/vault/vault.go#L140
* `NewSession(creds, config.Region)` create manage the AWS credentials that you use to 


a occhio e croce qua chiama `AssumeRoleWithWebIdentityRequest`
https://github.com/99designs/aws-vault/blob/85ab787a6fa70a4e4a386cd6829260cb9730d33e/vault/assumerolewithwebidentityprovider.go#L54



## IAM + Cognito

https://medium.com/pravin-lolage/authorization-using-cognito-api-gateway-iam-5a1cf01f1915

## Cross Account Roles

Funziona un modo abbastanza simile a come funziona il Business Manager di Facebook:

* Un account AWS concede agli utenti IAM di un secondo account AWS di assumere un ruolo, quindi ricevere delle chiavi temporanee e agire come se fosse un utente, anche loggandosi nella console. dei permessi a un secondo account. 
* Nel secondo account vengono fissate delle policy per decidere quali utenti IAM possono assumere un ruolo nel primo account.




# Use Cases

## Allow IAM users to change their password

https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_enable-user-change.html

## Allow IAM users to manage a Group

https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam_users-manage-group.html


# Identities (Users, Groups, and Roles)

[AWS Doc](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html)

## Roles

An IAM role is an IAM identity that you can create in your account that has specific permissions.

An IAM role is similar to an IAM user:
* it is an AWS identity with permission policies that determine what the identity can and cannot do in AWS.
* However:
  * instead of being uniquely associated with one person, a role is intended to be assumable by anyone who needs it.
  * Credential duration is short: it does not have standard long-term credentials such as a password or access keys associated with it. Instead, when you assume a role, it provides you with temporary security credentials for your role session.

Roles main use-case scenarios are delegation of access to users, applications, or services that don't normally have access to your AWS resources:
* grant users in your AWS account access to resources they don't usually have
* grant users in one AWS account access to resources in another account

Roles can be used by the following:
* An IAM user in the same AWS account as the role
* An IAM user in a different AWS account than the role
* A web service offered by AWS such as Amazon Elastic Compute Cloud (Amazon EC2)
* An external user authenticated by an external identity provider (IdP) service that is compatible with SAML 2.0 or OpenID Connect, or a custom-built identity broker.

### Roles Terms and Concepts

https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html

#### AWS Service Role

A role that an AWS service assumes to perform actions in your account on your behalf.

Most of the time AWS create and manage Service for you, see below "AWS service-linked role" (When you set up some AWS service environments, many services require a role for the service to assume).

https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html

#### AWS service-linked role

Service Linked Roles were introduced in April of 2017. Here is the blog post link that details this: [Introducing an Easier Way to Delegate Permissions to AWS Services: Service-Linked Roles | Amazon Web Services](https://aws.amazon.com/blogs/security/introducing-an-easier-way-to-delegate-permissions-to-aws-services-service-linked-roles/)

What they are essentially is nothing but a regular role with the only difference being that:
* these are pre-defined roles that 
* are assignable only one type of service to perform actions on your behalf. 

I’ll explain with an example below.

When you create a regular role lets say you created a role that has Full S3 access. Now you can assign this role to any User, EC2 or your application, change the trust policies of the role etc. Now on the other hand, service linked roles are a predefined set of permissions that are assignable to only 1 type of service. For example a service linked role for Amazon Lex will have all the permissions it needs for accessing other services on your behalf so that you don’t have to manually create these permissions and this role can only be used by Lex. You cannot modify the trust policy of a service-linked role which means only Lex can assume this role.

https://www.quora.com/What-are-service-linked-roles-in-AWS-IAM-How-is-it-different-from-a-normal-IAM-role

#### AWS service role for an EC2 instance

A special type of service role that an application running on an Amazon EC2 instance can assume to perform actions in your account. This role is assigned to the EC2 instance when it is launched. Applications running on that instance can retrieve temporary security credentials and perform actions that the role allows.

#### Role chaining
Role chaining occurs when you use a role to assume a second role through the AWS CLI or API. For example, assume that User1 has permission to assume RoleA and RoleB. Additionally, RoleA has permission to assume RoleB. You can assume RoleA by using User1's long-term user credentials in the AssumeRole API operation.

See more in the doc.

#### Delegation

The granting of permissions to someone to allow access to resources that you control. Delegation involves setting up a trust between two accounts:
* The first is the account that owns the resource (the trusting account).
* The second is the account that contains the users that need to access the resource (the trusted account).

The trusted and trusting accounts can be any of the following:
* The same account.
* Separate accounts that are both under your organization's control.
* Two accounts owned by different organizations.


To delegate permission to access a resource you create an IAM role in the trusting account that has two policies attached:
* The permissions policy grants the user of the role the needed permissions to carry out the intended tasks on the resource.
* The trust policy specifies which trusted account members are allowed to assume the role.

When you create a trust policy, you cannot specify a wildcard (*) as a principal. The trust policy is attached to the role in the trusting account, and is one-half of the permissions. The other half is a permissions policy attached to the user in the trusted account that allows that user to switch to, or assume the role. A user who assumes a role temporarily gives up his or her own permissions and instead takes on the permissions of the role. When the user exits, or stops using the role, the original user permissions are restored. An additional parameter called external ID helps ensure secure use of roles between accounts that are not controlled by the same organization.

#### Federation

The creation of a trust relationship between an external identity provider and AWS. Users can sign in to a web identity provider, such as Login with Amazon, Facebook, Google, or any IdP that is compatible with OpenID Connect (OIDC). Users can also sign in to an enterprise identity system that is compatible with Security Assertion Markup Language (SAML) 2.0, such as Microsoft Active Directory Federation Services. When you use OIDC and SAML 2.0 to configure a trust relationship between these external [identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html) and AWS, the user is assigned to an IAM role. The user also receives temporary credentials that allow the user to access your AWS resources.

#### Federated user
Instead of creating an IAM user, you can use existing identities from AWS Directory Service, your enterprise user directory, or a web identity provider. These are known as federated users. AWS assigns a role to a federated user when access is requested through an identity provider. For more information about federated users, see Federated Users and Roles in the IAM User Guide.

For more information about federated users, see [Federated Users and Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_access-management.html#intro-access-roles) in the IAM User Guide.

#### Trust policy
A JSON policy document in which you define the principals that you trust to assume the role. A role trust policy is a required resource-based policy that is attached to a role in IAM. The principals that you can specify in the trust policy include users, roles, accounts, and services.

#### Permissions policy
A permissions document in JSON format in which you define what actions and resources the role can use. The document is written according to the rules of the IAM policy language.

#### Permissions boundary
An advanced feature in which you use policies to limit the maximum permissions that an identity-based policy can grant to a role. You cannot apply a permissions boundary to a service-linked role. For more information, see Permissions Boundaries for IAM Entities.

#### Principal
An entity in AWS that can perform actions and access resources. A principal can be an AWS account root user, an IAM user, or a role. You can grant permissions to access a resource in one of two ways:

* You can attach a permissions policy to a user (directly, or indirectly through a group) or to a role.
* For those services that support resource-based policies, you can identify the principal in the Principal element of a policy attached to the resource.

If you reference an AWS account as principal, it generally means any principal defined within that account.

Note: You cannot use a wildcard (*) in the Principal element in a role's trust policy.

#### Role for cross-account access
A role that grants access to resources in one account to a trusted principal in a different account. Roles are the primary way to grant cross-account access. However, some AWS services allow you to attach a policy directly to a resource (instead of using a role as a proxy). These are called resource-based policies, and you can use them to grant principals in another AWS account access to the resource. Some of these resources include Amazon Simple Storage Service (S3) buckets, S3 Glacier vaults, Amazon Simple Notification Service (SNS) topics, and Amazon Simple Queue Service (SQS) queues. To learn which services support resource-based policies, see AWS Services That Work with IAM. For more information about resource-based policies, see How IAM Roles Differ from Resource-based Policies.


### Common Scenarios for Roles: Users, Applications, and Services

https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios.html

#### Providing Access to an IAM User in Another AWS Account That You Own

https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html

 Imagine that you have Amazon EC2 instances that are critical to your organization. Instead of directly granting your users permission to terminate the instances, you can create a role with those privileges.
* PRO:
  * avoid accidental mistakes
  * You can add multi-factor authentication (MFA) protection only to the role so that  users who sign in with an MFA device can assume the role. This balance agility with security.
  * enforce the principle of least privilege: restricting the use of elevated permissions to only those times when they are needed for specific tasks.
  * Auditing:  to help ensure that roles are only used when needed.

[Example Scenario Using Separate Development and Production Accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html#id_roles_common-scenarios_aws-accounts-example)
* Users in the development account might occasionally need to access resources in the production account.
* all users are managed in the development account, but some developers require limited access to the production account.
* The development account has two groups: Testers and Developers, and each group has its own policy.

We will use:
* AWS Security Token Service (AWS STS) AssumeRole API 


#### Providing Access to AWS Accounts Owned by Third Parties

When third parties require access to your organization's AWS resources, you can use roles to delegate access to them. For example, a third party might provide a service for managing your AWS resources.

See how: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html


#### Providing Access to Externally Authenticated Users (Identity Federation)

Your users might already have identities outside of AWS, such as in your corporate directory.

* OpenID Connect
* Federating users with SAML 2.0
* Federating users by creating a custom identity broker application

See how: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html

### Identity Providers and Federation

AWS allow you to federate with many identity providers (IdPs) that support one or both:
* OIDC: Open ID Connect protocol 
* SAML 2.0: Security Assertion Markup Language 2.0 

SAML2.0 and OIDC are the most widely used federation protocols for web based single sign-on.

When you want to configure federation with an external identity provider (IdP) service, you create an IAM identity provider to inform AWS about the IdP and its configuration. This establishes "trust" between your AWS account and the IdP.

Which one should you choose? see https://medium.com/@awskarthik82/simple-guide-to-saml-vs-oidc-33a3349189c6

TL;DR: A combination of OIDC and OAuth2 protocols can be used for various use cases like machine-to-machine authentication, device authentication etc. whereas SAML is not preferred for these use cases.

NOTE:
* OAuth 2.0 is an authorization framework, not an authentication protocol. OAuth 2.0 can be used for a lot of cool tasks, one of which is person authentication.
* OpenID Connect is a “profile” of OAuth 2.0 specifically designed for attribute release and authentication.
* Ref: https://www.gluu.org/resources/documents/articles/oauth-vs-saml-vs-openid-connect/


#### About Web Identity Federation

Typical Scenario:
* mobile app users that accesses AWS resources (S3, DynamoDB, etc). When you write such an app, you'll make requests to AWS services that must be signed with an AWS access key.
* PROBLEM: we strongly recommend that you DO NOT EMBED or distribute LONG-TERM AWS CREDENTIALS with apps that a user downloads to a device, even in an encrypted store.

SOLUTION: web identity federation
* users of your app can sign in using a well-known external identity provider (IdP), such as Login with Amazon, Facebook, Google, or any other OpenID Connect (OIDC)-compatible IdP. 
* They can receive an authentication token, and then exchange that token for temporary security credentials in AWS that map to an IAM role with permissions to use the resources in your AWS account. 
* you don't have to embed and distribute long-term security credentials with your application.

##### Using Amazon Cognito for Mobile Apps

https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc_cognito.html

PRO:
* less code?
* Amazon Cognito is easy to use and provides additional capabilities like anonymous (unauthenticated) access, and synchronizing user data across devices and providers. ???? 

##### Using Web Identity Federation API Operations for Mobile Apps

REF:
* [AWS DOC](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc_manual.html)
* [AWS IAM FEDERATION PLAYGROUND](http://aws.amazon.com/blogs/aws/the-aws-web-identity-federation-playground/)

Scenarios:

* You don't want to use AWS Cognito (ex: to avoid AWS lock-in)
* if you have already created an app that uses web identity federation by manually calling the AssumeRoleWithWebIdentity API


See [AWS DOC](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc_manual.html) for details, key concepts are:
* `AssumeRoleWithWebIdentity` receives IdP's authentication token (ex: Facebook Token) and specify the Amazon Resource Name (ARN) for the IAM role that you created for that IdP.
*  AWS verifies that the token is trusted and valid and if so, returns temporary security credentials to your app that have the permissions for the role that you name in the request.

Basically you tell to AWS to trust Facebook Authentication system (this is Federation)


##### Identifying Users with Web Identity Federation

TODO https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc_user-id.html

Scenarios:
* Give to your user a permission to read and write only in a specific sub-directory of a S3 Bucket.

```bash
myBucket/app1/user1
myBucket/app1/user2
myBucket/app1/user3
...
myBucket/app2/user1
myBucket/app2/user2
myBucket/app2/user3
...
```


#### About SAML 2.0 Federation

TODO https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html

TL;DR: Per ora non lo consideriamo usiamo OIDC

#### Creating IAM Identity Providers

* When you want to configure federation with an external identity provider (IdP) service, you create an IAM identity provider to inform AWS about the IdP and its configuration.
* This establishes "trust" between your AWS account and the IdP. 


##### Creating OpenID Connect (OIDC) Identity Providers
TODO
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html

##### Creating IAM SAML Identity Providers
TODO: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml.html
TL;DR: Per ora non lo consideriamo usiamo OIDC

#### Enabling SAML 2.0 Federated Users to Access the AWS Management Console
TODO  https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-saml.html
TL;DR: Per ora non lo consideriamo usiamo OIDC

#### Enabling Custom Identity Broker Access to the AWS Console

TODO https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.html


## Temporary Security Credentials
[AWS DOC: intro to STS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)


`AWS Security Token Service (AWS STS)` : create and provide trusted users with temporary security credentials.

