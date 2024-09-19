---
layout: post
title: "Ruby 3 and Rubinius 3"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["ruby"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# References

* Static type
  * https://www.omniref.com/blog/blog/2014/11/17/matz-at-rubyconf-2014-will-ruby-3-dot-0-be-statically-typed/


# Road to Rubinius 3

* http://rubini.us/2014/11/10/rubinius-3-0-part-1-the-rubinius-team/
* http://rubini.us/2014/11/11/rubinius-3-0-part-2-the-process/
* http://rubini.us/2014/11/13/rubinius-3-0-part-4-the-system-and-tools/,
    intro to what will change to Rubinius main components:
  * garbage collector
  * just-in-time compiler
  * Rubinius Console: Rubinius::Console
  * instruction interpreter
  * code that coordinates these components and starts and stops native threads
  * inspector: show the value of local variables, what methods are currently executing, and other aspects of the running program
  * Analysis:  investigate the execution graph to find relationships between code that are not visible in the source code due to Ruby's dynamic types.
  * Memory allocation measurement
  * CodeDB: store the bytecode from compiling Ruby code and read from
      this cache instead of recompiling the Ruby code. will improve load
      time and reduce memory usage from storing unused code.One of these
      may be a refactoring editor, which seems to be the holy grail of
      every object-oriented programmer. We think there are even more
      interesting tools than automated refactoring and are excited to
      tell you more about them.
*  http://rubini.us/2014/11/14/rubinius-3-0-part-5-the-language/ we have these things in Rubinius 3.0:
  * functions
  * gradual types for functions
  * multiple dispatch for methods and functions.
  * this is not Rubinius X
  * I want to thank the following people: Chad Slaughter for entertaining endless conversations about the purpose of programming languages and challenging my ideas. Yehuda Katz for planting the seed about functions. Brian T. Rice for trying to convince me that multiple dispatch was useful even if it took six years to see it. Joe Mastey and Gerlando Piro for review and feedback, some of it on these topics going back more than a year. 
  * http://titani.us/

