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
- [SOJS](/Volumes/ArchiveDisk/Archive/Misc/ebook/javascript/Secrets_of_the_JavaS.pdf) http://www.manning.com/resig/
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

# VS Code Extensions: best practices

When writing JavaScript with an editor such as Visual Studio Code, there are a number of ways you can ensure your code is syntactically correct and in line with current best practices. You can use a linter to do this. Linters check your code for syntax errors and highlight errors to make sure you can quickly find and fix them. ESLint is a linter that you can integrate into your Visual Studio Code setup in order to ensure code integrity.

`ESLint` can both format your code and analyze it to make suggestions for improvement. It is also configurable. This means that you can customize how your code is evaluated.

`Prettier` reprint the entire program from scratch in a consistent way. Linter only highlight if you write but worse – they might conflict with Prettier. Luckily it’s easy to turn off rules that conflict or are unnecessary with Prettier (see #Setup).

For code formatting the best solution is to invoke `Prettier` on save of a file (see #Setup).

[Ref](https://prettier.io/docs/en/comparison.html)

## Setup

- [Ref](https://medium.com/matheus-barbosa/integrating-prettier-eslint-airbnb-style-guide-editorconfig-no-vscode-ff950263adbf)

If it's a new project use the `npm init` command to initialize your project will create a package.json.

```bash
#In VSCode, download the following extensions: ESLint, Prettier e EditorConfig.
code --install-extension dbaeumer.vscode-eslint
code --install-extension EditorConfig.EditorConfig
code --install-extension esbenp.prettier-vscode

# Install the libraries **ESLint** and **Prettier** in your project
npm install --save-dev --save-exact eslint prettier

# Install the configuration of Airbnb
npx install-peerdeps --dev eslint-config-airbnb

#  Install eslint-config-prettier (deactivate the format to ESLint) and eslint-plugin-prettier (Allows ESLint to report on format errors while typing)
npm install --save-dev --save-exact eslint-config-prettier eslint-plugin-prettier
```

Create `.editorconfig` file:

```
root = true

[]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = false
```

Create `.eslintrc.json` file:

```json
{
  "extends": ["airbnb", "prettier"],
  "plugins": ["prettier"],
  "rules": {
    "prettier/prettier": ["error"]
  }
}
```

The last step is to make sure the Prettier formatting happens when you save a file.

Insert on User Settings in VScode:

```json
"editor.formatOnSave": true
```

(To open the User Settings, use the shortcut `Ctrl + Shift + P` then search for: `_Preferences: Open Settings (JSON)_`)

NOTES:

- [eslint-config-prettier](https://github.com/prettier/eslint-config-prettier): Turns off all rules that are unnecessary or might conflict with Prettier.
- [eslint-plugin-prettier](https://github.com/prettier/eslint-plugin-prettier): Runs Prettier as an ESLint rule and reports differences as individual ESLint issues.

## ESLint

[Homepage](https://eslint.org/)

- statically analyzes your code to quickly find problems
- Customize: Preprocess code, use custom parsers, and write your own rules that work alongside ESLint's built-in rules.

At the bottom of the `.eslintrc.json` file, you will see a `rules` object.
To customize the errors that trigger ESLint or to disable ESLint’s response to certain pieces of code, you will add key-value pairs to the "rules" object. The key will match the name of the rule you want to add or change. The value will match the severity level of the issue. You have three choices for severity level:

- `error` - produces a red underline
- `warn` - will produce a yellow underline
- `off` - will not display anything.

EX: If you do not want to produce any error messages for `console.log` statements, you can use the `no-console` rule name as the key. Input off as the value for no-console:

```json
//.eslintrc.json
"rules" : {
  "no-console": "off"
}
```

Some rules require multiple pieces of information, including a severity level and a value. To specify the type of quotes you want to use in your code, you have to pass in both the chosen type of quotes and the severity level:

```json
//.eslintrc.json
"rules" : {
  "no-console": "off",
   "quotes": [
      "error",
      "double"
    ]
}
```

Now, if you include single quotes in your quote, ESLint will raise an error.

## Prettier

[Homepage](https://github.com/prettier/prettier)

- Opinionated Code Formatter
- It enforces a consistent style by parsing your code and re-printing it with its own rules that take the maximum line length into account, wrapping code when necessary.

https://prettier.io/docs/en/integrating-with-linters.html

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

- [https://yarnpkg.com/lang/en/docs/cli/list/](doc)
- all `yarn list --depth=0`
- all and their dependencies `yarn list`
- `yarn list --depth=0 --pattern react-native-localization`

Perform a vulnerability audit against the installed packages:

- [https://yarnpkg.com/en/docs/cli/audit](doc)
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
	a: 2
};

Object.getOwnPropertyDescriptor( myObject, "a" );
// {
//    value: 2,
//    writable: true,
//    enumerable: true,
//    configurable: true
// }
```

As you can see, the property descriptor (called a "data descriptor" since it's only for holding a data value) for our normal object property a is much more than just its value of 2. 

It includes 3 other characteristics:

* writable:  If a property has writable set to false then that property’s value cannot be reassigned another value.
  * example: https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch3.md#writable
* enumerable: will show up in certain object-property enumerations, such as the for..in loop
  * example: https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch3.md#enumerable
* configurable: we can modify its descriptor definition or delete the property.
  * example: https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch3.md#configurable

While we can see what the default values for the property descriptor characteristics are when we create a normal property, we can use `Object.defineProperty(..)` to add a new property, or modify an existing one (if it's configurable!), with the desired characteristics.

For example:

```js
var myObject = {};

Object.defineProperty( myObject, "a", {
	value: 2,
	writable: true,
	configurable: true,
	enumerable: true
} );

myObject.a; // 2
```

Using `defineProperty(..)`, we added the plain, normal a property to myObject in a manually explicit way. However, you generally wouldn't use this manual approach unless you wanted to modify one of the descriptor characteristics from its normal behavior.

All Object Properties have Property Descriptors:

* Every object property has a property descriptor, even if we don’t set one using the Object.defineProperty() method.
* We can use another method, Object.getOwnPropertyDescriptor(), to read a property descriptor. 


#### Enumerable and Value

Ref: https://medium.com/intrinsic/javascript-object-property-descriptors-proxies-and-preventing-extension-1e1907aa9d10

The most basic property descriptors are value and enumerable. value contains the value which will be returned when the property is being read. enumerable determines whether or not the property will be visible when listing the properties of the object. Here’s a code sample using these two property descriptors:

```js
const obj = {}
Object.defineProperty(obj, 'foo', {
  value: 'hello', // the property value
  enumerable: false // property will not be listed
})
console.log(obj) // {}
console.log(obj.foo) // 'hello'
console.log(Object.keys(obj)) // []
console.log(Reflect.ownKeys(obj)) // [ 'foo' ]
console.log('foo' in obj) // true
```

The enumerable property descriptor has been set to false:

* it becomes a harder to discover the foo property if we don’t know to look for it. 
* For example, when we call `console.log(obj)`, we get an empty object in return.`
* When we call `Object.keys(obj)`, we get an empty array in response.
* BUT If we know the name of the property we can still use the in operator, like we’re doing with 'foo' in obj, which returns a true. However, keep in mind this doesn’t completely hide the property, as we can still find it using `Reflect.ownKeys(obj)`.

#### Use-case: Enumerable

Adding a method to an object’s prototype causes that property will now be present in for...in loops and you always need to use `Object#hasOwnProperty()` when enumerating properties.
By specifically setting this enumerable property of the method to `false` you can solve the problem.

```js
const proto = {}
const obj = { ok: 1 }
obj.__proto__ = proto
for (let key in obj) console.log(key) // [ok]

proto.bad = () => 42

for (let key in obj) console.log(key) // [ok,bad]
for (let key in obj) {
  if (obj.hasOwnProperty(key)) {
    console.log(key) // [ok]
  }
}
```

In this first example we’ve created a method on our object’s prototype called bad by simply assigning the method to a property using proto.bad. What we instead need to do is the following:

```js
const proto = {}
const obj = { ok: 1 }
obj.__proto__ = proto
for (let key in obj) console.log(key) // [ok]

Object.defineProperty(proto, 'good', {
  value: () => 42,
  enumerable: false
})

for (let key in obj) console.log(key) // [ok]
```

In this new example we create a method called good, and that method is set using the more verbose Object.defineProperty() syntax. Now, when we iterate the properties of our object, we don’t see our rogue prototype method and we no longer need to use the Object#hasOwnProperty() check.

#### Writable and Configurable

If a property has writable set to false then that property’s value cannot be reassigned another value. If a property has configurable set to false then it cannot be deleted and it cannot have its property descriptor changed again. The following code example shows these two property descriptors at work:

```js
const obj = Object.defineProperty({}, 'foo', {
  value: 'hello',
  writable: false, // reassignable?
  configurable: false // deletable/redefinable?
})
obj.foo = 'bye'
console.log(obj.foo) // 'hello'
delete obj.foo
console.log(obj.foo) // 'hello'
Object.defineProperty(obj, 'foo', {
  value: 1
}) // TypeError: Cannot redefine property: foo
```

#### Getter/Setter Property Descriptors

Getters and Setters are some pretty interesting property descriptors, specifically because they allow us to call functions which we define when reading or writing to an object. These are powerful tools with security and performance considerations. The following is an example of the get and set property descriptors:

```js
const obj = { realAge: 0 }

Object.defineProperty(obj, 'age', {
  get: function() {
    return this.realAge
  },
  set: function(value) {
    this.realAge = Number(value)
  }
})

console.log(obj.age) // 0
obj.age = '32'
console.log(obj.age) // 32
```

In this example, we have an object which has a numeric realAge property. For sake of this example consider it being hidden from the outside world. Now, we also have another property called age which is how others will interact with the underlying realAge property. The get property descriptor for age will be called when we read the property, and will simply return realAge. However the set property descriptor will first take the value which is provided, convert it into a Number, and then set realAge to the number we’ve created. This feature prevents others from setting a non-numeric age value on our object and keeps our data in a consistent shape.

ES6 SYNTAX: 

```js
const obj = {
  realAge: 0,
  get age() {
    return this.realAge
  },
  set age(value) {
    this.realAge = Number(value)
  }
}
```

When using the getter/setter object literal syntax, things look a little bit different from usual:

```js
const obj2 = {
  get b() { }
}

console.log(Object.getOwnPropertyDescriptor(obj2, 'b'))
//{
//  get: Function,
//  set: undefined,
//  enumerable: true,
//  configurable: true
//} // (e.g. Accessor Property)
```

This is a different type of property descriptor, called an `Accessor Property` and looks a little different than the one before it:

* the value and writable properties are missing
* and that the get and set properties are now present.

### Immutability: Sealing, Preventing Extension, and Freezing 

Refs:

* https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch3.md#immutability
* https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze
* https://medium.com/intrinsic/javascript-object-property-descriptors-proxies-and-preventing-extension-1e1907aa9d10

Objects are extensible by default:

* they can have new properties added to them or removed from them.
* and (in engines that support `__proto__`) their `__proto__` property can be modified.

It is sometimes desired to make properties or objects that cannot be changed (either by accident or intentionally). ES5 adds support for handling that in a variety of different nuanced ways.

Sealing, Preventing Extension, and Freezing allow you to lock down an object to varying degrees:

* `Object.preventExtensions()`
* `Object.seal()`
* `Object.freeze()`

Each one of these approaches has the same effect; an object will no longer be extensible, meaning that new properties cannot be added to the object. However there are small nuances which affect each approach as well.

WARNING:

* all of these approaches create SHALLOW immutability.
* If an object has a reference to another object (array, object, function, etc), the contents of that object are not affected, and remain mutable. Example:
* For that reason you may want to consider recursively locking down objects.

```js
"use strict";

let myImmutableObject = {
  foo: [1,2,3] 
};

Object.freeze(myImmutableObject)

console.log("After freezing an object I can still modify the referenced variables")

console.log(myImmutableObject.foo); // [1,2,3]
myImmutableObject.foo.push( 4 );
console.log(myImmutableObject.foo); // [1,2,3,4]

try {
  myImmutableObject.foo = [];  
} catch (e){
  console.log("But I cannot modify the object properties")
  console.log(e)
}
```

#### Preventing Extension

`Object.preventExtensions()` 

* ADD: prevents new properties from ever being added to an object (i.e. prevents future extensions to the object).
* Existing properties can be modified and deleted
* Existing property descriptors are not modified.

`Object.isExtensible()` method to see if an object can be extended.

Note: is the weakest protection when compared to sealing and freezing

```js
const obj = { p: 'first' }
Object.preventExtensions(obj)

obj.p = 'second' // OK
obj.p2 = 'new val' // fail silently, throw in strict

console.log(obj) // { p: 'second' }
console.log(Object.isExtensible(obj)) // false
console.log(Object.getOwnPropertyDescriptor(obj, 'p'))
// { value: 'second', writable: true,
//   enumerable: true, configurable: true }
delete obj.p // OK
```

#### Sealing

`Object.seal()`:

* Every property on a sealed object will have its `configurable` property descriptor set to `false`
* `writable`, `enumerable` don't change

`Object.isSealed()` method to see if an object has been sealed.

USE-CASE: an object and you want it to adhere to a certain set of expectations regarding the properties it has, however you don’t necessarily want to prevent changes to those properties.

```js
const obj = { p: 'first' }
Object.seal(obj)

obj.p = 'second' // OK
delete obj.p // fail silently, throw in strict
obj.p2 = 'new val' // fail silently, throw in strict

console.log(obj) // { p: 'second' }
console.log(Object.isSealed(obj)) // true
console.log(Object.getOwnPropertyDescriptor(obj, 'p'))
// { value: 'second', writable: true,
//   enumerable: true, configurable: false }
```

#### Freezing

`Object.freeze()`:

* no properties can be reassigned, added, or deleted.
* each property will have both their `writable` and `configurable` values set to false

`Object.isFrozen()` method which will tell you if an object is frozen.

```js
const obj = { p: 'first' }
Object.freeze(obj)

obj.p = 'second' // fail silently, throw in strict
delete obj.p // fail silently, throw in strict
obj.p2 = 'new val' // fail silently, throw in strict

console.log(obj) // { p: 'first' }
console.log(Object.isFrozen(obj)) // true
console.log(Object.getOwnPropertyDescriptor(obj, 'p'))
// { value: 'first', writable: false,
//   enumerable: true, configurable: false }
```

#### Summary


![summary](images/js_immutability_summary.png)

Note that isExt is short for isExtensible. reassign is whether or not a property can be assigned another value. del is whether or not properties can be deleted. add is whether or not a new property can be added.

### Getter/Setter

If you don't modify and default, when you access an object property:

* the default `[[Put]]` operation completely control how values are set to existing or new properties.
* the default `[[Get]]` control how values are retrieved from existing properties.

#### Standard [[Get]]

Consider:

```js
var myObject = {
	a: 2
};

myObject.a; // 2
myObject.b; // undefined
```

According to the spec, the code above actually performs a [[Get]] operation (kinda like a function call: [[Get]]()) on the myObject:
* The default built-in [[Get]] operation for an object first inspects the object for a property of the requested name, and if it finds it, it will return the value accordingly.
* if it does not find a property of the requested name it will traverse of the [[Prototype]] chain, if any.
* if it cannot through any means come up with a value for the requested property, it instead returns the value `undefined`.

NOTE see also the Paragraph "#### Getter/Setter Property Descriptors"

#### Standard [[Put]]

If the property is present, the `[[Put]]` algorithm will roughly check:

* Is the property an accessor descriptor (see below)? If so, call the setter, if any.
* Is the property a data descriptor with writable of false? If so, silently fail in non-strict mode, or throw TypeError in strict mode.
* Otherwise, set the value to the existing property as normal.

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
	}
};

Object.defineProperty(
	myObject,	// target
	"b",		// property name
	{			// descriptor
		// define a getter for `b`
		get: function(){ return this.a * 2 },

		// make sure `b` shows up as an object property
		enumerable: true
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
	}
};

myObject.a = 2;

myObject.a; // 4
```

Note: In this example, we actually store the specified value 2 of the assignment ([[Put]] operation) into another variable _a_. The _a_ name is purely by convention for this example and implies nothing special about its behavior -- it's a normal property like any other.

### Property Existence

If you reference a variable that cannot be resolved within the applicable lexical scope look-up a `ReferenceError` is thrown.

Instead the result is undefined for a not existing object property:

```js
var myObject = {
	a: undefined
};

myObject.a; // undefined
myObject.b; // undefined
```

From a value perspective, there is no difference between these two references -- they both result in undefined, you cannot distinguish whether a property exists and holds the explicit value undefined, or whether the property does not exist and undefined was the default return value after [[Get]] failed to return something explicitly. 

How you can distinguish these two scenarios?

We can ask an object if it has a certain property without asking to get that property's value:

```js
var myObject = {
	a: 2
};

("a" in myObject);				// true
("b" in myObject);				// false

myObject.hasOwnProperty( "a" );	// true
myObject.hasOwnProperty( "b" );	// false

myObject2 = Object.create(myObject); // {}

myObject2.b //undefined
myObject2.a // 2  // gotten from the prototype
myObject2.hasOwnProperty( "a"); // false  // it belongs to the prototype

for (const property in myObject2) {
  console.log(`${property}: ${myObject2[property]}`);
}
```

`in` operator checks if:

* the property is in the object
* or exists at any higher level of the [[Prototype]] chain object

`hasOwnProperty(..)` checks:

* only if myObject has the property,
* DOESN'T traverse the prototype chain

Note: The in operator has the appearance that it will check for the existence of a value inside a container, but it actually checks for the existence of a property name. This difference is important to note with respect to arrays, as the temptation to try a check like 4 in [2, 4, 6] is strong, but this will not behave as expected:

```js
4 in [2, 4, 6]          //false  // 4 is not a property
"length" in [2, 4, 6]   //true   // "length" is a property
```
### Enumeration and Interation

https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch3.md#enumeration

The `enumerable` property descriptor means "the object will be included if the object's properties are iterated through".

In the example below you'll notice that:

* `myObject.b` in fact exists and has an accessible value` 
* but it doesn't show up in a `for..in` loop (though, surprisingly, it is revealed by the in operator existence check). 

```js
var myObject = { };

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
("b" in myObject); // true
myObject.hasOwnProperty( "b" ); // true

// .......

for (var k in myObject) {
	console.log( k, myObject[k] );
}
// "a" 2
```

* `propertyIsEnumerable(..)` tests whether the given property name exists directly on the object and is also `enumerable:true`
* `Object.keys(..)` returns an array of all enumerable properties. DON'T consult the [[Prototype]]
* `Object.getOwnPropertyNames(..)` returns an array of all properties, enumerable or not. DON'T consult the [[Prototype]]

PROBLEM: There is no built-in way to get a list of all properties consulting also the `[[Prototype]]` chain.
* SOLUTION You could approximate such a utility by recursively traversing the [[Prototype]] chain of an object, and for each level, capturing the list from Object.keys(..) -- only enumerable properties.

### Iteration

#### for...in

The `for...in` statement:

* iterates over all enumerable properties of an object that are keyed by strings (ignoring ones keyed by Symbols)
* CONSULT the [[Prototype]] 

```js
var myObject = { };

Object.defineProperty( myObject, "a", { enumerable: true, value: 2 });
Object.defineProperty( myObject, "b", { enumerable: false, value: 3 });
// Shows up the prototype behaviour
myObject2 = Object.create(myObject);
Object.defineProperty( myObject2, "c", { enumerable: true, value: 4 });

// "b" is not enumerable, "a" is defined in the Prototype
for (var k in myObject2) {
	console.log( k, myObject2[k] );
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
	console.log( myArray[i] );
}
// 1 2 3
```

#### helpers for arrays: forEach, some, every 

Each of these helpers accepts a function callback to apply to each element in the array, differing only in how they respectively respond to a return value from the callback:

`forEach(..)`
*	will iterate over all values in the array
*	ignores any callback return values

`some(..)`
*	keeps going until the end or the callback returns a true (or "truthy") value

`every(..)`
* keeps going until the end or the callback returns a false (or "falsy") value

#### for..of

If you iterate on an object with a for..in loop, you're also only getting at the values indirectly, because it's actually iterating only over the enumerable properties of the object, leaving you to access the properties manually to get the values.

if you want to iterate over the values directly instead of the array indices (or object properties), ES6 adds a `for..of` loop syntax for iterating over arrays (and objects, if the object defines its own custom iterator):

```js
var myArray = [ 1, 2, 3 ];

// Print values not indexes
for (var v of myArray) {
	console.log( v );
}
// 1
// 2
// 3
```


The for..of loop asks for an iterator object (from a default internal function known as @@iterator in spec-speak) of the thing to be iterated, and the loop then iterates over the successive return values from calling that iterator object's next() method, once for each loop iteration.

Arrays have a built-in @@iterator, so for..of works easily on them, as shown. But let's manually iterate the array, using the built-in @@iterator, to see how it works:

```js
var myArray = [ 1, 2, 3 ];
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

- An `iterable` is a data structure that wants to make its elements accessible to the public. It does so by implementing a method whose key is Symbol.iterator. That method is a factory for iterators. That is, it will create iterators.
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
iterator.next(); //{ value: undefined, done: true }
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

A function can be anonymous functions: `function(){return "test"}`

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

### Closure Example

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

### Closure Example: Common mistake in for loops

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


### Closure Example: Private variable using closures

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

### Keep state. Timers and callbacks using closures.

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

### Common Errors with events handlers and how to fix them: bind()

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

## Lexical Context (or Scope)

Ref:

* See [SOJS_2nd] 5.4
* Mozilla: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures

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

* a function,
* a block of code,
* or the catch part of a try-catch statement.

Each of these structures (functions, blocks, and catch parts) can have its own separate identifier mappings. Each of these code structures gets an associated lexical environment **every time** the **code is evaluated**.

Each `execution context` has a `lexical environment` associated with it, that contains the mapping for all identifiers defined directly in that context.

NOTE In pre-ES6 versions of JavaScript, a lexical environment could be associated with only a function. Variables could be only function scoped. This caused a lot of confusion. Because JavaScript is a C-like language, people coming from other C-like languages (such as C++, C#, or Java) naturally expected some low-level concepts, such as the existence of block scopes, to be the same. With ES6, this is finally fixed.

Scope Nesting:

* in Javascript you can access variables defined in outer code structures.
* JS supports closure

Both behaviours are supported by JS engines using a linked list of `lexical environment`: each lexical environment has to keep track of its outer (parent) lexical environment.

If an identifier can’t be found in the current environment, the outer environment is searched. This stops either when:

* the matching variable is found,
* or with a reference error if we’ve reached the global environment and there’s no sign of the searched-for identifier.

![image](https://raw.githubusercontent.com/getify/You-Dont-Know-JS/2nd-ed/scope-closures/images/fig2.png)

Ref: See [SOJS_2nd] figure 5.9

In order to support the closure, how is the outer lexical environment set when we call a function?

* JavaScript does this by taking advantage of functions as first-class objects. Whenever a function is created, a reference to the lexical environment in which the function was created is stored in an internal (meaning that you can’t access or manipulate it directly) property named [[Environment]]; double brackets is the notation that we’ll use to mark these internal properties.

Whenever a function is called:

* a new function execution context is created and pushed onto the execution context stack.
* a new associated lexical environment is created.
* Now comes the **crucial part**: For the outer environment of the newly created lexical environment, the JavaScript engine puts the environment referenced by the called function’s internal [[Environment]] property, the environment in which the now-called function was created!


NOTE: This might seem odd at first. Why don’t we just traverse the whole stack of execution contexts and search their matching environments for iden- tifier mappings? Technically, this would work in our example. But remember, a JavaScript function can be passed around as any other object, so the posi- tion of the function definition and the position from where the function is called generally aren’t related (remember closures).

### Metaphore: conversation Compiler-ScopeManager-Engine

SEE: https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch2.md#a-conversation-among-friends

TL;DR:

```js
var students = [
    { id: 14, name: "Kyle" },
    { id: 73, name: "Suzy" },
    { id: 112, name: "Frank" },
    { id: 6, name: "Sarah" }
];
```

Let's now meet the members of the JS engine that will have conversations as they process that program:

* Engine: responsible for start-to-finish compilation and execution of our JavaScript program.

* Compiler: one of Engine's friends; handles all the dirty work of parsing and code-generation.

* Scope Manager: another friend of Engine; collects and maintains a look-up list of all the declared variables/identifiers, and enforces a set of rules as to how these are accessible to currently executing code.

A typical line of code consist of two parts: declaration and initialization-assignment. Engine sees two distinct operations:

* `declaration`: which Compiler will handle during compilation
* `initialization`: which Engine will handle during execution.

Once Compiler gets to code-generation, there's more detail to consider than may be obvious. A reasonable assumption would be that Compiler will produce code for the first statement such as: "Allocate memory for a variable, label it students, then stick a reference to the array into that variable." But there's more to it.

Here's how Compiler will handle that statement:

* Encountering var students, Compiler will ask Scope Manager to see if a variable named students already exists for that particular scope bucket. If so, Compiler would ignore this declaration and move on. Otherwise, Compiler will produce code that (at execution time) asks Scope Manager to create a new variable called students in that scope bucket.

* Compiler then produces code for Engine to later execute, to handle the students = [] assignment. The code Engine runs will first ask Scope Manager if there is a variable called students accessible in the current scope bucket. If not, Engine keeps looking elsewhere (see "Nested Scope"). Once Engine finds a variable, it assigns the reference of the [ .. ] array to it.


Later, when the Engine is executing, since the declaration has an initialization assignment, Engine asks Scope Manager to look up the variable, and assigns to it once found.

### Looking up errors

Ref: https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch2.md#lookup-failures

"Reference Error: XYZ is not defined" is thrown when we cannot resolve the lookup of an identifier:

* and is a source variable 
* or When is a target variable and STRICT MODE is enabled

### var VS Accidental Global Variables

Ref: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var#Description

TL;DR:

* It is recommended to always declare variables, regardless of whether they are in a function or global scope.
* In ECMAScript 5 strict mode, assigning to an undeclared variable throws an error.


Assigning a value to an undeclared variable implicitly creates it as a global variable (it becomes a property of the global object) when the assignment is executed.

The differences between declared and undeclared variables are:

1. Declared variables (var,let,const) are constrained in the execution context in which they are declared. Undeclared variables are always global.

```js
function x() {
  y = 1;     // Throws a ReferenceError in strict mode.
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
console.log(a);                // undefined
console.log('still going...'); // still going...
var a = 1;
console.log(a);                // 1
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

* Engine: Hey Scope Manager (for the function), I have a target reference for nextStudent, ever heard of it?
* (Function) Scope Manager: Nope, never heard of it. Try the next outer scope.
* Engine: Hey Scope Manager (for the global scope), I have a target reference for nextStudent, ever heard of it?
* (Global) Scope Manager: Nope, but since we're in non-strict-mode, I helped you out and just created a global variable for you, here you go!

Yuck. This sort of accident (almost certain to lead to bugs eventually) is a great example of the protections of strict-mode, and why it's such a bad idea to not use it.

### Scope is only partially determined at compile time

Ref: https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch3.md#lookup-is-mostly-conceptual


lexical scope is partially determined during the initial compilation processing, exeption are: 

* variable that isn't declared in any lexically available scopes in the current file (ex: modules)

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
window.studentName
```

### Scope: Legal and Illegal shadowing examples


* let (in an inner scope) can always shadow an outer scope's var. var (in an inner scope) can only shadow an outer scope's let if there is a function boundary in between.

* Ref: https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch3.md#illegal-shadowing
* Examples: https://github.com/breezeight/javascript_nicola_courses/tree/master/you-dont-know-js-yet/scope-and-closure/ch3-the-scope-chain

### Function Name Scope

https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch3.md#function-name-scope

This example will create a variable in the enclosing scope (in this case, the global scope) named askQuestion:

```js
function askQuestion() {
    // ..
}
```

With this function definition you will obtain the same result of the above example but  it will not "hoist" :

```js
var askQuestion = function(){
    // ..
};
```

A 3rd, not obvious case is:

```js
var askQuestion = function ofTheTeacher(){
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

* The env your are running (Browser, Web Workers, NodeJS...)
* How you bundle and load your JS files

TODO: read this https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch4.md#chapter-4-around-the-global-scope

### Limiting Scope Exposure (BEST PRACTICE)

https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch6.md

### More about Forward Declaration in Javascript or Hoisting

See:
* http://www.i-programmer.info/programming/javascript/5364-javascript-hoisting-explained.html
* http://www.w3schools.com/js/js_hoisting.asp

**NOTE** JavaScript in _strict mode_ does not allow variables to be used if they are not declared.

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

Ref:

* Kyle Simpson https://frontendmasters.com/courses/advanced-javascript/
* YDKJSY "The (not so) Secret Lifecycle of Variables" https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch5.md

To understand Lexical Environment in JS you must understand that JS is a compiled language. Most of us think that JAVA or CPP are compiled languages because we use compilers to ship our application as bytecode or machine readable Executables, but it not the right way to classify a compiled language.

With JS we distribute our source code so a lot of people tend to say it is interpreted language but it's not. All JS engine will compile your source code before running it, every single time you execute it.

What is an interpreted language?  Let's look at Bash scripting: when the bash interpreter is running line 3, it has NO IDEA of what to expect at line 4.
Instead a compiled language read the whole source code before running it! This is the main point!

### Hoisting YDNJSY metaphor

https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch5.md#hoisting-yet-another-metaphor

The hoisting (metaphor) proposes that JS pre-processes (during compiling) the original program and re-arranges it slightly, so that all the declarations have been moved to the top of their respective scopes, before execution. Moreover, the hoisting metaphor asserts that function declarations are, in their entirety, hoisted to the top of each scope, as well.

Consider:

```js
studentName = "Suzy"
greeting();
// Hello Suzy!

function greeting() {
    console.log(`Hello ${ studentName }!`);
}

var studentName;
```

The "rule" of the hoisting metaphor is that function declarations are hoisted first, then variables immediately after all the functions. Thus, hoisting suggests that program is re-written by the JS engine to look like this:

```js
function greeting() {
    console.log(`Hello ${ studentName }!`);
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
  * NOTE: ECMAScript 5, the current official specification of the JavaScript language, does not define the behavior for function declarations inside blocks.
  * NOTE: in ES6 are allowed https://stackoverflow.com/questions/31419897/what-are-the-precise-semantics-of-block-level-functions-in-es6
  * NOTE: MY OPINION, avoid them....
  * TODO: https://stackoverflow.com/questions/25111087/why-is-a-function-declaration-within-a-condition-block-hoisted-to-function-scope

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



Puting it all together — compilation + execution:   Hoisting is simply a mental construct. You saw hoisting in action during the compilation phase in the example above. Understanding how JavaScript is compiled and executed is the key to understanding hoisting. Let’s go through one more simpler conversation in the context of hoisting and examine what happens with the code before, during and after compilation.

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

* Line 4: Hey global scope, I have an RHS reference for a variable named a. Ever heard of it?
  * The global scope has because a was registered on line 5 in the compilation phase, its value is undefined.
* Line 5: Hey global scope, I have an RHS reference for a variable named b. Ever heard of it?
  * The global scope has because b was registered on line 6 in the compilation phase, its value is undefined.
* Line 6: Hey global scope, I have an LHS reference for a variable named a. Ever heard of it?
  * The global scope has because a was registered on line 5 in the compilation phase, so the assignment occurs.
* Line 7: Hey global scope, I have an LHS reference for a variable named b. Ever heard of it?
  * The global scope has because b was registered on line 6 in the compilation phase, so the assignment occurs.
* Line 8: Hey global scope, I have an RHS reference for a variable named b. Ever heard of it?
  * The global scope has because b was registered on line 6 in the compilation phase and a value was assigned to it on line 7 in the [current] execution phase, its value is the number 2.
* Line 9: Hey global scope, I have an RHS reference for a variable named a. Ever heard of it?
  * The global scope has because a was registered on line 5 in the compilation phase and b was assigned to it on line 6 in the [current] execution phase. As b was undefined at the time of its assignment to a, the value of a is undefined.

To keep our example short and simple, I did not include functions. Note that functions are hoisted in the same way variables are. Functions get hoisted above variables during the compilation phase.

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

## Exploring how closures work

TODO: see [SOJS_2nd] ch 5.6



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

## Named parameters via destructuring

ref:
* [[ExploringJS - Exploring ES6]](http://exploringjs.com/es6/ch_parameter-handling.html#_named-parameters-via-destructuring)

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
# Destructuring

Refs:

* [ExploringJS - Exploring ES6](https://exploringjs.com/es6/ch_destructuring.html#ch_destructuring)
* [MindMap](https://drive.mindmup.com/map/10_OUi7vCUtiANR2pXZqHcwoY_WjQaXpX)

Destructuring is a convenient way of extracting multiple values from data stored in (possibly nested) objects and Arrays. It can be used in locations that receive data (such as the left-hand side of an assignment) using different patterns.


Decustructuring
	a convenient way of extracting multiple values from data stored in (possibly nested) objects and Arrays
	Where can destructuring be used?
		Variable declaration and assignment
		param definition
		for-of loops
	destructuring target pattern
		Assignment target
		Object Pattern
			Most common: match the key x assign the value to my_var
				const { x: my_var } = { x: 7, y: 3 }; // my_var = 7
			Property value shorthands https://exploringjs.com/es6/ch_destructuring.html#_more-complex-default-values
				const { x, y } = { x: 11, y: 8 }; // x = 11; y = 8 // Same as: const { x: x, y: y } = { x: 11, y: 8 };
				 with default values:
					const { x, y = 1 } = {}; // x = undefined; y = 1
			ADVANCED: values to objects https://exploringjs.com/es6/ch_destructuring.html#_object-patterns-coerce-values-to-objects
				const {length : len} = 'abc'; // len = 3
			computed Property keys https://exploringjs.com/es6/ch_destructuring.html#_computed-property-keys
				const FOO = 'foo'; const { [FOO]: f } = { foo: 123 }; // f = 123
		Array pattern
			Most common: match all elements
				const [x,y] = [ {a:1}, {b:1}]. // x = {a: 1}
			Array patterns work with iterables https://exploringjs.com/es6/ch_destructuring.html#_array-patterns-work-with-iterables (strings, array, etc)
				A value is iterable if it has a method whose key is Symbol.iterator that returns an object. { * [Symbol.iterator]() { yield 1 } }; // OK, iterable 
			Elision https://exploringjs.com/es6/ch_destructuring.html#_elision
				const [,, x, y] = ['a', 'b', 'c', 'd']; // x = 'c'; y = 'd'
			Rest Operator https://exploringjs.com/es6/ch_destructuring.html#sec_rest-operator
				const [x, ...y] = ['a', 'b', 'c']; // x='a'; y=['b', 'c']
	Default Values for Patternhttps://exploringjs.com/es6/ch_destructuring.html#sec_default-values-destructuring
		For part of the pattern (an obj prop or array element)
			missing obj prop
				const {foo: x=3, bar: y} = {}; // x = 3; y = undefined
			missing array elem
				const [x=3, y] = []; // x = 3; y = undefined
			If a part (an object property or an Array element) has no match in the source, it is matched against: 
				its default value (if specified; it’s optional)
				undefined (otherwise)
		For the whole Pattern https://exploringjs.com/es6/ch_destructuring.html#_default-values-for-patterns
			NON CAPISCO il senso ... const [{ prop: x=123 } = {}] = [{}]; 
				TODO
		provide a fallback if nothing is found in the source https://exploringjs.com/es6/ch_destructuring.html#_more-complex-default-values
		undefined triggers default values
			const {prop: y=2} = {prop: undefined}; // y = 2
		Default values are computed on demand https://exploringjs.com/es6/ch_destructuring.html#_default-values-are-computed-on-demand
		Default values can refer to other variables in the pattern https://exploringjs.com/es6/ch_destructuring.html#_default-values-can-refer-to-other-variables-in-the-pattern
			const [x=3, y=x] = []; // x=3; y=3 const [x=3, y=x] = [7]; // x=7; y=7 const [x=3, y=x] = [7, 2]; // x=7; y=2
	Examples
		Multiple return values https://exploringjs.com/es6/ch_destructuring.html#sec_multiple-return-values
	[ExploringJS - Exploring ES6] https://exploringjs.com/es6/ch_destructuring.html#ch_destructuring




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

