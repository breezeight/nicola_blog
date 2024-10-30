let promise = new Promise(function (resolve, reject) {
    // the function is executed automatically when the promise is constructed
    console.log("Executor is started")
    // after 1 second signal that the job is done with the result "done"
    setTimeout(() => resolve("done"), 1000);
  });
  console.log("Waiting for the promise")