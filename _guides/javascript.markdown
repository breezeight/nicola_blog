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

* [SOJS](/Volumes/ArchiveDisk/Archive/Misc/ebook/javascript/Secrets_of_the_JavaS.pdf)    http://www.manning.com/resig/
* [FJS](/Volumes/ArchiveDisk/Archive/Misc/ebook/javascript/Functional_JavaScript.pdf)

# TODO
typeof -> how does it works?


# Basic Concepts

## Functions

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

# How to use functions: usecases

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
