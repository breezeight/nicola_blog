# Learning Python

## Document Scope

This document is a collection of resources to learn Python and some learning paths. 

Some of the sections are my personal notes, and some are more generic.

## Free Resources

[Free Python Books](https://github.com/pamoroso/free-python-books):

[Python Roadmap](https://roadmap.sh/python)


## Nicola's Learning Path

In 2024 I started learning Python in a more structured way, and I took notes about it.

I'm using [Python Roadmap](https://roadmap.sh/python) as a guide but I'm not following it 100% because I'm also following other resources.

### Learn the basics

#### Python Basic Syntax
[Python Basic Syntax](https://www.tutorialspoint.com/python/python_basic_syntax.htm)

This article on Python's basic syntax introduces the fundamental rules for writing Python programs. Key points include:

- **Clean and Simple Syntax**: Python's syntax is designed to be clean and simple, with similarities to languages like Perl, C, and Java, yet with distinct differences.
- **First Python Program**: The article guides readers through writing a basic "Hello, World!" program in Python, demonstrating both interactive and script modes.
- **Indentation for Code Blocks**: Python uses indentation to define code blocks, replacing the need for braces {} found in other languages.
- **Comments**: The hash symbol # is used for comments in Python.
- **Importance of Proper Indentation**: Proper indentation is crucial for code readability and structure in Python.

These elements form the foundation of Python programming, emphasizing readability and simplicity.


#### Python Variables
[Python Variables](https://www.tutorialspoint.com/python/python_variables.htm):

- **Definition of Python Variables**: Python variables are reserved memory locations used to store values.
- **Generic introduction to Memory Addresses**: Data is stored in memory locations with specific addresses.
- **Assignment and Labels**: Variables act as labels pointing to objects in memory. Creating Python Variables.
- **Python's `id()` function**: Returns the memory address of an object.
- **Printing Variables**: The `print()` function is used to display variable values.
- **Deleting Variables**: The `del` statement removes references to objects.
- **Getting Variable Types**: The `type()` function returns the data type of a variable.
- **Casting Variables**: Explicit data type conversion can be done using `int()`, `float()`, `str()`, etc.
- **Case-Sensitivity**: Variables are case-sensitive (age and Age are different).
- **Multiple Assignment**: Multiple variables can be assigned the same value or different values in a single statement.
- **Naming Conventions**: Rules for valid variable names, Start with a letter or underscore, Cannot start with a number or special character, Case-sensitive, Cannot use reserved keywords, Naming patterns, Examples of valid and invalid variable names, Using variables in computations, Local variables, Global variables, Constants, Python vs. C/C++ variables, Identity operator (is).
- **Using Variables in Computations**: Variables simplify computations and are useful in scripts and programs.
- **Local vs Global Variables**: Local variables are defined within a function and cannot be accessed outside the function. Global variables are defined outside a function and accessible inside any function.
- **Constants**: Python uses naming conventions (all caps, e.g., PI\_VALUE) to indicate constants. Note: Python's typing system allows you to specify constant types using type hints, but it does not enforce immutability.

#### Expressions and Operators
- Arithmetic Operators
- Comparison Operators
- Logical Operators
- Bitwise Operators
- Assignment Operators
- Membership Operators
- Identity Operators
- Operator Precedence and Associativity
- **Identity Operator** `is`: Checks if two variables refer to the same object.

Nicola's notes: [Expressions and Operators](expressions-and-operators.md)

#### Data Types and Literals

* Nicola's notes: [Data Types and Literals](data-types-and-literals.md)
* Other resource: https://www.tutorialspoint.com/python/python_data_types.htm

#### Control Flow

##### Conditional Statements

The [Real Python article on Python Conditional Statements](https://realpython.com/python-conditional-statements/) covers:
- `if` Statements: Conditional execution based on true expressions.
- Indentation and Blocks: Code grouping defined by indentation.
- `else` and `elif` Clauses: Alternatives and multiple conditions.
- One-Line if Statements - ternary operators: For simple conditions.
- Conditional Expressions: Inline evaluation with ternary operators `s = 'minor' if age < 21 else 'adult'`.
- `pass` Statement: Placeholder for empty blocks.

> [!NOTE] This is a good resource for people who want to learn about conditional statements in general. It explain the general concept of conditional statements and how they work in Python.

[Match Statement in Python](control-flow.md#match-statement): Available from Python 3.10. (NOTE: python does not have a `switch` statement, match statement is the closest thing to it). NOTE: A beginner does not need to learn all the advanced pattern matching, but it's good to know it exists in the language.


##### Loops

* [For Loops](for-while-iterables.md#for-loops)
* [While Loops](for-while-iterables.md#while-loops)
* [Iterables](for-while-iterables.md#iterables)


Additional resources:
-   [articleLoops in Python](https://www.geeksforgeeks.org/loops-in-python/)
-   [articlePython "while" Loops (Indefinite Iteration)](https://realpython.com/python-while-loop/)
-   [articlePython "for" Loops (Definite Iteration)](https://realpython.com/python-for-loop/#the-guts-of-the-python-for-loop)
-   [videoPython For Loops](https://www.youtube.com/watch?v=KWgYha0clzw)

#### Type Casting

* Nicola's notes: [Type Casting](type-casting.md)

#### Exception Handling

* Nicola's notes: [Exception Handling](exception-handling-and-with.md)

#### Functions

* Nicola's notes: [Functions](functions.md):

### Modules and Packages

* Nicola's notes: [Modules and Packages](modules-and-packages.md)


### Python Packaging Process and Package Managers

* Nicola's notes: [Python Packaging Explanation](python-packaging-explanation.md)

Package managers allow you to manage the dependencies (external code written by you or someone else) that your project needs to work correctly.

`PyPI` and `Pip` are the most common contenders but there are some other options available as well:

* [UV](uv-explanation.md)

### Namespaces and Scopes

This topic is very important to understand how Python works, and it's a good idea to understand it before going deeper into the language.

* Nicola's notes: [Scopes and Namespaces](scopes-and-namespaces.md): this is a good overview of the topic.
* the same topic is also covered in more detail in the following sections:
  - [classes](classes-and-objects.md#how-scopes-and-namespaces-apply-to-classes)
  - [functions](functions.md#how-scopes-and-namespaces-apply-to-functions)

### Object Oriented Programming

* Nicola's notes: [Classes and Objects](classes-and-objects.md)

### Decorators

* Nicola's notes: [Decorators](decorators.md)


### Data Structures and Algorithms

TODO see https://roadmap.sh/python

### Context Managers

* Nicola's notes: [Context Managers](context-managers.md)







## Python Runtime Services, Memory Management and Garbage Collection
   - Dynamic Typing
   - Introspection
   - Memory Management
   - Reference Counting
   - The `gc` Module
   - Interpreter Command Line Options
   - Environment Variables 
   - Python Virtual Machine Details
   - Extending Python with C/C++


## Python Development Tools
   - The Python Interactive Interpreter
   - Debugging with `pdb`
   - Profiling and Benchmarking
   - Unit Testing (`unittest`, `pytest`)
   - Code Style Guide (PEP 8)

## Concurrency and Parallelism
- Multithreading (`threading` Module)
- Multiprocessing (`multiprocessing` Module)
- Async Programming (`asyncio`)

NOTE: In "Python Runtime Services, Memory Management and Garbage Collection", the topics about memory management and reference counting are somewhat related to how concurrency manages shared resources.
Consider adding cross-references between these sections to help the reader navigate the related content.

## The Standard Library
   - Overview of Commonly Used Modules
   - `math` and `cmath`
   - `datetime`
   - `collections`
   - `os` and `sys`
   - `re` (Regular Expressions)
   - `itertools`
   - `functools`

## Networking and Internet Data Handling
- `socket` Module
- HTTP Requests (`urllib`, `requests`)
- Data Serialization (`json`, `pickle`)

## Advanced Data Structures
- Custom Data Structures
  - User-Defined Classes
- Collections Module
  - `namedtuple`, `deque`, `Counter`, `OrderedDict`, etc.


## The Python C API (if applicable)
   - Interfacing with C Code
   - Writing C Extensions
   - Using `ctypes` and `cffi`


## Prompts


### Solution 1: start from the Diataxis Custom GTP


#### Context

We are going to create a complete language reference to the python language, you are an expert python teacher and developer that will help me defining the content of the full reference. For this reason, please don't be afraid to use technical terms and to be very specific.

#### Initial Prompt: build the outline

create a language reference from this, give me the initial outline in markdown. To find the initial list of topics look at this webpages: https://docs.python.org/3/tutorial/index.html and  https://learnxinyminutes.com/docs/python/



#### 

I want to build a page that summarizes the python language reference. I want to use the outline that I already have, but I want to add more details to each point.