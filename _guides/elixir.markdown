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

# People and companies

* José Valim, Founder and Director of Research and Development at Plataformatec
  * https://www.linkedin.com/in/jovalim
* 

# Atom Elixir

https://brainlid.org/elixir/2015/11/12/atom-editor-and-elixir.html


# CHEATSHEET

* Help from iex: `h String`
* Cheatsheet: https://media.pragprog.com/titles/elixir/ElixirCheat.pdf
* Start a script: `iex math.exs`

# Install Elixir

Docker Example:

* Erlang image: https://github.com/c0b/docker-erlang-otp/blob/ea32d5f6f1735f9f55bee04b112166da96eb9c73/19/Dockerfile
* Elixir image: https://github.com/c0b/docker-elixir/blob/22ee98417200ef8d9a049b2b4504e7cf279e911f/1.2/Dockerfile

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

* A typical Elixir tuple has two to four elements—any more and you’ll probably want to look at maps,, or structs,.
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

The ordering comparisons in Elixir are less strict than in many languages, as you can compare values of different types. If the types are the same or are compatible (for example 3 > 2 or 3.0 < 5), the comparison uses natural ordering. Otherwise comparison is based on type according to this rule:

number < atom < reference < function < port < pid < tuple < map < list < binary

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

# Pattern Matching

* http://elixir-lang.org/getting-started/pattern-matching.html
* https://elixirschool.com/lessons/basics/pattern-matching/

`=` operator is actually a match operator.

## The pin operator ^

```

```

# Function Modules Pattern matching

Ref:

* Intro: http://elixir-lang.org/getting-started/modules.html
* Doc: http://elixir-lang.org/docs/stable/elixir/Module.html
* https://github.com/doomspork/elixir-school/blob/master/lessons/basics/functions.md

* `defmodule` create a module
* `def` definine a function
* `defp` definine a private function


Why ?

* grouping functions ( they allow us to define named and private functions )

Let’s look at a basic example:

```
defmodule Example do
  def greeting(name) do
    "Hello #{name}."
  end
end

iex> Example.greeting "Sean"
"Hello Sean."
```

It is possible to nest modules in Elixir, allowing you to further namespace your functionality:

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

## Private Functions

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

## Functions and pattern matching



## Guards and multiple clauses

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



# Mix

Ref:

* into: http://elixir-lang.org/getting-started/mix-otp/introduction-to-mix.html
* Mix doc: http://elixir-lang.org/docs/stable/mix/Mix.html

A build tool that ships with Elixir that provides tasks for

* creating,
* compiling,
* testing your application,
* managing its dependencies and much more;

TODO:

* archive.install
* nerves.new
* deps.get
* compile
* firmware

## Project Structure


* ebin - contains the compiled bytecode
* lib - contains elixir code (usually .ex files)
* test - contains tests (usually .exs files)



# Applications and use cases

Elixir and big data: https://elixirforum.com/t/big-data-with-elixir/154/2

Leveraging Elixir to access HDFS-like and inter-operate to Python for the map-reduce or machine-learning, and back again to Elixir for the database and Web inter-operability. This can be done by using protobuffer or a common swap space. 
Again, one of the weakness of the software you mentioned is of being monolithic and to enforce the use of certain tools (above all Java). 
