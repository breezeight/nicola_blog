---
layout: post
title: "Bower"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["javascript", "css"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# Intro

http://bower.io/

Bower is a package manager for the web. It offers a generic, unopinionated solution to the problem of front-end package management, while exposing the package dependency model via an API that can be consumed by a more opinionated build stack. 

Is a content-agnostic transport tool that only dumps all your dependencies (and their dependencies, recursively) into the file system. it’s up to you what to do with them. 
Tools like Broccoli sit on top of Bower.

 ??????????   main string or array: The primary acting files necessary to use your package.


Bower configuration files:

* `bower.json` : [documentation](http://bower.io/docs/creating-packages/#bowerjson)
* `.bowerrc` : [documentation](http://bower.io/docs/config/)

Bower command line documentation:  http://bower.io/docs/api/

# Install packages

TODO: 

* how to persist with --save
* how to add development dependencies

## From the registry

TODO

## Install a package for a local or remote git

In your main project edit bower.json file to add (or expand):

~~~
  "dependencies": {
    …
    "you-need-me":  "file:///path/to/you-need-me/.git/"
    "you-need-me-windows":  "C:/path/to/you-need-me-windows/.git/"
  }
~~~

So you don’t give a version, but a local or remote git endpoint:

If you use local path you MUST  these requi:

* specify the subdirectory **.git/**
* use an absolute directory

Instead of a version you can specify:

* `tag` : "bootstrap": "https://github.com/twbs/bootstrap.git#v3.0.0"
* `commit sha` : "bootstrap": "https://github.com/twbs/bootstrap.git#b67a4ec28b9cb0f16cd88f34491284dd15826d33"
* `branch name` : "bootstrap": "https://github.com/twbs/bootstrap.git#clean_super_clean"


# Create a bower package

* http://bower.io/docs/creating-packages/
* http://bob.yexley.net/creating-and-maintaining-your-own-bower-package/

What you need:

* a git repo to host the package

Package content:

* file to be IGNORED: rule of thumb is, just distribute what consumers need to be able to use your package...not all of your development dependencies, test suite, documentation, etc, etc.
* Typically you have a build script that generates that module into a dist folder, one thats minified, and one thats not.
* main???????

## Live update a dependency with bower link

REF:

* https://oncletom.io/2013/live-development-bower-component/

This is particularly useful for the following use cases:

* prototyping a Bower component before releasing it in the wild (you can link it even if it’s not yet available in the bower registry)
* testing a new feature in a live project
* checking why a component is failing to work as expected despite its unit and functional tests are fine

The link functionality allows developers to easily test their packages (ex: bootstrap-theme-pitchtarget). Linking is a two-step process:
    
1) Using `bower link` in the local development folder of the package will create a global link. This will "register" the package in a kind of local registry.

~~~
12:11 ~/SRC/ADDICTIVE/bootstrap-theme-pitchtarget (develop)$ bower link
bower                    link /Users/nicolabrisotto/.local/share/bower/links/bootstrap-theme-pitchtarget > /Users/nicolabrisotto/SRC/ADDICTIVE/bootstrap-theme-pitchtarget
~~~


2) Then to use the local linked package in some other package use `bower link <name>`. It will create a link in the bower_components folder pointing to the previously created link.
    
This allows to easily test a package because changes will be reflected immediately.

~~~
bower link bootstrap-theme-pitchtarget
bower bootstrap#~3.3.2          cached git://github.com/twbs/bootstrap.git#3.3.2
bower bootstrap#~3.3.2        validate 3.3.2 against git://github.com/twbs/bootstrap.git#~3.3.2
bower                    link /Users/nicolabrisotto/SRC/ADDICTIVE/middleman/pitchtarget_www_middleman/bower_components/bootstrap-theme-pitchtarget > /Users/nicolabrisotto/.local/share/bower/links/bootstrap-theme-pitchtarget
~~~

When the link is no longer necessary, simply remove it with `bower uninstall <name>` or `bower update` to restore the version listed in `bower.json`.




## Bootstrap bower package example

* https://github.com/twbs/bootstrap/blob/master/bower.json
* http://stackoverflow.com/questions/14450408/using-bootstrap-with-bower



# CHEATSHEET

* `bower install jquery` : will add jquery as an extraneous package

Example:

~~~
20:27 /tmp/pippo $ bower install jquery
bower jquery#*                  cached git://github.com/jquery/jquery.git#2.1.1
bower jquery#*                validate 2.1.1 against git://github.com/jquery/jquery.git#*
bower jquery#~2.1.1            install jquery#2.1.1

jquery#2.1.1 bower_components/jquery
~~~

* `bower install <package> --save` : will add <package> to your project’s bower.json dependencies array. Run it every time you want to definetively add a dependency

* `bower install <package> --save-dev` : install package and add it to bower.json devDependencies
Example:

~~~
bower list
bower check-new     Checking for new versions of the project dependencies..
pippo#0.0.0 /private/tmp/pippo
└── jquery#2.1.1 extraneous
~~~

* `bower prune` : Uninstalls local extraneous packages

Example:
~~~
20:19 /tmp/pippo $ bower prune
bower uninstall     jquery

? what types of modules does this package expose?:
 ◯ amd
 ◯ es6
❯◯ globals
 ◯ node
 ◯ yui
~~~
