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

# Ecosystem we use

* [Broccoli](https://github.com/joliss/broccoli) asset pipeline. It's an
alternative to (grunt, make, Rails pipeline).
* [Ember-cli](http://www.ember-cli.com/)
* [ES6 Module Transpiler](https://github.com/esnext/es6-module-transpiler) see [here](http://eviltrout.com/2014/05/03/getting-started-with-es6.html) to learn how it works

# Broccoli

[Intro blog post](http://www.solitr.com/blog/2014/02/broccoli-first-release)

# Ember-Cli
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



`ember-runtime/lib/system/core_objects.js` define ` extend: function extend()` at line 500

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
function makeCtor()


* **ember-metal/lib/core.js** Define the Ember namespace. A lot of init staff are performed here.

### ember-runtime/lib/system/core_objects.js

* function makeCtor() // ritorna Class
* var CoreObject = makeCtor(); //CoreObject è contruito da makeCtor()
* CoreObject.PrototypeMixin = Mixin.create(...)

### ember-runtime/lib/system/object.js


