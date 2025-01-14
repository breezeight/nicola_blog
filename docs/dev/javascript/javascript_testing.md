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