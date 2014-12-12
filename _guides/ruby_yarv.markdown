---
layout: post
title: "YARV"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["ruby"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# References

* [Ruby under a microscope](/Volumes/ArchiveDisk/Archive/Misc/ebook/ruby/RubyUnderaMicroscope.pdf)
  * user **ruby 2.0**
* [RubyVM class doc](http://www.ruby-doc.org/core-2.1.5/RubyVM.html)
* [YARV: Yet Another RubyVM by Koichi Sasada](http://www.atdot.net/yarv/oopsla2005eabstract-rc1.pdf)
* [Interview to Matz and Koichi abount the merge of YARV into the ruby trunk](https://archive.today/yCFB)
  * http://graysoftinc.com/the-ruby-vm-interview/the-ruby-vm-episode-iii
  * thread implementation http://graysoftinc.com/the-ruby-vm-interview/the-ruby-vm-episode-iv
  * optimizations: http://graysoftinc.com/the-ruby-vm-interview/the-ruby-vm-episode-v
* http://patshaughnessy.net/2012/6/29/how-ruby-executes-your-code
* [Misc notes](http://yarvinstructions.herokuapp.com/notes)
* http://rehanjaffer.com/how-to-disassemble-ruby-code-into-rubyvm-yarv-opcodes-instruction-sequences/

# Why YARV

Ruby has following characteristics.

* Simple syntax
* Normal OO features (class, method call, etc.)
* Advanced OO features (all values are objects, Min-in, Sin- gleton method, etc.)
* Dynamic-typing, re-definable behavior, dynamic evaluation
* Operator overloading
* Exception handling
* Closure and method invocation with a block • Garbage collection support
* Dynamic module loading
* Many useful libraries
* Highly portable

Old Ruby intepreters was slow (< 1.9x). This is because old-ruby works by traversing abstract syntax tree and evaluates each node.

To solve this problem YARV (Yet Another RubyVM) was developed. YARV is a stack machine and runs Ruby programs in compiled intemediate representation of sequential instructions.


# Overview

YARV is a simple stack machine written in C. YARV compiles a Ruby script
into YARV instruction (intermediate) code sequences ( `ISEQ` ). The instruction set
is designed for Ruby specifically. 

## YARV Stacks

* YARV is a **double-stack** machine:
  * YARV uses a stack internally to track intermediate values, arguments, and return values
  * YARV keeps track of your Ruby program’s call stack, recording which methods call which other methods, functions, blocks, lambdas, and so on

YARV maintains a stack of `rb_control_frame_t` that represents the path
that YARV has taken through your Ruby program. In other words, this is
your `Ruby call stack`.

YARV use `CFP (Control Frame Pointer)` to maintain a reference to the
top of the ruby stack.

![yarv_stack_of_rb_control_frames]({{ site.url }}/guides/images/yarv_stack_of_rb_control_frames.jpg)

{% github_sample_ref /ruby/ruby/blob/v2_2_0_preview2/vm_core.h %}
{% highlight c %}
{% github_sample /ruby/ruby/blob/v2_2_0_preview2/vm_core.h 516 532 %}
{% endhighlight %}

Each `rb_control_frame_t` has a set of pointer:

  * `PC (Program Counter)` denotes the position of the instruction being executed
  * `SP (Stack Pointer)`  denotes stack top
  * `ISEQ`
  * `BLOCK_ISEQ`
  * `EP (Environment pointer)` points to where the local variables for the current method are located on the stack.


The `rb_control_frame_t` allow YARV to keep track of the status of a
`YARV internal stack`, one for each entry in the ruby call stack. The
YARV internal stack is used to evaluate a snippet of YARV bytecode. Each YARV
instruction uses this stack to read inputs and store results.

For example the `opt_plus` YARV instruction that result from the compilation
of the `2+2` ruby code:

* sum the first two elements of the stack as input arguments
* remove those two elements from the stack
* push the resul on the top of the stack

![yarv_double_stack]({{ site.url }}/guides/images/yarv_double_stack.jpg)

CH3 of Ruby undere a microscope go though the compilation and execution
of this two ruby codes (step by step evolution of the two stacks):

~~~ruby
2+2
~~~

~~~ruby
10.times do
  puts "The quick brown fox jumps over the lazy dog."
end
~~~



## YARV variable and ruby variables

REF: See Ruby under a microscope ch2 and ch3

### Local Table

REFs:

* See Ruby under a microscope ch2
* https://ruby-hacking-guide.github.io/module.html

The execution of Ruby is also basically nothing but chained calls of
methods which are procedures, it works like a C program. Things being
accessed such as local variable scope and the block local scope will
be changing. And these kind of scopes are expressed by stacks.

Each NODE_SCOPE element in the AST contains information labeled table and args.
YARV copies these informations into a `local table` saved with the code
snippet.

Each snippet of YARV instructions, each scope in your Ruby program, has its own local table.
The `local table` contains the snippet local variables and the method or
block arguments. Pay attention that the local scope of a method call is
influenced also by the class to which the method belongs.

In the example below the local table is: `[ 2] n<Arg>`

~~~ruby
code = <<END
   10.times do |n|
     puts n
   end
END
puts RubyVM::InstructionSequence.compile(code).disasm
~~~

~~~
== disasm: <RubyVM::InstructionSequence:<compiled>@<compiled>>==========
== catch table
| catch type: break  st: 0002 ed: 0006 sp: 0000 cont: 0006
|------------------------------------------------------------------------
0000 trace            1                                               (   1)
0002 putobject        10
0004 send             <callinfo!mid:times, argc:0, block:block in <compiled>>
0006 leave
== disasm: <RubyVM::InstructionSequence:block in <compiled>@<compiled>>=
== catch table
| catch type: redo   st: 0000 ed: 0009 sp: 0000 cont: 0000
| catch type: next   st: 0000 ed: 0009 sp: 0000 cont: 0009
|------------------------------------------------------------------------
local table (size: 2, argc: 1 [opts: 0, rest: -1, post: 0, block: -1, keyword: 0@3] s3)
[ 2] n<Arg>
0000 trace            256                                             (   1)
0002 trace            1                                               (   2)
0004 putself
0005 getlocal_OP__WC__0 2
0007 opt_send_simple  <callinfo!mid:puts, argc:1, FCALL|ARGS_SKIP>
0009 trace            512                                             (   3)
0011 leave
~~~

Each entry in the local table has a type:

* `<Arg>` A standard method or block argument
* `<Rest>`  An array of unnamed arguments that are passed together using a splat (*) operator
* `<Post>` A standard argument that appears after the splat array <Block> A Ruby proc object that is passed using the & operator
* `<Opt=i>` A parameter defined with a default value. The integer value i is an index into a table that stores the actual default value. This table is stored along with the YARV snippet but not in the local table itself.
* if no type is spefified its a local variable

![ruby_yarv_local_table.jpg]({{ site.url }}/guides/images/ruby_yarv_local_table.jpg)

The local table only describe which local variable a YARV snippet needs.
The next paragraph describe where the interprester stores thos
variables.

### Local and Dynamic Access of Ruby Variables

REFS:

* REF: See Ruby under a microscope ch3

In this two examples the `str` variable is a local variable or a method
argument:

~~~ruby
def display_string
  str = "Local access."
  puts str
end
~~~

~~~ruby
def display_string(str)
  puts str
end
~~~

Both cases are managed in the same way by ruby:

* The YARV reads the `local table` of the ISEQ to define and allocate an area on the internal stack to store args and local variables
* `EP (Environment pointer)` points to where the local variables for the current method are located on the stack.
* `setlocal <offset>`: the offset from the ep pointer used to find the variable location. It will copy the top of the stack into the variable.
* `getlocal <offset>`: the offset from the ep pointer used to find the variable location. It will push the value of the variable onto the top of the stack.

Instread when we have blocks arguments ruby may need to access also to
local variable of parent scopes: let’s see how dynamic variable access works and what that special
value is. Ruby uses dynamic access when you use a variable that’s
defined in a different scope. For example, when you write a block that references values in the surrounding code.

~~~ruby
def display_string
  str = "Dynamic access."
  10.times do
    puts str
  end
end
~~~

When ruby call the `times` method and detect that it has a block argument:

* it saves a pointer to a new `rb_block_t` structure as the special value in the new stack frame.

![ruby_special_method_with_block_arg.jpg]({{ site.url }}/guides/images/ruby_special_method_with_block_arg.jpg)

Instead when ruby invoke the block it will copy the previous value of the
EP pointer into the `special variable` of the new stack frame.

![ruby_special_call_block.jpg]({{ site.url }}/guides/images/ruby_special_call_block.jpg)

This will give access to parent local variables. The `setlocal` and
`getlocal` instruction accept a second parameter that represent the
number of step that YARV need to go back in the stack to find variable:

~~~ruby
getlocal 2, 1  ### get the second variable of the previous stack frame
~~~

~~~ruby
getlocal 2, 2  ### get the second variable of the second to the last stack frame
~~~

#### svar/cref

Usually, the EP-1 slot in the stack will contain the svar value, which
is a pointer to a table of any special variables defined in this stack
frame.

Ruby provides for this behavior by saving a separate set of special
variables at each level of the stack using the svar value.

**BUT** Ruby considers the top-level and inner-block scope to be the same with regard to special variables.

~~~ruby
str = "The quick brown fox jumped over the lazy dog.\n"
/fox/.match(str)
2.times do
  /dog/.match(str)
  puts "Value of $& inside block: #{$&}"
end
puts "Value of $& in the top-level scope: #{$&}"
~~~

result in:

~~~
Value of $& inside block: dog
Value of $& inside block: dog
Value of $& in the top-level scope: dog
~~~

Ruby has overwritten the value of $& in the top scope with the matching word dog from the search I performed inside the block!
This is similar to how dynamic variable access works; we expect variables inside the block to have the same values as those in the parent scope.

![ruby_cref_for_blocks.jpg]({{ site.url }}/guides/images/ruby_cref_for_blocks.jpg)

Inside the block scope (because there is no need for a separate copy of
the special variables), Ruby takes advantage of the EP-1 open slot and
saves the value cref there instead. Ruby uses the `cref`  value to keep
track of which lexical scope this block belongs to. `Lexical` scope refers
to a section of code within the syntactical structure of your program
and is used by Ruby to look up constant values. (See Chapter 6 of ruby
under a microscope for more on lexical scope.) Specifically, Ruby uses
the cref value here to implement metaprogramming API calls, such as eval
and instance_eval.

## YARV Method calls

REF: See Ruby under a microscope ch4

YARV call Methods in different ways:

* C methods: calling the C function (with some informatino for backtraces)
* Ruby methods: execute the compiled iseq (Instruction SEQuence)

NOTE: each Thread has a stack (allocated from heap).

## Catch Table

A `catch table` is a table of pointers optionally attached to any YARV
code snippet.

# Ruby 2.1 VM

* `vm_exec.c` contains the primary YARV loop that steps through the YARV instruc- tions in your program one after another and calls the C code corresponding to each one.
* `vm.inc` is generated by `tool/insns2vm.rb`, see "YARV instruction". Is a C file included by `vm_exec.c`
* `vm_insnhelper.c` implements some of the helper methods used by YARV instructions like:
  * `vm_search_method`
* `vm.c` 
  * init the VM `Init_VM(void)`
  * `static VALUE vm_exec(rb_thread_t *th)`

# YARV instruction

refs:
* [ruby 1.9.x instructions](http://yarvinstructions.herokuapp.com/)

* VM instructions are defined in `<ruby_repo>/insns.def` and compiled into *.c/*.h by `tool/insns2vm.rb`

## Leave

`leave` is like a return statement. It returns from this scope.

## Send

## Trace

`trace` is the function that YARV uses to support the ruby
[set_trace_func](http://www.ruby-doc.org/core-2.1.1/Kernel.html#method-i-set_trace_func)


## Throws

## Optimized less-than

`opt_lt`: This evaluation leaves either a true or false value on the stack.


# RubyVM Class

Refs:

* [RubyVM::InstructionSequence Class](http://www.ruby-doc.org/core-2.1.5/RubyVM/InstructionSequence.html)
* Ch2 of ruby under a microscope






~~~ruby
code = <<END
10.times do |n|
puts n end
END
puts RubyVM::InstructionSequence.compile(code).disasm
~~~




ruby --dump parsetree ruby_examples/yarv_example1.rb
ruby ruby_examples/yarv_example1_ripper_output.rb







