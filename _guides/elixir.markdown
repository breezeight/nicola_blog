---
layout: post
title: "Elixir"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["elixir"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# TODO

Functional programming is about making the complex parts of your system explicit.

Questions
What are the strengths of Erlang?
Why is the programming world becoming more interested in concurrency, distributed systems and functional languages?
Can you contrast how errors are handled in Erlang and Elixir, compared to other languages?
What was the reason for building Elixir? What did Erlang lack?
Elixir compiles to bytecode for the Erlang VM – what does this mean?
What is meta programming?
How is the adoption of Phoenix and where is it headed?

http://softwareengineeringdaily.com/2016/04/18/elixir-erlang-jose-valim/


* `@behaviour  @callback   @macrocallback @optional_callbacks`
* [Naming Convention](https://hexdocs.pm/elixir/naming-conventions.html#content)




# Resources

* Awesome Elixir: https://github.com/h4cc/awesome-elixir
* Trending on Github: https://github.com/trending/elixir
* Static code analyzer: https://github.com/rrrene/credo   
  * code style: https://github.com/rrrene/elixir-style-guide
* Docker Hub: https://hub.docker.com/_/elixir/
* https://elixirforum.com/
* http://elixirstream.com/
* http://joearms.github.io/2013/05/31/a-week-with-elixir.html

Books:

* 2016 THE LITTLE ELIXIR & OTP GUIDEBOOK: http://benjamintan.io/
* "Metaprogramming Elixir" by Chris McCord the author of Phoenix https://pragprog.com/book/cmelixir/metaprogramming-elixir

Elixir release notes:

* All: http://elixir-lang.org/blog/categories.html#Releases
* http://elixir-lang.org/blog/2014/04/21/elixir-v0-13-0-released/
* http://elixir-lang.org/blog/2014/06/17/elixir-v0-14-0-released/
  * derive
  * Protocol consolidation
  * Nested access
  * Mix and OTP
*
  * Full release: https://github.com/elixir-lang/elixir/releases/tag/v1.4.0
  * Registry
  * Syntax coloring
  * Task.async_stream
  * Application inference
  * Mix install from SCM

# People and companies

* José Valim, Founder and Director of Research and Development at Plataformatec
  * https://www.linkedin.com/in/jovalim
* 

# IEx

Doc: https://hexdocs.pm/iex/IEx.html#summary

* Print the current config `IEx.configuration()`
* History: https://github.com/ferd/erlang-history

# Atom Elixir

https://brainlid.org/elixir/2015/11/12/atom-editor-and-elixir.html


# CHEATSHEET

IEx:

* Help from iex: `h String`
* `~/.iex.exs` and local `.iex.exs`
* inspect (implement proto, etc):  `i "hello"`
* `#iex:break` Cancel a multiline command

* Cheatsheet: https://media.pragprog.com/titles/elixir/ElixirCheat.pdf
* Start a script: `iex math.exs`

# Install Elixir, Erlang and hex 

Docker Example:

* Erlang image: https://github.com/c0b/docker-erlang-otp/blob/ea32d5f6f1735f9f55bee04b112166da96eb9c73/19/Dockerfile
* Elixir image: https://github.com/c0b/docker-elixir/blob/22ee98417200ef8d9a049b2b4504e7cf279e911f/1.2/Dockerfile

## Install Multiple versions

EVM Switching between multiple Erlang versions:

* evm https://medium.com/@ivorpaul/switching-between-multiple-erlang-versions-5559923ea7cd#.24kbmsk9x
* kerl: `brew install kerl`


Manage multiple Elixir version with Kiex:

* `brew install kiex`
* To install https://github.com/taylor/kiex
* http://learningelixir.joekain.com/installing-multiple-elixir-version-with-kiex/
* `kiex use 1.3.4`


Another alternative is [ASDF](https://github.com/asdf-vm/asdf)

## Erlang-Elixir Code Portability

http://stackoverflow.com/questions/2255658/how-portable-are-erlang-beam-files


## Editor - IDE

### Intellij

* `brew cask install intellij-idea-ce` ce = comunity edition

# Mix

A build tool that ships with Elixir.

Ref:

* into: http://elixir-lang.org/getting-started/mix-otp/introduction-to-mix.html
* [Mix doc](https://hexdocs.pm/mix/Mix.html)

Mix that provides tasks for:

* creating,
* compiling,
* testing your application,
* managing its dependencies and much more;

TODO:

* archive.install
Non ho capito come avere versioni multiple di phoenix e perchè non si usa hex....
```
 mix archive.install https://github.com/phoenixframework/archives/raw/master/phoenix_new.ez
Found existing archive: /Users/nicolabrisotto/.mix/archives/phoenix_new-1.2.1.
Are you sure you want to replace it with "https://github.com/phoenixframework/archives/raw/master/phoenix_new.ez"? [Yn] Y
```

* nerves.new
* deps.get
* compile
* firmware
* OTP application: come va gestita la voce "application" in un progetto gestito con Mix ?


## Project Structure

* ebin - contains the compiled bytecode
* lib - contains elixir code (usually .ex files)
* test - contains tests (usually .exs files)

## Create a simple Mix Project

http://elixir-lang.org/getting-started/mix-otp/introduction-to-mix.html#our-first-project

`-S option` to run scripts: `iex -S mix`

## Custom Mix Tasks

* [Tutorial](https://medium.com/blackode/mix-task-creation-in-elixir-project-d89e49267fe3#.crf3y6ic3)
* [Doc](http://elixir-recipes.github.io/mix/custom-mix-task/)

## Mix Alias 

https://sergiotapia.me/alias-your-phoenix-mix-commands-for-some-nice-developer-ux-4a02b2bf3474#.i9ag1tbd1

## Mix Xref

Ref: http://elixir-lang.org/blog/2016/06/21/elixir-v1-3-0-released/

`mix xref unreachable`:

* performs cross reference checks in your code and find calls to modules and functions that do not exist.
* Since such checks can discover possible bugs in your codebase, a new compiler called xref has been added to Mix.compilers/0, so it runs by default every time you compile your code.

 `mix xref callers Foo` or `mix xref callers Ecto.Queryable.to_query/1`
*  used to find all places in your code that calls a function from the module Foo

* `mix xref graph` - generates a graph with dependencies between source files

## Mix app.tree and deps.tree

list all applications your current project needs to start in order to boot (i.e. the ones listed in application/0 in your mix.exs) while the second will lists all of your dependencies and so on recursively

* mix deps.tree --format dot --only prod
* `--format dot` option can also be given to generate graph files to be opened by GraphViz.

## Mix task commandline options

Elixir v1.3 includes improvements to the option parser, including OptionParser.parse!/2 and OptionParser.parse_head!/2 functions that will raise in case of invalid or unknown switches. Mix builds on top of this functionality to provide automatic error reporting solving a common complaint where invalid options were not reported by Mix tasks.

For example, invoking mix test --unknown in earlier Elixir versions would silently discard the --unknown option. Now mix test correctly reports such errors:

```
$ mix test --unknown
** (Mix) Could not invoke task "test": 1 error found!
--unknown : Unknown option
```

# HEX

* [Hex Homepage](https://github.com/hexpm/hex)
* https://hex.pm/docs/usage

Hex is a package manager for the Erlang ecosystem.

This project currently provides tasks that integrate with Mix, Elixir's build tool.


# Testing and code quality


## Code coverage

https://github.com/parroty/excoveralls  + optionally coveralls.io service

## Profiling

Using kcachegrind: http://blog.equanimity.nl/blog/2013/04/24/fprof-kcachegrind/

## Best Practices

### When to Use Structs, String-keyed Maps, and Atom-keyed Maps

https://engineering.appcues.com/2016/02/02/too-many-dicts.html

# Are Elixir variables really immutable?

* http://stackoverflow.com/questions/29967086/are-elixir-variables-really-immutable
* http://blog.plataformatec.com.br/2016/01/comparing-elixir-and-erlang-variables/

In Elixir, once a variable references a list such as [1,2,3], you know it will always reference those same values (until you rebind the variable).

## What is the difference between mutability and rebinding?

```
name = "elixir"     
cap_name = String.capitalize name
"Elixir"     
name    
"elixir"
```

* The data structure referenced by name is never changed
* In functional we never tranform data

# Types

Elixir’s built-in types are

Value types:
Arbitrary-sized integers
Floating-point numbers
Atoms
Ranges
Regular expressions

System types:
PIDs and ports
References

Collection types:
Tuples
Lists
Maps
Binaries

In Elixir, functions are a type too.

String and structures are built using the types above

## Type Safety: type checking

http://learningelixir.joekain.com/elixir-type-safety/


## Integer

Binary, hexdecimal, octal:

```
iex(14)> 0b101
5
iex(15)> 0xaf
175
iex(16)> 0o10
8
```

Sugar, use underscore to improve readability : `1_000_000`

## Float

`1.0   0.2456   0.314159e1 314159.0e-5`

## Truth

* `true`, `:true` is its alias
* `false`, `nil` 
* In most context any value other than `nil` or `false` is treated as `true`  

## Binaries

* Data binary type: to access data as a sequence of bits or bytes
* Litterals are enclosed between `<< >>`
* http://elixir-lang.org/getting-started/binaries-strings-and-char-lists.html

```
iex(8)> bin = << 1, 2 >>
<<1, 2>>
iex(9)> byte_size bin
2
```

You can add modifiers to control the type and size of each individual field:

```
iex> bin = << 1::size(1), 0::size(7) >>
<<128>>
iex(25)> :io.format("~8.2b~n", :binary.bin_to_list(bin))
10000000

iex> bin = << 1::size(1), 1::size(7) >>
<<129>>
iex(23)> :io.format("~8.2b~n", :binary.bin_to_list(bin))
10000001
```

TODO: come funziona la stampa con :io.format ??? è Erlang...
TODO: non ho ben capito come si gestiscono Binaries con più di 8 bit

```
bin = << 1::size(1), 0::size(8) >>
 <<128, 0::size(1)>>
```

## Strings

* By default are encoded in UTF-8
* represented internally by binaries which are sequences of bytes
* [String module doc]( http://elixir-lang.org/docs/stable/elixir/String.html#content )

String interpolation:


```
name="nicola"
"ciao #{name}"
-> "ciao nicola"
```

Print string: `IO.puts "hello\nworld"`


### Binaries, strings and char lists

http://elixir-lang.org/getting-started/binaries-strings-and-char-lists.html

* String byte size and length are different

```
byte_size("hellö") # ö is encoded with 2 bytes
6

byte_size("hello")
5

String.length("hellö")
5

String.length("hello")
5

```


## Atoms

Atoms are constants that represent something’s name. We write them using a leading colon (:)


`:fred  :is_binary?  :var@2  :<>  :===  :"func/3"  :"long john silver"`


Two atoms with the same name will always compare as being equal, even if they were created by different applications on two computers separated by an ocean.

We’ll be using atoms a lot to tag values.

## Ranges

start..end

## RegExp

~r{regexp} or ~r{regexp}opts or ~r/…/

Based on PCRE that provides a Perl-5

http://elixir-lang.org/docs/stable/elixir/Regex.html

## PIDs and Ports

PID is a reference to a local or remote process

`self` is the PID 

## Anonymous functions

Functions are delimited by the keywords `fn` and `end`:

```
add = fn a, b -> a + b end
is_function(add)
iex> is_function(add, 2) # Test function's arity
true
iex> is_function(add, 1)
false
iex> add.(1, 2)
3
```

* Functions are “first class citizens” in Elixir meaning they can be passed as arguments 
* dot (.) between the variable and parenthesis is required to invoke an anonymous function.
* CLOSURE: anonymous functions are closures

```
iex> add_two = fn a -> add.(a, 2) end
 #Function<6.71889879/1 in :erl_eval.expr/5>
iex> add_two.(2)
4
```

* A variable assigned inside a function does not affect its surrounding environment:

```
iex> x = 42
42
iex> (fn -> x = 0 end).()
0
iex> x
42
```

## References

TODO make_ref

## Collections

Elixir collections can hold values of any type (including other collections).

### Best Practices



### Tuples

Ordered collection

`{ 1, 2 }      { :ok, 42, "next"  }   { :error, :enoent }`


CONVENTION: 

* A typical Elixir tuple has two to four elements, any more and you’ll probably want to look at maps, or structs.
* It is common for functions to return a tuple where the first element is the atom :ok. A common idiom is to write matches that assume success

```
iex> { :ok, file } = File.open("Rakefile")
{:ok, #PID<0.39.0>}
iex> { :ok, file } = File.open("non-existent-file")
** (MatchError) no match of right hand side value: {:error, :enoent}
```
The second open failed, and returned a tuple where the first element was :error.

Patter matching:

```
iex> {status, count, action} = {:ok, 42, "next"}
{:ok, 42, "next"}
iex> status  
:ok          
iex> count   
42           
iex> action  
"next"

```

### Lists

`[1,2,3]`

Are like linked list:

* head contains a value
* tails contains the list
* O(1) easy to traverse linearly
* O(n) expensive to access in random order (to get to the nth element, you have to scan through n–1 previous elements)


    “Chapter 7, Lists and Recursion, ”

Excerpt From: Thomas, Dave. “Programming Elixir: Functional |> Concurrent |> Pragmatic |> Fun.” iBooks. 

remove the head is cheap because also if the list is immutable you can return a pointer to the tail structure (which contains the whole data except the head)

```
[ 1, 2, 3 ] ++ [ 4, 5, 6 ]      # concatenation
[1, 2, 3, 4] -- [2, 4]           # difference
1 in [1,2,3,4]                   # membership
true         
iex> "wombat" in [1, 2, 3, 4]
false        
```

#### Keywords List

* Allow more entries for a given key (!= map)


SHORTCUT to generate a list of key value tuples (a KEYWORD LIST):

`[ name: "Dave", city: "Dallas", likes: "Programming" ]`

Elixir converts it into a list of two-value tuples:

`[ {:name, "Dave"}, {:city, "Dallas"}, {:likes, "Programming"} ]`

`DB.save record, [ {:use_transaction, true}, {:logging, "HIGH"} ]` is equivalent to `DB.save record, use_transaction: true, logging: "HIGH"`

{1, fred: 1, dave: 2}



TODO: questo è un po' cervellotico secondo me ....


“We can also leave off the brackets if a keyword list appears as the last item in any context where a list of values is expected.

iex> [1, fred: 1, dave: 2]
[1, {:fred, 1}, {:dave, 2}]
iex> {1, fred: 1, dave: 2}
{1, [fred: 1, dave: 2]}”

in pratica una tuple di 2 elementi dentro una lista viene sempre stampata come una keyword list


### Maps

* Allow only one entry for a given key (!= keyword list)
* Efficient as they grow
* can be used with pattern matching
* use it when you need associative arrays


```
states = %{ "AL" => "Alabama", "WI" => "Wisconsin" }

response_types = %{ { :error, :enoent } => :fatal, { :error, :busy } => :retry }

colors = %{ red: 0xff0000, green: 0x00ff00, blue: 0x0000ff }


```

Accessing:

* If the keys are atoms, you can also use a dot notation: `colors.green`
* `states["AL"]`
* `response_types[{:error,:busy}]`

### Structs

http://elixir-lang.org/getting-started/structs.html

Define a Struct with `defstruct`, with defaults:

```
defmodule User do
  defstruct name: "John", age: 27  # Keyword list defines what fields the struct will have along with their default values.
end
```

without defaults, `nil` will be assumed ad default:

```
defmodule Product do
  defstruct [:name]
end

%Product{}  # %Product{name: nil}
```



To create a User: 

* `%User{}` produces `%User{age: 27, name: "John"}` which takes the default values
* `%User{name: "Meg"}` produces `%User{age: 27, name: "Meg"}`, age field is still the default value

To access a User:

```
john = %User{}
john.name

```

To create a new User from existing one ():

```
john = %User{}                    # %User{age: 27, name: "John"}
laura = %{john|name: "laura"}     # %User{age: 27, name: "laura"}  NOTE: john don't change value
```


Structs VS maps:

* structs are bare maps with a fixed set of fields.
* bare means that none of the protocols implemented for maps are available for structs.For example, you can neither enumerate nor access a struct:

```
iex> john = %User{}
%User{age: 27, name: "John"}
iex> john[:name]
** (UndefinedFunctionError) function User.fetch/2 is undefined (User does not implement the Access behaviour)
             User.fetch(%User{age: 27, name: "John"}, :name)
iex> Enum.each john, fn({field, value}) -> IO.puts(value) end
** (Protocol.UndefinedError) protocol Enumerable not implemented for %User{age: 27, name: "John"}
```

But you can use all the function of the [Map Module](https://hexdocs.pm/elixir/Map.html)

```
iex> kurt = Map.put(%User{}, :name, "Kurt")
%User{age: 27, name: "Kurt"}
iex> Map.merge(kurt, %User{name: "Takashi"})
%User{age: 27, name: "Takashi"}
iex> Map.keys(john)
[:__struct__, :age, :name]
```

* As maps, structs store a “special” field named `__struct__` that holds the name of the struct
* Structs provide compile-time guarantees that only the fields (and all of them) defined through defstruct will be allowed to exist in a struct


#### Required Keys

You can also enforce that certain keys have to be specified when creating the struct:

```
defmodule Car do
  @enforce_keys [:make]
  defstruct [:model, :make]
end

iex> %Car{}
** (ArgumentError) the following keys must also be given when building struct Car: [:make]
    expanding struct: Car.__struct__/1
```

#### Derive

Ref: http://elixir-lang.org/blog/2014/06/17/elixir-v0-14-0-released/

In many situation we want to implement some protocol like `Enumerable` for a struct.

`@derive` allows us to dynamically derive implementations for structs based on the implementation for maps.

```
defmodule User do
  @derive [Enumerable]
  defstruct name: "", age: 0
end

Enum.each %User{name: "jose"}, fn {k, v} ->
  IO.puts "Got #{k}: #{v}"
end
#=> Got __struct__: Elixir.User
#=> Got name: jose
#=> Got age: 0
```

The deriving functionality can be customized by implementing `PROTOCOL.Map.__deriving__/3`. For example, a JSON protocol could define a `JSON.Map.__deriving__/3` function that derives specific implementations for every struct. Such implementations could access the struct fields and generate a JSON template at compilation time, avoiding work at runtime.

### Records

WARNING: Are Records will be DEPRECATED http://elixir-lang.org/blog/2014/04/21/elixir-v0-13-0-released/  "Structs are meant to replace Elixir records. "

Records in Elixir are simply tuples supported by modules which store record metadata


# Protocols

Refs:

* http://culttt.com/2016/06/27/what-are-elixir-protocols/
* http://elixir-lang.org/getting-started/protocols.html

TODO:

* How can we use protocols with our functions?


Polymorphism:

* is “the condition of occurring in several different forms”.
* In programming this means you can usually act on something in a generic way, without knowing specifically what the thing is.
* As long as the thing you are acting on knows how to handle the action, you’re good to go. This is polymorphism because it doesn’t matter what the thing is, as long as it responds correctly.
* EX: you can print something as a string, without knowing what the thing is.

```
to_string("Hello World")
"Hello World"
 
to_string(123)
"123"
 
to_string(99.9)
"99.9"
```

Structs alongside protocols provide one of the most important features for Elixir developers: data polymorphism.

Example:

```
defprotocol Size do
  @doc "Calculates the size (and not the length!) of a data structure"
  def size(data)
end
```


The Size protocol expects a function called size that receives one argument (the data structure we want to know the size of) to be implemented. We can now implement this protocol for the data structures that would have a compliant implementation:

```
defimpl Size, for: BitString do
  def size(string), do: byte_size(string)
end

defimpl Size, for: Map do
  def size(map), do: map_size(map)
end

defimpl Size, for: Tuple do
  def size(tuple), do: tuple_size(tuple)
end
```

We didn’t implement the Size protocol for lists as there is no “size” information precomputed for lists, and the length of a list has to be computed (with length/1).

## Elixir Standard Protocols

TODO: look for examples

Example: https://hexdocs.pm/elixir/Collectable.html#content


# Operators

## Comparison operators

`a === b`    # strict equality   (so 1 === 1.0 is false)
`a !== b`    # strict inequality (so 1 !== 1.0 is true)
`a ==  b`    # value equality    (so 1 ==  1.0 is true)
`a !=  b`    # value inequality  (so 1 !=  1.0 is false)
`a  >  b`    # normal comparison
`a >=  b`    #   :
`a  <  b`    #   :
`a <=  b`    #   :

The ordering comparisons in Elixir are less strict than in many languages, as you can compare values of different types. If the types are the same or are compatible (for example `3 > 2` or `3.0 < 5`), the comparison uses natural ordering. Otherwise comparison is based on type according to this rule:

`number < atom < reference < function < port < pid < tuple < map < list < binary`

## Boolean operators

(These operators expect true or false as their first argument.)

`a or  b`    # true if a is true, otherwise b
`a and b`    # false if a is false, otherwise b
`not a`      # false if a is true, true otherwise


## Relaxed Boolean operators

These operators take arguments of any type. Any value apart from nil or false is interpreted as true.

`a || b`  a if a is truthy, otherwise b
`a && b`  b if a is truthy, otherwise a
`!a`      false if a is truthy, otherwise true

## Arithmetic operators

`+     -    *    /  div rem`


Integer division yields a floating-point result. Use `div(a,b)` to get an integer result.


* `rem` is the remainder operator. It is called as a function `(rem(11, 3) => 2)`. It differs from normal modulo operations in that the result will have the same sign as the function’s first argument.



## Join operators

* `binary1 <> binary2` concatenates two binaries (later we'll see that binaries include strings)
* `list1   ++ list2`   concatenates two lists
* `list1   -- list2`   returns elements in list1 not in list2

## The in operator

`a in enum` tests if a is included in enum (for example, a list or a range)

## The pipe operator

Refs:

* http://culttt.com/2016/04/25/using-pipe-operator-elixir/
* https://elixirschool.com/lessons/basics/pipe-operator/

The Pipe operator makes easy to combine functions.

In functional languages, you will often want to combine functions by passing the result of one function as the argument to the next.

The pipe operator `|>` passes the result of an expression as the first parameter of another expression.

Example:

* `foo(bar(baz(new_function(other_function()))))` is quite messy
* `other_function() |> new_function() |> baz() |> bar() |> foo()` has the same meaning but much more readable

If you have more than one parameters, for example the `String.ends_with?(string, suffixes)` function, this syntax are equivalent:

```
"elixir" |> String.ends_with?("ixir")

String.ends_with?("Elixir","ixir")
```


# Function, Modules and Pattern matching

Ref:

* https://github.com/doomspork/elixir-school/blob/master/lessons/basics/functions.md
* http://learningelixir.joekain.com/use-import-require-in-elixir/

## Modules

Ref:

* Intro: http://elixir-lang.org/getting-started/modules.html
* Doc: http://elixir-lang.org/docs/stable/elixir/Module.html
* http://culttt.com/2016/04/18/working-functions-modules-elixir/


A module is a way of organizing a collection of functions into a namespace. A module basically acts as a namespace.

```
defmodule Calculator do
  def sum(a, b) do
    a+b
  end
end
```

`defmodule` create a module

To define functions within a module: 
* `def` definine a function
* `defp` definine a private function

iex calculator.ex

### Nested modules

It is possible to nest modules in Elixir, allowing you to further namespace your functionality:


```
defmodule Calculator.Addition do
  def sum(a, b) do
    a+b
  end
end
```

or 

```
defmodule Calculator do
  defmodule Addition do
    def sum(a, b) do
      a+b
    end
  end
end
```

```
defmodule Example.Greetings do
  def morning(name) do
    "Good morning #{name}."
  end

  def evening(name) do
    "Good night #{name}."
  end
end

iex> Example.Greetings.morning "Sean"
"Good morning Sean."
```



### Private Module Functions

* Function defined with `defp` can be invoked only from a function of the module
* When we don't want other modules accessing a specific function we can make the function private.
* Private functions can only be called from within their own Module
* Error if you call a private func: `UndefinedFunctionError`

```
defmodule Math do
  def sum(a, b) do
    do_sum(a, b)
  end

  defp do_sum(a, b) do
    a + b
  end
end

IO.puts Math.sum(1, 2)    #=> 3
IO.puts Math.do_sum(1, 2) #=> ** (UndefinedFunctionError)
```


```
defmodule Greeting do
  def hello_public
    hello_private
  end

  defp hello_private
    IO.puts "Hello from a private function"
  end
end

iex(1)> Greeting.hello_public
Hello from a private function
:ok

iex(2)> Greeting.hello_private
** (UndefinedFunctionError) function Greeting.hello_private/0 is undefined or private
    Greeting.hello_private()

```

### Import and Alias Modules

Ref:

* http://elixir-lang.org/getting-started/alias-require-and-import.html#import
* https://hexdocs.pm/elixir/Kernel.SpecialForms.html#import/2

Use `import` to avoid prefixing the module 

```
IO.puts "Hello"
puts  #  ** (CompileError) iex:1: undefined function puts/0
import IO
puts "hello"
```

Import only selected functions:

* https://hexdocs.pm/elixir/Kernel.SpecialForms.html#import/2-selector
* `import List, only: [duplicate: 2]` : import only duplicate/2 (with arity 2) function from the List module
* `import List, only: :functions`
* `import List, only: :macros`
* `import List, except: [flatten: 1]` 

Alias a module to add an alternative module name:

```
IO.puts "Hello"
alias IO, as: Say
Say.puts "Hello"

```

```
defmodule UseImportRequire do
  alias UseImportRequire.AliasMe
  alias UseImportRequire.AliasMe, as: AnotherName

  def alias_test do
    AliasMe.my_function
  end

  def alias_as_test do
     AnotherName.my_function
  end
end
```

* I would recommend using import sparingly. It removes a lot of information which can be a burden for any reader of your code.
* However, there are a few cases where import is helpful. If you are writing a module that is very focused in that it makes heavy use of a specific module then import may make sense.
* One common example is that in a module that makes extensive use of Ecto queries it is common to import Ecto.Query.


The import macro also allows importing of specific functions or macros. This limits “namespace pollution” and can reduce the chance of ambiguity or confusion. Again, this is common with Ecto.Query - the documentation recommends:

```
import Ecto.Query, only: [from: 2]
```

in order to import only the Ecto.Query.from/2 macro.

#### Restrict alias and import Scope

As I’ve mentioned there are tradeoffs for using alias and import between convenience and clarity. There is another way to help mitigate this tradeoff. The alias and import macros don’t need to be called at the outer module scope as we have been using them. They can, for example, be called from within another function. Here’s an example using import:

``` 
defmodule UseImportRequire.WithScope do
  def scope_test do
    import UseImportRequire.ReferenceMe
    function
  end
end
```


### "use" a module

* http://www.zohaib.me/use-in-elixir-explained/
* [Elixir Doc](https://hexdocs.pm/elixir/Kernel.html#use/2)

With `use` developers can inject code into your module. When calling:

```
use MyModule, some: :options
```

the `__using__/1` macro from the MyModule module is invoked with the second argument passed to use as its argument and the module is required. Since __using__/1 is a macro, all the usual macro rules apply, and its return value should be quoted code that is then inserted where use/2 is called.

Behind the scenes, `use` allow the module to inject some code into the current context. Generally speaking, the following module:

```
defmodule Example do
  use Feature, option: :value
end
```

is compiled into

```
defmodule Example do
  require Feature
  Feature.__using__(option: :value)
end
```

Here’s an example:

```
# lib/use_import_require/use_me.ex
defmodule UseImportRequire.UseMe do
  defmacro __using__(_) do
    quote do
      def use_test do
        IO.puts "Use test!"
      end
    end
  end
end
```

and we add this line to UseImportRequire:

```
defmodule TestLibrary do  
  use UseImportRequire.UseMe
end

iex(1)> TestLibrary.use_test  
Use test!  
:ok
```


Using `UseImportRequire.UseMe` defines a `use_test/0` function through invocation of the `__using__/1` macro.


Here we have defined a module in which under __using__ macro we inject a function.

It is common for the `__using__` macro to in turn call alias, require, or import. This in turn will create aliases or imports in the using module. This allows the module being used to define a policy for how its functions and macros should be referenced. This can be quite flexible in that `__using__/1` may set up references to other modules, especially submodules.

The Phoenix framework makes use of use and `__using__/1` to cut down on the need for repetitive alias and import calls in user defined modules.

Here’s an nice and short example from the Ecto.Migration module:

```
defmacro __using__(_) do
  quote location: :keep do
    import Ecto.Migration
    @disable_ddl_transaction false
    @before_compile Ecto.Migration
  end
end
```

The `Ecto.Migration.__using__/1` macro includes an import call so that if use `Ecto.Migration` you also `import Ecto.migration`. It also sets up a module property which I assume control Ecto’s behavior.

To recap: the use macro just invokes the `__using__/1` macro of the specified module. To really understand what that does you need to read the `__using__/1` macro.


### use VS import VS require

Ref: http://stackoverflow.com/questions/28491306/elixir-use-vs-import

* `import Module` brings all the Functions and Macros of Module un-namespaced into your module.

* `require Module` allows you to use macros of Module but does not import them. (Functions of Module are always available namespaced.)

* `use Module` first requires module and then calls the __using__ macro on Module.


Examples:

* Phoenix framework make heavy use of `use`, Crish also wrote a book about it https://pragprog.com/book/cmelixir/metaprogramming-elixir
* Exprotobuf make heavy use of `use` https://github.com/bitwalker/exprotobuf

#### Ecto Example

Here’s a really nice example of using import:

```
defmodule Orthrus.Repo.Migrations.CreateUser do
  use Ecto.Migration

  def change do
    create table(:users) do
      add :name, :string
      add :username, :string
      add :password_hash, :string
      add :email, :string

      timestamps
    end

  end
end
```

The use `Ecto.Migration` call invokes `Ecto.Migration.__using__/1`. And we saw above that this macro in turn calls `import Ecto.Migration`. The import allows us to write very clean code in the migration. We can call create, add, timestamps without needing to clutter up the code with an Ecto.Migration prefix.

For migrations, this is a good tradeoff a migration is narrowly focused task. When you read these references to create table, and add you are in the mindset of thinking about database migrations so this code makes sense.

If you have other tasks that are not as focused you may want to ask yourself if import is the right choice.


### Require a module

The require macro instructs the compiler to load the specified module before compiling the containing module.

This is only necessary if you want to reference macros from the specified module

## Pattern Matching

* http://elixir-lang.org/getting-started/pattern-matching.html
* https://elixirschool.com/lessons/basics/pattern-matching/
* https://medium.com/@turnandface/pattern-matching-in-elixir-743e71ceac92#.fyyf62wg7
* http://stackoverflow.com/questions/23693173/elixir-pattern-matching-works-differently-for-tuples-and-maps

`=` operator is actually a match operator.

### Pattern Matching Tuples

```
> {a, b, c} = {:hello, “world”, 42}
{:hello, “world”, 42}
> a
:hello
> b
“world”
> c
42
```


Here the right-hand side of the match operator, =, is a tuple. It has three elements, an atom, a string and an integer. Ok so far.
Now, in order to make the left-hand side equal to the right we’d need to have a three element tuple on the left with with either identical values or ‘placeholders’, variables that can be assigned. Elixir does this by assigning the variables a, b & c into them. We have a match!


In contrast to this, if the tuples have a different number of element there is an error:

```
{a, b} = {:hello, “world”, 42}
** (MatchError) no match of right hand side value: {:hello, “world”, 42}
```

In this case, you can pass an underscore on the left-hand side and Elixir will immediately discard the value it matches, while still allowing the match to take place.

```
> {a, b, _} = {:hello, “world”, 42}
{:hello, “world”, 42}
```

``` 
iex(6)> {_,a} = {1,2}
{1, 2}
iex(7)> a
2
```

`_` is the "catch-all" pattern but you need to provide it for all elements of the tuple:


```
iex(8)> {_,b} = {1,2,3}
** (MatchError) no match of right hand side value: {1, 2, 3}

iex(8)> {_, b, _} = {1,2,3}
{1, 2, 3}
iex(9)> b
2
```

Taking this one step further, let’s change up the example slightly.

```
> {:hello, b, c} = {:hello, “world”, 42}
{:hello, “world”, 42}
> b
“world”
> c
42
```

Here, we’ve hard-coded the first element of the left-hand tuple to :hello. The pattern matching remains the same, can it make the left equal to the right? Here it can, and two variables are created, b and c. This was the start of my understanding of why pattern matching exists.


### Pattern Matching Lists

```
[a, b, _] = [1, 2, 3]
```

or using the `|`:

``` 
[h|t] = [1, 2, 3]

iex(11)> h
1

iex(12)> t
[2, 3]

```

### Pattern Matching Maps

When matching maps though, you can match on one or more keys in the map, which gives you thesyntax:

```
%{a: b} = %{a: :foo, b: :bar}


```

The semantics are a bit different between data structures, but are fairly common sense.

The tuple rule exists because two tuples cannot be the same unless they have the same number of elements, a list has the same limitation

Because of the semantics of lists, accessing the head element of the list is the most common operation when working with them, hence the [h|t] syntax.

Maps however can match based on specific keys, so the number of elements are irrelevant, as long as both sides of the match contain the same key, and optional pattern for the value, then it's a successful match.

NOTE: maps are the only data structure that allow partial pattern matching, everything else requires the pattern to match the entire structure.


### Pattern Matching with Structs

Structs can also be used in pattern matching:

* for matching on the value of specific keys

``` 
iex> %User{name: name} = john
%User{age: 27, name: "John"}
iex> name     #We extract the value of the field name
"John"
```

* for ensuring that the matching value is a struct of the same type as the matched value.

```
iex> %User{} = %{}
** (MatchError) no match of right hand side value: %{}
```

### Pattern Matching with functions

Declare three method definitions with the same name and arity:

```
defmodule Chatter do
  def converse({:hello, name, employer}) do
    IO.puts “Hi #{name}. Nice to meet you. I hear you work for #{employer}.”
  end
  
  def converse({:small_talk, name, fav_hobby}) do
    IO.puts “Hey #{name}, have you been doing much #{fav_hobby} lately?”
  end
  
  def converse({:goodbye, name}) do
    IO.puts “#{name}, great to talk to you today, goodbye.”
  end
end
```
I can call the converse/1 function thus, the tuple will be passed to the converse/1 function in our Chatter module:

```
> Chatter.converse({:hello, “Stephanie”, “World Bank”})
# Hi Stephanie. Nice to meet you. I hear you work for World Bank.
> Chatter.converse({:hello, “Trevor”, “Local Bank”})
# Hi Trevor. Nice to meet you. I hear you work for Local Bank.
> Chatter.converse({:small_talk, “Stephanie”, “fishing”})
# Hey Stephanie, have you been doing much fishing lately?
> Chatter.converse({:goodbye, “Trevor”})
# Trevor, it was great to talk to you today, goodbye.
```

you can see we have allowed for three different types of conversation without any conditionals in our code. Each of the method signatures clearly show their intent through the first element of the tuple. Our code is simplified.





#### Assign variables in the function definition:  Phoenix controller example

 When I first used Phoenix I saw something I found confusing in some method signatures. Here’s an example from the show action of a controller.
 
Here’s an example from the show action of a controller:

```
def show(conn, %{“user_id” => user_id} = params) do
  # … show stuff here using variables user_id and params
end
```

Hmmm. This `show/2` function takes two parameters, but, in the signature there appears to be some pattern matching going on, this really confused me.

The explanation is quite simple. Elixir is pattern matching params first (the passed in map is the right-hand side, params becomes the left), then pattern matches user_id, as the left-hand side, against params which is now the right-hand side, like so.

```
%{“user_id” => user_id} = params = <map passed in>
# breaks down to
params = <map passed in>
# then to
%{“user_id” => user_id} = params
```

As a result of this you have access to the full params map, and a separate user_id in the function body. This is another example of decomposition.

##### Assign variables in the function definition: 

https://medium.com/rebirth-delivery/how-to-use-elixir-pattern-matched-functions-arguments-a793733acc6d#.c0l26oy4d

#### Pattern Matching and default parameters

http://stackoverflow.com/questions/38820327/pattern-matching-and-default-parameters


#### The case operator

```
# my_case.exs
defmodule MyCase do

  def do_something(tuple) do
    case tuple do
      {:ok, value} -> "The status was :ok!"
      {:nope, value}  - > "Nope nope nope nope..."
      _ -> "You passed in something else."
    end
  end

end
```

Then load up the file in iex by running `$ iex my_case.exs.`

```
iex> MyCase.do_something({:ok, true})
"The status was :ok!"
iex> MyCase.do_something({:nope, true})
"Nope nope nope nope..."
iex> MyCase.do_something({:wat, true})
"You passed in something else."
```


### The pin operator ^

```

```


## Guards and multiple clauses

* [Elixir Guard Doc on HEX](https://hexdocs.pm/elixir/guards.html#content)
* Use pattern matching
* support both do: and do/end block syntax

```
defmodule Math do
  def zero?(0) do
    true
  end

  def zero?(x) when is_integer(x) do
    false
  end
end

IO.puts Math.zero?(0)         #=> true
IO.puts Math.zero?(1)         #=> false
IO.puts Math.zero?([1, 2, 3]) #=> ** (FunctionClauseError)
IO.puts Math.zero?(0.0)       #=> ** (FunctionClauseError) 
```

```
defmodule Math do
  def zero?(0), do: true
  def zero?(x) when is_integer(x), do: false
end
```

## One line function definition

To make small function much more readable you can use this compact syntax:

```
defmodule Calculator do
  def sum(a, b), do: a + b 
end
```

## Function Capturing - & operator

```
iex> Math.zero?(0)
true
iex> fun = &Math.zero?/1
&Math.zero?/1
iex> is_function(fun)
true
iex> fun.(0)
true
```

If you want to capture a function from a module, you can do &Module.function():

```
iex> fun = &List.flatten(&1, &2)
&List.flatten/2
iex> fun.([1, [[2], 3]], [4, 5])
[1, 2, 3, 4, 5]
```


## & shortcut for creating functions

Shorthand to create anonymous functions

```
iex> sum = &(&1 + &2)
iex> sum.(2, 3)
5
```

Parameters are available to us as &1, &2, &3, and so on

## Closures

ref: http://joearms.github.io/2013/05/31/a-week-with-elixir.html

Closures in Elixir (fn's) are really just closures in Erlang (fun's).

`fn` capture the present value of any variables that are in their scope (ie we can create immutable closures). This is something that JavaScript gets very wrong.

Here's an example in JavaScript and Elixir so you can see the difference:

```
js> a = 5;
5
js> f = function(x) { return x+a }; 
function (x){return x+a}
js> f(10)
15
js> a = 100
100
js> f(10)
110
```

We broke the function f:

* We define a function f,
* start using it.
* Redefine a and this has the side effect of breaking f.

One of the good things about functional programming is that it makes it easy to reason about programs. If f(10) evaluates to 15 then it should evaluate to 15 forever, you should not be able to remotely break it.

What about Elixir? This gets closures right:

```
iex> a = 5  
5
iex> f = fn(x) -> x + a end
#Function
iex> f.(10)
15
iex> a = 100
100
iex> f.(10)
15
```

* Proper closures should only contain pointers into immutable data (which is the case in Erlang) - no pointers into mutable data.
* If a closure contains a pointer into mutable data and you change the data later you break the closure. This means you can't parallelize your program and even sequential code can contain weird errors.


* In a conventional language creating proper closures would be very expensive since it would require deep copying of all the variables that are captured in the environment, but this is not the case in Erlang or Elixir, since data once written is immutable. All you can do later is refer to it.
* Internally this is through a pointer (which the programmer never sees) and the garbage collector removes all data that can never be referenced since nothing points to it.

## Compilation

* `elixirc math.ex` generate `Elixir.Math.beam`
*  

## def VS fn

* http://stackoverflow.com/questions/18011784/why-are-there-two-kinds-of-functions-in-elixir

## With

* Elxir DOC: https://hexdocs.pm/elixir/Kernel.SpecialForms.html#with/1
* http://learningelixir.joekain.com/learning-elixir-with/
* http://elixir-lang.org/getting-started/mix-otp/docs-tests-and-with.html#with

The pipe operator is great when all functions are acting on a consistent piece of data. It falls apart when we introduce variability.

That's where `with` comes in. with is a lot like a |> except that it allows you to match each intermediary result. It allows developers to match on multiple expressions concisely

Previously, one would write

```
case File.read("my_file.ex") do
  {:ok, contents} ->
    case Code.eval_string(contents) do
      {res, _binding} ->
        {:ok, res}
      error ->
        error
  error -> error
    error
end
```

such can now be rewritten as

```
with {:ok, contents} <- File.read("my_file.ex"),
     {res, binding} <- Code.eval_string(contents),
     do: {:ok, res}
```

with will match each left side of `<-` against the right side, executing expressions until one of those match fails or until the do: expression is performed.

In case a match fails, the non-matching result is returned. An `else` option can be given to modify what is being returned from with in the case of a failed match:

* use left arrow
* can have multiple pattern matching clauses
* use-case: you want to return an uniform return value for all the errors that can happen in your chain

If there is no matching else condition, then a `WithClauseError` exception is raised.

```
with ... <- ... ,
    ... <- ... ,
    ... <- ... ,
    ... <- ... do 
  {:ok, double_width * height}
else
  :error -> {:error, :wrong_data}
  :error2 -> {:error, :nil_data}
end
```


NOTE that:

* non andare a capo con il `do` quando si usa `else`
* “bare expressions” may also be inserted between the clauses
* Guards can be used in patterns
* variables bound inside with/1 won’t leak;

Example:

```
width = nil
opts = %{width: 10, height: 15}
with {:ok, width} <- Map.fetch(opts, :width),
    double_width = width * 2,
    {:ok, height} <- Map.fetch(opts, :height),
    do: {:ok, double_width * height}

{:ok, 300}




width = nil
opts = %{width: 10}
with {:ok, width} <- Map.fetch(opts, :width),
    double_width = width * 2,
    {:ok, height} <- Map.fetch(opts, :height),
    do: {:ok, double_width * height}

:error





width = nil
opts = %{width: 10}
a = with {:ok, width} <- Map.fetch(opts, :width),
    double_width = width * 2,
    {:ok, height} <- Map.fetch(opts, :height) do
  {:ok, double_width * height}
else
  :error -> {:error, :wrong_data}
end

{:error, :wrong_data}
```



Refactor example: http://openmymind.net/Elixirs-With-Statement/

### Happy With


If you want to be more specific in the way you handle errors and you cannot obtain it with patter matching use `happy_with` and `tags`:

* https://github.com/vic/happy_with
* https://github.com/vic/happy/blob/master/README.md#tags


# Elixir Macros

* TODO http://elixir-lang.org/getting-started/meta/macros.html
* http://slides.com/chrismccord/elixir-macros#/14

Warning about macros: Remember that explicit is better than implicit. Clear code is better than concise code.

MACRO RULE #1 : DON'T WRITE MACROS

MACRO RULE #2 : USE MACROS GRATUITOUSLY

What is a macro:

* Code that writes code
* Elixir itself is primarily built with macros (if, unless, cond, def, defmodule)
* Full access to Elixir at compile time

`quote `Returns the representation of any expression (AST)

* AST is represented as a series of three element tuples
* The first element is always an atom or another tuple
* The second element represents metadata
* The third element is the arguments for the function call


```
iex> quote do: div(10, 2)
{:div, [], [10, 2]} 
```

```
iex> add = fn a, b -> a + b end 

iex> quote do: add.(1, 2)
{
  {:., [], [{:add, [], Elixir}]}, 
  [],
  [1, 2]
}
```




ASSERT MACRO



## Macro use-cases

* Eliminating boilerplate
* Advanced compile time code generation
* Domain Specific Languages (DSLs)


# Deployment production Monitoring




# OTP

## Supervisor

TODO: https://jbodah.github.io/blog/2016/11/18/supervisors-work/

# Applications and use cases

Elixir and big data: https://elixirforum.com/t/big-data-with-elixir/154/2

Leveraging Elixir to access HDFS-like and inter-operate to Python for the map-reduce or machine-learning, and back again to Elixir for the database and Web inter-operability. This can be done by using protobuffer or a common swap space. 
Again, one of the weakness of the software you mentioned is of being monolithic and to enforce the use of certain tools (above all Java).


# Code Snippet

## Iterate over an Enumerable ()

```
Enum.each %{foo: :bar}, fn {k, v} ->
  IO.puts "Got #{k}: #{v}"
end
```



# Common Liraries

# Recipes

https://elixir-examples.github.io/
