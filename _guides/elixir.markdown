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

# References

* Help from iex: `h String`
* Cheatsheet: https://media.pragprog.com/titles/elixir/ElixirCheat.pdf


# Are Elixir variables really immutable?

* http://stackoverflow.com/questions/29967086/are-elixir-variables-really-immutable

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

Functions are delimited by the keywords fn and end:

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
* CLOSURE: anonymoud functions are closures

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




### Binaries

http://elixir-lang.org/getting-started/binaries-strings-and-char-lists.html
