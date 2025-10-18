---
title: TypeScript Advanced Guide
abstract: >
  Comprehensive advanced guide to TypeScript covering learning paths, best practices, 
  core concepts, and practical implementation strategies for modern web development.
---


## Scope of the document

This document wants to be an advanced guide to Typescript, collecting all the information and best practices we decide to adopt in coherent way.

In the “Learning paths” section we collect learning materials for who is new to TS. We feasible we create and brief summary of the content provided by each resource.

# Links and Documentation

[Nicola's Typescript MindMap](https://drive.mindmup.com/map/1uicYTMNK7U71-HbLoRRtGa7ntRHBwXbI) 

({{ link_with_abstract("javascript-typescript-learningpaths.md") }})


# Why does Typescript exists? \=\> Be a TypeChecker for JS 

Ref:

* [https://basarat.gitbook.io/typescript/getting-started/why-typescript](https://basarat.gitbook.io/typescript/getting-started/why-typescript) 

The most common kinds of errors that programmers write can be described as type errors: a certain kind of value was used where a different kind of value was expected. 

The goal of TypeScript are:

*  to **be a static typechecker for JavaScript programs**  
  *  in other words, a tool that runs before your code runs (static) and ensures that the types of the program are correct (typechecked). ([Ref](https://www.typescriptlang.org/docs/handbook/intro.html))  
  * Types have proven ability to enhance code quality and understandability  
  * Types increase your agility when doing refactoring  
  * Types are one of the best forms of documentation you can have. The function signature is a theorem and the function body is the proof.  
  *   
* Provide planned features from future JavaScript editions to current JavaScript engines

**Your JavaScript is TypeScript** ➡️TypeScript is a **superset of javascript**:

* Built on top of JavaScript, TypeScript adds features to JavaScript that help us write code that is less likely to contain bugs and is easier to maintain.  
* everything you write in JS is valid TypeScript code

TypeScript provides compile time type safety for your JavaScript code. This is no surprise given its name. The great thing is that the types are completely optional. Your JavaScript code .js file can be renamed to a .ts file and TypeScript will still give you back valid .js equivalent to the original JavaScript file. TypeScript is *intentionally* and strictly a superset of JavaScript with optional Type checking.

The core of TS it’s the **Type System**, ⏭️ [see here to understand how it works](#bookmark=id.7h89pm2d6b35)

# VS Code \+ TypeScript

Basically VSCode is very well integrated with TS by design and to do most of the things that you need you need only the standard setup.

Extensions:

* Total TypeScript  
  Description: Learn TypeScript in VSCode with a TypeScript error translator and syntax guide.  
  VS Marketplace Link: [https://marketplace.visualstudio.com/items?itemName=mattpocock.ts-error-translator](https://marketplace.visualstudio.com/items?itemName=mattpocock.ts-error-translator) 

 

[https://blog.logrocket.com/9-essential-vs-code-extensions-typescript/](https://blog.logrocket.com/9-essential-vs-code-extensions-typescript/)   
To work with TS 

### TSServer integration

Tsserver is the TypeScript standalone server, it provides language services to VSCode: 

* autocomplete, inspection, navigation, and refactoring.   
* provides a “Go to Definition” feature (F12 or right click).  
* 🔥inferred value.  
  * Seeing for example the type of a variable change in the branch of a conditional is a tremendous way to build confidence in the type system


TSServer is the TypeScript standalone server. It provides language services to VSCode:

- autocomplete, inspection, navigation, and refactoring.
- provides a “Go to Definition” feature (F12 or right click).

-  🔥 inferred value: Seeing for example the type of a variable change in the branch of a conditional is a tremendous way to build confidence in the type system. Examples:		 	 	 		

1. type of a variable change in the branch

```typescript
function logMessage(message: string | null) {
  if (message) { // when you hover over the message variable, you will see that it is of type string
    console.log(message);
  }
} // when you hover over the logMessage function, you will see that it is of type (message: string | null) => void
```
Inspect individual properties in a larger object

```typescript
const foo = {
  x: [1, 2, 3], // (property) x: number[]
  bar: {
    name: 'Fred'
  }
};
// when you hover over the foo variable, you will see that it is of type { x: number[]; bar: { name: string } }
```

Inferred generic types in the middle of a chain of operations
→ In the case below, TS infers an array of strings:
```typescript
function restOfPath(path: string) {
  return path.split("/").slice(1).join("/");
  // (method) Array<string>.slice(start?: number, end?: number): string[]
} // when you hover over the restOfPath function, you will see that it is of type (path: string) => string
```

# Configure Projects for TypeScript

Ref: [https://basarat.gitbook.io/typescript/proj](https://basarat.gitbook.io/typescript/proj)	

Before everything else you need to understand how to setup a project.

To create a project using TypeScript you need to understand the various project organization language features available. In this section we will cover:

* "compilation context"  
* declaration spaces   
* modules.

Web browsers and NodeJS do not understand TypeScript code. It must first be converted to JavaScript through a process called compilation.  
The TypeScript compiler, which performs this compilation, is called \`**tsc**\`. Let’s see how we can use it.

tsconfig.json is a configuration file that is used to define the TypeScript compiler options for a project. It is used to specify the options that control how TypeScript files are compiled to JavaScript. This file is typically located at the root of a project and is used to configure the TypeScript compiler when you build your project.

## Initialize a new project

Many high level frameworks like KeystoneJS, NextJS, ReactJS can set up a project that uses TypeScript out of the box.

If you are looking for a way to setup a basic project just to make some experiment see here:

* Very basic, good for beginner: [How To Set Up a New TypeScript Project | DigitalOcean](https://www.digitalocean.com/community/tutorials/typescript-new-project)  ⏱️5 min  
* Or this that uses TS-Node, more advanced: [The fastest way to start a typescript project (in 30 seconds)](https://www.mailslurp.com/blog/fastest-way-to-start-a-typescript-project/) 

## Compilation Context \- tsconfig.js

Ref: [TypeScript: Documentation \- What is a tsconfig.json](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html) 

Compilation Context is:

* The list of files that TypeScript will parse, analyze and compile to JS (\`include\` and \`exclude\`)  
* A set of compiler options (ex: which ES7 )

tsconfig.json define our Compilation Context, includes options such as:

* **compilerOptions**: This property contains options that control the TypeScript compiler, such as the target JavaScript version, whether to generate source maps, and whether to check for type errors.  
* **include**: This property defines a list of files or glob patterns that should be included in the compilation.  
* **exclude**: This property defines a list of files or glob patterns that should be excluded from the compilation.  
* **files**: This property defines a list of files that should be included in the compilation, regardless of whether they are matched by the include or exclude properties.  
* **references**: This property defines a list of other tsconfig.json files that should be included in the compilation.

Use include and exclude to specify files / folders / globs. E.g.:

```json
{    
    "include":[
        "./folder"
    ],
    "exclude":[
        "./folder/**/*.spec.ts",
        "./folder/someSubFolder"]
}
```

For globs : \***\*/\*** (e.g. sample usage somefolder/\*\*/\*) means all folder and any files (the extensions .ts/.tsx will be assumed and if allowJs:true so will .js/.jsx)

Alternatively, you can use files to be explicit:

```json
{
    "files":[
        "./some/file.ts"
    ]
}
```

But it is not recommended as you have to keep updating it. Instead use include to just add the containing folder.

Read More here about best practices and consideration here: [https://docs.google.com/document/d/1fj1SDPrC81yDFbELpQ\_QRou-nNOyjZ1uaocja-KnkwE/edit\#bookmark=id.nnmxfbl9vw99](https://docs.google.com/document/d/1fj1SDPrC81yDFbELpQ_QRou-nNOyjZ1uaocja-KnkwE/edit#bookmark=id.nnmxfbl9vw99)	 

# Declaration Spaces

TL;DR:

* The type declaration space contains stuff that can be used as a type annotation.  
* The variable declaration space contains stuff that you can use as a variable.

E.g. the following are a few type declarations:

```typescript
class Foo {}; // both space
var foo: Foo; // var someVar = Foo;
interface Bar {}; // only declaration space
var bar: Bar; // > OK
var bar = Bar; // > ERROR
type Bas = {};
```

Notice that even though you have `interface Bar`, *you can't use it as a variable* because it doesn't contribute to the *variable declaration space*. This is shown below:

```typescript
interface Bar {};  
var bar = Bar; // ERROR: "cannot find name 'Bar'"
```

The reason why it says `cannot find name` is because the name `Bar` *is not defined* in the *variable* declaration space. That brings us to the next topic "Variable Declaration Space".

More here: [https://basarat.gitbook.io/typescript/project/declarationspaces](https://basarat.gitbook.io/typescript/project/declarationspaces) 

# Type System

REF: [Nicola's Typescript MindMap](https://drive.mindmup.com/map/1uicYTMNK7U71-HbLoRRtGa7ntRHBwXbI) : TYPE SYSTEM node is well documented

The **type system in TypeScript** is a way of adding type information to JavaScript code, which allows the TypeScript compiler to perform type checking and catch errors before the code is run:

* With the type system, you can specify the expected types for variables, function arguments, and return values, and the TypeScript compiler will validate that the code adheres to these types (this process is called “type annotation”).   
* This helps to catch errors and prevent unintended behavior, especially in large codebases where it can be difficult to keep track of the data types being used throughout the code.

TypeScript supports a variety of types including:

* primitive types (such as number, string, and boolean),  
* complex types (such as arrays and objects),   
* special types (any, unknow, void, never)  
* and user-defined types (such as classes and interfaces). 

**Your JavaScript is TypeScript** ➡️TypeScript is a **superset of javascript**:

* The type system in TypeScript is designed to be optional so that your JavaScript is TypeScript.  
* TypeScript does not block JavaScript emit in the presence of Type Errors, allowing you to progressively update your JS to TS.  
* TypeScript provides compile time type safety for your JavaScript code. This is no surprise given its name.   
* The great thing is that the types are completely optional.

Your JavaScript code .js file can be renamed to a .ts file and TypeScript will still give you back valid .js equivalent to the original JavaScript file. TypeScript is *intentionally* and strictly a superset of JavaScript with optional Type checking.

### What is typescript annotation?

TypeScript annotations are a way to add type information to JavaScript code. They allow developers to specify the type of variables, function parameters, and return values, making the code more predictable and easier to debug. This also allows the TypeScript compiler to catch type errors before the code is run, which can save time and effort during development. 

Annotation is done by adding a colon followed by the type after the variable name. 

For example, let x: number \= 5; declare that x is of type number.

In TypeScript, various elements of code can be annotated with types. Here are some examples:

* **Variables**: The type of a variable can be annotated by adding a colon and the type after the variable name. For example, let x: number \= 5; declare that x is of type number.

* **Function parameters**: The types of function parameters can be annotated by adding a colon and the type before the parameter name. For example, function add(a: number, b: number) { ... } declares that the add function takes two parameters, both of which are of type number.

* **Return type**: The return type of a function can be annotated by adding : type after the function signature. For example, function add(a: number, b: number): number { ... } declares that the add function returns a value of type number.

* **Classes and interfaces**: TypeScript allows you to create classes and interfaces and annotate their properties and methods with types.

* **Array, Tuples**: You can annotate arrays and tuples with their corresponding types.

* **Object properties**, **properties of classes**, etc.

* **Union**, **Intersection** and other advanced types

These are just a few examples of the many elements of code that can be annotated with types in TypeScript. In general, any element that can be assigned a value can have a type annotation.

### Type Annotations on Variables

Ref: [https://www.typescriptlang.org/docs/handbook/2/everyday-types.html\#type-annotations-on-variables](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-annotations-on-variables) 

When you declare a variable using const, var, or let, you can optionally add a type annotation to explicitly specify the type of the variable ([Try on Playground](https://www.typescriptlang.org/play/#code/DYUwLgBAtgngcgQyiAXBAzmATgSwHYDmEAvBAEQCCwOAxiGQNwCwAUAPRsRfdcB6-A-hAAqMAA4gICPHgD2YBGByy8QA)):

```typescript
let myName: string = "Alice";
```

📔 TypeScript doesn’t use “types on the left”-style declarations like `int x = 0;` Type annotations will always go *after* the thing being typed.

In most cases, though, this isn’t needed. Wherever possible, TypeScript tries to **automatically infer the types in your code**. 

For example, the type of a variable is inferred based on the type of its initializer ([Try on Playground](https://www.typescriptlang.org/play/#code/PTAEDkHtQFwTwA4FNQEMB27I1TAlpOqOkkgCbmgC0VoA5ALZzioNJ2h7oBmSATn0qoAzrEQo6wmHy4BzOgFgAUABskMUExZtQAXlAAiAIIq8AYyQGA3EA)):

```typescript
// No type annotation needed -- 'myName' inferred as type 'string'
let myName = "Alice";
```

For the most part you don’t need to explicitly learn the rules of inference. If you’re starting out, try using fewer type annotations than you think - you might be surprised how few you need for TypeScript to fully understand what’s going on.

### Type Annotations on Functions

Ref: [https://www.typescriptlang.org/docs/handbook/2/everyday-types.html\#functions](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#functions) 

Functions are the primary means of passing data around in JavaScript. TypeScript allows you to specify the types of both the input and output values of functions.

**Parameter Type Annotations**  
When you declare a function, you can add type annotations after each parameter to declare what types of parameters the function accepts. Parameter type annotations go after the parameter name ( [Try](https://www.typescriptlang.org/play/#code/PTAEAUEMCdIWwKYBcHVEgngBwaSA7fAeyUiQEsj8BYAKADMBXfAYwqtAHNoFkAKfPAQAuUAGck0cvk4BKUAG86oUCBXqNm9QD1de3ctAsqYogBsEAOjNFOfAEQAJBGZsAaUPdABqUIMSWSEQAqlg40ADCkGIIfPK+9gCEifayANx0AL5AA) ):

```typescript
// Parameter type annotation
function greet(name: string) {
 console.log("Hello, " + name.toUpperCase() + "!!");
}
```

When a parameter has a type annotation, arguments to that function will be checked ( [Try](https://www.typescriptlang.org/play/#code/PTAEAEFMCdoe2gZwFygEwGYAsBWAsAFAAmkAxgDYCG0koAZgK4B2pALgJZxOgDmNkrABRNKAW0ipEraOyY8AlKgBucdkQDchEKAC0e0g1Z6dWsAHU4DckVAAjWpVDRmHcaBjxoodnXcAPMkNIIgBCQj5IAUEsNHl1IA) ):

```typescript
// Would be a runtime error if executed!!
greet(42); // Argument of type 'number' is not assignable to parameter of type 'string'.
```

Even if you don’t have type annotations on your parameters, TypeScript will still check that you passed the right number of arguments.

**Return Type Annotations**

You can also add return type annotations. Return type annotations appear after the parameter list ( [Try](https://www.typescriptlang.org/play/#code/GYVwdgxgLglg9mABAcwKZQGIEMBucBOMUqAciALYBGq+AFAJQBciYF1+iA3gLABQiiAPSCBoseIliAejNky+A-OhD4kAJgBsAbj4BfIA) ):

```typescript
function getFavoriteNumber(): number {
 return 26;
}
```

Infer: 

* Much like variable type annotations, you usually don’t need a return type annotation because TypeScript will infer the function’s return type based on its return statements.  
* The type annotation in the above example doesn’t change anything. Some codebases will explicitly specify a return type for documentation purposes, to prevent accidental changes, or just for personal preference.

**Anonymous Functions - Contextual** 

Anonymous functions are a little bit different from function declarations. When a function appears in a place where TypeScript can determine how it’s going to be called, the parameters of that function are automatically given types.

Here’s an example:

```typescript
// No type annotations here, but TypeScript can spot the bug
const names = ["Alice", "Bob", "Eve"];

// Contextual typing for function
names.forEach(function (s) {
    console.log(s.toUppercase()); // <<<<< Error: Property 'toUppercase' does not exist on type 'string'. Did you mean 'toUpperCase'?
});

// Contextual typing also applies to arrow functions
names.forEach((s) => {
    console.log(s.toUppercase()); // <<<<<  Error: Property 'toUppercase' does not exist on type 'string'. Did you mean 'toUpperCase'?
});
```

Even though the parameter s  didn’t have a type annotation, TypeScript used the types of the forEach function, along with the inferred type of the array, to determine the type s will have.

This process is called **contextual typing** because the context that the function occurred within informs what type it should have.

Similar to the inference rules, you don’t need to explicitly learn how this happens, but understanding that it does happen can help you notice when type annotations aren’t needed. Later, we’ll see more examples of how the context that a value occurs in can affect its type.

### [Types can be Implicit or Explicit](https://basarat.gitbook.io/typescript/getting-started/why-typescript#types-can-be-implicit)

Implicit

```typescript
var foo = 123;
foo = '456'; // Error: cannot assign 'string' to 'number'
```

Explicit:

```typescript
var foo: number = 123;
var foo: number = '123'; // Error: cannot assign a 'string' to a 'number'
```

### [Types are structural](https://basarat.gitbook.io/typescript/getting-started/why-typescript#types-are-structural)

This means that duck typing is a first class language construct. 


```typescript
interface Point2D {
    x: number;
    y: number;
}
interface Point3D {
    x: number;
    y: number;
    z: number;
}
var point2D: Point2D = { x: 0, y: 10 }
var point3D: Point3D = { x: 0, y: 10, z: 20 }
function iTakePoint2D(point: Point2D) { /* do something */ }

iTakePoint2D(point2D); // exact match okay
iTakePoint2D(point3D); // extra information okay
iTakePoint2D({ x: 0 }); // Error: missing information `y`
```

### [Type errors do not prevent JavaScript emit](https://basarat.gitbook.io/typescript/getting-started/why-typescript#type-errors-do-not-prevent-javascript-emit)

To make it easy for you to migrate your JavaScript code to TypeScript, even if there are compilation errors, by default TypeScript will emit valid JavaScript

TODO Rileggere questo [https://basarat.gitbook.io/typescript/getting-started/why-typescript\#types-can-be-ambient](https://basarat.gitbook.io/typescript/getting-started/why-typescript#types-can-be-ambient)

### Type Categories

Types in TS are categorized in:

* Built-in Primitive types  
* Built-in Complex types  
* Built-in Special Types  
* Custom Types

### Primitive Types

Ref:

* TypeScript Handbook  [here](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#the-primitives-string-number-and-boolean) and  [here](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#less-common-primitives) 

These types are the building blocks of TypeScript and are used to define values that have a basic data type. They are not objects, and cannot be extended or modified in any way.

JavaScript has three very commonly used [primitives](https://developer.mozilla.org/en-US/docs/Glossary/Primitive): **string, number, and boolean**. Each has a corresponding type in TypeScript. As you might expect, these are the same names you’d see if you used the JavaScript typeof operator on a value of those types:

* **string** represents string values like "Hello, world"  
* **number** is for numbers like 42. JavaScript does not have a special runtime value for integers, so there’s no equivalent to int or float - everything is simply number  
* **boolean** is for the two values true and false  
* **bigint** From ES2020 onwards, there is a primitive in JavaScript used for very large integers  
* **symbol**  
* **undefined**  
* **null**

### ⭐Complex Types and Custom Type ⭐

Why is a type considered complex in typescript?

A type is considered complex in TypeScript because it **is made up of multiple values**, unlike primitive types like number, string, and boolean which have a single value.

Complex types in TypeScript include:

* **arrays, tuples, enums, interfaces, classes, and objects.**   
* **date**

While some complex types are included with the language itself (ex: Date), most of the Complex types you will work with will be **custom types** (also known as a **custom data type** or **custom object type**), they are a user-defined type that can be used to define a structure for a specific kind of object. Custom types can be created using the type, class or interface keywords

These types allow you to group multiple values together and work with them as a single unit.

For example, an array type `number[]` represents a collection of numbers, while a tuple type `[string, number]` represents a pair of values where the first value is a string and the second value is a number. An interface type, such as Person, can define the structure of an object with multiple properties.

Complex types in TypeScript provide more flexibility and power when working with data structures in your code. They allow you to describe the structure and shape of the data you are working with, which helps to catch errors early and improve the maintainability of your code.

### Special types

* **any** [https://basarat.gitbook.io/typescript/type-system\#any](https://basarat.gitbook.io/typescript/type-system#any)  
  * you can use it whenever you don’t want a particular value to cause type checking errors.  
  * It’s useful when you are migrating an existing JS codebase.  
  * is useful when you don’t want to write out a long type just to convince TypeScript that a particular line of code is okay.  
  * **Anything can be assigned.** When a value is of type any, you can access any properties of it (which will in turn be of type any), call it like a function, assign it to (or from) a value of any type, or pretty much anything else that’s syntactically legal:

```typescript
let obj: any = { x: 0 };
// None of the following lines of code will throw compiler errors.
// Using `any` disables all further type checking, and it is assumed 
// you know the environment better than TypeScript.
obj.foo();
obj();
obj.bar = 100;
obj = "hello";
const n: number = obj;
```
  * When you don’t specify a type, and TypeScript can’t infer it from context, the compiler will typically default to any.  
  * You usually want to avoid this, though, because any isn’t type-checked. Use the compiler flag [noImplicitAny](https://www.typescriptlang.org/tsconfig#noImplicitAny) to flag any implicit any as an error.

  * 🔥💥 don't abuse the use of any TL:DR; you are disabling type checking\! 

* **unknown**  
  * :void https://basarat.gitbook.io/typescript/type-system\#void  
    * represents the absence of a value. It is used as the return type of functions that do not return a value.

* **never**  
  * represents values that never occur.

### Array Type

An array is a complex type that is used to represent a collection of values.

To specify the type of an array like \[1, 2, 3\], you can use the syntax number\[\]; this syntax works for any type (e.g. string\[\] is an array of strings, and so on). You may also see this written as Array\<number\>, which means the same thing. We’ll learn more about the syntax T\<U\> when we cover generics.  
Note that \[number\] is a different thing; refer to the section on [Tuples](https://www.typescriptlang.org/docs/handbook/2/objects.html#tuple-types).

### Object Types

To define an object type, we simply list its properties and their types.

For example, here’s a function that takes a point-like object ( [try](https://www.typescriptlang.org/play?#code/PTAEBUAsFNQBwIYCcEFtoBdpIOQGdQMBPOWBAO3IHsMEMBLK80egi0KgIwCtoBjDIRLQAsACgAZgFdyAxszhJ65DAGEqVJABMAFHAwAuUAG9QADyPkpqTtgDcoIpeu2koAL4BKE+NCgQfoFBwSF+AHoRkVHRMZG+oHxMeFQANtAAdClUAOY6AERQsImaWsp00PjmoABuCClSsKygeaAA1PAY6WaedvGJ5MlpmTn5hQka2mVYlUQ1dQ0sBC3t+ulEPeLu4orKahO6phagAMwANI5GAOwePUA) ):

```typescript
// The parameter's type annotation is an object type
function printCoord(pt: { x: number, y: number }) {
  console.log("The coordinate's x value is " + pt.x);
  console.log("The coordinate's y value is " + pt.y);
}
printCoord({ x: 3, y: 7 });
```

Here, we annotated the parameter with a type with two properties \- x and y \- which are both of type number. You can use , or ; to separate the properties, and the last separator is optional either way.

The type part of each property is also optional. If you don’t specify a type, it will be assumed to be any.

#### Optional Properties

[https://www.typescriptlang.org/docs/handbook/2/everyday-types.html\#optional-properties](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#optional-properties)  
Object types can also specify that some or all of their properties are optional. To do this, add a ? after the property name ( [Try](https://www.typescriptlang.org/play?#code/GYVwdgxgLglg9mABABwE4zFAcgQwLYCmAFHAEYBWAXIgN6LAyoDOU1L6YA5gNyIA2OFgH42UDp0QBfAJS0AsAChEiAPQrEAOi2LJitYgBCcKAAtEAeQDSitBmz5idBs1aIAREdJup07jY72hEROjCzUbgCCfDAQBG4ANPyCrpHRTEwI3jLcQA) ):

```typescript
function printName(obj: { first: string; last?: string }) {
  // ...
}
// Both OK
printName({ first: "Bob" });
printName({ first: "Alice", last: "Alisson" });
```

In JavaScript, if you access a property that doesn’t exist, you’ll get the value undefined rather than a runtime error. Because of this, when you read from an optional property, you’ll have to check for undefined before using it ( [TRY](https://www.typescriptlang.org/play?#code/PTAEAEFMCdoe2gZwFygEwFYDMaCwAoAMwFcA7AYwBcBLOU0AB2mtMoDkBDAW0gAo4ARgCtUAb1CFqSSqkSVmpAOYBuUABsOcgPyz5LRaAC+ASlCiCoUBdDk6iOGsgA6NXEX9hLzZSeU4AVQYGGABhTT5jY1UQUABRACV4gHl40ABaUC5qRQALShtoTRzQakJQAHJBIS85ctAAd01ScvymOAA3agATSC6AQlB4yC4OyFBKHLG1FjGBSFd68bhQSAAPSHJiSjGJsbXuBkcCa1LQD2qNOVA+gF4b0DIeyVJe03ErfEtLW1J7Rxc3LwAAYAElEVSckmkhlAYIhlx8fkCwWgYUQEUMQKioBiSQA0tZDMdPjY7A5nK53KDwZ4oXIYXDPAitL4AkFQuFeMZMdjcXjQABBUCIDiEMYcNTbaCkDg0dpjYiIfSZOA9aWgABSHHaHAAyuRmAx8ogAJ6sDirZAEIn4AhMFjsbh8cR0mSgABEWp4iHdJmJ9tYnB4vBdUjkqE9Tp9ABp1N4I3ipABrX3GIA) ).

```typescript
function printName(obj: { first: string; last?: string }) {
  console.log(obj.last.toUpperCase()); // ERROR - might crash if 'obj.last' wasn't provided! Remove the line below to execute the example

 if (obj.last !== undefined) { 
   console.log(`${obj.first} ${obj.last.toUpperCase()}`); // OK
 }

 console.log(`${obj.first} ${obj.last?.toUpperCase()}`); // OK A safe alternative using modern JavaScript syntax:
}

printName({ first: "James"})

printName({ first: "James", last: "Kirk"})
```

### Union Type

[https://camchenry.com/blog/typescript-union-type](https://camchenry.com/blog/typescript-union-type) 

[https://camchenry.com/blog/typescript-union-type\#what-is-a-discriminated-union](https://camchenry.com/blog/typescript-union-type#what-is-a-discriminated-union) 

TypeScript’s type system allows you to build new types out of existing ones using a large variety of operators. 

A union type is a type formed from two or more other types, representing **values that may be any one of those types**. We refer to each of these types as the union’s members. For example the id param can be both a number and a string but not an object ( [Try](https://www.typescriptlang.org/play/#code/PTAEAEFMCdoe2gZwFygEwGYAsBWAsAFABmArgHYDGALgJZxmgAO0NZVAkgCYAUNnqZEgFsARjFAAfUIiosyAcwCUoAN6FQoCvURwANpAB0uuPO4AiAJpwS0UOwAioGilBnQAaiedFAbkIBfQhBQAHkAaUJmVg4eAEYABljfILBwyLkY8zR4tDNkgmCAUVgEdOiubhVQIQBPB1Q0TCw0UH9fIA) )

```typescript
function printId(id: number | string) {
 console.log("Your ID is: " + id);
}

printId(101); // OK
printId("202"); // OK
printId({ myID: 22342 }); // <<< Error Argument of type '{ myID: number; }' is not assignable to parameter of type 'string | number'.
```

#### Working with Union Types \- Narrowing \- Type Guards

It’s easy to provide a value matching a union type \- simply provide a type matching any of the union’s members. If you have a value of a union type, how do you work with it?  
TypeScript will only allow an operation if it is valid for every member of the union. 

For example, if you have the union string | number, you can’t use methods that are only available on string:

```typescript
function printId(id: number | string) {
 console.log(id.toUpperCase()); // ERROR Property 'toUpperCase' does not exist on type 'string | number'. Property 'toUpperCase' does not exist on type 'number'.
}
```

The solution is to narrow the union with code, the same as you would in JavaScript without type annotations. **Narrowing** occurs when TypeScript can deduce a more specific type for a value based on the structure of the code.

While it might not look like much, there’s actually a lot going under the covers here. Much like how TypeScript analyzes runtime values using static types, it overlays type analysis on JavaScript’s runtime control flow constructs like if/else, conditional ternaries, loops, truthiness checks, etc., which can all affect those types.

Within our if check, TypeScript sees typeof padding \=== "number" and understands that as a special form of code called a type guard. TypeScript follows possible paths of execution that our programs can take to analyze the most specific possible type of a value at a given position. It looks at these special checks (called **type guards**) and assignments, and the process of refining types to more specific types than declared is called **narrowing**. In many editors we can observe these types as they change, and we’ll even do so in our examples.

```typescript
function padLeft(padding: number | string, input: string) {
  if (typeof padding === "number") {
    return " ".repeat(padding) + input;
    // (parameter) padding: number
  }

  return padding + input;
  // (parameter) padding: string
}
```

See the paragraph “Narrowing Techniques” for a deep dive on narrowing.

The union type provides more information to the TypeScript compiler that allows it to ⚡ **prove code is safe for all possible situations ⚡**, which is a powerful tool. We may not know whether the user will pass a string, number, or object (for example) to a function, but we can guarantee that every case is handled without needing to write any unit tests to check that.

For example, TypeScript knows that only a string value will have a typeof value "string":

```typescript
function printId(id: number | string) {
  if (typeof id === "string") {
    // In this branch, id is of type 'string'
    console.log(id.toUpperCase());
  } else {
    // Here, id is of type 'number'
    console.log(id);
  }
}

printId(101); // OK
printId("202"); // OK
printId({ myID: 22342 }); // <<< Error Argument of type '{ myID: number; }' is not assignable to parameter of type 'string | number'.
```

Sometimes you’ll have a union where all the members have something in common. For example, both arrays and strings have a slice method. If every member in a union has a property in common, you can use that property without narrowing:

```typescript
// Return type is inferred as number[] | string
function getFirstThree(x: number[] | string) {
  return x.slice(0, 3);
}
```

### TypeScript Union of Literal Types

**Literal Type**  
[Ref: TS Handbook](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#literal-types) : In addition to the general types string and number, we can refer to specific strings and numbers in type positions. In the example below because constantString can only represent 1 possible string, it has a literal type representation.  

```typescript
let changingString = "Hello World";
changingString = "Olá Mundo";

// Because `changingString` can represent any possible string,
// that is how TypeScript describes it in the type system
changingString;
// ➜ let changingString: string
```
   
By themselves, literal types aren’t very valuable: It’s not much use to have a variable that can only have one value! But by combining literals into unions, you can express a much more useful concept - for example, functions that only accept a certain set of known values

You can declare a union type consisting of literal types, such as string literals, number literals or boolean literals. These will create union types that are more specific and have distinct states.

For example, we could write some business logic functions that only accept days of the week:

```typescript
type DayOfWeek =
  | "Monday"
  | "Tuesday"
  | "Wednesday"
  | "Thursday"
  | "Friday"
  | "Saturday"
  | "Sunday";

function isBusinessDay(day: DayOfWeek): boolean {
  return day !== "Saturday" && day !== "Sunday";
}

isBusinessDay("Monday"); // => true
isBusinessDay("Saturday"); // => false
isBusinessDay("Whensday");
//             ^^^^^^^^ ERROR: Argument of type '"Whensday"'
// is not assignable to parameter of type 'DayOfWeek'

```

**When should you use union type?**

Union types are a perfect fit for a situation where we know exactly what all of the possible states are, but we don't know when we compile the program which one will be used. For example, we could use union types to store:

* days of the week,  
* color palettes,  
* columns of a database table  
* [DOM event names](https://developer.mozilla.org/en-US/docs/Web/Events),  
* [finite state machine](https://en.wikipedia.org/wiki/Finite-state_machine) states

As a counterexample, something like a person's name is not a good fit for a union type, because there are essentially an infinite (or very large) number of possible states.

**When should you not use a union type?**  
Although union types are an excellent modeling tool, there are legitimate reasons to not use them:

* When the types are known at compile-time, we can use [generics](https://www.typescriptlang.org/docs/handbook/2/generics.html) instead to provide further type safety and flexibility. If the types are known ahead of time, then there is no need to use a union type.  
* When we need to enumerate all possibilities at run-time  
* When we want named values

These are just a few common reasons to not use a union type, but there are others as well. If you are interested in knowing the comprehensive difference between union types and other language features, check out my article on [the differences between union types, enums, and objects](https://camchenry.com/blog/typescript-union-vs-enum-vs-object).

### Type Aliases

[https://www.typescriptlang.org/docs/handbook/2/everyday-types.html\#type-aliases](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-aliases) 

We’ve been using object types and union types by writing them directly in type annotations. This is convenient, but it’s common to want to use the same type more than once and refer to it by a single name.

A type alias is exactly that \- a name for any type. The syntax for a type alias is ([Try](https://www.typescriptlang.org/play#code/C4TwDgpgBACg9gSwHbCgXigbwLACgpQAeAXFEgK4C2ARhAE4DceBIpFN9TuAvl3gPT8oAUUIBDAMbAANiCjAAFtADOYytDHL5SqBDF1pCervGUw0iHgBm5JFIRwkUMHWTAAwnDh0AJgAowYFJ4NwBKLGYoCUdlOAsAOmk4AHM-ACIAFR1o7x9kMWAIAHItQigANzFpcmgELTSoAGpnYHjCUK4CaKRYhKTUzOyvX3zCkqg5Sura+qaW+JAOvG48PBc3T1y-TCJSAEYABgOAGgn9o6huDqA)):

```typescript
type Point = {
  x: number;
  y: number;
};
 
// Exactly the same as the earlier example
function printCoord(pt: Point) {
  console.log("The coordinate's x value is " + pt.x);
  console.log("The coordinate's y value is " + pt.y);
}
 
printCoord({ x: 100, y: 100 });
```

You can actually use a type alias to give a name to any type at all, not just an object type. For example, a type alias can name a union type:

```typescript
type ID = number | string;
```

Note that aliases are only aliases \- you cannot use type aliases to create different/distinct “versions” of the same type. When you use the alias, it’s exactly as if you had written the aliased type. In other words, this code might look illegal, but is OK according to TypeScript because both types are aliases for the same type:

```typescript
type UserInputSanitizedString = string;
 
function sanitizeInput(str: string): UserInputSanitizedString {
  return sanitize(str);
}
 
// Create a sanitized input
let userInput = sanitizeInput(getInput());
 
// Can still be re-assigned with a string though
userInput = "new input";
```

### Interfaces \- Structurally typed type system

[https://www.typescriptlang.org/docs/handbook/2/everyday-types.html\#interfaces](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#interfaces) 

An interface declaration is another way to name an object type ([Try](https://www.typescriptlang.org/play/#code/JYOwLgpgTgZghgYwgAgAoHtRmQbwLABQyyAHgFzIgCuAtgEbQDchxAnhdfU4QL6GEwqIBGGDoQyAA5QsAYXTooAEwAUksBQxYAlLhbIE4gM7oANhAB0p9AHMVAIgAqACxSHFS0HEgByI6WQANzhTKhRgf3tkAGopMAsSbWYiA2MzS2s7J1dUjy9ff1YgkLDkCOQo2PULViTefgJpOQVlFRxSCgBGAAZugBpkdmQe7uQeJKA)):

```typescript
interface Point {
 x: number;
 y: number;
}
 
function printCoord(pt: Point) {
 console.log("The coordinate's x value is " + pt.x);
 console.log("The coordinate's y value is " + pt.y);
}
 
printCoord({ x: 100, y: 100 });
```

Just like when we used a type alias above, the example works just as if we had used an anonymous object type.🔥 TypeScript is only concerned with the structure of the value we passed to printCoord \- it only cares that it has the expected properties. 🔥Being concerned only with the structure and capabilities of types is why we call TypeScript a **structurally typed type system**.

### Differences Between Type Aliases and Interfaces

[https://www.typescriptlang.org/docs/handbook/2/everyday-types.html\#differences-between-type-aliases-and-interfaces](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#differences-between-type-aliases-and-interfaces)

Type aliases and interfaces are very similar, and in many cases you can choose between them freely. Almost all features of an interface are available in type:

* they are defined with a similar syntax  
* both can be extended (with different syntax)

the key distinction is that:

* a type cannot be re-opened to add new properties vs an interface which is always extendable.  
* Type aliases may not participate [in declaration merging, but interfaces can](https://www.typescriptlang.org/play?#code/PTAEEEDtQS0gXApgJwGYEMDGjSfdAIx2UQFoB7AB0UkQBMAoEUfO0Wgd1ADd0AbAK6IAzizp16ALgYM4SNFhwBZdAFtV-UAG8GoPaADmNAcMmhh8ZHAMMAvjLkoM2UCvWad+0ARL0A-GYWVpA29gyY5JAWLJAwGnxmbvGgALzauvpGkCZmAEQAjABMAMwALLkANBl6zABi6DB8okR4Jjg+iPSgABboovDk3jjo5pbW1d6+dGb5djLwAJ7UoABKiJTwjThpnpnGpqPBoTLMAJrkArj4kOTwYmycPOhW6AR8IrDQ8N04wmo4HHQCwYi2Waw2W1S6S8HX8gTGITsQA).  
* Interfaces may only be used to [declare the shapes of objects, not rename primitives](https://www.typescriptlang.org/play?#code/PTAEAkFMCdIcgM6gC4HcD2pIA8CGBbABwBtIl0AzUAKBFAFcEBLAOwHMUBPQs0XFgCahWyGBVwBjMrTDJMAshOhMARpD4tQ6FQCtIE5DWoixk9QEEWAeV37kARlABvaqDegAbrmL1IALlAEZGV2agBfampkbgtrWwMAJlAAXmdXdy8ff0Dg1jZwyLoAVWZ2Lh5QVHUJflAlSFxROsY5fFAWAmk6CnRoLGwmILzQQmV8JmQmDzI-SOiKgGV+CaYAL0gBBdyy1KCQ-Pn1AFFplgA5enw1PtSWS+vCsAAVAAtB4QQWOEMKBuYVUiVCYvYQsUTQcRSBDGMGmKSgAAa-VEgiQe2GLgKQA).  
* Interface names will [always appear in their original form](https://www.typescriptlang.org/play?#code/PTAEGEHsFsAcEsA2BTATqNrLusgzngIYDm+oA7koqIYuYQJ56gCueyoAUCKAC4AWHAHaFcoSADMaQ0PCG80EwgGNkALk6c5C1EtWgAsqOi1QAb06groEbjWg8vVHOKcAvpokshy3vEgyyMr8kEbQJogAFND2YREAlOaW1soBeJAoAHSIkMTRmbbI8e6aPMiZxJmgACqCGKhY6ABGyDnkFFQ0dIzMbBwCwqIccabcYLyQoKjIEmh8kwN8DLAc5PzwwbLMyAAeK77IACYaQSEjUWY2Q-YAjABMAMwALA+gbsVjNXW8yxySoAADaAA0CCaZbPh1XYqXgOIY0ZgmcK0AA0nyaLFhhGY8F4AHJmEJILCWsgZId4NNfIgGFdcIcUTVfgBlZTOWC8T7kAJ42G4eT+GS42QyRaYbCgXAEEguTzeXyCjDBSAAQSE8Ai0Xsl0K9kcziExDeiQs1lAqSE6SyOTy0AKQ2KHk4p1V6s1OuuoHuzwArMagA) in error messages, but only when they are used by name.

For the most part, **you can choose based on personal preference**, and TypeScript will tell you if it needs something to be the other kind of declaration. If you would like a heuristic, use interface until you need to use features from type.

#### Extending Declarations

**Interfaces** can be extended using the `extends` keyword:

```typescript
interface Animal {
  name: string
}

interface Bear extends Animal {
  honey: boolean
}

const bear = getBear()
bear.name
bear.honey
```

**Types** can be extended using intersection types (`&`):

```typescript
type Animal = {
  name: string
}

type Bear = Animal & {
  honey: boolean
}

const bear = getBear();
bear.name;
bear.honey;
```

#### Modifying Existing Declarations - adding new properties

**Interfaces** can be extended multiple times (interface merging). You can extend an existing interface by declaring it multiple times. TypeScript merges the declarations:

```typescript
// First declaration of the 'User' interface
interface User {
  name: string;
}

// Second declaration of the same 'User' interface
// This adds a new property, not overwrites it
interface User {
  age: number;
}

// The merged 'User' interface now has both 'name' and 'age'
const user: User = {
  name: "Alice",
  age: 30
};

console.log(user); // { name: 'Alice', age: 30 }    
```

**❌ Type Aliases Cannot Be Merged**. Unlike interfaces, type aliases **cannot be declared multiple times with the same name**:

```typescript
type User = {
  title: string
}

type User = {
  ts: TypeScriptAPI
}
// Error: Duplicate identifier 'User'.
```

### Type Assertions - AS

[https://www.typescriptlang.org/docs/handbook/2/everyday-types.html\#type-assertions](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions) 

Sometimes you will have information about the type of a value that TypeScript can’t know about.  
For example, if you’re using document.getElementById, TypeScript only knows that this will return some kind of HTMLElement, but you might know that your page will always have an HTMLCanvasElement with a given ID.  
In this situation, you can use a type assertion to specify a more specific type:

```typescript
const myCanvas = document.getElementById("main_canvas") as HTMLCanvasElement;
```

[Try](https://www.typescriptlang.org/play/#code/MYewdgzgLgBAtgTwMIEMwDcURgXhgExGAFc4BTMKAOgHMyoBRAGzPMoCEEBJfACgCI4KAJZgA+sDSYI-AJQwsMABIAVALIAZVBizNWFKAG4gA)

Like a type annotation, type assertions are removed by the compiler and won’t affect the runtime behavior of your code.  
You can also use the angle-bracket syntax (except if the code is in a .tsx file), which is equivalent:

```typescript
const myCanvas = <HTMLCanvasElement>document.getElementById("main_canvas");
```

TypeScript only allows type assertions which convert to a more specific or less specific version of a type. This rule prevents “impossible” coercions like:

```typescript
const x = "hello" as number;
```

Conversion of type 'string' to type 'number' may be a mistake because neither type sufficiently overlaps with the other. If this was intentional, convert the expression to 'unknown' first.

Sometimes this rule can be too conservative and will disallow more complex coercions that might be valid. If this happens, you can use two assertions, first to any (or unknown, which we’ll introduce later), then to the desired type:

```typescript
const a = (expr as any) as T;
```

### Literal inference - `as` and `as const`

Ref: [https://www.typescriptlang.org/docs/handbook/2/everyday-types.html\#literal-inference](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#literal-inference) 

```typescript
const req = { url: "https://example.com", method: "GET" };
handleRequest(req.url, req.method); // COMPILE ERROR Argument of type 'string' is not assignable to parameter of type '"GET" | "POST"'.
```

In the above example req.method is inferred to be string, not "GET". Because code can be evaluated between the creation of req and the call of handleRequest which could assign a new string like "GUESS" to req.method, TypeScript considers this code to have an error.

There are two ways to work around this:

1. You can change the inference by adding a type assertion in either location:

```typescript
// Change 1:
const req = { url: "https://example.com", method: "GET" as "GET" };
// Change 2
handleRequest(req.url, req.method as "GET");
```

Change 1 means “I intend for req.method to always have the literal type "GET"”, preventing the possible assignment of "GUESS" to that field after. Change 2 means “I know for other reasons that req.method has the value "GET"“.

2. You can use as const to convert the entire object to be type literals:

```typescript
const req = { url: "https://example.com", method: "GET" } as const;
handleRequest(req.url, req.method);
```

The `as const` suffix acts like `const` but for the type system, ensuring that all properties are assigned the literal type instead of a more general version like string or number.

### Discriminated Union Type or "distinguished union" or "tagged union"

[https://camchenry.com/blog/typescript-union-type\#what-is-a-discriminated-union](https://camchenry.com/blog/typescript-union-type#what-is-a-discriminated-union) 

A **discriminated union** (also called "**distinguished union**" or **"tagged union**") is a special case of a union type that allows us to easily differentiate between the types within it.

This is accomplished by adding a field to each type that has a unique value, which can be used to differentiate between the types using an equality type guard.

For example, if we had a type which represented all possible events that could occur, we could give each event a unique name. Then, we just nease we are handling.

```typescript
type AppEvent =
  | { kind: "click"; x: number; y: number }
  | { kind: "keypress"; key: string; code: number }
  | { kind: "focus"; element: HTMLElement };

function handleEvent(event: AppEvent) {
  switch (event.kind) {
    case "click":
      // We know it is a mouse click, so we can access `x` and `y` now
      console.log(`Mouse clicked at (${event.x}, ${event.y})`);
      break;
    case "keypress":
      // We know it is a key press, so we can access `key` and `code` now
      console.log(`Key pressed: (key=${event.key}, code=${event.code})`);
      break;
    case "focus":
      // We know it is a focus event, so we can access `element`
      console.log(`Focused element: ${event.element.tagName}`);
      break;
  }
}
```

In this example, the advantage is that we can have completely disparate types in our union, and easily handle each case with just a single if check. This lends itself well to extension, because we can easily add new events and new cases to our application and lean on TypeScript to ensure that we don't forget to handle them.

Example (by Popock): use discriminated union to give special property ("role" in the example): we are going to require the field "superAdminPassword" only if the role is "super-admin"

* [https://youtu.be/p6dO9u0M7MQ?t=3304](https://youtu.be/p6dO9u0M7MQ?t=3304)   
* ([TRY playground](https://www.typescriptlang.org/play?strict=false#code/C4TwDgpgBAqgzhATlAvFA3gKClAlgEwC4oA7AVwFsAjJAbmygDNdE5gA5AQwogH5i2iXCQDm9HABtObLj35RBwsZgC+UAGRQAFAxxYcBqIgD2EiMQBEnfBWEXxhqNdskACtLgB3Y4iILgQqIOOCoMAD4YugYmZpZkCIj2UaE4EfqOMeZQFnBkkIgAtM52wQa5+QCCNsLucF4+fopByZgAlJgdEAAeYD7AUADGxiRsToTwSKiROATEAIwANAyZlsUkFks4a7X1vpb4cJwWqh2YAPRnUBUSwEgknMC4AG7QAMogJMCcXR2gkFAAJVMEAqwACuCoZFucCmOkM6UMK2yaySjic1TcHm8e38gWUhhSUDSURwSIs8SQqIMhOJaLJ5SQRQxVMMDMQVRcO2xjXBzQJbV+4GgE0QAH0ngAmKbpWakSg0RAOZisDjcPgCXn4qBSGRq+RNZRqTRAsyg8GQ6GnIA)) 

Application: [(44:02)](https://youtu.be/tDT214cE6Lo?list=PLj6YeMhvp2S40Q-TEPEKOeypLvTVd5uME&t=2638) Conditional params that are dependent on the value of another param, for example: myObj.prop2 is required only if myObj.prop1 is true. \-\> Use discriminated Union

### Utility Types

#### Union and Extract / Exclude

Tutorial: [Everything You Need To Know About TypeScript Union Types](https://camchenry.com/blog/typescript-union-type#how-to-get-a-single-type-from-a-union-type)   
Reference:

* Extract Ref: [https://www.typescriptlang.org/docs/handbook/utility-types.html\#extracttype-union](https://www.typescriptlang.org/docs/handbook/utility-types.html#extracttype-union)    
* Exclude Ref:  [https://www.typescriptlang.org/docs/handbook/utility-types.html\#excludeuniontype-excludedmembers](https://www.typescriptlang.org/docs/handbook/utility-types.html#excludeuniontype-excludedmembers) 

For the most part, `Extract` and `Exclude` are interchangeable, they are just complements of each other. So the general rule for when to use them is:

* Use `Extract` when you only need to extract a few types from a union type  
* Use `Exclude` when you need to extract most types from a union type

Sometimes, we want to deal with just a single type from union type, or a subset of the types. Thankfully, TypeScript provides a built-in utility type called [Extract](https://camchenry.com/blog/typescript-utility-types#extracttype-union) to *extract* a single type from a union type (NOTE: Exclude is very similar).

`Exclude<UnionType, ExcludedMembers>`:  Constructs a type by excluding from UnionType all union members that are assignable to ExcludedMembers.

Using the DayOfWeek type from before, we can extract individual days from the type:

```typescript
type DayOfWeek =  
  | "Monday"  
  | "Tuesday"  
  | "Wednesday"  
  | "Thursday"  
  | "Friday"  
  | "Saturday"  
  | "Sunday";

type BusinessDay = Extract<  
  DayOfWeek,  
  "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday"  
>;   // => "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday"

type Weekend = Extract<DayOfWeek, "Saturday" | "Sunday">;  // => "Saturday" | "Sunday"
```

This might seem redundant, but the advantage is that we are deriving types based on our DayOfWeek type. So, if the base type ever changes, we can be sure that all of our types are still valid.

### null and undefined

JavaScript has two primitive values used to signal absent or uninitialized value: null and undefined.

TypeScript has two corresponding types by the same names. How these types behave depends on whether you have the [strictNullChecks](https://www.typescriptlang.org/tsconfig#strictNullChecks) option on.

**strictNullChecks OFF**  
With [strictNullChecks](https://www.typescriptlang.org/tsconfig#strictNullChecks) off, values that might be null or undefined can still be accessed normally, and the values null and undefined can be assigned to a property of any type. This is similar to how languages without null checks (e.g. C\#, Java) behave. The lack of checking for these values tends to be a major source of bugs; we always recommend people turn [strictNullChecks](https://www.typescriptlang.org/tsconfig#strictNullChecks) on if it’s practical to do so in their codebase. This example ( [try](https://www.typescriptlang.org/play?strictNullChecks=false#code/GYVwdgxgLglg9mABAcwE4FN1QBRgIYC26AXIgM5SoxjICUiA3gLABQiiECZcANugHQ84ybAAMAEuh5DEAEgb4i-KHACqAB3XpUAYTxl02WgF9R9APTnEAJVUA5ACoBJALIBRRG+vWA8tfYARG4AHugQIFDoACaIAFJ4AG54AMoQVOpQiABieDB8UcQB7HpgYHCZGHgx6qhwWqiw6GSIcMCIYCDSiNiVUdTIiADkKhr1egaD9KzGrKxomDgd0rQA3EA) ) has strictNullChecks OFF and JS will crash at runtime:

```typescript
function greet(name: string) {
  console.log(`Hello ${name.toUpperCase()}`) // RUNTIME ERROR  "Executed JavaScript Failed:"  Cannot read properties of null (reading 'toUpperCase') 
}

greet(null);
```

**strictNullChecks ON (**or **strict ON with strictNullChecks OFF)**  
With [strictNullChecks](https://www.typescriptlang.org/tsconfig#strictNullChecks) on, when a value is null or undefined, the TS compiler will show us an error ( [try](https://www.typescriptlang.org/play?#code/GYVwdgxgLglg9mABAcwE4FN1QBRgIYC26AXIgM5SoxjICUiA3gLABQiiECZcANugHQ84ybAAMAEuh5DEAEgb4i-KHACqAB3XpUAYTxl02WgF9RtVsdas0mHGBDTaAbkQB6V4h0B5ALIAFAEkAGQBRRBCAJQivCMQAQVRkECIwKEQ4YEQoAE8tRABye2l8xBgyRDA4NP0yGGR8ACM+LLhEdTxUQixtdMycvPyKKhp8-iA) ):

```typescript
function greet(name: string) {
 console.log(`Hello ${name.toUpperCase()}`)
}

greet(null); // COMPILE ERROR Argument of type 'null' is not assignable to parameter of type 'string'.
```

This is great, but what if you want to allow the null value, and print out "Hello Buddy" in the null case?  
You will need to test for those values before using methods or properties on that value. Just like checking for undefined before using an optional property, we can use **narrowing** to check for values that might be null and make x an union type string | null:  
( [try](https://www.typescriptlang.org/play?ssl=10&ssc=13&pln=1&pc=1#code/GYVwdgxgLglg9mABAcwE4FN1QBRgIYC26AXIgM5SoxjKIA+iYIANswJSIDeAsAFCKIA9IIgIycZugB0zOMmwADABLpWcRABJO+IlKhwAqgAcj6VAGE8ZdNjYBfBR2GJzAeQCyABQCSAGQCiiP4ASsGuwYgA5DrokYgwZIhGcGRkMABGzACeUUyskVJ8AjDAiLiE6BycQoIx8YlQABaoIFA5RQKIomDikjJyiipqmtoVeoYmZpbWtg5sHXaIqtZcHQLdvdKy8sqqsogAQiAAJsdZjgt8dnx8aJg4eewA3EA) )

```typescript
function greet(name: string | null) {
 //console.log(`Hello ${name.toUpperCase()}`) // COMPILE ERROR 'name' is possibly 'null'.
 if (name) { //name is thruty
   console.log(`Hello ${name.toUpperCase()}`)
 } else {
   console.log(`Hello Buddy`)
 }
}

greet(null);
```

To manage also undefined you need to add it as well to the union type:  
 
```typescript
function greet(name: string | null | undefined) {
 //console.log(`Hello ${name.toUpperCase()}`) // COMPILE ERROR 'name' is possibly 'null'.
 if (name) { //name is thruty
   console.log(`Hello ${name.toUpperCase()}`)
 } else {
   console.log(`Hello Buddy`)
 }
 if (name === undefined) {
   console.log(`Hello Guest`)
 }
}

greet(null);
greet(undefined);  
```

### Non-null Assertion Operator (Postfix \!)

TODO: [https://www.typescriptlang.org/docs/handbook/2/everyday-types.html\#non-null-assertion-operator-postfix-](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#non-null-assertion-operator-postfix-) 

TODO con calma, non ne vedo tanto l'utilità al momento....

### Optional Chaining .?

[Optional Chaining](https://youtu.be/d56mG7DezGs?t=3555)  
See here: [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional\_chaining](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)

```typescript
//Optional property accessor operator
customer.?birthday.?getFullYear()

// Optional element accessor operator
myarray.?[0]

// Optional Call
myfunction.?(...)

```

Ref:

- [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical\_AND](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND) 

### Enum Type

[https://www.typescriptlang.org/docs/handbook/enums.html](https://www.typescriptlang.org/docs/handbook/enums.html)

## Narrowing Techniques 

[https://www.typescriptlang.org/docs/handbook/2/narrowing.html](https://www.typescriptlang.org/docs/handbook/2/narrowing.html) 

Narrowing in TypeScript refers to the process of refining or narrowing down the type of a value based on some conditions or logic. The purpose of narrowing is to **increase the accuracy of type information**, which can lead to more reliable and safer code. By narrowing the type of a value, TypeScript can better check for type mismatches and potential runtime errors.

if you check the example function below you will see how TypeScript analyzes runtime values using static types.   
In TypeScript, checking against the value returned by typeof is a type guard:

* it overlays type analysis on JavaScript’s runtime control flow constructs like if/else, conditional ternaries, loops, truthiness checks, etc., which can all affect those types.  
* Because TypeScript encodes how typeof operates on different values, it knows about some of its quirks in JavaScript. For example, notice that in the list above strs can be null, so \`typeof null\` can return "object", causing the error `Uncaught TypeError: null is not iterable`

```typescript
function printAll(strs: string | string[] | null) {
  // TypeScript error occurs here if we only check typeof,
  // because (typeof null === "object"), so 'strs' could still be null
  if (typeof strs === "object") {  // ❌ Error: 'strs' is possibly 'null'
    for (const s of strs) {
      console.log(s);
    }
  } else if (typeof strs === "string") {
    console.log(strs);
  } else {
    // do nothing
  }
}
```

There are several techniques for narrowing types in TypeScript, including type guards, conditional types, type aliases, type inference, and type casting. These techniques allow you to specify more precise types for variables, functions, and expressions, making it easier to catch type-related errors at compile-time.

- typeof type guards  
- Truthiness narrowing  
- Equality narrowing  
- The in operator narrowing  
- instanceof narrowing  
- Assignments  
- Control flow analysis  
- Using type predicates  
- Discriminated unions  
- The never type  
- Exhaustiveness checking

### typeof guards

As we’ve seen, JavaScript supports a typeof operator which can give very basic information about the type of values we have at runtime. TypeScript expects this to return a certain set of strings:

- "string"  
- "number"  
- "bigint"  
- "boolean"  
- "symbol"  
- "undefined"  
- "object"  
- "function"

Like we saw with padLeft, this operator comes up pretty often in a number of JavaScript libraries, and TypeScript can understand it to narrow types in different branches.

In TypeScript, checking against the value returned by typeof is a **type guard**. 

Because TypeScript encodes how typeof operates on different values, it knows about some of its quirks in JavaScript. For example, notice that in the list above, typeof doesn’t return the string null. Check out the following example: [https://www.typescriptlang.org/docs/handbook/2/narrowing.html\#typeof-type-guards](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#typeof-type-guards) 

### Truthiness narrowing

It's especially useful for guarding against values like null or undefined.  
See example here [https://www.typescriptlang.org/docs/handbook/2/narrowing.html\#truthiness-narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#truthiness-narrowing) 

In JavaScript, constructs like `if` first “coerce” their conditions to `boolean`s to make sense of them, and then choose their branches depending on whether the result is `true` or `false`. Values like

* `0`  
* `NaN`  
* `""` (the empty string)  
* `0n` (the `bigint` version of zero)  
* `null`  
* `undefined`

all coerce to `false`, and other values get coerced to `true`.

### Equality Narrowing

see [https://www.typescriptlang.org/docs/handbook/2/narrowing.html\#equality-narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#equality-narrowing)

### The in operator narrowing

[https://www.typescriptlang.org/docs/handbook/2/narrowing.html\#the-in-operator-narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#the-in-operator-narrowing) 

JavaScript has an operator for determining if an object has a property with a name: the in operator. TypeScript takes this into account as a way to narrow down potential types.

```typescript
type Fish = { swim: () => void };
type Bird = { fly: () => void };
 
function move(animal: Fish | Bird) {
  if ("swim" in animal) {
    return animal.swim();
  }
 
  return animal.fly();
}
```

### instanceof narrowing

[https://www.typescriptlang.org/docs/handbook/2/narrowing.html\#instanceof-narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#instanceof-narrowing) 

JavaScript has an operator for checking whether or not a value is an “instance” of another value. 

More specifically, in JavaScript x instanceof Foo checks whether the prototype chain of x contains Foo.prototype. 

While we won’t dive deep here, and you’ll see more of this when we get into classes, they can still be useful for most values that can be constructed with new. 

As you might have guessed, instanceof is also a type guard, and TypeScript narrows in branches guarded by instanceofs.

```typescript
function logValue(x: Date | string) {
  if (x instanceof Date) {
    console.log(x.toUTCString());
               
(parameter) x: Date
  } else {
    console.log(x.toUpperCase());
               
(parameter) x: string
  }
}
```

### Assignments

When we assign to any variable, TypeScript looks at the right side of the assignment and narrows the left side appropriately. In [this example](https://www.typescriptlang.org/play?#code/DYUwLgBAdgrgtgIxAJwPoHs0GczIJZQDmEAXNPEshAD4Q75EQC8EAjANwCwAUDwMbooWdKAB0wdIQAUYAJ4AHEOgBm5RCgzZcBQgEoIAegMQARLHXITPHucqbU9Hc1PC44ABY6Th4wHkA0hBg6BAAhlhYeIRQYXTajEh8oTBYIBAA7mkgAB7ywHh8eGDAshAAJiB8wKHIIGVB7mkAbjV4oQigYVhhMTBQeIJBCiDW3AJCIiDikjLDKmp2mA7xej4uK1a83KCQgiWotijOHKPjwmIS0nKK83uyBxQo+kamh5ajdw8WziauHl4QQEvAAqAE0AAoAUQgkIASrDfLCADQNNJ4OB5ArlSrVZChMADGKnQTnKaXWY3VSfN7PYy-DZAA) the variable only\_number is implicitly defined by the RHV

```typescript
let only_number = 1;
console.log(typeof only_number) // "number"
only_number = "something"   // TYPE ERROR, the implic declaration 
console.log(typeof only_number) // "string"
```

### Control flow analysis

[https://www.typescriptlang.org/docs/handbook/2/narrowing.html\#control-flow-analysis](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#control-flow-analysis)

Up until this point, we’ve gone through some basic examples of how TypeScript narrows within specific branches. But there’s a bit more going on than just walking up from every variable and looking for type guards in ifs, whiles, conditionals, etc. For example ([Try](https://www.typescriptlang.org/play/#code/GYVwdgxgLglg9mABABwIYBMAyBTYUAUa66MYA5gFyJggC2ARtgE6IA+iAzlE6WQDSJSyEFCpce5AJSIA3gChEg4InxQAnsmxxlREuUQBeI4gBENBsxPT5ixU2xQQTJCdMA6e5tQFdvaQGpBMGEoAG4FRABfCPtHZxQMPTJEQKERcMigA)):

```typescript
function padLeft(padding: number | string, input: string) {
 if (typeof padding === "number") {
   return " ".repeat(padding) + input;
 }
 return padding + input;
}
```

padLeft returns from within its first if block. TypeScript was able to analyze this code and see that:

* the rest of the body (return padding \+ input;) is unreachable in the case where padding is a number. As a result, it was able to remove number from the type of padding (narrowing from string | number to string) for the rest of the function.

This analysis of code based on reachability is called **control flow analysis**, and TypeScript uses this flow analysis to narrow types as it encounters type guards and assignments. When a variable is analyzed, control flow can split off and re-merge over and over again, and that variable can be observed to have a different type at each point.

### Using type predicates

[https://www.typescriptlang.org/docs/handbook/2/narrowing.html\#using-type-predicates](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#using-type-predicates)   
TODO: Using type predicates ??????????

### The never type

[https://www.typescriptlang.org/docs/handbook/2/narrowing.html\#the-never-type](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#the-never-type)

### Exhaustiveness checking

[https://www.typescriptlang.org/docs/handbook/2/narrowing.html\#exhaustiveness-checking](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#exhaustiveness-checking) 

## Code Generation Is Independent of Types

Ref: Effective TS “Item 3: Understand That Code Generation Is Independent of Types”	

At a high level, tsc (the TypeScript compiler) does two things:

* It converts next-generation TypeScript/JavaScript to an older version of JavaScript that works in browsers (“transpiling”).   
* It checks your code for type errors.			

What’s surprising is that these two behaviors are entirely independent of one another. Put another way, the **types in your code cannot affect the JavaScript that TypeScript emits**. Since it’s this JavaScript that gets executed, this means that your types can’t affect the way your code runs.

This has some surprising implications and should inform your expectations about what TypeScript can and cannot do for you.

### JS Code Downleveling

[https://www.typescriptlang.org/docs/handbook/2/basic-types.html\#downleveling](https://www.typescriptlang.org/docs/handbook/2/basic-types.html#downleveling) 

Typescript Example:

```typescript
function greet(person: string, date: Date) {
  console.log(`Hello ${person}, today is ${date.toDateString()}!`);
}
 
greet("Maddison", Date());
```

Let’s take a look at what happens when we compile the above function greet with tsc to output JavaScript with different target:

* ES5

```typescript
function greet(person, date) {
    console.log("Hello ".concat(person, ", today is ").concat(date.toDateString(), "!"));
}
greet("Maddison", new Date());
```

* ES6

```typescript
function greet(person, date) {
    console.log(`Hello ${person}, today is ${date.toDateString()}!`);
}
greet("Maddison", new Date());
```

   
Our template string was rewritten from in the first case, because template string \`... \` are not available in ES5, they was introduced in ES6.

### Code with Type Errors Can Produce Output

* You can think of all TypeScript errors as being similar to warnings in those languages  
* as your TypeScript is valid JavaScript (and often even if it isn’t), the TypeScript compiler will produce output.  
* If you want to disable output on errors, you can use the noEmitOnError option in tsconfig.json

### You Cannot Check TypeScript Types at Runtime

…. Vedi Effective TS

### Type Operations Cannot Affect Runtime Values

Suppose you have a value that could be a string or a number and you’d like to normalize it so that it’s always a number. Here’s a misguided attempt that the type checker accepts:

```typescript
function asNumber(val: number | string): number { 
  return val as number;
}
```

Looking at the generated JavaScript makes it clear what this function really does:

```typescript
function asNumber(val) { 
  return val;
}
```

There is no conversion going on whatsoever. The as number is a type operation, so it cannot affect the runtime behavior of your code. To normalize the value you’ll need to check its runtime type and do the conversion using JavaScript constructs:

```typescript
function asNumber(val: number | string): number {
   return typeof(val) === 'string' ? Number(val) : val;
}
```

### 💥💥💥Runtime Types May Not Be the Same as Declared Types

Could this function ever hit the final console.log?

```typescript
function setLightSwitch(value: boolean) {
    switch (value) {
        case true: turnLightOn(); break;
        case false: turnLightOff(); break;
        default:
            console.log(`I'm afraid I can't do that.`);
    }
}
```

TypeScript usually flags dead code, but it does not complain about this, even with the strict option. How could you hit this branch?  
The key is to remember that boolean is the declared type. Because it is a TypeScript type, it goes away at runtime. In JavaScript code, a user might inadvertently call set LightSwitch with a value like "ON".

There are ways to trigger this code path in pure TypeScript, too. Perhaps the function is called with a value which comes from a network call:

```typescript
interface LightApiResponse {
    lightSwitchValue: boolean;
}
async function setLight() {
    const response = await fetch('/light');
    const result: LightApiResponse = await response.json();
    setLightSwitch(result.lightSwitchValue);
}
```

You’ve declared that the result of the /light request is LightApiResponse, but nothing enforces this. If you misunderstood the API and lightSwitchValue is really a string, then a string will be passed to setLightSwitch at runtime. Or perhaps the API changed after you deployed.

TODO: 🔥🔥TypeScript can get quite confusing when your runtime types don’t match the declared types, and this is a situation you should avoid whenever you can. 🔥🔥🔥 ⇒ HOW?\!?\!

But be aware that it’s possible for a value to have types other than the ones you’ve declared.

### You Cannot Overload a Function Based on TypeScript Types

Languages like C++ allow you to define multiple versions of a function that differ only in the types of their parameters. This is called “function overloading.”

Because he runtime behavior of your code is independent of its TypeScript types, this construct isn’t possible in TypeScript:

```typescript
function add(a: number, b: number) { return a + b; } // ~~~ Duplicate function implementation 
function add(a: string, b: string) { return a + b; } // ~~~ Duplicate function implementation
```

TypeScript does provide a facility for overloading functions, but it operates entirely at the type level. You can provide multiple declarations for a function, but only a single implementation:

```typescript
function add(a: number, b: number): number;
function add(a: string, b: string): string;

function add(a, b) { 
  return a + b;
}

const three = add(1, 2); // Type is number
const twelve = add('1', '2'); // Type is string
```

The first two declarations of add only provide type information. When TypeScript produces JavaScript output, they are removed, and only the implementation remains. (If you use this style of overloading, take a look at Item 50 first. There are some subtleties to be aware of.)

### TypeScript Types Have No Effect on Runtime Performance

Because types and type operations are erased when you generate JavaScript, they cannot have an effect on runtime performance. TypeScript’s static types are truly zero cost.

There are two caveats to this:

  * While there is no runtime overhead, the **TypeScript compiler will introduce build time overhead**. The TypeScript team takes compiler performance seriously and compilation is usually quite fast, especially for incremental builds. If the overhead becomes significant, your build tool may have a “transpile only” option to skip the type checking.  

  * The **code that TypeScript emits to support older runtimes may incur a performance overhead vs. native implementations**. For example, if you use generator functions and target ES5, which predates generators, then tsc will emit some helper code to make things work. This may have some overhead vs. a native implementation of generators. In any case, this has to do with the emit target and language levels and is still independent of the types.

## Type Manipulation

### Creating Types from Types

[https://www.typescriptlang.org/docs/handbook/2/types-from-types.html](https://www.typescriptlang.org/docs/handbook/2/types-from-types.html)   
TypeScript’s type system is very powerful because it allows expressing types in terms of other types.  
The simplest form of this idea is generics, we actually have a wide variety of type operators available to use. It’s also possible to express types in terms of values that we already have.  
By combining various type operators, we can express complex operations and values in a succinct, maintainable way. In this section we’ll cover ways to express a new type in terms of an existing type or value.

* [Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html) \- Types which take parameters  
* [Keyof Type Operator](https://www.typescriptlang.org/docs/handbook/2/keyof-types.html) \- Using the keyof operator to create new types  
* [Typeof Type Operator](https://www.typescriptlang.org/docs/handbook/2/typeof-types.html) \- Using the typeof operator to create new types  
* [Indexed Access Types](https://www.typescriptlang.org/docs/handbook/2/indexed-access-types.html) \- Using Type\['a'\] syntax to access a subset of a type  
* [Conditional Types](https://www.typescriptlang.org/docs/handbook/2/conditional-types.html) \- Types which act like if statements in the type system  
* [Mapped Types](https://www.typescriptlang.org/docs/handbook/2/mapped-types.html) \- Creating types by mapping each property in an existing type  
* [Template Literal Types](https://www.typescriptlang.org/docs/handbook/2/template-literal-types.html) \- Mapped types which change properties via template literal strings

### Generics

Refs: 

* [https://www.typescriptlang.org/docs/handbook/2/generics.html](https://www.typescriptlang.org/docs/handbook/2/generics.html)  
  * This section assumes too much knowledge, teaches things in the wrong order, and misses out key information. \-\> read the 3 link below  
* [https://www.digitalocean.com/community/tutorials/how-to-use-generics-in-typescript](https://www.digitalocean.com/community/tutorials/how-to-use-generics-in-typescript)   
* Matt Popock intro to generics [(29:00)](https://youtu.be/tDT214cE6Lo?list=PLj6YeMhvp2S40Q-TEPEKOeypLvTVd5uME&t=1748)   
* [Mental Model for TypeScript Generics | Matt Pocock](https://www.totaltypescript.com/mental-model-for-typescript-generics)  
* [Advanced TypeScript: Let’s Learn Generics\!](https://youtu.be/xk_PbxR7G8A?t=459)with Matt Pocock and Jason Lengstorf

In languages like C\# and Java, one of the main tools in the toolbox for creating reusable components is generics, that is, being able to create a component that can work over a variety of types rather than a single one.   
This allows users to consume these components and use their own types.

Generics are a fundamental feature of statically-typed languages, allowing developers to pass [types](https://www.digitalocean.com/community/tutorials/how-to-use-basic-types-in-typescript) as parameters to another type, [function](https://www.digitalocean.com/community/tutorials/how-to-use-functions-in-typescript), or other structure. When a developer makes their component a generic component, they give that component the ability to accept and enforce typing that is passed in when the component is used, which improves code flexibility, makes components reusable, and removes duplication.  
This short article is a good introduction to the mental model you need to grasp with Generics [Mental Model for TypeScript Generics | Matt Pocock](https://www.totaltypescript.com/mental-model-for-typescript-generics)

[TypeScript](https://www.typescriptlang.org/) fully supports generics as a way to introduce type-safety into components that accept arguments and return values whose type will be indeterminate until they are consumed later in your code. In this tutorial, you will try out real-world examples of TypeScript generics and explore how they are used in:

* Functions,  
* Types,  
* [Classes](https://www.digitalocean.com/community/tutorials/how-to-use-classes-in-typescript),  
* [interfaces](https://www.digitalocean.com/community/tutorials/how-to-use-interfaces-in-typescript). 

You will also use generics to create mapped types and conditional types, which will help you create TypeScript components that have the flexibility to apply to all necessary situations in your code.

#### **When do you really need advanced Typescript (generics, utility types, etc)?** 

Libraries authors use generics a lot, for example the XState lib makes a heavy use of generics. This is need ([cit Matt Popock](https://youtu.be/tDT214cE6Lo?list=PLj6YeMhvp2S40Q-TEPEKOeypLvTVd5uME&t=2159))If you want to be a library author you need to understand TS in depth.

[Advanced TypeScript: Let’s Learn Generics\!](https://youtu.be/xk_PbxR7G8A?t=459)with Matt Pocock and Jason Lengstorf

* TS is like an english teacher watching you  
* **When do you really need advanced Typescript (generics, utility types, etc)?**   
  I think if you're consuming stuff from \-- I think the point really \-- or the dividing line is, if you're writing an abstraction, and virtually any abstraction, then you're probably gonna need some kind of \-- even intermediate to advanced TypeScript to make that abstraction feel powerful. Because in JavaScript you can basically pull anything into a function, return anything out of a function, do crazy stuff like all through it. And if like you're not using TypeScript to its fullest extent, you probably end up with the user themselves having to annotate the code writing, this is this shape, this is this shape. Where if you can get it to a point that it's inferred throughout that, in any abstraction you write, then you're probably going to have a good time using advanced TypeScript.  
  If I can kind of walk this back a little bit: Is that where these generics and other advanced TypeScript concepts really start to shine is when you are building code for writing code.  
    
  Like so if you're building an application and you're gonna ship that and that's what runs in the browser, you probably can figure out enough about how your code works to not need any of these really advanced things. And personally, I'm a big fan of like if you can refactor something to be just a standard type, you probably should, right? Like don't get clever if you don't need to get clever. 

  But as you start writing code that's a layer of abstraction to empower other Devs to build more things. You've found a common pattern and people are gonna wrap all their code with this thing that adds something. Then suddenly you have this deeper need to accommodate people who are gonna do arbitrary stuff. And you want to support that without making them do a bunch of extra lifting.  
* Generics allow you to avoid the use of  any when you don’t know in advance what type you are going to use, for example if you are a lib author you can create a structure but let the lib user finalize types using generics.

#### Generic \- Syntax

Generics appear in TypeScript code inside angle brackets, in the format \<T\>, where **T represents a passed-in type**. 

\<T\> can be read as a generic of type T. In this case, T will operate in the same way that parameters work in functions, as placeholders for a type that will be declared when an instance of the structure is created. The generic types specified inside angle brackets are therefore also known as generic type parameters or just type parameters. 

Multiple generic types can also appear in a single definition, like \<T, K, A\>.

Generics can appear in functions, types, classes, and interfaces.

| 📔 Note \<T\> Convention: By convention, programmers usually use a single letter to name a generic type. This is not a syntax rule, and you can name generics like any other type in TypeScript, but this convention helps to immediately convey to those reading your code that a generic type does not require a specific type. |
| :---- |

#### Hello World of Generics

To start off, let’s do the “hello world” of generics: the identity function. The identity function is a function that will return back whatever is passed in. You can think of this in a similar way to the echo command.  
Without generics, we would either have to give the identity function a specific type ([Try](https://www.typescriptlang.org/play/#code/GYVwdgxgLglg9mABDAJgUzLKBPAFAQwCcBzALkTBAFsAjNQgSnMtvsQG8AoRRQtKEISRFiAbk4BfIA)):

```typescript
function identity(arg: number): number {
 return arg;
}
```

Or, we could describe the identity function using the any type ([Try](https://www.typescriptlang.org/play/#code/GYVwdgxgLglg9mABDAJgUzLKBPAFAQwCcBzALkXzGwEpzLtEBvAKEUULShEKSOIG5mAXyA)):

```typescript
function identity(arg: any): any {
 return arg;
}
```

* While using any is certainly generic in that it will cause the function to accept any and all types for the type of arg,  
* we actually are losing the information about what that type was when the function returns. If we passed in a number, the only information we have is that any type could be returned.

Instead, we need a way of capturing the type of the argument in such a way that we can also use it to denote what is being returned. Here, we will use a type variable, a special kind of variable that works on types rather than values ([Try](https://www.typescriptlang.org/play/#code/GYVwdgxgLglg9mABDAJgUzLKBPAPAFWwAc0A+ACgEMAnAcwC5FCSBKR5tRAbwChFFqaKCGpIatANw8AvkA)).

```typescript
function identity<Type>(arg: Type): Type {
 return arg;
}
```

We’ve now added a type variable Type to the identity function. This Type allows us to capture the type the user provides (e.g. number), so that we can use that information later. Here, we use Type again as the return type. On inspection, we can now see the same type is used for the argument and the return type. This allows us to traffic that type information in one side of the function and out the other.

We say that this version of the identity function is **generic**, as it works over a range of types. Unlike using any, it’s also just as precise (i.e., it doesn’t lose any information) as the first identity function that used numbers for the argument and return type.

Once we’ve written the generic identity function, we can call it in one of two ways. The first way is to pass all of the arguments, including the type argument, to the function [Try](https://www.typescriptlang.org/play/#code/GYVwdgxgLglg9mABDAJgUzLKBPAPAFWwAc0A+ACgEMAnAcwC5FCSBKR5tRAbwChFFqaKCGpIatANw8AvjwD0cxAFoVEEFBVKeAGyGI46ousQBeZOkwwcuAM5RqMMLQoAiALbYAyvce0XLKQV+YP4APQB+IA):

```typescript
let output = identity<string>("myString");
```

1. Here we explicitly set Type to be string as one of the arguments to the function call, denoted using the **\<\>** around the arguments rather than ().

2. The second way is also perhaps the most common. Here we use type argument inference — that is, we want the compiler to set the value of Type for us automatically based on the type of the argument we pass in: ([Try](https://www.typescriptlang.org/play/#code/GYVwdgxgLglg9mABDAJgUzLKBPAPAFWwAc0A+ACgEMAnAcwC5FCSBKR5tRAbwChFFqaKCGpIatANw8AvjwD0cxAFoVEEFBVKeAGyGI46ousQBeZOkwwc5AEQBbbAGUo1GGFo2WUhf1-8AegD8QA))

```typescript
let output = identity("myString");
```

    

Notice that we didn’t have to explicitly pass the type in the angle brackets (\<\>); the compiler just looked at the value "myString", and set Type to its type. While type argument inference can be a helpful tool to keep code shorter and more readable, you may need to explicitly pass in the type arguments as we did in the previous example when the compiler fails to infer the type, as may happen in more complex examples.

#### Working with Generic Type Variables

When you begin to use generics, you’ll notice that when you create generic functions like identity, the compiler will enforce that you use any generically typed parameters in the body of the function correctly. That is, that you actually treat these parameters as if they could be any and all types.

Let’s take our identity function from earlier:

```typescript
function identity<Type>(arg: Type): Type {
 return arg;
}
```

What if we want to also log the length of the argument arg to the console with each call? We might be tempted to write this ([Try](https://www.typescriptlang.org/play/#code/PTAEAEFMCdoe2gZwFygEwGYME4BQAzAVwDsBjAFwEs5jQAbOAc0cuMYEkATSYq8gTwA8AFX4AHSAD4AFAENojVKIkBKJeMigA3rlChSNRHDqQAdA0ZyF5no3IALFQG5doaJHKFoteYxcBfIA)):

```typescript
function loggingIdentity<Type>(arg: Type): Type {
 console.log(arg.length); //COMPILER ERROR Property 'length' does not exist on type 'Type'.
 return arg;
}
```

When we do, the compiler will give us an error that we’re using the arg.length member, but nowhere have we said that arg has this member. Remember, we said earlier that these type variables stand in for any and all types, so someone using this function could have passed in a number instead, which does not have a .length member.

Let’s say that we’ve actually intended this function to work on arrays of Type rather than Type directly. Since we’re working with arrays, the .length member should be available. We can describe this just like we would create arrays of other types ([Try](https://www.typescriptlang.org/play/#code/GYVwdgxgLglg9mABAGzgczTMaCSATAUzFigE8AeAFVIAcCA+ACgEMAnNALkWroG0BdAJRceBAYgDeAKESIICAM5xkBAHSo0LduqJooAC0EBuGYlYEoIVkjZoTAXyA)):

```typescript
function loggingIdentity<Type>(arg: Type[]): Type[] {
 console.log(arg.length);
 return arg;
}
```

You can read the type of loggingIdentity as “the generic function loggingIdentity takes a type parameter Type, and an argument arg which is an array of Types, and returns an array of Types.” If we passed in an array of numbers, we’d get an array of numbers back out, as Type would bind to number. This allows us to use our generic type variable Type as part of the types we’re working with, rather than the whole type, giving us greater flexibility.

We can alternatively write the sample example this way ([Try](https://www.typescriptlang.org/play/#code/GYVwdgxgLglg9mABAGzgczTMaCSATAUzFigE8AeAFVIAcCA+ACgEMAnNALkQEFXXmK1OvQCUXXv0G0GiAN4AoRIggIAznGQEAdKjQt2OomigALEQG5EAeis8+AxCearEzRIeymANInWIwcIgAtnCsBIgEfKGKiGFQIKxIbGjm8gC+QA)):

```typescript
function loggingIdentity<Type>(arg: Array<Type>): Array<Type> {
 console.log(arg.length); // Array has a .length, so no more error
 return arg;
}
```

You may already be familiar with this style of type from other languages. In the next section, we’ll cover how you can create your own generic types like **Array\<Type\>**.

#### Generic Types

In previous sections, we created generic identity functions that worked over a range of types. In this section, we’ll explore the type of the functions themselves and how to create **generic interfaces**.

The type of generic functions is just like those of non-generic functions, with the type parameters listed first, similarly to function declarations ([Try](https://www.typescriptlang.org/play/#code/GYVwdgxgLglg9mABDAJgUzLKBPAPAFWwAc0A+ACgEMAnAcwC5FCSBKR5tRAbwChFFqaKCGpIatANw8Avjx4AbIYgC22AJLpMMHIwLEyVOu30tEAXlJN955JqzYJQA)):

```typescript
function identity<Type>(arg: Type): Type {
 return arg;
}
let myIdentity: <Type>(arg: Type) => Type = identity;
```

We could also have used a different name for the generic type parameter in the type, so long as the number of type variables and how the type variables are used line up ([Try](https://www.typescriptlang.org/play/#code/GYVwdgxgLglg9mABDAJgUzLKBPAPAFWwAc0A+ACgEMAnAcwC5FCSBKR5tRAbwChFFqaKCGpIatANw8Avjx4AbIYgC22AJLpMMHI1xqwREFArjG+w1BaIAvKUTmjN5JqzYJQA)).

```typescript
function identity<Type>(arg: Type): Type {
 return arg;
}
let myIdentity: <Input>(arg: Input) => Input = identity;
```

We can also write the generic type as a call signature of an object literal type ([Try](https://www.typescriptlang.org/play/#code/GYVwdgxgLglg9mABDAJgUzLKBPAPAFWwAc0A+ACgEMAnAcwC5FCSBKR5tRAbwChFFqaKCGpIatANw8Avjx4AbIYgC22AJLpMMHIy6ICxMlTrtDbJocTTEAXmSas2CUA)):

```typescript
function identity<Type>(arg: Type): Type {
 return arg;
}
let myIdentity: { <Type>(arg: Type): Type } = identity;
```

Which leads us to writing our first generic interface. Let’s take the object literal from the previous example and move it to an interface ([Try](https://www.typescriptlang.org/play/#code/JYOwLgpgTgZghgYwgAgOIRNYCCSATDMYMATwDERkBvAKGWQB4AVEgBwgD4AKOKAcwBcyFuwCUQkRADcNAL40aMAK4gERAPaVgBcMRLM2nHvwmHxww9TrIoEMEqiVefGfJoAbO8gC2JfIT0hdEwobH9dUgpkAF5kbQDSKSA)):

```typescript
interface GenericIdentityFn {
 <Type>(arg: Type): Type;
}
function identity<Type>(arg: Type): Type {
 return arg;
}
let myIdentity: GenericIdentityFn = identity;
```

In a similar example, we may want to move the generic parameter to be a parameter of the whole interface. This lets us see what type(s) we’re generic over (e.g. Dictionary\<string\> rather than just Dictionary). This makes the type parameter visible to all the other members of the interface ([Try](https://www.typescriptlang.org/play/#code/JYOwLgpgTgZghgYwgAgOIRNYCCSATDMYMATwDEQAeAFRIAcIA+ZAbwChlkAKOKAcwBcyWgwCUQkRADcbAL5s2MAK4gERAPYhkwAuGIka9Jj34Sj44UdYdkUCGCVQtvPjPlsANveQBbEvkJ9IXRMKGwAvVIKShAlHwAjaGYAXm1dIlIpIA)).

```typescript
interface GenericIdentityFn<Type> {
 (arg: Type): Type;
}
function identity<Type>(arg: Type): Type {
 return arg;
}
let myIdentity: GenericIdentityFn<number> = identity;
```

Notice that our example has changed to be something slightly different. Instead of describing a generic function, we now have a non-generic function signature that is a part of a generic type.  
When we use GenericIdentityFn, we now will also need to specify the corresponding type argument (here: number), effectively locking in what the underlying call signature will use. Understanding when to put the type parameter directly on the call signature and when to put it on the interface itself will be helpful in describing what aspects of a type are generic.

In addition to generic interfaces, we can also create generic classes. Note that it is not possible to create generic enums and namespaces.

#### Generic Classes

A generic class has a similar shape to a generic interface. Generic classes have a generic type parameter list in angle brackets (**\<\>**) following the name of the class ([Try](https://www.typescriptlang.org/play/#code/PTAEAEGcBcCcEsDG0BcoBmBDANpApgFCLaaSSgDieAdngogHICuAtgEZ0A8zLAKgJ4AHPAD5QAbwKhQALzoB7AGo4meNDwHCA3FNCYAJvrQAKAB7rWmvABpQ-C3yF4AlKAC8YjU50BfAgWw8aFAWfipaeh4OWHdQWgB3Sho6JCiualZokWNnHVDwlMZMugA6OVglFTxYgAY8sOTI4tgSg31Y9CZqZHh5alAzW35XSWlYIKZYftNQAGo7Xy0gA)).

```typescript
class GenericNumber<NumType> {
 zeroValue: NumType;
 add: (x: NumType, y: NumType) => NumType;
}
let myGenericNumber = new GenericNumber<number>();
myGenericNumber.zeroValue = 0;
myGenericNumber.add = function (x, y) {
 return x + y;
};
```

> [!TODO] problem with the code above
> 🪲PROBLEMA 🪲 Il ([codice qua sopra](https://www.typescriptlang.org/play/#code/PTAEAEGcBcCcEsDG0BcoBmBDANpApgFCLaaSSgDieAdngogHICuAtgEZ0A8zLAKgJ4AHPAD5QAbwKhQALzoB7AGo4meNDwHCA3FNCYAJvrQAKAB7rWmvABpQ-C3yF4AlKAC8YjU50BfAgWw8aFAWfipaeh4OWHdQWgB3Sho6JCiualZokWNnHVDwlMZMugA6OVglFTxYgAY8sOTI4tgSg31Y9CZqZHh5alAzW35XSWlYIKZYftNQAGo7Xy0gA)) da questi errori:
> - Property 'zeroValue' has no initializer and is not definitely assigned in the constructor. 
> - Property 'add' has no initializer and is not definitely assigned in the constructor. 
> Leggendo [qua](https://www.angularjswiki.com/angular/property-has-no-initializer-and-is-not-definitely-assigned-in-the-constructor/) ci sono varie soluzioni, per esempio questa sembra funzionare: 
> ```typescript
> class GenericNumber<NumType> {  zeroValue: undefined | NumType ;  add: undefined | ((x: NumType, y: NumType) => NumType) ; }
> ```  

This is a pretty literal use of the GenericNumber class, but you may have noticed that nothing is restricting it to only use the number type. We could have instead used string or even more complex objects ([Try](https://www.typescriptlang.org/play/#code/PTAEAEGcBcCcEsDG0BcoBmBDANpApgFCLaaSSgDieAdngogHICuAtgEZ0A8zLAKgJ4AHPAD5QAbwKhQALzoB7AGo4meNDwHCA3FNCYAJvrQAKAB7rWmvABpQ-C3yF4AlKAC8YjU50BfAiFAAWmDEJmhgwIJsPGhQGARqAHMeOiR3UFoAd0oaVMZWDlhOePgkkWNnHRKklPoAOjlYJRU8dIAiNqq4UuTWPLqDfXT0JmpkeHlqUDNbfldJaVgYplgp01AAajtfHSJJyHlouux5RONq3pZ+wfPumr76xubsVVs26DwYNudKoA)).

```typescript
let stringNumeric = new GenericNumber<string>();
stringNumeric.zeroValue = "";
stringNumeric.add = function (x, y) {
 return x + y;
};
console.log(stringNumeric.add(stringNumeric.zeroValue, "test"));
```

Just as with interface, putting the type parameter on the class itself lets us make sure all of the properties of the class are working with the same type.

As we cover in [our section on classes](https://www.typescriptlang.org/docs/handbook/2/classes.html), a class has two sides to its type: the static side and the instance side. Generic classes are only generic over their instance side rather than their static side, so when working with classes, static members can not use the class’s type parameter.

# [Getting started] Add TypeScript to an npm project

like so:  

```bash
    mkdir test-app
    cd test-app
    npm init -y
    npm install --save-dev typescript
    npx tsc --init
```


A file called `tsconfig.json` will be generated after running `tsc --init` and placed in the root directory of the project. This file contains settings and options for the TypeScript compiler (`tsc`).

Ideally, we will keep our TypeScript files in one directory, and all our generated JavaScript files will go into their own directory. Let’s create a src directory for TS files and a dist directory for JS files: `mkdir src dist`. We can tell tsc where to find our TS files and where to place our JS files by editing two fields in the tsconfig.json file:

Open the project in a code editor and make the above changes. Finally, we can add a `build:dev` script to our `package.json` file:

```json
{
  "name": "from-js-to-ts",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build:dev": "tsc --watch --preserveWatchOutput",
    "start": "node dist/index.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "typescript": "^3.7.3"
  }
}
```


The compiler is set to run in watch mode to recompile our code as we save changes. I have also set it to preserve the console output, which is a personal preference that you can remove. A start script was also added so we can run a quick test.  
Create a file called index.ts inside of the src directory:  
touch src/index.ts  
echo "console.log('hello');" \> src/index.ts  
Then compile the code and run it:  
npm run build:dev  
(In a separate terminal window or tab)  
npm start

We are going to return to this test-app later. For now, kill the server by pressing Ctrl C in the terminal.

# Modules

Modules https://basarat.gitbook.io/typescript/project/modules  
apparentemente si applicano le stesse regole di JS

\[Official Doc\](https://www.typescriptlang.org/docs/handbook/modules.html)

🔥🔥🔥 non mi sembra il massimo che si possa definire una variablie

 	

# Compiler Flag considerations

## \[Best Practive\] strict: true

📔 NextJS enable it by default  
See effective TS pag 7

Enables a set of stricter checks and settings that help to catch common errors and improve the overall type safety of your code.

will enable the following strict checks and settings:

* "**noImplicitAny**": This option disallows implicit any types, and will raise an error if a variable is used without an explicit type annotation.  
* "**strictNullChecks**": This option enforces stricter null and undefined checks, and will raise an error if a variable is used without first checking if it is null or undefined.  
* "**strictFunctionTypes**": This option enforces stricter function type checking, and will raise an error if function arguments or return types do not match the expected types.  
* "**strictBindCallApply**": This option disallows non-standard calling and binding of functions, and will raise an error if a function is called with a non-standard call or apply method.  
* "**strictPropertyInitialization**": This option enforces stricter property initialization checks, and will raise an error if a class property is used without first being initialized.

These strict checks and settings can help to **catch common errors**, such as using variables without first checking if they are null or undefined, or using variables without an explicit type annotation. They also help to improve the overall type safety of your code, by ensuring that variables and functions are used with the correct types.

It's important to note that enabling "strict: true" may require you to make changes to your existing code in order to pass the stricter type checks and settings. But, it will also help you to write more robust and safer code in the long run.

# \[JOB\] Strategies for Moving existing code bases from JS to TS
