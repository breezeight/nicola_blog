---
title: JavaScript and TypeScript Index
abstract: >
  Comprehensive learning paths for JavaScript and TypeScript, covering beginner to advanced topics and practical implementation guides.
---

* Matt Popock  
  [Total TypeScript](https://www.totaltypescript.com/)   
  [Matt Pocock (@mattpocockuk) / Twitter](https://twitter.com/mattpocockuk)  
  [Advanced TypeScript \- YouTube](https://www.youtube.com/playlist?list=PLIvujZeVDLMx040-j1W4WFs1BxuTGdI_b)   
  **“Matt’s TS Wizards” Discord- \> a lot of people learning TS**

[Official TypeScript Website](https://www.typescriptlang.org/docs/), the most useful are:

1. [The TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html):  
    - is intended to be a comprehensive document that explains TypeScript to everyday programmers.   
    - is not a complete language specification, but it is intended to be a comprehensive guide to all of the language’s features and behaviors.

2. Reference Files  
    - The reference section below the handbook in the navigation is built to provide a richer understanding of how a particular part of TypeScript works. You can read it top-to-bottom, but each section aims to provide a deeper explanation of a single concept \- meaning there is no aim for continuity.

Free and open-source books:

- [Learn by doing by Fabio Biondi: TypeScript for Frontend Developers](https://www.learnbydo.ing/courses/typescript/typescript-for-frontend-developers)

- **TypeScript Deep Dive Book** ([read online](https://basarat.gitbook.io/typescript/getting-started))  
    * ⭐18K on github  
    * ⏱️?  
    * 🇮🇹🇬🇧🇫🇷🇪🇸🇷🇺  
    * Source code [GitHub \- basarat/typescript-book: The definitive guide to TypeScript and possibly the best TypeScript book . Free and Open Source 🌹](https://github.com/basarat/typescript-book)   
    * [youtube](https://www.youtube.com/playlist?list=PLYvdvJlnTOjF6aJsWWAt7kZRJvzw-en8B) [Twitter](https://twitter.com/basarat)  
    * : riprende molto JS e   
    * Per chi è il libro \- Summary:  
        * Nei capitoli [JavaScript](https://basarat.gitbook.io/typescript/recap) e [Future JavaScript Now](https://basarat.gitbook.io/typescript/future-javascript) fa una carrellatta sulla sintassi base, ⚠️Forse è un po’ vecchiotto come libro? Tante delle funzionalità che cita con future sono già incorporate in JS nel 2023  


BLOG By the Effective Typescript Book author: [https://effectivetypescript.com/](https://effectivetypescript.com/)	

- Free download [https://books-library.net/files/books-library.net-10121732Pl7G6.pdf](https://books-library.net/files/books-library.net-10121732Pl7G6.pdf) 

# Learning Paths

**Q: How much of TS handbook content is applicable to React? As in if I'm only using React, is there a good portion of content I shouldn't bother with?**

* Doesn't matter what framework you're using, I'd say pretty much all the things you learn are applicable to any sufficiently complex typescript app. What you end up using probably depends much more on the needs of the app than what framework you use.  
* Once you master TS, it won't matter which underline framework you are using to apply your knowledge. If you push your goal towards learn  "TS for React" you will be learning recipes, not TS, and you will end up with a feeling of not knowing what you are doing.  
* In different words, **there are 2 types of TS devs: authors and users**.   
  * Type authors are the ones that build the types you are supposed to be using. In the React world that title will be better applied to the team behind React.   
  * As a TS user you are not supposed to expand much in those types but know how to use them, in which case, if you have authored skills you will know that more easy than a user because you won't be following a recipe of how to type a useReducer, you will be able to read the type definition and understand what you need. You should go for Matt course to later understand why you don't need a TS React course.

## Basics 

[The TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html):

* is intended to be a comprehensive document that explains TypeScript to everyday programmers.   
* is not a complete language specification, but it is intended to be a comprehensive guide to all of the language’s features and behaviors.  
* A reader who completes the walkthrough should be able to:  
  * Read and understand commonly-used TypeScript syntax and patterns  
  * Explain the effects of important compiler options  
  * Correctly predict type system behavior in most cases  
  * In the interests of clarity and brevity, the main content of the Handbook will not explore every edge case or minutiae of the features being covered. You can find more details on particular concepts in the reference articles.  
* 1\. “The Basics”  
  * Intro to type checking, compiler, code editor  
  * Emit code  
  * Explicit Types  
  * Erased Types and Downleveling on code emit  
  * Strictness of the compiler  
* 2\. “Everyday Types”  
  * cover some of the most common types of values you’ll find in JavaScript code  
  * [Main primitives](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#the-primitives-string-number-and-boolean): string, number, boolean

Very basic Typescript exercises : [Exercise v3.0](https://www.w3schools.com/typescript/exercise.php?filename=exercise_enums2) 

[🔴 TypeScript Crash Course with Matt Pocock](https://www.youtube.com/watch?v=p6dO9u0M7MQ)

* Molto Hands-on. Nella descrizione del video YT c’è un link al TypeScript Repo [https://aka.ms/TypeScriptRepo](https://aka.ms/TypeScriptRepo) che funziona con   
* ⏱️ **1 H**

[🔴 Can VS Code teach you TypeScript?](https://youtu.be/tDT214cE6Lo?list=PLj6YeMhvp2S40Q-TEPEKOeypLvTVd5uME&t=158) with Matt Popock

* VScode has many feature that can help you to understand how the TSC compiler works  
* [06:04](https://www.youtube.com/watch?v=tDT214cE6Lo&list=PLj6YeMhvp2S40Q-TEPEKOeypLvTVd5uME&index=4&t=364s) Total TypeScript VS Code extension  
  [Total TypeScript Extension](https://marketplace.visualstudio.com/items?itemName=mattpocock.ts-error-translator): translates TS errors in human readable format, provide hints to the documentation, highlighted in blue (you can mark them are learned). The extensions uses the TS abstract syntax tree  
* [(16:08)](https://youtu.be/tDT214cE6Lo?list=PLj6YeMhvp2S40Q-TEPEKOeypLvTVd5uME&t=968) Learn the DOM API and NODE API using TS hint: types for these apis are provided by default. To learn you can: hover to some function and read the documentation or  click “go to definition” if you want to see where they are defined.  
* [Renaming across modules](https://youtu.be/tDT214cE6Lo?list=PLj6YeMhvp2S40Q-TEPEKOeypLvTVd5uME&t=1319)  
* Part of the tutorial in Matt website are free  
* [(29:00)](https://youtu.be/tDT214cE6Lo?list=PLj6YeMhvp2S40Q-TEPEKOeypLvTVd5uME&t=1748) Generics  
* [(38:20 \- 44:22)](https://youtu.be/tDT214cE6Lo?list=PLj6YeMhvp2S40Q-TEPEKOeypLvTVd5uME&t=2301) satisfies operator  
* [(44:02)](https://youtu.be/tDT214cE6Lo?list=PLj6YeMhvp2S40Q-TEPEKOeypLvTVd5uME&t=2638) Conditional params that are dependent on the value of another param, for example: myObj.prop2 is required only if myObj.prop1 is true. \-\> Use discriminated Union

   
[Advanced TypeScript: Let’s Learn Generics\!](https://youtu.be/xk_PbxR7G8A?t=459)with Matt Pocock and Jason Lengstorf

* TS is like an english teacher watching you  
* Tutorial Repo: [GitHub \- total-typescript/typescript-generics-workshop: Interactive tutorial on using generics in TypeScript](https://github.com/total-typescript/typescript-generics-workshop)   
* **When do you really need advanced Typescript (generics, utility types, etc)?**   
  I think if you're consuming stuff from \-- I think the point really \-- or the dividing line is, if you're writing an abstraction, and virtually any abstraction, then you're probably gonna need some kind of \-- even intermediate to advanced TypeScript to make that abstraction feel powerful. Because in JavaScript you can basically pull anything into a function, return anything out of a function, do crazy stuff like all through it. And if like you're not using TypeScript to its fullest extent, you probably end up with the user themselves having to annotate the code writing, this is this shape, this is this shape. Where if you can get it to a point that it's inferred throughout that, in any abstraction you write, then you're probably going to have a good time using advanced TypeScript.  
  If I can kind of walk this back a little bit: Is that where these generics and other advanced TypeScript concepts really start to shine is when you are building code for writing code.  
    
  Like so if you're building an application and you're gonna ship that and that's what runs in the browser, you probably can figure out enough about how your code works to not need any of these really advanced things. And personally, I'm a big fan of like if you can refactor something to be just a standard type, you probably should, right? Like don't get clever if you don't need to get clever. 

  But as you start writing code that's a layer of abstraction to empower other Devs to build more things. You've found a common pattern and people are gonna wrap all their code with this thing that adds something. Then suddenly you have this deeper need to accommodate people who are gonna do arbitrary stuff. And you want to support that without making them do a bunch of extra lifting.  
* Generics allow you to avoid the use of  any when you don’t know in advance what type you are going to use, for example if you are a lib author you can create a structure but let the lib user finalize types using generics.

[🔴 TypeScript tips and Tricks with Matt](https://youtu.be/hBk4nV7q6-w?list=PLj6YeMhvp2S40Q-TEPEKOeypLvTVd5uME&t=218)

* ⏱️ **1 H**  
* Advanced 10 TS code challenges

[TypeScript Tutorial for Beginners](https://www.youtube.com/watch?v=d56mG7DezGs)  by Mosh

* ⭐ Quick and effective, the best for experienced developer, cover the same subjects of the “Everyday Types” portion of the Handbook  
* ⏱️ **1 H**  
  * [0:00:00](https://www.youtube.com/watch?v=d56mG7DezGs&t=0s) Introduction  
  * [0:00:52](https://www.youtube.com/watch?v=d56mG7DezGs&t=52s) Prerequisites  
  * [0:01:28](https://www.youtube.com/watch?v=d56mG7DezGs&t=88s) How to Take This Course  
  * [0:02:57](https://www.youtube.com/watch?v=d56mG7DezGs&t=177s) What is TypeScript?  
  * [0:07:38](https://www.youtube.com/watch?v=d56mG7DezGs&t=458s) Setting Up the Development Environment   
  * [0:09:30](https://www.youtube.com/watch?v=d56mG7DezGs&t=570s) Your First TypeScript Program  
  * [0:13:20](https://www.youtube.com/watch?v=d56mG7DezGs&t=800s) Configuring the TypeScript Compiler   
  * [0:17:24](https://www.youtube.com/watch?v=d56mG7DezGs&t=1044s) Debugging TypeScript Applications   
  * [0:22:55](https://www.youtube.com/watch?v=d56mG7DezGs&t=1375s) Fundamentals  
  * [0:23:23](https://www.youtube.com/watch?v=d56mG7DezGs&t=1403s) Built-In Types  
  * [0:25:21](https://www.youtube.com/watch?v=d56mG7DezGs&t=1521s) The any Type  
  * [0:28:06](https://www.youtube.com/watch?v=d56mG7DezGs&t=1686s) Arrays  
  * [0:30:24](https://www.youtube.com/watch?v=d56mG7DezGs&t=1824s) Tuples  
  * [0:33:08](https://www.youtube.com/watch?v=d56mG7DezGs&t=1988s) Enums  
  * [0:36:31](https://www.youtube.com/watch?v=d56mG7DezGs&t=2191s) Functions  
  * [0:43:22](https://www.youtube.com/watch?v=d56mG7DezGs&t=2602s) Objects  
  * [0:47:57](https://www.youtube.com/watch?v=d56mG7DezGs&t=2877s) Advanced Types  
  * [0:48:26](https://www.youtube.com/watch?v=d56mG7DezGs&t=2906s) Type Aliases  
  * [0:50:04](https://www.youtube.com/watch?v=d56mG7DezGs&t=3004s) Union Types   
  * [0:52:40](https://www.youtube.com/watch?v=d56mG7DezGs&t=3160s) Intersection Types   
  * [0:54:44](https://www.youtube.com/watch?v=d56mG7DezGs&t=3284s) Literal Types   
  * [0:56:30](https://www.youtube.com/watch?v=d56mG7DezGs&t=3390s) Nullable Types   
  * [0:59:06](https://www.youtube.com/watch?v=d56mG7DezGs&t=3546s) Optional Chaining
