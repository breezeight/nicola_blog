
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
