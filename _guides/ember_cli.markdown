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
* Asset compilation: is based on [Broccoli.js](evernote:///view/11497273/s106/1bf59758-e5f6-4a28-82c2-e63f62944f95/1bf59758-e5f6-4a28-82c2-e63f62944f95/)
* Testing:
  * [QUnit](http://qunitjs.com/)
  * [Ember Testing package](http://emberjs.com/guides/testing/integration/)
  * [Ember QUnit](https://github.com/rpflorence/ember-qunit)
* Bower.io: for front-end dependencies ( bower.json )
  * [Nicola Bower Guide]({{site.url}}/guides/bower.html)
* NPM for internal dependencies ( package.json )

See deeper intro http://www.ember-cli.com 

# Ember cli internals

## Shims

Call it shims if you want to keep the directory generic. A polyfill is a type of shim that retrofits legacy browsers with modern HTML5/CSS3 features usually using Javascript or Flash. A shim, on the other hand, refers to any piece of code that performs interception of an API call and provides a layer of abstraction. It isn't necessarily restricted to a web application or HTML5/CSS3.

A polyfill is code that detects if a certain "expected" API is missing and manually implements it. E.g.

if (!Function.prototype.bind) { Function.prototype.bind = ...; }
A shim is code that intercepts existing API calls and implements different behavior. The idea here is to normalize certain APIs across different environments. 

Ember-cli defines its owns shims:

* https://github.com/stefanpenner/ember-cli-shims


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

