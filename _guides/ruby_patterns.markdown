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

Using only `include MyModule`, this pattern will allow you to add methods both to:

* the Student class singleton_class
* the objects instance of the Student class

To obtain this result you need a module `ClassMethods` nested into the `MyModule`. MyModule will use the `included` hook of `MyModule` to extend the including class.

**TODO**: check if this pattern is deprecated by `refinements`

~~~ruby
module MyModule
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
  include MyModule

  has_many :books
end
~~~

ref: http://stackoverflow.com/questions/4074962/class-vs-module-in-designing-ruby-api
