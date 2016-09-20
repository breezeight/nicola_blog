---
layout: post
title: "Ruby: How To Debug"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["ruby"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# References

# Find Memory Leaks

* http://www.be9.io/2015/09/21/memory-leak/?utm_source=rubyweekly&utm_medium=email


# Ruby >= 2.0

## RubyMine

Use debase

## ByeBug

* [Home page with some doc](https://github.com/deivid-rodriguez/byebug)
* [Official Guide](https://github.com/deivid-rodriguez/byebug/blob/master/GUIDE.md)
* [Rails guide about byebug](http://guides.rubyonrails.org/debugging_rails_applications.html#debugging-with-the-byebug-gem)

cheatsheet:

* `where` 
* `break line` set breakpoint in the line in the current source file.
* `break file:line [if expression]` set breakpoint in the line number inside the file. If an expression is given it must evaluated to true to fire up the debugger.
* `break class(.|\#)method [if expression]` set breakpoint in method (. and # for class and instance method respectively) defined in class. The expression works the same way as with file:line. 
* `n` or `next` will go to the next line within the same context. If this is the last line of the method, so byebug will jump to next next line of the previous frame.
* `s` or `step` will go the next ruby instruction to be executed.
* `display @articles` will watch the variable
* `v[ar] cl[ass]`                   show class variables of self
* `v[ar] const <object>`            show constants of object
* `v[ar] g[lobal]`                  show global variables
* `v[ar] i[nstance] <object>`       show instance variables of object
* `v[ar] l[ocal]`                   show local variables

## Pry-ByeBug

https://github.com/deivid-rodriguez/pry-byebug

# ruby <= 1.9

`gem debugger`
