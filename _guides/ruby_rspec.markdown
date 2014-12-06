---
layout: post
title: "Ruby: RSpec"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["ruby"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}


# Intro


RSpec is a tool to make Test-Driven Development. It is a multi-gem project:

* `rspec`:  a rich command line program
* `rspec-core`: textual descriptions of examples and groups
* `rspec-mocks`: built-in mocking/stubbing framework
* `rspec-expectations`: extensible expectation language
* `rspec-rails`: integration with rails

[Full documentation](https://relishapp.com/rspec/rspec-core/docs) generated
by cucumber features (`rspec-core/features`) is published on Relishapp

RSpec rubydoc is available here:

* [rspec-core](http://www.rubydoc.info/gems/rspec-core)
* [rspec-mocks](http://www.rubydoc.info/gems/rspec-mocks)
* [rspec-expectations](http://www.rubydoc.info/gems/rspec-expectations)
* [rspec-rails](http://www.rubydoc.info/github/rspec/rspec-rails)


# References

* https://www.relishapp.com/rspec/rspec-core/docs
* Intro:      http://rspec.info/
* rspec binary DOC: https://www.relishapp.com/rspec/
* http://www.intridea.com/blog/2012/3/23/polishing-rubies-part-iii
* RSPEC3 matcher for double number: http://wegowise.github.io/blog/2014/09/03/rspec-verifying-doubles/
* http://betterspecs.org/


# RSpec3

# Upgrade from RSpec2

One of the may news is the new "expect" syntax, it allows RSpec to avoid monkey-patching the Ruby Object class.

* ref: Upgrade guide from rspec2: https://relishapp.com/rspec/docs/upgrade
* ref: Notable Changes in RSpec 3 http://myronmars.to/n/dev-blog/2014/05/notable-changes-in-rspec-3
* RSPEC3 composable matcher: http://myronmars.to/n/dev-blog/2014/01/new-in-rspec-3-composable-matchers


# Conventions and CheatSheet

# RSPEC Under the HOOD


http://modocache.svbtle.com/rspec-under-the-covers
http://modocache.svbtle.com/code-reading-shared-examples-in-rspec

RSpec is a DSL for creating executable examples of how code is expected to behave, organized in groups.

Main concept and relationship:

* the `describe` (alias: `context`) creates an `ExampleGroup`
* it  <-> Example
* let <->
* subject <->
* expect <->   ExpectationTarget
* to, to_not  <->   PositiveExpectationHandler,  NegativeExpectationHandler
* Expectations are the “left-side” part of the example. The “right-side” part is the Matcher. 
* ExpectationHandler  <-> Matcher



# RSpec2


