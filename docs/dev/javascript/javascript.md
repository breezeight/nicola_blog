---
layout: post
title: "Javascript"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["javascript"]
---



# References:

Refresh and reference:
- [Learn X in Y minutes - Javascript](https://learnxinyminutes.com/docs/javascript/)

Books to start programming from scretch with Javascript:

- [YDKJSY](https://github.com/getify/You-Dont-Know-JS)
    - It's not just for someone picking up the language for the first time (though it's for them, too); it's for all software craftspeople who want to master their tools, who want to understand the ins and outs of their trade, and who want to select the proper methods for solving problems.
- [EJS - Eloquent_JavaScript](https://eloquentjavascript.net/) 3rd edition

Books:

- [YDKJSY - You Don't Know JS Yet](https://github.com/getify/You-Dont-Know-JS)
- [EJS - Eloquent_JavaScript](https://eloquentjavascript.net/) 3rd edition
    - All code in this book may also be considered licensed under an MIT license.
    - [GITHUB](https://github.com/marijnh/Eloquent-JavaScript)
    - License "CC BY-NC 3.0"
- SOTJSN2nd - Secrets of a Javascript Ninja [ebook](/Volumes/ArchiveDisk/Archive/Misc/ebook/javascript/Secrets_of_the_JavaS.pdf), [website](http://www.manning.com/resig/)
- [FJS - Functional_JavaScript](/Volumes/ArchiveDisk/Archive/Misc/ebook/javascript/Functional_JavaScript.pdf)
- [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
  Mozilla Developer Network - Javascript
- [FLJS](https://github.com/getify/Functional-Light-JS) Functional-Light JavaScript
- [Codeacademy](http://www.codecademy.com/en/tracks/javascript)

Books By Dr. Axel Rauschmayer [Exploring JS: JavaScript books for programmers](http://exploringjs.com/):

- [JSFIP](http://exploringjs.com/impatient-js/index.html) JavaScript for impatient programmers (ES1–ES2020)
  - A full modern guide to the language, No required knowledge (apart from programming).
  - More compact than my other books, which go into more detail.
  - [JSFIP ES2020 Update](https://exploringjs.com/impatient-js/ch_about-book.html#new-in-es2020-edition): Operators, undefined, “Typed Arrays: handling binary data (Advanced)”, Modules, Single Objects, Promise combinators: working with Arrays of Promises”,
- [EES6](http://exploringjs.com/es6.html) "Exploring ES6", Covers what’s new in ES6 (relative to ES5)
- [EES20162017](http://exploringjs.com/es2016-es2017.html) "Exploring ES2016 and ES2017", Covers what’s new in ES2016 and ES2017 (relative to ES6)
- [EES20182019](http://exploringjs.com/es2018-es2019/index.html) "Exploring ES2018 and ES2019", Covers what’s new in ES2018 and ES2019 (relative to ES2017)

Blogs:

- http://perfectionkills.com/

Video Courses:

- Good introduction to NodeJS that go through a lot of JS basic concepts, GOOD for beginners: https://www.youtube.com/playlist?list=PLSn0N7ekG2FjiNp23kxOcjK8Xe0xRRO8a
- Advanced JavaScript By Kyle Simpson:
  - https://frontendmasters.com/courses/advanced-javascript/

MISC

- My Evernote about NodeJS: https://www.evernote.com/shard/s106/nl/2147483647/c61f9319-9f5c-4a91-b662-46bb5a8b644e/
- ES6 in Depth by Mozilla: https://hacks.mozilla.org/category/es6-in-depth/
- Full list of ES6 new features: http://es6-features.org

- Nicola Testing "4.1 - TDD Jest" https://docs.google.com/presentation/d/1VO5His3lxFu_MP3zLlrh9M-R6T7VlqYw7upvAug7qHg/edit#slide=id.p

# Glossary

https://developer.mozilla.org/en-US/docs/Glossary

# TODO

typeof -> how does it works?

# Style Guides

Airbnb JavaScript Style Guide: https://github.com/airbnb/javascript
JS Standard Style Guide: https://github.com/standard/standard


* camelCase when naming objects, functions, and instances (and relative files)
* PascalCase only when naming constructors or classes (and relative files)
* Acronyms and initialisms should always be all uppercased, or all lowercased. (SMSContainer)


# VSCode

## VSCode Debugger

- https://strongloop.com/strongblog/interactive-debugging-with-node-js/
- [VSCode NodeJS Debugger Doc](https://code.visualstudio.com/docs/nodejs/nodejs-debugging)

Call Stack Pane:

- function calls that got you to the current position in the code when execution is paused, and enables you to step back up that stack and examine the application state in earlier “frames.” By clicking the frame below the current frame you can jump to the code that called the current function.
- `Skipped by skipfiles` are files that usally not usefull to be shown in the stack

```js
"debug.javascript.terminalOptions": {
  "skipFiles": [
    "<node_internals>/**"
  ]
},
```

## VSCode Extensions: best practices
Moved here: https://docs.google.com/document/d/1X4HrockI5tyBTgq20ITz_ZGXExy9EZry3CRfmD2g8vw/edit#


# Package Manager

## Package.json syntax and SEMVER

[Blog Post](https://bytearcher.com/articles/semver-explained-why-theres-a-caret-in-my-package-json/)

Semver uses three part version number like `3.9.2` and call these three numbers from left to right as:

- `major number`: 3
- `minor number`: 9
- `patch number`: 2

The basic contract for the module maintainer making changes is

- backward incompatible change increments the major number
- new functionality that is backwards compatible increments the minor number
- simple bug fix to existing functionality increments the patch number

When executing npm install in a clean project directory, the version that satisfies package.json is installed for each dependency. Instead of specifying in package.json the exact version to be installed, npm allows you to widen the range of accepted versions. You can allow newer patch level version with tilde (~) and newer minor or patch level version with caret (^). The default when using --save is to use caret (^).

https://docs.npmjs.com/misc/semver

Tilde Ranges, Allows patch-level changes if a minor version is specified on the comparator. Allows minor-level changes if not.:

- Ex: `~1.2.3` means `>=1.2.3` and `<1.3.0`
- Ex: `~1.2` means `>=1.2.0` and `<1.3.0`
- Ex: `~1` means `>=1.0.0` and `<2.0.0`

Caret Ranges ( ex: ^1.2.3 ) Allows changes that do not modify the left-most _non-zero digit_ in the [major, minor, patch]:

- Here `1` is the left-most non zero digit: `^1.2.3` means `>=1.2.3 and <2.0.0`
- Here `2` is the left-most non zero digit: `^0.2.3` means `>=0.2.3 and <0.3.0`
- Here `3` is the left-most non zero digit: `^0.0.3` means `>=0.0.3 and <0.0.4`

NOTE: caret is the standard behavior

## NPM

[CheatSheet](https://devhints.io/npm)

- -E, --save-exact: Saved dependencies will be configured with an exact version rather than using npm’s default semver range operator.

## NPX

An npm package runner — helps to execute packages without installing explicitly.

Is included since npm@5.2.0

https://hackernoon.com/npx-npm-package-runner-7f6683e4304a

## YARN

List all installed package of a project :

- [doc](https://yarnpkg.com/lang/en/docs/cli/list/)
- all `yarn list --depth=0`
- all and their dependencies `yarn list`
- `yarn list --depth=0 --pattern react-native-localization`

Perform a vulnerability audit against the installed packages:

- [https://yarnpkg.com/en/docs/cli/audit](https://yarnpkg.com/en/docs/cli/audit)
- `yarn audit`

# Standard Built-in objects

Ref: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects

## Null VS undefined

- https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/get-started/ch2.md#values
- http://codechutney.in/blog/nodejs/javascript-null-vs-undefined/

TL;DR: better to use only undefined

In addition to strings, numbers, and booleans, two other primitive values in JS programs are `null` and `undefined`. While there are differences between them (some historic and some contemporary), for the most part both values serve the purpose of indicating emptiness (or absence) of a value.

Many developers prefer to treat them both consistently in this fashion, which is to say that the values are assumed to be indistinguishable. If care is taken, this is often possible. However, it's safest and best to use only undefined as the single empty value, even though null seems attractive in that it's shorter to type!

```js
while (value != undefined) {
  console.log("Still got something!");
}
```

# Expression, Statements and operators

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects

See the elequent JS pdf book for a nice introduction to the topic.

REF: [Statements and declarations by category](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements)

## Explaining Value vs. Reference in Javascript

TODO: prendersi le parti interessanti di questo post:
https://codeburst.io/explaining-value-vs-reference-in-javascript-647a975e12a0
fanno vedere visivamente come la memoria si comporta a seconda del tipo di oggetto JS si utilizza.

## Equality operator === vs ==

Always use `===` equals unless you have a good reason to use `==`.

Fatto molto bene: https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/get-started/ch2.md#comparisons

http://dorey.github.io/JavaScript-Equality-Table/?utm_content=buffer4f1b9&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer

http://stackoverflow.com/questions/359494/does-it-matter-which-equals-operator-vs-i-use-in-javascript-comparisons

## Logical AND (&&)

Ref: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND

The AND && operator does the following:

- Evaluate operands from left to right.
- For each operand, convert it to a boolean. If the result is false, stop and return the original value of that result.
- If all other operands have been assessed (i.e. all were truthy), return the last operand.

As I said, each operand is convert to a boolean, if it's 0 it's falsy and every other value different than 0 (1, 56, -2, etc etc) are truthy

# Control Flow

## Exception handling statements: throw, try...catch, finally

REF:

- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#Exception_handling_statements
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch

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

- [ECMAScript exceptions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error#Error_types)
- DOMException and DOMError

The try statement consists of:

- a `try block`, which contains one or more statements. {} must always be used, even for single statements.
- At least one `catch clause`, or a `finally clause`.

This gives us three forms for the try statement:

- try...catch
- try...finally
- try...catch...finally

Flow:

- If any statement within the try block (or in a function called from within the try block) throws an exception, control immediately shifts to the catch block.
- If no exception is thrown in the try block, the catch block is skipped.
- The finally block executes after the try and catch blocks execute but before the statements following the try...catch statement.

### Catch

The catch block specifies an identifier (catchID in the preceding syntax) that holds the value specified by the throw statement:

```js
try {
  throw 'myException'; // generates an exception and create the 'myException' string object
} catch (e) {
  // statements to handle any exceptions
  console.log(e); // e is the 'myException' string object. It logs 'myException'
  console.log(typeof e); // string
}
```

### Finally

The finally block contains statements to execute:

- after the try and catch blocks execute
- but before the statements following the try...catch statement.

The finally block executes whether or not an exception is thrown. If an exception is thrown, the statements in the finally block execute even if no catch block handles the exception.

You can use the finally block to make your script fail gracefully when an exception occurs; for example, you may need to release a resource that your script has tied up. The following example opens a file and then executes statements that use the file (server-side JavaScript allows you to access files). If an exception is thrown while the file is open, the finally block closes the file before the script fails.

```js
openMyFile();
try {
  writeMyFile(theData); //This may throw an error
} catch(e) {
  handleError(e); // If we got an error we handle it
} finally {
  closeMyFile(); // always close the resource
}
```

If the finally block returns a value, this value becomes the return value of the entire try-catch-finally production, regardless of any return statements in the try and catch blocks:

```js
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

```js
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

# Primitive values

Ref: https://developer.mozilla.org/en-US/docs/Glossary/Primitive

There are 6 primitive data types: string, number, boolean, null, undefined, symbol (new in ECMAScript 2015).

Most of the time, a primitive value is represented directly at the lowest level of the language implementation.

All primitives are immutable, i.e., they cannot be altered. It is important not to confuse a primitive itself with a variable assigned a primitive value. The variable may be reassigned a new value, but the existing value can not be changed in the ways that objects, arrays, and functions can be altered.

# THIS

- [YDKJS 1st Chapter 1: this Or That](https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch1.md)

This is one of the most misunderstood JS concepts, most common misconceptions about how it doesn't actually work are:

- "this refers to the function itself, because in JS a function is an object" -> WRONG!
  - Read here a full example [YDKJS 1st Chapter 1: this Or That](https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch1.md#itself)
- "this somehow refers to the function's scope." -> WRONG
  - Read here a full example [YDKJS 1st Chapter 1: this Or That](https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch1.md#its-scope)

What is `this`?

We said earlier that this is not an author-time binding but a runtime binding. It is contextual based on the conditions of the function's invocation. this binding has nothing to do with where a function is declared, but has instead everything to do with the manner in which the function is called.

When a function is invoked, an activation record, otherwise known as an execution context, is created. This record contains information about where the function was called from (the call-stack), how the function was invoked, what parameters were passed, etc. One of the properties of this record is the this reference which will be used for the duration of that function's execution.

`this` is actually a binding that is made when a function is invoked, and what it references is determined entirely by the call-site where the function is called.

## Default Binding

ref: https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch2.md#default-binding

If strict mode is in effect, the global object is not eligible for the default binding, so the this is instead set to undefined.

Function invoked as a standalone function `f()`:

- Strict mode: this is `undefined`
- Non Strict mode: Window, the global context

## Implicit binding

https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch2.md#implicit-binding

Function invoked as a method `obj.f()`

Common problem: "Implicitly lost" https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch2.md#implicitly-lost

- SCENARIO: Event handlers in popular JavaScript libraries are quite fond of forcing your callback to have a this which points to, for instance, the DOM element that triggered the event.

## new Binding

https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch2.md#new-binding

Function invoked as a constructor: `new F()`

`this` is the newly created object

## Explicit binding

https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch2.md#explicit-binding

`apply()` or `call()` or `bind()`

Scenario: set "this" explicitly

Usecases: Callback event  handlers

### HARD bind

The most typical way to wrap a function with a hard binding creates a pass-thru of any arguments passed and any return value received:

```js
function foo(something) {
  console.log(this.a, something);
  return this.a + something;
}

var obj = {
  a: 2,
};

var bar = function () {
  return foo.apply(obj, arguments);
};

var b = bar(3); // 2 3
console.log(b); // 5
```

Another way to express this pattern is to create a re-usable helper:

```js
function foo(something) {
  console.log(this.a, something);
  return this.a + something;
}

// simple `bind` helper
function bind(fn, obj) {
  return function () {
    return fn.apply(obj, arguments);
  };
}

var obj = {
  a: 2,
};

var bar = bind(foo, obj);

var b = bar(3); // 2 3
console.log(b); // 5
```

Since hard binding is such a common pattern, it's provided with a built-in utility as of ES5: Function.prototype.bind, and it's used like this:

```js
function foo(something) {
  console.log(this.a, something);
  return this.a + something;
}

var obj = {
  a: 2,
};

var bar = foo.bind(obj);

var b = bar(3); // 2 3
console.log(b); // 5
```

`bind(..)` returns a new function that is hard-coded to call the original function with the this context set as you specified.

Note: As of ES6, the hard-bound function produced by bind(..) has a .name property that derives from the original target function. For example: bar = foo.bind(..) should have a bar.name value of "bound foo", which is the function call name that should show up in a stack trace.

## Arrow Functions

See REF: see [SOJS_2nd] paragraph 4.3.1 for more details

- IMPORTANT: Arrow functions don’t have their own this value. Instead, they remember the value of the this parameter at the time of their definition.
- more concise way of creating functions

See REF: see [SOJS_2nd] paragraph 4.3.2 for more details

- Every function has access to the `bind(function_context)` method
- `bind()` return a new function has the same body, but its context is always bound to the `function_context` parameter.
- For the new returned function, the value of the `this` parameter is always set to the object referenced by the `bind()` argument, regardless of the way the function was invoked. (similar to the arrow function).

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

- Call or Apply
- bind()
- Arrow functions

### Arrow function solution

- When the click arrow function is defined the function context is the `button` object create with `new Button()`.
- When the event handler callback `button.click` is invoked `this` will be assigned to `button`.

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

# Objects

- [YDKJS 1st Chapter 3: Objects](https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch3.md)

## Syntax

Objects come in two forms: the declarative (literal) form, and the constructed form.

```js
The literal syntax for an object looks like this:

var myObj = {
	key: value
	// ...
};
```

The constructed form looks like this:

```js
var myObj = new Object();
myObj.key = value;
```

The constructed form and the literal form result in exactly the same sort of object. The only difference really is that you can add one or more key/value pairs to the literal declaration, whereas with constructed-form objects, you must add the properties one-by-one.

Note: It's extremely uncommon to use the "constructed form" for creating objects as just shown. You would pretty much always want to use the literal syntax form. The same will be true of most of the built-in objects (see below).

## Built-in objects and primitive type Coercion

Ref: https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch3.md#built-in-objects

The primitive value "I am a string" is not an object, it's a primitive literal and immutable value. To perform operations on it, such as checking its length, accessing its individual character contents, etc, a String object is required.

```js
var strPrimitive = "I am a string";
typeof strPrimitive; // "string"
strPrimitive instanceof String; // false

var strObject = new String("I am a string");
typeof strObject; // "object"
strObject instanceof String; // true

// inspect the object sub-type
Object.prototype.toString.call(strObject); // [object String]
```

Luckily, the language automatically coerces a "string" primitive to a String object when necessary, which means you almost never need to explicitly create the Object form.

Consider:

```js
var strPrimitive = "I am a string";
console.log(strPrimitive.length); // 13
console.log(strPrimitive.charAt(3)); // "m"
```

In both cases, we call a property or method on a string primitive, and the engine automatically coerces it to a String object, so that the property/method access works.

## Contents

ref: https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch3.md#contents

The contents of an object consist of values (any type) stored at specifically named locations, which we call `properties`.

What is stored in the container are these property names, which act as pointers (technically, references) to where the values are stored.

Consider:

```js
var myObject = {
  a: 2,
};

myObject.a; // 2

myObject["a"]; // 2
```

To access the value at the location a in myObject, we need to use either the `.` operator or the `[ ]` operator.

- The .a syntax is usually referred to as "property" access,
- whereas the `["a"]` syntax is usually referred to as "key" access.

In reality, they both access the same location, and will pull out the same value, 2, so the terms can be used interchangeably. We will use the most common term, "property access" from here on.

The main difference between the two syntaxes is:

- the . operator requires an Identifier compatible property name after it,
- whereas the [".."] syntax can take basically any UTF-8/unicode compatible string as the name for the property.

EXAMPLE: To reference a property of the name "Super-Fun!", for instance, you would have to use the ["Super-Fun!"] access syntax, as Super-Fun! is not a valid Identifier property name.

Also, since the [".."] syntax uses a string's value to specify the location, this means the program can _ programmatically build up_ the value of the string, such as:

```js
var wantA = true;
var myObject = {
  a: 2,
};

var idx;

if (wantA) {
  idx = "a";
}

// later

console.log(myObject[idx]); // 2
```

In objects, property names are always strings. If you use any other value besides a string (primitive) as the property, it will first be converted to a string. This even includes numbers, which are commonly used as array indexes, so be careful not to confuse the use of numbers between objects and arrays.

```js
var myObject = {};

myObject[true] = "foo";
myObject[3] = "bar";
myObject[myObject] = "baz";

myObject["true"]; // "foo"
myObject["3"]; // "bar"
myObject["[object Object]"]; // "baz"
```

### Computed Property Names [ES6]

https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch3.md#computed-property-names

Example:

```js
var prefix = "foo";

var myObject = {
  [prefix + "bar"]: "hello",
  [prefix + "baz"]: "world",
};

myObject["foobar"]; // hello
myObject["foobaz"]; // world
```

USECASE: .... ??? TODO vedi ref ma cercare altro

### Property VS Method

https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch3.md#property-vs-method

Some developers like to make a distinction when talking about a property access on an object, if the value being accessed happens to be a function. Because it's tempting to think of the function as belonging to the object, and in other languages, functions which belong to objects (aka, "classes") are referred to as "methods", it's not uncommon to hear, "method access" as opposed to "property access".

BUT Every time you access a property on an object, that is a property access, regardless of the type of value you get back. If you happen to get a function from that property access, it's not magically a "method" at that point. There's nothing special (outside of possible implicit this binding as explained earlier) about a function that comes from a property access.

The safest conclusion is probably that "function" and "method" are interchangeable in JavaScript.

### Duplicating Objects

https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch3.md#duplicating-objects

- Shallow Copy: ES6 has now defined Object.assign(..)
- Deep Copy: Still an open issue in JS, some lib cope with it

ISSUES: Circular Reference

Shallow Copy example:

```js
function anotherFunction() {
  /*..*/
}

var anotherObject = {
  c: true,
};

var anotherArray = [];

var myObject = {
  a: 2,
  b: anotherObject, // reference, not a copy!
  c: anotherArray, // another reference!
  d: anotherFunction,
};

var newObj = Object.assign({}, myObject);

newObj.a; // 2
newObj.b === anotherObject; // true
newObj.c === anotherArray; // true
newObj.d === anotherFunction; // true
```

### Property Descriptors

https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch3.md#property-descriptors

as of ES5, all properties are described in terms of a property descriptor.

Consider this code:

```js
var myObject = {
  a: 2,
};

Object.getOwnPropertyDescriptor(myObject, "a");
// {
//    value: 2,
//    writable: true,
//    enumerable: true,
//    configurable: true
// }
```

As you can see, the property descriptor (called a "data descriptor" since it's only for holding a data value) for our normal object property a is much more than just its value of 2.

It includes 3 other characteristics:

- writable: If a property has writable set to false then that property’s value cannot be reassigned another value.
  - example: https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch3.md#writable
- enumerable: will show up in certain object-property enumerations, such as the for..in loop
  - example: https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch3.md#enumerable
- configurable: we can modify its descriptor definition or delete the property.
  - example: https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch3.md#configurable

While we can see what the default values for the property descriptor characteristics are when we create a normal property, we can use `Object.defineProperty(..)` to add a new property, or modify an existing one (if it's configurable!), with the desired characteristics.

For example:

```js
var myObject = {};

Object.defineProperty(myObject, "a", {
  value: 2,
  writable: true,
  configurable: true,
  enumerable: true,
});

myObject.a; // 2
```

Using `defineProperty(..)`, we added the plain, normal a property to myObject in a manually explicit way. However, you generally wouldn't use this manual approach unless you wanted to modify one of the descriptor characteristics from its normal behavior.

All Object Properties have Property Descriptors:

- Every object property has a property descriptor, even if we don’t set one using the Object.defineProperty() method.
- We can use another method, Object.getOwnPropertyDescriptor(), to read a property descriptor.

#### Enumerable and Value

Ref: https://medium.com/intrinsic/javascript-object-property-descriptors-proxies-and-preventing-extension-1e1907aa9d10

The most basic property descriptors are value and enumerable. value contains the value which will be returned when the property is being read. enumerable determines whether or not the property will be visible when listing the properties of the object. Here’s a code sample using these two property descriptors:

```js
const obj = {};
Object.defineProperty(obj, "foo", {
  value: "hello", // the property value
  enumerable: false, // property will not be listed
});
console.log(obj); // {}
console.log(obj.foo); // 'hello'
console.log(Object.keys(obj)); // []
console.log(Reflect.ownKeys(obj)); // [ 'foo' ]
console.log("foo" in obj); // true
```

The enumerable property descriptor has been set to false:

- it becomes a harder to discover the foo property if we don’t know to look for it.
- For example, when we call `console.log(obj)`, we get an empty object in return.`
- When we call `Object.keys(obj)`, we get an empty array in response.
- BUT If we know the name of the property we can still use the in operator, like we’re doing with 'foo' in obj, which returns a true. However, keep in mind this doesn’t completely hide the property, as we can still find it using `Reflect.ownKeys(obj)`.

#### Use-case: Enumerable

Adding a method to an object’s prototype causes that property will now be present in for...in loops and you always need to use `Object#hasOwnProperty()` when enumerating properties.
By specifically setting this enumerable property of the method to `false` you can solve the problem.

```js
const proto = {};
const obj = { ok: 1 };
obj.__proto__ = proto;
for (let key in obj) console.log(key); // [ok]

proto.bad = () => 42;

for (let key in obj) console.log(key); // [ok,bad]
for (let key in obj) {
  if (obj.hasOwnProperty(key)) {
    console.log(key); // [ok]
  }
}
```

In this first example we’ve created a method on our object’s prototype called bad by simply assigning the method to a property using proto.bad. What we instead need to do is the following:

```js
const proto = {};
const obj = { ok: 1 };
obj.__proto__ = proto;
for (let key in obj) console.log(key); // [ok]

Object.defineProperty(proto, "good", {
  value: () => 42,
  enumerable: false,
});

for (let key in obj) console.log(key); // [ok]
```

In this new example we create a method called good, and that method is set using the more verbose Object.defineProperty() syntax. Now, when we iterate the properties of our object, we don’t see our rogue prototype method and we no longer need to use the Object#hasOwnProperty() check.

#### Writable and Configurable

If a property has writable set to false then that property’s value cannot be reassigned another value. If a property has configurable set to false then it cannot be deleted and it cannot have its property descriptor changed again. The following code example shows these two property descriptors at work:

```js
const obj = Object.defineProperty({}, "foo", {
  value: "hello",
  writable: false, // reassignable?
  configurable: false, // deletable/redefinable?
});
obj.foo = "bye";
console.log(obj.foo); // 'hello'
delete obj.foo;
console.log(obj.foo); // 'hello'
Object.defineProperty(obj, "foo", {
  value: 1,
}); // TypeError: Cannot redefine property: foo
```

#### Getter/Setter Property Descriptors

Getters and Setters are some pretty interesting property descriptors, specifically because they allow us to call functions which we define when reading or writing to an object. These are powerful tools with security and performance considerations. The following is an example of the get and set property descriptors:

```js
const obj = { realAge: 0 };

Object.defineProperty(obj, "age", {
  get: function () {
    return this.realAge;
  },
  set: function (value) {
    this.realAge = Number(value);
  },
});

console.log(obj.age); // 0
obj.age = "32";
console.log(obj.age); // 32
```

In this example, we have an object which has a numeric realAge property. For sake of this example consider it being hidden from the outside world. Now, we also have another property called age which is how others will interact with the underlying realAge property. The get property descriptor for age will be called when we read the property, and will simply return realAge. However the set property descriptor will first take the value which is provided, convert it into a Number, and then set realAge to the number we’ve created. This feature prevents others from setting a non-numeric age value on our object and keeps our data in a consistent shape.

Descriptors for accessor properties are different from those for data properties.

For accessor properties, there is no value or writable, but instead there are get and set functions.

That is, an accessor descriptor may have:

- get – a function without arguments, that works when a property is read,
- set – a function with one argument, that is called when the property is set,
- enumerable – same as for data properties,
- configurable – same as for data properties.

For instance, to create an accessor fullName with defineProperty, we can pass a descriptor with get and set:

```js
let user = {
  name: "John",
  surname: "Smith",
};

Object.defineProperty(user, "fullName", {
  get() {
    return `${this.name} ${this.surname}`;
  },

  set(value) {
    [this.name, this.surname] = value.split(" ");
  },
});

alert(user.fullName); // John Smith

for (let key in user) alert(key); // name, surname
```

Please note that a property can be either an accessor (has get/set methods) or a data property (has a value), not both.
If we try to supply both get and value in the same descriptor, there will be an error.

#### ES6 Getter/setter syntax

```js
const obj = {
  realAge: 0,
  get age() {
    return this.realAge;
  },
  set age(value) {
    this.realAge = Number(value);
  },
};
```

When using the getter/setter object literal syntax, things look a little bit different from usual:

```js
const obj2 = {
  get b() {},
};

console.log(Object.getOwnPropertyDescriptor(obj2, "b"));
//{
//  get: Function,
//  set: undefined,
//  enumerable: true,
//  configurable: true
//} // (e.g. Accessor Property)
```

This is a different type of property descriptor, called an `Accessor Property` and looks a little different than the one before it:

- the value and writable properties are missing
- and that the get and set properties are now present.

### Setter/Getter - Private variables

#### Solution 1 - Convention

Ref: https://javascript.info/property-accessors#smarter-getters-setters

Getters/setters can be used as wrappers over “real” property values to gain more control over operations with them.

For instance, if we want to forbid too short names for user, we can have a setter name and keep the value in a separate property \_name:

```js
let user = {
  get name() {
    return this._name;
  },

  set name(value) {
    if (value.length < 4) {
      alert("Name is too short, need at least 4 characters");
      return;
    }
    this._name = value;
  },
};

user.name = "Pete";
alert(user.name); // Pete

user.name = ""; // Name is too short...
```

So, the name is stored in `_name` property, and the access is done via getter and setter.

Technically, external code is able to access the name directly by using `user._name`. But there is a widely known convention that properties starting with an underscore "\_" are internal and should not be touched from outside the object.

#### Solution 2 - Constructor Function and closure

Ref:

- https://itnext.io/how-to-control-access-to-your-javascript-objects-1a75435c04e3
- [SOTJSN2nd] 5.6.1 Revisiting mimicking private variables with closures

```js
function Trump() {
  let _taxReturns = true;

  this.getReturns = () => {
    console.log("getting returns");
    return _taxReturns;
  };

  this.setReturns = (value) => {
    console.log("setting returns");
    if (!(value === true || value === false)) {
      throw new TypeError(
        `YOURE FIRED! cannot set value to ${value}, expected boolean value`
      );
    }
    _taxReturns = value;
  };
}
```

Access to our `_taxReturns` variable is really restricted. Using `using Object.defineProperty` we can define getter and setters:

```js
function Trump() {
  let _taxReturns = true;

  Object.defineProperty(this, "taxReturns", {
    get: () => _taxReturns,
    set: (value) => {
      _taxReturns = value;
    },
  });
}
```

### Immutability: Sealing, Preventing Extension, and Freezing

Refs:

- https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch3.md#immutability
- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze
- https://medium.com/intrinsic/javascript-object-property-descriptors-proxies-and-preventing-extension-1e1907aa9d10

Objects are extensible by default:

- they can have new properties added to them or removed from them.
- and (in engines that support `__proto__`) their `__proto__` property can be modified.

It is sometimes desired to make properties or objects that cannot be changed (either by accident or intentionally). ES5 adds support for handling that in a variety of different nuanced ways.

Sealing, Preventing Extension, and Freezing allow you to lock down an object to varying degrees:

- `Object.preventExtensions()`
- `Object.seal()`
- `Object.freeze()`

Each one of these approaches has the same effect; an object will no longer be extensible, meaning that new properties cannot be added to the object. However there are small nuances which affect each approach as well.

WARNING:

- all of these approaches create SHALLOW immutability.
- If an object has a reference to another object (array, object, function, etc), the contents of that object are not affected, and remain mutable. Example:
- For that reason you may want to consider recursively locking down objects.

```js
"use strict";

let myImmutableObject = {
  foo: [1, 2, 3],
};

Object.freeze(myImmutableObject);

console.log(
  "After freezing an object I can still modify the referenced variables"
);

console.log(myImmutableObject.foo); // [1,2,3]
myImmutableObject.foo.push(4);
console.log(myImmutableObject.foo); // [1,2,3,4]

try {
  myImmutableObject.foo = [];
} catch (e) {
  console.log("But I cannot modify the object properties");
  console.log(e);
}
```

#### Preventing Extension

`Object.preventExtensions()`

- ADD: prevents new properties from ever being added to an object (i.e. prevents future extensions to the object).
- Existing properties can be modified and deleted
- Existing property descriptors are not modified.

`Object.isExtensible()` method to see if an object can be extended.

Note: is the weakest protection when compared to sealing and freezing

```js
const obj = { p: "first" };
Object.preventExtensions(obj);

obj.p = "second"; // OK
obj.p2 = "new val"; // fail silently, throw in strict

console.log(obj); // { p: 'second' }
console.log(Object.isExtensible(obj)); // false
console.log(Object.getOwnPropertyDescriptor(obj, "p"));
// { value: 'second', writable: true,
//   enumerable: true, configurable: true }
delete obj.p; // OK
```

#### Sealing

`Object.seal()`:

- Every property on a sealed object will have its `configurable` property descriptor set to `false`
- `writable`, `enumerable` don't change

`Object.isSealed()` method to see if an object has been sealed.

USE-CASE: an object and you want it to adhere to a certain set of expectations regarding the properties it has, however you don’t necessarily want to prevent changes to those properties.

```js
const obj = { p: "first" };
Object.seal(obj);

obj.p = "second"; // OK
delete obj.p; // fail silently, throw in strict
obj.p2 = "new val"; // fail silently, throw in strict

console.log(obj); // { p: 'second' }
console.log(Object.isSealed(obj)); // true
console.log(Object.getOwnPropertyDescriptor(obj, "p"));
// { value: 'second', writable: true,
//   enumerable: true, configurable: false }
```

#### Freezing

`Object.freeze()`:

- no properties can be reassigned, added, or deleted.
- each property will have both their `writable` and `configurable` values set to false

`Object.isFrozen()` method which will tell you if an object is frozen.

```js
const obj = { p: "first" };
Object.freeze(obj);

obj.p = "second"; // fail silently, throw in strict
delete obj.p; // fail silently, throw in strict
obj.p2 = "new val"; // fail silently, throw in strict

console.log(obj); // { p: 'first' }
console.log(Object.isFrozen(obj)); // true
console.log(Object.getOwnPropertyDescriptor(obj, "p"));
// { value: 'first', writable: false,
//   enumerable: true, configurable: false }
```

#### Summary

![summary](../images/js_immutability_summary.png)

Note that isExt is short for isExtensible. reassign is whether or not a property can be assigned another value. del is whether or not properties can be deleted. add is whether or not a new property can be added.

### Getter/Setter

If you don't modify and default, when you access an object property:

- the default `[[Put]]` operation completely control how values are set to existing or new properties.
- the default `[[Get]]` control how values are retrieved from existing properties.

#### Standard [[Get]]

Consider:

```js
var myObject = {
  a: 2,
};

myObject.a; // 2
myObject.b; // undefined
```

According to the spec, the code above actually performs a [[Get]] operation (kinda like a function call: [[Get]]()) on the myObject:

- The default built-in [[Get]] operation for an object first inspects the object for a property of the requested name, and if it finds it, it will return the value accordingly.
- if it does not find a property of the requested name it will traverse of the [[Prototype]] chain, if any.
- if it cannot through any means come up with a value for the requested property, it instead returns the value `undefined`.

NOTE see also the Paragraph "#### Getter/Setter Property Descriptors"

#### Standard [[Put]]

If the property is present, the `[[Put]]` algorithm will roughly check:

- Is the property an accessor descriptor (see below)? If so, call the setter, if any.
- Is the property a data descriptor with writable of false? If so, silently fail in non-strict mode, or throw TypeError in strict mode.
- Otherwise, set the value to the existing property as normal.

If the property is not yet present on the object in question, the [[Put]] operation is even more nuanced and complex.

TODO We will revisit this scenario in Chapter 5 when we discuss [[Prototype]] to give it more clarity.

#### Define Setter and Getter

When you define a property to have either a getter or a setter or both, its definition becomes an "accessor descriptor" (as opposed to a "data descriptor").

For accessor-descriptors, the `value` and `writable` characteristics of the descriptor are moot and ignored, and instead JS considers the set and get characteristics of the property (as well as configurable and enumerable).

Consider:

```js
var myObject = {
  // define a getter for `a`
  get a() {
    return 2;
  },
};

Object.defineProperty(
  myObject, // target
  "b", // property name
  {
    // descriptor
    // define a getter for `b`
    get: function () {
      return this.a * 2;
    },

    // make sure `b` shows up as an object property
    enumerable: true,
  }
);

myObject.a; // 2

myObject.b; // 4

//we didn't define a setter
myObject.a = 3;
myObject.a; // 2
```

Either through object-literal syntax with `get a() { .. }` or through explicit definition with `defineProperty(..)`, in both cases we created a property on the object that actually doesn't hold a value, but whose access automatically results in a hidden function call to the getter function, with whatever value it returns being the result of the property access.

Since we only defined a getter for a, if we try to set the value of a later, the set operation won't throw an error but will just silently throw the assignment away. Even if there was a valid setter, our custom getter is hard-coded to return only 2, so the set operation would be moot.

To make this scenario more sensible, properties should also be defined with setters, which override the default [[Put]] operation (aka, assignment), per-property, just as you'd expect. You will almost certainly want to always declare both getter and setter (having only one or the other often leads to unexpected/surprising behavior):

```js
var myObject = {
  // define a getter for `a`
  get a() {
    return this._a_;
  },

  // define a setter for `a`
  set a(val) {
    this._a_ = val * 2;
  },
};

myObject.a = 2;

myObject.a; // 4
```

Note: In this example, we actually store the specified value 2 of the assignment ([[Put]] operation) into another variable _a_. The _a_ name is purely by convention for this example and implies nothing special about its behavior -- it's a normal property like any other.

#### You cannot have a setter and property with same name

If you define a setter `name(value)` and then a property `name`:

```js
p = {
  set name(value) {
    this.name = value;
  },
  name: "default",
};
```

The setter will be replaced by a simple property:

```js
console.log(p);
//{name: "default"}
```

### Property Existence

If you reference a variable that cannot be resolved within the applicable lexical scope look-up a `ReferenceError` is thrown.

Instead the result is undefined for a not existing object property:

```js
var myObject = {
  a: undefined,
};

myObject.a; // undefined
myObject.b; // undefined
```

From a value perspective, there is no difference between these two references -- they both result in undefined, you cannot distinguish whether a property exists and holds the explicit value undefined, or whether the property does not exist and undefined was the default return value after [[Get]] failed to return something explicitly.

How you can distinguish these two scenarios?

We can ask an object if it has a certain property without asking to get that property's value:

```js
var myObject = {
  a: 2,
};

"a" in myObject; // true
"b" in myObject; // false

myObject.hasOwnProperty("a"); // true
myObject.hasOwnProperty("b"); // false

myObject2 = Object.create(myObject); // {}

myObject2.b; //undefined
myObject2.a; // 2  // gotten from the prototype
myObject2.hasOwnProperty("a"); // false  // it belongs to the prototype

for (const property in myObject2) {
  console.log(`${property}: ${myObject2[property]}`);
}
```

`in` operator checks if:

- the property is in the object
- or exists at any higher level of the [[Prototype]] chain object

`hasOwnProperty(..)` checks:

- only if myObject has the property,
- DOESN'T traverse the prototype chain

Note: The in operator has the appearance that it will check for the existence of a value inside a container, but it actually checks for the existence of a property name. This difference is important to note with respect to arrays, as the temptation to try a check like 4 in [2, 4, 6] is strong, but this will not behave as expected:

```js
4 in [2, 4, 6]; //false  // 4 is not a property
"length" in [2, 4, 6]; //true   // "length" is a property
```

### Enumeration and Interation

https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch3.md#enumeration

The `enumerable` property descriptor means "the object will be included if the object's properties are iterated through".

In the example below you'll notice that:

- `myObject.b` in fact exists and has an accessible value`
- but it doesn't show up in a `for..in` loop (though, surprisingly, it is revealed by the in operator existence check).

```js
var myObject = {};

Object.defineProperty(
  myObject,
  "a",
  // make `a` enumerable, as normal
  { enumerable: true, value: 2 }
);

Object.defineProperty(
  myObject,
  "b",
  // make `b` NON-enumerable
  { enumerable: false, value: 3 }
);

myObject.b; // 3
"b" in myObject; // true
myObject.hasOwnProperty("b"); // true

// .......

for (var k in myObject) {
  console.log(k, myObject[k]);
}
// "a" 2
```

- `propertyIsEnumerable(..)` tests whether the given property name exists directly on the object and is also `enumerable:true`
- `Object.keys(..)` returns an array of all enumerable properties. DON'T consult the [[Prototype]]
- `Object.getOwnPropertyNames(..)` returns an array of all properties, enumerable or not. DON'T consult the [[Prototype]]

PROBLEM: There is no built-in way to get a list of all properties consulting also the `[[Prototype]]` chain.

- SOLUTION You could approximate such a utility by recursively traversing the [[Prototype]] chain of an object, and for each level, capturing the list from Object.keys(..) -- only enumerable properties.

### Iteration

#### for...in

The `for...in` statement:

- iterates over all enumerable properties of an object that are keyed by strings (ignoring ones keyed by Symbols)
- CONSULT the [[Prototype]]

```js
var myObject = {};

Object.defineProperty(myObject, "a", { enumerable: true, value: 2 });
Object.defineProperty(myObject, "b", { enumerable: false, value: 3 });
// Shows up the prototype behaviour
myObject2 = Object.create(myObject);
Object.defineProperty(myObject2, "c", { enumerable: true, value: 4 });

// "b" is not enumerable, "a" is defined in the Prototype
for (var k in myObject2) {
  console.log(k, myObject2[k]);
}
// "a" 2
// "c" 4
```

#### for with Arrays

Array Note: `for..in` loops applied to arrays can give somewhat unexpected results, in that the enumeration of an array will include not only all the numeric indices, but also any enumerable properties. It's a good idea to use for..in loops only on objects, and traditional for loops with numeric index iteration for the values stored in arrays.

With numerically-indexed arrays, iterating over the values is typically done with a standard for loop, like:

```js
var myArray = [1, 2, 3];

for (var i = 0; i < myArray.length; i++) {
  console.log(myArray[i]);
}
// 1 2 3
```

#### helpers for arrays: forEach, some, every

Each of these helpers accepts a function callback to apply to each element in the array, differing only in how they respectively respond to a return value from the callback:

`forEach(..)`

- will iterate over all values in the array
- ignores any callback return values

`some(..)`

- keeps going until the end or the callback returns a true (or "truthy") value

`every(..)`

- keeps going until the end or the callback returns a false (or "falsy") value

#### for..of

If you iterate on an object with a `for..in` loop, you're also only getting at the values indirectly, because it's actually iterating only over the enumerable properties of the object, leaving you to access the properties manually to get the values.

If you want to iterate over the values directly instead of the array indices (or object properties), ES6 adds a `for..of` loop syntax for iterating over arrays (and objects, if the object defines its own custom iterator):

```js
var myArray = [1, 2, 3];

// Print values not indexes
for (var v of myArray) {
  console.log(v);
}
// 1
// 2
// 3
```

The `for..of` loop asks for an iterator object (from a default internal function known as @@iterator in spec-speak) of the thing to be iterated, and the loop then iterates over the successive return values from calling that iterator object's next() method, once for each loop iteration.

Arrays have a built-in `@@iterator`, so `for..of` works easily on them, as shown. But let's manually iterate the array, using the built-in `@@iterator`, to see how it works:

```js
var myArray = [1, 2, 3];
var it = myArray[Symbol.iterator]();

it.next(); // { value:1, done:false }
it.next(); // { value:2, done:false }
it.next(); // { value:3, done:false }
it.next(); // { done:true }
```

### [ADVANCED] Iterator Protocol and the Iterable Protocol

Ref:

- Long story https://codeburst.io/a-simple-guide-to-es6-iterators-in-javascript-with-examples-189d052c3d8e
- [MDN The iterable protocol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#The_iterable_protocol)
- https://hacks.mozilla.org/2015/04/es6-in-depth-iterators-and-the-for-of-loop/

Iterators are a new way to loop over any collection in JavaScript. They were introduced in ES6.

Symbols offer names that are unique and cannot clash with other property names. `Symbol.iterator` will return an object called an iterator. This iterator will have a method called next which will return an object with keys value and done.

- `value` key will contain the current value. It can be of any type.
- `done` key is boolean. It denotes whether all the values have been fetched or not.

The `Iteration Protocol` establishes the relationship between: iterables, iterators, and next.

- An `iterable` is a data structure that wants to make its elements accessible to the public. It does so by implementing a method whose key is `Symbol.iterator`. That method is a factory for iterators. That is, it will create iterators.
- An `iterator` is a pointer for traversing the elements of a data structure.

The `iteration protocol` is defined here https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#The_iterator_protocol

#### Making Object iterable

We need to implement the `iterable protocol`, we add a method called `Symbol.iterator`. We will use computed property syntax to set this key. A short example is:

```js
const iterable = {
  [Symbol.iterator]() {
    let step = 0;
    const iterator = {
      // we make the iterator. It’s an object with next method defined
      next() {
        // The next method returns the value according to step variable.
        step++;
        if (step === 1) {
          return { value: "This", done: false };
        } else if (step === 2) {
          return { value: "is", done: false };
        } else if (step === 3) {
          return { value: "iterable", done: false };
        }
        return { value: undefined, done: true };
      },
    };
    return iterator;
  },
};

// we retrieve the iterator
var iterator = iterable[Symbol.iterator]();

// we called next. We keep calling next until done becomes true.
iterator.next(); // { value: 'This', done: false }
iterator.next(); // { value: 'is', done: false }
iterator.next(); // { value: 'iterable', done: false }
iterator.next(); // { value: undefined, done: true }
```

This is exactly what happens in `for-of` loop. The for-of loops takes an iterable, and creates its iterator. It keeps on calling the next() until done is true.

HISTORY: That [Symbol.iterator] syntax seems weird. What is going on there? It has to do with the method’s name. The standard committee could have just called this method .iterator(), but then, your existing code might already have some objects with .iterator() methods, and that could get pretty confusing. So the standard uses a symbol, rather than a string, as the name of this method.

#### Iterators: return and throw

- An iterator object can also implement optional `.return()` and `.throw(exc)` methods. If it needs to do some cleanup or free up resources it was using. Most iterator objects won’t need to implement it.
- The `for–of` loop calls `.return()` if the loop exits prematurely, due to an exception or a break or return statement.
- .throw(exc) is even more of a special case: for–of never calls it at all. But we’ll hear more about it next week.

### Natively Iterables objects in JavaScript

A lot of things are iterables in JavaScript:

- Arrays and TypedArrays
- Strings — iterate over each character or Unicode code-points.
- Maps — iterates over its key-value pairs
- Sets — iterates over their elements
- arguments — An array-like special variable in functions
- DOM elements (Work in Progress)

```js
a = [1, 2, 3];
i = a[Symbol.iterator]();
i.next(); // { value: 1, done: false }
```

```js
a = [0, 2, 3]; // Arrays are iterable
for (const value of a) {
} // OK

b = 1;
for (const value of b) {
} // TypeError: b is not iterable
```

Set:

```js
// make a set from an array of words
var words = ["foo", "bar", "foo"];
var uniqueWords = new Set(words);

for (var word of uniqueWords) {
  console.log(word);
}
```

A Map is slightly different: the data inside it is made of key-value pairs, so you’ll want to use destructuring to unpack the key and value into two separate variables:

```js
for (var [key, value] of phoneBookMap) {
  console.log(key + "'s phone number is: " + value);
}
```

Destructuring is yet another new ES6 feature.

### for-of VS for-in and foreach

Ref:

- [Mozilla Ref](https://hacks.mozilla.org/2015/04/es6-in-depth-iterators-and-the-for-of-loop/)
- http://exploringjs.com/es6/ch_generators.html#_ways-of-iterating-over-a-generator

Since ES5, you can use the built-in forEach method:

```
 myArray.forEach(function (value) {
  console.log(value);
});
```

CONS: you can’t break out of this loop using a break statement or return from the enclosing function using a return statement.

How about the old `for–in` loop?

```
 for (var index in ["foo", "bar"]) {    // don't actually do this
  console.log(myArray[index]);
}
```

CONS:

- The values assigned to index in this code are the strings "0", "1", "2" and so on, not actual numbers. Since you probably don’t want string arithmetic ("2" + 1 == "21"), this is inconvenient at best.
- The loop body will execute not only for array elements, but also for any other expando properties someone may have added. For example, if your array has an enumerable property myArray.name, then this loop will execute one extra time, with index == "name". Even properties on the array’s prototype chain can be visited.
- Most astonishing of all, in some circumstances, this code can loop over the array elements in an arbitrary order.
- **In short, for–in was designed to work on plain old Objects with string keys. For Arrays, it’s not so great.**

HISTORY: So there was never any question of “fixing” for–in to be more helpful when used with arrays. The only way for ES6 to improve matters was to add some kind of new loop syntax.

SOLUTION the `for-of` loop:

```js
for (var value of myArray) {
  console.log(value);
}
```

Hmm. After all that build-up, it doesn’t seem all that impressive, does it? Well, we’ll see whether `for–of` has any neat tricks up its sleeve. For now, just note that:

- this is the most concise, direct syntax yet for looping through array elements
- it avoids all the pitfalls of for–in
- unlike forEach(), it works with break, continue, and return

NOTE:

- The `for–in` loop is for looping over **object properties**.
  - `for–of` does not work with plain old Objects, but if you want to iterate over an object’s properties you can either use for–in
  - BETTER SOLUTION: `Object.keys()` expose an object iterable object, so you can avoid `for-in` completly: `for (var key of Object.keys(someObject))`
- The `for–of` loop is for looping over **data—like the values** in an array.

for–of is not just for arrays. It also works on most array-like objects like:

- DOM NodeLists
- Unicode characters: `for (var chr of "😺😲"){}`
- Map and Set objects (new in ES6).
- Any object with an `myObject[Symbol.iterator]()` method

The `for-of loops` require an iterable. Otherwise, it will throw a TypeError.
Like the for/foreach statements in those other languages(Java, C#, etc), for–of works entirely in terms of method calls. What Arrays, Maps, Sets, and the other objects we talked about all have in common is that they have an iterator method.

### Iterating over an interable: Destructuring of Arrays

TODO: questa parte non mi torna moltissimo... non capisco come si relazionano il destructuring e

The code

```
const array = ['a', 'b', 'c', 'd', 'e'];
const [first, ,third, ,last] = array;
```

is equivalent to

```
const array = ['a', 'b', 'c', 'd', 'e'];
const iterator = array[Symbol.iterator]();
const first = iterator.next().value
iterator.next().value // Since it was skipped, so it's not assigned
const third = iterator.next().value
iterator.next().value // Since it was skipped, so it's not assigned
const last = iterator.next().value
```

### Iterating over an interable with the spread operator (…)

re: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax

Spread syntax `...` allows an iterable such as an array expression or string to be expanded in places where zero or more arguments (for function calls) or elements (for array literals) are expected.

#### Function Call example

```js
function sum(x, y, z) {
  return x + y + z;
}

const numbers = [1, 2, 3];

console.log(sum(...numbers));
// expected output: 6

// is equivalent to using the apply method
console.log(sum.apply(null, numbers));
```

#### Array Litteral Example

In the example below the spread operator `...` turns iterable objects into elements of an array literal.

```
const array = ['a', 'b', 'c', 'd', 'e'];
const newArray = [1, ...array, 2, 3];
```

NOTE: array literal

And is equivalent to this ES5 code

```
const array = ['a', 'b', 'c', 'd', 'e'];
const iterator = array[Symbol.iterator]();
const newArray = [1];
for (let nextValue = iterator.next(); nextValue.done !== true; nextValue = iterator.next()) {
  newArray.push(nextValue.value);
}
newArray.push(2)
newArray.push(3)
```

Promise.all and Promise.race accept iterables over Promises.

#### Other Less common examples

// Merge Array
[...array1, ...array2]

// Clone Array
[...array]

// String → Array
[...'string']

// Set → Array
[...new Set([1,2,3])]

// Node List → Array
[...nodeList]

// Arguments → Array
[...arguments]

See here for details: https://www.samanthaming.com/tidbits/92-6-use-cases-of-spread-with-array/#_6-arguments-to-array

### Maps and Sets

The constructor of a Map turns an iterable over [key, value] pairs into a Map and the constructor of a Set turns an iterable over elements into a Set—

const map = new Map([[1, 'one'], [2, 'two']]);
map.get(1)
// one
const set = new Set(['a', 'b', 'c]);
set.has('c');
// true
Iterators are also a precursor to understanding generator functions.

### other Examples

https://gist.github.com/ArfatSalman/49f05cbeb05bb929ada4a3b386ec8aac#file-iterableobject-js

# Functions
[Functions](./javascript_functions.md)

Here are the key topics from the JavaScript Functions file:

1. **JavaScript Compilation**: Two-phase process of declaration scanning and execution.

2. **Scope and Hoisting**: How variables and functions are hoisted during compilation phase.

3. **LHS/RHS References**: Understanding left-hand vs right-hand side references in assignments.

4. **Function Parameters**: Rest parameters, default values, destructuring, and argument handling.

5. **This Context**: Four ways to invoke functions (function, method, constructor, apply/call) and how each affects `this`.

6. **Symbols**: Creation, usage as object properties, well-known symbols, and global symbol registry.

7. **Generators**: Creation, iteration, communication with `yield`, error handling, and composition with `yield*`.

The file provides a deep dive into JavaScript function mechanics, focusing on execution context, parameter handling, and generator functionality.


# Modularity in JS

[JS Modularity](./javascript_modularity.md)

In JS we achive modularity with:

1. **Modularity in JavaScript**: Achieving modularity through modules, prototypes, and classes.

2. **Prototype**: Definition and references to resources on prototypes and inheritance.

3. **CheatSheet and TL;DR**: Key characteristics of objects and functions regarding prototypes.

4. **Object's Prototype**: Explanation of the `[[Prototype]]` property and methods for getting and setting prototypes.

5. **Prototypal Inheritance**: How inheritance works in JavaScript, including examples of prototype chains.

6. **This and Prototype**: Understanding the value of `this` in methods and inherited properties.

7. **Setting & Shadowing Properties**: Behavior of property assignments and shadowing in prototypes.

8. **Constructor Function**: Role of constructor functions and their prototype properties.

9. **Approximate Private Variables**: Using closures and prototypes to manage private variables.

10. **Example Problems**: Issues with prototype references and how to avoid them.

11. **Instanceof and Constructor Property**: Using `instanceof` to check prototype chains and constructor references.

12. **Writing Doesn’t Use Prototype**: How property assignments work directly with objects.

13. **Advanced Topics**: Discussion on the `for..in` loop and deprecated `__proto__` property.

14. **Inheritance**: Setting up prototype chains for inheritance and the importance of `Object.create`.

15. **Classes**: Introduction to ES6 classes as syntactic sugar over prototypes and their features.

# JavaScript Asynchronicity

[JS Asynchronicity](./javascript_asynchronicity.md)

Here are the key topics extracted from the file on JavaScript Asynchronicity:

1. **Introduction to Asynchronicity**: Importance of asynchronous programming and examples like `fetch()`.

2. **Event Loop and Callbacks**: Role of the Event Loop, `setTimeout`, and the callback queue.

3. **Callback Hell**: Issues with nested callbacks and introduction to Promises as a solution.

4. **Promises**: Definition, states (pending, fulfilled, rejected), creation, usage, and error handling.

5. **Promise Chaining**: Benefits of chaining Promises for sequential operations.

6. **Async/Await**: Use of `async` and `await` for cleaner asynchronous code.

7. **Error Handling in Promises**: Techniques for managing errors and unhandled rejections.

8. **Microtask Queue**: Role of the microtask queue in Promise execution.

9. **Promise API**: Overview of static methods like `Promise.all` and `Promise.race`.

10. **Promisification**: Converting callback-based functions into Promise-based functions.


# Is JavaScript a pass-by-reference or pass-by-value language?

ref: https://stackoverflow.com/questions/6605640/javascript-by-reference-vs-by-value

- Javascript is always pass by value, but when a variable refers to an object (including arrays), the "value" is a reference to the object.
- Changing the value of a variable never changes the underlying primitive or object, it just points the variable to a new primitive or object.
- However, changing a property of an object referenced by a variable does change the underlying object.

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

- Multi-tiered inheritance hierarchies are occasionally useful for describing the natural order of objects but if the primary motivation is function re-use they can quickly become gnarly labyrinths of meaningless subtypes, frustrating redundancies and unmanageable logic (“is a button a rectangle or is it a control? tell you what, lets make Button inherit from Rectangle, and Rectangle can inherit from Control…wait a minute….”).
- The most straightforward approach is **delegation**: any public function can be invoked directly via `call` or `apply`. However delegation is so convenient that sometimes it actually works against structural discipline in your code; moreover the syntax can get a little wordy.

Here there is a naive implementation:

```javascript
function extend(destination, source) {
  for (var k in source) {
    if (source.hasOwnProperty(k)) {
      destination[k] = source[k];
    }
  }
  return destination;
}
```

which we can call to extend our prototype…

```javascript
var RoundButton = function (radius, label) {
  this.radius = radius;
  this.label = label;
};

extend(RoundButton.prototype, circleFns);
extend(RoundButton.prototype, buttonFns);
//etc. ...
```

See [this post](http://javascriptweblog.wordpress.com/2011/05/31/a-fresh-look-at-javascript-mixins/) for more about different approach.

See the ember guide for the Ember.Mixin.

# Browser

## Browser runtime, Eventloop, message passing, iframe, memory

See [GUIDE JavaScript runtime environment: EventLoop, Execution Stack, Task, Microtask, rendering steps (ADVANCED)](https://docs.google.com/document/d/10Nr0ETeagEhPX02y_VXKCXRDFeaAlp85p43rRDHuJ-U/edit#heading=h.s0j9kv5n1fti)


## Browser Events

## Browser Debugger TIPS

- `alert("my message")`

### DOM breakpoint

- `on subtree modification`

## Event listeners

If you use the ispector there is a tab that list all listeners.

## MAPS

TODO: dovrebbe essere possibile fare delle mappe per non avere dei mega file CSS e JS

## Same-Site and Same-Origin

 https://web.dev/same-site-same-origin/ 


# CDN

## JSDelivr

https://www.jsdelivr.com/

## CDNJS.com

an lternative to Unpkg, looks better ordinazied but soffers of similar problems:

- To include a package into the CDN it must be added to this repo https://github.com/cdnjs/packages/blob/master/CONTRIBUTING.md
- NON STANDARD: The author of the package is in charge of defining which files he want to expose into the CDN and in which format

For example the date-fns package:

- uses travis to run a script on every new tag https://github.com/date-fns/date-fns/blob/master/.travis.yml#L35
- Use WebPack with the option libraryTarget: 'umd'.
  - This exposes your library under all the module definitions, allowing it to work with CommonJS, AMD and as global variable. Take a look at the UMD Repository to learn more.
  - CDNJS config: https://github.com/cdnjs/packages/blob/master/packages/d/date-fns.json
  - Webpack config:https://github.com/date-fns/date-fns/blob/master/config/webpack.js

## Unpkg: global CDN for everything on NPM

https://unpkg.com/

Use unpkg to quickly and easily load any file from any package using a URL like: `unpkg.com/:package@:version/:file`

NOTE: The unpkg CDN is powered by Cloudflare on Google Cloud

To get a specific version:

If I enter the url: https://unpkg.com/angular-calendar@0.21.3
It would serve: https://unpkg.com/angular-calendar@0.21.3/dist/umd/angular-calendar.js

To get the latest version:

If I enter the url: https://unpkg.com/angular-calendar
It would serve: https://unpkg.com/angular-calendar@0.23.6/bundles/angular-calendar.umd.js

To browse the files in a package:

If you append a / to the url, it will list all the files in the package, ie.

https://unpkg.com/angular-calendar@0.21.3/ will list all the files in that particular package.

Examples
Using a fixed version:

unpkg.com/react@16.7.0/umd/react.production.min.js
unpkg.com/react-dom@16.7.0/umd/react-dom.production.min.js
You may also use a semver range or a tag instead of a fixed version number, or omit the version/tag entirely to use the latest tag.

unpkg.com/react@^16/umd/react.production.min.js
unpkg.com/react/umd/react.production.min.js

# Webpack

https://www.youtube.com/watch?v=MpGLUVbqoYQ&t=0s

The Webpack core goal is: it takes a bunch of different assets, different files of different types (javascript, ../images, like SVG P&G JPEGs, CSS stylesheets or less or sass), all sorts of different files and it combines them down, it bundles them, into smaller group of files.

A standard setup is:

- One file for your JavaScript
- one for your third-party JavaScript (ex: vendor js)
- one for your CSS
- one for your app code app
- one for each image
- ....

Webpack is very configurable which is where it can become a little tedious and pretty intimidating to people who are learning it. But the idea behind it is very simple.

In addition to just bundling things together and just shoving them into a file it's also managing dependencies it's:

- making sure that code that needs to load first is loading first
- so if you write a file that depends on three other files those three need to be included first so often it's a very complex web of dependencies and larger apps and it would be very difficult to manage it on your own.
- webpack does it for you and it spits out one or two or however many files you tell it to bundle and I like how the

Webpack Loaders are responsible for the dependencies

## Getting Started

https://webpack.js.org/guides/getting-started/

## Concepts

[Webpack Guide Concepts](https://webpack.js.org/concepts/)

## Exmaples

### Create React App (Ejected)

npx create-react-app my-app
cd my-app
npm run eject

The webpack config is:

- config/webpack.config.js
- config/webpackDevServer.config.js

## Loaders

https://webpack.js.org/concepts/loaders/

`module.rules` allows you to specify several loaders within your webpack configuration.

Loaders are evaluated/executed from right to left (or from bottom to top).

### Most Common loaders

https://webpack.js.org/loaders/

TODO

### Writing a Loader

https://webpack.js.org/contribute/writing-a-loader/

## Webpack 5

- Module Federation allows a JavaScript application to dynamically load code from another application and  in the process, share dependencies. If an application consuming a federated module does not have a dependency needed by the federated code,  Webpack will download the missing dependency from that federated build origin.

Ref: https://indepth.dev/webpack-5-module-federation-a-game-changer-in-javascript-architecture/

# Browserify

WARNING: capire se è ancora in uso nel 2019

http://browserify.org/#install

Browserify is a tool for compiling node-flavored commonjs modules for the browser:

- Sharing code between Node.js and the browser
- The module system that browserify uses is the same as node, so packages published to npm that were originally intended for use in node but not browsers will work just fine in the browser too.
- people are publishing modules to npm which are intentionally designed to work in both node and in the browser using browserify and many packages on npm are intended for use in just the browser. npm is for all javascript, front or backend alike.

- Getting started: https://github.com/browserify/browserify-handbook

- https://blog.codecentric.de/en/2014/02/cross-platform-javascript/
- introduction to Browserify and Grunt.js and how to leverage Browserify to write code that runs on Node.js and in the browser.

Node, of course, provides a require method in its environment that serves to synchronously load dependencies. The client side, however, is an entirely different beast. There is no require available natively in browsers, so Browserify implements it for us and gives us access to it by passing it into these closures.

# Snowpack and Pika.dev

https://www.snowpack.dev/

Goals:

- Snowpack 1.0: was designed for a simple mission: install npm packages to run directly in the browser. Use a bundler because you want to, and not because you need to.
- Snowpack 2.0: ....

Snowpack isn’t against bundling for production. In fact, we recommend it. File minification, compression, dead-code elimination and network optimizations can all make a bundled site run faster for your users, which is the ultimate goal of any build tool.

Snowpack treats bundling as a final, production-only build optimization. By bundling as the final step, you avoid mixing build logic and bundle logic in the same huge configuration file. Instead, your bundler gets already-built files and can focus solely on what it does best: bundling.

_Snowpack maintains official plugins for both Webpack & Parcel_

If you don’t want to use a bundler, that’s okay too. Snowpack’s default build will give you an unbundled site that also runs just fine. This is what the Snowpack project has been all about from the start: Use a bundler because you want to, and not because you need to.

## Pika.dev CDN

https://www.pika.dev/cdn

- Every npm package can be loaded from Pika CDN as a modern ESM import.
- smart: Every package is optimized to the environment that requested it. That means that only legacy browsers pay the cost of transpiled/polyfilled code, and modern environments get native code.

If a package wasn't written as ESM, we'll do the work to convert it for you.

##

# Babel

https://babeljs.io/docs/en/

## What is Babel?

Babel is a toolchain that is mainly used to convert ECMAScript 2015+ code into a backwards compatible version of JavaScript in current and older browsers or environments.

Here are the main things Babel can do for you:

- Transform syntax
- Polyfill features that are missing in your target environment (through @babel/polyfill)
- Source code transformations (codemods)
- And more! (check out these videos for inspiration)

# Child Processes

Ref:

- https://nodejs.org/api/child_process.html
- https://www.cs.unb.ca/~bremner/teaching/cs2613/books/nodejs-api/child_process/

# MISC: tips and tricks

- Print content of JavaScript object? https://stackoverflow.com/questions/1625208/print-content-of-javascript-object

# NPM packages I used

## Date

This guide https://github.com/you-dont-need/You-Dont-Need-Momentjs

- compares native JS with many date libs, many times you don't need to import an external lib!!!
-

Moment.js is very huge and mutable, AVOID it

- https://github.com/you-dont-need/You-Dont-Need-Momentjs#eslint-plugin

date-fns

- is immutable, a good alternative to moments
- support ranges https://date-fns.org/v1.28.5/docs/isWithinRange

# Components

## Widget VS WebComponents

https://selleo.com/blog/how-to-create-embedded-react-widget

# Testing

[JavaScript Testing](./javascript_testing.md)



Here are the key topics from the JavaScript Testing file:

1. **Testing Fundamentals**: Implementation of a simple Jest clone and basic testing concepts.

2. **Mocking**: Understanding `jest.fn`, `jest.spyOn`, module mocking, and shared mocks.

3. **Static Analysis**: ESLint, Prettier, and TypeScript integration for code quality.

4. **Automation**: Git hooks with Husky, lint-staged for pre-commit checks, parallel npm scripts.

5. **Jest Setup**: Basic configuration, Babel integration, and test file patterns.

6. **Resources**: References to Jest docs, tutorials, and testing strategies.

The file serves as a comprehensive guide to setting up a modern JavaScript testing environment, focusing on Jest and code quality tools.
