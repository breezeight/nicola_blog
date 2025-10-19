---
title: Understanding TypeScript Compilation
abstract: >
  Hands-on tutorial exploring how TypeScript compiles to JavaScript, 
  covering compiler configuration, target settings, and practical compilation examples.
type: tutorial
---

# Understanding TypeScript Compilation

## 📘 Purpose & Scope

This tutorial guides you through understanding how TypeScript compilation works by creating a simple project and manually compiling TypeScript code into JavaScript. You'll learn how the TypeScript Compiler (tsc) transforms your code and how different target settings affect the output.

## What We'll Build

We'll create a simple TypeScript project, write some TypeScript code, and compile it using the TypeScript compiler to see how different configurations affect the generated JavaScript.

## Step 1: Initialize the Project

Let's start by creating a new project directory and initializing it:

```bash
mkdir typescript-compilation-tutorial
cd typescript-compilation-tutorial
```

Create a `package.json` file:

```bash
npm init -y
```

> **💡 Explanation Box**: The `-y` option automatically answers "yes" to all npm init questions, creating a package.json with default values.

## Step 2: Install TypeScript

Install TypeScript as a development dependency:

```bash
npm i typescript -D
```

> **💡 Explanation Box**: The `-D` (or `--save-dev`) flag adds TypeScript to `devDependencies`, meaning it's only needed during development, not in production.

## Step 3: Initialize TypeScript Configuration

Create a `tsconfig.json` file with default settings:

```bash
npx tsc --init
```

This generates a `tsconfig.json` file with comprehensive default settings. For our tutorial, we'll use these defaults initially.

## Step 4: Write TypeScript Code

Create a source directory and add our first TypeScript file:

```bash
mkdir src
touch src/index.ts
```

Open `src/index.ts` and add some TypeScript code:

```typescript
const a: number = 1;
console.log(a);

class Foo {
  constructor(public name: string) {}
  
  greet(): string {
    return `Hello, ${this.name}!`;
  }
}

const instance = new Foo("World");
console.log(instance.greet());
```

## Step 5: Compile TypeScript to JavaScript

Now let's compile our TypeScript code:

```bash
npx tsc
```

You should see a new `index.js` file generated in the `src` directory. Let's examine what was created:

```javascript
"use strict";
const a = 1;
console.log(a);
class Foo {
    constructor(name) {
        this.name = name;
    }
    greet() {
        return `Hello, ${this.name}!`;
    }
}
const instance = new Foo("World");
console.log(instance.greet());
```

Notice how TypeScript removed the type annotations (`: number`, `: string`) and kept the modern JavaScript syntax like `const`, `let`, and `class`.

## Step 6: Understanding Target Settings

The output looks similar to our input because our `tsconfig.json` targets ES2016 by default, which supports modern JavaScript features.

Let's see what happens when we target older browsers. Update your `tsconfig.json`:

```json
{
  "compilerOptions": {
    "target": "ES5",
    "module": "commonjs",
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "strict": true,
    "skipLibCheck": true
  }
}
```

Now compile again:

```bash
npx tsc
```

The output is dramatically different:

```javascript
"use strict";
var a = 1;
console.log(a);
var Foo = /** @class */ (function () {
    function Foo(name) {
        this.name = name;
    }
    Foo.prototype.greet = function () {
        return "Hello, " + this.name + "!";
    };
    return Foo;
}());
var instance = new Foo("World");
console.log(instance.greet());
```

Notice the changes:
- `const` became `var`
- `class` became a function constructor
- Template literals became string concatenation
- Methods are attached to the prototype

## Step 7: Run the Compiled Code

Let's run our compiled JavaScript:

```bash
node src/index.js
```

You should see:
```
1
Hello, World!
```

## Step 8: Exploring Different Targets

Let's try targeting ES2020 to see modern output:

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "strict": true,
    "skipLibCheck": true
  }
}
```

Compile and check the output:

```bash
npx tsc
cat src/index.js
```

The output should be very close to our original TypeScript code, with only type annotations removed.

## What We Learned

Through this tutorial, we discovered:

1. **TypeScript removes type annotations** during compilation
2. **Target settings determine JavaScript output** - ES5 produces verbose, compatible code while ES2020 keeps modern syntax
3. **The compiler handles syntax transformation** - classes become functions, template literals become concatenation
4. **TypeScript preserves runtime behavior** while adding compile-time safety

## Real-World Applications

In real projects, you rarely compile manually like this. Instead, you use build tools like:
- **Vite** for fast development and modern bundling
- **Webpack** for complex applications with many dependencies  
- **Rollup** for libraries and optimized bundles

These tools handle TypeScript compilation automatically while providing additional features like hot reloading, bundling, and optimization.

## References

- [TypeScript Compiler Options](https://www.typescriptlang.org/docs/handbook/compiler-options.html)
- [TypeScript Target Settings](https://www.typescriptlang.org/tsconfig#target)
- [Understanding TypeScript Compilation](https://www.typescriptlang.org/docs/handbook/compiler-options.html#compiler-options)
