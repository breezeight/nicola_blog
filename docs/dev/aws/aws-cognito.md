# What is Amazon Cognito?

AWS Doc: https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html

Amazon Cognito provides authentication, authorization, and user management for your web and mobile apps. Your users can sign in directly with a user name and password, or through a third party such as Facebook, Amazon, Google or Apple.

The two main components of Amazon Cognito are user pools and identity pools. User pools are user directories that provide sign-up and sign-in options for your app users. Identity pools enable you to grant your users access to other AWS services. You can use identity pools and user pools separately or together.

Main Features:

- Amazon Cognito User Pools provide a secure user directory that scales to hundreds of millions of users.
- Federation: your users can sign in through social identity providers such as Apple, Google, Facebook, and Amazon, and through enterprise identity providers such as SAML and OpenID Connect, Oauth 2.0.
- Access control for AWS resources: map users to different roles so your app can access only the resources that are authorized for each user

Cognito User Pool VS Identity Pool: https://serverless-stack.com/chapters/cognito-user-pool-vs-identity-pool.html

The two main components of Amazon Cognito are **user pools** and **identity pools**

## Security and certifications

Amazon Cognito is compliant with SOC 1-3, PCI DSS, ISO 27001, and is HIPAA-BAA eligible.

## Example Scenario: An Amazon Cognito user pool and identity pool used together

https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html

Here the goals are:

1. to authenticate your user,
2. and then grant your user access to another AWS service.

To achieve this:

1. In the first step your app user signs in through a user pool and receives user pool tokens after a successful authentication.
2. Next, your app exchanges the user pool tokens for AWS credentials through an identity pool.
3. Finally, your app user can then use those AWS credentials to access other AWS services such as Amazon S3 or DynamoDB.

# Common Amazon Cognito Scenarios

https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-scenarios.html

# Getting Started with Cognito

Common use cases: https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-getting-started.html

After a successful user pool sign-in, your web or mobile app will receive user pool tokens from Amazon Cognito. (JSON web tokens JWT)

You can use groups in a user pool to control permissions with API Gateway by mapping group membership to IAM roles. The groups that a user is a member of are included in the ID token provided by a user pool when your app user signs in.

# Amazon Cognito user pools

https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html

- A user pool is a user directory in Amazon Cognito.
- Whether your users sign in directly or through a third party, all members of the user pool have a directory profile that you can access through a Software Development Kit (SDK).

User pools provide:

- Sign-up and sign-in services.
- A built-in, customizable web UI to sign in users.
- Social sign-in with Facebook, Google, Login with Amazon, and Sign in with Apple, as well as sign-in with SAML identity providers from your user pool.
- User directory management and user profiles.
- Security features such as multi-factor authentication (MFA), checks for compromised credentials, account takeover protection, and phone and email verification.
- Customized workflows and user migration through AWS Lambda triggers.

# Amazon Cognito Identity Pools (Federated Identities)

https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html

The two main components of Amazon Cognito are user pools and identity pools. Identity pools provide AWS credentials to grant your users access to other AWS services. To enable users in your user pool to access AWS resources, you can configure an identity pool to exchange user pool tokens for AWS credentials.
