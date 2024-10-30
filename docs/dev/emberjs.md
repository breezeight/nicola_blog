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

# Community and Team

* IRC #emberjs on freenode.net
* [Ember Discourse site](http://discuss.emberjs.com/)
* [Ember Core Team Minutes](http://emberjs.com/blog/tags/core-team-meeting-minutes.html)
* http://emberjs.com/community/
* TEAM: http://emberjs.com/team/

books:

* http://balinterdi.com/rock-and-roll-with-emberjs/
* https://leanpub.com/ember-cli-101

Developer team notes: https://github.com/emberjs/core-notes

RFC (request for comments):

* RFC are used for "substantial" changes (ie: add/remove APIs), and we ask that these be put through a bit of a design process and produce a consensus among the Ember core team.
* RFC lifecycle is explained here: https://github.com/emberjs/rfcs#the-rfc-life-cycle
  * Each week a list of new RFC reviewed is reported in the core team notes: https://github.com/emberjs/core-notes/tree/master/ember.js
    * if OK: "final comment period" label added to github pull request and twitted for 7 days
  * After the "final comment period" an RFC may be merged and become "active".
  * Implementation:
    * The author of an RFC is not obligated to implement it.
    * If you are interested in working on the implementation for an 'active' RFC, but cannot determine if someone else is already working on it, feel free to ask (e.g. by leaving a comment on the associated issue).


* All RFCs proposed: https://github.com/emberjs/rfcs/pulls
* All RFCs in the final comment period:  https://github.com/emberjs/rfcs/labels/Final%20Comment%20Period
* All active RFCs: https://github.com/emberjs/rfcs/tree/master/text

You may choose to close a pull request without merging it into the upstream branch. This can be handy if the changes proposed in the branch are no longer needed, or if another solution has been proposed in another branch.


https://twitter.com/emberjs

# Static Website: fastboot and prember

Prember: https://github.com/ef4/prember

* you must configure some URLs that you would like to prerender


# Ember-Cli: How to develop and build Ember.js Project

Ember.js is a Javascript framework for web application.
Ember-cli is command line utility which provides a fast asset pipeline
for Ember.

[Ember-cli Guide](https://cli.emberjs.com/release/)

To be productive with Ember it's really important that you understand
how it works. See here for more notes: [Ember-cli internal guide](ember_cli.md)

Ember Cli will install the `ember` executable

```
ember --version
ember-cli: 3.15.1
node: 12.14.1
os: darwin x64
```

Why do we need a CLI?
The Ember CLI is like a dependency packager, test runner, optimizer, and local server all rolled into one. Since all the features were built to work together, common tasks (such as upgrading the app version or deploying) can be automated with production-ready, open source plugins. The CLI is backwards-compatible with older Ember apps and maintains a six-week release schedule.

## Advanced Pod Layout

https://cli.emberjs.com/release/advanced-use/project-layouts/



## Ember-cli addons

Ember CLI’s addon system provides a way to create reusable units of code, share components and styling, extend the build tooling, and more — all with minimal configuration.

## Writing Addons

https://cli.emberjs.com/release/writing-addons/#addonfilestructure



## Ember-cli Generators

`ember generate route scientists` creates :

* A template to be displayed when the user visits /scientists.
* A Route object that fetches the model used by that template.
* An entry in the application's router (located in app/router.js).
* A unit test for this route.

## Ember Try

ember try:ember 2.14.0

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

# Components

A component is kind of like your own custom HTML tag:

* You can tell that a tag refers to an Ember component because it starts with a capital letter (<ReceivedMessage>).
* Built-in HTML tags start with lowercase letters (<div>, <p>, <table>).
* A component's name is the same as its name on the file system, capitalizing the first letter and every letter following a `-`, and removing the `-` ("pascal case").

## Templates

https://guides.emberjs.com/release/components/

*  Ember's UIs are HTML driven


The central template in an Ember application is th Application template:

* app/templates/application.hbs
* This template is always on screen while the user has your application loaded
* `{{outlet}}` means that any route will be rendered in that place.


Restrictions. There are a handful of restrictions on the HTML that you can put in an Ember template:

* Only valid HTML elements in a <body> tag can be used
* No <script> tags

## Nesting Components in Folders

https://guides.emberjs.com/release/components/introducing-components/#toc_nesting-components-in-folders

```
app/
  components/
    received-message.hbs
      received-message/
        avatar.hbs
        username.hbs
```

Use the `::` separator in templates to access components within a folder: `<ReceivedMessage::Username />`

If you prefer to keep all components in subdir, these syntax equivalent:

* app/components/received-message.hbs
* app/components/received-message/index.hbs

Both allow you to include the components as `<ReceivedMessage />`

## Components Arguments

This component app/components/avatar.hbs: `<div class="avatar" title="{{@title}}">{{@initial}}</div>`

* Have two args: {{@title}} and {{@initial}}
* To use it: `<Avatar @title="Tomster's avatar" @initial="T" />`

@ Syntax:

* Ember uses the `@` syntax for its components instead of normal HTML attribute syntax
* The `...attributes` syntax determines where the attributes from a tag should appear in the component's template.


NOTE:

* If ...attributes appears after an attribute, it overrides that attribute. If it appears before an attribute, it does not.
* In addition, the class attribute is special, and will be merged with any existing classes on the element rather than overwriting them. This allows you to progressively add CSS classes to your components, and makes them more flexible overall.

## Conditional content

`#if` https://guides.emberjs.com/release/components/conditional-content/

```
  {{#if @localTime}}
    <span class="local-time">their local time is {{@localTime}}</span>
  {{/if}}
```

Inline:

* Useful to conditially adding standard attributes
* <div class="avatar {{if @isActive "is-active"}}" title="{{@title}}">

Falsy in Ember Templates:

* 0, false, null, undefined, and the empty string are falsy (like in JS) 
* ... and also the `empty array``

example of true:

```
<Avatar
  @title="Tomster's avatar"
  @initial="T"
  @isActive={{true}}
/>
```

NOTE: we have to wrap the values in double curlies (like {{true}}). Values that are not wrapped in curlies are assigned as strings, matching the behavior of HTML attributes.

example of false by omitting:

```
<Avatar
  @title="Zoey's avatar"
  @initial="Z"
  class="current-user"
/>
```


## Block Content



# Router and Routes

[Guide](https://guides.emberjs.com/release/routing/)

Imagine we are writing a web app for managing a blog. At any given time, we should be able to answer questions like What post are they looking at? and Are they editing it?

In Ember.js, the answer to these questions is determined by the URL.

The URL can be set in a few ways:

* The user loads the app for the first time.
* The user changes the URL manually, such as by clicking the back button or by editing the address bar.
* The user clicks a link within the app.
* Some other event in the app causes the URL to change.
* Regardless of how the URL becomes set, the Ember router then maps the current URL to one or more route handlers.

A route handler can do several things:

* It can render a template.
* It can load a model that is then available to the template.
* It can redirect to a new route, such as if the user isn't allowed to visit that part of the app.
* It can handle actions that involve changing a model or transitioning to a new route.

What is a Route? An object that fetches the model used by that template

When your application starts, the router matches the current URL to the routes that you've defined. The routes (`app/routes/route-name.js`), in turn, are responsible for:

* displaying templates `app/templates/route-name.hbs`
* loading data,
* and setting up application state.

The Router config is here: `app/router.js`

```
Router.map(function() {
  this.route('about', { path: '/about' });
  this.route('favorites', { path: '/favs' });
});
```

`path` is optional, if omitted it will the same as the route name

To add a link to a route from a template: <LinkTo @route="about">About</LinkTo>

## Defining Routes

### Nested Routes

TODO:

* Use case pratico: https://thoughtbot.com/blog/embracing-ember-routes   ma meglio cercarne altri....
* When to don't use them https://ilyaradchenko.com/ember's-nested-routes-and-urls-explored/
* When to use them: https://ilyaradchenko.com/using-nested-routes-in-ember/
* Leggersi meglio come funziona l' {{outlet}} nella parent route


https://guides.emberjs.com/release/routing/defining-your-routes/#toc_nested-routes

```
Router.map(function() {
  this.route('posts', function() {
    this.route('new');
  });
});
```

Assuming you have already generated the posts route, to generate the above nested route you would run: `ember generate route posts/new`

### The Application Route

https://guides.emberjs.com/release/routing/defining-your-routes/#toc_the-application-route

TODO

### Index Routes

https://guides.emberjs.com/release/routing/defining-your-routes/#toc_index-routes

TODO 

### Dynamic Segments

https://guides.emberjs.com/release/routing/defining-your-routes/#toc_dynamic-segments

TODO

`this.route('post', { path: '/post/:post_id' });`

If the user navigates to /post/5, the route will then have the post_id of 5 to use to load the correct post. 

Convention of `:model-name_id`:

* in the example above `Post` will be the Specifyed Route's Model, https://guides.emberjs.com/release/routing/specifying-a-routes-model/

### Wildcard Globbing Routes

https://guides.emberjs.com/release/routing/defining-your-routes/#toc_wildcard--globbing-routes

Usecase: This could be used, for example, if you'd like a catch-all route which is useful when the user enters an incorrect URL not managed by your app.

### Route Handlers

https://guides.emberjs.com/release/routing/defining-your-routes/#toc_route-handlers

### Transitioning Between Routes

https://guides.emberjs.com/release/routing/defining-your-routes/#toc_transitioning-between-routes

Once the routes are defined, how do we go about transitioning between them within our application? It depends on where the transition needs to take place:

* From a template, use <LinkTo /> as mentioned above
* From a route, use the `transitionTo()` method
* From a controller, use the `transitionToRoute()` method
* From anywhere else in your application, such as a component, inject the Router Service and use the `transition()` method

## Linking between routes

https://guides.emberjs.com/release/routing/linking-between-routes/

TODO

## Specifying a Route's Model

https://guides.emberjs.com/release/routing/specifying-a-routes-model/



# Models

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



# Wrapping external code

Wrapping code in Ember

* https://eviltrout.com/2016/02/25/fixing-android-performance.html paragraph ""Wrapping code in Ember"
* https://www.youtube.com/watch?v=S_l_DL8ysQQ

# Widget in Ember

Ember Engines? cerca mail di matte

# Ember Debug

A Flowchart about howto debug an Ember App: https://www.mutuallyhuman.com/blog/2016/08/12/an-ember-debugging-flowchart

# Ember Test

* Toran Billups @toranb
* EMBERCONF 2015 - TEST-DRIVEN DEVELOPMENT BY EXAMPLE https://www.youtube.com/watch?v=2b1vcg_XSR8
  * tutorial inspired by the above talk: http://culttt.com/2015/06/22/writing-your-first-ember-js-acceptance-test/
  * The idea behind this talk is to get feedback with TDD and in giving this demonstration Billups mentions that whenever he watched live coding sessions it was very often the smaller things that proved helped him learn than the bigger picture itself. Throughout this talk Billups commentates the things that he has learnt about Test Driven Development and how he will fail tests to monitor feedback with what is expected.

* Outside In TDD by Toran Billups - Global Ember Meetup gen 2016 https://vimeo.com/146953048
* Write Better Ember Tests https://medium.com/@jonpitch/write-better-ember-tests-d2e22fb76bf2#.p3j9lnv62


# Ember Best Practicies

## Enforce Code Style Guides

https://github.com/DockYard/ember-suave

## Ember Style

Project style:

* https://github.com/chrislopresto/ember-freestyle
* https://usecanvas.com/dockyard/emberconf-2016-living-style-guide-driven-development-chris-lopresto/3PFRQprRsMJKccvGbjGTHF


# Ember Internals


## Reference

* http://discuss.emberjs.com/t/guide-to-hacking-ember/8565/3
* [ALapAround] VIDEO Oct 19, 2015: A lap around the Ember source code with Yehuda Katz https://www.youtube.com/watch?v=RN_kVPga9y8
* How to build, code guidelines, etc: https://github.com/emberjs/ember.js/blob/master/CONTRIBUTING.md

* http://stackoverflow.com/questions/8947156/overview-of-the-ember-js-code


## Run tests

npm install && bower install && npm test

`/tests/index.html?hidepassed&package=ember-metal`

(To see tests in the browser, run npm start and open http://localhost:4200/tests/index.html)

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

#### Helpers

`is_blank.js`:

* Why is it useful? Because it's not easy with JS to check if an object is Empty
* Problems arise because the are different scenarios in which we consider the object empity:
  * an object could be none or undefined (see `isNone` helper)
  * an object with size or length properties set to 0
  * if the object is a function it has a length property (the numeber of args)


`is_empty.js`



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
