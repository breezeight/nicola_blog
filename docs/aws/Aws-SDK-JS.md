# What Is the AWS SDK for JavaScript?
[Aws Ref](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/welcome.html)

The AWS SDK for JavaScript provides a JavaScript API for AWS services. You can use the JavaScript API to build libraries or applications for:
* Node.js
* Browsers

Using the SDK for JavaScript in a web browser differs from the way in which you use it for Node.js. The difference comes from the way in which you load the SDK and in how you obtain the credentials needed to access specific web services. When use of particular APIs differs between Node.js and the browser, those differences will be called out.

Using the SDK with `AWS Amplify`:
For browser-based web, mobile, and hybrid apps, you can also use the AWS Amplify Library on GitHub, which extends the SDK for JavaScript, providing a declarative interface. [Ref](https://github.com/aws/aws-amplify)


# Getting Started
## Getting Started in a Browser Script
https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/getting-started-browser.html

## Getting Started in Node.js

https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/getting-started-nodejs.html

npm install aws-sdk

The example uses promises

# Working with Services in the SDK for JavaScript

[Aws Ref](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/working-with-services.html)

* `client classes` (ex: AWS.DynamoDB)
* `service interface` (commonly called `service objects`)

From client classes you create service objects.

The SDK for JavaScript follow the request-response: a service submits an HTTP/HTTPS request to an endpoint for the service.

Invoking an AWS service includes the full request and response lifecycle of an operation on a service object, including any retries that are attempted: 
* A request is encapsulated in the SDK by the `AWS.Request` object.
* The response is encapsulated in the SDK by the `AWS.Response object`
* NOTE: the response is provided to the requestor through one of several techniques:
  * callback function 
  * or a JavaScript promise
  * .....

## Creating and Calling Service Objects

https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/creating-and-calling-service-objects.html


* require an individual service: `require('aws-sdk/clients/SERVICE');`
* require the whole service: `var AWS = require('aws-sdk');`

TODO: You can still access the global AWS namespace without every service attached to it: `require('aws-sdk/global');`..... non so a cosa serva....


You first create a service object through which you access a set of features provided by the underlying client class:
* By default, a service object is configured with the global settings also used to configure the SDK. 
* However, you can configure a service object with runtime configuration data that is specific to that service object. 


In addition to supporting service-specific configuration applied to an individual service object, you can also apply service-specific configuration to all newly created service objects of a given class. For example, to configure all service objects created from the Amazon EC2 class to use the US West (Oregon) (us-west-2) Region, add the following to the AWS.config global configuration object.

AWS.config.ec2 = {region: 'us-west-2', apiVersion: '2016-04-01'};


Specific API version of a service: 
```js
var dynamodb = new AWS.DynamoDB({apiVersion: '2011-12-05'});
```

### Specifying Service Object Parameters

Pass parameters in JSON to the service object: 
```js
s3.getObject({Bucket: 'bucketName', Key: 'keyName'});
```

You can also create a service object with some parmeter configured as default for all the API calls

The value of the params parameter of service objects is a map that specifies one or more of the parameter values defined by the service object. The following example shows the Bucket parameter of an Amazon S3 service object being bound to a bucket named myBucket.

```js
var s3bucket = new AWS.S3({params: {Bucket: 'myBucket'}, apiVersion: '2006-03-01' });
s3bucket.getObject({Key: 'keyName'}); // use the default Bucket: 'myBucket' 
```

## Logging

https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/logging-sdk-calls.html

## Calling Services Asychronously

**Using async/await** 

Rather than using promises, you should consider using async/await. Async functions are simpler and take less boilerplate than using promises. Await can only be used in an async function to asynchronously wait for a value.

### Using an Anonymous Callback Function
https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/using-a-callback-function.html

Each service object method that creates an AWS.Request object can accept an anonymous callback function as the last parameter.

* If the method call succeeds, the contents of the response are available to the callback function in the data parameter.
* If the call doesn't succeed, the details about the failure are provided in the error parameter.

Typically the code inside the callback function tests for an error, which it processes if one is returned. If an error is not returned, the code then retrieves the data in the response from the data parameter. 

* `this`:  Within the callback function, the JavaScript keyword this refers to the underlying AWS.Response. 

In the following example, the httpResponse property of an AWS.Response object is used within a callback function to log the raw response data and headers to help with debugging.

```js
new AWS.EC2({apiVersion: '2014-10-01'}).describeInstances(function(error, data) {
  if (error) {
    console.log(error); // an error occurred
    // Using this keyword to access AWS.Response object and properties
    console.log("Response data and headers: " + JSON.stringify(this.httpResponse));

  } else {
    console.log(data); // request succeeded
  }
});
```

*  the `AWS.Response` object has a Request property that contains the `AWS.Request` that was sent by the original method call, you can also access the details of the request that was made.

### Using a Request Object Event Listener

TODO
https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/using-a-response-event-handler.html

### Using Promise

https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/using-promises.html

The `AWS.Request.promise` method provides a way to call a service operation and manage asynchronous flow instead of using callbacks. I

An `AWS.Request` object is returned when a service operation is **called without a callback function** and the service call is NOT executed.

However, `AWS.Request.promise` immediately starts the service call and returns a promise that is either fulfilled with the response data property or rejected with the response error property.

```js
var request = new AWS.EC2({apiVersion: '2014-10-01'}).describeInstances();

// create the promise object
var promise = request.promise();

// handle promise's fulfilled/rejected states
promise.then(
  function(data) {
    /* process the data */
  },
  function(error) {
    /* handle the error */
  }
);
```


NOTE: if for some obscure reason you don't to use a promise you can stille use the `AWS.Request.send()` method

#### Using Other Promise Implementations

if you need your code to run in environments that don't support the native promise implementation in ECMAScript 5 and ECMAScript 2015, AWS support:

* bluebird
* RSVP
* Q

https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/using-promises.html#using-other-promise-implementations