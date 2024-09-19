
'use strict';

// the promise becomes resolved immediately upon creation
let promise = new Promise(resolve => {
  resolve("done!");
  console.log("promise fulfilled!")
});

promise.then((result)=> console.log(`[THEN HANDLER] Promise result: ${result}`)); // done! (shows up right now)

console.log("Even if the promise is fulfilled synchronously, this console log is printed before the .then() handler is executed")

