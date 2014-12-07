---
layout: post
title: "MRI Ruby internals and the Ruby Object Model"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["ruby"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# References

* [Ruby Hacking Guide](http://ruby-hacking-guide.github.io) This book explores several themes with the following goals in mind:
  * To have knowledge of the structure of ruby
  * To gain knowledge about language processing systems in general
  * To acquire skills in reading source code
  * use **ruby 1.7.3**
* [Ruby under a microscope](/Volumes/ArchiveDisk/Archive/Misc/ebook/ruby/RubyUnderaMicroscope.pdf)
  * user **ruby 2.0**


# The Ruby Object model

## References

* https://github.com/rubyconfindia/conference/blob/master/2011/presentations/karthikS-DecipheringtheROM.pdf

## Classes and Objects

To define a class:

~~~ruby
class Mathematician
end
~~~

define a class means assign to a constant a reference to an instance of Class


If we don’t specify a superclass, Ruby assigns the Object class as the superclass

Mathematician.superclass => Object

Every value in Ruby is an object. This might be true for classes, too:

~~~ruby
Mathematician.class => Class
~~~


### Inheritance

Ruby support single inheritance:

~~~ruby
class Mathematician < Person
end
~~~

Mathematician.superclass => Person

You can inherit only from object of class Class

~~~ruby
class MyClass < String.new
  def self.to_s
     puts “Class method”
  end
end

TypeError: superclass must be a Class (String given)
~~~

`new` will instatiate a object:

~~~ruby
vivalabamba = KaraokeSong.new
~~~

When you call `new` on a class, ruby creates an uninitialized object and
then calls that object's initialize method, passing in any parameters
that were passed to new. You can call the superclass initialize method
with `super`:

~~~ruby
class KaraokeSong < Song
   def initialize(name, artist, duration, lyrics)
     super(name, artist, duration)
     @lyrics = lyrics
   end
end
~~~

### Class Instance Variables vs. Class Variables

* Instance variables: a name preceded by an `@` sign
  * created only when initializated
* Class variables: a name preceded by an `@@` sign
  *  shared among all objects of a class, there's only one copy
  *  are private to a class and its instances

example:

~~~ruby
class Planet
  @@planets_count = 0

  def initialize(name)
    @name = name
    @@planets_count += 1
  end

  def self.planets_count
    @@planets_count
  end
end

Planet.new("earth"); Planet.new("uranus")
p Planet.planets_count
~~~

~~~ruby
class B; @@y; end
NameError: uninitialized class variable @@y in B

class B; @@y=1; end
OK
~~~

### Class Methods

Class methods can be defined using different syntaxes:

~~~ruby
class Foo
  def self.bar # MOST READABLE
end
~~~

~~~ruby
class Foo
  class << self
     def bar
  end
end
~~~

~~~ruby
class Foo; end 
def Foo.bar
~~~

To call a class method:

~~~ruby
  Foo.bar
~~~

### Declaring Methods Visibility

http://en.wikibooks.org/wiki/Ruby_Programming/Syntax/Classes#Declaring_Visibility

`public`:

* its the default

`private`:

* In Ruby, “private” visibility is similar to what “protected” is in Java. Private methods in Ruby are accessible from children. You can’t have truly private methods in Ruby; you can’t completely hide a method.
* in C++, “private” means “private to this class”, while in Ruby it
    means “private to this instance”. What this means, in C++ from code in class A, you can access any private method for any other object of type A. In Ruby, you cannot: you can only access private methods for your instance of object, and not for any other object instance (of class A).
* Only accessible within the scope of a single object in which it is defined (truly private)
* Rule of thumb: private methods can only be called with implicit receiver
* for class methods (those that are declared using def
    ClassName.method_name), you need to use another function:
    `private_class_method`

~~~ruby
class Speaker
  def talk
    self.confident? ? "lecture..." : "Abscond!"
  end
private   # all methods that follow will be made private
  def confident?
    true
  end
end
~~~

~~~ruby
Speaker.new.talk
NoMethodError: private method 'confident?' called for #<Speaker:0x007fbcc484f430>
~~~

`protected`:

* [tender love post about protected methods](http://tenderlovemaking.com/2012/09/07/protected-methods-and-ruby-2-0.html)

[Method Visiblity Example]({{site.url}}/guides/ruby_examples/visibility.rb)

#### Syntax

For instance methods:

~~~ruby
private   # all methods that follow will be made private
  def confident?
~~~

~~~ruby
  def methodP
  end

   private :methodP   # Only this method is private
~~~

For private class methods:

~~~ruby
class SingletonLike
  private_class_method :new

  def SingletonLike.create(*args, &block)
    @@inst = new(*args, &block) unless @@inst
    return @@inst
  end
end
~~~

#### Use Case: Make new private for singleton

~~~ruby
 class SingletonLike
    private_class_method :new
 
    def SingletonLike.create(*args, &block)
      @@inst = new(*args, &block) unless @@inst
      return @@inst
    end
  end
~~~

### Accessors

[Accessor](http://www.rubyist.net/~slagell/ruby/accessors.html)

ruby has shortcut:

* `attr_reader :v` expands to: `def v; @v; end`
* `attr_writer :v` expands to: `def v=(value); @v=value; end`
* `attr_accessor :v` expands to: `attr_reader :v; attr_writer :v`
* `attr_accessor :v, :w` expands to `attr_accessor :v; attr_accessor :w` 


### Method lookup chain

http://tiagodev.wordpress.com/tag/ruby-object-model/


### Making Copies of Objects

Ruby is pass by reference, To duplicate any object, simply call the
`some_object.dup` method. A new object will be allocated and all of the object's instance variables will be copied over. However, copying instance variables is what this was supposed to avoid: this is what's called a "shallow copy." If you were to hold a file in an instance variable, both of the duplicated objects would now be referring to the same file.

## Modules

You can create a module just as you create a class—by typing the module keyword followed by a series of method definitions.

But while modules are similar to classes, they are handled differently by Ruby in three important ways:

* Ruby doesn’t allow you to create objects directly from modules. In practice this means that you can’t call the new method on a module because new is a method of Class, not of Module.
* Ruby doesn’t allow you to specify a superclass for a module.
* In addition, you can include a module into a class using the include keyword.
* you cannot create instance level variable of a Module

### Include

TODO: http://stackoverflow.com/questions/17552915/ruby-mixins-extend-and-include

### Extend

# MRI Internals

This chapter is summary of [Ruby Hack Guide](http://ruby-hacking-guide.github.io/object.html)
and Ruby under a Microscope

## YARV

To execute your code MRI ruby will go through 3 steps:

* `tokenizes` your code, which means it reads the text characters in your code file and converts them into `tokens`
* `parses` these tokens; that is, it groups the tokens into meaningful Ruby `statements` just as one might group words into sentences.
* `compiles` these statements into `low-level instructions` that it can execute later using a virtual machine.

### Code Tokenization and Parsing

See Ch1 of Ruby Under a microscope.

Ruby don't use Lex, the core team wrote the Ruby tokenization code by
hand, whether for performance reasons or because Ruby’s tokenization
rules required spe- cial logic that Lex couldn’t provide.

For parsing Ruby uses an LALR parser generator called `Bison`.

As Ruby parses your code, matching one grammar rule after another, it
converts the tokens in your code file into a complex internal data
structure called an `abstract syntax tree (AST)`

#### Ripper
`Ripper` makes it very easy to see what tokens Ruby creates for
different code files. Ripper is a library introduced in MRI Ruby 1.9 that hooks directly into Ruby 1.9's parser and which can provide you with abstract syntax trees or simple lexical analysis of the code that you provide

Ripper is not well documented, here you can find some doc:

* http://ruby-doc.org/stdlib-2.0/libdoc/ripper/rdoc/Ripper.html
* http://www.rubyinside.com/using-ripper-to-see-how-ruby-is-parsing-your-code-5270.html


~~~ruby
Ripper.sexp("your ruby code")

[
    [0] :program,
    [1] [...]
]
~~~


The `sexp` method parses src and create S-exp tree. It always return an
array of size 2, where the first element is the `:program` symbol and
the second is an array that contains one element for each statement of
the code. For example:

~~~ruby
require 'ripper'
require 'pp'

code = <<STR
puts "Hello"   ## one statements
STR

ast = Ripper.sexp(code)
puts ast[1].size
=> 1

code = <<STR
puts "Hello "  ## two statements
puts "World!";
STR

ast = Ripper.sexp(code)
puts ast[1].size
=> 2
~~~


This example defines a class

~~~ruby
require 'ripper'
require 'pp'

code = <<STR
class A < Array; end;
STR

pp Ripper.sexp(code)
~~~

~~~ruby
[
    [0] :program,
    [1] [
        [0] [
            [0] :class,
            [1] [
                [0] :const_ref,
                [1] [
                    [0] :@const,
                    [1] "A",
                    [2] [
                        [0] 1,
                        [1] 6
                    ]
                ]
            ],
            [2] [
                [0] :var_ref,
                [1] [
                    [0] :@const,
                    [1] "Array",
                    [2] [
                        [0] 1,
                        [1] 10
                    ]
                ]
            ],
            [3] [
                [0] :bodystmt,
                [1] [
                    [0] [           #### In this example the Class has no method, so the array has size 1 with and empty statement
                        [0] :void_stmt
                    ]
                ],
                [2] nil,
                [3] nil,
                [4] nil
            ]
        ]
    ]
]
~~~


If we add a couple of method the `:bodystmt` will contain 2 elements,
one for each method:

~~~ruby
require 'ripper'
require 'pp'

code = <<STR
class A < Array;
  def first
  end

  def second
  end
end;
STR

pp Ripper.sexp(code)
~~~


~~~ruby
.....
            [3] [
                [0] :bodystmt,
                [1] [
                    [0] [                 #### FIRST METHOD
                        [0] :def,         #### the :def symbol will tell you that this statement is a method definition
                        [1] [
                            [0] :@ident,  #### this t
                            [1] "first",
                            [2] [
                                [0] 2,
                                [1] 6
                            ]
                        ],
                        [2] [
                            [0] :params,  #### method parames
                            [1] nil,
                            [2] nil,
                            [3] nil,
                            [4] nil,
                            [5] nil,
                            [6] nil,
                            [7] nil
                        ],
                        [3] [
                            [0] :bodystmt, #### method body
                            [1] [
                                [0] [
                                    [0] :void_stmt
                                ]
                            ],
                            [2] nil,
                            [3] nil,
                            [4] nil
                        ]
                    ],
                    [1] [                 #### SECOND METHOD
                        [0] :def,
                        [1] [
                            [0] :@ident,
                            [1] "second",
.....
~~~


### Code Compilation

### Code Execution

http://patshaughnessy.net/2012/6/29/how-ruby-executes-your-code


## What is an Object

Three conditions are truly indispensable for objects to
be objects:

* The ability to differentiate itself from other objects (an identity)
    -> `VALUE`
* The ability to respond to messages (methods)
* The ability to store internal state (instance variables)

## VALUE pointer

In MRI VALUE is `typedef unsigned long VALUE;`

Each time ruby creates an instance of an object an `RObject` is created,
if you store a reference to that object it will be of type `VALUE`.

In practice, when using a `VALUE`, we cast it to the pointer to each
object struct. To cast there are helper macros, `Rxxxx()` that return a pointer:

~~~c
  VALUE str = ....;
  VALUE arr = ....;
  RSTRING(str)->len;   /* ((struct RString*)str)->len */
  RARRAY(arr)->len;    /* ((struct RArray*)arr)->len */
~~~

{% github_sample_ref /ruby/ruby/blob/v2_2_0_preview2/include/ruby/ruby.h %}
{% highlight c %}
{% github_sample /ruby/ruby/blob/v2_2_0_preview2/include/ruby/ruby.h 1079 1091 %}
{% endhighlight %}

All object structs start with a member `basic` of type `struct RBasic`.
As a result, if you cast this `VALUE` to `struct RBasic*`, you will be able to access the content of `basic`, regardless of the type of struct pointed to by `VALUE`.

* `RObject` contains
  * `RBasic`: contains information that all values use:
    * `flags` a set of Boolean that store a variety of internal technical
      value (type of the object, etc)
    * `klass` indicates which class an object is an
        instance of. It is a pointer to an instance of `RClass`

NOTE: this member is named `klass` so as not to conflict with the reserved word `class` when the file is processed by a C++ compiler.


{% github_sample_ref /ruby/ruby/blob/v2_2_0_preview2/include/ruby/ruby.h %}
{% highlight c %}
{% github_sample /ruby/ruby/blob/v2_2_0_preview2/include/ruby/ruby.h 771 774 %}
{% endhighlight %}


The structs, on the other hand, have several variations, a different struct is used based on the class of the object.

* `struct RObject`	 all things for which none of the following applies
* `struct RClass`	 class object
* `struct RFloat`	 small numbers
* `struct RString`	 string
* `struct RArray`	 array
* `struct RRegexp`	 regular expression
* `struct RHash`	 hash table
* `struct RFile`	 `IO`, `File`, `Socket`, etc…
* `struct RData`	 all the classes defined at C level, except the ones mentioned above
* `struct RStruct`	 Ruby’s `Struct` class
* `struct RBignum`	 big integers


## Methods

### RClass struct and Method Search

* Its struct type flag is `T_CLASS`
* Modules also use the `struct RClass` struct, and are differentiated by the `T_MODULE` struct flag.

{% github_sample_ref /ruby/ruby/blob/v2_2_0_preview2/include/ruby/ruby.h %}
{% highlight c %}
{% github_sample /ruby/ruby/blob/v2_2_0_preview2/include/ruby/ruby.h 814 819 %}
{% endhighlight %}

* `struct st_table` is an **hashtable** used everywhere in `ruby`. Its details will be explained in the next chapter “Names and name tables”, but basically, it is a table mapping names to objects.
* In the case of `m_tbl`, it keeps the correspondence between the name (`ID`) of the methods possessed by this class and the methods entity itself.
* `super` keeps, like its name suggests, the superclass.

* In Ruby there is only one class that has no superclass (the root class): `Object`.
* All `Object` methods are defined in the `Kernel` module, `Object` just includes it.

* The `m_tbl` of the object’s class is searched, and if the method was not found, the `m_tbl` of `super` is searched, and so on. If there is no more `super`, that is to say the method was not found even in `Object`, then it must not be defined.
* The sequential search process in `m_tbl` is done by `search_method()`.
* CACHE: once called, a method is cached. So starting from the second time it will be found without following `super` one by one.

## Instance variables

TODO: mi sa che è cambiato qualcosa in ruby 2.2 rispetto al libro

anche il meccanismo delle variabili di instanza usa una `struct st_table`

### st_table is an hash

http://ruby-hacking-guide.github.io/name.html

## Instances, Classes And Modules

See more at [ruby-hacking-guide Chapter 4: Classes and
modules](http://ruby-hacking-guide.github.io/class.html) and
RubyUnderaMicroscope.pdf Chapter 5

* A **Ruby object** is the combination of a class pointer and an array of instance variables.
* A **Ruby class** is a Ruby object that also contains method definitions, attribute names, a superclass pointer, and a constants table.

The main API to define classes and modules consists of the following 6 functions:

* `rb_define_class()`
* `rb_define_class_under()`
* `rb_define_module()`
* `rb_define_module_under()`
* `rb_define_method()`
* `rb_define_singleton_method()`

These C functions implement this ruby syntax:

~~~ruby
class Array < Object
~~~
(Ruby creates one RClass structure)

~~~ruby
class File < IO
  class Stat < Object
~~~

~~~ruby
module Enumerable
~~~

~~~ruby
class Pippo
  def to_s
  end
end
~~~

## Instance and Class variables

Internally, however, Ruby actually saves both class variables and class
instance variables in the same table inside the RClass structure. But:

* When you get or set a class instance variable, Ruby looks up the variable in the RClass structure corresponding to the target class and either saves or retrieves the value.


## Class methods and Singleton Class (aka Metaclass)

How does ruby handle class method definition?

Mathematician is a class with class method called `my_class_method`:

~~~ruby
class Mathematician
  class << self
    def class_method
      puts "This is a class method."
    end
  end
end
~~~

A class method are obviously not saved in the RClass method table along with normal methods, because instances of Mathematician cannot call them, as demonstrated here:

~~~
obj = Mathematician.new > obj.class_method
 => undefined method 'class_method' for #< Mathematician:0x007fdd8384d1c8 (NoMethodError)
~~~

Instead It turns out that whenever ruby create a new class, internally
Ruby creates two classes:

~~~
ObjectSpace.count_objects[:T_CLASS] v => 859
class Mathematician; end
ObjectSpace.count_objects[:T_CLASS] w => 861
~~~

The second class is a Singleton Class (aka `metaclass`) that ruby uses to store class methods:

~~~
class Mathematician
end

p Mathematician
 => Mathematician

 p Mathematician.singleton_class
 => #<Class:Mathematician>       #The metaclass of Mathematician

 p obj.singleton_class.methods
 => [ ... :class_method, ...  ]
~~~

See RubyUnderAMicroscope Experiment 5-2 for more details

[Object.singleton_class ruby doc](http://ruby-doc.org/core-2.1.0/Object.html#method-i-singleton_class)

![ruby_object_class_metaclass]({{ site.url }}/guides/images/ruby_object_class_metaclass.jpg)

NOTE: some old post call metaclass the singleton_class

## Modules implementation

REF: ch6 of ruby under a microscope

A `Ruby module` is a Ruby object that also contains method definitions, a superclass pointer, and a constants table.

* Ruby creates a copy of the RClass structure for the Professor module and uses it as the new superclass for Mathematician
* You can’t create object instances of a module, there are no object-level attributes to keep track of.
* When you include a module into a class, Ruby creates a copy of the RClass structure for module and uses it as the new superclass for class that includes that module.

NOTE: I suppose that ruby needs to create a copy of the RClass because
it need to change the value of the `super` pointer.

![ruby_object_class_metaclass]({{ site.url }}/guides/images/ruby_include_module.jpg)

## Method Lookup algorithm

This algorithm is remarkably simple, Ruby simply follows the super pointers until it finds the class or module that contains
the target method.
You might imagine that Ruby would have to distinguish between modules and classes using some special logic that it would have to handle the case where there are multiple included modules, for example. But no, it’s just a simple loop on the super pointer linked list.

What is most interesting here is that internally, Ruby implements module inclusion using class inheritance.

Essentially, **there is no difference between including a module and specifying a superclass**.

Both procedures make new methods available to the target class, and both use the class’s super pointer internally. Including multiple modules into a Ruby class is equivalent to specifying multiple superclasses.

### The Global Method Cache
Depending on the number of superclasses in the chain, method lookup can be time consuming. To alleviate this, Ruby caches the result of a lookup for later use.

Ruby uses another type of cache, called an `inline method cache`, to
speed up method lookup even more. The inline cache saves information
alongside the compiled YARV instructions that Ruby executes.

### Including two modules into a class

~~~ruby
class Mathematician < Person
  include Professor
  include Employee
end
~~~

Because Employee appears above Professor in the superclass chain, as shown along the left side of Figure 6-11, methods from Employee override methods from Professor, which in turn override methods from Person, the actual superclass.

![Including_two_modules_into_a_class]({{ site.url }}/guides/images/Including_two_modules_into_a_class.jpg)

### Including One Module into Another

We can include one module into another:

~~~ruby
module Professor < Employee
end

module Professor
  include Employee
end
~~~

Implementation: Modules can’t have a superclass in your code, but they can inside Ruby because Ruby represents modules with classes internally!
When we include Professor into Mathematician, Ruby iterates over the two
modules and inserts them both as superclasses of Mathematician.

![ruby_including_two_modules_into_a_class_at_the_same_time]({{ site.url }}/guides/images/ruby_including_two_modules_into_a_class_at_the_same_time.jpg)

### Classes See Methods Added to a Module Later

Lets define and include a module:

~~~ruby
module Professor
  def lectures; end
end

class Mathematician
  attr_accessor :first_name
  attr_accessor :last_name
  include Professor
end
~~~

Now add a new method to the Professor Module, it will be add also to the
Mathematician class:

~~~ruby
module Professor
     def primary_classroom; end
end

p fermat.methods.sort
 => [ ... :first_name, :first_name=, ... :last_name, :last_name=, :lectures,
   ... :primary_classroom, ... ]
~~~

This happens because ruby make a copy of the class module but the
included classes share the method table with the original module

Ruby doesn’t copy the method table for Professor. Instead, it simply
sets `m_tbl` in the new copy of Professor, the “included class,” to point
to the same method table.

![ruby_module_class_copy_shares_method_table]({{ site.url }}/guides/images/ruby_module_class_copy_shares_method_table.jpg)

### Classes Don’t See Submodules Included Later

Including a module into a module already included into a class does not affect that class.

~~~ruby
module Professor            ### Professor module defined
  def lectures; end
end

class Mathematician
  attr_accessor :first_name
  attr_accessor :last_name
  include Professor         ### Include Professor
end

module Employee
  def hire_date; end
end

module Professor
  include Employee          ### Include Employee module into Professor
end
~~~

Instances of Mathematician don't include the `hire_date` method:

~~~ruby
Mathematician.new.methods.grep(/hire_date/)
=> []
~~~

Why? Including Employee into Professor changes the Professor module. The
chain that ruby creates when you included the module Professor into the
Mathematician class was based on the previous status of the module, the
RClass of the module referred by Mathematician is a copy that share only
the method hash with the original RClass.


### Prepend a Module, the origin class

Sometime you want to override a class method including a module but you
cannot because ruby handle `included` module as a superclass.

In this example we want to add "Prof" to the name method:

~~~ruby
module Professor
  def name
    "Prof. #{super}"
  end
end

class Mathematician
  attr_accessor :name
  include Professor
end

poincaré = Mathematician.new
poincaré.name = "Henri Poincaré"

p poincaré.name
=> "Henri Poincaré"
~~~

![ruby_include_module]({{ site.url }}/guides/images/ruby_include_module.jpg)


The solution is to use `prepend`. When you prepend a module:

* Ruby creates a copy of the target class (called the `origin class` internally)
* sets `origin class` as the superclass of the prepended module
* moves all of the methods from the original class to the origin class, which means that those methods may now be overridden by methods with the same name in the prepended module.

![ruby_prepend_module]({{ site.url }}/guides/images/ruby_prepend_module.jpg)

## Advanced Object management

**TODO** : move this chapter somewhere else

[Object Space](http://www.ruby-doc.org/core-2.1.5/ObjectSpace.html)
contains routines that interact with the garbage collection facility and allow you to traverse all living objects with an iterator.

`ObjectSpace.count_objects` returns the number of objects of a given type that exist.


