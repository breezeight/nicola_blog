---
layout: post
title: "Ruby: RSpec"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["javascript", "nodejs"]
---

# Contents


{:.no_toc}
- Will be replaced with the ToC, excluding the "Contents" header
* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# TODO

Build RESTful API using NodeJS, ExpressJS and MongoDB:
- https://medium.com/datadriveninvestor/build-restful-api-using-nodejs-expressjs-and-mongodb-df99e18666f6
- https://www.robinwieruch.de/node-express-server-rest-api
* https://www.robinwieruch.de/node-express-server-rest-api

* https://bitbucket.org/blog/deploy-an-express-js-app-to-aws-lambda-using-the-serverless-framework
- https://bitbucket.org/blog/deploy-an-express-js-app-to-aws-lambda-using-the-serverless-framework

# Tools

## VSCode

"ExpressJs 4 Snippet" Extension:

- Complete list of snippets: https://marketplace.visualstudio.com/items?itemName=gurayyarar.expressjs-4-snippets

Example, write `e4-app-post` you will get

```js
app.post("path", (req, res) => {});
```

## Postman

- `brew cask install postman`
- https://www.postman.com/
- Open the app and click "Skip signing in and take me straight to the app"


# Intro

Books:
* [Vasan Subramanian - Pro MERN Stack_ Full Stack Web App Development with Mongo, Express, React, and Node (2019, Apress) - libgen.lc]()

* [Mindmap](https://drive.mindmup.com/map/1pi8cLcLNOy-iRY9X6_DdyH9_AB2L9_qC)


# Express Getting Started - Without Scaffolding

[ExpressJS Official Getting Started](https://expressjs.com/en/starter/installing.html)

```bash
mkdir myapp
cd myapp
npm init
npm install express --save
```

NOTE: `index.js` will be your default entry point


Tutorial REST API only [How to build a REST API with Node js & Express](https://www.youtube.com/watch?v=pKd0Rpw7O48&t=2587s)
* Very basic tutorial, it explain also what REST and HTTP are (very high level), good for absolute code beginner but also for somebody that need a refresh.
* Don't use a Database
* 00:00 - 07:00 Rest Conventions, Show an example of API built without a framework, Callback - Route Handler
* 14:41 Compare the router syntax with and without a framework
* 15:00 Nodemon 
* 16:37 Env Variables
* 19:46 Route Parameters(``), Query Parameters. Ex: GET /api/courses/:id



# TODO Express Getting Started - With Scaffolding

IDEAS:

* NX
* express-generator https://expressjs.com/en/starter/generator.html

# Express Getting Started - ExpressJS Generator

Tutorial:
* [FreeCodeCamp](https://www.youtube.com/watch?v=G8uL0lFFoN0)
  * Use `express-generator`
  * 04:00 `express --view=pug myapp-express-generator`
  * Run the app: `DEBUG=myapp-express-generator:* npm start`
  * 36:00 migration
  * 43:00 save leads into the database
  * 45:30 get leads, fetch them from the database
  * 50:40 show one lead
  * 55:44 edit leads (Non mi piace molto lo stile che hanno seguito: POST /lead/:id/edit avrei usato una PUT)
  * 01:05:00 delete routes

Dirs:

* routes: routing logic
* views: one per page
* bin/www is the initialization script (the one that start your app when you run `npm start`)
* app.js is the main entrypoint for the express app ()

# Express Getting Started - NX

Nx is an open source toolkit for enterprise applications that is created and maintained by the team at Nrwl. It's based on their experience working at Google and helping the Fortune 500 build ambitious Angular applications.


# Middleware

Ref:
* [ExpressJS Using Middleware Doc](https://expressjs.com/en/guide/using-middleware.html)

Middleware functions are functions that have access to:
* the request object (req),
* the response object (res),
and the next middleware function in the application’s request-response cycle. The next middleware function is commonly denoted by a variable named `next`.

An Express application is essentially a series of middleware function calls.

Middleware functions can perform the following tasks:

* Execute any code.
* Make changes to the request and the response objects.
* End the request-response cycle.
* Call the next middleware function in the stack.

If the current middleware function does not end the request-response cycle, it must call next() to pass control to the next middleware function. Otherwise, the request will be left hanging.

An Express application can use the following types of middleware:

* Application-level middleware
* Router-level middleware
* Error-handling middleware
* Built-in middleware
* Third-party middleware

You can load application-level and router-level middleware with an optional mount path. You can also load a series of middleware functions together, which creates a sub-stack of the middleware system at a mount point.

## Application-level middleware



# Routing

## Intro

Ref: 
* [ExpressJS Guide Basic routing](https://expressjs.com/en/starter/basic-routing.html)

Routing refers to determining how an application responds to a client request to a particular endpoint, which is a URI (or path) and a specific HTTP request method (GET, POST, and so on).

Each route can have one or more handler functions, which are executed when the route is matched.

Route definition takes the following structure:

```js
app.METHOD(PATH, HANDLER)
```

Where:

* app is an instance of express.
* METHOD is an HTTP request method, in lowercase (get, post, etc.).
* PATH is a path on the server.
* HANDLER is the function executed when the route is matched.

NOTE:This tutorial assumes that an instance of express named app is created and the server is running. If you are not familiar with creating an app and starting it, see the Hello world example.

The handler is passed in a request object and a response object:

* The request object can be inspected to get the various details of the request, 
* and the response object’s methods can be used to send the response to the client.

## Basic Examples

Respond with Hello World! on the homepage:

```js
app.get('/', function (req, res) {
  res.send('Hello World!')
})
```

Respond to POST request on the root route (/), the application’s home page:

```js
app.post('/', function (req, res) {
  res.send('Got a POST request')
})
```

Respond to a PUT request to the /user route:

```js
app.put('/user', function (req, res) {
  res.send('Got a PUT request at /user')
})
```

Respond to a DELETE request to the /user route:

```js
app.delete('/user', function (req, res) {
  res.send('Got a DELETE request at /user')
})
```

## Route Parameters

Ref: https://expressjs.com/en/guide/routing.html

Route parameters are named **URL segments** that are used to capture the values specified at their position in the URL. The captured values are populated in the req.params object, with the name of the route parameter specified in the path as their respective keys.

* Route path: `/users/:userId/books/:bookId`
* Request URL: `http://localhost:3000/users/34/books/8989`
* req.params: `{ "userId": "34", "bookId": "8989" }`


To define routes with route parameters, simply specify the route parameters in the path of the route as shown below.

```js
app.get('/users/:userId/books/:bookId', function (req, res) {
  res.send(req.params)
})
```

The name of route parameters must be made up of “word characters” `[A-Za-z0-9_]`.

Since the hyphen (-) and the dot (.) are interpreted literally, they can be used along with route parameters for useful purposes.

* Route path: /flights/:from-:to
* Request URL: http://localhost:3000/flights/LAX-SFO
* req.params: { "from": "LAX", "to": "SFO" }

OR:

* Route path: /plantae/:genus.:species
* Request URL: http://localhost:3000/plantae/Prunus.persica
* req.params: { "genus": "Prunus", "species": "persica" }

