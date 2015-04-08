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

https://github.com/joyent/node/wiki/Using-Eclipse-as-Node-Applications-Debugger

# REPL Console

`node` command from command line

# Promise

## RSVP

* https://www.npmjs.com/package/rsvp

rsvp is library for promise

* [Promise.hash()](https://www.npmjs.com/package/rsvp#hash-of-promises)

# Modules

Ref:

* [Intro doc](https://github.com/maxogden/art-of-node/#modular-development-workflow)
* [Official doc](https://nodejs.org/api/modules.html)


TODO:

* `export`
* `require`
* `require.resolve`

One of the useful tools Node.js adds on top of standard ECMAScript is a notation for defining and using modules. 

A "module" exports objects and functions by adding them to exports, and another module can import it by using require. The semantics are explained well in the official documentation.

`module.exports` is the object that's actually returned as the result of a `require` call.


To test out which module actually gets loaded by node, you can use the `require.resolve('some_module')` command


## Internals

* http://eli.thegreenplace.net/2013/05/27/how-require-loads-modules-in-node-js
* https://github.com/joyent/node/blob/master/lib/module.js#L380
* What is the purpose of Node.js module.exports and how do you use it? http://stackoverflow.com/questions/5311334/what-is-the-purpose-of-node-js-module-exports-and-how-do-you-use-it

## Require VS import

* `require` is defined by the node module system
* `import` ???? the rsvp npm package use it.... but other package no (ex: https://github.com/strongloop/express)   WHY??? WHAT is the DIFFERENCE?




 
## HOWTO write a module

https://github.com/maxogden/art-of-node/#how-to-write-a-module

* By default node tries to load module/index.js when you require('module'), any other file name won't work unless you set the main field of package.json to point to it.

## Require package

https://www.npmjs.com/package/resolve
