---
layout: post
title: "Ruby"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["ruby"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# References

* [Official Ruby reference](http://www.ruby-doc.org/)

* RUAM: RubyUnderaMicroscope.pdf

https://www.youtube.com/user/CooperPress/videos

# Intro to Ruby for Java developers

Java:

* Classes should be closed to modification and open to extension
* Has Interfaces: desing by contract using interfaces

Ruby:

* Class can be modified
* has NO interfaces
* Duck Typing
* `self` is not the same as this in Java


# Ruby Object model

See [Here]({{site.url}}/guides/ruby_object_model.html) for:

* Classes
* Objects
* Modules
* Method visibility: public, private, protected
* inheritance

# Exceptions

* http://rubylearning.com/satishtalim/ruby_exceptions.html
* http://ruby-doc.com/docs/ProgrammingRuby/html/tut_exceptions.html
* http://en.wikibooks.org/wiki/Ruby_Programming/Exceptions
* [Exception class doc](http://www.ruby-doc.org/core-2.1.5/Exception.html)

~~~ruby
begin
  # Exceptions raised by this code will
  # be caught by the following rescue clause
  while data = socket.read(512)
    opFile.write(data)
  end

rescue SystemCallError
  $stderr.print "IO failed: " + $!
  opFile.close
  File.delete(opName)
  raise
end
~~~

* `$!` will contain the current exception
* `$@` contains the current exception’s backtrace.


# Enumeration in Ruby 2.x

**TODO**
https://www.youtube.com/watch?v=Kg4aWWIsszw

# Keyword Arguments

Why you should use keyword arguments:

* By using keyword arguments, we know what the arguments mean without looking up the implementation
* don’t have to write the boilerplate code to extract hash options.
* Like most things, keyword arguments have their trade-offs. Positional arguments offer a more succinct way to call a method.
* Usually, the code clarity and maintainability gained from keyword arguments outweigh the terseness offered by positional arguments. I would use positional arguments if I could easily guess their meanings based on the method’s name, but I find this rarely to be the case.

Since ruby 2.0:

{% highlight ruby %}
def foo(bar: 'default')
  puts bar
end

foo # => 'default'
foo(bar: 'baz') # => 'baz'
{% endhighlight %}


Also blocks can be defined with keyword arguments:

{% highlight ruby %}
define_method(:foo) do |bar: 'default'|
  puts bar
end

foo # => 'default'
foo(bar: 'baz') # => 'baz'
{% endhighlight %}

Since ruby 2.1 required arguments are supported:

{% highlight ruby %}
def foo(bar:)
  puts bar
end

foo # => ArgumentError: missing keyword: bar
foo(bar: 'baz') # => 'baz'
{% endhighlight %}


In Ruby 1.9, we could do something similar using a single Hash parameter:

{% highlight ruby %}
def foo(options = {})
  bar = options.fetch(:bar, 'default')
  puts bar
end

foo # => 'default'
foo(bar: 'baz') # => 'baz'
{% endhighlight %}


## TIPS: Migrate from hash to keywords

Calling code is syntactically equal to calling a method with hash arguments, which makes for an easy transition from options hashes to keyword arguments.

# Connascence in Ruby


“Two software components are connascent if a change in one would require the other to be modified in order to maintain the overall correctness of the system. Connascence is a way to characterize and reason about certain types of complexity in software systems.”

Below I’ve listed out the various kinds of connascence in order from weakest to strongest.

* `Name`: when multiple components must agree on the name of an entity.
* `Type`: when multiple components must agree on the type of an entity.
* `Meaning`: when multiple components must agree on the meaning of specific values.
* `Position`: when multiple components must agree on the order of values.
* `Algorithm`: when multiple components must agree on a particular algorithm.
* `Execution (order)`: when the order of execution of multiple components is important.
* `Timing`: when the timing of the execution of multiple components is important.
* `Identity`: when multiple components must reference the entity.

See here for more detaisl http://blog.rubybestpractices.com/posts/gregory/056-issue-24-connascence.html

# Interpreter Internals
This chapeter is only a brief summary, see RubyUnderaMicroscope.pdf for
more info

## Compile ruby code

* Starting with version 1.9, Ruby compiles your code before executing it.
* Ruby core team introduced **Yet Another Ruby Virtual Machine (YARV)**,
    which actually executes your Ruby code. Similar at highlevel to a
    JVM
* YARV Produce **bytecode** : YARV instructions
* RubyVM::InstructionSequence object
