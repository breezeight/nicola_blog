---
layout: post
title: "Ember.js"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["javascript"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

http://bower.io/

Bower is a package manager for the web. It offers a generic, unopinionated solution to the problem of front-end package management, while exposing the package dependency model via an API that can be consumed by a more opinionated build stack. 

Is a content-agnostic transport tool that only dumps all your dependencies (and their dependencies, recursively) into the file system. it’s up to you what to do with them. 
Tools like Broccoli sit on top of Bower.

 ??????????   main string or array: The primary acting files necessary to use your package.



bower.json documentation: http://bower.io/docs/creating-packages/#bowerjson

.bowerrc documentation:     http://bower.io/docs/config/

Bower command line documentation:  http://bower.io/docs/api/


CHEATSHEET

bower install jquery
will add jquery as an extraneous package

Example:
20:27 /tmp/pippo $ bower install jquery
bower jquery#*                  cached git://github.com/jquery/jquery.git#2.1.1
bower jquery#*                validate 2.1.1 against git://github.com/jquery/jquery.git#*
bower jquery#~2.1.1            install jquery#2.1.1

jquery#2.1.1 bower_components/jquery

bower install <package> --save
will add <package> to your project’s bower.json dependencies array. Run it every time you want to definetively add a dependency

bower install <package> --save-dev
install package and add it to bower.json devDependencies


Example:

bower list
bower check-new     Checking for new versions of the project dependencies..
pippo#0.0.0 /private/tmp/pippo
└── jquery#2.1.1 extraneous


bower prune
Uninstalls local extraneous packages

Example:
20:19 /tmp/pippo $ bower prune
bower uninstall     jquery

? what types of modules does this package expose?:
 ◯ amd
 ◯ es6
❯◯ globals
 ◯ node
 ◯ yui

