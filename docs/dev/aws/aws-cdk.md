# TODO

Testing

https://aws.amazon.com/blogs/developer/testing-infrastructure-with-the-aws-cloud-development-kit-cdk/

[aws](../aws.md)

# What is the AWS CDK?
[Aws Ref](https://docs.aws.amazon.com/cdk/v2/guide/home.html)

CDK is a developer-friendly version of Cloud Formation.

The AWS CDK lets you build reliable, scalable, cost-effective applications in the cloud with the considerable expressive power of a programming language. This approach yields many benefits, including:

* Build with high-level constructs that automatically provide sensible, secure defaults for your AWS resources, defining more infrastructure with less code.
* Use programming idioms like parameters, conditionals, loops, composition, and inheritance to model your system design from building blocks provided by AWS and others.
* Put your infrastructure, application code, and configuration all in one place, ensuring that at every milestone you have a complete, cloud-deployable system.
* Employ software engineering practices such as code reviews, unit tests, and source control to make your infrastructure more robust.
* Connect your AWS resources together (even across stacks) and grant permissions using simple, intent-oriented APIs.
* Import existing AWS CloudFormation templates to give your resources a CDK API.
* Use the power of AWS CloudFormation to perform infrastructure deployments predictably and repeatedly, with rollback on error.
* Easily share infrastructure design patterns among teams within your organization or even with the public.

The AWS CDK supports TypeScript, JavaScript, Python, Java, C#/.Net, and (in developer preview) Go. Developers can use one of these supported programming languages to define reusable cloud components known as Constructs. You compose these together into Stacks and Apps.


Use the AWS CDK to define your cloud resources in a familiar programming language. The AWS CDK supports TypeScript, JavaScript, Python, Java, and C#/.Net.

Developers can use one of the supported programming languages to define reusable cloud components known as [Constructs](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html). You compose these together into:
* [Stacks](https://docs.aws.amazon.com/cdk/latest/guide/stacks.html)
* [Apps](https://docs.aws.amazon.com/cdk/latest/guide/apps.html)

![CdkAppStacks](CdkAppStacks.png)

Composition is THE pattern of CDK.

[Ref: labs.consol.de](https://labs.consol.de/development/2019/11/04/introduction-to-aws-cdk.html)


An application comprises all the cloud resources that you are going to provision in AWS. It represents basically all your workloads that you are going to deploy to AWS in order to solve the particular business problem you have (or your customer has). An application could consist e.g. of a VPC, RDS instances running databases, EC2 instances running your application and web servers and ALBs distributing load over the EC2 instances.

The application consists of stacks which correspond to CloudFormation stacks. Stacks are there to logically bundle resources which should be deployed together as one unit. You could have e.g. stack A for VPC, Subnets, Security Groups, Network ACLs, Route Tables and other VPC-related configuration, stack B for RDS instances, stack C for application servers and their ALBs and stack D for web servers and their ALBs.

Each stack can include AWS resources either directly or as constructs. A construct is a set of AWS resources which represents a reusable component which may be included in multiple other CDK applications. [Dynamo table viewer](https://github.com/eladb/cdk-dynamo-table-viewer) is an open source example of a construct.

OK, so you start writing a CDK application. You add a couple of stacks to it. The stacks consist of various AWS resources such as SQS queues, Lambdas, S3 buckets, DynamoDB tables etc. You add those resources using the corresponding CDK libraries such as @aws-cdk/aws-ec2. And then you use the CDK tool to deploy your application. The tool executes your code, finds the stacks, generates a CloudFormation template for each of them and deploys these templates producing a CloudFormation stack for each of them:

![how-aws-cdk-works](how-aws-cdk-works.png)

## Why use the AWS CDK?


Comparison with AWS CloudFormation:
* working with it is a challenge, hard to define and get an overview for a complex template in either JSON or YAML format.
* configure networking resources including VPC, subnets, route tables, security groups, bastion hosts, integrate gateway, nat gateways, etc. We need to write around **1000 lines of code in JSON format** using CloudFormation. When we try with AWS CDK, we only need to write around **50 lines of code**. As you can see, AWS CDK can do the same thing, even add more features such as conditional number of NAT gateway, number of subnets and availability zones.
  * [Ref](https://dev.to/hoangleitvn/top-reasons-why-we-use-aws-cdk-over-cloudformation-2b2f)
* Easy to use logic (if statements, for-loops, etc) when defining your infrastructure
* CDK comes with code Completition with IDE
* with CDK you can write tests with JEST [Ref](https://aws.amazon.com/blogs/developer/testing-infrastructure-with-the-aws-cloud-development-kit-cdk/) 
* Use object-oriented techniques to create a model of your system
* Define high level abstractions, share them, and publish them to your team, company, or community
* Organize your project into logical modules
* Use your existing code review workflow

Comparison with AWS Terraform:
* AWS CDK is an imperative programming language, supporting Java, JavaScript, Python, TypeScript and .NET. We can utilize our developer programming skills to reduce the time for learning a new syntax like Terraform. 
* AWS CDK provides commands to **generate the CloudFormation template**, so we can still review the generated CloudFormation template before applying

## Permission

https://docs.aws.amazon.com/cdk/latest/guide/permissions.html

`addToPolicy`: Add to the policy of this principal. 



# Getting started with the AWS CDK
[Aws Ref](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html)

Create an empty app:

```bash
mkdir hello-cdk
cd hello-cdk
cdk init --language javascript
```

The `cdk.json` file tells the CDK Toolkit how to execute your app. The build step is not required when using JavaScript.

The `lib/hello-cdk-stack.js` file defines our stack, let's add an S3 bucket to it.

To add an S3 bucket we need to install a package `npm install @aws-cdk/aws-s3`

```js
const core = require('@aws-cdk/core');
const s3 = require('@aws-cdk/aws-s3');

class HelloCdkStack extends core.Stack {
  constructor(scope, id, props) {
    super(scope, id, props);

    new s3.Bucket(this, 'MyFirstBucket', {
      versioned: true
    });
  }
}

module.exports = { HelloCdkStack }
```

Notice a few things:

* `Bucket` is a construct. This means its initialization signature has scope, id, and props and it is a child of the stack.

* `MyFirstBucket` is the id of the bucket construct, not the physical name of the Amazon S3 bucket. The logical ID is used to uniquely identify resources in your stack across deployments. 

```yml
Resources:
  MyFirstBucketB8884501:
    Type: AWS::S3::Bucket
```


* To specify a physical name for your bucket, set the `bucketName` property (bucket_name in Python) when you define your bucket.

Because the bucket's versioned property is true, versioning is enabled on the bucket.

Useful commands:
* `npm run test`     perform the jest unit tests
* `cdk deploy`       deploy this stack to your default AWS account/region
* `cdk diff`         compare deployed stack with current state
* `cdk synth`        emits the synthesized CloudFormation template
* `cdk ls`           List the stacks in the app 


# Concepts




## Contructs

https://docs.aws.amazon.com/cdk/latest/guide/constructs.html

Constructs are the basic building blocks of AWS CDK apps. A construct represents a "cloud component" and encapsulates everything AWS CloudFormation needs to create the component.

A construct can represent:
* a single resource, such as an Amazon Simple Storage Service (Amazon S3) bucket,
* a higher-level component consisting of multiple AWS CDK resources. Examples of such components include:
  * a worker queue with its associated compute capacity,
  * a cron job with monitoring resources and a dashboard,
  * or even an entire app spanning multiple AWS accounts and regions.

### AWS Construct library

The AWS CDK includes the AWS Construct Library, which contains constructs representing AWS resources. AWS Contructs Lib.:

* [TypeScript](https://docs.aws.amazon.com/cdk/api/latest/typescript/api/index.html)
* ...

There are different levels of constructs in this library:
* `CNF Resources` low-level constructs
* `AWS Resources` high-level resource with additional properties and methods, such as bucket.addLifeCycleRule()
* `Patterns` even higher-level constructs, are designed to help you complete common tasks in AWS, often involving multiple kinds of resources. For example, the aws-ecs-patterns.ApplicationLoadBalancedFargateService construct represents an architecture that includes an AWS Fargate container cluster employing an Application Load Balancer (ALB).

Most of the time you will work with`AWS Resources` and `Patterns`. 

## Identifiers
[Aws Ref](https://docs.aws.amazon.com/cdk/latest/guide/identifiers.html)

Identifiers must be unique within the scope in which they are created; they do not need to be globally unique in your AWS CDK application.

If you attempt to create an identifier with the same value within the same scope, the AWS CDK throws an exception.

## Parameters
https://docs.aws.amazon.com/cdk/latest/guide/parameters.html

Using the AWS CDK, you can both define:
* parameters, which can then be used in the properties of constructs you create,
* and you can also deploy stacks containing parameters.



# ISSUE

## If the stack creation fails with ROLLBACK_COMPLETE, a subsequent deploy will no-op 

https://github.com/aws/aws-cdk/issues/7340#issuecomment-620656644


# FAQ

## method to get current accountId and region 

https://github.com/aws/aws-cdk/issues/1754#issuecomment-513542145

The recommended way is: Stack.of(this).account and Stack.of(this).region. Closing for now. Feel free to reopen.



# WIP


https://gitter.im/awslabs/aws-cdk?at=5d6037d649ac0519239c05b4

Script per gli users: https://gist.github.com/phstc/fada4819a922187ebfed88c27d946889

* username
* tags
* Access type: Programmatic access/ AWS Management Console access (enable password)
* Add user to group
* Add policies
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html



SSM structured:
https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-su-organize.html


Your business organization:
/Finance/Accountants/UserList
/Finance/Analysts/UserList
/HR/Employees/EU/UserList


aws ssm put-parameter \
    --name "/Finance/Analysts/UserList" \
    --value "nicola.brisotto,matteo.briani" \
    --type StringList

aws ssm get-parameters-by-path --path "/Finance/Analysts" 
aws ssm get-parameter --name "/Finance/Analysts/UserList"

delete-parameter --name <value>


Delete parameters by path:
https://stackoverflow.com/questions/52266744/aws-ssm-parameters-store


Example of CDK stack to create users:
https://gist.github.com/phstc/fada4819a922187ebfed88c27d946889


## CDK: programmatic deploy usage

### Soluzione 1 - non va bene in molti casi... per gli utenti iam ok per VPC no ....
è un gran casino, c'è una issue aperta:
https://github.com/aws/aws-cdk/issues/601

Avevo usato su aws-educate-cli la strategia di sintetizzare gli stack CF su file e poi importarli ma ha molti problemi con risorse come le VPC che usano i TOKEN https://docs.aws.amazon.com/cdk/latest/guide/tokens.html

### Soluzione 2 - da testare

Invocare il comando cdk usando 
cdk list --app "npx ts-node bin/cdk-app.ts"

cdk list --app "npx ts-node bin/cdk-app.ts" -c coachAccountId=1 -c crossAccountCoachRoleName=2

## Tutorial EC2
https://medium.com/tysonworks/introduction-to-aws-cdk-with-ec2-example-2355505c70b3


## Tutorial: Build a CDK library

https://garbe.io/blog/2019/03/26/construct-your-own-cdk-construct-library/

## Import existing resources into a Stack

https://aws.amazon.com/blogs/aws/new-import-existing-resources-into-a-cloudformation-stack/

## CDK + ReactApp

https://medium.com/swlh/aws-cdk-and-typescript-deploy-a-static-react-app-to-s3-df74193e9e3d


##  CDK cli internals

ISSUE: Nodejs does not wait for promise resolution - exits instead
https://github.com/nodejs/node/issues/22088

## promptly

https://github.com/aws/aws-cdk/blob/540a7e6d020a2af867adbd9928d32bfec30c97ae/packages/aws-cdk/lib/cdk-toolkit.ts#L241

https://github.com/moxystudio/node-promptly


## yargs

Use yargs to parse cli params: https://github.com/yargs/yargs/blob/master/docs/advanced.md#configurations:

Command configuration:
https://github.com/aws/aws-cdk/blob/master/packages/aws-cdk/bin/cdk.ts


Command dir:
* https://github.com/aws/aws-cdk/blob/ca90f5b8650815641c761eee9fa7d565ce0bc20c/packages/aws-cdk/bin/cdk.ts#L90
* 


Formatted output: https://github.com/aws/aws-cdk/blob/ca90f5b8650815641c761eee9fa7d565ce0bc20c/packages/%40aws-cdk/cloudformation-diff/lib/format.ts#L96





