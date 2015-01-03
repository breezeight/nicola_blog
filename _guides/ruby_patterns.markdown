---
layout: post
title: "Ruby Patterns"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["ruby"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# References


# Add class method including a module

This pattern 
~~~ruby
module Base
  def self.included(klass)
    klass.extend ClassMethods
  end

  module ClassMethods
    def has_many(*args)
      # ...
    end
  end
end

class Student
  include Base

  has_many :books
end
~~~

ref: http://stackoverflow.com/questions/4074962/class-vs-module-in-designing-ruby-api


# Monadas

* http://codon.com/refactoring-ruby-with-monads
* https://www.youtube.com/watch?v=J1jYlPtkrqQ&feature=share



## Some Minor pattern you can find in code

### Singleton classes

`(class << self; self; end)` : return the singleton class of `self`
