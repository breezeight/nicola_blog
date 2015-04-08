---
layout: post
title: "Ember-cli"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["javascript"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# Refs

[HomePage](http://iamstef.net/ember-cli/)
[GitHub](https://github.com/stefanpenner/ember-cli)
[RoadMap](https://waffle.io/stefanpenner/ember-cli)

# Intro

ember-cli is command line utility which provides a fast asset pipeline
for Ember. It makes really simple and fast to build a project and it's
dependecies (sass, less, linting, etc).

Ember-cli components:

* JS modules, based on ES6 Module Transpiler
  * [ES6 Module Transpiler Homepage](https://github.com/esnext/es6-module-transpiler)
  * [Internals](http://eviltrout.com/2014/05/03/getting-started-with-es6.html)
* Asset compilation: is based on [Broccoli.js]
  * [Nicola Broccoli Guide]({{site.url}}/guides/broccoli.html)
* Testing:
  * [QUnit](http://qunitjs.com/)
  * [Ember Testing package](http://emberjs.com/guides/testing/integration/)
  * [Ember QUnit](https://github.com/rpflorence/ember-qunit)
* Bower.io: for front-end dependencies ( bower.json )
  * [Nicola Bower Guide]({{site.url}}/guides/bower.html)
* NPM for internal dependencies ( package.json )

See deeper intro http://www.ember-cli.com 

# Debug Ember-CLI

Because the `ember` executable is smart enough to detect that a local version is installed in `$PROJECT_HOME/node_modules/emebr-cli` we can safely locale ember-cli files and add a `console.log` statements.

# Ember cli internals

## Ember executable

* `lib/tasks/`
* `lib/commands/`

Build:

### Build Command


## Node Bundle

Ember-cli uses bundleddependencies to include most of its dependencies and keep them stables, see here for details:

* https://docs.npmjs.com/files/package.json#bundleddependencies
* ....

I noticed that if I use `bower install` the global bower is used instead using `ember install:bower` ember will use the bundled version


## Shims

Call it shims if you want to keep the directory generic. A polyfill is a type of shim that retrofits legacy browsers with modern HTML5/CSS3 features usually using Javascript or Flash. A shim, on the other hand, refers to any piece of code that performs interception of an API call and provides a layer of abstraction. It isn't necessarily restricted to a web application or HTML5/CSS3.

A polyfill is code that detects if a certain "expected" API is missing and manually implements it. E.g.

if (!Function.prototype.bind) { Function.prototype.bind = ...; }
A shim is code that intercepts existing API calls and implements different behavior. The idea here is to normalize certain APIs across different environments. 

Ember-cli defines its owns shims:

* https://github.com/stefanpenner/ember-cli-shims

## ES6 modules

TODO: Understand if embercli is still using `es6-module-transpiler`. It looks that the ember-cli web site is outdate:

* https://github.com/ember-cli/ember-cli/commit/c6b65278bea0cbd05a12e9997291808d35418f64
* http://discuss.emberjs.com/t/working-with-docker-ember-cli-in-development/7658


## Resolver

Ember-cli 0.22 uses this Resolver: https://github.com/ember-cli/ember-resolver

See doc: http://www.ember-cli.com/#using-modules

The Ember Resolver is the mechanism responsible for looking up code in your application and converting its naming conventions into the actual:

* classes
* functions
* templates 

that Ember needs to resolve its dependencies, for example, what template to render for a given route.

Actually the Ember-cli 0.22 Resolver extends `Ember.DefaultResolver`. See the code into `ember-resolver/packages/ember-resolver/lib/core.js:` :

~~~
var Resolver = Ember.DefaultResolver.extend
~~~

TODO: capire perchè ember usa babel ma poi ne disabilita il support per i  modules https://github.com/babel/ember-cli-babel

# Why Ember-cli?

* SPEED: The few seconds it takes to generate a production build of our
application are nothing compared to the minutes we are used from a Middleman setup
* the ES6 module transpiler allows you to use and write the future ES6 module syntax.
* The ability to proxy API requests to a different webserver is another promising feature of the Ember CLI server. 
* out of the box support for the history location of the Ember.js router.
* compiling and building your project on the fly when a file change occurs.



# Install

Install: npm -g install ember-cli

http://edgycircle.com/blog/2014-building-an-emberjs-production-application-with-ember-cli/


# Upgrade
see here http://www.ember-cli.com/

NOTE: most modern version of the ember executable will lock at your local directory and will execute the ember-cli version installed locally (like most modern ruby executable do with Bundler)


# Ember-cli Project File Structure

See [here](http://www.ember-cli.com/#folder-layout) the official doc

package.json is the equivalent of a Bundler Gemfile in ruby https://www.npmjs.org/doc/files/package.json.html

