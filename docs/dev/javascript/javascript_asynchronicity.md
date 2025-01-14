
# JavaScript Asynchronicity

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

```js
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

```js
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
