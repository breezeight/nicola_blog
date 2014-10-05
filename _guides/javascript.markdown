---
layout: post
title: "Javascript"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["javascript"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}




# References:

Books:

* [SOJS](/Volumes/ArchiveDisk/Archive/Misc/ebook/javascript/Secrets_of_the_JavaS.pdf)    http://www.manning.com/resig/
* [FJS](/Volumes/ArchiveDisk/Archive/Misc/ebook/javascript/Functional_JavaScript.pdf)


* [Codeacademy](http://www.codecademy.com/en/tracks/javascript)

Blogs:

* http://perfectionkills.com/


# TODO
typeof -> how does it works?


# Functions

Function, not objects are at the core of JavaScript

JS is Functional language, functions are first-class objects


Anonymous functions:
function(){return "test"}

* Functions can be arguments of other functions.
* All Functions have the **name** property, if it's anonymous name is an empty string.
* Functions can be referenced by variables `var canFly = function(){ return true; };`
* A Function can be invoked through a variable that reference the function `var canFly = function(){ return true; }; canFly() )`


For more example about how to declare functions: see [SOJS] pag 40

## Scope

* In JS **scope are declared by functions not blocks**

In the example x is still in scope after the end of the block because
the function scope is not changed:

~~~
if(window) {
  var x = 123
}
alert(x)
~~~

* named global functions are property of the window object
* a function is available throughout the scope it is declared. Also if it
is declared at the end of the scope it is available also at the
beginning of the scope.
* a variable is available only after it is declared to the end of the
scope (the inner example here file:///devel/SRC/JAVASCRIPT/ninja-code/chapter-3/listing-3.2.html,
inner is defined after a but it is in scope before the variable a).
* for the purpose of declaration scopes the global context act acts like
one big function encompassing the code on the page.



http://www.smashingmagazine.com/2009/08/01/what-you-need-to-know-about-javascript-scope/

### More about Forward Declaration in Javascript or Hoisting

See:
* http://www.i-programmer.info/programming/javascript/5364-javascript-hoisting-explained.html
* http://www.w3schools.com/js/js_hoisting.asp

**NOTE** JavaScript in _strict mode_ does not allow variables to be used if they are not declared.

### Closures

~~~javascript
      var outerValue = 'ninja';
      var later;

      function outerFunction() {
        var innerValue = 'samurai';

        function innerFunction(paramValue) {                       //#1
          assert(outerValue,"Inner can see the ninja.");
          assert(innerValue,"Inner can see the samurai.");
          assert(paramValue,"Inner can see the wakizashi.");       //#2
          assert(tooLate,"Inner can see the ronin,");              // All variables in an outer scope, even those declared after the function declaration, are included.
        }

        later = innerFunction;
      }

      assert(!tooLate,"Outer can't see the ronin");                //#3

      var tooLate = 'ronin';                                       //#4

      outerFunction();
      later('wakizashi');                                          //#5
~~~

When we declared innerFunction() inside the outer function a closure was also created that encompasses not only the function declaration, but also all variables that are in scope at the point of the declaration.
This “bubble,” containing the function and its variables, stays around as long as the function itself does.

Function parameters are included in the closure of that function. (Seems obvi- ous, but now we’ve said it for sure.

* All variables in an outer scope, even those declared after the function declaration, are included.
* Within the same scope, variables not yet defined cannot be forward-referenced.

#### Private variable using closures

SOJS ch 5.2
All assert are true, we can use the accessor method to obtain the value of the private variable, but that we cannot access it directly.

~~~javascript

      function Ninja() {                                            //#1

        var feints = 0;                                             //#2

        this.getFeints = function(){                                //#3
          return feints;                                            //#3
        };                                                          //#3

        this.feint = function(){                                    //#4
          feints++;                                                 //#4
        };                                                          //#4
      }

      var ninja = new Ninja();                                      //#5

      ninja.feint();                                                //#6

      assert(ninja.feints === undefined,                            //#7
          "And the private data is inaccessible to us." );          //#7

      assert(ninja.getFeints() == 1,                                //#8
             "We're able to access the internal feint count." );    //#8
~~~

#### Timers and callbacks using closures

SOJS ch 5.2.2

In this chapter there are a nice example to avoid pollution of the global scope using closure.

#### Common Errors with events handlers and how to fix them: bind()

SOJS ch 5.3:

~~~javascript
  var button = {
    clicked: false,
    click: function(){
      this.clicked = true;
      assert(button.clicked,"The button has been clicked");
      //FAILS: the context of the click function is not refer- ring to the button object as we intended.
} };
  var elem = document.getElementById("test");
  elem.addEventListener("click",button.click,false);
~~~

the context of the click function is not refer- ring to the button object as we intended.
To solve:

~~~javascript

  function bind(context,name){
    return function(){
      return context[name].apply(context,arguments);
    };
}
  var button = {
    clicked: false,
    click: function(){
      this.clicked = true;
      assert(button.clicked,"The button has been clicked");
      console.log(this);
} };
var elem = document.getElementById("test"); elem.addEventListener("click",bind(button,"click"),false);

~~~


The secret sauce that we’ve added here is the bind() method. This method is designed to create and return a new anonymous function that calls the original function, using apply(), so that we can force the context to be whatever object we want.

### Prototype

All functions have a prototype property that initially references an empty object. This property doesn’t serve much purpose until the function is used as a constructor (using the `new` operator).



Instance members created inside a constructor will occlude properties of the same name defined in the prototype.

Each object in JavaScript has an implicit property named `constructor` that references the constructor that was used to create the object. And because the prototype is a property of the constructor, each object has a way to find its prototype.

**NOTE**: _ONLY functions_ have a prototype property, _EVERY object_ has a
costructor property!

* _instanceof_ operator for a constructed object tests for its constructor.

### JS Scope Exercise
http://stackoverflow.com/questions/18067742/variable-scope-in-nested-functions-in-javascript

http://doppnet.com/2011/10/10-advanced-javascript-interview-questions/

http://www.codecademy.com/forums/javascript-intro/4/exercises/2


### Scope example

#### Ex 1


~~~javascript
var foo;
function setFoo(val) {
  var foo = val;
}
setFoo(10);
alert(foo); // print undefined
~~~

if you remove the var:

~~~javascript

var foo;
function setFoo(val) {
   foo = val;  //removed var
}
setFoo(10);
alert(foo); // print 10

~~~

http://www.codecademy.com/forum_questions/4f166ff96390db0001003803



## Function invocation

Function can be invoked as:

+ functions
+ methods
+ constructors
+ via call() or apply()

The main difference between different kind of invocation is the object
referenced by `this`.

**this** is the function context:

* Different than Java, is not the reference to the instance of the class
* represent different things, depends on the invocation type

Functions can be invoked in various ways, and the invocation mechanism determines the function context value (`this`):

+ When invoked as a simple function, the context is the global object (window).
+ When invoked as a method, the context is the object owning the method.
+ When invoked as a constructor, the context is a newly allocated object.
+ When invoked via the apply() or call() methods of the function, the context can be whatever the heck we want.

**arguments** : 

* collection of all arguments provided to the function
* (has a `length` property).
* Is not an Array but array notation can be used `arguments[2]`.


A function can invoked with:

* more arguments than in the function signature: is allowed...yes ???
* less arguments than in the function signature: is allowed. Missing params are set
to `undefined`.


### call() and apply()
see [SOJS] paragraph 3.3.5

Usecases: implement a "foreach", implement a callback system

To invoke a function using its `apply()` method, we pass two parameters to apply(): the object to be used as the function context, and an array of values to be used as the invocation arguments. The `call()` method is used in a similar manner, except that the arguments are passed directly in the argument list rather than as an array.

~~~javascript
<script type="text/javascript">
  function juggle() {
    var result = 0;
    for (var n = 0; n < arguments.length; n++) {
      result += arguments[n];
    }
    this.result = result;
  }
  var ninja1 = {};
  var ninja2 = {};
  juggle.apply(ninja1,[1,2,3,4]);
  juggle.call(ninja2,5,6,7,8);
￼￼￼￼￼￼e Sets up test subjects
￼￼￼￼￼￼￼  assert(ninja1.result === 10,"juggled via apply");
  assert(ninja2.result === 26,"juggled via call");
</script>
~~~

## How to use functions: usecases

see [SOJS] ch 4

+ Recursion 
Recursion in named functions The pilfered reference problem The callee property 70
+ Fun with function as objects
Recursion with methods 65 Inline named functions 68
Storing functions 72 ■ Self-memoizing functions 73 Faking array methods 76
+ Checking for functions 86

## Using apply() to supply variable arguments


~~~ javascript
function smallest(array){
  return Math.min.apply(Math, array);
}

smallest([0, 1, 2, 3])
~~~

Also note that we specify the context as being the Math object. This isn’t necessary

## Function overloading
see [SOJS] ch 4.4.2

## Variable-length argument lists

# Event Loop

Event Loop: it's executed by the browser.
Browser event loop processing is single thread (events processed in FIFO order) but the mechanism that manage events before their handlers are executed are not on the same thread


# Window Object

http://www.w3schools.com/js/js_window.asp

The window object is supported by all browsers. It represent the browser's window.

All global JavaScript objects, functions, and variables automatically become members of the window object.
Global variables are properties of the window object.
Global functions are methods of the window object.
Even the document object (of the HTML DOM) is a property of the window object:

window.document.getElementById("header");
is the same as:
document.getElementById("header");

# Mixin

The Problem:
* Multi-tiered inheritance hierarchies are occasionally useful for describing the natural order of objects but if the primary motivation is function re-use they can quickly become gnarly labyrinths of meaningless subtypes, frustrating redundancies and unmanageable logic (“is a button a rectangle or is it a control? tell you what, lets make Button inherit from Rectangle, and Rectangle can inherit from Control…wait a minute….”).
* The most straightforward approach is **delegation**: any public function can be invoked directly via call or apply. However delegation is so convenient that sometimes it actually works against structural discipline in your code; moreover the syntax can get a little wordy.

Here there is a naive implementation:

~~~javascript
function extend(destination, source) {
  for (var k in source) {
    if (source.hasOwnProperty(k)) {
      destination[k] = source[k];
    }
  }
  return destination;
}
~~~~

…which we can call to extend our prototype…

~~~javascript
var RoundButton = function(radius, label) {
  this.radius = radius;
  this.label = label;
};

extend(RoundButton.prototype, circleFns);
extend(RoundButton.prototype, buttonFns);
//etc. ...
~~~

See [this post](http://javascriptweblog.wordpress.com/2011/05/31/a-fresh-look-at-javascript-mixins/) for more about different approach.

See the ember guide for the Ember.Mixin.


# ES6

* [Intro](http://www.wintellect.com/blogs/nstieglitz/5-great-features-in-es6-harmony)
* [ES6 Draft](http://wiki.ecmascript.org/doku.php?id=harmony:specification_drafts)
* [Easy Summary](http://www.frontendjournal.com/javascript-es6-learn-important-features-in-a-few-minutes/)

## ES6 Modules

Some reference about ES6 module:

* http://www.2ality.com/2013/07/es6-modules.html
* http://www.2ality.com/2014/09/es6-modules-final.html
* [Yeuda draft](https://gist.github.com/wycats/51c96e3adcdb3a68cbc3)
* http://eviltrout.com/2014/05/03/getting-started-with-es6.html

* A **module** is simply a file with JavaScript code in it.
* By default anything you declare in a file in a ES6 project is not available outside that file. You have to use the export keyword to explicitly make it available.
* A module can export multiple things by prefixing their declarations with the keyword **export** .

File structure:

~~~ bash
calculator/
  lib/
    calc.js
  main.js
~~~

Define a module:

~~~javascript
//------ lib.js ------
export const sqrt = Math.sqrt;
export function square(x) {
    return x * x;
}
export function diag(x, y) {
    return sqrt(square(x) + square(y));
}
~~~

Use a module:

~~~javascript
//------ main.js ------
import { square, diag } from 'lib';
console.log(square(11)); // 121
console.log(diag(4, 3)); // 5
~~~

you can also import the whole module and refer to its named exports via property notation:

~~~javascript
    //------ main.js ------
    import * as lib from 'lib';
    console.log(lib.square(11)); // 121
    console.log(lib.diag(4, 3)); // 5
~~~

### Traspiler
The great news is you can use ES6 modules today! You just have to run your code through a **transpiler**

[ES6 module transpiler](https://github.com/esnext/es6-module-transpiler)
is a JavaScript library for converting JavaScript files written using the ES6 draft specification module syntax to existing library-based module systems such as AMD, CommonJS, or simply globals.
This [post](http://esnext.github.io/es6-module-transpiler/) introduce how the traspiler works.

The subset of the ES6 module syntax supported by the transpiler is described [here](https://github.com/esnext/es6-module-transpiler#supported-es6-module-syntax)

