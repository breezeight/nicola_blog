---
layout: post
title: "Javascript"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["javascript"]
---

# Contents

{:.no_toc}

- Will be replaced with the ToC, excluding the "Contents" header
  {:toc}

# References:

Books to start programming from scretch with Javascript:

- [YDKJSY](https://github.com/getify/You-Dont-Know-JS)
- It's not just for someone picking up the language for the first time (though it's for them, too); it's for all software craftspeople who want to master their tools, who want to understand the ins and outs of their trade, and who want to select the proper methods for solving problems.
- [EJS]Eloquent_JavaScript(https://eloquentjavascript.net/) 3rd edition

Books:

- [YDKJSY](https://github.com/getify/You-Dont-Know-JS)
- [EJS]Eloquent_JavaScript(https://eloquentjavascript.net/) 3rd edition
- All code in this book may also be considered licensed under an MIT license.
- [GITHUB](https://github.com/marijnh/Eloquent-JavaScript)
- License "CC BY-NC 3.0"
- [SOTJSN2nd](/Volumes/ArchiveDisk/Archive/Misc/ebook/javascript/Secrets_of_the_JavaS.pdf) http://www.manning.com/resig/
- [FJS](/Volumes/ArchiveDisk/Archive/Misc/ebook/javascript/Functional_JavaScript.pdf)
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

In addition to strings, numbers, and booleans, two other primitive values in JS programs are null and undefined. While there are differences between them (some historic and some contemporary), for the most part both values serve the purpose of indicating emptiness (or absence) of a value.

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

Always use === equals unless you have a good reason to use ==.

Fatto molto bene: https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/get-started/ch2.md#comparisons

http://dorey.github.io/JavaScript-Equality-Table/?utm_content=buffer4f1b9&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer

http://stackoverflow.com/questions/359494/does-it-matter-which-equals-operator-vs-i-use-in-javascript-comparisons

## Logical AND (&&)

Ref:https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND

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

- after the try and catch blocks execute
- but before the statements following the try...catch statement.

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

A function is a procedure, a collection of statements that can be invoked one or more times, may be provided some inputs, and may give back one or more outputs.

ref: https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/get-started/ch2.md#functions

A function definition is a regular binding where the value of the binding is the function:

```js
const power = function (base, exponent) {
  let result = 1;
  for (let count = 0; count < exponent; count++) {
    result *= base;
  }
  return result;
};
```

A function is created with an expression that begins with the keyword `function`.

A function have:

- zero o more parameters: they works like regular bindings, but the initial value is given by the caller of the function.
- a body

Functions, not objects are at the core of JavaScript. JS is a Functional language, functions are first-class objects:

- Functions can be arguments of other functions.
- All Functions have the **name** property, if it's anonymous name is an empty string.
- Functions can be referenced by variables `var canFly = function(){ return true; };`

Invoke:

- A Function can be invoked through a variable that reference the function `var canFly = function(){ return true; }; canFly() )`
- a `return` statement determines the value of the returned value and make cotrol jumping out to the caller.
- It there isn't a `return` statement, the value returned is implicitly `undefined`.

A function can be anonymous functions: `function(){return "test"}`

For more example about how to declare functions: see [SOJS] pag 40

Whatever we can do with objects, we can do with functions as well.

Functions are objects, just with an additional, special capability of **being invokable** : Functions can be called or invoked in order to perform an action.

## Closures

Ref:
* https://dmitripavlutin.com/simple-explanation-of-javascript-closures/
* freecodecamp.org/news/lets-learn-javascript-closures-66feb44f6a44/

While being used everywhere, closures are difficult to grasp. Before learning closures, you need to grasp two concept:

* scope 
* lexical scope

These concepts are crucial to closures, and if you get them well, the idea of closure becomes self-evident. Then, after grasping the basics, you'll need just one step to finally understand closures.

### Scope

- When you define a variable, you want it to exist within some boundaries. E.g. a result variable makes sense to exist within a calculate() function, as an internal detail. Outside of the calculate(), the result variable is useless.
- The accessibility of variables is managed by scope. You are free to access the variable defined within its scope. But outside of that scope, the variable is inaccessible.
- In JavaScript, a scope is created by a function or a code block.

Let's see how the scope affects the availability of a variable count. This variable belongs to the scope created by function foo():

```js
function foo() {
  // The function scope
  let count = 0;
  console.log(count); // logs 0
}
foo();
console.log(count); // ReferenceError: count is not defined
```

[Demo on JS Fiddle](https://jsfiddle.net/dmitri_pavlutin/81nmhury/)

count is freely accessed within the scope of foo().

However, outside of the foo() scope, count is inaccessible. If you try to access count from outside anyways, JavaScript throws ReferenceError: count is not defined.

If you've defined a variable inside of a function or code block, then you can use this variable only within that function or code block. The above example demonstrates this behavior.

![](../images/js_scope-3.svg)

Now, let's see a general formulation: "The scope is a space policy that rules the accessibility of variables".

The scope isolates variables. That's great because different scopes can have variables with the same name. You can reuse common variables names (count, index, current, value, etc) in different scopes without collisions.

`foo()` and `bar()` function scopes have their own, but same named, variables count:

```js
function foo() {
  // "foo" function scope
  let count = 0;
  console.log(count); // logs 0
}
function bar() {
  // "bar" function scope
  let count = 1;
  console.log(count); // logs 1
}
foo();
bar();
```

[Demo on JS Fiddle](https://jsfiddle.net/dmitri_pavlutin/weyqczga/)

`count` variables from `foo()` and `bar()` function scopes do not collide.

### Nested Scopes

Let's play a bit more with scopes, and nest one scope into another. For example, the function `innerFunc()` is nested inside an outer function `outerFunc()`.

How would the 2 function scopes interact with each other? Can I access the variable outerVar of outerFunc() from within innerFunc() scope?

Let's try that in the example:

```js
function outerFunc() {
  // the outer scope
  let outerVar = 'I am outside!';
  function innerFunc() {
    // the inner scope
    console.log(outerVar); // => logs "I am outside!"
  }
  innerFunc();
}
outerFunc();
```

[Try the demo](https://jsfiddle.net/dmitri_pavlutin/x4rzf61c/)

Indeed, `outerVar` variable is accessible inside `innerFunc()` scope. The variables of the outer scope are accessible inside the inner scope.


![](../images/js_nested-scopes-3.svg)

Now you know 2 interesting things:

- Scopes can be nested
- The variables of the outer scope are accessible inside the inner scope

### The lexical scope

How does JavaScript understand that outerVar inside innerFunc() corresponds to the variable outerVar of outerFunc()?

JavaScript implements a scoping mechanism named lexical scoping (or static scoping). Lexical scoping means that the accessibility of variables is determined by the position of the variables inside the nested scopes.

Simpler, the lexical scoping means that inside the inner scope you can access variables of outer scopes.

It's called lexical (or static) because the engine determines (at lexing time) the nesting of scopes just by looking at the JavaScript source code, without executing it.

The distilled idea of the lexical scope:

The lexical scope consists of outer scopes determined statically.

For example:

```js
const myGlobal = 0;
function func() {
  const myVar = 1;
  console.log(myGlobal); // logs "0"
  function innerOfFunc() {
    const myInnerVar = 2;
    console.log(myVar, myGlobal); // logs "1 0"
    function innerOfInnerOfFunc() {
      console.log(myInnerVar, myVar, myGlobal); // logs "2 1 0"
    }
    innerOfInnerOfFunc();
  }
  innerOfFunc();
}
func();
```

[Try the demo](https://jsfiddle.net/dmitri_pavlutin/sga5jhku/)

The lexical scope of `innerOfInnerOfFunc()` consits of scopes of `innerOfFunc()`, `func()` and global scope (the outermost scope). Within `innerOfInnerOfFunc()` you can access the lexical scope variables `myInnerVar`, `myVar` and `myGlobal`.

The lexical scope of `innerFunc()` consists of `func()` and global scope. Within `innerOfFunc()` you can access the lexical scope variables myVar and myGlobal.

Finally, the lexical scope of `func()` consists of only the global scope. Within `func()` you can access the lexical scope variable `myGlobal`.

### Closure Definition

Ok, the lexical scope allows to access the variables statically of the outer scopes. There's just one step until the closure!

A closure is a special kind of feature of JS that combines two things:

- a function
- the environment in which that function was created.

Let's take a look again at the outerFunc() and innerFunc() example:

```js
function outerFunc() {
  let outerVar = 'I am outside!';
  function innerFunc() {
    console.log(outerVar); // => logs "I am outside!"
  }
  innerFunc();
}
outerFunc();
```

Inside the `innerFunc()` scope, the variable `outerVar` is accessed from the lexical scope. That's known already.

Note that `innerFunc()` invocation happens inside its lexical scope (the scope of `outerFunc()`).

Let's make a change: `innerFunc()` to be invoked outside of its lexical scope: in a function `exec()`. Would `innerFunc()` still be able to access outerVar?

Let's make the adjustments to the code snippet:

```js
function outerFunc() {
  let outerVar = 'I am outside!';
  function innerFunc() {
    console.log(outerVar); // => logs "I am outside!"
  }
  return innerFunc;
}
function exec() {
  const myInnerFunc = outerFunc();
  myInnerFunc();
}
exec();
```

Running this code has exactly the same effect as the previous example of the `outerFunc()` function above. What's different (and interesting) is that the `innerFunc()` inner function is returned from the outer function before being executed and `innerFunc()` still has access to `outerVar` from its lexical scope, even being executed outside of its lexical scope.

In other words, `innerFunc()` closes over (a.k.a. captures, remembers) the variable outerVar from its lexical scope. In other words, `innerFunc()` is a closure because it closes over the variable outerVar from its lexical scope.

![](../images/js-closure-6.svg)


You've made the final step to understanding what a closure is: The closure is a function that accesses its lexical scope even executed outside of its lexical scope.

Simpler, the closure is a function that remembers the variables from the place where it is defined, regardless of where it is executed later.

A rule of thumb to identify a closure: if inside a function you see an alien variable (not defined inside that function), most likely that function is a closure because the alien variable is captured.

In the previous code snippet, outerVar is an alien variable inside the closure innerFunc() captured from outerFunc() scope.

See a more detailed explanation in the [MDN guide](https://developer.mozilla.org/en/docs/Web/JavaScript/Guide/Closures)

There is a critical difference between a C pointer to a function, and a
JavaScript reference to a function. In JavaScript, you can think of a
function reference variable as having both a pointer to a function as
well as a hidden pointer to a closure. In C, and most other common languages after a function returns, all the local variables are no longer accessible because the stack-frame is destroyed.


Conclusion: 

* The scope rules the accessibility of variables. There can be a function or a block scope.

* The lexical scope allows a function scope to access statically the variables from the outer scopes.

* Finally, a closure is a function that captures variables from its lexical scope. In simple words, the closure remembers the variables from the place where it is defined, no matter where it is executed.

* Closures allow event handlers, callbacks to capture variables. They're used in functional programming. Moreover, you could be asked how closures work during a Frontend job interview.

Every JavaScript developer must know how closures work. Deal with it!

### Closure 

freecodecamp.org/news/lets-learn-javascript-closures-66feb44f6a44/


### Closure Examples: 7 Interview Questions on JavaScript Closures. Can You Answer Them?

What about a challenge? [7 Interview Questions on JavaScript Closures. Can You Answer Them?](https://dmitripavlutin.com/javascript-closures-interview-questions/)

NIK SOLUTION TO question #4:

```js
for (var i = 0; i < 3; i++) {
  let a = i // because i is an integer it's copied by value, then we caputure the variable "a" in the setTimeout function
  setTimeout(function log() {
    console.log(a); // We caputure a instead of i
  }, 1000);
}
```

### Closure Example: Event handler

Let's display how many times a button is clicked:

```js
let countClicked = 0;
myButton.addEventListener('click', function handleClick() {
  countClicked++;
  myText.innerText = `You clicked ${countClicked} times`;
});
```

[Open the demo](https://codesandbox.io/s/event-handling-ymvr9) and click the button. The text updates to show the number of clicks.

When the button is clicked, `handleClick()` is executed somewhere inside of the DOM code. The execution happens far from the place of the definition.

But being a closure, `handleClick()` captures `countClicked` from the lexical scope and updates it when a click happens. Even more, `myText` is captured too.

### Closure Example: Callbacks

Capturing variables from the lexical scope is useful in callbacks.

A `setTimeout()` callback:

```js
const message = 'Hello, World!';
setTimeout(function callback() {
  console.log(message); // logs "Hello, World!"
}, 1000);
The callback() is a closure because it captures the variable message.

An iterator function for forEach():

let countEven = 0;
const items = [1, 5, 100, 10];
items.forEach(function iterator(number) {
  if (number % 2 === 0) {
    countEven++;
  }
});
countEven; // => 2
```
[Try the demo](https://jsfiddle.net/dmitri_pavlutin/kxpscLzv/1/)

The iterator is a closure because it captures countEven variable.

### Closure Example: Functional programming - Currying

Currying happens when a function returns another function until the arguments are fully supplied.

For example:

```js
function multiply(a) {
  return function executeMultiply(b) {
    return a * b;
  }
}
const double = multiply(2);
double(3); // => 6
double(5); // => 10
const triple = multiply(3);
triple(4); // => 12
```

[Try the demo](https://jsfiddle.net/dmitri_pavlutin/fqswk8v0/)

multiply is a curried function that returns another function.

Currying, an important concept of functional programming, is also possible thanks to closures.

executeMultiply(b) is a closure that captures a from its lexical scope. When the closure is invoked, the captured variable a and the parameter b are used to calculate a * b.

### Closure Example

This example taken from SOJS is more advanced:

```javascript
var outerValue = "ninja";
var later;

function outerFunction() {
  var innerValue = "samurai";

  function innerFunction(paramValue) {
    //#1
    assert(outerValue, "Inner can see the ninja.");
    assert(innerValue, "Inner can see the samurai.");
    assert(paramValue, "Inner can see the wakizashi."); //#2
    assert(tooLate, "Inner can see the ronin,"); // All variables in an outer scope, even those declared after the function declaration, are included.
  }

  later = innerFunction;
}

assert(!tooLate, "Outer can't see the ronin"); //#3

var tooLate = "ronin"; //#4

outerFunction();
later("wakizashi"); //#5
```

`open /devel/SRC/JAVASCRIPT/ninja-code/chapter-5/listing-5.3.html`

When we declared `innerFunction()` inside the outer function a closure was also created that encompasses not only the function declaration, but also all variables that are in scope at the point of the declaration.
This “bubble,” containing the function and its variables, stays around as long as the function itself does.

Function parameters are included in the closure of that function. (Seems obvi- ous, but now we’ve said it for sure.

- All variables in an outer scope, even those declared after the function declaration, are included.
- Within the same scope, variables not yet defined cannot be forward-referenced.

### Closure Example: Common mistake in for loops

```html
<p id="help">Helpful notes will appear here</p>
<p>E-mail: <input type="text" id="email" name="email" /></p>
<p>Name: <input type="text" id="name" name="name" /></p>
<p>Age: <input type="text" id="age" name="age" /></p>
```

```javascript
function showHelp(help) {
  document.getElementById("help").innerHTML = help;
}

function setupHelp() {
  var helpText = [
    { id: "email", help: "Your e-mail address" },
    { id: "name", help: "Your full name" },
    { id: "age", help: "Your age (you must be over 16)" },
  ];

  for (var i = 0; i < helpText.length; i++) {
    var item = helpText[i];
    document.getElementById(item.id).onfocus = function () {
      showHelp(item.help);
    };
  }
}

setupHelp();
```

[View On JsFiddle](http://jsfiddle.net/v7gjv)

If you try this code out, you'll see that it doesn't work as expected. No matter what field you focus on, the message about your age will be displayed.

The reason for this is that the functions assigned to onfocus are closures; they consist of the function definition and the captured environment from the setupHelp function's scope. Three closures have been created, but each one shares the same single environment.

The `for` statement don't define a new scope, the `var item` is defined
only once.

NIK NOTE (TODO): a me sembra che se metto un let al posto di var tutto funziona...

To fix the above example we need to define a new scope for each
interation in the for loop using a function factory:

```javascript
function showHelp(help) {
  document.getElementById("help").innerHTML = help;
}

function makeHelpCallback(help) {
  return function () {
    showHelp(help);
  };
}

function setupHelp() {
  var helpText = [
    { id: "email", help: "Your e-mail address" },
    { id: "name", help: "Your full name" },
    { id: "age", help: "Your age (you must be over 16)" },
  ];

  for (var i = 0; i < helpText.length; i++) {
    var item = helpText[i];
    document.getElementById(item.id).onfocus = makeHelpCallback(item.help);
  }
}

setupHelp();
```

[View On JsFiddle](http://jsfiddle.net/v7gjv/1)

This works as expected. Rather than the callbacks all sharing a single environment, the makeHelpCallback function creates a new environment for each one in which help refers to the corresponding string from the helpText array.

This doesn't works, see comments to understand why:

```javascript
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
```

Also this doesn't work, WHY?

```javascript

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
```

### Closure Example: Private variable using closures

See [MDN Guide](https://developer.mozilla.org/en/docs/Web/JavaScript/Guide/Closures#Emulating_private_methods_with_closures)
See [SOJS_2nd] ch 5.2.1

- All assert are true, we can use the accessor method to obtain the value of the private variable, but that we cannot access it directly.
- The JavaScript scoping rules for this variable limit its accessibility to within the constructor.

```javascript
function Ninja() {
  //#1

  var feints = 0; //#2

  this.getFeints = function () {
    //#3
    return feints; //#3
  }; //#3

  this.feint = function () {
    //#4
    feints++; //#4
  }; //#4
}

var ninja = new Ninja(); //#5

ninja.feint(); //#6

assert(
  ninja.feints === undefined, //#7
  "And the private data is inaccessible to us."
); //#7

assert(
  ninja.getFeints() == 1, //#8
  "We're able to access the internal feint count."
); //#8
```

### Keep state. Timers and callbacks using closures.

SOJS ch 5.2.2

In this chapter there are a nice example to avoid pollution of the global scope using closure.

SCENARIO: when a function is called at an unspecified later time and need to keep a state.

SOLUTION 1: object oriented

- you can keep the state in an object instance
- CONS: it's verbose. You have to write a lot of code just to
- PRO: each animation gets its own private “bubble” of variables, you can instantiate multiple animation.

SOLUTION 2: use closures

- PRO: less verbose. With a single function definition you get the same result.
- PRO: each animation gets its own private “bubble” of variables, you can instantiate multiple animation.
- NOTE: Without closures, doing multiple things at once, whether event handling, anima- tions, or even server requests, would be incredibly difficult. If you’ve been waiting for a reason to care about closures, this is it!
- in the below example `elem` and `tick` are kept by the closure `setInterval`:

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

- CONS; If we keep the variables in the global scope, we need a set of three variables for each animation to run multiple animations.

### Common Errors with events handlers and how to fix them: bind()

SOJS ch 5.3:

```javascript
var button = {
  clicked: false,
  click: function () {
    this.clicked = true;
    assert(button.clicked, "The button has been clicked");
    //FAILS: the context of the click function is not referring to the button object as we intended.
  },
};
var elem = document.getElementById("test");
elem.addEventListener("click", button.click, false);
```

the context of the click function is not referring to the button object as we intended.
To solve:

```javascript
function bind(context, name) {
  return function () {
    return context[name].apply(context, arguments);
  };
}
var button = {
  clicked: false,
  click: function () {
    this.clicked = true;
    assert(button.clicked, "The button has been clicked");
    console.log(this);
  },
};
var elem = document.getElementById("test");
elem.addEventListener("click", bind(button, "click"), false);
```

The secret sauce that we’ve added here is the bind() method. This method is designed to create and return a new anonymous function that calls the original function, using apply(), so that we can force the context to be whatever object we want.

### JS Scope Exercise

http://stackoverflow.com/questions/18067742/variable-scope-in-nested-functions-in-javascript

http://doppnet.com/2011/10/10-advanced-javascript-interview-questions/

http://www.codecademy.com/forums/javascript-intro/4/exercises/2

### Scope example

#### Ex 1

```javascript
var foo;
function setFoo(val) {
  var foo = val;
}
setFoo(10);
alert(foo); // print undefined
```

if you remove the var:

```javascript
var foo;
function setFoo(val) {
  foo = val; //removed var
}
setFoo(10);
alert(foo); // print 10
```

http://www.codecademy.com/forum_questions/4f166ff96390db0001003803

## Difference between identifier and variable (in JavaScript)

Ref: https://stackoverflow.com/questions/28185877/difference-between-identifier-and-variable-in-javascript#28185939

The difference between identifiers and variables is the same as that between names and people.

Names identify people. They can also identify dogs, for example. Names are not people, nor are people names. But you can say that I am Amadan (since saying that I am identified by the name Amadan sounds clunky).

Identifiers identify variables. Identifiers are not variables, nor are variables identifiers.

```
var pippo = 2;
```

- `pippo` is the identifier
- `2` is the value of the variable
- the variable is a generic container that can contain different type of values (strings, arrays, etc), it's the memory location.

NOTE: since saying that is the variable containing the value `2` is identified by the identifier `pippo` sounds clunky, usually you say that that variable is `pippo`.

A good analogy for a variable would be locker boxes:

- **identifiers**: the number written on the box. A way to reference a variable in your source code.
- **value**: the contents of whatever you put inside.
- **variable**: the box. A variable is memory space identified by an identifier that can contain a value (whether a primitive value or a reference value) as its content.

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

- [SOJS_2nd] 5.3
- https://medium.com/@gaurav.pandvia/understanding-javascript-function-executions-tasks-event-loop-call-stack-more-part-1-5683dea1f5ec


NOTE: For more details about how JS runtime runs SYNC and ASYNC code see [GUIDE JavaScript runtime environment: EventLoop, Execution Stack, Task, Microtask, rendering steps (ADVANCED)](https://docs.google.com/document/d/10Nr0ETeagEhPX02y_VXKCXRDFeaAlp85p43rRDHuJ-U/edit#heading=h.s0j9kv5n1fti)

When a fragment of JavaScript code runs, it runs inside an execution context. There are three types of code that create a new execution context:

* The global context is the execution context created to run the main body of your code; that is, any code that exists outside of a JavaScript function.
* Each function is run within its own execution context. This is frequently referred to as a "local context."
* Using the ill-advised eval() function also creates a new execution context.

Each context is, in essence, a level of scope within your code. As one of these code segments begins execution, a new context is constructed in which to run it; that context is then destroyed when the code exits. 

In JavaScript, the fundamental unit of execution is a function.

Problem: When a function call another function, our program execution has to return to the position from which the function was called.

The JS runtime internally uses the the `execution context` and the `Call Stack` to achieve this:

- `execution context`: is a data structure which records the function calls executed for each code structure (function, code block, etc); basically where in the program we are (which statements and expression have been runned). There are only one global execution context and one execution context for each function execution.
- Every time a function is invoked the JS engine pauses the current execution context and create a new one, which is pushed on the `Call Stack`.
- `Call Stack`: is a data structure which records the of current and stopped Execution context
- each time a function return its Execution Context is _popped out_ from the stack and _discarded_.
- Video animation : https://youtu.be/8aGhZQkoFbQ?t=270
- NOTE: in [SOJS_2nd] the Call Stack is called `Execution Context Stack`

This is because JavaScript is based on a **single-threaded execution model**:

- Only one piece of code can be executed at a time.
- Every time a function is invoked, the current execution context has to be stopped, and a new function execution context, in which the function code will be evaluated, has to be created.
- See [SOJS_2nd] Figure 5.6

TODO : Blocking: https://youtu.be/8aGhZQkoFbQ?t=439

## Binding Scope

Each binding has a scope. A scope is the part the part of the program in which the binding is visible.

In JS **scope are declared by functions not blocks** In the example x is still in scope after the end of the block because the function scope is not changed:

```
if(window) {
  var x = 123
}
alert(x)
```

- named global functions are property of the window object
- a function is available throughout the scope it is declared. Also if it
  is declared at the end of the scope it is available also at the
  beginning of the scope.
- a variable is available only after it is declared to the end of the
  scope (the inner example here file:///devel/SRC/JAVASCRIPT/ninja-code/chapter-3/listing-3.2.html,
  inner is defined after a but it is in scope before the variable a).
- for the purpose of declaration scopes the global context act acts like
  one big function encompassing the code on the page.

## Lexical Context (or Scope)

Ref:

- See [SOJS_2nd] 5.4
- Mozilla: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures

By the time you've written your first few programs, you're probably starting to feel more comfortable with creating variables and storing values in them. Working with variables is one of the most foundational things we do in programming!

But you may not have considered very closely the underlying mechanisms used by the engine to organize and manage these variables. I don't mean how the memory is allocated on the computer, but rather: how does JS know which variables are accessible by any given statement, and how does it handle two variables of the same name?

The answers to questions like these take the form of well-defined rules called scope.

`Lexical environment` or `scope` is an internal JavaScript engine construct used to keep track of the mapping from identifiers to specific variables. It's an internal implementation of the JavaScript scoping mechanism.

`Indentifier resolution`: is the process of figuring out which variable a certain identifier refers to.

For example, consider the following code:

```
  var ninja = "Hattori";
  console.log(ninja);
```

The lexical environment is consulted when the ninja variable is accessed in the console.log statement.

Usually, a lexical environment is associated with a specific structure of JavaScript code. It can be associated with:

- a function,
- a block of code,
- or the catch part of a try-catch statement.

Each of these structures (functions, blocks, and catch parts) can have its own separate identifier mappings. Each of these code structures gets an associated lexical environment **every time** the **code is evaluated**.

Each `execution context` has a `lexical environment` associated with it, that contains the mapping for all identifiers defined directly in that context.

NOTE In pre-ES6 versions of JavaScript, a lexical environment could be associated with only a function. Variables could be only function scoped. This caused a lot of confusion. Because JavaScript is a C-like language, people coming from other C-like languages (such as C++, C#, or Java) naturally expected some low-level concepts, such as the existence of block scopes, to be the same. With ES6, this is finally fixed.

Scope Nesting:

- in Javascript you can access variables defined in outer code structures.
- JS supports closure

Both behaviours are supported by JS engines using a linked list of `lexical environment`: each lexical environment has to keep track of its outer (parent) lexical environment.

If an identifier can’t be found in the current environment, the outer environment is searched. This stops either when:

- the matching variable is found,
- or with a reference error if we’ve reached the global environment and there’s no sign of the searched-for identifier.

![image](https://raw.githubusercontent.com/getify/You-Dont-Know-JS/2nd-ed/scope-closures/../images/fig2.png)

Ref: See [SOJS_2nd] figure 5.9

In order to support the closure, how is the outer lexical environment set when we call a function?

- JavaScript does this by taking advantage of functions as first-class objects. Whenever a function is created, a reference to the lexical environment in which the function was created is stored in an internal (meaning that you can’t access or manipulate it directly) property named [[Environment]]; double brackets is the notation that we’ll use to mark these internal properties.

Whenever a function is called:

- a new function execution context is created and pushed onto the execution context stack.
- a new associated lexical environment is created.
- Now comes the **crucial part**: For the outer environment of the newly created lexical environment, the JavaScript engine puts the environment referenced by the called function’s internal [[Environment]] property, the environment in which the now-called function was created!

NOTE: This might seem odd at first. Why don’t we just traverse the whole stack of execution contexts and search their matching environments for iden- tifier mappings? Technically, this would work in our example. But remember, a JavaScript function can be passed around as any other object, so the posi- tion of the function definition and the position from where the function is called generally aren’t related (remember closures).

### Metaphore: conversation Compiler-ScopeManager-Engine

SEE: https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch2.md#a-conversation-among-friends

TL;DR:

```js
var students = [
  { id: 14, name: "Kyle" },
  { id: 73, name: "Suzy" },
  { id: 112, name: "Frank" },
  { id: 6, name: "Sarah" },
];
```

Let's now meet the members of the JS engine that will have conversations as they process that program:

- Engine: responsible for start-to-finish compilation and execution of our JavaScript program.

- Compiler: one of Engine's friends; handles all the dirty work of parsing and code-generation.

- Scope Manager: another friend of Engine; collects and maintains a look-up list of all the declared variables/identifiers, and enforces a set of rules as to how these are accessible to currently executing code.

A typical line of code consist of two parts: declaration and initialization-assignment. Engine sees two distinct operations:

- `declaration`: which Compiler will handle during compilation
- `initialization`: which Engine will handle during execution.

Once Compiler gets to code-generation, there's more detail to consider than may be obvious. A reasonable assumption would be that Compiler will produce code for the first statement such as: "Allocate memory for a variable, label it students, then stick a reference to the array into that variable." But there's more to it.

Here's how Compiler will handle that statement:

- Encountering var students, Compiler will ask Scope Manager to see if a variable named students already exists for that particular scope bucket. If so, Compiler would ignore this declaration and move on. Otherwise, Compiler will produce code that (at execution time) asks Scope Manager to create a new variable called students in that scope bucket.

- Compiler then produces code for Engine to later execute, to handle the students = [] assignment. The code Engine runs will first ask Scope Manager if there is a variable called students accessible in the current scope bucket. If not, Engine keeps looking elsewhere (see "Nested Scope"). Once Engine finds a variable, it assigns the reference of the [ .. ] array to it.

Later, when the Engine is executing, since the declaration has an initialization assignment, Engine asks Scope Manager to look up the variable, and assigns to it once found.

### Looking up errors

Ref: https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch2.md#lookup-failures

"Reference Error: XYZ is not defined" is thrown when we cannot resolve the lookup of an identifier:

- and is a source variable
- or When is a target variable and STRICT MODE is enabled

### var VS Accidental Global Variables

Ref: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#Description

TL;DR:

- It is recommended to always declare variables, regardless of whether they are in a function or global scope.
- In ECMAScript 5 strict mode, assigning to an undeclared variable throws an error.

Assigning a value to an undeclared variable implicitly creates it as a global variable (it becomes a property of the global object) when the assignment is executed.

The differences between declared and undeclared variables are:

1. Declared variables (var,let,const) are constrained in the execution context in which they are declared. Undeclared variables are always global.

```js
function x() {
  y = 1; // Throws a ReferenceError in strict mode.
  var z = 2;
}

x();

console.log(y); // 1
console.log(z); // Throws a ReferenceError: z is not defined outside x.
```

2. Declared variables are created before any code is executed. Undeclared variables do not exist until the code assigning to them is executed.

```js
console.log(a); // Uncaught ReferenceError: a is not defined
```

```js
console.log(a); // undefined
console.log("still going..."); // still going...
var a = 1;
console.log(a); // 1
```

3. Declared variables are a non-configurable property of their execution context (function or global). Undeclared variables are configurable (e.g. can be deleted).

```js
var a = 1;
b = 2;

delete this.a; // Throws a TypeError in strict mode. Fails silently otherwise.
delete this.b;

console.log(a, b); // Throws a ReferenceError.
// The 'b' property was deleted and no longer exists.
```

If the variable is a target and strict-mode is not in effect, a confusing and surprising legacy behavior kicks in. The deeply unfortunate outcome is that the global scope's Scope Manager will just create an accidental global variable to fulfill that target assignment!

Consider:

```js
function getStudentName() {
  // assignment to an undeclared variable :(
  nextStudent = "Suzy";
}

getStudentName();

console.log(nextStudent);
// "Suzy" -- oops, an accidental-global variable!
```

Here's how that conversation would go:

- Engine: Hey Scope Manager (for the function), I have a target reference for nextStudent, ever heard of it?
- (Function) Scope Manager: Nope, never heard of it. Try the next outer scope.
- Engine: Hey Scope Manager (for the global scope), I have a target reference for nextStudent, ever heard of it?
- (Global) Scope Manager: Nope, but since we're in non-strict-mode, I helped you out and just created a global variable for you, here you go!

Yuck. This sort of accident (almost certain to lead to bugs eventually) is a great example of the protections of strict-mode, and why it's such a bad idea to not use it.

### Scope is only partially determined at compile time

Ref: https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch3.md#lookup-is-mostly-conceptual

lexical scope is partially determined during the initial compilation processing, exeption are:

- variable that isn't declared in any lexically available scopes in the current file (ex: modules)

Because each file is its own separate program from the perspective of JS compilation.

So the ultimate determination of whether the variable was ever appropriately declared in some accessible bucket may need to be deferred to the run-time.

### Scope: Variable Shadowing

Ref: https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch3.md#shadowing

When two variables have the same name the one in the inner scope hide the one in the outer scope.

"Variables lookup" starts with the current scope and works its way outward/upward, stopping as soon as a matching variable is found.

EXAMPLE: a function parameter shadows (or is shadowing) a global variable with the same name

In the global scope, `var` declarations and `function-declarations` also expose themselves as properties (of the same name as the identifier) on the global object.

NOTE: this is not true for `let`, `const`, `class`

```js
var studentName = "Suzy";
// In the browser is mirrored to:
window.studentName;
```

### Scope: Legal and Illegal shadowing examples

- let (in an inner scope) can always shadow an outer scope's var. var (in an inner scope) can only shadow an outer scope's let if there is a function boundary in between.

- Ref: https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch3.md#illegal-shadowing
- Examples: https://github.com/breezeight/javascript_nicola_courses/tree/master/you-dont-know-js-yet/scope-and-closure/ch3-the-scope-chain

### Function Name Scope

https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch3.md#function-name-scope

This example will create a variable in the enclosing scope (in this case, the global scope) named askQuestion:

```js
function askQuestion() {
  // ..
}
```

With this function definition you will obtain the same result of the above example but it will not "hoist" :

```js
var askQuestion = function () {
  // ..
};
```

A 3rd, not obvious case is:

```js
var askQuestion = function ofTheTeacher() {
  // ..
};
askQuestion();
// function ofTheTeacher()...

console.log(ofTheTeacher);
// ReferenceError: 'ofTheTeacher' is not defined
```

WARNING: `ofTheTeacher` is declared as an identifier inside the function itself:

See https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch3.md#function-name-scope for more details

### Arrow Function and scope

https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch3.md#arrow-functions

Arrow functions have the same rules with respect to lexical scope as function functions do. An arrow function, with or without { .. } around its body, still creates a separate, inner nested bucket of scope. Variable declarations inside this nested scope bucket behave the same as in function functions.

### Global Scope in different Environment

The global scope of a JS program is a rich topic, with much more utility and nuance than you would likely assume. Many corner cases will rise, related to:

- The env your are running (Browser, Web Workers, NodeJS...)
- How you bundle and load your JS files

TODO: read this https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch4.md#chapter-4-around-the-global-scope

### Limiting Scope Exposure (BEST PRACTICE)

https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch6.md

### More about Forward Declaration in Javascript or Hoisting

See:

- http://www.i-programmer.info/programming/javascript/5364-javascript-hoisting-explained.html
- http://www.w3schools.com/js/js_hoisting.asp

**NOTE** JavaScript in _strict mode_ does not allow variables to be used if they are not declared.

## Lexical scoping: Explaining Value vs. Reference in Javascript

ref:

- https://codeburst.io/explaining-value-vs-reference-in-javascript-647a975e12a0

Javascript has 5 data types that are `passed by value`, we’ll call these primitive types:

- Boolean,
- null,
- undefined,
- String,
- Number

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

- `var`
  - been part of JavaScript since its beginning
- `let`
  - ES6 additions
- `const`
  - ES6 additions
  - we have to provide an initialization value when it’s declared and we can’t assign a completely new value to it afterward.
  - We can’t assign a completely new object, but there’s nothing stopping us from modifying the one we already have (ex: add item to an array).

They differ in two aspects:

- mutability
- their relationship toward the lexical environment.

### Variable definition keywords: mutability

Usecase: const primitive type

- `const` is expecially usefull for all the type that in JS can be assigned only by value (string, Boolean, number, etc)
- ex: `const MAX_BUFFER_SIZE = 256` will guarantee that `MAX_BUFFER_SIZE` cannot be changed. We are safeguarded our code against unwanted or accidental modifications.

Usecase: const object

- we can’t assign a completely new value to a const variable. But there’s nothing stopping us from modifying the current one

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

- DIFFERENT FROM CPP and JAVA: we can access the variables defined with the `for` code blocks even outside those blocks
- None of the function variables are accessible outside of the function.

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

- [SOJS_2nd] 5.5.3
- Mozilla MDN: https://developer.mozilla.org/en-US/docs/Glossary/Hoisting
- https://john-dugan.com/hoisting-in-javascript/

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

- The variables can be initialized and used before they are declared.
- But **only declarations** are hoisted, not initializations.

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

Ref:

- Kyle Simpson https://frontendmasters.com/courses/advanced-javascript/
- YDKJSY "The (not so) Secret Lifecycle of Variables" https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch5.md

To understand Lexical Environment in JS you must understand that JS is a compiled language. Most of us think that JAVA or CPP are compiled languages because we use compilers to ship our application as bytecode or machine readable Executables, but it not the right way to classify a compiled language.

With JS we distribute our source code so a lot of people tend to say it is interpreted language but it's not. All JS engine will compile your source code before running it, every single time you execute it.

What is an interpreted language? Let's look at Bash scripting: when the bash interpreter is running line 3, it has NO IDEA of what to expect at line 4.
Instead a compiled language read the whole source code before running it! This is the main point!

### Hoisting YDNJSY metaphor

https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch5.md#hoisting-yet-another-metaphor

The hoisting (metaphor) proposes that JS pre-processes (during compiling) the original program and re-arranges it slightly, so that all the declarations have been moved to the top of their respective scopes, before execution. Moreover, the hoisting metaphor asserts that function declarations are, in their entirety, hoisted to the top of each scope, as well.

Consider:

```js
studentName = "Suzy";
greeting();
// Hello Suzy!

function greeting() {
  console.log(`Hello ${studentName}!`);
}

var studentName;
```

The "rule" of the hoisting metaphor is that function declarations are hoisted first, then variables immediately after all the functions. Thus, hoisting suggests that program is re-written by the JS engine to look like this:

```js
function greeting() {
  console.log(`Hello ${studentName}!`);
}
var studentName;

studentName = "Suzy";
greeting();
// Hello Suzy!
```

### Re-Declaration of variables and functions

https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch5.md#re-declaration

### Simplified overview of how a JS Engine parse and execute code

Ref:

- https://john-dugan.com/hoisting-in-javascript/
- [SOJS_2nd] 5.5.3

To understand how Lexical Environment works we need to

- know how the step "finding decorations of variables and functions" of the compilation process is managed.
- know how the JS engine registrers identifiers

Decorations are: `var`, `let`, `function`, etc

`var foo = "bar";` is a single JS statement but is treated by the engine as two different operations that happens at different time:

- the decoration operation `var foo`
- the initialization operation `foo = "bar";`

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

- Line 1: Hey global scope, I have a declaration for a variable named foo.
- Line 3: Hey global scope, I have a declaration for a function1 named bar.
  - NOTE: Since bar is a function, we recursively decent into its scope and continue compilation.
- Line 4: Hey bar scope, I have a declaration for a variable named foo.
- Line 6: Hey bar scope, I have a declaration for a function named baz.
- Line 6: Hey baz scope, I have a declaration for a parameter named foo.

JavaScript Execution, The second step take by the browser’s JavaScript engine.

There are two terms that you need to be familiar with as we enter the execution phase: LHS and RHS. LHS stands for left hand side, and RHS stands for right hand side. LHS references are located on the left hand side of the = assignment operator. RHS references are located on the right hand size of the of the = assignment operator, or implied when there is no LHS reference. If this seams a bit confusing, a good way to think about LHS versus RHS is target versus source. LHS is the target, and RHS is the source.

- Line 1: Hey global scope, I have an LHS reference for a variable named foo. Ever heard of it?

  - The global scope has because foo was registered on line 1 in the compilation phase, so the assignment occurs.
  - NOTE: Lines 3–11 don’t exist in the execution phase because they were compiled away. So, we move to line 13.

- Line 13: Hey global scope, I have an RHS2 reference for a variable named bar. Ever heard of it?

  - The global scope has because bar was registered as a function on line 3 in the compilation phase, so the function executes.
  - NOTE: The reason line 13 is an RHS is because there is no assignment. As such, we cannot establish a left/right reference. Therefore, we know that the value on line 13 represents the source.

- Line 4: Hey bar scope, I have an LHS reference for a variable named foo. Ever heard of it?

  - The bar scope has because foo was registered on line 1 in the compilation phase, so the the assignment occurs.
  - Within the bar scope, foo will always refer to the value assigned to it on line 4. This is because the foo variable on line 4 is preceded with the var keyword, and will therefore be the first reference to foo inside the bar scope.
  - NOTE: Lines 6–9 don’t exist in the execution phase because they were compiled away. So, we move to line 10.

- Line 10: Hey bar scope, I have an RHS reference for a variable named baz. Ever heard of it?

  - The bar scope has because baz was registered as a function on line 6 in the compilation phase, so the function executes.

- Line 7: Hey baz scope, I have an LHS reference for a variable named foo. Ever heard of it?

  - The baz scope has because foo was declared as a parameter of the baz function on line 6 in the compilation phase, so the assignment occurs.

- Line 8: Hey baz scope, I have an LHS reference for a variable named bam. Ever heard of it?
  - The baz scope has not. Therefore we look for bam in the next outer scope, the bar scope.
- Line 8: Hey bar scope, I have an LHS reference for a variable named bam. Ever heard of it?
  - The bar scope has not. Therefore we look for bam in the next outer scope, the global scope.
- Line 8: Hey global scope, I have an LHS reference for a variable named bam. Ever heard of it?

  - The global scope has not. Therefore the global scope automatically registers a variable named bam.
  - NOTE: If you are in strict mode, the bam variable will not be registered. Therefore, because bam doesn’t exist a reference error will be thrown.

- Line 14: Hey global scope, I have an RHS reference for a variable named foo. Ever heard of it?

  - The global scope has because foo was declared on line 1 in the compilation phase, its value is the string “bar”.

- Line 15: Hey global scope, I have an RHS reference for a variable named bam. Ever heard of it?

  - The global scope has because bar was automatically created two steps back, its value is the string “yay”.
  - NOTE if you are in strict mode, a reference error will be thrown because bam doesn’t exist.

- Line 16: Hey global scope, I have an RHS reference for a variable named baz. Ever heard of it?
  - The global scope has not because baz was exists in the function scope of bar. Therefore, baz is inaccessible to the global scope and a reference error is thrown.

During the `Compilation Phase`, the engine will search for `decorations of variables and functions`:

The behavior depends on type of code (global code, function code, or block code), for each of type:

- code is parsed but isn’t executed.
- new lexical environment is created.
- JS engine visits and registers all declared variables and functions within the current lexical environment. The exact behavior depends on the type of variable (let, var, const, function declaration) and the type of environment (global, function, or block). The process of `registering variables` is as follows:

step 1 create `arguments identifier`:

- If we’re creating a `function lexical environment`: the implicit `arguments` identifier is created, along with all formal function parameters and their argument values.
- If we’re dealing with a nonfunction environment, this step is skipped.

step 2, scan for `function declarations` (without going into the body of other functions):

- If we’re creating a `global or a function environment`:
  - scan for function declarations (but not function expressions or arrow functions!).
  - For each discovered function declaration, a new function is created and bound to an identifier in the environment with the function’s name.
  - If that identifier name already exists, its value is overwritten.
  - NOTE: this explain how hoi
- If we’re dealing with `block environments`: this step is skipped.
  - NOTE: ECMAScript 5, the current official specification of the JavaScript language, does not define the behavior for function declarations inside blocks.
  - NOTE: in ES6 are allowed https://stackoverflow.com/questions/31419897/what-are-the-precise-semantics-of-block-level-functions-in-es6
  - NOTE: MY OPINION, avoid them....
  - TODO: https://stackoverflow.com/questions/25111087/why-is-a-function-declaration-within-a-condition-block-hoisted-to-function-scope

step 3, scan for `variable declarations`:

- In `function or global environments`:
  - all variables declared with the keyword `var` and defined outside other functions (but they can be placed within blocks!) are found,
  - and all variables declared with the keywords `let` and `const` defined outside other functions and blocks are found.
- In `block environments`:
  - the code is scanned only for variables declared with the keywords `let` and `const`, directly in the current block.
- For each discovered variable:

  - if the identifier doesn’t exist in the environment, the identifier is registered and its value initialized to `undefined`.
  - if the identifier exists, it’s left with its value.

- second phase:
  - starts after this has been accomplished
  - all the expressions and statement are evaluated in order.

Puting it all together — compilation + execution: Hoisting is simply a mental construct. You saw hoisting in action during the compilation phase in the example above. Understanding how JavaScript is compiled and executed is the key to understanding hoisting. Let’s go through one more simpler conversation in the context of hoisting and examine what happens with the code before, during and after compilation.

```
  // Code as authored by developer, Before Compilation
  a;
  b;
  var a = b;
  var b = 2;
  b;
  a;
```

```
  /*
      During Compilation
      Notice: Variable declarations have been **hoisted** to the top of the
      containing scope. In this case, the global scope.
  */
  var a;
  var b;
  a;
  b;
  a = b;
  b = 2;
  b;
  a;
```

```
  /*
      After Compilation
      Notice: The var keyword has been compiled away.
  */
  a;      // undefined // line 4
  b;      // undefined // line 5
  a = b;
  b = 2;
  b;      // 2
  a;      // undefined
```

Now that you understand how variables get hoisted during the compilation phase, understanding the execution phase is much easier. Below is the conversation that occurs during the execution phase, as shown in the After Compilation figure above.

- Line 4: Hey global scope, I have an RHS reference for a variable named a. Ever heard of it?
  - The global scope has because a was registered on line 5 in the compilation phase, its value is undefined.
- Line 5: Hey global scope, I have an RHS reference for a variable named b. Ever heard of it?
  - The global scope has because b was registered on line 6 in the compilation phase, its value is undefined.
- Line 6: Hey global scope, I have an LHS reference for a variable named a. Ever heard of it?
  - The global scope has because a was registered on line 5 in the compilation phase, so the assignment occurs.
- Line 7: Hey global scope, I have an LHS reference for a variable named b. Ever heard of it?
  - The global scope has because b was registered on line 6 in the compilation phase, so the assignment occurs.
- Line 8: Hey global scope, I have an RHS reference for a variable named b. Ever heard of it?
  - The global scope has because b was registered on line 6 in the compilation phase and a value was assigned to it on line 7 in the [current] execution phase, its value is the number 2.
- Line 9: Hey global scope, I have an RHS reference for a variable named a. Ever heard of it?
  - The global scope has because a was registered on line 5 in the compilation phase and b was assigned to it on line 6 in the [current] execution phase. As b was undefined at the time of its assignment to a, the value of a is undefined.

To keep our example short and simple, I did not include functions. Note that functions are hoisted in the same way variables are. Functions get hoisted above variables during the compilation phase.

### Problem of overriding function identifiers

If you look at the code below we declare the `fun` function below the `var fun = 3` number. We could suppose that at the end the `fun` identifier is bound to the function. But If you run this code, you’ll see that both asserts pass.

This behavior follows as a direct consequence of the steps taken when registering identifiers:

- in the first phase

  - functions defined with function declarations are created and associated to their identifiers before any code is evaluated: `fun` is bound to a function
  - then the `var fun` variable is discoved but it's already bound, therefore left untouched

- in the second phase:
  - `var fun = 3;` is executed and `function fun(){}` is skipped beacouse already processed.

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

## Exploring how closures work

TODO: see [SOJS_2nd] ch 5.6

## How to use functions: usecases

see [SOJS] ch 4

- Recursion
  Recursion in named functions The pilfered reference problem The callee property 70
- Fun with function as objects
  Recursion with methods 65 Inline named functions 68
  Storing functions 72 ■ Self-memoizing functions 73 Faking array methods 76
- Checking for functions 86

## Arguments and function parameters

see [SOJS] ch 3.4

- A parameter is a variable that we list as part of a function definition.
- An argument is a value that we pass to the function when we invoke it.

When a list of arguments is supplied as a part of a function invocation, these argu- ments are assigned to the parameters in the function definition in the order specified. The first argument gets assigned to the first parameter, the second argument to the second parameter, and so on.

- If **more arguments than parameters** : the “excess” arguments aren’t assigned to parameter names:
- if **more parameters than arguments** : the parameters that have no corresponding argument are set to `undefined`.

```
function practice (ninja, weapon, technique) { ... }

# "katana" is not assigned
practice ("Yoshi", "sword", "shadow sword", "katana");
# "Yoshi" is assigned to ninja, weapon and technique are assigned to undefined
practice ("Yoshi");
```

## Rest Parameters: Variable-length argument lists

NOTE: available since ES6 standard

ref: http://exploringjs.com/es6/ch_parameter-handling.html#_rest-parameters

- Only the last function parameter can be a rest parameter.
- By prefixing the last-named argument of a function with an ellipsis `...`, we turn it into an array called the rest parameters, which contains the remaining passed-in arguments.

```
function format(pattern, ...params) {
    return {pattern, params};
}
format(1, 2, 3);
    // { pattern: 1, params: [ 2, 3 ] }
format();
    // { pattern: undefined, params: [] }
```

## Default Parameters

NOTE: available since ES6 standard

ref: http://exploringjs.com/es6/ch_parameter-handling.html#_default-parameter-values

Scenario:

- a function with a parameter that has **almost** always the same
- JS don't have function overloading, so default params are a possible solution.

Before ES6:

- we checks whether the value of the action parameter is undefined (by using the typeof operator), and if it is, the func- tion sets the value of the action variable to skulking.
- If the action parameter is sent through a function call (it’s not undefined), we keep the value.

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

## Named parameters via destructuring

ref:

- [[ExploringJS - Exploring ES6]](http://exploringjs.com/es6/ch_parameter-handling.html#_named-parameters-via-destructuring)

You can simulate named parameters if you destructure with an object pattern in the parameter list:

```
function selectEntries({ start=0, end=-1, step=1 } = {}) { // (A)
    // The object pattern is an abbreviation of:
    // { start: start=0, end: end=-1, step: step=1 }
    // Use the variables `start`, `end` and `step` here
    console.log(`start = ${start}, end = ${end}, step = ${step}`)
}

selectEntries({ start: 10, end: 30, step: 2 });  // start = 10, end = 30, step = 2
selectEntries({ step: 3 });  // start = 0, end = -1, step = 3
selectEntries({}); // start = 0, end = -1, step = 1
selectEntries(); // start = 0, end = -1, step = 1
```

The `= {}` in line A enables you to call `selectEntries()` without paramters:

```
function selectEntries({ start=0, end=-1} ){console.log(`start = ${start}, end = ${end}, step = ${step}}
//TypeError: Cannot destructure property `start` of 'undefined' or 'null'.
```

WHY? because the first param is undefined and the matching will be tried

## Paramters of a forEach() and destructuring

NOTE: probably you use more the `for-of` loop in ES6 so you can avoid to use the feature described here but it's good to know if you read other code bases.

ref: http://exploringjs.com/es6/ch_parameter-handling.html#_foreach-and-destructuring

First example: destructuring the Arrays in an Array.

```
const items = [ ['foo', 3], ['bar', 9] ];
items.forEach(([word, count]) => {
    console.log(word+' '+count);
});
```

Second example: destructuring the objects in an Array.

```
const items = [
    { word:'foo', count:3 },
    { word:'bar', count:9 },
];
items.forEach(({word, count}) => {
    console.log(word+' '+count);
});
```

## Implicit parameters: arguments

see [SOJS_2nd] ch 4.1.1

Function invocations are usually passed two implicit parameters:

`arguments`:

- a collection of all arguments passed to a function;
- NOTE: with rest parameters, introduced in the preceding chapter, the need for the arguments parameter has been greatly reduced
- (has a `length` property).
- Is not an Array but array notation can be used `arguments[2]`.

`this`:

- the function context
- represent different things, depends on the invocation type

By implicit, we mean that these parameters aren’t explicitly listed in the function signature, but are silently passed to the function and accessible within the function. They can be referenced within the function just like any other explicitly named parameter.

Parametes alias:

- Arguments object is an alias for the function parameters, if we change the arguments object, the change is also reflected in the matching function parameter.
- with `use strict` this behavior is disabled.

## Parameters: Handling an Array returned via a Promise

ref: http://exploringjs.com/es6/ch_parameter-handling.html#_handling-an-array-returned-via-a-promise

## Parametes: Transforming Maps

ref: http://exploringjs.com/es6/ch_parameter-handling.html#_transforming-maps

## Coding style tips: Optional parameters

ref: http://exploringjs.com/es6/ch_parameter-handling.html#_optional-parameters

## Coding style tips: Enforcing a maximum arity

http://exploringjs.com/es6/ch_parameter-handling.html#_enforcing-a-maximum-arity

## Implicit parameters: "this" is the "function context"

**JAVA, CPP Developer WARNING** :

- In such languages, this usually points to an instance of the class within which the method is defined. The `this` is
- But beware! in JavaScript this is true only when invoking a function as a method **it's not the only one way** a function can be invoked.

in JS `this`:

- Represent the function context
- Depends by HOW the function is **INVOKED**

We can invoke a function in four ways:

- As a **function**: `skulk()`, in which the function is invoked in a straightforward manner
- As a **method**: `ninja.skulk()`, which ties the invocation to an object, enabling object-oriented programming
- As a **constructor**: `new Ninja()`, in which a new object is brought into being
- Via the function’s **apply or call methods**: skulk.call(ninja)or skulk.apply(ninja) Here are examples:

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

- a function is invoked using the () operator,
- and the expression to which the () operator is applied doesn’t reference the function as a property of an object. (In that case, we’d have a method invocation, but we discuss that next.)

Strict VS NON Strict mode:

- nonstrict mode: `this` will be the global context (the window object)
- strict mode: `this` will be `undefined`.

### This: invoke as method

see [SOJS] ch 4.2.2

NOTE: this example is simple, the best way to create an object is using the `constructor`

The function is invoked as a method of that object:

- When a function is assigned to a property of an object
- when the invocation occurs by referencing the function using that property
- When we invoke a function as a method of an object, that object becomes `this`, the function context.

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

REF: [SOTJSN2nd] 4.2.3 invocation as a constructor

A constructor is a function like any other functions, the main difference is that we expect to use it with the `new` operator.

When a constructor function is invoked with `new`, a couple of special actions take place:

- A new empty object is created.
- This object is passed to the constructor as the this parameter, and thus becomes the constructor’s function context.
- The newly constructed object is returned as the new operator’s value (with an exception that we’ll get to in short order).

Example:

```js
function Ninja() {
  // A constructor that creates a skulk property on whatever object is the function context.
  this.skulk = function () {
    return this;
  };
}
```

In this example, we create a function named Ninja that we’ll use to construct, well, ninjas. When invoked with the keyword new, an empty object instance is created and passed to the function as its function context, the this parameter. The constructor creates a property named skulk on this object, which is assigned a function, making that function a method of the newly created object.

NOTE: do not to confuse these `function constructors` with `constructor functions`:

- A function constructor enables us to create functions from dynamically created strings.
- Constructor functions, the topic of this section, are functions that we use to create and initialize object instances

The intent of constructors is to initialize the new object that will be created by the function invocation to initial conditions. And although such functions can be called as “normal” functions, or even assigned to object properties in order to be invoked as methods, they’re generally not useful as such.

`constructor functions` return value:

- If the constructor returns an object, that object is returned as the value of the whole new expression, and the newly constructed object passed as this to the constructor is discarded.
- If, however, a nonobject is returned from the constructor, the returned value is ignored, and the newly created object is returned.

Naming Convention:

- Functions and methods are generally named starting with a verb that describes what they do (skulk, creep, sneak, doSomethingWonderful, and so on) and start with a lowercase letter.
- Constructors, on the other hand, are usually named as a noun that describes the object that’s being constructed and start with an uppercase character: Ninja, Samurai, Emperor, Ronin, and so on.

### This: Invoke function with call() and apply()

REF: see [SOJS_2nd] paragraph 4.2.4

Scenario: set "this" explicitly

Usecases:

- browser event handlers
- implement a "foreach", implement a callback system

`apply()`: To invoke a function using its `apply()` method we pass two parameters to apply()

- the object to be used as the function context(this),
- an array of values to be used as the invocation arguments.

The `call()` method is used in a similar manner, except that the arguments are passed directly in the argument list rather than as an array.

Syntax example:

```javascript
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
```

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

- Our iteration function accepts the collection to be iterated over and a callback function.
- Using `call()` the callback is invoked such that the current is the function context.
- The assert test that the function context is correct for each invocation of the callback

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

```javascript
function smallest(array) {
  return Math.min.apply(Math, array);
}

smallest([0, 1, 2, 3]);
```

Also note that we specify the context as being the Math object. This isn’t necessary

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

- The string `"isMoving"` in `Symbol("isMoving")` is called a `description`. It’s helpful for debugging. It’s shown when you write the symbol to console.log(), when you convert it to a string using .toString(), and possibly in error messages. That’s all.

- element[isMoving] is called a **symbol-keyed property** . It’s simply a property whose name is a symbol rather than a string. Apart from that, it is in every way a normal property.

- symbol-keyed properties can’t be accessed using dot syntax, as in `obj.name`. They must be accessed using square brackets.

- It’s trivial to access a symbol-keyed property if you’ve already got the symbol. The above example shows how to get and set element[isMoving], and we could also ask if (isMoving in element) or even delete element[isMoving] if we needed to.

On the other hand, all of that is only possible as long as isMoving is in scope. This makes symbols a mechanism for weak encapsulation: a module that creates a few symbols for itself can use them on whatever objects it wants to, without fear of colliding with properties created by other code.

### Well-known symbols

JavaScript has a set of Symbols already allocated, used to access standard object's properties. They represent internal language behaviors and they can be accessed using the Symbol's properties.

For example : Iteration symbols

- `Symbol.iterator` : A method returning the default iterator for an object. Used by `for...of`.
- `Symbol.asyncIterator` : A method that returns the default AsyncIterator for an object. Used by for `await...of`.

A full references of this Symbols: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol#Well-known_symbols

### Global symbol registry: Shared symbols

Ref: https://developer.mozilla.org/en-US/docs/Glossary/Symbol#Global_symbol_registry

- `Symbol.for("tokenString")` returns a symbol value from the registry,
- `Symbol.keyFor(symbolValue)` returns a token string from the registry;

Each is the other's inverse, so the following is true: `Symbol.keyFor(Symbol.for("tokenString")) == "tokenString"; // true`

### List Symbols of an Object

`Reflect.ownKeys()`

`Object.getOwnPropertySymbols()`:

- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertySymbols

### Symbol usescases

Ref:

- https://hacks.mozilla.org/2015/06/es6-in-depth-symbols/
- https://stackoverflow.com/questions/21724326/what-is-the-motivation-for-bringing-symbols-to-es6

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

## Generators

Refs:

- https://hacks.mozilla.org/2015/05/es6-in-depth-generators/
- https://hacks.mozilla.org/2015/07/es6-in-depth-generators-continued/
- [SOJSN2nd]6.2 Working with generator functions
- [JSINFO](https://javascript.info/generators)

Generator are a new kind of function added to ES6 to simplify code and straighten out the “callback hell”.

```js
function* quips(name) {
  yield "hello " + name + "!";
  yield "i hope you are enjoying the blog posts";
  if (name.startsWith("X")) {
    yield "it's cool how your name starts with X, " + name;
  }
  yield "see you later!";
}
```

What happens when you call the `quips()` generator-function?

```js
> var iter = quips("jorendorff");
  [object Generator]
> iter.next()
  { value: "hello jorendorff!", done: false }
> iter.next()
  { value: "i hope you are enjoying the blog posts", done: false }
> iter.next()
  { value: "see you later!", done: false }
> iter.next()
  { value: undefined, done: true }
```

You can think of generators as processes (pieces of code) that you can pause and resume.

The process is initially paused in line A, `next()` resumes execution, a `yield` inside the function pauses execution.

`Generators functions` are a special type of function, it has a lot in common with functions. But you can see differences right away:

- Regular functions start with `function`, Generator-functions start with `function*`
- a standard function produces at most a single value, while running its code from start to finish
- instead generators produce **multiple values**, on a per request basis, while suspending their execution between these requests.
- `yield` is a keyword, with syntax rather like return. The difference is that while a function (even a generator-function) can only return once, a generator-function can yield any number of times. The yield expression suspends execution of the generator so it can be resumed again later.
- When you call a generator, it doesn’t start running yet. Instead, it returns a paused `Generator object` (called iter in the example above). Specifically, it’s frozen right at the top of the generator-function, just before running its first line of code.
- You can think of this Generator object as a function call, frozen in time.
- Generator are Iterator, they implement the Iterable protocol. `Generator functions` reduce the amount of boilerplate code you need to make your objects iterable.

Generators are not threads:

- When a generator runs, it runs in the same thread as the caller.
- The order of execution is sequential and deterministic, and never concurrent.

So that’s it, that’s the big difference between regular functions and generator-functions. **Regular functions can’t pause themselves**. Generator-functions can.

Generators usecase:

- simplify convoluted loops
- write simpler and more elegant asynchronous code

Generators can play three roles:

- `Iterators (data producers)`: Each yield can return a value via next(), which means that generators can produce sequences of values via loops and recursion. Due to generator objects implementing the interface Iterable, these sequences can be processed by any ECMAScript 6 construct that supports iterables. Two examples are: for-of loops and the spread operator (...).
- `Observers (data consumers)`: yield can also receive a value from next() (via a parameter). That means that generators become data consumers that pause until a new value is pushed into them via next().
- `Coroutines (data producers and consumers)`: Given that generators are pausable and can be both data producers and data consumers, not much work is needed to turn them into coroutines (cooperatively multitasked tasks).

The basic interface of a generator is:

```js
interface Iterable {
    [Symbol.iterator]() : Iterator;
}
interface Iterator {
    next() : IteratorResult;
}
interface IteratorResult {
    value : any;
    done : boolean;
}
```

The full interface of generator objects will be shown later.

### Kind of generators

There are four kinds of generators:

Generator function declarations:

```js
 function* genFunc() { ··· }
 const genObj = genFunc();
```

Generator function expressions:

```js
 const genFunc = function* () { ··· };
 const genObj = genFunc();
```

Generator method definitions in object literals:

```js
 const obj = {
     * generatorMethod() {
         ···
     }
 };
 const genObj = obj.generatorMethod();
```

Generator method definitions in class definitions (class declarations or class expressions):

```js
 class MyClass {
     * generatorMethod() {
         ···
     }
 }
 const myInst = new MyClass();
 const genObj = myInst.generatorMethod();
```

### Is a generator object an iterator or an iterable?

Ref: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#Is_a_generator_object_an_iterator_or_an_iterable

A generator object is both, iterator and iterable:

```js
var aGeneratorObject = (function* () {
  yield 1;
  yield 2;
  yield 3;
})();
typeof aGeneratorObject.next;
// "function", because it has a next method, so it's an iterator
typeof aGeneratorObject[Symbol.iterator];
// "function", because it has an @@iterator method, so it's an iterable
aGeneratorObject[Symbol.iterator]() === aGeneratorObject;
// true, because its @@iterator method returns itself (an iterator), so it's an well-formed iterable
[...aGeneratorObject];
// [1, 2, 3]
```

### Returning from a generator

ref: http://exploringjs.com/es6/ch_generators.html#_returning-from-a-generator

An implicit return is equivalent to returning undefined and it will generates `{ value: undefined, done: true }`:

An explicit return in a generator iterator will generates `{ value: 'my_result', done: true }`:

```js
function* genFuncWithReturn() {
  yield "a";
  yield "b";
  return "my_result";
}

const genObjWithReturn = genFuncWithReturn();
genObjWithReturn.next(); // { value: 'a', done: false }
genObjWithReturn.next(); // { value: 'b', done: false }
genObjWithReturn.next(); // { value: 'my_result', done: true }
```

NOTE: you don't need to return from a generator, if you call `next()` on an Generator iterator after the last `yield` it's equivalent to `return`

Most constructs that work with iterables ignore the value inside the done object:

```js
for (const x of genFuncWithReturn()) {
  console.log(x);
}
// Output:
// a
// b

const arr = [...genFuncWithReturn()]; // ['a', 'b']
```

`yield*`, an operator for making recursive generator calls, does consider values inside done objects. It is explained later.

### How to shut down a generator

Scenario:

- Your `Generator function` need to perfom a `cleanUp()` function at the end of the iteration (ex: closing connections or files, freeing system resources, or just updating the DOM to turn off an “in progress” spinner).
- AND Something goes wrong in your for-of loop or it contains a break or return statement.

A naive implementation could be:

```js
function* produceValues() {
  setup();
  try {
    // ... yield some values ...
  } finally {
    cleanup();
  }
}

for (var value of produceValues()) {
  work(value);
}
```

But the `cleanUp` will be performed only if the errror will happens while yielding values.

Calling `myGenerator.return()` causes the generator to run any finally blocks and then exit, just as if the current yield point had been mysteriously transformed into a return statement.

Note that the `.return()` is not called automatically by the language in all contexts, only in cases where the language uses the iteration protocol. So it is possible for a generator to be garbage collected without ever running its finally block.

How would this feature play out on stage? The generator is frozen in the middle of a task that requires some setup, like building a skyscraper. Suddenly someone throws an error! The for loop catches it and sets it aside. She tells the generator to .return(). The generator calmly dismantles all its scaffolding and shuts down. Then the for loop picks the error back up, and normal exception handling continues.

### Throwing an exception from a generator

If an exception leaves the body of a generator then next() throws it:

```js
function* genFunc() {
  throw new Error("Problem!");
}
const genObj = genFunc();
genObj.next(); // Error: Problem!
```

That means that next() can produce three different “results”:

- For an item x in an iteration sequence, it returns `{ value: x, done: false }`
- For the end of an iteration sequence with a return value z, it returns `{ value: z, done: true }`
- For an exception that leaves the generator body, it throws that exception.

### Generator Usecase: implement a range iterator

Let’s make a simple range iterator that simply counts up from one number to another, like an old-fashioned C for (;;) loop.

```js
// This should "ding" three times
for (var value of range(0, 3)) {
  alert("Ding! at floor #" + value);
}
```

Here’s one solution, using an ES6 class:

```js
class RangeIterator {
  constructor(start, stop) {
    this.value = start;
    this.stop = stop;
  }

  [Symbol.iterator]() {
    return this;
  }

  next() {
    var value = this.value;
    if (value < this.stop) {
      this.value++;
      return { done: false, value: value };
    } else {
      return { done: true, value: undefined };
    }
  }
}

// Return a new iterator that counts up from 'start' to 'stop'.
function range(start, stop) {
  return new RangeIterator(start, stop);
}
```

[See this code in action](http://codepen.io/anon/pen/NqGgOQ)

A lot of code! We can replace the same code with a 4-line generator:

```js
function* range(start, stop) {
  for (var i = start; i < stop; i++) yield i;
}
```

[See this code in action](http://codepen.io/anon/pen/mJewga)

This is possible because generators are iterators:

- All generators have a built-in implementation of .next() and [Symbol.iterator]().
- You just write the looping behavior.

### Generator Usecase: Making any object iterable

To Make any object iterable:

- Just write a generator-function that traverses `this`, yielding each value as it goes.
- Then install that generator-function as the [Symbol.iterator] method of the object.
- NOTE: Generators reduce the boilerplate code needed to implement the Iterable protocol

```js
class Matrix {
  constructor() {
    this.matrix = [
      [1, 2, 9],
      [5, 3, 8],
      [4, 6, 7],
    ];
  }

  *[Symbol.iterator]() {
    for (let row of this.matrix) {
      for (let cell of row) {
        yield cell;
      }
    }
  }
}
```

The usage of such a class would be:

```js
let matrix = new Matrix();

for (let cell of matrix) {
  console.log(cell);
}
```

Which would output:

```
1
2
9
....
```

### Generator Usecase: Simplifying array-building functions.

Suppose you have a function that returns an array of results each time it’s called, like this one:

```js
// Divide the one-dimensional array 'icons'
// into arrays of length 'rowLength'.
function splitIntoRows(icons, rowLength) {
  var rows = [];
  for (var i = 0; i < icons.length; i += rowLength) {
    rows.push(icons.slice(i, i + rowLength));
  }
  return rows;
}
```

Generators make this kind of code a bit shorter:

```js
function* splitIntoRows(icons, rowLength) {
  for (var i = 0; i < icons.length; i += rowLength) {
    yield icons.slice(i, i + rowLength);
  }
}
```

The only difference in behavior is that instead of computing all the results at once and returning an array of them, this returns an iterator, and the results are computed one by one, on demand.

### Generator Usecase: unlimited size results

You can’t build an infinite array. But you can return a generator that generates an endless sequence, and each caller can draw from it however many values they need.

### Generator Usecase: Refactoring complex loops

Do you have a huge ugly function? Would you like to break it into two simpler parts? Generators are a new knife to add to your refactoring toolkit. When you’re facing a complicated loop, you can factor out the part of the code that produces data, turning it into a separate generator-function. Then change the loop to say for (var data of myNewGenerator(args)).

### Generator Usecase: Tools for working with iterables

ES6 does not provide an extensive library for filtering, mapping, and generally hacking on arbitrary iterable data sets. But generators are great for building the tools you need with just a few lines of code.

For example, suppose you need an equivalent of Array.prototype.filter that works on DOM NodeLists, not just Arrays. Piece of cake:

```js
function* filter(test, iterable) {
  for (var item of iterable) {
    if (test(item)) yield item;
  }
}
```

### Generator Usecase: iterating over properties of an object

ref: http://exploringjs.com/es6/ch_generators.html#objectEntries_generator

### You can only yield in generators

ref: http://exploringjs.com/es6/ch_generators.html#_you-can-only-yield-in-generators

A significant limitation of generators is that you can only yield while you are (statically) inside a generator function. That is, yielding in callbacks doesn’t work:

```js
function* genFunc() {
    ['a', 'b'].forEach(x => yield x); // SyntaxError
}
```

yield is not allowed inside non-generator functions, which is why the previous code causes a syntax error. In this case, it is easy to rewrite the code so that it doesn’t use callbacks (as shown below). But unfortunately that isn’t always possible.

```js
function* genFunc() {
  for (const x of ["a", "b"]) {
    yield x; // OK
  }
}
```

The upside of this limitation is explained later: it makes generators easier to implement and compatible with event loops.

### Generator Composition and Recursion via `yield*`

ref:

- http://exploringjs.com/es6/ch_generators.html#_recursion-via-yield
- https://javascript.info/generators#generator-composition

You can only use yield within a generator function. Therefore, if you want to implement a recursive algorithm with generator, you need a way to call one generator from another one. This section shows that that is more complicated than it sounds, which is why ES6 has a special operator, `yield*`, for this. For now, I only explain how `yield*` works if both generators produce output, I’ll later explain how things work if input is involved.

The `yield*` directive delegates the execution to another generator. This term means that `yield*` gen iterates over the generator gen and transparently forwards its yields outside. As if the values were yielded by the outer generator.

NOTE: operand of `yield*` can be any **iterable**

How can one generator recursively call another generator? Let’s assume you have written a generator function foo:

```js
function* foo() {
  yield "a";
  yield "b";
}
```

How would you call foo from another generator function bar? The following approach does not work!

```js
function* bar() {
  yield "x";
  foo(); // does nothing!
  yield "y";
}
```

Calling foo() returns an object, but does not actually execute foo(). That’s why ECMAScript 6 has the operator `yield*` for making recursive generator calls:

```js
function* bar() {
  yield "x";
  yield* foo();
  yield "y";
}

// Collect all values yielded by bar() in an array
const arr = [...bar()];
// ['x', 'a', 'b', 'y']
```

Internally, `yield*` works roughly as follows:

```js
function* bar() {
  yield "x";
  for (const value of foo()) {
    yield value;
  }
  yield "y";
}
```

The operand of `yield*` does not have to be a generator object, it can be any iterable:

```js
function* bla() {
  yield "sequence";
  yield* ["of", "yielded"];
  yield "values";
}

const arr = [...bla()];
// ['sequence', 'of', 'yielded', 'values']
```

### Communicating with a generator - next(arg)

Ref:

- [JSINFO](https://javascript.info/generators#yield-is-a-two-way-street)
- [SOTJSN2nd] 6.2.3 Communicating with a generator

Until this moment, generators were similar to iterable objects, with a special syntax to generate values. But in fact they are much more powerful and flexible.

That’s because yield is a two-way street: it not only returns the result to the outside, but also can pass the value inside the generator.

To do so, we should call generator.next(arg), with an argument. That argument becomes the result of yield:

```js
function* gen() {
  let ask1 = yield "2 + 2 = ?";

  alert(ask1); // 4

  let ask2 = yield "3 * 3 = ?";

  alert(ask2); // 9
}

let generator = gen();

alert(generator.next().value); // "2 + 2 = ?"

alert(generator.next(4).value); // "3 * 3 = ?"

alert(generator.next(9).done); // true
```

![](../images/js-generators-next-arg.png)

### `yield*` considers end-of-iteration values

Most constructs that support iterables ignore the value included in the end-of-iteration object (whose property done is true). Generators provide that value via return. The result of `yield*` is the end-of-iteration value:

NOTE: this example not so easy to understand

```js
function* genFuncWithReturn() {
  yield "a";
  yield "b";
  return "The result";
}
function* logReturned(genObj) {
  const result = yield* genObj; // result has the value of the return statement not the of the next() method
  console.log(result); // (A)
}
```

If we want to get to line A, we first must iterate over all values yielded by logReturned():

```js
> a = [...logReturned(genFuncWithReturn())]
The result // is the row log at line A

// the value of a is [ 'a', 'b' ]
```

### Generator Throw

Ref: https://javascript.info/generators#generator-throw

As we observed in the examples above, the outer code may pass a value into the generator, as the result of yield.
…But it can also initiate (throw) an error there. That’s natural, as an error is a kind of result.

To pass an error into a yield, we should call `generator.throw(err)`. In that case, the err is thrown in the line with that yield.

For instance, here the yield of "2 + 2 = ?" leads to an error:

```js
function* gen() {
  try {
    let result = yield "2 + 2 = ?"; // (1)
    console.log(
      "The execution does not reach here, because the exception is thrown above"
    );
  } catch (e) {
    console.log(e); // shows the error
  }
}

let generator = gen();

let question = generator.next().value;

let throw_return = generator.throw(
  new Error("The answer is not found in my database")
); // (2)

console.log("error is catched");
```

The error, thrown into the generator at line (2) leads to an exception in line (1) with yield. In the example above, try..catch catches it and shows it.
If we don’t catch it, then just like any exception, it “falls out” the generator into the calling code.
The current line of the calling code is the line with generator.throw, labelled as (2).

If we don’t catch the error there, then, as usual, it falls through to the outer calling code (if any) and, if uncaught, kills the script:

```js
function* generate() {
  let result = yield "2 + 2 = ?"; // Error in this line
}

let generator = generate();

let question = generator.next().value;

try {
  generator.throw(new Error("The answer is not found in my database"));
} catch (e) {
  alert(e); // shows the error
}
```

### Generator example:

ref: http://exploringjs.com/es6/ch_generators.html#_iterating-over-trees

Iterating over a tree with recursion is simple, writing an iterator for a tree with traditional means is complicated. That’s why generators shine here: they let you implement an iterator via recursion. As an example, consider the following data structure for binary trees. It is iterable, because it has a method whose key is Symbol.iterator. That method is a generator method and returns an iterator when called.

```
class BinaryTree {
    constructor(value, left=null, right=null) {
        this.value = value;
        this.left = left;
        this.right = right;
    }

    /** Prefix iteration */
    * [Symbol.iterator]() {
        yield this.value;
        if (this.left) {
            yield* this.left;
            // Short for: yield* this.left[Symbol.iterator]()
        }
        if (this.right) {
            yield* this.right;
        }
    }
}
```

The following code creates a binary tree and iterates over it via for-of:

```
const tree = new BinaryTree('a',
    new BinaryTree('b',
        new BinaryTree('c'),
        new BinaryTree('d')),
    new BinaryTree('e'));

for (const x of tree) {
    console.log(x);
}
// Output:
// a
// b
// c
// d
// e
```

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator

# Modularity in JS

In JS we achive modularity with:

- Modules
- Prototype and classes

## Prototype

Ref:

- [JSINFO](https://javascript.info/prototypes)
- [MDN Object prototypes - Basic](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)
- [MDN Advanced](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain#Using_prototypes_in_JavaScript)
- [YDKJSY: this & Object Prototypes](https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch5.md)
- [JSFIP Prototype chains](https://exploringjs.com/impatient-js/ch_proto-chains-classes.html#prototype-chains)
- [FreeCodeCamp Prototype intro](https://www.freecodecamp.org/news/a-guide-to-prototype-based-class-inheritance-in-javascript-84953db26df0/)

### CheatSheet and TL;DR

Def: A prototype is an object to which the search for a particular property can be delegated to.

TODO elencare tutti i modi di usare la prototype inheritance

EVERY OBJECT:

- has a constructor property
- has a prototype that is either null or an object
- can have "own properties" (Non-inherited properties)
- if an object doesn't have a property JS looks up in the object prototype

ONLY FUNCTIONS:

- have a prototype property
- Object.setPrototypeOf (obj.\_\_proto=... is deprecated)
- Object.create(proto[, descriptors]) – creates an empty object with given proto as [[Prototype]] and optional property descriptors.
- Classes are syntactical sugar over JS https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes

WARNIGN: It's important to understand that there is a distinction between an object's prototype (available via Object.getPrototypeOf(obj), or via the deprecated **proto** property) and the prototype property on constructor functions. The former is the property on each instance, and the latter is the property on the constructor. That is, Object.getPrototypeOf(new Foobar()) refers to the same object as Foobar.prototype.

### Intro

In programming, we often want to take something and extend it.

A prototype is an object to which the search for a particular property can be delegated to. Prototypes serve a similar purpose to that of classes in classical object-oriented languages.

For instance, we have a user object with its properties and methods, and want to make admin and guest as slightly modified variants of it. We’d like to reuse what we have in user, not copy/reimplement its methods, just build a new object on top of it.

JavaScript objects use prototype-based inheritance. Its design is logically similar (but different in implementation) from class inheritance in strictly Object Oriented Programming languages.

It can be loosely described by saying that when methods or properties are attached to object’s prototype they become available for use on that object and its descendants. But this process often takes place behind the scenes.

When writing code, you will not even need to touch the `prototype` property directly. When executing the `split` method, you would call it directly from a string literal as: `”hello”.split(“e”)` or from a variable: `string.split(“,”)`;

When you use class and extends keywords internally JavaScript will still use prototype-based inheritance. It just simplifies the syntax. Perhaps this is why it’s important to understand how prototype-based inheritance works. It’s still at the core of the language design.

This is why in many tutorials you will see String.prototype.split written instead of just String.split. This means that there is a method split that can be used with objects of type string because it is attached to that object’s prototype property.

Note: ES6 Proxies are outside of our discussion scope in this section, but everything we discuss here about normal [[Get]] and [[Put]] behavior does not apply if a Proxy is involved.

### Object's prototype

Prototypal inheritance is a language feature that helps in that.

`[[Prototype]`: In JavaScript, every objects have a special hidden property `[[Prototype]]` (as named in the specification), that is either null or references another object. That object is called “a prototype”.

This property is HIDDEN, to manipulate it we use:

- Object.getPrototypeOf
- Object.setPrototypeOf

GET

- `myObject.__proto__` **DEPRECATED**
- `Object.getPrototypeOf(obj: Object) : Object`

SET

- `myObject.__proto__ = ....` **DEPRECATED**
- `Object.create(proto: Object, [propertiesObject: Object]) : Object` (BEST way when you create an object)
  - prepertiesObjects: property descriptors to be added
- `Object.setPrototypeOf`
- the `new` operator

Ref: [MDN Object.create](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create)

The prototype is a little bit “magical”. When we want to read a property from object, and it’s missing, JavaScript automatically takes it from the prototype. In programming, such thing is called “prototypal inheritance”. Many cool language features and programming techniques are based on it.

```js
let animal = {
  eats: true,
};
let rabbit = {
  jumps: true,
};

rabbit.__proto__ = animal; // (*)

// we can find both properties in rabbit now:
alert(rabbit.eats); // true (**)
alert(rabbit.jumps); // true
```

If we later add a method to animal rabbit will inherit it:

```js
animal.walk = function () {
  alert("Animal walk");
};
rabbit.walk();
```

The prototype chain can be longer:

```js
let animal = {
  eats: true,
  walk() {
    alert("Animal walk");
  },
};

let rabbit = {
  jumps: true,
  __proto__: animal,
};

let longEar = {
  earLength: 10,
  __proto__: rabbit,
};

// walk is taken from the prototype chain
longEar.walk(); // Animal walk
alert(longEar.jumps); // true (from rabbit)
```

what happens is:

- The js engine initially checks to see if the longEar object has a walk() method available on it and it doesn't.
- So the js engine checks to see if the longEar's prototype object has a walk() method available on it.
- It doesn't, then the browser checks rabbit's prototype object's prototype object, and it has. So the method is called, and all is good!

![](../images/js_prototype_long_chain.png)

There are only two limitations:

- The references can’t go in circles. JavaScript will throw an error if we try to assign **proto** in a circle.
- The value of **proto** can be either an object or null. Other types are ignored.
- Also it may be obvious, but still: there can be only one [[Prototype]]. An object may not inherit from two others.

Given that a prototype object can have a prototype itself, we get a chain of objects – the so-called `prototype chain`.

![](../images/js_prototype_chain.svg)

Prototypes are JavaScript’s only inheritance mechanism: each object has a prototype that is either null or an object.

### This and Prototype

REF: https://javascript.info/prototype-inheritance#the-value-of-this

```js
let user = {
  name: "John",
  surname: "Smith",

  set fullName(value) {
    [this.name, this.surname] = value.split(" ");
  },

  get fullName() {
    return `${this.name} ${this.surname}`;
  },
};

let admin = {
  __proto__: user,
  isAdmin: true,
};

alert(admin.fullName); // John Smith (*)

// setter triggers!
admin.fullName = "Alice Cooper"; // (**)
```

### Setting & Shadowing Properties. Inherited Setters

Refs:

- https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch5.md#setting--shadowing-properties
- https://javascript.info/prototype-inheritance#writing-doesn-t-use-prototype

An interesting question may arise in the example above: what’s the value of this inside `set fullName(value)`? Where are the properties `this.name` and `this.surname` written: into user or admin?

The answer is simple: this is not affected by prototypes at all.

No matter where the method is found: in an object or its prototype. In a method call, this is always the object before the dot.

So, the setter call admin.fullName= uses admin as this, not user.

That is actually a super-important thing, because we may have a big object with many methods, and have objects that inherit from it. And when the inheriting objects run the inherited methods, they will modify only their own states, not the state of the big object.

For instance, here animal represents a “method storage”, and rabbit makes use of it.

The call rabbit.sleep() sets this.isSleeping on the rabbit object:

```js
// animal has methods
let animal = {
  walk() {
    if (!this.isSleeping) {
      alert(`I walk`);
    }
  },
  sleep() {
    this.isSleeping = true;
  },
};

let rabbit = {
  name: "White Rabbit",
  __proto__: animal,
};

// modifies rabbit.isSleeping
rabbit.sleep();

alert(rabbit.isSleeping); // true
alert(animal.isSleeping); // undefined (no such property in the prototype)
```

If we had other objects, like bird, snake, etc., inheriting from animal, they would also gain access to methods of animal. But this in each method call would be the corresponding object, evaluated at the call-time (before dot), not animal. So when we write data into this, it is stored into these objects.

As a result, methods are shared, but the object state is not.

### More on setting a property

We will now revisit this situation more completely.

```
myObject.foo = "bar";
```

If the myObject object already has a normal data accessor property called foo directly present on it, the assignment is as simple as changing the value of the existing property.

If foo is not already present directly on myObject, the [[Prototype]] chain is traversed, just like for the [[Get]] operation. If foo is not found anywhere in the chain, the property foo is added directly to myObject with the specified value, as expected.

However, if foo is already present somewhere higher in the chain, nuanced (and perhaps surprising) behavior can occur with the myObject.foo = "bar" assignment. We'll examine that more in just a moment.

If the property name foo ends up both on myObject itself and at a higher level of the [[Prototype]] chain that starts at myObject, this is called shadowing. The foo property directly on myObject shadows any foo property which appears higher in the chain, because the myObject.foo look-up would always find the foo property that's lowest in the chain.

As we just hinted, shadowing foo on myObject is not as simple as it may seem. We will now examine three scenarios for the myObject.foo = "bar" assignment when foo is not already on myObject directly, but is at a higher level of myObject's [[Prototype]] chain:

1. If a normal data accessor (see Chapter 3) property named foo is found anywhere higher on the [[Prototype]] chain, and it's not marked as read-only (writable:false) then a new property called foo is added directly to myObject, resulting in a shadowed property.
2. If a foo is found higher on the [[Prototype]] chain, but it's marked as read-only (writable:false), then both the setting of that existing property as well as the creation of the shadowed property on myObject are disallowed. If the code is running in strict mode, an error will be thrown. Otherwise, the setting of the property value will silently be ignored. Either way, no shadowing occurs.
3. If a foo is found higher on the [[Prototype]] chain and it's a setter (see Chapter 3), then the setter will always be called. No foo will be added to (aka, shadowed on) myObject, nor will the foo setter be redefined.
   Most developers assume that assignment of a property ([[Put]]) will always result in shadowing if the property already exists higher on the [[Prototype]] chain, but as you can see, that's only true in one (#1) of the three situations just described.

If you want to shadow foo in cases #2 and #3, you cannot use = assignment, but must instead use Object.defineProperty(..) (see Chapter 3) to add foo to myObject.

Note: Case #2 may be the most surprising of the three. The presence of a read-only property prevents a property of the same name being implicitly created (shadowed) at a lower level of a [[Prototype]] chain. The reason for this restriction is primarily to reinforce the illusion of class-inherited properties. If you think of the foo at a higher level of the chain as having been inherited (copied down) to myObject, then it makes sense to enforce the non-writable nature of that foo property on myObject. If you however separate the illusion from the fact, and recognize that no such inheritance copying actually occurred (see Chapters 4 and 5), it's a little unnatural that myObject would be prevented from having a foo property just because some other object had a non-writable foo on it. It's even stranger that this restriction only applies to = assignment, but is not enforced when using Object.defineProperty(..).

Shadowing with methods leads to ugly explicit pseudo-polymorphism (see Chapter 4) if you need to delegate between them. Usually, shadowing is more complicated and nuanced than it's worth, so you should try to avoid it if possible. See Chapter 6 for an alternative design pattern, which among other things discourages shadowing in favor of cleaner alternatives.

Shadowing can even occur implicitly in subtle ways, so care must be taken if trying to avoid it. Consider:

```js
var anotherObject = {
  a: 2,
};

var myObject = Object.create(anotherObject);

anotherObject.a; // 2
myObject.a; // 2

anotherObject.hasOwnProperty("a"); // true
myObject.hasOwnProperty("a"); // false

myObject.a++; // oops, implicit shadowing!

anotherObject.a; // 2
myObject.a; // 3

myObject.hasOwnProperty("a"); // true
```

Though it may appear that `myObject.a++` should (via delegation) look-up and just increment the anotherObject.a property itself in place, instead the ++ operation corresponds to `myObject.a = myObject.a + 1`. The result is [[Get]] looking up a property via [[Prototype]] to get the current value 2 from `anotherObject.a`, incrementing the value by one, then [[Put]] assigning the 3 value to a new shadowed property a on myObject. Oops!

Be very careful when dealing with delegated properties that you modify. If you wanted to increment `anotherObject.a`, the only proper way is `anotherObject.a++`.

### Constructor Function

All functions have a prototype property that initially references an empty object:

- This property doesn’t serve much purpose until the function is used as a constructor (using the `new` operator).
- this empty object's prototype is `Object.prototype`, so it inherits from Object
- The prototype object initially has only one property, `constructor`, that references back to the function (we will see how it is used)

```js
function f() {}
Object.getPrototypeOf(f.prototype) === Object.prototype;
```

NOTE:

- It's important to understand that there is a distinction between an object's prototype (available via `Object.getPrototypeOf(obj)`, or via the deprecated `__proto__` property) and the prototype property on constructor functions.
- The former is the property on each instance, and the latter is the property on the constructor. That is, Object.getPrototypeOf(new Foobar()) refers to the same object as Foobar.prototype.
- REF: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes

Now we will see how JS use the function prototype property to create and initialize an object.

For example we define a seemingly donothing function named `Ninja` that we’ll invoke in two ways:

- as a “normal” function, const ninja1 = Ninja();
- and as a constructor, const ninja2 = new Ninja();.

```js
function Ninja() {}
Ninja.prototype.swingSword = function () {
  return true;
};

const ninja1 = Ninja();

//As expected a function without an explicit return statement, returns undefined
assert(ninja1 === undefined, "No instance of Ninja created.");

// With new something different happen, it return an object
const ninja2 = new Ninja();
assert(
  ninja2 && ninja2.swingSword && ninja2.swingSword(),
  "Instance exists and method is callable."
);

//Ninja.prototype is the ninja2 prototype object
Object.getPrototypeOf(ninja2) === Ninja.prototype;

// ninja2 and ninja3 have the same prototype
const ninja3 = new Ninja();
Object.getPrototypeOf(ninja2) === Object.getPrototypeOf(ninja3);
```

When we call the function via the new operator, invoking it as a constructor, and something completely different happens:

- The function is once again called, but this time a newly allocated object has been created
- and it is set as the context of the function (and is accessible through the this keyword).
- The result returned from the new operator is a reference to this new object
- that object has a `swingSword` method that we can call
- the prototype of the newly constructed object is set to the object referenced by the constructor function’s prototype property.

Notice that all objects created with the Ninja constructor will have access to the swingSword method. Now that’s code reuse!

![](../images/js_prototype_ninja.png)

IMPORTANT:

- The prototype property is one of the most confusingly-named parts of JavaScript — you might think that this points to the prototype object of the current object, but it doesn't (that's an internal object that can be accessed by `__proto__`, remember?). prototype instead is a property containing an object on which you define members that you want to be inherited.
- Ref: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes

### Approximate private variables with closures and Prototype

### Example and problems with prototype and references

Ref: https://medium.com/better-programming/prototypes-in-javascript-5bba2990e04b

```js
//Create an empty constructor function
function Person() {}
//Add property name, age to the prototype property of the Person constructor function
Person.prototype.name = "Ashwin";
Person.prototype.age = 26;
//Arrays are of reference type in JavaScript
Person.prototype.friends = ["Jadeja", "Vijay"];
Person.prototype.sayName = function () {
  console.log(this.name);
};

//Create an object using the Person constructor function
var person1 = new Person();

//Access the name property using the person object
console.log(person1.name); // Output" Ashwin

var person2 = new Person();
//Access the name property using the person2 object
console.log(person2.name); // Output: Ashwin

//Now, let’s define a property name on the person1 object
person1.name = "Anil";
console.log(person1.name); //Output: Anil
console.log(person2.name); //Output: Ashwin
```

- Here person1.name outputs “Anil”. As mentioned earlier, the JavaScript engine first tries to find the property on the object itself. In this case, name property is present on the object person1 itself, hence JavaScript engines outputs the value of name property of person1.
- In the case of person2, the name property is not present on the object. Hence, it outputs person2’s prototype object’s property name.

The code above is doing what we expect but let's see what happen if we try to change person1.friend array:

```js
//Add a new element to the friends array
person1.friends.push("Amit");

console.log(person1.friends); // Output: "Jadeja, Vijay, Amit"
console.log(person2.friends); // Output: "Jadeja, Vijay, Amit"
```

PROBLEM: we are changing also person2's friends! This happens because we are referncing the same array from the prototype. We are not setting a new property as with `name` we are updating the same array.

To solve the problems with the prototype and the problems with the constructor, we can combine both the constructor and function:

- Problem with the constructor function: Every object has its own instance of the function
- Problem with the prototype: Modifying a property using one object reflects the other object also

To solve both problems, we can define all the object-specific properties inside the constructor and all shared properties and methods inside the prototype as shown below:

```js
//Define the object specific properties inside the constructor
function Human(name, age) {
  (this.name = name), (this.age = age), (this.friends = ["Jadeja", "Vijay"]);
}
//Define the shared properties and methods using the prototype
Human.prototype.sayName = function () {
  console.log(this.name);
};
//Create two objects using the Human constructor function
var person1 = new Human("Virat", 31);
var person2 = new Human("Sachin", 40);

//Lets check if person1 and person2 have points to the same instance of the sayName function
console.log(person1.sayName === person2.sayName); // true

//Let's modify friends property and check
person1.friends.push("Amit");

console.log(person1.friends); // Output: "Jadeja, Vijay, Amit"
console.log(person2.friends); //Output: "Jadeja, Vijay"
```

Here as we have wanted each object to have their own name, age, and friends property. Hence, we have defined these properties inside the constructor using this. However, as sayName is defined on the prototype object, it will be shared among all the objects.
In the above example, the friend’s property of person2 did not change on changing the friends' property of person1.

![](../images/js_prototype_example1.png)

### Example: Problem when you replace a prototype

You can change the reference to a function's prototype but it can cause strange behaviours if you already create some object with that function: you could end up with objects created with the same function that behaves differently (see example below).

The reference between an object and the function’s prototype is established at
the time of object instantiation. Newly created objects will have a reference to the new prototype and will have access to the pierce method, whereas the old, pre-prototype-change objects keep their original prototype, happily swinging their swords.

```js
function Ninja() {
  this.swung = true;
}
const ninja1 = new Ninja();

// !! Change the constructor function prototype
Ninja.prototype.swingSword = function () {
  return this.swung;
};

Ninja.prototype = {
  pierce: function () {
    return true;
  },
};

const ninja2 = new Ninja();

//
ninja1.pierce(); // Uncaught TypeError: ninja1.pierce is not a function
ninja2.pierce(); //true
```

![](../images/js_redefine_prototype.png)

### instanceof and Constructor property

REF: [SOJSN2ND] 7.3.2 The instanceof operator

`instanceof` operator checks whether the prototype of the argument function is in the prototype chain of the object.

```js
function Person() {}
function Admin() {}
Admin.prototype = new Person();
admin = new Admin();
admin instanceof Person; // true
```

![](../images/js_instance_of_example.png)

```js
> [] instanceof Array
true
> 2 instanceof Array
false
```

THE INSTANCEOF CAVEAT: if we change the prototype of Admin the result is false:

```js
function Person() {}
function Admin() {}
Admin.prototype = new Person();
admin = new Admin();
admin instanceof Person; // true

Admin.prototype = {};
admin2 = new Admin();
admin2 instanceof Person; // false
```

This will surprise us only if we cling to the inaccurate assumption that the instanceof operator tells us whether an instance was created by a particular function constructor. If, on the other hand, we take the real semantics of the instanceof operator—that it checks only whether the prototype of the function on the right side is in the prototype chain of the object on the left side—we won’t be surprised.

NOTE: Many developer belive that each object in JavaScript has an implicit property named `constructor` that references the constructor function that was used to create the object. And because the prototype is a property of the constructor, each object has a way to find its prototype.

This behavior is quite standard but is not reliable.
`.constructor` is extremely unreliable, and an unsafe reference to rely upon in your code.

- [REF](https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch5.md#mechanics)

For example:

```js
function Foo() {
  /* .. */
}

Foo.prototype = {
  /* .. */
}; // create a new prototype object

var a1 = new Foo();
a1.constructor === Foo; // false!
a1.constructor === Object; // true!
```

Especially when you create multiple level of prototypal inheritance:

- [REF](https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch5.md#constructor-redux)

**NOTE**: _ONLY functions_ have a prototype property, _EVERY object_ has a
costructor property!

### Writing doesn’t use prototype

The prototype is only used for reading properties.

Write/delete operations work directly with the object.

In the example below, we assign its own walk method to rabbit:

```js
let animal = {
  eats: true,
  walk() {
    /* this method won't be used by rabbit */
  },
};

let rabbit = {
  __proto__: animal,
};

rabbit.walk = function () {
  alert("Rabbit! Bounce-bounce!");
};

rabbit.walk(); // Rabbit! Bounce-bounce!
```

From now on, rabbit.walk() call finds the method immediately in the object and executes it, without using the prototype:

Accessor properties are an exception, as assignment is handled by a setter function. So writing to such a property is actually the same as calling a function.

For that reason admin.fullName works correctly in the code below:

```js
let user = {
  name: "John",
  surname: "Smith",

  set fullName(value) {
    [this.name, this.surname] = value.split(" ");
  },

  get fullName() {
    return `${this.name} ${this.surname}`;
  },
};

let admin = {
  __proto__: user,
  isAdmin: true,
};

alert(admin.fullName); // John Smith (*)

// setter triggers!
admin.fullName = "Alice Cooper"; // (**)
```

Here in the line (\*) the property admin.fullName has a getter in the prototype user, so it is called. And in the line (\*\*) the property has a setter in the prototype, so it is called.

HowTo call a prototype method that is hidden by an object method:

- `Person.prototype.getName.call(this);`
- Ref: https://stackoverflow.com/questions/11542192/override-function-in-javascript

### [Advanced] for..in loop

https://javascript.info/prototype-inheritance#for-in-loop

The for..in loop iterates over inherited properties too.
If that’s not what we want, and we’d like to exclude inherited properties, there’s a built-in method obj.hasOwnProperty(key): it returns true if obj has its own (not inherited) property named key.

### [DEPRECATED] **proto**

Ref:

- https://javascript.info/prototype-methods
- https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes

`__proto__` is a historical getter/setter for [[Prototype]]

Please note that `__proto__` is not the same as [[Prototype]]. It’s a getter/setter for it.

It exists for historical reasons. In modern language it is replaced with functions `Object.getPrototypeOf/Object.setPrototypeOf` that also get/set the prototype. We’ll study the reasons for that and these functions later.

By the specification, **proto** must only be supported by browsers, but in fact all environments including server-side support it. For now, as **proto** notation is a little bit more intuitively obvious, we’ll use it in the examples.

## "(Prototypal) Inheritance"

We traditionally think of "inheritance" as being a relationship between two "classes", rather than between "class" and "instance". Until now we saw only this kind of relationship.

In JS you can achive inheritance creating setting up Prototype Chain (prototype linkage). It's important to notice that it's still a linkage between objects, that create a delegation mechanism.

here's the typical "prototype style" code that creates such links:

```js
function Foo(name) {
  this.name = name;
}

Foo.prototype.myName = function () {
  return this.name;
};

function Bar(name, label) {
  Foo.call(this, name);
  this.label = label;
}

// here, we make a new `Bar.prototype`
// linked to `Foo.prototype`
Bar.prototype = Object.create(Foo.prototype);

// Beware! Now `Bar.prototype.constructor` is gone,
// and might need to be manually "fixed" if you're
// in the habit of relying on such properties!

Bar.prototype.myLabel = function () {
  return this.label;
};

var a = new Bar("a", "obj a");

a.myName(); // "a"
a.myLabel(); // "obj a"
```

The important part is `Bar.prototype = Object.create( Foo.prototype )`. `Object.create(..)` creates a "new" object out of thin air, and links that new object's internal [[Prototype]] to the object you specify (Foo.prototype in this case).

In other words, that line says: "make a new 'Bar dot prototype' object that's linked to 'Foo dot prototype'."

When function `Bar() { .. }` is declared, Bar, like any other function, has a .prototype link to its default object. But that object is not linked to Foo.prototype like we want. So, we create a new object that is linked as we want, effectively throwing away the original incorrectly-linked object.

Note: A common mis-conception/confusion here is that either of the following approaches would also work, but they do not work as you'd expect:

```js
// doesn't work like you want!
Bar.prototype = Foo.prototype;

// works kinda like you want, but with
// side-effects you probably don't want :(
Bar.prototype = new Foo();
```

`Bar.prototype = Foo.prototype` doesn't create a new object for `Bar.prototype` to be linked to. It just makes `Bar.prototype` be another reference to `Foo.prototype`, which effectively links Bar directly to the same object as Foo links to: `Foo.prototype`. This means when you start assigning, like Bar.prototype.myLabel = ..., you're modifying not a separate object but the shared Foo.prototype object itself, which would affect any objects linked to Foo.prototype. This is almost certainly not what you want. If it is what you want, then you likely don't need Bar at all, and should just use only Foo and make your code simpler.

`Bar.prototype = new Foo()` does in fact create a new object which is duly linked to `Foo.prototype` as we'd want. But, it uses the Foo(..) "constructor call" to do it. If that function has any **side-effects** (such as logging, changing state, registering against other objects, adding data properties to this, etc.), those side-effects happen at the time of this linking (and likely against the wrong object!), rather than only when the eventual Bar() "descendants" are created, as would likely be expected.

So, we're left with using Object.create(..) to make a new object that's properly linked, but without having the side-effects of calling Foo(..). The slight downside is that we have to create a new object, throwing the old one away, instead of modifying the existing default object we're provided.

ES6: It would be nice if there was a standard and reliable way to modify the linkage of an existing object. Prior to ES6, there's a non-standard and not fully-cross-browser way, via the .**proto** property, which is settable. ES6 adds a `Object.setPrototypeOf(..)` helper utility, which does the trick in a standard and predictable way.

Compare the pre-ES6 and ES6-standardized techniques for linking Bar.prototype to Foo.prototype, side-by-side:

```js
// pre-ES6
// throws away default existing `Bar.prototype`
Bar.prototype = Object.create(Foo.prototype);

// ES6+
// modifies existing `Bar.prototype`
Object.setPrototypeOf(Bar.prototype, Foo.prototype);
```

Ignoring the slight performance disadvantage (throwing away an object that's later garbage collected) of the Object.create(..) approach, it's a little bit shorter and may be perhaps a little easier to read than the ES6+ approach. But it's probably a syntactic wash either way.

## Classes

REF: [SOJSN2ND] 7.4.1 Using the class keyword

ES6 introduces a new class keyword that provides a much more elegant way of creating objects and implementing inheritance than manually implementing it ourselves with prototypes.

```js
//Defines a constructor function that will be called when we call the class with the keyword new
class Ninja {
  constructor(name) {
    this.name = name;
  }
  //Defines an additional method accessible to all Ninja instances
  swingSword() {
    return true;
  }
}
```

- CONSTRUCTOR: We can explicitly define a constructor function: it will be invoked when instantiating a Ninja, the newly created instance with the this keyword, and we can easily add new properties, such as the name property.
- METHODS: we can also define methods that will be accessible to all Ninja instances (`swingSword()`)
- we can create a Ninja instance by calling the Ninja class with the keyword `new`: `var ninja = new Ninja("Yoshi");`

### CLASSES ARE SYNTACTIC SUGAR

Under the hood we’re still dealing with good old prototypes; classes are syntactic sugar designed to make our lives a bit easier when mimicking classes in JavaScript.

The class above can be translated to functionally identical ES5 code:

```js
function Ninja(name) {
  this.name = name;
}

Ninja.prototype.swingSword = function () {
  return true;
};
```

### Static Methods

```js
class Ninja {
  constructor(name, level) {
    this.name = name;
    this.level = level;
  }

  swingSword() {
    return true;
  }

  //Uses the static keyword to make a static method
  static compare(ninja1, ninja2) {
    return ninja1.level - ninja2.level;
  }
}
```

The compare method, which compares the skill levels of two ninjas, is defined on the class level, and not the instance level! Later we test that this effectively means that the compare method isn’t accessible from ninja instances but is accessible from the Ninja class.

We can also look at how “static” methods can be implemented in pre-ES6 code:

```js
function Ninja(){}
Ninja.compare = function(ninja1, ninja2){...}
```

### Implementing inheritance

```js
class Person {
  constructor(name) {
    this.name = name;
  }

  dance() {
    return true;
  }
}

class Ninja extends Person {
  constructor(name, weapon) {
    super(name);
    this.weapon = weapon;
  }

  wieldWeapon() {
    return true;
  }
}
var person = new Person("Bob");

assert(person instanceof Person, "A person's a person");
assert(person.dance(), "A person can dance.");
assert(person.name === "Bob", "We can call it by name.");
assert(!(person instanceof Ninja), "But it's not a Ninja");
assert(!("wieldWeapon" in person), "And it cannot wield a weapon");
var ninja = new Ninja("Yoshi", "Wakizashi");
assert(ninja instanceof Ninja, "A ninja's a ninja");
assert(ninja.wieldWeapon(), "That can wield a weapon");
assert(ninja instanceof Person, "But it's also a person");
assert(ninja.name === "Yoshi", "That has a name");
assert(ninja.dance(), "And enjoys dancing");
```

## Mixin

TODO

https://github.com/getify/You-Dont-Know-JS/blob/9959fc904d584bbf0b02cf41c192f74ff4238581/objects-classes/ch4.md

See also the second example here: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create#Examples

# Asynchronous JavaScript

Ref:
* https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous
* https://javascript.info/async 

## Asynchronicity: intro and callbacks

Asynchronous programming is a technique that enables your program to start a potentially long-running task and still be able to be responsive to other events while that task runs, rather than having to wait until that task has finished. Once that task has finished, your program is presented with the result.

Many functions provided by browsers, especially the most interesting ones, can potentially take a long time, and therefore, are asynchronous. For example:

-  Making HTTP requests using [`fetch()`](https://developer.mozilla.org/en-US/docs/Web/API/fetch "fetch()")
-  Accessing a user's camera or microphone using [`getUserMedia()`](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia "getUserMedia()")
-  Asking a user to select files using [`showOpenFilePicker()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/showOpenFilePicker "showOpenFilePicker()")

So even though you may not have to *implement* your own asynchronous functions very often, you are very likely to need to *use* them correctly.

Many functions are provided by JavaScript host environments that allow you to schedule asynchronous actions. In other words, actions that we initiate now, but they finish later.

For instance, one such function is the `setTimeout` function:

In the following example, the browser will wait two seconds before executing the anonymous function, then will display the alert message:

```js
let myGreeting = setTimeout(function () {
  alert("Hello, Mr. Universe!");
}, 2000);
```

The image below show you the stack status when the code snippet in the image is executed. We can think about the stack as a pile of post-it: each time we start the execution of a function we add a post-it with the name of the function to the pile, when the execution is over we remove it. 

![](../images/js_event_loop_with_callback.png)

[Ref: JavaScript. Event Loop and Promises](https://medium.com/javascript-in-plain-english/javascript-event-loop-y-promises-951ba6845899)

In the case above, if we were working on a synchronous execution stack, the `setTimeout` function would cause the execution to stop 10 seconds (thus blocking the program) so there would be no way to do anything else while we wait for the counter to finish.

To solve these types of situations, the well-known Event Loop was implemented, which allows the execution of these types of tasks to be performed in a synchronous manner so that:

- execution is not blocked
- once the asynchronous task has been completed, execute your callback whenever possible (the latter is very important to keep in mind)

Let’s see how it works:

- In step 2, when the setTimeout(callback, 10000) function is put on the stack, this call is passed to the Web API of the browser so it no longer belongs to the Javascript engine, but to an additional feature provided by the browser (or the system where it runs).

- Therefore, in step 3 you can see how it is the Web API who takes responsibility for the callback function to be executed.
- In step 4 we can see how the other console.log is executed so that in step 5 the stack is already empty.
- Step 6 takes place once the 10 seconds of the setTimeout found in the Web API have passed (and the JavaScript motorcycle’s execution stack is empty). Since the Web API cannot directly add anything to the stack (it could cause the interruption of code that is currently running), what it does is add the callback to the Callback queue (step 7).
- It is in step 8 where the Event Loop comes into action. At the moment when the Javascript engine stack is empty, the Event Loop picks up what is in the queue callback and adds it to the execution stack.
- From there, the callback execution follows the normal execution process (steps 10 to 13) until the stack is empty.

Therefore, although Javascript is not asynchronous, the inclusion of the `WebAPI` together with the `Event Loop` and the `Queue Callback` allow it to provide a certain aspect of asicronicity so that the heavier tasks do not block the thread of execution.

However, there is a “but”. Since the callback of the function is not known at what time it will be executed (since as we have seen it is necessary that the stack is left empty so that the Event Loop can add things to it from the queue callback) it may be necessary Nesting successive calls within the callback of our function, something known as the “hell callback”.

It is to solve this for what promises arose as we will see below.

![](../images/js_hell_callback.png)


## Why Async?

Many of the user interface mechanisms of browsers also run in the JavaScript process (as tasks). Therefore, long-running JavaScript code can block the user interface.

https://exploringjs.com/impatient-js/ch_async-js.html#how-to-avoid-blocking-the-javascript-process

36.4.1 esempio con un while di 5000 ms che blocca un pulsante. Forse sarebbe carino fare un esempio di una chiamata HTTP con relativo processing, è + reale. IDEA: trovare un modo per fare molte chiamate a una API con pagination e renderle sync, oppure trovare un file grosso, oppure si simula tutto con un while .....

### Other Examples

See here for a detailed explanation https://javascript.info/callbacks

```js
function loadScript(src, callback) {
  let script = document.createElement('script');
  script.src = src;

  script.onload = () => callback(script);

  document.head.append(script);
}
```


## EventLoop - Deep dive (Advanced and not required for beginner) 

See here https://docs.google.com/document/d/10Nr0ETeagEhPX02y_VXKCXRDFeaAlp85p43rRDHuJ-U/edit
 for :
 * EventLoop
 * Callback stack

### Event Loop

Ref:
* https://javascript.info/event-loop Molto light, si perde molto in esempi.... non mi piace molto perchè non è rigoroso. Forse può andare bene per un beginner ma lascia molti punti oscuri

* Video with animations VERY USEFULL! https://2014.jsconf.eu/speakers/philip-roberts-what-the-heck-is-the-event-loop-anyway.html

* Another Video from JSConf https://www.youtube.com/watch?v=cCOL7MC4Pl0 (more recent)



By default, JavaScript runs in a single thread – in both web browsers and Node.js. The so-called event loop sequentially executes tasks (pieces of code) inside that thread. The event loop is depicted in the fig below:

![](../images/js_event_loop.svg)

- Browser event loop processing is single thread (events processed in FIFO order) but the mechanism that manage events before their handlers are executed are not on the same thread.
- The event loop sequentially executes tasks (pieces of code) inside that thread.

Two parties access the task queue:

- `Task sources` add tasks to the queue. Some of those sources run concurrently to the JavaScript process.

  - For example, one task source takes care of `user interface events`: if a user clicks somewhere and a click listener was registered, then an invocation of that listener is added to the task queue.

- The event loop runs continuously inside the JavaScript process. During each loop iteration, it takes one task out of the queue (if the queue is empty, it waits until it isn’t) and executes it. That task is finished when the call stack is empty and there is a return. Control goes back to the event loop, which then retrieves the next task from the queue and executes it. And so on.

The following JavaScript code is an approximation of the event loop:

```js
while (true) {
  const task = taskQueue.dequeue();
  task(); // run task
}
```

- Video with animations VERY USEFULL! https://2014.jsconf.eu/speakers/philip-roberts-what-the-heck-is-the-event-loop-anyway.html

### Call Stack

https://exploringjs.com/impatient-js/ch_async-js.html#the-call-stack

Whenever a function calls another function, we need to remember where to return to after the latter function is finished. That is typically done via a stack – the call stack: the caller pushes onto it the location to return to, and the callee jumps to that location after it is done.

This is an example where several calls happen:

function h(z) {
const error = new Error();
console.log(error.stack);
}
function g(y) {
h(y + 1);
}
function f(x) {
g(x + 1);
}
f(3);
// done
Initially, before running this piece of code, the call stack is empty. After the function call f(3) in line 11, the stack has one entry:

Line 12 (location in top-level scope)
After the function call g(x + 1) in line 9, the stack has two entries:

Line 10 (location in f())
Line 12 (location in top-level scope)
After the function call h(y + 1) in line 6, the stack has three entries:

Line 7 (location in g())
Line 10 (location in f())
Line 12 (location in top-level scope)
Logging error in line 3, produces the following output:

Error:
at h (demos/async-js/stack_trace.mjs:2:17)
at g (demos/async-js/stack_trace.mjs:6:3)
at f (demos/async-js/stack_trace.mjs:9:3)
at demos/async-js/stack_trace.mjs:11:1
This is a so-called stack trace of where the Error object was created. Note that it records where calls were made, not return locations. Creating the exception in line 2 is yet another call. That’s why the stack trace includes a location inside h().

After line 3, each of the functions terminates and each time, the top entry is removed from the call stack. After function f is done, we are back in top-level scope and the stack is empty. When the code fragment ends then that is like an implicit return. If we consider the code fragment to be a task that is executed, then returning with an empty call stack ends the task.

## Callback in callback

Ref: https://javascript.info/callbacks#callback-in-callback

How can we load two scripts sequentially: the first one, and then the second one after it?

The natural solution would be to put the second loadScript call inside the callback, like this:

```js
loadScript("/my/script.js", function (script) {
  alert(`Cool, the ${script.src} is loaded, let's load one more`);
  loadScript("/my/script2.js", function (script) {
    alert(`Cool, the second script is loaded`);
  });
});
```

After the outer loadScript is complete, the callback initiates the inner one.

What if we want one more script…?

```js
loadScript("/my/script.js", function (script) {
  loadScript("/my/script2.js", function (script) {
    loadScript("/my/script3.js", function (script) {
      // ...continue after all scripts are loaded
    });
  });
});
```

So, every new action is inside a callback. That’s fine for few actions, but not good for many, so we’ll see other variants soon -> Callback Hell

We can try to alleviate the problem by making every action a standalone function, like this:

```js
loadScript("1.js", step1);

function step1(error, script) {
  if (error) {
    handleError(error);
  } else {
    // ...
    loadScript("2.js", step2);
  }
}

function step2(error, script) {
  if (error) {
    handleError(error);
  } else {
    // ...
    loadScript("3.js", step3);
  }
}

function step3(error, script) {
  if (error) {
    handleError(error);
  } else {
    // ...continue after all scripts are loaded (*)
  }
}
```

See? It does the same, and there’s no deep nesting now because we made every action a separate top-level function.

It works, but the code looks like a torn apart spreadsheet. It’s difficult to read, and you probably noticed that one needs to eye-jump between pieces while reading it. That’s inconvenient, especially if the reader is not familiar with the code and doesn’t know where to eye-jump.

Also, the functions named `step\*` are all of single use, they are created only to avoid the “pyramid of doom.” No one is going to reuse them outside of the action chain. So there’s a bit of namespace cluttering here.

We’d like to have something better.

Luckily, there are other ways to avoid such pyramids. One of the best ways is to use “promises,” described in the next chapter.

## Callback: handling errors

Ref: https://javascript.info/callbacks#handling-errors

In the above examples we didn’t consider errors. What if the script loading fails? Our callback should be able to react on that.

Here’s an improved version of loadScript that tracks loading errors:

```js
function loadScript(src, callback) {
  let script = document.createElement("script");
  script.src = src;

  script.onload = () => callback(null, script);
  script.onerror = () => callback(new Error(`Script load error for ${src}`));

  document.head.append(script);
}
```

It calls:

- `callback(null, script)` for successful load
- `callback(error)` otherwise.

The usage:

```js
loadScript("/my/script.js", function (error, script) {
  if (error) {
    // handle error
  } else {
    // script loaded successfully
  }
});
```

Once again, the recipe that we used for loadScript is actually quite common. It’s called the “error-first callback” style.

The convention is:

- The first argument of the callback is reserved for an error if it occurs. Then callback(err) is called.
- The second argument (and the next ones if needed) are for the successful result. Then callback(null, result1, result2…) is called.

So the single callback function is used both for reporting errors and passing back results.

## Callback: performing a number of steps in parallel

Sometimes, the steps that we have to go through to get to the final result don’t depend on each other, so we don’t have to make them in sequence. Instead, to save precious milliseconds, we can do them in parallel.

For example, if we want to set a plan in motion that requires us to know which ninjas we have at our disposal, the plan itself, and the location where our plan will play out, we could take advantage of jQuery’s get method and write something like this:

```js
var ninjas, mapInfo, plan;
$.get("data/ninjas.json", function (err, data) {
  if (err) {
    processError(err);
    return;
  }
  ninjas = data;
  actionItemArrived();
});
$.get("data/mapInfo.json", function (err, data) {
  if (err) {
    processError(err);
    return;
  }
  mapInfo = data;
  actionItemArrived();
});

$.get("plan.json", function (err, data) {
  if (err) {
    processError(err);
    return;
  }
  plan = data;
  actionItemArrived();
});
function actionItemArrived() {
  if (ninjas != null && mapInfo != null && plan != null) {
    console.log("The plan is ready to be set in motion!");
  }
}
function processError(err) {
  alert("Error", err);
}
```

Because we don’t know the order in which the data is received, every time we get some data, we have to check whether it’s the last piece of the puzzle that we’re missing. Finally, when all pieces are in place, we can set our plan in motion. Notice that we have to write a lot of boiler- plate code just to do something as common as executing a number of actions in paral- lel. This leads us to the third problem with callbacks: performing a number of steps in parallel is also tricky.

## Pyramid of Doom

see https://javascript.info/callbacks#pyramid-of-doom

At first glance, it looks like a viable approach to asynchronous coding. And indeed it is. For one or maybe two nested calls it looks fine.

But for multiple asynchronous actions that follow one after another, we’ll have code like this:

```js
loadScript('1.js', function(error, script) {

  if (error) {
    handleError(error);
  } else {
    // ...
    loadScript('2.js', function(error, script) {
      if (error) {
        handleError(error);
      } else {
        // ...
        loadScript('3.js', function(error, script) {
          if (error) {
            handleError(error);
          } else {
            // ...continue after all scripts are loaded (*)
          }
        });

      }
    });
  }
});
```

In the code above:

1. We load 1.js, then if there’s no error…
2. We load 2.js, then if there’s no error…
3. We load 3.js, then if there’s no error – do something else (*).

As calls become more nested, the code becomes deeper and increasingly more difficult to manage, especially if we have real code instead of ... that may include more loops, conditional statements and so on.

That’s sometimes called “callback hell” or “pyramid of doom.”

## Promises

Refs:

- [JSINFO](https://javascript.info/promise-basics)
- Promise and Async Course: https://www.pluralsight.com/courses/javascript-promises-async-programming

### History and Why Promises where introduced

Callback programmig style have many problems

- "callback hell": performing sequences of steps is tricky.
- "difficult error handling"
- performing a number of steps in parallel is also tricky.

In order to avoid these problemes, a series of libraries such as `Bluebird` or `Q` were developed that allowed to clean a little all that tangle of nested functions and write code that operated asynchronously but that seemed written as if it were synchronous: the Promises were born.

With ES6 JS has introduced the support for Native Promises.

### Native Promises

Refs:

- [JSINFO](https://javascript.info/promise-basics)
- [IJS Promises](https://exploringjs.com/impatient-js/ch_promises.html)

`Promises` are a new, built-in type of object that help you work with asynchronous code, it's a placeholder for a value that we don’t have yet but will at some later point.

In programming we often have:

- A "producing code" that does something and takes time. For instance, some code that loads a list of blog posts over a network..
- A "consuming code" that wants the result of the "producing code" once it’s ready. Many functions may need that result. For instance a list that will show the list of blog post and a numeric field that shows the total number of posts.

A promise is a special JavaScript object that links the “producing code” and the “consuming code” together.. The “producing code” takes whatever time it needs to produce the promised result, and the “promise” makes that result available to all of the subscribed code when it’s ready.

The analogy isn’t terribly accurate, because JavaScript promises are more complex than a simple subscription list: they have additional features and limitations. But it’s fine to begin with.

The constructor syntax for a promise object is:

```js
let promise = new Promise(function (resolve, reject) {
  // executor (the producing code)
});
```

The function passed to new Promise is called the `executor`. When new Promise is created, the executor is immediatly invoked by the Promise implementation. It contains the producing code which should eventually produce the result.

Its arguments `resolve` and `reject` are callbacks provided by JavaScript itself. Our code is only inside the executor.

When the executor obtains the result, be it soon or late, doesn’t matter, it should call one of these callbacks:

- `resolve(value)` — if the job finished successfully, with result value.
- `reject(error)` — if an error occurred, error is the error object.

So to summarize: the executor runs automatically and attempts to perform a job. When it is finished with the attempt it calls resolve if it was successful or reject if there was an error.

The promise object returned by the new Promise constructor has these internal properties:

- `state`: initially "pending", then changes to either "fulfilled" when resolve is called or "rejected" when reject is called.
- `result`: initially undefined, then changes to value when `resolve(value)` called or error when `reject(error)` is called.

BEST PRACTICE: `error` could be of any type but it's a best practice to use an `Error` object.

So the executor eventually moves promise to one of these states:

- fulfilled
- rejected

To summarize a Promise can be in three states:

- pending,
- fulfilled
- rejected

![](../images/js_promises_statuses.png)

To these Promise objects, developers can attach callbacks through the `then` instruction so that we can execute code once the value resolved by the Promise is available (or the reason why it could not be resolved).

Later we’ll see how consumers can subscribe to these changes.

Here’s an example of a promise constructor and a simple executor function with “producing code” that takes time (via setTimeout):

```js
let promise = new Promise(function (resolve, reject) {
  // the function is executed automatically when the promise is constructed
  console.log("Executor is started");
  // after 1 second signal that the job is done with the result "done"
  setTimeout(() => resolve("done"), 1000);
});
console.log("Waiting for the promise");
```

We can see two things by running the code above:

The executor is called automatically and immediately (by new Promise).

- The executor receives two arguments: resolve and reject. These functions are pre-defined by the JavaScript engine, so we don’t need to create them. We should only call one of them when ready.
- After one second of “processing” the executor calls resolve("done") to produce the result. This changes the state of the promise object:

![](../images/js_promise_resolve.png)

That was an example of a successful job completion, a “fulfilled promise”.

And now an example of the executor rejecting the promise with an error:

```js
let promise = new Promise(function (resolve, reject) {
  // after 1 second signal that the job is finished with an error
  setTimeout(() => reject(new Error("Whoops!")), 1000);
});
```

The call to `reject(...)` moves the promise object to "rejected" state:

![](../images/js_promise_reject.png)

A promise that is either resolved or rejected is called “settled”, as opposed to an initially “pending” promise.

WARNING: There can be only a single result or an error. The executor should call only one resolve or one reject. Any state change is final.

All further calls of resolve and reject are ignored:

```js
let promise = new Promise(function (resolve, reject) {
  resolve("done");

  reject(new Error("…")); // ignored
  setTimeout(() => resolve("…")); // ignored
});
```

The idea is that a job done by the executor may have only one result or an error.

Also, resolve/reject expect only one argument (or none) and will ignore additional arguments.

### Consumers: then

A Promise object serves as a link between the executor and the consuming functions, which will receive the result or error. Consuming functions can be registered (subscribed) using methods `.then`, `.catch` and `.finally`.

The most important, fundamental one is `.then`, syntax:

```js
promise.then(
  function (result) {
    /* handle a successful result */
  },
  function (error) {
    /* handle an error */
  }
);
```

1. The first argument of .then is a function that runs when the promise is resolved, and receives the result.
2. The second argument of .then is a function that runs when the promise is rejected, and receives the error.

For instance, here’s a reaction to a successfully resolved promise:

```js
let promise = new Promise(function (resolve, reject) {
  setTimeout(() => resolve("done!"), 1000);
});

// resolve runs the first function in .then
promise.then(
  (result) => alert(result), // shows "done!" after 1 second
  (error) => alert(error) // doesn't run
);
```

And in the case of a rejection, the second one:

```js
let promise = new Promise(function (resolve, reject) {
  setTimeout(() => reject(new Error("Whoops!")), 1000);
});

// reject runs the second function in .then
promise.then(
  (result) => alert(result), // doesn't run
  (error) => alert(error) // shows "Error: Whoops!" after 1 second
);
```

If we’re interested only in successful completions, then we can provide only one function argument to .then:

```js
let promise = new Promise((resolve) => {
  setTimeout(() => resolve("done!"), 1000);
});

promise.then(alert); // shows "done!" after 1 second
```

WARNING: a common mistake is to pass in a non-function parameter to `Promise.then()` without causing an error. For example code below:

```js 
// 1
new Promise(resolve => setTimeout(resolve, 2000))
    .then(() => console.log("after 2 seconds"));

// 2
new Promise(resolve => setTimeout(resolve, 3000))
    .then(console.log("before 3 seconds (instantly)"));
```

Produces the following output:
```
before 3 seconds (instantly)
after 2 seconds
```

The second Promise should resolve after the first but the opposite is happening, why? Because the parameter to the second `then()` is not a function, the expression `console.log("before 3 seconds (instantly)"))` is evaluated before the function `then()` is invoked (print the output above) and the return value is `undefined`. Passing undefined to .then() is allowed, and since that's what console.log() returns, there's no error raised.


REF: https://stackoverflow.com/questions/42094764/why-is-it-possible-to-pass-in-a-non-function-parameter-to-promise-then-without/42094874

### Consumers: catch

If we’re interested only in errors, then we can use null as the first argument: `.then(null, errorHandlingFunction)` Or we can use `.catch(errorHandlingFunction)`, which is exactly the same:

```js
let promise = new Promise((resolve, reject) => {
  setTimeout(() => reject(new Error("Whoops!")), 1000);
});

// .catch(f) is the same as promise.then(null, f)
promise.catch(alert); // shows "Error: Whoops!" after 1 second
```

The call .catch(f) is a complete analog of .then(null, f), it’s just a shorthand.

### Consumers: finally

Just like there’s a finally clause in a regular `try {...} catch {...}`, there’s finally in promises.

The call `.finally(f)` is similar to `.then(f, f)` in the sense that `f` always runs when the promise is settled: be it resolve or reject.

finally is a good handler for **performing cleanup**, e.g. stopping our loading indicators, as they are not needed anymore, no matter what the outcome is.

Like this:

```js
new Promise((resolve, reject) => {
/_ do something that takes time, and then call resolve/reject _/
})
// runs when the promise is settled, doesn't matter successfully or not
.finally(() => stop loading indicator)
// so the loading indicator is always stopped before we process the result/error
.then(result => show result, err => show error)
```

That said, `finally(f)` isn’t exactly an alias of `then(f,f)` though. There are few subtle differences:

- A finally handler has no arguments. In finally we don’t know whether the promise is successful or not. That’s all right, as our task is usually to perform “general” finalizing procedures.
- A finally handler passes through results and errors to the next handler.

For instance, here the result is passed through finally to then:

```js
new Promise((resolve, reject) => {
  setTimeout(() => resolve("result"), 2000);
})
  .finally(() => alert("Promise ready"))
  .then((result) => alert(result)); // <-- .then handles the result
```

And here there’s an error in the promise, passed through finally to catch:

```js
new Promise((resolve, reject) => {
  throw new Error("error");
})
  .finally(() => alert("Promise ready"))
  .catch((err) => alert(err)); // <-- .catch handles the error object
```

That’s very convenient, because finally is not meant to process a promise result. So it passes it through.

We’ll talk more about promise chaining and result-passing between handlers in the next chapter.

### Can we attach handlers to settled promises?

You can add callbacks with `.then()` before or after the promise has been resolved, and you can even add more than one callback.

These callbacks will be called in the order they were added, but always asynchronously, after the current turn of the event loop. So if the promise has already been resolved when you add a .then, your handler will be called immediately, but in the "asynchronous sense".

The Promises/A+ spec says:

[...] onFulfilled and onRejected execute asynchronously, after the event loop turn in which then is called, and with a fresh stack.

```js
// the promise becomes resolved immediately upon creation
let promise = new Promise((resolve) => {
  resolve("done!");
  console.log("promise fulfilled!");
});

promise.then((result) =>
  console.log(`[THEN HANDLER] Promise result: ${result}`)
); // done! (shows up right now)

console.log(
  "Even if the promise is fulfilled synchronously, this console log is printed before the .then() handler is executed"
);
```

The output of the above example is:
```
promise fulfilled!
Even if the promise is fulfilled synchronously, this console log is printed before the .then() handler is executed
[THEN HANDLER] Promise result: done!
```

Example: code_snippet/promises_attach_handler_to_resolved_promise.js

### Promises chaining

Let’s return to the problem mentioned in the chapter Introduction: callbacks: we have a sequence of asynchronous tasks to be performed one after another — for instance, loading scripts. How can we code it well?

Promises provide a couple of recipes to do that:

- promise chaining
- and ???

Promise chaining looks like this:

```js
new Promise(function (resolve, reject) {
  setTimeout(() => resolve(1), 1000); // (*)
})
  .then(function (result) {
    // (**)
    alert(result); // 1
    return result * 2;
  })
  .then(function (result) {
    // (***)
    alert(result); // 2
    return result * 2;
  })
  .then(function (result) {
    alert(result); // 4
    return result * 2;
  });
```

The idea is that the result is passed through the chain of .then handlers.

Here the flow is:

- The initial promise resolves in 1 second (\*),
- Then the .then handler is called (\*\*).
- The value that it returns is passed to the next .then handler (\*\*\*)
- …and so on.

![](../images/js_promise_chain.png)

As the result is passed along the chain of handlers, we can see a sequence of alert calls: 1 → 2 → 4.

The whole thing works, because a call to promise.then returns a promise, so that we can call the next .then on it.

When a handler returns a value, it becomes the result of that promise, so the next .then is called with it.

A classic newbie error: technically we can also add many .then to a single promise. This is not chaining.

For example:

```js
let promise = new Promise(function (resolve, reject) {
  setTimeout(() => resolve(1), 1000);
});

promise.then(function (result) {
  alert(result); // 1
  return result * 2;
});

promise.then(function (result) {
  alert(result); // 1
  return result * 2;
});

promise.then(function (result) {
  alert(result); // 1
  return result * 2;
});
```

![](../images/js_promise_chain_common_error.png)

Then always return a promise [ref](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)

A handler, used in `.then(handler)` may create and return a promise or not.

The behavior of the handler function follows a specific set of rules. If a handler function:

- returns a value, the promise returned by then gets resolved with the returned value as its value.
- doesn't return anything, the promise returned by then gets resolved with an undefined value.
- throws an error, the promise returned by then gets rejected with the thrown error as its value.
- returns an already fulfilled promise, the promise returned by then gets fulfilled with that promise's value as its value.
- returns an already rejected promise, the promise returned by then gets rejected with that promise's value as its value.
- returns another pending promise object, the resolution/rejection of the promise returned by then will be subsequent to the resolution/rejection of the promise returned by the handler. Also, the resolved value of the promise returned by then will be the same as the resolved value of the promise returned by the handler.

In a chain further handlers wait until the promise returned by the previous the settles, for instance:

```js
new Promise(function (resolve, reject) {
  setTimeout(() => resolve(1), 1000);
})
  .then(function (result) {
    alert(result); // 1
    return new Promise((resolve, reject) => {
      // (*)
      setTimeout(() => resolve(result * 2), 1000);
    });
  })
  .then(function (result) {
    // (**)
    alert(result); // 2
    return new Promise((resolve, reject) => {
      setTimeout(() => resolve(result * 2), 1000);
    });
  })
  .then(function (result) {
    alert(result); // 4
  });
```

Here the first `.then` shows 1 and returns `new Promise(…)` in the line (\*). After one second it resolves, and the result (the argument of resolve, here it’s `result * 2`) is passed on to handler of the second .then. That handler is in the line (\*\*), it shows 2 and does the same thing.

So the output is the same as in the previous example: 1 → 2 → 4, but now with 1 second delay between alert calls.

Returning promises allows us to build chains of asynchronous actions.

### Chaining Example: loadscript

The example below load 3 script in a sequence:

```js
function loadScript(src) {
  return new Promise(function (resolve, reject) {
    let script = document.createElement("script");
    script.src = src;

    script.onload = () => resolve(script);
    script.onerror = () => reject(new Error(`Script load error for ${src}`));

    document.head.append(script);
  });
}

loadScript("/article/promise-chaining/one.js")
  .then((script) => loadScript("/article/promise-chaining/two.js"))
  .then((script) => loadScript("/article/promise-chaining/three.js"))
  .then((script) => {
    // scripts are loaded, we can use functions declared there
    one();
    two();
    three();
  });
```

Here each loadScript call returns a promise, when that promise resolves, also the promise returned by `.then` resolves and the next `.then` runs.

Please note that the code is still “flat” — it grows down, not to the right. There are no signs of the “pyramid of doom”.

Technically, we could add `.then directly to each loadScript, like this:

```js
loadScript("/article/promise-chaining/one.js").then((script1) => {
  loadScript("/article/promise-chaining/two.js").then((script2) => {
    loadScript("/article/promise-chaining/three.js").then((script3) => {
      // this function has access to variables script1, script2 and script3
      one();
      two();
      three();
    });
  });
});
```

This code does the same: loads 3 scripts in sequence. But it “grows to the right”. So we have the same problem as with callbacks.

People who start to use promises sometimes don’t know about chaining, so they write it this way. Generally, chaining is preferred.

### Chaining Example: fetch API

In frontend programming promises are often used for network requests. So let’s see an extended example of that.

See here: https://javascript.info/promise-chaining#bigger-example-fetch

### Thenable

To be precise, a handler may return not exactly a promise, but a so-called “thenable” object – an arbitrary object that has a method .then. It will be treated the same way as a promise.

The idea is that 3rd-party libraries may implement “promise-compatible” objects of their own. They can have an extended set of methods, but also be compatible with native promises, because they implement .then.

Here’s an example of a thenable object:

```js
class Thenable {
  constructor(num) {
    this.num = num;
  }
  then(resolve, reject) {
    alert(resolve); // function() { native code }
    // resolve with this.num*2 after the 1 second
    setTimeout(() => resolve(this.num * 2), 1000); // (**)
  }
}

new Promise((resolve) => resolve(1))
  .then((result) => {
    return new Thenable(result); // (*)
  })
  .then(alert); // shows 2 after 1000ms
```

JavaScript checks the object returned by the `.then` handler in line (\*): if it has a callable method named then, then it calls that method providing native functions `resolve`, `reject` as arguments (similar to an executor) and waits until one of them is called. In the example above `resolve(2)` is called after 1 second (\*\*). Then the result is passed further down the chain.

This feature allows us to integrate custom objects with promise chains without having to inherit from Promise.

### Error handling with promises

https://javascript.info/promise-error-handling

Promise chains are great at error handling. When a promise rejects, the control jumps to the closest rejection handler. That’s very convenient in practice.

For instance, in the code below the URL to fetch is wrong (no such site) and .catch handles the error:

```js
fetch("https://no-such-server.blabla") // rejects
  .then((response) => response.json())
  .catch((err) => alert(err)); // TypeError: failed to fetch (the text may vary)
```

As you can see, the .catch doesn’t have to be immediate. It may appear after one or maybe several .then.

Or, maybe, everything is all right with the site, but the response is not valid JSON. The easiest way to catch all errors is to append .catch to the end of chain:

```js
fetch("/article/promise-chaining/user.json")
  .then((response) => response.json())
  .then((user) => fetch(`https://api.github.com/users/${user.name}`))
  .then((response) => response.json())
  .then(
    (githubUser) =>
      new Promise((resolve, reject) => {
        let img = document.createElement("img");
        img.src = githubUser.avatar_url;
        img.className = "promise-avatar-example";
        document.body.append(img);

        setTimeout(() => {
          img.remove();
          resolve(githubUser);
        }, 3000);
      })
  )
  .catch((error) => alert(error.message));
```

Normally, such .catch doesn’t trigger at all. But if any of the promises above rejects (a network problem or invalid json or whatever), then it would catch it.

### Implicit try...catch

The code of a promise executor and promise handlers has an "invisible try..catch" around it. If an exception happens, it gets caught and treated as a rejection.

For instance, this code:

```js
new Promise((resolve, reject) => {
  throw new Error("Whoops!");
}).catch(alert); // Error: Whoops!
```

…Works exactly the same as this:

```js
new Promise((resolve, reject) => {
  reject(new Error("Whoops!"));
}).catch(alert); // Error: Whoops!
```

The "invisible try..catch" around the executor automatically catches the error and turns it into rejected promise.

This happens not only in the executor function, but in its handlers as well. If we throw inside a `.then` handler, that means a rejected promise, so the control jumps to the nearest error handler.

Here’s an example:

```js
new Promise((resolve, reject) => {
  resolve("ok");
})
  .then((result) => {
    throw new Error("Whoops!"); // rejects the promise
  })
  .catch(alert); // Error: Whoops!
```

This happens for all errors, not just those caused by the throw statement. For example, a programming error:

```js
new Promise((resolve, reject) => {
  resolve("ok");
})
  .then((result) => {
    blabla(); // no such function
  })
  .catch(alert); // ReferenceError: blabla is not defined
```

The final `.catch` not only catches explicit rejections, but also accidental errors in the handlers above.

### Rethrowing

As we already noticed, .catch at the end of the chain is similar to try..catch. We may have as many .then handlers as we want, and then use a single .catch at the end to handle errors in all of them.

In a regular try..catch we can analyze the error and maybe rethrow it if it can’t be handled. The same thing is possible for promises.

If we throw inside `.catch`, then the control goes to the next closest error handler. And if we handle the error and finish normally, then it continues to the next closest successful .then handler.

In the example below the .catch successfully handles the error:

```js
// the execution: catch -> then
new Promise((resolve, reject) => {
  throw new Error("Whoops!");
})
  .catch(function (error) {
    alert("The error is handled, continue normally");
  })
  .then(() => alert("Next successful handler runs"));
```

Here the .catch block finishes normally. So the next successful .then handler is called.

In the example below we see the other situation with .catch. The handler (\*) catches the error and just can’t handle it (e.g. it only knows how to handle URIError), so it throws it again:

```js
// the execution: catch -> catch
new Promise((resolve, reject) => {
  throw new Error("Whoops!");
})
  .catch(function (error) {
    // (\*)
    if (error instanceof URIError) {
      // handle it
    } else {
      alert("Can't handle such error");
      throw error; // throwing this or another error jumps to the next catch
    }
  })
  .then(function () {
    /_ doesn't run here _/;
  })
  .catch((error) => {
    // (\*\*)
    alert(`The unknown error has occurred: ${error}`);
    // don't return anything => execution goes the normal way
  });
```

The execution jumps from the first .catch (\*) to the next one (\*\*) down the chain.

### Unhandled rejections

What happens when an error is not handled? For instance, we forgot to append .catch to the end of the chain, like here:

```js
new Promise(function () {
  noSuchFunction(); // Error here (no such function)
}).then(() => {
  // successful promise handlers, one or more
}); // without .catch at the end!
```

In case of an error, the promise becomes rejected, and the execution should jump to the closest rejection handler. But there is none. So the error gets “stuck”. There’s no code to handle it.

In practice, just like with regular unhandled errors in code, it means that something has gone terribly wrong.

What happens when a regular error occurs and is not caught by try..catch? The script dies with a message in the console. A similar thing happens with unhandled promise rejections.

The JavaScript engine tracks such rejections and generates a `global error` in that case. You can see it in the console if you run the example above.

In the browser we can catch such errors using the event unhandledrejection:

```js
window.addEventListener("unhandledrejection", function (event) {
  // the event object has two special properties:
  alert(event.promise); // [object Promise] - the promise that generated the error
  alert(event.reason); // Error: Whoops! - the unhandled error object
});

new Promise(function () {
  throw new Error("Whoops!");
}); // no catch to handle the error
```

The event is the part of the HTML standard.

If an error occurs, and there’s no .catch, the unhandledrejection handler triggers, and gets the event object with the information about the error, so we can do something.

Usually such errors are unrecoverable, so our best way out is to inform the user about the problem and probably report the incident to the server.

In non-browser environments like Node.js there are other ways to track unhandled errors.

### Promise API

https://javascript.info/promise-api

There are 5 static methods of Promise class:

- `Promise.all(promises)` – waits for all promises to resolve and returns an array of their results. If any of the given promises rejects, it becomes the error of Promise.all, and all other results are ignored.
- `Promise.allSettled(promises)` (recently added method) – waits for all promises to settle and returns their results as an array of objects with status: "fulfilled" or "rejected", value (if fulfilled) or reason (if rejected).
- `Promise.race(promises)` – waits for the first promise to settle, and its result/error becomes the outcome.
- `Promise.resolve(value)` – makes a resolved promise with the given value.
- `Promise.reject(error)` – makes a rejected promise with the given error.

### Promisification

Ref: https://javascript.info/promisify

“Promisification” is a long word for a simple transformation. It’s the conversion of a function that accepts a callback into a function that returns a promise.

There are also modules with a bit more flexible promisification functions, e.g. [es6-promisify](https://github.com/digitaldesignlabs/es6-promisify). In Node.js, there’s a built-in [util.promisify](https://nodejs.org/api/util.html#util_util_promisify_original) function for that.

Here you can find a deep explanation: https://javascript.info/promisify

Promisification is a great approach, especially when you use async/await (see the next chapter), but not a total replacement for callbacks:

- Remember, a promise may have only one result, but a callback may technically be called many times.
- So promisification is only meant for functions that call the callback once. Further calls will be ignored.

### Microtask Queue

****
[VEDI QUA per una spigazione dettagliata sull'eventloop e la microtask queue: [GUIDE] JavaScript runtime environment: EventLoop, Execution Stack, Task, Microtask, rendering steps (ADVANCED)](https://docs.google.com/document/d/10Nr0ETeagEhPX02y_VXKCXRDFeaAlp85p43rRDHuJ-U/edit#heading=h.p1j57u4reeei)
****

#### Unhandled rejection

Remember the `unhandledrejection` event from the article Error handling with promises?

Now we can see exactly how JavaScript finds out that there was an unhandled rejection.

An "unhandled rejection" occurs when a promise error is not handled at the end of the microtask queue.

Normally, if we expect an error, we add .catch to the promise chain to handle it:

```js
let promise = Promise.reject(new Error("Promise Failed!"));
promise.catch((err) => alert("caught"));

// doesn't run: error handled
window.addEventListener("unhandledrejection", (event) => alert(event.reason));
```

But if we forget to add .catch, then, after the microtask queue is empty, the engine triggers the event:

```js
let promise = Promise.reject(new Error("Promise Failed!"));

// Promise Failed!
window.addEventListener("unhandledrejection", (event) => alert(event.reason));
```

What if we handle the error later? Like this:

```js
let promise = Promise.reject(new Error("Promise Failed!"));
setTimeout(() => promise.catch((err) => alert("caught")), 1000);

// Error: Promise Failed!
window.addEventListener("unhandledrejection", (event) => alert(event.reason));
```

Now, if we run it, we’ll see Promise Failed! first and then caught.

If we didn’t know about the microtasks queue, we could wonder: “Why did unhandledrejection handler run? We did catch and handle the error!”

But now we understand that unhandledrejection is generated when the microtask queue is complete: the engine examines promises and, if any of them is in the “rejected” state, then the event triggers.

In the example above, .catch added by setTimeout also triggers. But it does so later, after unhandledrejection has already occurred, so it doesn’t change anything.

### Async/await

https://javascript.info/async-await

The word “async” before a function means one simple thing: a function always returns a promise. Other values are wrapped in a resolved promise automatically.

### [ADVANCED] State and Fates

https://github.com/domenic/promises-unwrapping/blob/master/docs/states-and-fates.md

### WIP

https://javascript.info/promise-chaining
LICENCE: scritto da Nicola

```js
new Promise(function (resolve, reject) {
  setTimeout(() => resolve(1), 1000); // (*)
})
  .then(function (result) {
    // (**)

    alert(result); // 1
    return result * 2;
  })
  .then(function (result) {
    // (***)

    alert(result); // 2
    return result * 2;
  })
  .then(function (result) {
    alert(result); // 4
    return result * 2;
  });
```

```js
let promiseA = new Promise(function (resolve, reject) {
  setTimeout(() => resolve(1), 1000); // (*)
});

let promiseB = promiseA.then(function (result) {
  // (**)

  alert(result); // 1
  return result * 2;
});

let promiseC = promiseB.then(function (result) {
  // (***)

  alert(result); // 2
  return result * 2;
});

let promiseD = promiseC.then(function (result) {
  alert(result); // 4
  return result * 2;
});
```

```js
function fA(resolve, reject) {
  setTimeout(() => resolve(1), 1000); // (*)
}
let pA = new Promise(fA);

function fB(result) {
  // (**)
  alert(result); // 1
  return result * 2;
}
let pB = pA.then(fB);

function fC(result) {
  // (***)
  alert(result); // 2
  return result * 2;
}
let pC = pB.then(fC);

function fD(result) {
  alert(result); // 4
  return result * 2;
}

let pD = pC.then(fD);
```

### [WIP] RSVP and Ember: inspector and instrumentation

RSVP implementation provide an Instrumentation feature: https://github.com/tildeio/rsvp.js#instrumentation

RSVP is used by EmberJS. EmberJS provide an Inspector which allow you to debug Promises

### WIP: Adehun a simple Promise Implementation for Educational Purpuse

Ref: https://stackoverflow.com/questions/17718673/how-is-a-promise-defer-library-implemented

The Lib:
https://github.com/abdulapopoola/Adehun/blob/master/adehun.js

Blog Post explaing the lib: https://abdulapopoola.com/2015/02/23/how-to-write-a-promisea-compatible-library/

The then function takes in two optional arguments (onFulfill and onReject handlers) and must return a new promise. Two major requirements:

1. The base promise (the one on which then is called) needs to create a new promise using the passed in handlers; the base also stores an internal reference to this created promise so it can be invoked once the base promise is fulfilled/rejected.

2. If the base promise is settled (i.e. fulfilled or rejected), then the appropriate handler should be called immediately. Adehun.js handles this scenario by calling process in the then function.

[then()](https://github.com/abdulapopoola/Adehun/blob/95c90fe91ed5db16477b9714d34029fc9393597f/adehun.js#L30)

### WIP ferch API with Promise example

example

https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API

The Fetch API provides an interface for fetching resources (including across the network). It will seem familiar to anyone who has used XMLHttpRequest, but the new API provides a more powerful and flexible feature set.

### USECASE: Don't block the UI making network requests

Naive code that fetch data from a remote server:

```
try {
  var ninjas = syncGetJSON("ninjas.json");
  var missions = syncGetJSON(ninjas[0].missionsUrl);
  var missionDetails = syncGetJSON(missions[0].detailsUrl); //Study the mission description
} catch(e){
          //Oh no, we weren't able to get the mission details
}
```

PROBLEM: We’ve just blocked our UI until the long-running operations finish because JavaScript relies on a single-threaded execution model.

We can solve rewriting the code using callbacks:

```
getJSON("ninjas.json", function(err, ninjas){
  if(err) {
    console.log("Error fetching list of ninjas", err);
    return;
  }
  getJSON(ninjas[0].missionsUrl, function(err, missions) {
    if(err) {
      console.log("Error locating ninja missions", err);
      return;
    }
    getJSON(missions[0].detailsUrl, function(err, missionDetails){ if(err) {
      console.log("Error locating mission details", err);
      return;
    }
    //Study the intel plan
    });
  });
});
```

PROBLEM: adds a lot of boilerplate error-handling code, and it’s plain ugly.

We can improve the above async code using generators and promise:

```
async(function*(){
  try {
   const ninjas = yield getJSON("ninjas.json");
   const missions = yield getJSON(ninjas[0].missionsUrl);
   const missionDescription = yield getJSON(missions[0].detailsUrl);
     //Study the mission details
  }
  catch(e) {
    //Oh no, we weren't able to get the mission details
  }
});
```

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


# JQuery

REFs:

- https://jquery.com/
- [JQuery Learning Center](http://learn.jquery.com/)

## How to select elements

- [Intro](https://learn.jquery.com/using-jquery-core/selecting-elements/)
- [Selector reference](http://api.jquery.com/category/selectors/)

The most basic concept of jQuery is to "select some elements and do something with them." jQuery supports most CSS3 selectors, as well as some non-standard selectors.

When a selection is made using `$()`, an object is always returned

To check if a selection contains elements:

- https://learn.jquery.com/using-jquery-core/selecting-elements/#does-my-selection-contain-any-elements
- `if ( $( "div.foo" ).length )`

# Modules, loaders and bundlers.

Ref:

- https://nolanlawson.com/2015/10/19/the-struggles-of-publishing-a-javascript-library/
- Long overview Oct 28, 2018: https://medium.com/@ajmeyghani/javascript-bundlers-a-comparison-e63f01f2a364
- Eloquent_JavaScript.pdf ch 10

## Intro: Modules, Module Loaders, Modules Bundlers

Ref:

- https://www.jvandemo.com/a-10-minute-primer-to-javascript-modules-module-formats-module-loaders-and-module-bundlers/
- https://medium.com/@ajmeyghani/javascript-bundlers-a-comparison-e63f01f2a364
- http://exploringjs.com/es6/ch_modules.html

Why do we need modules?

- to create reusable code
- to provide a clear public **interface** to it
- to state the dependency between reusable code (which other modules need to be present to be able to use a given module and to automatically load dependencies).

We will look at:

- Module formats: what are they and what are the different module definitions for JavaScript.
- Module loaders: what are loaders and how can they be used.
- Module bundlers: what are JavaScript bundlers, what is the process for setting up each, and how do they compare against each other.

The modules ecosystem is quite complex. JavaScript has had modules for a long time. However, they were implemented via libraries, not built into the language. ES6/ES2015 is the first time that JavaScript has built-in modules. EcmaScript 5 and earlier editions were not designed with modules in mind. Over time, developers came up with different patterns to simulate modular design in JavaScript.

### Module Formats Intro

A module format is the syntax we can use to define a module. Before EcmaScript 6 or ES2015, JavaScript did not have an official syntax to define modules. Therefore, smart developers came up with various formats to define modules in JavaScript. Some of the most widely adapted and well known formats are:

- Asynchronous Module Definition (AMD)
- CommonJS
- Universal Module Definition (UMD)
- System.register
- ES6 module format

- Module bundlers: what are JavaScript bundlers, what is the process for setting up each, and how do they compare against each other.

### Module Loaders Intro

Module loaders are used to load JavaScript modules at runtime, usually for development. Most notable loaders are:

- RequireJS: a library
- SystemJS:

becaouse the JS standard different module definitions for JavaScript

### Module Bundlers Intro

Module bundlers are used to bundle several modules into one or more optimized bundles for the browser. Most notable bundlers are:

- Webpack,
- SnowPack (nice one!)
- Rollup,
- Google Closure Compiler.
- Parcel
- Broserify

The Google Closure Compiler (Closure) is a code analyzer and optimizer that can also be used to create bundles. Closure is probably the most mature analyzer and optimizer out there. If you want to analyze your code and output the most optimized code possible, Closure will be your best friend. Rollup has a great Closure plugin that I’m going to cover later.

Most of the bundlers these days have very similar features.

**Tree Shaking**
The one feature that varies among them is tree shaking for CJS or ES modules (dead-code elimination). Out of all the bundlers, Webpack has the most consistent built-in support for ES and CJS module tree shaking. Rollup and Parcel do have tree shaking but Webpack’s is just a little better overall. Parcel however is working on making tree shaking available for both CJS and ES modules. Until tree shaking matures among bundlers it’s best to carefully examine what you are importing to minimize the final bundle size.
Overall all bundlers are pretty fast if you are careful about what you are importing. In the worst case in can take up to 7 seconds to bundle a very simple project.

Zero-config or not, you’ll have to spend some time experimenting with each bundler to learn them well. If a bundler is labelled as zero-config that does not mean that you don’t have to configure anything for production. It’s mostly true for development, but for production you have to create configuration files regardless. I think a better term would have been “bundlers for development”, rather than “bundlers with zero configuration”.

Tree Shaking:

- ref: https://webpack.js.org/guides/tree-shaking/
- Tree shaking is a term commonly used in the JavaScript context for **dead-code elimination**. It relies on the static structure of ES2015 module syntax, i.e. import and export. The name and concept have been popularized by the ES2015 module bundler rollup.

## History: Pre 2015

[JSFIP](https://exploringjs.com/impatient-js/ch_modules.html#scripts): another point of view about using js script manually.

Riassunto:

- ESM looks like the best modularity pattern
  - Browser support is good
  - NodeJS has experimental support (https://nodejs.org/api/esm.html#esm_package_exports)
  - TypeScript use this format
- CJS is still the way to go in NodeJS JS app. Many lib for NodeJS

TL;DR: In 2020 learn ESM first and then CJS if you need to use NodeJS

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

## NON Standard formats: CommonJS, AMD-RequireJS, UMD

Let's have a quick look at each one of them so you can recognize their syntax.

Two prominent module definitions were developed as part of the community effort: `CJS (CommonJS)` and `AMD (Asynchronous Module Definition)`.

`CommonJS` format:

- Main Target: Backend.
- was defined as a **synchronous** definition intended for **server-side JavaScript**.
- Node’s module system is practically based on CJS with some minor differences.
- uses `require` and `module.exports` to define dependencies and modules
- CommonJS modules work quite well and, in combination with NPM, have allowed the JavaScript community to start sharing code on a large scale. But now is obsolete.
- The imported result is a copy of the imported object.

```
var dep1 = require('./dep1');
var dep2 = require('./dep2');

module.exports = function(){
  // ...
}
```

`AMD` format:

- Main Target: Frontend
- Imports modules: Asynchronously.
- was defined an **asynchronous** model intended for modules in the browser
- `RequireJS` is the most popular implementation of AMD.
- The AMD format is used in browsers and uses a `define` function to define modules

```
//Calling define with a dependency array and a factory function
define(['dep1', 'dep2'], function (dep1, dep2) {

    //Define the module value by returning a value.
    return function () {};
});
```

`UMD` format:

- Main Target: Frontend and Backend (“Universal”).
- UMD stands for Universal Module Definition. It’s essentially a piece of JavaScript code placed at the top of libraries that enables any loader to load them regardless of the environment they are in.
- It's more like an interface for bringing compatibility in Frontend and Backend environments to both AMD and CJS.

`ESM - ECMAScript Modules (2015)` format:

- Main Target: Frontend and Backend.
- A standard module system was finally introduced in 2015 as part of the ES2015 (ES6) specification. It defined the semantics for importing and exporting modules asynchronously.
- Works in many modern browsers
- Tree-shaking support due to ES6's static module structure

Ref:

- Eloquent_JavaScript.pdf ch 10

## Current state of Modules in Node.js

2020 July:

- With the release of Node version 13.9.0, ES modules can now be used without an experimental flag since they are enabled by default.

- https://2ality.com/2019/10/hybrid-npm-packages.html
- https://blog.logrocket.com/es-modules-in-node-today/
- https://medium.com/@nirsky/make-your-npm-package-work-on-both-node-js-and-browser-58bff1a18f55

2019 July :
https://blog.logrocket.com/es-modules-in-node-js-12-from-experimental-to-release/

## ESM ES6/ES2015 Modules: Standard Javascript Modules

- [javascript.info Modules](https://javascript.info/modules-intro)
  - Good intro for beginners
  - Super brief History of modules
  - basic usage of import/export with browser example
  - `<script type="module">` : Always "use strict", Module-level scope, A module code is evaluated only the first time when imported, import.meta, "this" is undefined, Module scripts are deferred, `<script async type="module">` , External scripts, No “bare” modules allowed, Compatibility, “nomodule”,

- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules


- [CommonJS vs. ES Modules: Modules and Imports in NodeJS in 2022](https://reflectoring.io/nodejs-modules-imports/)



- [JSFIP Modules ES2020](https://exploringjs.com/impatient-js/ch_modules.html)
- [Yeuda draft](https://gist.github.com/wycats/51c96e3adcdb3a68cbc3)
- http://eviltrout.com/2014/05/03/getting-started-with-es6.html


As our application grows bigger, we want to split it into multiple files, so called “modules”. A module may contain a class or a library of functions for a specific purpose.

For a long time, JavaScript existed without a language-level module syntax. That wasn’t a problem, because initially scripts were small and simple, so there was no need. 

But eventually scripts became more and more complex, so the community invented a variety of ways to organize code into modules, special libraries to load modules on demand. UMD, AMD, was 

JavaScript standard from 2015 introduces its own, different module system. It is usually called ES modules (ESM), where ES stands for ECMAScript.

In 2022 modern browsers, NodeJS 14 and typescript support ESM. So if you are starting a new project, use ES Modules ( ref https://reflectoring.io/nodejs-modules-imports/ ).

The full standard of ES modules comprises the following parts:

1. Syntax (how code is written): What is a module? How are imports and exports declared? Etc.
2. Semantics (how code is executed): How are variable bindings exported? How are imports connected with exports? Etc.
3. A programmatic loader API for configuring module loading (https://javascript.info/modules-dynamic-imports). Usecase: conditional imports.


A **module** is simply a file with JavaScript code in it. By default anything you declare in a file in a ES6 project is not available outside that file. You have to use the export keyword to explicitly make it available, defining the **module interface**. An ES module’s interface is not a single value but a set of named bindings. Modules can load each other and use special directives `export` and `import` to interchange functionality, call functions of one module from another one.

`export` keyword labels variables and functions that should be accessible from outside the current module.

The easiest way to use it is to place it in front of any items you want exported out of the module, for example to export the `name` variable and the `draw` function:

```js
export const name = 'square';

export function draw(ctx, length, x, y, color) {
  ctx.fillStyle = color;
  ctx.fillRect(x, y, length, length);

  return { length, x, y, color };
}
```

`import` allows the import of functionality from other modules:

```js
import { name, draw, reportArea, reportPerimeter } from './modules/square.js';

draw(...) // here we are using a function defined in the square.js file
```


You can export functions, var, let, const, and — as we'll see later — classes. They need to be top-level items; you can't use export inside a function, for example.

A more convenient way of exporting all the items you want to export is to use a single export statement at the end of your module file, followed by a comma-separated list of the features you want to export wrapped in curly braces. For example:

```js
export { name, draw, reportArea, reportPerimeter };
```

WARNING:

- in this paragraph we'll describe the ESM syntax and convention. Many bundlers (ex: Webpack) use a similar syntax but with a slightly different behaviour.


### Default exports versus named exports

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#default_exports_versus_named_exports 

default export — this is designed to make it easy to have a default function provided by a module, and also helps JavaScript modules to interoperate with existing CommonJS and AMD module systems (as explained nicely in [ES6 In Depth: Modules by Jason Orendorff](https://hacks.mozilla.org/2015/08/es6-in-depth-modules/); search for "Default exports").

For example it's very handy to create ReactJS components.
`export default` is used to export a single class, function or primitive from a script file.

The export can also be written as

```js
export default class HelloWorld extends React.Component {
  render() {
    return <p>Hello, world!</p>;
  }
}
```

You could also write this as a function component like

```js
export default function HelloWorld() {
  return <p>Hello, world!</p>
}
```

This is used to import this function in another script file

```js
import HelloWorld from './HelloWorld';
```

You don't necessarily import it as HelloWorld you can give it any name as it's a default export.

Again, note the lack of curly braces. This is because there is only one default export allowed per module, and we know that randomSquare is it. The above line is basically shorthand for:

```js
import {default as randomSquare} from './modules/square.js';
```

### Named Import - Avoiding naming conflicts

If we tried to import different functions of the same name into the same top-level module file, we'd end up with conflicts and errors.

Fortunately there are a number of ways to get around this.

Renaming imports and exports : Inside your import and export statement's curly braces, you can use the keyword as along with a new feature name, to change the identifying name you will use for a feature inside the top-level module.

```js
// inside module.js
export { function1, function2 };

// inside main.js
import {
  function1 as newFunctionName,
  function2 as anotherNewFunctionName,
} from './modules/module.js';
```

See here for more details: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#avoiding_naming_conflicts


### Cheatsheet: syntax of ECMAScript modules

Ref: [JSFIP Modules ES2020](https://exploringjs.com/impatient-js/ch_modules.html#overview-syntax-of-ecmascript-modules)

#### 24.1.1 Exporting

```js
// Named exports
export function f() {}
export const one = 1;
export { foo, b as bar };

// Default exports
export default function f() {} // declaration with optional name
// Replacement for `const` (there must be exactly one value)
export default 123;

// Re-exporting from another module
export * from "./some-module.mjs";
export { foo, b as bar } from "./some-module.mjs";
```

#### 24.1.2 Importing

```js
// Named imports
import { foo, bar as b } from "./some-module.mjs";
// Namespace import
import * as someModule from "./some-module.mjs";
// Default import
import someModule from "./some-module.mjs";

// Combinations:
import someModule, * as someModule from "./some-module.mjs";
import someModule, { foo, bar as b } from "./some-module.mjs";

// Empty import (for modules with side effects)
import "./some-module.mjs";
```

### Named Export

Each module can have zero or more named exports.

We can label any declaration as exported by placing export before it, be it a variable, function or a class.

For instance, here all exports are valid:

```js
// export an array
export let months = [
  "Jan",
  "Feb",
  "Mar",
  "Apr",
  "Aug",
  "Sep",
  "Oct",
  "Nov",
  "Dec",
];

// export a constant
export const MODULES_BECAME_STANDARD_YEAR = 2015;

// export a class
export class User {
  constructor(name) {
    this.name = name;
  }
}
```

Also, we can put export separately from declarations.

Here we first declare, and then export:

```js
// 📁 say.js
function sayHi(user) {
  alert(`Hello, ${user}!`);
}

function sayBye(user) {
  alert(`Bye, ${user}!`);
}

export { sayHi, sayBye }; // a list of exported variables
```

...Or, technically we could put export above functions as well.

Summary:

- To export something, we put the keyword export in front of a declaration.
- Entities that are not exported are private to a module and can’t be accessed from outside.

WARNING: No semicolons after export class/function

Please note that export before a class or a function does not make it a function expression. It’s still a function declaration, albeit exported.

Most JavaScript style guides don’t recommend semicolons after function and class declarations.

That’s why there’s no need for a semicolon at the end of export class and export function:

```js
export function sayHi(user) {
  alert(`Hello, ${user}!`);
} // no ; at the end
```

### Named Export

### example

File structure:

```bash
calculator/
  lib/
    calc.js
  main.js
```

Define a module:

```javascript
//------ lib.js ------
export const sqrt = Math.sqrt;
export function square(x) {
  return x * x;
}
export function diag(x, y) {
  return sqrt(square(x) + square(y));
}
```

Use a module:

```javascript
//------ main.js ------
import { square, diag } from "lib";
console.log(square(11)); // 121
console.log(diag(4, 3)); // 5
```

you can also import the whole module and refer to its named exports via property notation:

```javascript
//------ main.js ------
import * as lib from "lib";
console.log(lib.square(11)); // 121
console.log(lib.diag(4, 3)); // 5
```

### Traspiler

The great news is you can use ES6 modules today! You just have to run your code through a **transpiler**

[ES6 module transpiler](https://github.com/esnext/es6-module-transpiler)
is a JavaScript library for converting JavaScript files written using the ES6 draft specification module syntax to existing library-based module systems such as AMD, CommonJS, or simply globals.
This [post](http://esnext.github.io/es6-module-transpiler/) introduce how the traspiler works.

The subset of the ES6 module syntax supported by the transpiler is described [here](https://github.com/esnext/es6-module-transpiler#supported-es6-module-syntax)

#### ES6 Module transpiler

- [ES6 Module Traspiler](https://github.com/esnext/es6-module-transpiler)
- [NPM node package](https://www.npmjs.com/package/es6-module-transpiler): npm install -g es6-module-transpiler

- [Broccoli Plugin](https://github.com/mmun/broccoli-es6-module-transpiler)

Supported syntax : https://github.com/esnext/es6-module-transpiler#supported-es6-module-syntax

How use it?

- rsvp

### HOW-TO ESM and Browser

The import statement cannot be used in embedded scripts unless such script has a type="module":

```html
<script type="module">
  ....
</script>

------------------------------------------

<!DOCTYPE html>
<script type="module">
  import { sayHi } from "./say.js";
  document.body.innerHTML = sayHi("John");
</script>
```

```js
//say.js
export function sayHi(user) {
  return `Hello, ${user}!`;
}
```

WARNING! : Modules work only via HTTP(s), not in local files

If you try to open a web-page locally, via `file://` protocol, you’ll find that import/export directives don’t work. Use a local web-server, such as static-server or use the “live server” capability of your editor, such as VS Code Live Server Extension to test modules.

Ref: [JSINFO](https://javascript.info/modules-intro)

- Good intro to ESM for beginners
- Super brief History of modules
- basic usage of import/export with browser example
- `<script type="module">` : Always "use strict", Module-level scope, A module code is evaluated only the first time when imported

#### [ADVANCED] import.meta

#### [ADVANCED] In a module, top-level "this" is undefined.

So the global scope pollution is avoided by desing. Ref: https://javascript.info/modules-intro#in-a-module-this-is-undefined

Compare it to non-module scripts, where this is a global object:

```js
<script>
  alert(this); // [object Window]
</script>

<script type="module">
  alert(this); // undefined
</script>
```

#### [ADVANCED] Module scripts are deferred

In other words:

- downloading external module scripts `<script type="module" src="...">`doesn’t block HTML processing, they load in parallel with other resources.
- module scripts wait until the HTML document is fully ready (even if they are tiny and load faster than HTML), and then run.
- relative order of scripts is maintained: scripts that go first in the document, execute first.

As a side-effect, module scripts always “see” the fully loaded HTML-page, including HTML elements below them.

```js
<script type="module">
  alert(typeof button); // object: the script can 'see' the button below
  // as modules are deferred, the script runs after the whole page is loaded
</script>

Compare to regular script below:

<script>
  alert(typeof button); // Error: button is undefined, the script can't see elements below
  // regular scripts run immediately, before the rest of the page is processed
</script>

<button id="button">Button</button>
```

Please note: the second script actually runs before the first! So we’ll see undefined first, and then object.

That’s because modules are deferred, so we wait for the document to be processed. The regular script runs immediately, so we see its output first.

When using modules, we should be aware that the HTML page shows up as it loads, and JavaScript modules run after that, so the user may see the page before the JavaScript application is ready. Some functionality may not work yet. We should put “loading indicators”, or otherwise ensure that the visitor won’t be confused by that.

#### [ADVANCED] Async on inline scripts

If you add the `async` keyword:

```js
<script async type="module">
```

The module async scripts run immediately when ready, independently of other scripts or the HTML document (otherwise it would have waited the previous html and script tags).

Also non module script support async but only works on external scripts, For module scripts, it works on inline scripts as well.

USE-CASES: functionality that doesn’t depend on anything, like counters, ads, document-level event listeners.

```js
<!-- all dependencies are fetched (analytics.js), and the script runs -->
<!-- doesn't wait for the document or other <script> tags -->
<script async type="module">
  import {counter} from './analytics.js';

  counter.count();
</script>
```

#### [ADVANCED] External module scripts

External scripts that have type="module" are different in two aspects:

1. External scripts with the same src run only once:

```js
<!-- the script my.js is fetched and executed only once -->
<script type="module" src="my.js"></script>  <!-- FETCH AND LOAD!!! -->
<script type="module" src="my.js"></script>  <!-- DO NOTING!!! -->
```

2. External scripts that are fetched from another origin (e.g. another site) require CORS headers, as described in the chapter Fetch: Cross-Origin Requests. In other words, if a module script is fetched from another origin, the remote server must supply a header Access-Control-Allow-Origin allowing the fetch.

```js
<!-- another-site.com must supply Access-Control-Allow-Origin -->
<!-- otherwise, the script won't execute -->
<script type="module" src="http://another-site.com/their.js"></script>
That ensures better security by default.
```

#### [ADVANCED] No “bare” modules allowed in a Browser

In the browser, import must get either a relative or absolute URL. Modules without any path are called “bare” modules. Such modules are not allowed in import.

For instance, this import is invalid:

```js
import { sayHi } from "sayHi"; // Error, "bare" module
// the module must have a path, e.g. './sayHi.js' or wherever the module is
```

Certain environments, like Node.js or bundle tools allow bare modules, without any path, as they have their own ways for finding modules and hooks to fine-tune them. But browsers do not support bare modules yet.

#### [ADVANCED] Compatibility, “nomodule”

Old browsers do not understand type="module". Scripts of an unknown type are just ignored. For them, it’s possible to provide a fallback using the nomodule attribute:

```js
<script type="module">
  alert("Runs in modern browsers");
</script>

<script nomodule>
  alert("Modern browsers know both type=module and nomodule, so skip this")
  alert("Old browsers ignore script with unknown type=module, but execute this.");
</script>
```

#### A notes about build tools

SEE https://javascript.info/modules-intro#build-tools

TL;DR: In real-life, browser modules are rarely used in their “raw” form. Usually, we bundle them together with a special tool such as Webpack and deploy to the production server (Eventhough it's really useful to use them raw when you teach or do some quick esperiment). That's why we use babel, webpack etc

### HOW-TO ESM and NodeJS

Native support for ES modules in Node.js:

- Node.js 12+ supports ESM natively behind the flag --experimental-modules
- Node.js 13.2.0+ supports native ESM without that flag.

Ref:

- https://nodejs.org/api/esm.html#esm_ecmascript_modules

Node.js will treat the following as ES modules when passed to node as the initial input, or when referenced by import statements within ES module code:

- Files ending in `.mjs`.

- Files ending in .js when the nearest parent package.json file contains a top-level field `"type"` with a value of `"module"`.

- Strings passed in as an argument to --eval, or piped to node via STDIN, with the flag --input-type=module.

Node.js will treat as CommonJS all other forms of input, such as .js files where the nearest parent package.json file contains no top-level "type" field, or string input without the flag --input-type. This behavior is to preserve backward compatibility. However, now that Node.js supports both CommonJS and ES modules, it is best to be explicit whenever possible. Node.js will treat the following as CommonJS when passed to node as the initial input, or when referenced by import statements within ES module code:

- Files ending in .cjs.

- Files ending in .js when the nearest parent package.json file contains a top-level field "type" with a value of "commonjs".

- Strings passed in as an argument to --eval or --print, or piped to node via STDIN, with the flag --input-type=commonjs

### HOW-TO write Hybrid npm packages (ESM and CommonJS)

https://2ality.com/2019/10/hybrid-npm-packages.html

### ES6Modules

- https://github.com/ember-cli/broccoli-es6modules

ES6Modules wraps the esperanto library. All options described for esperanto can be provided here.

### Esperanto

Refs:

- [Homepage](http://esperantojs.org/)
- [Github Homepage](https://github.com/esperantojs/esperanto)

Esperanto is a tool for converting ES6 modules to AMD, CommonJS or UMD. It's built for speed, interoperability and ease of use.

How use it?

- Ember.js

## Node Modules

Ref:

- [Intro doc](https://github.com/maxogden/art-of-node/#modular-development-workflow)
- [Official doc](https://nodejs.org/api/modules.html)
- [Module Intenals] https://medium.com/better-programming/node-js-modules-basics-to-advanced-2464001229b6

TODO:

- Does NodeJS support es6 modules in 2019? https://medium.com/the-node-js-collection/an-update-on-es6-modules-in-node-js-42c958b890c
- `export`
- `require`
- `require.resolve`

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

- `export`
- `require`
- `require.resolve`

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

- “Who is its parent? Who are its children?
- What are all the paths it took to resolve third-party modules?
- Is it completely loaded, or not?”

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

- module.filename is the fully resolved filename of the module.
- module.id is the identifier for the module. Typically, this is the fully resolved filename, except for the main module, it is ‘.’ (period), see pic 3. Main module is the module that spins up your Node application, e.g if we write node app.js in the terminal, then app.js is the main module.
- module.path is the directory name of your name module.
- module.parent is an object which refers to the parent module.
- module.children is an array of all the children module objects.
- module.loaded is a boolean property which tells us whether or not the module is done loading, or is in the process of loading.
- module.paths is an array of all the paths that Node will look up to resolve a module.

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
So, if we do console.log(**filename)within b.js, we will get /User/home/node_blog/node_modules/b/b.js. If we do console.log(**filename) within a.js, we will get /User/home/node_blog/a.js.

#### dirname

The directory name of the current module. This is the same as the path.dirname() of the **filename.
So, for the above modules, a.js and b.js.
If we do console.log(**dirname) within b.js, we will get /User/home/node_blog/node_modules/b/ and in a.js, we will get /User/home/node_blog/.
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

- git clone git@github.com:breezeight/javascript_nicola_courses.git
- cd javascript_nicola_courses
- node node-modules-under-the-hood/app_export_gotcha.js

#### Modules in Detail

It is not necessary that only a file can be a module that we require. Other than files, we also have folders as modules that we can require in.

Generally, a folder as a module is a module of modules, i.e. it contains various modules inside it to achieve functionality. This is what libraries do, they are organized in a self-contained directory and then they provide a single entry point to that directory.

There are two ways in which we can require a folder.

- Create a package.json in the root of the folder, which specifies a main module. An example package.json file might look like this:

```
{ "name" : "some-library",
  "main" : "./lib/some-library.js" }
```

If this was in a folder at ./some-library, then require('./some-library') would attempt to load ./some-library/lib/some-library.js.

This is the extent of Node.js awareness of package.json.

- If Node does not find any package.json in the root directory of the module, or in package.json if the main entry is missing or cannot be resolved. Then, Node.js will try to load index.js or index.node from that directory. For example, if there was no package.json file in the above example, then require('./some-library') would attempt to load:
- ./some-library/index.js
- ./some-library/index.node

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

- `require('./foo.js');` : load a file foo.js from the same dir of your main.js file
- `require('../foo.js');` : load from the parent dirs\*

**Non-relative** path: such as `require('xyz')` from /beep/boop/foo.js, node searches these paths in order, stopping at the first match and raising an error if nothing is found:

- `/beep/boop/node_modules/xyz`
- `/beep/node_modules/xyz`
- `/node_modules/xyz`

For each xyz directory that exists, node will:

- first look for an `xyz/package.json` to see if a `main` field exists. The "main" field defines which file should take charge if you require() the directory path.
- second, if there is no package.json or no "main" field, index.js is assumed

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

- `require` is defined by the node module system
- `import` ???? the rsvp npm package use it.... but other package no (ex: https://github.com/strongloop/express) WHY??? WHAT is the DIFFERENCE?

may be reading this will answer: https://appdividend.com/2019/01/23/javascript-import-statement-tutorial-with-example/

https://medium.com/@geekguy/javascript-modues-exports-vs-exports-whats-the-difference-9a61cdb99386

### HOWTO write a module

https://github.com/maxogden/art-of-node/#how-to-write-a-module

- By default node tries to load module/index.js when you require('module'), any other file name won't work unless you set the main field of package.json to point to it.

### Require package

https://www.npmjs.com/package/resolve

### Internals

- http://eli.thegreenplace.net/2013/05/27/how-require-loads-modules-in-node-js
- https://github.com/joyent/node/blob/master/lib/module.js#L380
- What is the purpose of Node.js module.exports and how do you use it? http://stackoverflow.com/questions/5311334/what-is-the-purpose-of-node-js-module-exports-and-how-do-you-use-it

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

Refs:
- [Getting Started JEST](https://jestjs.io/docs/getting-started)
- [The test book club](https://club.ministryoftesting.com/)
- [TJS Testing Javascript](https://testingjavascript.com/)
- https://mercedesbernard.com/blog/jest-mocking-strategies elenco di problemi e strategie

## Learning Testing in JS

### Browser Testing

TODO quando affronteremo meglio l'argomento sarà da controllare questo problema: " User Clicks a Button VS JS code" vedi  
https://docs.google.com/document/d/10Nr0ETeagEhPX02y_VXKCXRDFeaAlp85p43rRDHuJ-U/edit#heading=h.cxek2j6rx8za

### TestingJavaScript.com

#### Fundamentals of Testing in JavaScript

Summary: implement a simple JEST clone to understand how testing works

##### Throw an Error with a Simple Test in JavaScript

https://testingjavascript.com/lessons/javascript-throw-an-error-with-a-simple-test-in-javascript
02-scikit-learn-write-the-simplest-test-in-javascript-B10-8nRlQ.mp4

- Show a first implementation

##### Abstract Test Assertions into a JavaScript Assertion Library

https://testingjavascript.com/lessons/javascript-abstract-test-assertions-into-a-javascript-assertion-library
03-scikit-learn-build-a-javascript-assertion-library-rkUSQkUZQ.mp4

Objective : "Ecapsulate assertion in an assertion library", refactoring this code:

```js
expected = 10;
if (result !== expected) {
  throw new Error(`${result} is not equal to ${expected}`);
}
```

There're all kinds of assertions that we could add to our little assertion library here to make writing our test a little easier: toBe, toBeGreaterThan or toBeLessThan, and then it could take an expected value.

##### Encapsulate and Isolate Tests by building a JavaScript Testing Framework

https://testingjavascript.com/lessons/javascript-encapsulate-and-isolate-tests-by-building-a-javascript-testing-framework
04-scikit-learn-build-a-javascript-testing-framework-SJLU41U-7.mp4

One of the limitations of the way that this test is written is that as soon as one of these assertions experiences an error, the other tests are not run. It can really help developers identify what the problem is if they can see the results of all of the tests.

At this point we have implemented something really similar to what we have in the JEST tutorial https://jestjs.io/docs/getting-started

##### Support Async Tests with JavaScripts Promises through async await

05-scikit-learn-support-async-tests-with-javascripts-promises-By3WrJI-7.mp4
https://testingjavascript.com/lessons/javascript-support-async-tests-with-javascripts-promises-through-async-await

If we turn this test into an async function, and then await that callback, if that promise is rejected, then we'll land in our catch block.

##### Provide Testing Helper Functions as Globals in JavaScript

https://testingjavascript.com/lessons/javascript-provide-testing-helper-functions-as-globals-in-javascript

These testing utilities are pretty useful. We want to be able to use them throughout our application in every single one of our test files.

We could put these into a module that we would require an import into every single one of our test files, but many testing frameworks embrace the fact that you're going to be using these in every single one of your test files, and so they just make them available globally

global.test = test, and global.expect = expect.

##### Verify Custom JavaScript Tests with Jest

.... and now simply replace the global with JEST!

https://testingjavascript.com/lessons/jest-verify-custom-javascript-tests-with-jest

#### JavaScript Mocking Fundamentals

##### Intro to JavaScript Mocking Fundamentals

https://testingjavascript.com/lessons/javascript-intro-to-javascript-mocking-fundamentals

Even though what we're doing in node land without Jest is not what Jest is doing at all because Jest is in total control of the module system when it's running your test, it's enlightening to see how this might be working if we were to implement it ourselves.

The idea is that (with the exception of the first test), you look at the jest version first, then see how that would be implemented without a testing framework.

GITHUB Repo: https://github.com/kentcdodds/js-mocking-fundamentals

- Example implement monkey patching in a naive way
- An essential part of mocking is that you clean up after yourself so that you don't impact other tests that may not want to mock the thing that you want, or may want to mock it in a different way.

##### Ensure Functions are Called Correctly with JavaScript Mocks

`jest.fn`: https://jestjs.io/docs/jest-object#jestfnimplementation

Return a mock. Mock functions are also known as "spies", because they let you spy on the behavior of a function that is called indirectly by some other code, rather than only testing the output.
After you mock a function you may want to verify, for example, that it's being called with the right things at the right time.

```js
utils.getWinner = jest.fn((p1, p2) => p1);

expect(utils.getWinner.mock.calls).toEqual([
  ["Kent C. Dodds", "Ken Wheeler"],
  ["Kent C. Dodds", "Ken Wheeler"],
]);
```

A Mocks works by wrapping your function and saving data about the args you will pass each time you invoke the the mock. A naive implementation of `fn` is:

```js
function fn(impl) {
  const mockFn = (...args) => {
    mockFn.mock.calls.push(args);
    return impl(...args);
  };
  mockFn.mock = { calls: [] };
  return mockFn;
}
```

##### Restore the Original Implementation of a Mocked JavaScript Function with jest.spyOn

Ref: 04-jest-restore-the-original-implementation-of-a-mocked-javascript-function-with-jest-spyon-rJwyG2DAB.mp4

With our current usage of the mock function, we have to manually keep track of the original implementation

Jest exposes another utility that we can use to simplify this. We can run `jest.spyOn` and pass utils as the object and 'getWinner' as the method. `jest.spyOn` will replace `getWinner` with a Mock that has an additional method `mockRestore`, which we can use to restore the original function.

We have a specific implementation that we want to use for our mock function. Mock functions have an additional method on them called `mockImplementation`.

```js
// removed const originalGetWinner = utils.getWinner
spyOn(utils, 'getWinner')
utils.getWinner.mockImplementation((p1, p2) => p2)

...

// cleanup
utils.getWinner.mockRestore()
```

Implementation without framework:
https://github.com/kentcdodds/js-mocking-fundamentals/blob/main/src/no-framework/spy.js

##### Mock a JavaScript module in a test

ref:

- 05-jest-mock-a-javascript-module-in-a-test-SJW0hGEfX.mp4
- https://testingjavascript.com/lessons/jest-mock-a-javascript-module-in-a-test

In an ES module situation, monkey patching doesn't work. This happens because

We need to take things a little bit further so that we can mock the entire module, and Jest allows you to do this with the jest.mock API. The first argument to jest.mock is the path to the module that you're mocking, and that's relative to our jest.mock is being called.

The second argument is a module factory function that will return the mocked version of the module. Here, we can return an object that has getWinner and that would be a jest.fn() with our mock implementation.

```js
jest.mock("../utils", () => {
  return {
    getWinner: jest.fn((p1, p2) => p1),
  };
});

test("returns winner", () => {
  const winner = thumbWar("Kent C. Dodds", "Ken Wheeler");
  expect(winner).toBe("Kent C. Dodds");
  expect(utilsMock.getWinner.mock.calls).toEqual([
    ["Kent C. Dodds", "Ken Wheeler"],
    ["Kent C. Dodds", "Ken Wheeler"],
  ]);

  // cleanup
  utils.getWinner.mockReset();
});
```

TODO: sarebbe da rileggere questo https://mercedesbernard.com/blog/jest-mocking-strategies

##### Make a shared JavaScript mock module

Ref:

- 06-javascript-make-a-shared-javascript-mock-module-r1VVYtzMX.mp4
- https://testingjavascript.com/lessons/jest-make-a-shared-javascript-mock-module

Often you’ll want to mock the same file throughout all the tests in your codebase. So let’s make a shared mock file in Jest's `__mocks__` directory which Jest can load for us automatically.

#### Static Analysis Testing JavaScript Applications

See Also the [Addictive Confluence space](https://pitchtarget.atlassian.net/wiki/spaces/AKB/pages/12943361/Static+Analysis+and+linters)


Ref: https://testingjavascript.com/playlists/static-analysis-testing-javascript-applications-6c9c

There are tools like ESLint, TypeScript, Prettier, and more which we can use to satisfy a whole category of testing with a great developer experience: typos and incorrect types.

##### Lint JavaScript by Configuring and Running ESLint

https://testingjavascript.com/lessons/javascript-lint-javascript-by-configuring-and-running-eslint

##### Use the ESLint Extension for VSCode

https://testingjavascript.com/lessons/eslint-use-the-eslint-extension-for-vscode
03-scikit-learn-use-the-eslint-extension-for-vscode-SkwXGgcjH.mp4

a nice in-editor experience using ESLint so you don’t have to run the ESLint script to check your code and instead can identify issues as you’re writing and editing your code.

##### Use pre-built ESLint Configuration using extends

https://testingjavascript.com/lessons/eslint-use-pre-built-eslint-configuration-using-extends

Instead of configuring each one of these rules, we can say "extends", and specify a rule set that we want to extend. ESLint ships with a rule set, and it's called "eslint:recommended".

```js
  "extends": ["eslint:recommended"],
  "rules": {
    "strict": ["error", "never"]
  },
```

##### Run ESLint with npm Scripts

https://testingjavascript.com/lessons/eslint-run-eslint-with-npm-scripts

I don't actually care to lint the //dist directory, the built version of my library. What I'm going to do is I'm going to add an .eslintignore file

package.json

```js
{
  ...
  "scripts": {
     "build": "babel src --out-dir dist",
     "lint": "eslint --ignore-path .gitignore"
   },
  ...
}
```

Now I can run `npm run lint`

##### Format Code by Installing and Running Prettier

https://testingjavascript.com/lessons/javascript-format-code-by-installing-and-running-prettier-7bfbc691

Niente, di che... utile solo per chi non sa cosa sia Prettier

##### Configure Prettier

https://testingjavascript.com/lessons/eslint-configure-prettier

The Prettier project has a playground that you can play around with up in here.

##### Use the Prettier Extension for VSCode

https://testingjavascript.com/lessons/javascript-use-the-prettier-extension-for-vscode

settings.json
{
"editor.defaultFormatter": "esbenp.pretter-vscode",
"editor.formatOnSave": true,
...
}

##### Disable Unnecessary ESLint Stylistic Rules with eslint-config-prettier

Because prettier can automatically fix a lot of stylistic issues in our codebase, you could like to disable eslint check for those ( you can find it annoying while typing):

npm install --save-dev eslint-config-prettier

Add "eslint-config-prettier" to .eslintrc:

```js
{
  "parserOptions": ..... ,
  "extends": ["eslint:recommended", "eslint-config-prettier"],
  "rules": {
    "strict": ["error", "never"]
  }
}
```

##### Validate All Files are Properly Formatted with Prettier

10-scikit-learn-validate-all-files-are-properly-formatted-B14hf6_oB.mp4

To ensure our project is in good shape we created a new "validate" script that runs this new "check-format" script, our "lint" script, and our build. We made the "check-format" script by making a new "prettier" script, which contains the prettier --ignore-path and the files that we want to run "prettier" against.

```js
{
  ...
  "scripts": {
    "build": "babel src --out-dir dist",
    "lint": "eslint --ignore-path .gitignore .",
    "prettier": "prettier --ignore-path .gitignore \"**/*.+(js|json)\"",
    "format": "npm run prettier -- --write",
    "check-format": "npm run prettier -- --list-different",
    "validate": "npm run lint && npm run build"
  }
}
```

##### Avoid Common Errors by Installing and Configuring TypeScript (type checking, etc...)

11-scikit-learn-avoid-common-errors-by-installing-and-configuring-typescript-H17XjFOjB.mp4
https://testingjavascript.com/lessons/javascript-avoid-common-errors-by-installing-and-configuring-typescript


ESLint can check for a lot of things, but it’s not a great tool for checking the types of variables that flow through your application.

In this exaple:

- `tsc` is used to do the type-checking (`npm install --save-dev typescript`)
- `babel` is used to build our typescript code (`npm install --save-dev @babel/preset-typescript`)
- !!! WHY don't we use a single tool for everything ? BOH..... here there are some explanation https://www.typescriptlang.org/docs/handbook/babel-with-typescript.html 


tsconfig.json is the `tsc` config

```js
{
  "compilerOptions": {
    "noEmit": true,
    "baseUrl": "./src"
  }
}
```


package.json: add "check-types" script, configure babel and prettier to work also on ts and tsx files

```js
{
  ...
  "scripts": {
     "build": "babel src --extensions .js,.ts,.tsx --out-dir dist",
     "lint": "eslint --ignore-path .gitignore .",
     "check-types": "tsc",
     "prettier": "prettier --ignore-path .gitignore \"**/*.+(js|json|ts|tsx)\"",
     "format": "npm run prettier -- --write",
     "check-format": "npm run prettier -- --list-different",
     "validate": "npm run check-types && npm run check-format && npm run lint && npm run build"
   },
  ...
}
```

.babelrc :
```js
{
  "presets": [
    [
      .... 
    ],
    "@babel/preset-typescript"   // add typescript 
  ]
}
```

##### Make ESLint Support TypeScript Files

https://testingjavascript.com/lessons/javascript-make-eslint-support-typescript-files
12-scikit-learn-make-eslint-support-typescript-files-H16VV9OsH.mp4

* ESLint runs across TypeScript files, so I'm going to add an --ext for extension .js, .ts, and .tsx. Now when I run npm run lint, it's going to run across my TypeScript files. Of course, it still isn't configured to parse TypeScript files properly, so let's go ahead and do that next: `"lint": "eslint —-ignore-path .gitignore —ext .js,.ts,.tsx ."`

* npm install --save-dev @typescript-eslint/eslint-plugin @typescript-eslint/parser

The we need to update `.eslintrc` and override this configuration for TypeScript files:
* For "files" which matched this glob of **/*.+(ts|tsx).
* We'll set the "parser" to be "@typescript-eslint/parser". For the "parserOptions", we need to specify where our TypeScript configuration is. That's what the "project" property and the "./tsconfig.json" pointing to our configuration file.
* "plugin" configurations:We're going to have @typescript-eslint/eslint-plugin. This adds a couple additional rules that we can configure. We're not going to configure those manually, instead, we're going to extend these "extends" a couple of pre-built configurations.
* "extends": There are "plugin" configurations and the plugin is going to be from @typescript-eslint/eslint-recommended. We'll also have a plugin @typescript-eslint/recommended. What this one does is it disables some rules that are not necessary because we're using TypeScript. I'll show an example of that really quick. 
* Then we finally extended the "eslint-config-prettier", so we disable all the rules that typescript-eslint adds that we don't necessarily need because we're using Prettier.

```js
{
  ...
  "overrides": [
    {
      "files": "**/*.+(ts|tsx)",
      "parser": "@typescript-eslint/parser",
      "parserOptions": {
        "project": "./tsconfig.json"
      },
      "plugins": ["@typescript-eslint/eslint-plugin"],
      "extends:" : [
        "plugin:@typescript-eslint/eslint-recommended",
        "plugin:@typescript-eslint/recommended",
        "eslint-config-prettier/@typescript-eslint"
      ]
    }
  ]
}
```

##### Validate Code in a pre-commit git Hook with husky

https://testingjavascript.com/lessons/javascript-validate-code-in-a-pre-commit-git-hook-with-husky-c78dc757
13-scikit-learn-validate-code-in-a-pre-commit-git-hook-with-husky-Hy7aSnOoS.mp4

WARNING: il video usa una versione vecchia di husky, ora le cose si fanno come scritto qua sotto (aprile 2021, "husky": "^6.0.0")

Run `npx husky install`, Husky will configure your local Git clone to run Git hooks from the dir `.husky`:

```bash
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true
	hooksPath = .husky     /// ADDED BY HUSKY
```

To make it easier to setup a fresh new cloned repo we add "prepare" script:

```js
  "scripts": {
    ....
    "prepare": "husky install"
    ....
  },
```

Add a hook: `npx husky add .husky/pre-commit "npm test"`

Make a commit and your precommit hook will run:

```bash
$ git commit -m "Keep calm and commit"
```

If we just want to make this commit, then we can add the no verify flag to bypass this. We can add a `--no-verify` flag


##### Auto-format All Files and Validate Relevant Files in a precommit Script with lint-staged

Rather than failing when a developer has failed to format their files or run linting on all the files in the project on every commit, it would be even better to just automatically format the files on commit and only check the **relevant files** with eslint.
Let’s use `lint-staged` to run scripts on the **files that are staged to be committed** as part of our precommit hook.

ex: Git clone the example `git clone -b tjs/step-12 git@github.com:kentcdodds/static-testing-tools.git`

We're going to do a tool called lint-staged: `npm install --save-dev lint-staged`
Now at lint-staged, we're going to create a configuration file for that, `.lintstagedrc`:
* eslint
* prettier --write and 
* NOTE: in the original tutorial they use `git add` because files are going to be changed and we need to re-add them. Since v10 of lint-staged git add is automatically performed and we DON'T need to add it manually. (Ref: https://stackoverflow.com/a/63014864).

```js
{
  "*.+(js|ts|tsx)": [
    "eslint"
  ],
  "**/*.+(js|json|ts|tsx)": [
    "prettier --write"
  ]
}
```

Husky is in-charge of running some scripts on commit. We're going to instead of running the validate script, we're actually going to run lint-staged.

##### Run Multiple npm Scripts in Parallel with npm-run-all

https://testingjavascript.com/lessons/javascript-run-multiple-npm-scripts-in-parallel-with-npm-run-all

I love having this "validate" script that I can run NCI and it runs my type checking, it runs my format checking, and my linting and my build, but it kind of takes a little while. Since none of these really impact each other, it'd be really nice if I could just run these all at the same time.
To make that work, we simply installed npm-run-all in our devDependencies of our project. 

```js
npm install --save-dev npm-run-all
"validate": "npm-run-all --parallel check-types check-format lint build"
```

#### Configure Jest for Testing JavaScript Applications

Code on github: https://github.com/kentcdodds/jest-cypress-react-babel-webpack/tree/egghead-2018/config-jest-00
* a small, but real-world application that’s built with webpack and React
* 
##### Install and Run Jest

We start in a small, but real-world application that’s built with webpack and React. We’ll go over installing the Jest testing framework locally to our project, adding an npm script to make it easy to run, and adding an example test file.

Start from here: `git clone git@github.com:kentcdodds/jest-cypress-react-babel-webpack.git -b tjs/jest-00`

Install jest: `npm install --save-dev jest`
Add an npm script:

```js
"scripts": {
    "test": "jest",
    ....
```

Jest will look for "test files" when we run `jest`. So Next we need to add our tests, by default we have two alternative:
* `**/__tests__/**/*.[jt]s?(x)` : will match the `__tests__/*` glob in the terminal (all the file contained in `__test__` will match)
* `**/?(*.)+(spec|test).[tj]s?(x)` : all file ending in `test.{js|jsx|ts|tsx}` will match


Next you want to add test to the validate script: 

```js
    "validate": "npm run lint && npm run test && npm run build",
```

##### Compile Modules with Babel in Jest Tests

https://testingjavascript.com/lessons/jest-compile-modules-with-babel-in-jest-tests

Jest picks up the .babelrc automatically, so that we can benfit of all our existing babel configuration.

But if we try to run this test:

```js
import {getFormattedValue} from '../utils'

test('formats the value', () => {
  expect(getFormattedValue('1234.0')).toBe('1,234.0')
})
```

t we have a syntax error -- Unexpected Token {. What's going on here is jest runs in node, but node does not support import statements. The way that this works in our app is we're actually compiling those import statements using Webpack. But jest does't pickup also the webpack config.

The trick here is that in our Babel RC, we're configuring @babel/preset-env to not compile the modules so that Webpack can manage those.

`.babelrc.js` : 

```js
module.exports = {
  presets: [
    ['@babel/preset-env', {modules: false}],  //HERE
    '@babel/preset-react',
    [
    ...
```

If we actually remove that configuration and then try to run NPM T again, we're actually going to get things working, but now we're not going to get the benefits of **tree shaking with Webpack**.

Jest automatically defines environment variable `NODE_ENV` as `test`(see https://jestjs.io/docs/en/getting-started.html), we can use it to distinguish if we are in a test environment: if we are running jest, we are in test env and we want to compile in `commonjs`, the format supported by nodejs.

```js
const isTest = String(process.env.NODE_ENV) === 'test'

module.exports = {
  presets: [
    ['@babel/preset-env', {modules: isTest ? 'commonjs' : false}],
```