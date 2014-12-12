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

## Ruby code interpretation
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

#### ruby --dump parsetree

`ruby --dump parsetree /tmp/class.rb` this command will dump the AST

This command will show the same information of Ripper but instead of
showing symbols it will show the actual AST Nodes names from the C code.

### YARV: Code Compilation and Execution

See the [YARV Guide]({{site.url}}/guides/ruby_yarv.html)

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

## Lexical Scope and Costant Lookup

Note: See
[Here]({{site.url}}/guides/languages_analogies_and_differences.html#scope-and-binding)
for the definition of scope

Ruby use `Lexical scope`.

### Why Constants are really important

Constant Lookup is very important because constants, like modules and
classes, are central to the way Ruby works internally and to the way we
use Ruby:

* Whenever you define a module or class, you also define a constant.
* And whenever you refer to or use a module or class, Ruby has to look up the corresponding constant.

Ruby can find a Constant defined in a Superclass:

~~~ruby
class MyClass
  SOME_CONSTANT = "Some value..."
end

class Subclass < MyClass
  p SOME_CONSTANT
end

=> "Some value..."
~~~

or in a parent Class or Module:

~~~ruby
module Namespace
  SOME_CONSTANT = "Some value..."
  class Subclass
    p SOME_CONSTANT
  end
end

=> "Some value..."
~~~

### How the costant Lookup works: mapping between code and scopes

A `syntactical section` in Ruby defines a scope. Think of your Ruby
program as a series `syntactical section` that defines a scope:

* one for each module or class that you create
  * `class X; <<<<---- This is a synthactical section ------>>>> end`
  * `module X; <<<<---- This is a syntactical section ------>>>> end`
* and another for the default, top-level lexical scope.

Ruby compiles the code within the `syntactical section` into a YARV
instruction snippet and then attaches to it a couple of pointers to keep
track of the scope:

* `nd_next` pointer is set to the parent or surrounding lexical scope.
* `nd_clss` pointer indicates which Ruby class or module corresponds to this scope.

Scope is the set of all constant that are are visible within the
`syntactical section`. When ruby looks for a constant it will:

* iterates over the linked list formed by the nd_next pointers in each lexical scope (nd_next)
  * for each scope’s class check for `autoload`
* iterates through superclass chain (`nd_clss`)
  * for each superclass check for `autoload`

If the constant is found the iteation will end, otherwise
`const_missing` is called.

If Ruby loops through the entire lexical scope chain without finding the given constant or a corresponding autoload keyword, it then iterates
up the superclass chain. This allows you to load constants defined in a superclass. Ruby once again honors any autoload key- word that might exist in any of those superclasses, loading an additional file if necessary.
Finally, if all else fails and the constant still isn’t found, Ruby
calls the `const_missing` method on your module if you provided one


Scope Example: define MyClass using the class
keyword. Ruby sets the `nd_clss` pointer to the RClass structure
corresponding to MyClass and `nd_next` to the top level scope:

~~~ruby
class MyClass
  SOME_CONSTANT = "Some value..."
end
~~~

![ruby_lexical_scope_nd_next_nd_clss]({{ site.url }}/guides/images/ruby_lexical_scope_nd_next_nd_clss.jpg)


Summary:

* Ruby uses both the lexical scope tree and the superclass hierarchy to find constants that your code refers to.
* Ruby uses the class tree to find the methods that your code (and Ruby’s own internal code) calls


### Load, Require, Autoload

**TODO**:

* forse l'autoload è morto: https://www.ruby-forum.com/topic/3036681
* http://www.slideshare.net/DonSchado/ruby-require-autoloadload

refs:

* http://ruby-doc.org/core-2.1.0/Kernel.html#method-i-require
* http://ruby-doc.org/core-2.1.0/Kernel.html#method-i-autoload
* http://ruby-doc.org/core-2.1.0/Kernel.html#method-i-auto

`autoload` works in a similar way to `require`, but it only loads the file specified when a constant of your choosing is accessed/used for the first time.

If you use `require` the `thin/command` file is evaluated immediadly,
the execution is synchronous and the `Command` class will be available
in the current lexical scope.

~~~ruby
require 'thin/command'
~~~

If you use `autoload` the `thin/command` file will be evauated only when
another piece of code will look for the `Command` constant:

~~~ruby
autoload :Command, 'thin/command'
~~~




## Closures

REF: Ruby under a microscope ch8

* Why don't ruby methods have lexical scope? http://stackoverflow.com/questions/9089414/why-dont-ruby-methods-have-lexical-scope
* http://joshcheek.com/blog/1_lambda_proc_and_proc_new

{% github_sample_ref /ruby/ruby/blob/v2_2_0_preview2/vm_core.h %}
{% highlight c %}
{% github_sample /ruby/ruby/blob/v2_2_0_preview2/vm_core.h 533 540 %}
{% endhighlight %}

Closure is a the computer science concept introduced in Lisp long before
Ruby was created in the 1990s. Here’s how Sussman and Steele defined the
term closure in 1975:

* A “lambda expression” that is, a function that takes a set of arguments
* An environment to be used when calling that lambda or function

Ruby’s rb_block_t structure contains two important values that maps to
the same concepts:

* A pointer to a snippet of YARV code instructions the `iseq pointer`. iseq is a pointer to a lambda expression
* A pointer to a location on YARV’s internal stack, the location that was at the top of the stack when the block was created the EP pointer. EP is a pointer to the environment to be used when calling that lambda or function—that is, a pointer to the surrounding stack frame.

### Blocks implementation

Ruby represents each block using a C structure called `rb_block_t`.

The behavior of blocks is that they can access variables in the
surrounding or parent Ruby scope. To implment this behavior YARV tracks
the location of variables using the EP, or environment pointer, located
in the `rb_control_frame_t` of the code that call a method with a block.

When you call a method with a block argument:

* ruby initializes a new `rb_block_t` structure to represent the block.
* copies the current value of the EP into the new `rb_block_t` structure (saving the location of the current stack frame in the new block.)
* create a new `rb_control_frame_t` frame for the method
* Each time the method invoke `yield`:
  * Ruby’s internal yield code copies the EP from the block into the new stack frame
  * the ruby bloa


Thanks to this ruby can dynamically access variables from blocks, see:
[Local and Dynamic Access of Ruby Variables]({{ site.url }}/guides/ruby_yarv.html#local-and-dynamic-access-of-ruby-variables)

### Lambda and Proc

Lambda example:

~~~ruby
def message_function
  str = "The quick brown fox"
  lambda do |animal|
    puts "#{str} jumps over the lazy #{animal}."
  end
end
function_value = message_function
function_value.call('dog')
~~~

In ruby `lambda` is a method of the [Kernel module](http://www.ruby-doc.org/core-2.1.5/Kernel.html#method-i-lambda).
It is equivalent to Proc.new, except:

* the resulting Proc objects check the number of parameters passed when called.
* the resulting Proc object method `is_lambda?` return `true`

The `function_value` is an is an example of “treating a function as a
first-class citizen”:

* a reference to the block is stored in the Proc object.
* we can invoke it with the `Proc#call` method.

With the `lambda` method or the equivalent `proc` Ruby allows you to convert a block into a data value in this way.


When you call lambda, Ruby copies the entire contents of the current
YARV stack frame into the heap.

In fact, along with the copy of the stack frame, Ruby creates two other new objects in the heap:

* An internal environment object, represented by the rb_env_t C structure at the lower left of the figure. It’s essentially a wrapper for the heap copy of the stack. As we’ll see in Chapter 9, you can access this environment object indirectly in your programs using the Binding class.
* A Ruby proc object, represented by the rb_proc_t structure. This is the actual return value from the lambda keyword; it’s what the message_function function returns.

#### How a Proc is intenally stored

Ruby saves your data in two places:

*  on the stack
*  in the heap

When you create a Proc with lamba ruby:

* create an internal environment object represented by a `rb_env_t` C structure. It's essentially a wrapper of a copy of the stack.
* the current stack 
* a ruby `Proc` object represented by the `rb_proc_t` structure, which contains:
  * a `rb_block_t` with the `EP` pointer set to the heap copy of the stack.

Think of a proc as a kind of Ruby object that wraps up a block.

![ruby_create_lambda]({{ site.url }}/guides/images/ruby_create_lambda.jpg)


#### How ruby call a Proc

When Ruby executes the `Proc#call` method on the proc object, it executes
its block as well:

* new stack frame and sets the EP to the block’s referencing environment.
* that environment is a copy of a stack frame previously copied into the heap; the new stack frame contains an EP that points to the heap.
* now the block code has access to all the variables it had access when it was created.

Example:

~~~ruby
def message_function
   str = "The quick brown fox"
   lambda do |animal|
     puts "#{str} jumps over the lazy #{animal}."
   end
end
function_value = message_function
function_value.call('dog')

=> The quick brown fox jumps over the lazy dog.  ### The block executed by the lambda still have access to the str variable
~~~

#### Changing Local Variables After Calling lambda

When you create a proc Ruby should have copied the stack frame to the
heap but Ruby allow us to modify the new persistent copy of the stack
once it’s been created.

~~~ruby
def message_function
  str = "The quick brown fox"
  func = lambda do |animal|
    puts "#{str} jumps over the lazy #{animal}."
  end
  str = "The sly brown fox"                     ##### update str after Proc is istantiated
  func
end
function_value = message_function
function_value.call('dog')

=> "The sly brown fox jumps over the lazy dog." #####  the Proc's block uses the updated version of the str variable
~~~

How it is possible? We should work on the copy of the stack...

This is beacause the new copy of the stack is meant to persist on the
heap not to be different for each Proc.
Once Ruby creates the new heap copy of the stack (the new rb_env_t
structure or internal environment object), it resets the EP in the
rb_control_frame_t structure to point to the copy, so the current ISEQ
will work on the same stack copy of the Proc.

But how many copies of the stack does ruby create if we create multiple
Proc?

Only one!

Let's experiment a little bit:

~~~ruby
i= 0
increment_function = lambda do
  puts "Incrementing from #{i} to #{i+1}"
  i += 1
end

decrement_function = lambda do
  i -= 1
  puts "Decrementing from #{i+1} to #{i}"
end
~~~

If Ruby made a separate copy of the stack frame for each call to lambda, each function would operate on a separate copy of i.

Instead the exact opposite happens:

~~~ruby
increment_function.call
=> Incrementing from 0 to 1

decrement_function.call
=> Decrementing from 1 to 0

increment_function.call
=> Incrementing from 0 to 1

increment_function.call
=> Incrementing from 1 to 2

decrement_function.call
=> Decrementing from 2 to 1
~~~

#### Summary

* `blocks` implement the computer science concept of closure in Ruby
* Ruby allows you to treat functions or code as first- class citizens using the `lambda` keyword, which converts a block into a data value that you can pass, save, and reuse.


## Advanced Object management

**TODO** : move this chapter somewhere else

[Object Space](http://www.ruby-doc.org/core-2.1.5/ObjectSpace.html)
contains routines that interact with the garbage collection facility and allow you to traverse all living objects with an iterator.

`ObjectSpace.count_objects` returns the number of objects of a given type that exist.


