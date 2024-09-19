---
layout: post
title: "Ruby: RSpec"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["javascript", "nodejs"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# Intro

# Debug

REFS:

* http://www.100percentjs.com/best-way-debug-node-js/
*
* https://github.com/joyent/node/wiki/Using-Eclipse-as-Node-Applications-Debugger

## Node Native Debugger

It's really similar to pry-byebug. Add a `debugger` statement to your code:

~~~
// myscript.js
x = 5;
setTimeout(function () {
  debugger;
  console.log("world");
}, 1000);
console.log("hello");
~~~

Then run you script with `node debug`:

~~~
node debug server.js
~~~

And then you are able to step through the code in your terminal by using the following commands:

* `cont, c` - Continue execution
* `next, n` - Step next
* `step, s` - Step in
* `out, o` - Step out
* `pause` - Pause running code (like pause button in Developer Tools)

## Node Inspector

More advanced ui than the Native Node Debugger but it doesn't properly handle `ember`, it stops in the wrog line (9 apr 2015)


# REPL Console

`node` command from command line

# Promise

## RSVP

* https://www.npmjs.com/package/rsvp

rsvp is library for promise

* [Promise.hash()](https://www.npmjs.com/package/rsvp#hash-of-promises)

# Node Modules System

Ref:

* [Intro doc](https://github.com/maxogden/art-of-node/#modular-development-workflow)
* [Official doc](https://nodejs.org/api/modules.html)


TODO:

* Does NodeJS support es6 modules in 2019? https://medium.com/the-node-js-collection/an-update-on-es6-modules-in-node-js-42c958b890c
* `export`
* `require`
* `require.resolve`


The NodeJS module system is derived from CommonJS.

One of the useful tools Node.js adds on top of standard ECMAScript is a notation for defining and using modules.


`require()` is a function for loading code from other files, it returns the exports of the module name that you specify.

```
var uniq = require('uniq');
var nums = [ 5, 2, 1, 3, 2, 5, 4, 2, 0, 1 ];
console.log(uniq(nums));
```

Note that require() returned a function and we assigned that return value to a variable called uniq. We could have picked any other name and it would have worked the same. require() returns the exports of the module name that you specify.

## How require looks for files

Ref: https://github.com/browserify/browserify-handbook/blob/master/readme.markdown#how-node_modules-works

**Relative** path : Paths that start with a `./` or `../` are always local to the file that calls require()

* `require('./foo.js');` :  load a file foo.js from the same dir of your main.js file
* `require('../foo.js');` : load from the parent dirs*

**Non-relative** path: such as `require('xyz')` from /beep/boop/foo.js,  node searches these paths in order, stopping at the first match and raising an error if nothing is found:

* `/beep/boop/node_modules/xyz`
* `/beep/node_modules/xyz`
* `/node_modules/xyz`


For each xyz directory that exists, node will:

* first look for an `xyz/package.json` to see if a `main` field exists. The "main" field defines which file should take charge if you require() the directory path.
* second, if there is no package.json or no "main" field, index.js is assumed


Example 1: if /beep/node_modules/xyz is the first match and /beep/node_modules/xyz/package.json has:

```
{
  "name": "xyz",
  "version": "1.2.3",
  "main": "lib/abc.js"
}
```

then the exports from /beep/node_modules/xyz/lib/abc.js will be returned by require('xyz').

Example 2: If there is no package.json or no "main" field, `index.js` is assumed: `/beep/node_modules/xyz/index.js`

If you need to, you can reach into a package to pick out a particular file. For example, to load the lib/clone.js file from the dat package, just do:

```
var clone = require('dat/lib/clone.js')
```

The recursive node_modules resolution will find the first dat package up the directory hierarchy, then the `lib/clone.js` file will be resolved from there. This `require('dat/lib/clone.js')` approach will work from any location where you can require('dat').


## What is an export?

A "module" exports objects and functions by adding them to exports, and another module can import it by using require. The semantics are explained well in the official documentation.

`module.exports` is the object that's actually returned as the result of a `require` call.

To test out which module actually gets loaded by node, you can use the `require.resolve('some_module')` command

## Node.js — module.exports vs exports, what’s the difference ?

https://medium.com/@geekguy/javascript-modues-exports-vs-exports-whats-the-difference-9a61cdb99386


## Internals

* http://eli.thegreenplace.net/2013/05/27/how-require-loads-modules-in-node-js
* https://github.com/joyent/node/blob/master/lib/module.js#L380
* What is the purpose of Node.js module.exports and how do you use it? http://stackoverflow.com/questions/5311334/what-is-the-purpose-of-node-js-module-exports-and-how-do-you-use-it

## Require VS import

* `require` is defined by the node module system
* `import` ???? the rsvp npm package use it.... but other package no (ex: https://github.com/strongloop/express)   WHY??? WHAT is the DIFFERENCE?

may be reading this will answer: https://appdividend.com/2019/01/23/javascript-import-statement-tutorial-with-example/



## HOWTO write a module

https://github.com/maxogden/art-of-node/#how-to-write-a-module

* By default node tries to load module/index.js when you require('module'), any other file name won't work unless you set the main field of package.json to point to it.

## Require package

https://www.npmjs.com/package/resolve
