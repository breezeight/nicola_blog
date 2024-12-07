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
- **Identity Operator** `is`: Checks if two variables refer to the same object.


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


### Decorators

* Nicola's notes: [Decorators](decorators.md)


### Data Structures and Algorithms

TODO see https://roadmap.sh/python


