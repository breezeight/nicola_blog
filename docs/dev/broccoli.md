---
layout: post
title: "Broccoli"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["javascript", "css"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# INTRO

Homepage: https://github.com/broccolijs/broccoli

A fast, reliable asset pipeline, supporting constant-time rebuilds and compact build definitions. Comparable to the Rails asset pipeline in scope, though it runs on Node and is backend-agnostic.
It's an alternative to (grunt, make, Rails pipeline).

Intro blog post from Jo Liss, the Broccoli creator: http://www.solitr.com/blog/2014/02/broccoli-first-release/:

* `Tree`: is a directory with files and subdirectories
* Filesystem as api is used to trigger rebuilds
* Plugin are chainable plugins input is a tree, plugin output is a tree
* support for 1:1 compilers like cofeescript and N:1 compilers like Sass
* Behind the scene broccoli create all the temp dirs for you, cleanup them and watch the filesystem.

Intro: http://moduscreate.com/better-builds-begin-with-broccoli/

# Broccoli VS

## VS GRUNT
Broccoli does not attempt to replace Grunt at all. In fact, it’s a grunt plugin.
Grunt can be used instead of Broccoli but is slower (do not support trees) and require to create tmp dirs manually.

## VS BOWER
Broccoli itself is angnostic about Bower or ES6 modules.
Bower is a content-agnostic transport tool that only dumps all your dependencies (and their dependencies, recursively) into the file system—it’s up to you what to do with them. Broccoli aims to become the missing build tool sitting on top.

# Brocfile.js

A Brocfile.js file in the project root contains the build specification.
Doc: https://github.com/broccolijs/broccoli#brocfilejs

# Plugins API 

Doc: https://github.com/broccolijs/broccoli#plugin-api-specification

# Plugins

https://github.com/joliss/broccoli-static-compiler
