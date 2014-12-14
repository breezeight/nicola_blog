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
* [Ruby Forum](https://www.ruby-forum.com/)
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

# Including other files: require, load, autoload, gems

If you define some ruby code in multiple files and you want to
incorporate them into your new programs, you need a way to tell ruby to
compile and execute them.

Ruby has two statements that do this: `load` and `require`

Any **constants or globals** within the loaded source file will be
available in the calling program’s **global namespace**.
(NB: this means also every class defined in that file).

The `load` method includes the named Ruby source file every time the method is executed

~~~ruby
load 'filename.rb'
~~~

The more commonly used `require` method loads any given file only once:

~~~ruby
require 'filename'
~~~

Local variables in a loaded or required file are not propagated to the scope that loads or requires them.

For example, here’s a file called included.rb:

~~~ruby
a=1
def b
  2
end
~~~

And here’s what happens when we include it into another file:


~~~ruby
a = "cat"
b = "dog"

require 'included'

a → "cat"
b → "dog"
b() → 2
~~~

`require` is a method of the Kernel Module, see
[doc](http://ruby-doc.org/core-2.1.0/Kernel.html#method-i-require)

`require my_file` will search a file `my_file.rb` into every directory
of the $LOAD_PATH variable (also defined as `$:`).

TODO:

* require 'rubygems' will add more search capabilities
* http://selfless-singleton.rickwinfrey.com/2012/12/20/-rubys-load-path/

## Autoload

[Autoload](http://www.subelsky.com/2008/05/using-rubys-autoload-method-to.html)
associate a constant with a filename to be loaded the first time that
constant is referenced.

load vs require: http://stackoverflow.com/questions/804297/when-to-use-require-load-or-autoload-in-ruby

# Ruby Closure: Block, Proc, Lambda

See the [Ruby Object model]({{site.url}}/guides/ruby_object_model.html)
for a deep analisys.

The Ruby implementation of closures is `block`, it act like drop-in
code snippets and has a reference to the environment it was created in.

~~~ruby
my_obj.my_method(arg0, arg1) do |a,b,c| ### This is a block with 3 params
end
~~~

* you can provide **ONLY ONE** block to a ruby method
* every ruby method can be invoked with a block param

To invoke a block a must use the `yield` keyword:

~~~ruby
def.my_method(arg0, arg1) do
  a = "..." + arg0 + arg1
  yeild(a, arg0, arg1) if block_given?
end
~~~

`Proc` is a class that can save a block for later execution.
`lambda` is a method of the Kernel module that return a Proc that will
check that the `call` method is invoked with same number of arguments
the wrapped block expects.

Procs fall into two categories:

* lambda Procs (that return true on`Proc#lambda?`). They are defined using `lambda` or `->()`.
* Procs that aren't lambda, simple procs. Dimple procs are defined using `Proc.new` or `proc`

~~~ruby
irb(main):001:0> lambda{ |x| x*2 }
=> #<Proc:0x007f9e8a8c3f40@(pry):34 (lambda)>

irb(main):002:0> ->(x){ x*2 }
=> #<Proc:0x007f9e7a896ed8@(pry):35 (lambda)>

irb(main):003:0> Proc.new{ |x| x*2 }
=> #<Proc:0x007f9e7a8f95d8@(pry):36>

irb(main):004:0> proc{ |x| x*2 }
=> #<Proc:0x007f9e7a950e28@(pry):37>
~~~

A `lambda Proc` is different because:

* lambdas are strict argument checkers, like methods, they can throw an ArgumentError exception if the number of arguments used to call the wrapped block is wrong. Simple procs will just ignore incorrect, extra or fewer argument combinations.
* lambdas act like methods regarding their return status - they can return values just like methods. When you try to return a value from a simple proc you end up with a `LocalJumpError` .

~~~ruby
def calls_with_args(proc)
  one = 1
  two = 2
  proc.call(one, two)
end

proc_with_new = Proc.new{|a, b, c| puts "Give me a #{a} and a #{b} and a #{c.class}"}
=> #<Proc:0x007fd5bb1e1bb0@(irb):8>

calls_with_args(proc_with_new)
=> Give me a 1 and a 2 and a NilClass

proc_with_lambda = lambda{|a, b, c| puts "Give me a #{a} and a #{b} and a #{c.class}"}
=> #<Proc:0x007fd5bb8ef128@(irb):10 (lambda)>

calls_with_args(proc_with_lambda)
=> ArgumentError: wrong number of arguments (2 for 3)
~~~


Refs:

* http://www.skorks.com/2010/05/closures-a-simple-explanation-using-ruby/


## The & operator

`&` can be quite confusing because it has a different meaning depending on the context in which it's used.

ref: http://ablogaboutcode.com/2012/01/04/the-ampersand-operator-in-ruby/

### Unary &
Since both Blocks and Procs are useful, it's convenient to be able to
switch between them - enter the unary  `&`.

`&` is almost the equivalent of calling `#to_proc` on the object, but
not quite. `&object` is evaluated in the following way:

* if object is a block, it converts the block into a simple proc.
* if object is a Proc, it converts the object into a block while preserving the lambda? status of the object.
* if object is not a Proc, it first calls #to_proc on the object and then converts it into a block.

Let's examine each of these steps individually.

#### If object is a block, it converts the block to a simple proc
The simplest example of this is when we want to have access to the block we pass to a method, instead of just calling yield. To do this we need to convert the block into a proc.

~~~ruby
def describe(&block)
  "The block that was passed has parameters: #{block.parameters}"
  end

irb(main):001:0> describe{ |a,b| }
=> "The block that was passed has parameters: [[:opt, :a], [:opt, :b]]"

irb(main):002:0> describe do |*args|
irb(main):003:0> end
=> "The block that was passed has parameters: [[:rest, :args]]"
~~~

#### If object is a Proc, it converts the object into a block while preserving the lambda? status of the object.
This is an extremely useful case of the `&` operator. For instance, we
know that `Array#map` takes a block, but say we have a proc that we want to re-use in multiple map calls.

~~~ruby
irb(main):001:0> multiply = lambda{ |x| x*2 }

irb(main):002:0> [1,2,3].map(&multiply)
=> [2, 4, 6]
irb(main):003:0> [4,5,6].map(&multiply)
=> [8, 10, 12]
~~~

Keep in mind that the operator also preserves the lambda? status of the original block. That's kind of neat because it means we are able to pass lambdas (not simple procs) as blocks. That means we can impose strict argument checking in our blocks and we can have them return values using the return keyword. The only exception to this preservation is methods, which are always lambdas regardless of how they are defined.

~~~ruby
def describe(&block)
  "Calling lambda? on the block results in #{block.lambda?}."
end
irb(main):001:0> describe(&lambda{})
=> "Calling lambda? on the block results in true."
irb(main):002:0> describe(&proc{})
=> "Calling lambda? on the block results in false."
class Container
  define_method(:m, &proc{})
end
irb(main):001:0> describe(&Container.new.method(:m).to_proc)
=> "Calling lambda? on the block results in true."
~~~

#### If object is not a Proc, it first calls to_proc on the object and then converts it into a block.

This is where the magic really happens because it makes passing objects
to functions in the place of blocks very simple. The most common case of
this is probably calling into `Array#map` with a symbol.

~~~ruby
irb(main):001:0> ["1", "2", "3"].map(&:to_i)
=> [1, 2, 3]
~~~

This works because calling `Symbol#to_proc` returns a proc that responds to the symbol's method.
So the `:to_i` symbol is first converted to a proc, and then to a block.
This is kind of cool because we can create our own `to_proc` methods.

~~~ruby
class Display
  def self.to_proc
    lambda{ |x| puts(x) }
  end
end

class FancyDisplay
  def self.to_proc
    lambda{ |x| puts("** #{x} **") }
  end
end
irb(main):001:0> greetings = ["Hi", "Hello", "Welcome"]

irb(main):002:0> greetings.map(&Display)
Hi
Hello
Welcome
=> [nil, nil, nil]

irb(main):003:0> greetings.map(&FancyDisplay)
** Hi **
** Hello **
** Welcome **
=> [nil, nil, nil]
~~~

### Bitwise &
Bitwise & is a simple method.

Bitwise AND is the binary bit-by-bit equivalent of boolean AND. So
binary `101 & 100 = 100` and binary `101 & 001 = 001`. `&` is defined as
a bitwise AND operator for Bignum, Fixnum and Process::Status, etc

Set Intersection, possibly the simplest use of the binary `&` operator
is in the `Array` class. & is the set-intersection operator, which means
the result is a collection of the common elements in both arrays:

~~~ruby
irb(main):001:0> [1,2,3] & [1,2,5,6]
=> [1, 2]
~~~

Boolean AND, On the FalseClass, NilClass and TrueClass binary & is the equivalent of the boolean AND. Keep in mind this does not work like the && operator, since it is only defined on these three classes.

~~~ruby
irb(main):001:0> false & true
=> false
irb(main):002:0> nil & true
=> false
irb(main):003:0> true & Object.new
=> true
irb(main):004:0> Object.new & true
=> NoMethodError: undefined method '&' for #<Object:0x007f9e7ac96420>
~~~

## Usecases

use cases for Blocks:

* Your method is breaking an object down into smaller pieces, and you want to let your users interact with these pieces.
* You want to run multiple expressions atomically, like a database migration.

Use cases for Procs:

* You want to reuse a block of code multiple times.
* Your method will have one or more callbacks.

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
