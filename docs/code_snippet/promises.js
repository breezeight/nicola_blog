new Promise((resolve, reject) => {
    setTimeout(()=> {
        console.log(1)
        resolve("Hello")
    }, 1000)  
}).then(() => console.log("2")).then(() => console.log("3"))

console.log("4")