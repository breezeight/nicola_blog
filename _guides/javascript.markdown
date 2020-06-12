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

Books to start programming from scretch with Javascript:

* [YDKJSY](https://github.com/getify/You-Dont-Know-JS) 
 *  It's not just for someone picking up the language for the first time (though it's for them, too); it's for all software craftspeople who want to master their tools, who want to understand the ins and outs of their trade, and who want to select the proper methods for solving problems.
* [EJS]Eloquent_JavaScript(https://eloquentjavascript.net/) 3rd edition 

Books:

* [YDKJSY](https://github.com/getify/You-Dont-Know-JS) 
* [EJS]Eloquent_JavaScript(https://eloquentjavascript.net/) 3rd edition
 * All code in this book may also be considered licensed under an MIT license.
 * [GITHUB](https://github.com/marijnh/Eloquent-JavaScript)
 * License "CC BY-NC 3.0"
* [SOJS](/Volumes/ArchiveDisk/Archive/Misc/ebook/javascript/Secrets_of_the_JavaS.pdf)    http://www.manning.com/resig/
* [FJS](/Volumes/ArchiveDisk/Archive/Misc/ebook/javascript/Functional_JavaScript.pdf)
* [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
    Mozilla Developer Network - Javascript
* [FLJS](https://github.com/getify/Functional-Light-JS) Functional-Light JavaScript
* [Codeacademy](http://www.codecademy.com/en/tracks/javascript)

Books By Dr. Axel Rauschmayer [Exploring JS: JavaScript books for programmers](http://exploringjs.com/):

* [JSFIP](http://exploringjs.com/impatient-js/index.html) JavaScript for impatient programmers (ES1–ES2018)
  * A full modern guide to the language, No required knowledge (apart from programming).
  * More compact than my other books, which go into more detail.
* [EES6](http://exploringjs.com/es6.html) "Exploring ES6", Covers what’s new in ES6 (relative to ES5)
* [EES20162017](http://exploringjs.com/es2016-es2017.html)  "Exploring ES2016 and ES2017", Covers what’s new in ES2016 and ES2017 (relative to ES6)
* [EES20182019](http://exploringjs.com/es2018-es2019/index.html)  "Exploring ES2018 and ES2019", Covers what’s new in ES2018 and ES2019 (relative to ES2017)

Blogs:

* http://perfectionkills.com/

Video Courses:

* Good introduction to NodeJS that go through a lot of JS basic concepts, GOOD for beginners: https://www.youtube.com/playlist?list=PLSn0N7ekG2FjiNp23kxOcjK8Xe0xRRO8a
* Advanced JavaScript By Kyle Simpson:
  * https://frontendmasters.com/courses/advanced-javascript/


MISC

* My Evernote about NodeJS: https://www.evernote.com/shard/s106/nl/2147483647/c61f9319-9f5c-4a91-b662-46bb5a8b644e/
* ES6 in Depth by Mozilla: https://hacks.mozilla.org/category/es6-in-depth/
* Full list of ES6 new features: http://es6-features.org

# Glossary

https://developer.mozilla.org/en-US/docs/Glossary

# TODO
typeof -> how does it works?

# Package Manager

## Package.json syntax and SEMVER

[Blog Post](https://bytearcher.com/articles/semver-explained-why-theres-a-caret-in-my-package-json/)

Semver uses three part version number like `3.9.2` and call these three numbers from left to right as:

* `major number`: 3  
* `minor number`: 9
* `patch number`: 2

The basic contract for the module maintainer making changes is

* backward incompatible change increments the major number
* new functionality that is backwards compatible increments the minor number
* simple bug fix to existing functionality increments the patch number

When executing npm install in a clean project directory, the version that satisfies package.json is installed for each dependency. Instead of specifying in package.json the exact version to be installed, npm allows you to widen the range of accepted versions. You can allow newer patch level version with tilde (~) and newer minor or patch level version with caret (^). The default when using --save is to use caret (^).


https://docs.npmjs.com/misc/semver

Tilde Ranges, Allows patch-level changes if a minor version is specified on the comparator. Allows minor-level changes if not.:

* Ex: `~1.2.3` means `>=1.2.3` and `<1.3.0`
* Ex: `~1.2`   means `>=1.2.0` and `<1.3.0`
* Ex: `~1`     means `>=1.0.0` and `<2.0.0`


Caret Ranges ( ex: ^1.2.3 ) Allows changes that do not modify the left-most *non-zero digit* in the [major, minor, patch]:

* Here `1` is the left-most non zero digit: `^1.2.3` means `>=1.2.3 and <2.0.0`
* Here `2` is the left-most non zero digit: `^0.2.3` means `>=0.2.3 and <0.3.0`
* Here `3` is the left-most non zero digit: `^0.0.3` means `>=0.0.3 and <0.0.4`

NOTE: caret is the standard behavior


## NPM

## NPX
An npm package runner — helps to execute packages without installing explicitly.

Is included since  npm@5.2.0

https://hackernoon.com/npx-npm-package-runner-7f6683e4304a

## YARN

List all installed package of a project :

* [https://yarnpkg.com/lang/en/docs/cli/list/](doc)
* all `yarn list --depth=0`
* all and their dependencies `yarn list`
* `yarn list --depth=0 --pattern react-native-localization`


Perform a vulnerability audit against the installed packages:

* [https://yarnpkg.com/en/docs/cli/audit](doc)
* `yarn audit`

# Standard Built-in objects

Ref: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects

## Null VS undefined

http://codechutney.in/blog/nodejs/javascript-null-vs-undefined/

# Expression, Statements and operators

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects

See the elequent JS pdf book for a nice introduction to the topic.

## Equality operator === vs ==

Always use === equals unless you have a good reason to use ==.

http://dorey.github.io/JavaScript-Equality-Table/?utm_content=buffer4f1b9&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer


http://stackoverflow.com/questions/359494/does-it-matter-which-equals-operator-vs-i-use-in-javascript-comparisons

# Control Flow

## Exception handling statements: throw, try...catch, finally

REF:

* https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#Exception_handling_statements
* https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch

You can throw exceptions using the `throw` statement and handle them using the `try...catch` statements.

Use the throw statement to throw an exception. When you throw an exception, you specify the expression containing the value to be thrown: `throw expression;`

Any object can be thrown in JavaScript.

```
throw 'Error2';   // String type
throw 42;         // Number type
throw true;       // Boolean type
throw {toString: function() { return "I'm an object!"; } };

// Create an object type UserException
function UserException(message) {
  this.message = message;
  this.name = 'UserException';
}

// Make the exception convert to a pretty string when used as a string
// (e.g. by the error console)
UserException.prototype.toString = function() {
  return this.name + ': "' + this.message + '"';
}

// Create an instance of the object type and throw it
throw new UserException('Value too high');
```

While it is fairly common to throw numbers or strings as errors it is frequently more effective to use one of the exception types specifically created for this purpose:

* [ECMAScript exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error#Error_types)
* DOMException and DOMError

The try statement consists of:

* a `try block`, which contains one or more statements. {} must always be used, even for single statements.
* At least one `catch clause`, or a `finally clause`.

This gives us three forms for the try statement:

* try...catch
* try...finally
* try...catch...finally

Flow:

* If any statement within the try block (or in a function called from within the try block) throws an exception, control immediately shifts to the catch block.
* If no exception is thrown in the try block, the catch block is skipped.
* The finally block executes after the try and catch blocks execute but before the statements following the try...catch statement.

### Catch

The catch block specifies an identifier (catchID in the preceding syntax) that holds the value specified by the throw statement:

```
try {
  throw 'myException'; // generates an exception and create the 'myException' string object
}
catch (e) {
  // statements to handle any exceptions
  console.log(e); // e is the 'myException' string object. It logs 'myException'
  console.log(typeof e); // string
}
```

### Finally

The finally block contains statements to execute:

* after the try and catch blocks execute
* but before the statements following the try...catch statement.

The finally block executes whether or not an exception is thrown. If an exception is thrown, the statements in the finally block execute even if no catch block handles the exception.

You can use the finally block to make your script fail gracefully when an exception occurs; for example, you may need to release a resource that your script has tied up. The following example opens a file and then executes statements that use the file (server-side JavaScript allows you to access files). If an exception is thrown while the file is open, the finally block closes the file before the script fails.

```
openMyFile();
try {
  writeMyFile(theData); //This may throw an error
} catch(e) {  
  handleError(e); // If we got an error we handle it
} finally {
  closeMyFile(); // always close the resource
}
If
```

If the finally block returns a value, this value becomes the return value of the entire try-catch-finally production, regardless of any return statements in the try and catch blocks:

```
function f() {
  try {
    console.log(0);
    throw 'bogus';
  } catch(e) {
    console.log(1);
    return true; // this return statement is suspended
                 // until finally block has completed
    console.log(2); // not reachable
  } finally {
    console.log(3);
    return false; // overwrites the previous "return"
    console.log(4); // not reachable
  }
  // "return false" is executed now  
  console.log(5); // not reachable
}
f(); // console 0, 1, 3; returns false
```

Overwriting of return values by the finally block also applies to exceptions thrown or re-thrown inside of the catch block:

```
function f() {
  try {
    throw 'bogus';
  } catch(e) {
    console.log('caught inner "bogus"');
    throw e; // this throw statement is suspended until
             // finally block has completed
  } finally {
    return false; // overwrites the previous "throw"
  }
  // "return false" is executed now
}

try {
  f();
} catch(e) {
  // this is never reached because the throw inside
  // the catch is overwritten
  // by the return in finally
  console.log('caught outer "bogus"');
}

// OUTPUT
// caught inner "bogus"
```

### Nesting try...catch statements

You can nest one or more try...catch statements. If an inner try...catch statement does not have a catch block, it needs to have a finally block and the enclosing try...catch statement's catch block is checked for a match. For more information, see nested try-blocks on the try...catch reference page.

# Functions

A function definition is a regular binding where the value of the binding is the function:

```
const power = function(base, exponent) {
  let result = 1;
  for(let count = 0; count < exponent; count++) {
    result *= base;
  };
  return result;
};
```

A function is created with an expression that begins with the keyword `function`.

A function have:

* zero o more parameters: they works like regular bindings, but the initial value is given by the caller of the function.
* a body

Functions, not objects are at the core of JavaScript. JS is a Functional language, functions are first-class objects:

* Functions can be arguments of other functions.
* All Functions have the **name** property, if it's anonymous name is an empty string.
* Functions can be referenced by variables `var canFly = function(){ return true; };`

Invoke:

* A Function can be invoked through a variable that reference the function `var canFly = function(){ return true; }; canFly() )`
* a `return` statement determines the value of the returned value and make cotrol jumping out to the caller.
* It there isn't a `return` statement, the value returned is implicitly `undefined`.

A function can be anonymous functions: `function(){return "test"}``

For more example about how to declare functions: see [SOJS] pag 40

Whatever we can do with objects, we can do with functions as well.

Functions are objects, just with an additional, special capability of **being invokable** : Functions can be called or invoked in order to perform an action.

## Closures

A closure is a special kind of object that combines two things:

* a function
* the environment in which that function was created.


~~~javascript
function makeAdder(x) {
  return function(y) { // is the inner function, a closure
    return x + y;      // x is the local variable
  };
}

var add5 = makeAdder(5);
var add10 = makeAdder(10);

console.log(add5(2));  // 7
console.log(add10(2)); // 12
~~~



This is an example of lexical scoping: in JavaScript, the scope of a variable is defined by its location within the source code (it is apparent lexically) and nested functions have access to variables declared in their outer scope.

See a more detailed explanation in the [MDN guide](https://developer.mozilla.org/en/docs/Web/JavaScript/Guide/Closures)

There is a critical difference between a C pointer to a function, and a
JavaScript reference to a function. In JavaScript, you can think of a
function reference variable as having both a pointer to a function as
well as a hidden pointer to a closure. In C, and most other common languages after a function returns, all the local variables are no longer accessible because the stack-frame is destroyed.

#### Closure Example

This example taken from SOJS is more advanced:

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

`open /devel/SRC/JAVASCRIPT/ninja-code/chapter-5/listing-5.3.html`

When we declared `innerFunction()` inside the outer function a closure was also created that encompasses not only the function declaration, but also all variables that are in scope at the point of the declaration.
This “bubble,” containing the function and its variables, stays around as long as the function itself does.

Function parameters are included in the closure of that function. (Seems obvi- ous, but now we’ve said it for sure.

* All variables in an outer scope, even those declared after the function declaration, are included.
* Within the same scope, variables not yet defined cannot be forward-referenced.

#### Closure Example: Common mistake in for loops

~~~html
<p id="help">Helpful notes will appear here</p>
<p>E-mail: <input type="text" id="email" name="email"></p>
<p>Name: <input type="text" id="name" name="name"></p>
<p>Age: <input type="text" id="age" name="age"></p>
~~~

~~~javascript
function showHelp(help) {
  document.getElementById('help').innerHTML = help;
}

function setupHelp() {
  var helpText = [
      {'id': 'email', 'help': 'Your e-mail address'},
      {'id': 'name', 'help': 'Your full name'},
      {'id': 'age', 'help': 'Your age (you must be over 16)'}
    ];

  for (var i = 0; i < helpText.length; i++) {
    var item = helpText[i];
    document.getElementById(item.id).onfocus = function() {
      showHelp(item.help);
    }
  }
}

setupHelp();
~~~

[View On JsFiddle](http://jsfiddle.net/v7gjv)

If you try this code out, you'll see that it doesn't work as expected. No matter what field you focus on, the message about your age will be displayed.

The reason for this is that the functions assigned to onfocus are closures; they consist of the function definition and the captured environment from the setupHelp function's scope. Three closures have been created, but each one shares the same single environment.

The `for` statement don't define a new scope, the `vat item` is defined
only once.

To fix the above example we need to define a new scope for each
interation in the for loop using a function factory:

~~~javascript
function showHelp(help) {
  document.getElementById('help').innerHTML = help;
}

function makeHelpCallback(help) {
  return function() {
    showHelp(help);
  };
}

function setupHelp() {
  var helpText = [
      {'id': 'email', 'help': 'Your e-mail address'},
      {'id': 'name', 'help': 'Your full name'},
      {'id': 'age', 'help': 'Your age (you must be over 16)'}
    ];

  for (var i = 0; i < helpText.length; i++) {
    var item = helpText[i];
    document.getElementById(item.id).onfocus = makeHelpCallback(item.help);
  }
}

setupHelp()
~~~

[View On JsFiddle](http://jsfiddle.net/v7gjv/1)

This works as expected. Rather than the callbacks all sharing a single environment, the makeHelpCallback function creates a new environment for each one in which help refers to the corresponding string from the helpText array.

This doesn't works, see comments to understand why:
~~~javascript
function showHelp(help) {
  document.getElementById('help').innerHTML = help;
}

function makeHelpCallback(help) { //This return undefined but executes
showHelp that change the
    showHelp(help);
}

function setupHelp() {
  var helpText = [
      {'id': 'email', 'help': 'Your e-mail address'},
      {'id': 'name', 'help': 'Your full name'},
      {'id': 'age', 'help': 'Your age (you must be over 16)'}
    ];

  for (var i = 0; i < helpText.length; i++) {
    var item = helpText[i];
    document.getElementById(item.id).onfocus = makeHelpCallback(item.help);
  }
}

setupHelp()
~~~

Also this doesn't work, WHY?

~~~javascript

function showHelp(help) {
  document.getElementById('help').innerHTML = help;
}

function setupHelp() {
  var helpText = [
      {'id': 'email', 'help': 'Your e-mail address'},
      {'id': 'name', 'help': 'Your full name'},
      {'id': 'age', 'help': 'Your age (you must be over 16)'}
    ];

  for (var i = 0; i < helpText.length; i++) {
    var item = helpText[i];
    document.getElementById(item.id).onfocus = function() {
      var help = item.help; //mi sa che questa non funziona perchè ho
      portato item nello scope.... infatti l unico modo per non portarsi
      dietro item è la soluzione proposta...
      showHelp(help);
    }
  }
}

setupHelp();
~~~


#### Closure Example: Private variable using closures

See [MDN Guide](https://developer.mozilla.org/en/docs/Web/JavaScript/Guide/Closures#Emulating_private_methods_with_closures)
See [SOJS_2nd] ch 5.2.1

* All assert are true, we can use the accessor method to obtain the value of the private variable, but that we cannot access it directly.
* The JavaScript scoping rules for this variable limit its accessibility to within the constructor.  

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

#### Keep state. Timers and callbacks using closures.

SOJS ch 5.2.2

In this chapter there are a nice example to avoid pollution of the global scope using closure.

SCENARIO: when a function is called at an unspecified later time and need to keep a state.

SOLUTION 1: object oriented

* you can keep the state in an object instance
* CONS: it's verbose. You have to write a lot of code just to
* PRO: each animation gets its own private “bubble” of variables, you can instantiate multiple animation.

SOLUTION 2: use closures

* PRO: less verbose. With a single function definition you get the same result.
* PRO: each animation gets its own private “bubble” of variables, you can instantiate multiple animation.
* NOTE: Without closures, doing multiple things at once, whether event handling, anima- tions, or even server requests, would be incredibly difficult. If you’ve been waiting for a reason to care about closures, this is it!
* in the below example `elem` and `tick` are kept by the closure `setInterval`:


```
<div id="box1">First Box</div>
<script>
  function animateIt(elementId) {
    var elem = document.getElementById(elementId);
    var tick = 0;
    var timer = setInterval(function(){
      if (tick < 100) {
        elem.style.left = elem.style.top = tick + "px";
        tick++;
      } else {
        clearInterval(timer);
        assert(tick === 100, "Tick accessed via a closure.");
        assert(elem, "Element also accessed via a closure.");
        assert(timer, "Timer reference also obtained via a closure." );
      }
    }, 10);
  }
  animateIt("box1");
</script>
```

SOLUTION: use global Variables

* CONS; If we keep the variables in the global scope, we need a set of three variables for each animation to run multiple animations.

#### Common Errors with events handlers and how to fix them: bind()

SOJS ch 5.3:

~~~javascript
  var button = {
    clicked: false,
    click: function(){
      this.clicked = true;
      assert(button.clicked,"The button has been clicked");
      //FAILS: the context of the click function is not referring to the button object as we intended.
    }
  };
  var elem = document.getElementById("test");
  elem.addEventListener("click",button.click,false);
~~~

the context of the click function is not referring to the button object as we intended.
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

### Functions Prototype

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

## Difference between identifier and variable (in JavaScript)

Ref: https://stackoverflow.com/questions/28185877/difference-between-identifier-and-variable-in-javascript#28185939

The difference between identifiers and variables is the same as that between names and people.

Names identify people. They can also identify dogs, for example. Names are not people, nor are people names. But you can say that I am Amadan (since saying that I am identified by the name Amadan sounds clunky).

Identifiers identify variables.  Identifiers are not variables, nor are variables identifiers.

```
var pippo = 2;
```

* `pippo` is the identifier
* `2` is the value of the variable
* the variable is a generic container that can contain different type of values (strings, arrays, etc), it's the memory location.

NOTE: since saying that is the variable containing the value `2` is identified by the identifier `pippo` sounds clunky, usually you say that that variable is `pippo`.


A good analogy for a variable would be locker boxes:

* **identifiers**: the number written on the box. A way to reference a variable in your source code.
* **value**: the contents of whatever you put inside.
* **variable**: the box. A variable is memory space identified by an identifier that can contain a value (whether a primitive value or a reference value) as its content.

A variable is not necessarily the memory location of a value, because a variable can contain a reference, and not an object itself (kind of like putting an address of a piece of real-estate into a locker, as opposed to trying to stuff a whole house into the box). So, in this stretched example, the house is the value; the locker is the variable; the "284" written on the locker is the identifier; and the piece of paper with "102 Nowhere Lane, Nowhereville" is a reference to the value, and also the contents of the variable. If the value is small and simple enough (in programming terms, a "primitive"), you can stuff the value itself into the variable, instead of the reference.

For instance:

```
var a = 1;         // assign a value
var b = [2, 3, 4]; // assign a reference
var aa = a;        // copy the contents
var bb = b;        // copy the contents
```

declares four variables (a, b, aa, bb), and four identifiers to name them (also a, b, aa and bb); it also mentions many values (1, 2, 3, 4, the array [2, 3, 4]). a and aa each contain a different copy of the primitive value 1. b contains the reference to the value [2, 3, 4] (not the value [2, 3, 4] itself!), which, in turn, contains the values 2, 3 and 4. bb contains another copy of... the reference! So if you change the value that is contained in b, the value in bb automagically changes too:

```
b.push(5);
console.log(b);
// => [2, 3, 4, 5]
console.log(bb);
// => [2, 3, 4, 5]
```

Functions are also values.

```
function hello(name) {
  console.log("Hello, " + name);
}
```

is (almost but not 100%) identical to

```
var hello = function(name) {
  console.log("Hello, " + name);
}
```

which defines a variable whose identifier is hello, and whose contents is a reference to a function. The function itself is a value.

## Execution Context and the Call Stack (or Execution Context Stack)

Ref:

* [SOJS_2nd] 5.3
* https://medium.com/@gaurav.pandvia/understanding-javascript-function-executions-tasks-event-loop-call-stack-more-part-1-5683dea1f5ec

In JavaScript, the fundamental unit of execution is a function.

Problem: When a function call another function, our program execution has to return to the position from which the function was called.

The JS runtime internally uses the the `execution context` and the `Call Stack` to achieve this:

* `execution context`: is a data structure which records the function calls executed for each code structure (function, code block, etc); basically where in the program we are (which statements and expression have been runned). There are only one global execution context and one execution context for each function execution.
* Every time a function is invoked the JS engine pauses the current execution context and create a new one, which is pushed on the `Call Stack`.
* `Call Stack`: is a data structure which records the of current and stopped Execution context
* each time a function return its Execution Context is *popped out* from the stack and *discarded*.
* Video animation : https://youtu.be/8aGhZQkoFbQ?t=270
* NOTE: in [SOJS_2nd] the Call Stack is called `Execution Context Stack`

This is because JavaScript is based on a **single-threaded execution model**:

* Only one piece of code can be executed at a time.
* Every time a function is invoked, the current execution context has to be stopped, and a new function execution context, in which the function code will be evaluated, has to be created.
* See [SOJS_2nd] Figure 5.6

TODO : Blocking: https://youtu.be/8aGhZQkoFbQ?t=439

## Binding Scope

Each binding has a scope. A scope is the part the part of the program in which the binding is visible.

In JS **scope are declared by functions not blocks** In the example x is still in scope after the end of the block because the function scope is not changed:

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


## Lexical Context (or Scope)

Ref:

* See [SOJS_2nd] 5.4
* Mozilla: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures

`Lexical environment` or `scope` is an internal JavaScript engine construct used to keep track of the mapping from identifiers to specific variables. It's an internal implementation of the JavaScript scoping mechanism.

`Indentifier resolution`: is the process of figuring out which variable a certain identifier refers to.

For example, consider the following code:

```
  var ninja = "Hattori";
  console.log(ninja);
```

The lexical environment is consulted when the ninja variable is accessed in the console.log statement.

Usually, a lexical environment is associated with a specific structure of JavaScript code. It can be associated with:

* a function,
* a block of code,
* or the catch part of a try-catch statement.

Each of these structures (functions, blocks, and catch parts) can have its own separate identifier mappings. Each of these code structures gets an associated lexical environment **every time** the **code is evaluated**.

Each `execution context` has a `lexical environment` associated with it, that contains the mapping for all identifiers defined directly in that context.

NOTE In pre-ES6 versions of JavaScript, a lexical environment could be associated with only a function. Variables could be only function scoped. This caused a lot of confusion. Because JavaScript is a C-like language, people coming from other C-like languages (such as C++, C#, or Java) naturally expected some low-level concepts, such as the existence of block scopes, to be the same. With ES6, this is finally fixed.

**Scope Nesting**:

* in Javascript you can access variables defined in outer code structures.
* JS supports closure

Both behaviours are supported by JS engines using a linked list of `lexical environment`: each lexical environment has to keep track of its outer (parent) lexical envi- ronment.

If an identifier can’t be found in the current environment, the outer environment is searched. This stops either when:

* the matching variable is found,
* or with a reference error if we’ve reached the global environment and there’s no sign of the searched-for identifier.

Ref: See [SOJS_2nd] figure 5.9

In order to support the closure, how is the outer lexical environment set when we call a function?

* JavaScript does this by taking advantage of functions as first-class objects. Whenever a function is created, a reference to the lexical environment in which the function was created is stored in an internal (meaning that you can’t access or manip- ulate it directly) property named [[Environment]]; double brackets is the notation that we’ll use to mark these internal properties.

Whenever a function is called:

* a new function execution context is created and pushed onto the execution context stack.
* a new associated lexical environment is created.
* Now comes the **crucial part**: For the outer environment of the newly created lexical environment, the JavaScript engine puts the environment referenced by the called function’s internal [[Environment]] property, the environment in which the now-called function was created!


NOTE: This might seem odd at first. Why don’t we just traverse the whole stack of execution contexts and search their matching environments for iden- tifier mappings? Technically, this would work in our example. But remember, a JavaScript function can be passed around as any other object, so the posi- tion of the function definition and the position from where the function is called generally aren’t related (remember closures).


## Lexical scoping: Explaining Value vs. Reference in Javascript

ref:

* https://codeburst.io/explaining-value-vs-reference-in-javascript-647a975e12a0

Javascript has 5 data types that are `passed by value`, we’ll call these primitive types:

* Boolean,
* null,
* undefined,
* String,
* Number

Javascript has 3 data types that are passed by reference: Array, Function, and Object. These are all technically Objects, so we’ll refer to them collectively as Objects.

Esempi stronzi:


```
x=1
xx=x // the identifier
console.log(`x=${x} xx=${xx}`)
x=2 // the identifier x now refer a different variable but xx still reference the old variable
console.log(`x=${x} xx=${xx}`)
```


```
x=1
function report() {
  console.log(x)
}
report();
x=2
report();
```

```
x=1
function report() {
  xx=x
  console.log(`x=${x} xx=${xx}`)
}
report();
x=2
report();
```

Let:

```
let x=1
function report() {
  let xx=x
  console.log(`x=${x} xx=${xx}`)
}
report();
x=2
report();
```


```
x = {
  'first_name': 'Mario',
  'last_name': 'Rossi'
}
xx = x // the identifier
console.log(`x=${util.inspect(x)} xx=${util.inspect(xx)}`)
x = 2 // the identifier x now refer a different variable but xx still reference the old variable
console.log(`x=${util.inspect(x)} xx=${util.inspect(xx)}`)
```

```
x = {
  'first_name': 'Mario',
  'last_name': 'Rossi'
}

function report() {
  xx=x
  console.log(`x=${util.inspect(x)} xx=${util.inspect(xx)}`)
}
report();
x=2
report();
```


```
var hundred = 100;
var two = 2;
function change(x, y) {
    x = 1000
    y = 10000;
}
```

## Understanding types of JavaScript variables (let, var, const)

Ref: see [SOJS_2nd] ch 5.5

In JavaScript, we can use three keywords for defining variables:

* `var`
  * been part of JavaScript since its beginning
* `let`
  * ES6 additions
* `const`
  * ES6 additions
  * we have to provide an initialization value when it’s declared and we can’t assign a completely new value to it afterward.
  * We can’t assign a completely new object, but there’s nothing stopping us from modifying the one we already have (ex: add item to an array).

They differ in two aspects:

* mutability
* their relationship toward the lexical environment.

### Variable definition keywords: mutability

Usecase: const primitive type

* `const` is expecially usefull for all the type that in JS can be assigned only by value (string, Boolean, number, etc)
* ex: `const MAX_BUFFER_SIZE = 256` will guarantee that `MAX_BUFFER_SIZE` cannot be changed. We are safeguarded our code against unwanted or accidental modifications.

Usecase: const object

*  we can’t assign a completely new value to a const variable. But there’s nothing stopping us from modifying the current one

```
const secondConst = {};
secondConst.weapon = "wakizashi";
assert(secondConst.weapon === "wakizashi", "We can add new properties");
```

### Variable definition keywords: lexical environments

var on one side, and let and const on the other.

`var`: the variable is defined in the closest function or global lexical environment (Note that blocks are ignored!).

```
var globalNinja = "Yoshi";
function reportActivity(){
  var functionActivity = "jumping";
  for(var i = 1; i < 3; i++) {
      var forMessage = globalNinja + " " + functionActivity;
      assert(forMessage === "Yoshi jumping",
             "Yoshi is jumping within the for block");
      assert(i, "Current loop counter:" + i);
  assert(i === 3 && forMessage === "Yoshi jumping",
        "Loop variables accessible outside of the loop");
  }
}
reportActivity();
assert(typeof functionActivity === "undefined"
    && typeof i === "undefined" && typeof forMessage === "undefined",
    "We cannot see function variables outside of a function");

```


* DIFFERENT FROM CPP and JAVA: we can access the variables defined with the `for` code blocks even outside those blocks
* None of the function variables are accessible outside of the function.


`let` and `const`: They define variables in the closest lexical environment (which can be a block environment, a loop environ- ment, a function environment, or even the global environment).

```
const GLOBAL_NINJA = "Yoshi";
function reportActivity(){
  const functionActivity = "jumping";
  for(let i = 1; i < 3; i++) {
      let forMessage = GLOBAL_NINJA + " " + functionActivity;
      assert(forMessage === "Yoshi jumping",
               "Yoshi is jumping within the for block");
        assert(i, "Current loop counter:" + i);
  }
  assert(typeof i === "undefined" && typeof forMessage === "undefined", "Loop variables not accessible outside the loop");
  }
  reportActivity();
  assert(typeof functionActivity === "undefined"
      && typeof i === "undefined" && typeof forMessage === "undefined",
      "We cannot see function variables outside of a function");
```

## HOW JS Engine register identifiers in a lexical environment: functions and variables Hoisting


REF:
* [SOJS_2nd] 5.5.3
* Mozilla MDN: https://developer.mozilla.org/en-US/docs/Glossary/Hoisting
* https://john-dugan.com/hoisting-in-javascript/

Hoisting is a term you will not find used in any normative specification prose prior to ECMAScript® 2015 Language Specification.

Hoisting was thought up as a general way of thinking about how execution contexts (specifically the creation and execution phases) work in JavaScript. However, the concept can be a little confusing at first.

Conceptually, for example, a strict definition of hoisting suggests that variable and function declarations are physically moved to the top of your code, but this is not in fact what happens. Instead, the variable and function declarations are put into memory during the compile phase, but stay exactly where you typed them in your code.

One of the advantages of JavaScript putting function declarations into memory before it executes any code segment is that it allows you to use a function before you declare it in your code. For example:

```
catName("Chloe");

function catName(name) {
  console.log("My cat's name is " + name);
}
/*
The result of the code above is: "My cat's name is Chloe"
*/
```

Even though we call the function in our code first, before the function is written, the code still works. This is because of how context execution works in JavaScript.

Hoisting works well with other data types and variables:

* The variables can be initialized and used before they are declared.
* But **only declarations** are hoisted, not initializations.

If we never declare a variable we get an error:

```
console.log(num); // ERROR: ReferenceError: num is not defined
```

JavaScript only hoists declarations, not initializations. If a variable is declared and initialized after using it, the value will be undefined. For example, if we declare `num` after we use it but before we inizialize it, it's `undefined`:

```
console.log(num); // Returns undefined
var num;
num = 6;
console.log(num); // Returns 6
```

### Is JS a compile or interpreted language?

Ref: Kyle Simpson https://frontendmasters.com/courses/advanced-javascript/

To understand Lexical Environment in JS you must understand that JS is a compiled language. Most of us think that JAVA or CPP are compiled languages because we use compilers to ship our application as bytecode or machine readable Executables, but it not the right way to classify a compiled language.

With JS we distribute our source code so a lot of people tend to say it is interpreted language but it's not. All JS engine will compile your source code before running it, every single time you execute it.

What is an interpreted language?  Let's look at Bash scripting: when the bash interpreter is running line 3, it has NO IDEA of what to expect at line 4.
Instead a compiled language read the whole source code before running it! This is the main point!


### Simplified overview of how a JS Engine parse and execute code

Ref:

 * https://john-dugan.com/hoisting-in-javascript/
 * [SOJS_2nd] 5.5.3

To understand how Lexical Environment works we need to

* know how the step "finding decorations of variables and functions" of the compilation process is managed.
* know how the JS engine registrers identifiers

Decorations are: `var`, `let`, `function`, etc

`var foo = "bar";` is a single JS statement but is treated by the engine as two different operations that happens at different time:

* the decoration operation `var foo`
* the initialization operation `foo = "bar";`

It's really important to look at our code knowing this concept to understand `hoisting`.


Every JavaScript engine process your code in two phases: `Compilation Phase` and `Execution Phase`. Modern engines will compile your code using advanced techniques like JIT but for educational porpouse of understanding hoisting we will keep thing simple.

In the course, Kyle explains the compilation and execution phases of JavaScript in a psuedocode-esque conversation. Below is a code snippet along with a recap of the conversations that take place during the compilaton and execution phases.

```
var foo = "bar"; //line 1

function bar() { //line 3
    var foo = "baz"; //line 4

    function baz(foo) { //line 6
	    foo = "bam"; //line 7
	    bam = "yay"; //line 8
    }
    baz(); //line 10
}

bar(); //line 13
foo; 		// "bar"
bam; 		// "yay"
baz(); 		// Error!
```

JavaScript Compilation, The first step taken by the browser’s JavaScript engine:

* Line 1: Hey global scope, I have a declaration for a variable named foo.
* Line 3: Hey global scope, I have a declaration for a function1 named bar.
  * NOTE: Since bar is a function, we recursively decent into its scope and continue compilation.
* Line 4: Hey bar scope, I have a declaration for a variable named foo.
* Line 6: Hey bar scope, I have a declaration for a function named baz.
* Line 6: Hey baz scope, I have a declaration for a parameter named foo.

JavaScript Execution, The second step take by the browser’s JavaScript engine.

There are two terms that you need to be familiar with as we enter the execution phase: LHS and RHS. LHS stands for left hand side, and RHS stands for right hand side. LHS references are located on the left hand side of the = assignment operator. RHS references are located on the right hand size of the of the = assignment operator, or implied when there is no LHS reference. If this seams a bit confusing, a good way to think about LHS versus RHS is target versus source. LHS is the target, and RHS is the source.

* Line 1: Hey global scope, I have an LHS reference for a variable named foo. Ever heard of it?
  * The global scope has because foo was registered on line 1 in the compilation phase, so the assignment occurs.
  * NOTE: Lines 3–11 don’t exist in the execution phase because they were compiled away. So, we move to line 13.

* Line 13: Hey global scope, I have an RHS2 reference for a variable named bar. Ever heard of it?
  * The global scope has because bar was registered as a function on line 3 in the compilation phase, so the function executes.
  * NOTE: The reason line 13 is an RHS is because there is no assignment. As such, we cannot establish a left/right reference. Therefore, we know that the value on line 13 represents the source.

* Line 4: Hey bar scope, I have an LHS reference for a variable named foo. Ever heard of it?
  * The bar scope has because foo was registered on line 1 in the compilation phase, so the the assignment occurs.
  * Within the bar scope, foo will always refer to the value assigned to it on line 4. This is because the foo variable on line 4 is preceded with the var keyword, and will therefore be the first reference to foo inside the bar scope.
  * NOTE: Lines 6–9 don’t exist in the execution phase because they were compiled away. So, we move to line 10.

* Line 10: Hey bar scope, I have an RHS reference for a variable named baz. Ever heard of it?
  * The bar scope has because baz was registered as a function on line 6 in the compilation phase, so the function executes.

* Line 7: Hey baz scope, I have an LHS reference for a variable named foo. Ever heard of it?
  * The baz scope has because foo was declared as a parameter of the baz function on line 6 in the compilation phase, so the assignment occurs.

* Line 8: Hey baz scope, I have an LHS reference for a variable named bam. Ever heard of it?
  * The baz scope has not. Therefore we look for bam in the next outer scope, the bar scope.
* Line 8: Hey bar scope, I have an LHS reference for a variable named bam. Ever heard of it?
  * The bar scope has not. Therefore we look for bam in the next outer scope, the global scope.
* Line 8: Hey global scope, I have an LHS reference for a variable named bam. Ever heard of it?
  * The global scope has not. Therefore the global scope automatically registers a variable named bam.
  * NOTE: If you are in strict mode, the bam variable will not be registered. Therefore, because bam doesn’t exist a reference error will be thrown.

* Line 14: Hey global scope, I have an RHS reference for a variable named foo. Ever heard of it?
  * The global scope has because foo was declared on line 1 in the compilation phase, its value is the string “bar”.

* Line 15: Hey global scope, I have an RHS reference for a variable named bam. Ever heard of it?
  * The global scope has because bar was automatically created two steps back, its value is the string “yay”.
  * NOTE if you are in strict mode, a reference error will be thrown because bam doesn’t exist.

* Line 16: Hey global scope, I have an RHS reference for a variable named baz. Ever heard of it?
  * The global scope has not because baz was exists in the function scope of bar. Therefore, baz is inaccessible to the global scope and a reference error is thrown.

During the `Compilation Phase`, the engine will search for `decorations of variables and functions`:

The behavior depends on type of code (global code, function code, or block code), for each of type:

  * code is parsed but isn’t executed.
  * new lexical environment is created.
  * JS engine visits and registers all declared variables and functions within the current lexical environment. The exact behavior depends on the type of variable (let, var, const, function declaration) and the type of environment (global, function, or block). The process of `registering variables` is as follows:

step 1 create `arguments identifier`:

* If we’re creating a `function lexical environment`: the implicit `arguments` identifier is created, along with all formal function parameters and their argument values.
* If we’re dealing with a nonfunction environment, this step is skipped.

step 2, scan for `function declarations` (without going into the body of other functions):

* If we’re creating a `global or a function environment`:
  * scan for function declarations (but not function expressions or arrow functions!).
  * For each discovered function declaration, a new function is created and bound to an identifier in the environment with the function’s name.
  * If that identifier name already exists, its value is overwritten.
  * NOTE: this explain how hoi
* If we’re dealing with `block environments`: this step is skipped.

step 3, scan for `variable declarations`:

* In `function or global environments`:
  * all variables declared with the keyword `var` and defined outside other functions (but they can be placed within blocks!) are found,
  * and all variables declared with the keywords `let` and `const` defined outside other functions and blocks are found.
* In `block environments`:
  * the code is scanned only for variables declared with the keywords `let` and `const`, directly in the current block.
* For each discovered variable:
  * if the identifier doesn’t exist in the environment, the identifier is registered and its value initialized to `undefined`.
  * if the identifier exists, it’s left with its value.


* second phase:
  * starts after this has been accomplished
  * all the expressions and statement are evaluated in order.



### Problem of overriding function identifiers

If you look at the code below we declare the `fun` function below the `var fun = 3` number. We could suppose that at the end the `fun` identifier is bound to the function. But If you run this code, you’ll see that both asserts pass.

This behavior follows as a direct consequence of the steps taken when registering identifiers:

* in the first phase
  * functions defined with function declarations are created and associated to their identifiers before any code is evaluated: `fun` is bound to a function
  * then the `var fun` variable is discoved but it's already bound, therefore left untouched

* in the second phase:
  * `var fun = 3;` is executed and `function fun(){}` is skipped beacouse already processed.

```
// fun refers to a function.
assert(typeof fun === "function", "We access the function");

// Defines a variable fun and assigns a number to it
var fun = 3;

// fun refers to a number.
assert(typeof fun === "number", "Now we access the number");      

// A fun function declaration
function fun(){}

// fun still refers to a number !!!!
assert(typeof fun === "number", "Still a number");


```




## How to use functions: usecases

see [SOJS] ch 4

+ Recursion
Recursion in named functions The pilfered reference problem The callee property 70
+ Fun with function as objects
Recursion with methods 65 Inline named functions 68
Storing functions 72 ■ Self-memoizing functions 73 Faking array methods 76
+ Checking for functions 86


## Arguments and function parameters

see [SOJS] ch 3.4

* A parameter is a variable that we list as part of a function definition.
* An argument is a value that we pass to the function when we invoke it.

When a list of arguments is supplied as a part of a function invocation, these argu- ments are assigned to the parameters in the function definition in the order specified. The first argument gets assigned to the first parameter, the second argument to the second parameter, and so on.

* If **more arguments than parameters** : the “excess” arguments aren’t assigned to parameter names:
* if **more parameters than arguments** : the parameters that have no corresponding argument are set to `undefined`.

```
function practice (ninja, weapon, technique) { ... }

# "katana" is not assigned
practice ("Yoshi", "sword", "shadow sword", "katana");
# "Yoshi" is assigned to ninja, weapon and technique are assigned to undefined
practice ("Yoshi");
```

## Rest Parameters: Variable-length argument lists

NOTE: available since ES6 standard


* Only the last function parameter can be a rest parameter.
* By prefixing the last-named argument of a function with an ellipsis `...`, we turn it into an array called the rest parameters, which contains the remaining passed-in arguments.

```
function multiMax(first, ...remainingNumbers){
  # remainingNumbers is an array
}
```

## Default Parameters

NOTE: available since ES6 standard

Scenario:

* a function with a parameter that has **almost** always the same
* JS don't have function overloading, so default params are a possible solution.


Before ES6:

* we checks whether the value of the action parameter is undefined (by using the typeof operator), and if it is, the func- tion sets the value of the action variable to skulking.
* If the action parameter is sent through a function call (it’s not undefined), we keep the value.

```
function performAction(ninja, action){
     action = typeof action === "undefined" ? "skulking" : action;
     return ninja + " " + action;
  }
```

with ES6 this job is made by the language:

```
function performAction(ninja, action = "skulking"){
   return ninja + " " + action;
}
```

We can assign any values to default parameters: simple, primitive values such as numbers or strings, but also complex types such as objects, arrays, and even functions.

We can reference previous parameters:

```
function performAction(ninja, action = "skulking", message = ninja + " " + action) {
  return message;
}
```

## Implicit parameters: arguments

see [SOJS_2nd] ch 4.1.1

Function invocations are usually passed two implicit parameters:

`arguments`:

* a collection of all arguments passed to a function;
* NOTE: with rest parameters, introduced in the preceding chapter, the need for the arguments parameter has been greatly reduced
* (has a `length` property).
* Is not an Array but array notation can be used `arguments[2]`.

`this`:

* the function context
* represent different things, depends on the invocation type

By implicit, we mean that these parameters aren’t explicitly listed in the function signature, but are silently passed to the function and accessible within the function. They can be referenced within the function just like any other explicitly named parameter.

Parametes alias:

* Arguments object is an alias for the function parameters, if we change the arguments object, the change is also reflected in the matching function parameter.
* with `use strict` this behavior is disabled.

## Implicit parameters: "this" is the "function context"

**JAVA, CPP Developer WARNING** :

* In such languages, this usually points to an instance of the class within which the method is defined. The `this` is
* But beware! in JavaScript this is true only when invoking a function as a method **it's not the only one way**  a function can be invoked.

in JS `this`:

* Represent the function context
* Depends by HOW the function is **INVOKED**

We can invoke a function in four ways:

* As a **function**: `skulk()`, in which the function is invoked in a straightforward manner
* As a **method**: `ninja.skulk()`, which ties the invocation to an object, enabling object-oriented programming
* As a **constructor**: `new Ninja()`, in which a new object is brought into being
* Via the function’s **apply or call methods**: skulk.call(ninja)or skulk.apply(ninja) Here are examples:

```
function skulk(name) {}
function Ninja(name) {}

/// Invoked as a function  
skulk('Hattori');
(function(who){ return who; })('Hattori');

/// Invoked as a method of ninja
var ninja = {
  skulk: function(){}
};

/// Invoked via the call method
ninja.skulk('Hattori');

/// Invoked as a constructor
ninja = new Ninja('Hattori');

/// Invoked via the apply or call method
skulk.call(ninja, 'Hattori');
skulk.apply(ninja, ['Hattori']);
```

For all but the call and apply approaches, the function invocation operator is a set of parentheses following any expression that evaluates to a function reference.


### This: invoke as a function

We say that a function is invoked “as a function” to distinguish it from the other invocation mechanisms: methods, constructors, and apply/call.

This type of invocation occurs when:

* a function is invoked using the () operator,
* and the expression to which the () operator is applied doesn’t reference the function as a property of an object. (In that case, we’d have a method invocation, but we discuss that next.)

Strict VS NON Strict mode:

* nonstrict mode: `this` will be the global context (the window object)
* strict mode: `this` will be `undefined`.

### This: invoke as method

see [SOJS] ch 4.2.2

NOTE: this example is simple, the best way to create an object is using the `constructor`

The function is invoked as a method of that object:

* When a function is assigned to a property of an object
* when the invocation occurs by referencing the function using that property
* When we invoke a function as a method of an object, that object becomes `this`, the function context.

Here’s an example:

```
var ninja = {};
ninja.skulk = function(){};
ninja.skulk();
```

The function is called `method` in this case.

The differences between function and method invocations:

```
function whatsMyContext() {
  return this;
}
assert(whatsMyContext() === window,
  "Function call on window");
var getMyThis = whatsMyContext;
assert(getMyThis() === window,
  "Another function call in window");
var ninja1 = {
  getMyThis: whatsMyContext
};
assert(ninja1.getMyThis() === ninja1,
  "Working with 1st ninja");
var ninja2 = {
  getMyThis: whatsMyContext
};
assert(ninja2.getMyThis() === ninja2,
  "Working with 2nd ninja");
```

### This: invoke functions as a construct

A constructor is a function like any other functions.


NOTE: do not to confuse these `function constructors` with `constructor functions`:

* A function constructor enables us to create functions from dynamically created strings.
* Constructor functions, the topic of this section, are functions that we use to create and initialize object instances

### This: Invoke function with call() and apply()

REF: see [SOJS_2nd] paragraph 4.2.4


Scenario: set "this" explicitly

Usecases:

* browser event handlers
* implement a "foreach", implement a callback system

`apply()`: To invoke a function using its `apply()` method we pass two parameters to apply()

* the object to be used as the function context(this),
* an array of values to be used as the invocation arguments.

The `call()` method is used in a similar manner, except that the arguments are passed directly in the argument list rather than as an array.

Syntax example:

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
￼￼￼￼￼￼￼  assert(ninja1.result === 10,"juggled via apply");
  assert(ninja2.result === 26,"juggled via call");
</script>
~~~

#### Usecase: Build a toy version of "forEach"

See REF: see [SOJS_2nd] paragraph 4.2.4 for more details

Scenario: in imperative programming the iteration on a collection is based on index that is incremented. In functional programming we want set the function context (`this`) of a callback to the item of the the collection.

imperative Styles

```
function(collection) {
  for (var n = 0; n < collection.length; n++) {
    /* do something to collection[n] */
  }
}
```

Functional style:

* Our iteration function accepts the collection to be iterated over and a callback function.
* Using `call()` the callback is invoked such that the current is the function context.
* The assert test that the function context is correct for each invocation of the callback


```
function forEach(list, callback) {
  for (var n = 0; n < list.length; n++) {
    callback.call(list[n], n);
  }
}
var weapons = [ { type: 'shuriken' },
                { type: 'katana' },
                { type:'nunchucks' }];

forEach(weapons, function(index){
  assert(this === weapons[index], "Got the expected value of " + weapons[index].type);
});
```

## Using apply() to supply variable arguments

~~~ javascript
function smallest(array){
  return Math.min.apply(Math, array);
}

smallest([0, 1, 2, 3])
~~~

Also note that we specify the context as being the Math object. This isn’t necessary

## Arrow Functions

See REF: see [SOJS_2nd] paragraph 4.3.1 for more details

* IMPORTANT: Arrow functions don’t have their own this value. Instead, they remember the value of the this parameter at the time of their definition.
* more concise way of creating functions

## This: using the bind method

See REF: see [SOJS_2nd] paragraph 4.3.2 for more details

* Every function has access to the `bind(function_context)` method
* `bind()` return a new function has the same body, but its context is always bound .
* For the new returned function, the value of the `this` parameter is always set to the object referenced by the `bind()` argument, regardless of the way the function was invoked. (similar to the arrow function).

see below "Usecase: callback for browser Events" for an example

## Usecase: callback for browser Events

```
<button id="test">Click Me!</button>
        <script>
          function Button(){
            this.clicked = false;
            this.click = function(){
              this.clicked = true;
              assert(button.clicked, "The button has been clicked");
            };
          }
          var button = new Button();
          var elem = document.getElementById("test");
          elem.addEventListener("click", button.click);
</script>
```

Problem: `assert(button.clicked, "The button has been clicked");` will fail because the function context of `button.click` will be `Window` or `undefined`

See REF: see [SOJS_2nd] paragraph 4.2.4 for more details

solutions:

* Call or Apply
* bind()
* Arrow functions

### Arrow function solution

* When the click arrow function is defined the function context is the `button` object create with `new Button()`.
* When the event handler callback `button.click` is invoked `this` will be assigned to `button`.

```
<button id="test">Click Me!</button>
<script>
  function Button(){
     this.clicked = false;
     this.click = () => {
       this.clicked = true;   //NOTE: here we use "this"
       assert(button.clicked,"The button has been clicked"); // here we assert on the button object
      };
  }
  var button = new Button();
  var elem = document.getElementById("test");
  elem.addEventListener("click", button.click);
</script>
```

WARNING: it's easy to make mistake see [SOJS_2nd] listing 4.14


### Bind solutions

This example uses the bind function to create a new function **bound to the button object**, when it's invoked `this` will remain the bouded object 

```
<button id="test">Click Me!</button>
<script>
  var button = {
    clicked: false,
    click: function(){
      this.clicked = true;
       assert(button.clicked,"The button has been clicked");
    }
  };
  var elem = document.getElementById("test");
  elem.addEventListener("click", button.click.bind(button));
  var boundFunction = button.click.bind(button);
  assert(boundFunction != button.click, "Calling bind creates a completly new function");
</script>
```


## Design Pattern: Immediately-Invoked Function Expression (IIFE)

Ref: http://benalman.com/news/2010/11/immediately-invoked-function-expression/

in JavaScript, parens can’t contain statements.

## Symbols

Ref: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol

The Symbol() function creates a new symbol of type `symbol`. Symbol is a primitive value (new in ECMAScript 2015).
(It's a kind of factory)

Syntax: `Symbol([description])`

To create a new primitive symbol, you write Symbol() with an optional string as its description:

```
var sym1 = Symbol();
var sym2 = Symbol('foo');
var sym3 = Symbol('foo');
```

The above code creates three new symbols. Note that Symbol("foo") does not coerce the string "foo" into a symbol.
Each symbol is unique, distinct from all others (even others that have the same description):

```
Symbol('foo') === Symbol('foo'); // false
```

The following syntax with the new operator will throw a TypeError: `var sym = new Symbol(); // TypeError`

In JS, identifiers and most property keys are still considered strings. Symbols are just an extra option.

### Use Symbols as Object Properties: Symbol-Keyed properties

```
// create a unique symbol
var isMoving = Symbol("isMoving");
var element = {};

// Symbol-Keyed properties can be used only with the [] notation. NOTE that the
element[isMoving] = true

// string based properties can be acces
element['foo']="bar"
element.foo="baz"

```

A few notes about this code:

* The string `"isMoving"` in `Symbol("isMoving")` is called a `description`. It’s helpful for debugging. It’s shown when you write the symbol to console.log(), when you convert it to a string using .toString(), and possibly in error messages. That’s all.

* element[isMoving] is called a **symbol-keyed property** . It’s simply a property whose name is a symbol rather than a string. Apart from that, it is in every way a normal property.

* symbol-keyed properties can’t be accessed using dot syntax, as in `obj.name`. They must be accessed using square brackets.

* It’s trivial to access a symbol-keyed property if you’ve already got the symbol. The above example shows how to get and set element[isMoving], and we could also ask if (isMoving in element) or even delete element[isMoving] if we needed to.

On the other hand, all of that is only possible as long as isMoving is in scope. This makes symbols a mechanism for weak encapsulation: a module that creates a few symbols for itself can use them on whatever objects it wants to, without fear of colliding with properties created by other code.

### Well-known symbols

JavaScript has a set of Symbols already allocated, used to access standard object's properties. They represent internal language behaviors and they can be accessed using the Symbol's properties.

For example : Iteration symbols

* `Symbol.iterator` : A method returning the default iterator for an object. Used by `for...of`.
* `Symbol.asyncIterator` : A method that returns the default AsyncIterator for an object. Used by for `await...of`.

A full references of this Symbols: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol#Well-known_symbols

### Global symbol registry: Shared symbols

Ref: https://developer.mozilla.org/en-US/docs/Glossary/Symbol#Global_symbol_registry

* `Symbol.for("tokenString")` returns a symbol value from the registry,
* `Symbol.keyFor(symbolValue)` returns a token string from the registry;

Each is the other's inverse, so the following is true: `Symbol.keyFor(Symbol.for("tokenString")) == "tokenString"; // true`


### List Symbols of an Object

`Reflect.ownKeys()`

`Object.getOwnPropertySymbols()`:

* https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertySymbols

### Symbol usescases

Ref:

* https://hacks.mozilla.org/2015/06/es6-in-depth-symbols/
* https://stackoverflow.com/questions/21724326/what-is-the-motivation-for-bringing-symbols-to-es6

Symbols are values that programs can create and use as property keys without risking name collisions.

Just like a string or number, you can use a symbol as a property key. Because it’s not equal to any string, this symbol-keyed property is guaranteed not to collide with any other property.

NOTE: The description of the Symbol doesn't affect the uniqueness

For example if we have two animation framework that want to set a property on a dom element.

```
// create a unique symbol
var isMovingFirstLib = Symbol("isMoving");

var isMovingSecondLib = Symbol("isMoving");

var myFakeDomElement = {}

function animateFirstLib(element) {
  element[isMovingFirstLib] = true
}

function animateSecondLib(element) {
  element[isMovingSecondLib] = true
}

animateFirstLib(myFakeDomElement)
animateSecondLib(myFakeDomElement)

Reflect.ownKeys(myFakeDomElement) // Two unique property are set: [ Symbol(isMoving), Symbol(isMoving) ]

```


# Is JavaScript a pass-by-reference or pass-by-value language?

ref: https://stackoverflow.com/questions/6605640/javascript-by-reference-vs-by-value

* Javascript is always pass by value, but when a variable refers to an object (including arrays), the "value" is a reference to the object.
* Changing the value of a variable never changes the underlying primitive or object, it just points the variable to a new primitive or object.
* However, changing a property of an object referenced by a variable does change the underlying object.


Example:

```
function changeStuff(a, b, c)
{
  a = a * 10;
  b.item = "changed";
  c = {item: "changed"};
}

var num = 10;
var obj1 = {item: "unchanged"};
var obj2 = {item: "unchanged"};

changeStuff(num, obj1, obj2);

// num is passed by value and will not change
console.log(num);
// the changeStuff worked on the referenced properties, obj1 is changed
console.log(obj1.item);
// the changeStuff worked on the reference, obj2 is NOT changed
console.log(obj2.item);
```

# Prototypal Inheritance and Function Constructors

Ref: https://youtu.be/CGEa8WmmQwQ?t=1953

Is a simple mechanism to make code run as soon as it is loaded.

```
(function(){ /* code */ }()); // Crockford recommends this one
(function(){ /* code */ })(); // But this one works just as well
```

In JavaScript, parens can’t contain statements.


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
* The most straightforward approach is **delegation**: any public function can be invoked directly via `call` or `apply`. However delegation is so convenient that sometimes it actually works against structural discipline in your code; moreover the syntax can get a little wordy.

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
~~~

which we can call to extend our prototype…

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

# Browser Events




# Browser Debugger TIPS

* `alert("my message")`

## DOM breakpoint

* `on subtree modification`

## Event listeners

If you use the ispector there is a tab that list all listeners.

## MAPS

TODO: dovrebbe essere possibile fare delle mappe per non avere dei mega file CSS e JS



# JQuery

REFs:

* https://jquery.com/
* [JQuery Learning Center](http://learn.jquery.com/)

## How to select elements

* [Intro](https://learn.jquery.com/using-jquery-core/selecting-elements/)
* [Selector reference](http://api.jquery.com/category/selectors/)

The most basic concept of jQuery is to "select some elements and do something with them." jQuery supports most CSS3 selectors, as well as some non-standard selectors.

When a selection is made using `$()`, an object is always returned

To check if a selection contains elements:

* https://learn.jquery.com/using-jquery-core/selecting-elements/#does-my-selection-contain-any-elements
* `if ( $( "div.foo" ).length )`

# JavaScript modules, loaders and bundlers.

Ref:

* https://nolanlawson.com/2015/10/19/the-struggles-of-publishing-a-javascript-library/
* Long overview Oct 28, 2018: https://medium.com/@ajmeyghani/javascript-bundlers-a-comparison-e63f01f2a364
* Eloquent_JavaScript.pdf ch 10
* june 2016:

## Intro: Modules, Module Loaders, Modules Bundlers


Why do we Modules?

* to create reusable code
* to provide a clear public **interface** to it
* to state the dependency between reusable code (which other modules need to be present to be able to use a given module and to automatically load dependencies).



https://medium.com/@ajmeyghani/javascript-bundlers-a-comparison-e63f01f2a364


Modules: what are they and what are the different module definitions for JavaScript.
Module loaders: what are loaders and how can they be used.
Bundlers: what are JavaScript bundlers, what is the process for setting up each, and how do they compare against each other.

**Module loaders** are used to load JavaScript modules at runtime, usually for development. Most notable loaders are:

* RequireJS
* SystemJS

**Module bundlers** are used to bundle several modules into one or more optimized bundles for the browser. Most notable bundlers are:

* Webpack,
* Rollup,
* Google Closure Compiler.


The Google Closure Compiler (Closure) is a code analyzer and optimizer that can also be used to create bundles. Closure is probably the most mature analyzer and optimizer out there. If you want to analyze your code and output the most optimized code possible, Closure will be your best friend. Rollup has a great Closure plugin that I’m going to cover later.

Most of the bundlers these days have very similar features. The one feature that varies among them is tree shaking for CJS or ES modules. Out of all the bundlers, Webpack has the most consistent built-in support for ES and CJS module tree shaking. Rollup and Parcel do have tree shaking but Webpack’s is just a little better overall. Parcel however is working on making tree shaking available for both CJS and ES modules. Until tree shaking matures among bundlers it’s best to carefully examine what you are importing to minimize the final bundle size.
Overall all bundlers are pretty fast if you are careful about what you are importing. In the worst case in can take up to 7 seconds to bundle a very simple project.

Zero-config or not, you’ll have to spend some time experimenting with each bundler to learn them well. If a bundler is labelled as zero-config that does not mean that you don’t have to configure anything for production. It’s mostly true for development, but for production you have to create configuration files regardless. I think a better term would have been “bundlers for development”, rather than “bundlers with zero configuration”.



* Tree Shaking:

** ref: https://webpack.js.org/guides/tree-shaking/
** Tree shaking is a term commonly used in the JavaScript context for **dead-code elimination**. It relies on the static structure of ES2015 module syntax, i.e. import and export. The name and concept have been popularized by the ES2015 module bundler rollup.


## History: Pre 2015

Until 2015, the JavaScript language had no built-in module system.

When JavaScript was first introduced it had a very basic system for loading “modules”. It involved including a script tag in an html file and the location of the JavaScript file. This mechanism wasn’t good, even for small projects because:

Everything was loaded in the global context leading to name collisions and overrides
It involved a lot of manual work by the developer to figure out the dependencies and the order of inclusion
These types of problems were exasperated as the client-side (browser) applications grew bigger and bigger and more complex. In order to solve the module problem two module definitions were introduced by the community around 2009. These module definitions were the CommonJS (CJS) and the Asynchronous Module Definition (AMD).

You can use JavaScript functions to create local scopes and objects to represent module interfaces.

```
const weekDay = function() {
const names = ["Sunday", "Monday", "Tuesday", "Wednesday",
"Thursday", "Friday", "Saturday"];
   return {
     name(number) { return names[number]; },
     number(name) { return names.indexOf(name); }
}; }();
console.log(weekDay.name(weekDay.number("Sunday"))); // → Sunday
```

Its interface consists of weekDay.name and weekDay .number, and it hides its local binding names inside the scope of a function expression that is immediately invoked.

This style of modules provides isolation, to a certain degree, but it does not declare dependencies. Instead, it just puts its interface into the global scope and expects its dependencies, if any, to do the same.

Just putting your JavaScript code into different files does not satisfy these requirements. The files still share the same global namespace.

**For a long time this was the main approach used in web programming, but it is mostly obsolete now.**

## History: CommonJS, AMD-RequireJS, UMD

TODO: Mi sembra di capire che sia obsoleto ma no so se nel 2019 sia necessario capirci qualcosa

Two prominent module definitions were developed as part of the community effort: `CJS (CommonJS)` and `AMD (Asynchronous Module Definition)`.

`CJS`:

* was defined as a **synchronous** definition intended for **server-side JavaScript**.
* Node’s module system is practically based on CJS with some minor differences.

`AMD`:

* was defined an **asynchronous** model intended for modules in the browser
* `RequireJS` is the most popular implementation of AMD.


You may have also heard of the term `UMD` thrown around a lot. UMD stands for Universal Module Definition. It’s essentially a piece of JavaScript code placed at the top of libraries that enables any loader to load them regardless of the environment they are in.

A standard module system was finally introduced in 2015 as part of the ES2015 (ES6) specification. It defined the semantics for importing and exporting modules asynchronously.

CommonJS modules work quite well and, in combination with NPM, have allowed the JavaScript community to start sharing code on a large scale. But now is obsolete.

Ref:

* Eloquent_JavaScript.pdf ch 10


## ES6 Modules - Ecmascript 2015

* [Intro](http://www.wintellect.com/blogs/nstieglitz/5-great-features-in-es6-harmony)
* [ES6 Draft](http://wiki.ecmascript.org/doku.php?id=harmony:specification_drafts)
* [Easy Summary](http://www.frontendjournal.com/javascript-es6-learn-important-features-in-a-few-minutes/)

## ES6 Modules

JavaScript standard from 2015 introduces its own, different module system. It is usually called ES modules, where ES stands for ECMAScript.

JavaScript standard from 2015 introduces its own, differ- ent module system. It is usually called ES modules, where ES stands for ECMAScript.

Why use ES6 modules?

* it's the first time we've had modules that are actually part of the language.
* Now that the standard has been formalised, we can look forward to a future in which browsers (and node.js, eventually) natively support ES6 modules. So code written in ES6 modules is future-proof.

### Syntax

Some reference about ES6 module:

* http://www.2ality.com/2013/07/es6-modules.html
* http://www.2ality.com/2014/09/es6-modules-final.html
* [Yeuda draft](https://gist.github.com/wycats/51c96e3adcdb3a68cbc3)
* http://eviltrout.com/2014/05/03/getting-started-with-es6.html

* A **module** is simply a file with JavaScript code in it.
* By default anything you declare in a file in a ES6 project is not available outside that file. You have to use the export keyword to explicitly make it available.
* A module can export multiple things by prefixing their declarations with the keyword **export** .
* An ES module’s interface is not a single value but a set of named bindings.

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

#### ES6 Module transpiler

* [ES6 Module Traspiler](https://github.com/esnext/es6-module-transpiler)
* [NPM node package](https://www.npmjs.com/package/es6-module-transpiler): npm install -g es6-module-transpiler

* [Broccoli Plugin](https://github.com/mmun/broccoli-es6-module-transpiler)

Supported syntax : https://github.com/esnext/es6-module-transpiler#supported-es6-module-syntax

How use it?

* rsvp

#### ES6Modules

* https://github.com/ember-cli/broccoli-es6modules

ES6Modules wraps the esperanto library. All options described for esperanto can be provided here.

#### Esperanto

Refs:

* [Homepage](http://esperantojs.org/)
* [Github Homepage](https://github.com/esperantojs/esperanto)

Esperanto is a tool for converting ES6 modules to AMD, CommonJS or UMD. It's built for speed, interoperability and ease of use.


How use it?

* Ember.js

## Node Modules System

Ref:

* [Intro doc](https://github.com/maxogden/art-of-node/#modular-development-workflow)
* [Official doc](https://nodejs.org/api/modules.html)
* [Module Intenals] https://medium.com/better-programming/node-js-modules-basics-to-advanced-2464001229b6


TODO:

* Does NodeJS support es6 modules in 2019? https://medium.com/the-node-js-collection/an-update-on-es6-modules-in-node-js-42c958b890c
* `export`
* `require`
* `require.resolve`

In Node, the modularity is a first-class concept. In the Node.js module system, each file is treated as a separate module.

So, if you are creating, let’s say, a demo.js file, this implies you are creating a module in Node. Basically modules help us encapsulating our code into manageable chunks.
Anything that we define in our module (i.e. in our JavaScript file) remains limited to that module only, unless we want to expose it to other parts of our code.

So, anything we define inside our module remains private to that module only.

The NodeJS module system is derived from CommonJS.

One of the useful tools Node.js adds on top of standard ECMAScript is a notation for defining and using modules.

`require()` is a function for loading code from other files, it returns the exports of the module name that you specify.

```
var uniq = require('uniq');
var nums = [ 5, 2, 1, 3, 2, 5, 4, 2, 0, 1 ];
console.log(uniq(nums));
```

Note that `require()` returned a function and we assigned that return value to a variable called uniq. We could have picked any other name and it would have worked the same. `require()` returns the exports of the module name that you specify.

TODO:

* `export`
* `require`
* `require.resolve`

A "module" exports objects and functions by adding them to exports, and another module can import it by using require. The semantics are explained well in the official documentation.

`module.exports` is the object that's actually returned as the result of a `require` call.


To test out which module actually gets loaded by node, you can use the `require.resolve('some_module')` command

In the next paragraphs we will see how modularity was implement before NodeJS and then how NodeJS implemented modularity.

### How Modularity Worked Before ES5 and NodeJS
Ref: https://medium.com/better-programming/node-js-modules-basics-to-advanced-2464001229b6

Prior to modules in Node.js or ES5 modules, the modularity in JavaScript was achieved using IIFE (Immediately Invoked Function Expression), which is, as the name suggests, a function which is invoked immediately after it is defined.

```
(function () {
  const sum = (a, b) => {
    return a + b;
  };
  const result = sum(2, 3)
  console.log(result)
})()

sum(5, 8) // ReferenceError: sum not defined
```

Now, if we run this code, we will get the output as 5.
The function sum is defined inside this IIFE and if any code outside that IIFE tries to access the sum function, it will result in ReferenceError: sum is not defined, i.e. the sum function is private to this particular IIFE.
So, how do we access this sum function outside of this IIFE?

```
const exportObj = {};
(function () {
  const sum = (a, b) => {
    return a + b;
  };
  const result1 = sum(2, 3)
  console.log(result1) //5
  exportObj.sum = sum;
})()
const result2 = exportObj.sum(5, 8)
console.log(result2) // 13
```

To expose our sum function outside IIFE, we create an object (exportObj) outside IIFE, then, through closure, we access that object inside our IIFE and assign our sum function to one of its property.
After that, we call the sum function on the exportObj object outside the IIFE. This time, we are able to get result without any errors.

### How Modularity Works in Node.js

We have seen above that, to achieve modularity prior to Node and ES5, we used functions.
In Node.js, this wrapping function that wraps our code is not written by us but is automatically added by Node for us.

Let’s look at an example to understand it better. Let’s say we defined one file, named sum.js, with the following content:

```
const sum = (a, b) => {
  return a + b;
};

const result = sum(2, 3)
console.log(result)
```
https://gist.github.com/udittyagi/e4b49683361c49fbff2fb3c5e62f93e7#file-sum-js

So, in Node.js, this code is wrapped and looks something like this in our running environment:

```
(function (exports, require, module, __filename, __dirname) {
  // Module code actually lives in here
  const sum = (a, b) => {
    return a + b;
  };

  const result = sum(2, 3)
  console.log(result)
});
```
https://gist.github.com/udittyagi/aa3c99a05504a210fa44249ac1477dad#file-summodule-js


Everything is wrapped as we wrapped in our IIFE but, here, this wrapper function gets some arguments. We will discuss them in detail later.

To check whether your code is wrapped in a function and whether we are receiving these arguments, or not. In JavaScript, we know that all functions receive an argument called arguments, so, if we get arguments in our code, it confirms that our code is inside a function: `console.log('Arguments given by node', arguments)`

Example HERE: https://github.com/breezeight/javascript_nicola_courses/blob/master/node-modules-under-the-hood/README.md

We can see that we get the output of arguments (arguments is an array-like object, whose keys are numeric, which is passed to every function by default). So, it confirms that our code is wrapped inside a function and that function receives five arguments, which are given by Node.js.
Let’s discuss these five arguments one-by-one.


#### Exports

This is an object used to expose our functionalities in one module, so these functionalities can be used in other modules.

We can expose anything, this can be a function, variable, constants, classes, etc. As we have done above in the How modularity worked before section, we have created a property on exportObj and then assigned a value to it.

The same way we do it with exports object — we create a property on the exports object and then assign a value, or whatever you want to expose (variable, function, classes, constants), to that property.

```
const sum = (a, b) => {
  return a + b;
};
const multiply = (a, b) => {
  return a * b
};
exports.multiply = multiply;
```

Here, we expose the multiply function by assigning the function reference to a newly created multiply property on the exports object, i.e. multiply function is only available outside this module, not the sum function.
Note: Do not provide a new reference to this exports object, i.e. don’t assign a new object to the exports argument. (We will discuss why not to do this.)


#### Require

This is a function that we use to import or require the functionalities from other modules. It is a compliment to the exports object, which is used to export functionalities. require, on the other hand, is used to import those functionalities.

To require a module, we call the require function with either the path of the module (absolute or relative), which starts with /, ./, or ../ in the case of local modules, or the name of the module in the case of core modules and third-party modules.
Then, it returns the exported content of the module that we require.

Note: Basically, we get the reference of the object module.exports (we will discuss this) when we require a module.

```
const os = require('os'); //node's core module
const express = require('express') // third party module
const operations = require('./operations.js'); //local module

//Do something with these modules
const result1 = operations.multiply(2, 4);
console.log('Multiply Result: ', result1)// 8

const result2 = operations.sum(2, 3);// Error, as it is not exported.
console.log('Sum Result: ', result2)
```

We implemented two functions, sum and multiply, but we have exported only multiply, so only that one is available outside of the operations.js module. That is why we will get an error if we try to call sum.
Node’s require function has a lot more to offer than just importing the functionalities, we will dive deeper into this.

#### Module

This is the third argument passed, the module variable is a reference to the object representing the current module. It has various useful properties which we can see in the terminal with `console.log(module)` in any module.

The module object contains all the data regarding our module, such as:

* “Who is its parent? Who are its children?
* What are all the paths it took to resolve third-party modules? 
* Is it completely loaded, or not?”

But the most important property of the module object is the exports property, we can also use this exports property on the module to export our data, rather than using exports arguments of the wrapper function.

```
const sum = (a, b) => {
  return a + b;
};
const multiply = (a, b) => {
  return a * b
};

module.exports = {
  sum,
  multiply
}
```

So, this is the second way of exporting functionalities out of our module.
Note: We will see the difference between exports and module.exports, and how they are connected to each other.

Summary of the module object

* module.filename is the fully resolved filename of the module.
* module.id is the identifier for the module. Typically, this is the fully resolved filename, except for the main module, it is ‘.’ (period), see pic 3. Main module is the module that spins up your Node application, e.g if we write node app.js in the terminal, then app.js is the main module.
* module.path is the directory name of your name module.
* module.parent is an object which refers to the parent module.
* module.children is an array of all the children module objects.
* module.loaded is a boolean property which tells us whether or not the module is done loading, or is in the process of loading.
* module.paths is an array of all the paths that Node will look up to resolve a module.

TODO: rileggere la question di delle [CIRCULAR] reference qua https://medium.com/better-programming/node-js-modules-basics-to-advanced-2464001229b6

Some of you might have noticed in pic 2 and pic 3, this weird [Circular] thing in module parent or children property. So, what is that?
Actually, [Circular] defines a circular reference, as in pic 2, which prints out the module object of operations.js. The parent property of the operations.js module references the app.js module.
Similarly, operations.js is a child module of app.js, so its children property should have a reference to the operations.js module. And, similarly, the operations.js module parent property again refers to the app.js module, so it will go into this infinite loop.
To prevent this infinite loop, Node sees that, if any module’s parent or child is already loaded, it will not load them again and show this [Circular] instead.

#### filename
This is a variable that contains the absolute path of the current module.
Given two modules: a and b, where b is a dependency of a and there is a directory structure of:
/User/home/node_blog/a.js
/User/home/node_blog/node_modules/b/b.js
So, if we do console.log(__filename)within b.js, we will get /User/home/node_blog/node_modules/b/b.js. If we do console.log(__filename) within a.js, we will get /User/home/node_blog/a.js.

#### dirname

The directory name of the current module. This is the same as the path.dirname() of the __filename.
So, for the above modules, a.js and b.js.
If we do console.log(__dirname) within b.js, we will get /User/home/node_blog/node_modules/b/ and in a.js, we will get /User/home/node_blog/.
Now we have studied the basics of the module. From now on, we will dive deep into this topic. Bear with me a bit longer as there are various interesting things we are going to discuss

#### Difference Between module.exports and exports

We use both `module.exports` and `exports` to export our functionalities out of our module.
But, there is a slight difference between them. Rather, I’ll say that they are not different but they are similar. The `exports` object is just shorthand for `module.exports`.
Inside Node, the exports object refers to the module.exports object. Which is somewhat like: `const exports = module.exports;`

VERY IMPORTANT: when we require in a module, `module.exports` object is returned by the require function.

And that is the reason we don’t change the reference of the exports object, because, if we change the exports object, that will no longer refer to the module.exports, resulting in the functionalities not being exported from our module.

Can we use both module.exports and exports in a single module?
Yes, we can, but there are some subtleties we should keep in mind if we are using both.
Those are, when we use require in any module, we get the module.exports object and the exports object referring to module.exports, so it is necessary to maintain this reference.

In the code below, the sum will not be exported as we have changed the reference of module.exports by assigning a new object to it but the exports object now also refers to the previous reference of module.exports.

https://github.com/breezeight/javascript_nicola_courses/blob/master/node-modules-under-the-hood/operations_gotcha.js

Test it: 

* git clone git@github.com:breezeight/javascript_nicola_courses.git
* cd javascript_nicola_courses
* node node-modules-under-the-hood/app_export_gotcha.js

#### Modules in Detail

It is not necessary that only a file can be a module that we require. Other than files, we also have folders as modules that we can require in.

Generally, a folder as a module is a module of modules, i.e. it contains various modules inside it to achieve functionality. This is what libraries do, they are organized in a self-contained directory and then they provide a single entry point to that directory.

There are two ways in which we can require a folder.

* Create a package.json in the root of the folder, which specifies a main module. An example package.json file might look like this:

```
{ "name" : "some-library",
  "main" : "./lib/some-library.js" }
```

If this was in a folder at ./some-library, then require('./some-library') would attempt to load ./some-library/lib/some-library.js.

This is the extent of Node.js awareness of package.json.

*  If Node does not find any package.json in the root directory of the module, or in package.json if the main entry is missing or cannot be resolved. Then, Node.js will try to load index.js or index.node from that directory. For example, if there was no package.json file in the above example, then require('./some-library') would attempt to load:
  * ./some-library/index.js
  * ./some-library/index.node

If these attempts fail, then Node.js will report the entire module as missing with the default error: `Error: Cannot find module ‘some-library’.`

In file modules, .js file is also not the only module, we have .json files and .node files, they are also modules in Node.

#### Requiring in Detail

When we require a module it is not necessary to give the file extension. For example, if there is a `some-file.js` file that we want to require and it is on the same level, we can require it as: `const someFile = require(‘./some-file’);`
That is without specifying the extension.
While resolving the path of this file, Node follows a procedure.
It first looks for some-file.js, if some-file.js is not present, it will look for some-file.json and if that is also not present, it will look for some-file.node.
.js files are interpreted as JavaScript text files, and .json files are parsed as JSON text files, i.e. we get the JavaScript object. .node files are interpreted as compiled add-on modules.

### How require looks for files

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


### What is an export?

A "module" exports objects and functions by adding them to exports, and another module can import it by using require. The semantics are explained well in the official documentation.

`module.exports` is the object that's actually returned as the result of a `require` call.

To test out which module actually gets loaded by node, you can use the `require.resolve('some_module')` command

### Node.js: Require VS import

* `require` is defined by the node module system
* `import` ???? the rsvp npm package use it.... but other package no (ex: https://github.com/strongloop/express)   WHY??? WHAT is the DIFFERENCE?

may be reading this will answer: https://appdividend.com/2019/01/23/javascript-import-statement-tutorial-with-example/


https://medium.com/@geekguy/javascript-modues-exports-vs-exports-whats-the-difference-9a61cdb99386

### HOWTO write a module

https://github.com/maxogden/art-of-node/#how-to-write-a-module

* By default node tries to load module/index.js when you require('module'), any other file name won't work unless you set the main field of package.json to point to it.

### Require package

https://www.npmjs.com/package/resolve


### Internals

* http://eli.thegreenplace.net/2013/05/27/how-require-loads-modules-in-node-js
* https://github.com/joyent/node/blob/master/lib/module.js#L380
* What is the purpose of Node.js module.exports and how do you use it? http://stackoverflow.com/questions/5311334/what-is-the-purpose-of-node-js-module-exports-and-how-do-you-use-it


# Browserify

WARNING: capire se è ancora in uso nel 2019

http://browserify.org/#install

Browserify is a tool for compiling node-flavored commonjs modules for the browser:

* Sharing code between Node.js and the browser
* The module system that browserify uses is the same as node, so packages published to npm that were originally intended for use in node but not browsers will work just fine in the browser too.
* people are publishing modules to npm which are intentionally designed to work in both node and in the browser using browserify and many packages on npm are intended for use in just the browser. npm is for all javascript, front or backend alike.


* Getting started: https://github.com/browserify/browserify-handbook

* https://blog.codecentric.de/en/2014/02/cross-platform-javascript/
* introduction to Browserify and Grunt.js and how to leverage Browserify to write code that runs on Node.js and in the browser.

 Node, of course, provides a require method in its environment that serves to synchronously load dependencies. The client side, however, is an entirely different beast. There is no require available natively in browsers, so Browserify implements it for us and gives us access to it by passing it into these closures.

# Babel

https://babeljs.io/docs/en/

## What is Babel?

Babel is a toolchain that is mainly used to convert ECMAScript 2015+ code into a backwards compatible version of JavaScript in current and older browsers or environments.

Here are the main things Babel can do for you:

* Transform syntax
* Polyfill features that are missing in your target environment (through @babel/polyfill)
* Source code transformations (codemods)
* And more! (check out these videos for inspiration)

