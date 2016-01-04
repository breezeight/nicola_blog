---
layout: post
title: "Ember.js"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["javascript"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# Info

* IRC #emberjs on freenode.net
* [Ember Discourse site](http://discuss.emberjs.com/)
* [Ember Core Team Minutes](http://emberjs.com/blog/tags/core-team-meeting-minutes.html)

books:

* http://balinterdi.com/rock-and-roll-with-emberjs/
* https://leanpub.com/ember-cli-101

# How to develop and build an Ember.js Project with Ember-Cli

Ember.js is a Javascript framework for web application. 
Ember-cli is command line utility which provides a fast asset pipeline
for Ember. [Ember-cli Homepage](http://www.ember-cli.com/)

To be productive with Ember it's really important that you understand
how it works. See here for more notes: [Ember-cli internal
guide]({{site.url}}/guides/ember_cli.html)


# Ember Core Concepts

REF: [Ember doc](http://guides.emberjs.com/v1.11.0/concepts/core-concepts/)

* Router
* Routes
* Models
* Templates
* Components

## Controller and views in Ember 2.0

See: https://www.youtube.com/watch?v=QgycDZjOnIg

* controller are not a bad concept simply it will be easier to map it on a single portion of the UI as a component
* MIGRATION HINT: refactor every thing as a component

# config/environment.js

Tutorial: http://blog.yanted.com/2015/04/02/ember-js-quick-tip-4-run-code-in-certain-environments/


Example of `config/environment.js` :

~~~
module.exports = function(environment) {
  // Default env (development)
  var ENV = {
    api: {
      host: 'http://localhost:3000',
    },
  };
 
  if (environment === 'production') {
    ENV.api.host = 'http://www.example.com';
  }
};
~~~

You could access the config by importing it everywhere in your app, from routes to controllers to functions in your lib  folder: `import config from '../config/environment';`

Bay default the `app.js` import environment:

~~~
import Ember from 'ember';
import Resolver from 'ember/resolver';
import loadInitializers from 'ember/load-initializers';
import config from './config/environment';
~~~

environment.js uses the `module.exports` syntax

## HOWTO include code based on the environment

how would you add certain code to your application depending on the environment?
Using `in-repo-addon`

TODO: see here

~~~
+  "ember-addon": {
+    "paths": [
+      "lib/errortracking"
+    ]
~~~

# Broccoli

[Intro blog post](http://www.solitr.com/blog/2014/02/broccoli-first-release)

Is....

It user the Ember-Resolver.

## Ember-Resolver

[Homepage](https://github.com/stefanpenner/ember-resolver)

It uses the es6-module-transpiler see [here](http://eviltrout.com/2014/05/03/getting-started-with-es6.html)

[Ember-cli doc: modules and resolver](http://www.ember-cli.com/#using-modules)

# Ember Object Model: Classes and Instances

Doc: [The Ember Object Model](http://emberjs.com/guides/object-model/classes-and-instances/)
ref:

* [UNDERSTANDING EMBER.OBJECT](http://www.cerebris.com/blog/2012/03/06/understanding-ember-object/): ember prototype chain.

Almost every object in Ember.js is derived from a common object: **Ember.Object**. This object is used as the basis for views, controllers, models, and even the application itself.

This simple architectural decision is responsible for much of the consistency across Ember. Because every object has been derived from the same core object, they all share some core capabilities. Every Ember object can observe the properties of other objects, bind their properties to the properties of other objects, specify and update computed properties, and much more.

* `_super()`
* `Ember.Object.extend()` : define classes
* `create()`: instantiate classes
* `init()`: 

`packages/ember-runtime/lib/system/core_object.js` define ` extend: function extend()` at line 500

~~~javascript
  extend: function extend() {
    var Class = makeCtor();
    var proto;
    Class.ClassMixin = Mixin.create(this.ClassMixin);
    Class.PrototypeMixin = Mixin.create(this.PrototypeMixin);

    Class.ClassMixin.ownerConstructor = Class;
    Class.PrototypeMixin.ownerConstructor = Class;

    reopen.apply(Class.PrototypeMixin, arguments);

    Class.superclass = this;
    Class.__super__  = this.prototype;

    proto = Class.prototype = o_create(this.prototype);
    proto.constructor = Class;
    generateGuid(proto);
    meta(proto).proto = proto; // this will disable observers on prototype

    Class.ClassMixin.apply(Class);
    return Class;
  },
~~~

## Mixin
Ember.Mixin is a [public class](http://emberjs.com/api/classes/Ember.Mixin.html).

The `Ember.Mixin` class allows you to create mixins, whose properties can beadded to other classes:

* Create a Mixin: `Ember.Mixin.create`
* Extend a constructor's prototype with a Mixin using Ember.Object
methods


For instance,

~~~javascript
  App.Editable = Ember.Mixin.create({
    edit: function() {
      console.log('starting to edit');
      this.set('isEditing', true);
    },
    isEditing: false
  });
~~~


### Internals
TODO: `ember-metal/lib/mixin.js` defines the Mixin function but I don't
understand when it is assigned to the Ember namespace to obtain
`Ember.Mixin`

`ember-metal/lib/mixin.js`

~~~javascript
Mixin.create = function() {
  // ES6TODO: this relies on a global state?
  Ember.anyUnprocessedMixins = true;
  var M = this;         ///// TRICK
  return initMixin(new M(), arguments);
};
~~~

TODO: non capisco che cavolo fa questo pezzo qua sopra... perchè fa quel trick con M() ? 
In sostanza un mixin sembra un'oggetto che raccoglie nella property
`properties` tutte i metodi che dell'oggetto che passi a `create()`





# Ember Internals


## Reference

* http://discuss.emberjs.com/t/guide-to-hacking-ember/8565/3
* [ALapAround] VIDEO Oct 19, 2015: A lap around the Ember source code with Yehuda Katz https://www.youtube.com/watch?v=RN_kVPga9y8
* How to build, code guidelines, etc: https://github.com/emberjs/ember.js/blob/master/CONTRIBUTING.md

## Run tests

`/tests/index.html?hidepassed&package=ember-metal`

## Intro to ember internal

function makeCtor()


* **ember-metal/lib/core.js** Define the Ember namespace. A lot of init staff are performed here.

## Source Code Overview

Ember.js consists of several packages including the most relevant ones:

* ember-metal
* ember-runtime
* ember-views
* ember-handlebars
* ember-routing

How deprecations are handled: [ALapAround] VIDEO min 17:00:
  * Deprecation are not bad, removal are bad. That's why Ember want to deprecate as soon as possible to give you time before removal.

How feature flag are handled: [ALapAround] VIDEO min 13:00



### Metal Package

* consists of several foundation technologies: observers, bindings, computed properties, and a run loop.

  * Is the module with least dependencies. It's like the Kernel of the Ember project. Optimisation stuff goes here. [Ref: ALapAround] 

### Runtime Package

* provides the Ember object system along with a handful of useful classes. The object system is built with many of the foundational technologies implemented in metal, but exposes them in a much cleaner way to the application developer.
  * Depends on ember metal 

ember-runtime/lib/system/core_objects.js:

* function makeCtor() // ritorna Class
* var CoreObject = makeCtor(); //CoreObject è contruito da makeCtor()
* CoreObject.PrototypeMixin = Mixin.create(...)

[ALapAround] VIDEO min 23:00: A lot of stuff in this module will be removed in the 2.x cycle

### ember-runtime/lib/system/object.js

### Container package

[ALapAround] VIDEO min 35:00


Responsability:

* is responsible for managing instances, give you instances and caching them
* The container uses the resolver to go grom internal name to location on disk

container.register
container.lookup
container.inject


registry.container to create multiple instances, use cases:
* app.reset() for test -> limitation for parallel test
* registry.container()
* Usefull for fastboot min 44:00 [ALapAround] how the fast boot visit method works



### Ember-views package

is pretty self-explanatory, it's the Ember view system built on top of the runtime. On top of that, is the ember-handlebars package which depends on ember-views to provide auto-updating templates on top of the Handlebars templating system.

### Ember-routing package

provides the system responsible for maintaining the application structure and state. It allows to connect the views to specific parts of your app as well as transitioning between states. For more details see the Router code source



#Ember Data

http://emberjs.com/guides/models/
http://www.toptal.com/emberjs/a-thorough-guide-to-ember-data

Application's controllers and routes have access to this shared store.

