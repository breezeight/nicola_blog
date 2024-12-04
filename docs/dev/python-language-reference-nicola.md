# Python Language Reference

> NOTE: at the end of the page there is a [list of prompts](python-language-reference-nicola.md#prompts) that I used to make AI summarize the python language reference and create this page.

## Introduction
- Overview of the Python Language
- Scope and Purpose of this Reference
- Conventions Used in the Documentation

## Lexical Structure
   - Keywords
   - Identifiers
   - Literals (Numeric, String, Boolean)
   - Operators and Punctuation
   - Line Structure and Indentation
   - Comments and Docstrings

## Variables, Constants, and Naming
See [python-language-reference-nicola/variables-constants-and-naming.md](python-language-reference-nicola/variables-constants-and-naming.md) for more details on:

- Variable Assignment
- Mutable vs Immutable Types
- Variable Naming Rules
- Constants

## Data Types
See [python-language-reference-nicola/data-types-and-literals.md](python-language-reference-nicola/data-types-and-literals.md) for more details on:

- Built-in Types Overview
- Numeric Types: int, float, complex
- Sequence Types: list, tuple, range
- Text Sequence Type: str
- Binary Sequence Types: bytes, bytearray, memoryview
- Set Types: set, frozenset
- Mapping Type: dict
- None Type
- Type Checking and Casting

## Expressions and Operators
- Arithmetic Operators
- Comparison Operators
- Logical Operators
- Bitwise Operators
- Assignment Operators
- Membership Operators
- Identity Operators
- Operator Precedence and Associativity

### The Walrus Operator  `:=`

The **Walrus Operator** (`:=`) was introduced in Python 3.8 as part of [PEP 572](https://peps.python.org/pep-0572/). It allows assignment expressions, enabling you to assign values to variables as part of an expression. This can lead to more concise and potentially more readable code by reducing the need for separate assignment statements.

Benefits

1. **Conciseness**: Reduces the number of lines by combining assignments and expressions.
2. **Efficiency**: Avoids redundant computations or function calls by storing results in variables.
3. **Readability**: When used appropriately, it can make the code more readable by clarifying the intent.

Use Cases

- **Loop Conditions**: Assigning loop variables within the loop condition.
- **Comprehensions**: Assigning intermediate values within list, set, or dictionary comprehensions.
- **Regular Expressions**: Capturing match objects within `if` statements.


#### Example 1: Assigning Within a While Loop

**Without Walrus Operator:**

```python
# Without Walrus Operator
line = input("Enter something: ")
while line != "quit":
    print(f"You entered: {line}")
    line = input("Enter something: ")
```

**With Walrus Operator:**

```python
# With Walrus Operator
while (line := input("Enter something: ")) != "quit":
    print(f"You entered: {line}")
```

In this example, the assignment of `line` occurs within the `while` loop condition, eliminating the need for a separate assignment before the loop and inside the loop.

#### Example 2: Using in List Comprehensions

**Without Walrus Operator:**

```python
# Without Walrus Operator
results = []
for n in range(10):
    square = n * n
    if square > 20:
        results.append(square)
```

**With Walrus Operator:**

```python
# With Walrus Operator
results = [square for n in range(10) if (square := n * n) > 20]
```

Here, `square` is assigned within the list comprehension, making the code more concise.


#### Example 3: Regular Expressions

**Without Walrus Operator:**

```python
import re

pattern = re.compile(r'\d+')
text = "There are 123 apples"
match = pattern.search(text)
if match:
    number = match.group()
    print(f"Found number: {number}")
```

**With Walrus Operator:**

```python
import re

pattern = re.compile(r'\d+')
text = "There are 123 apples"
if (match := pattern.search(text)):
    print(f"Found number: {match.group()}")
```

In this case, `match` is assigned within the `if` statement, streamlining the code.

## Cautions

While the Walrus Operator can make code more concise, it should be used judiciously to maintain readability. Overusing it or using it in complex expressions can make the code harder to understand.

### Example: Overuse Leading to Reduced Readability

**Less Readable:**

```python
# Overusing Walrus Operator
if (n := len(a := some_function())) > 10:
    print(f"Length of a ({n}) is greater than 10")
```

**More Readable:**

```python
# Improved readability
a = some_function()
n = len(a)
if n > 10:
    print(f"Length of a ({n}) is greater than 10")
```

In this example, separating the assignments enhances clarity.

#### Conclusion

The Walrus Operator is a powerful addition to Python that allows for more concise and efficient code by enabling assignment expressions. When used appropriately, it can enhance readability and reduce redundancy. However, it should be used thoughtfully to avoid compromising code clarity.


## Control Flow
- `if` Statements
- Loops: `for`,  `while` and Comprehensions
- Control Flow Modifiers: `break`, `continue`, `pass`
- Exception Handling: `try`, `except`, `finally`, `raise`
- Context Managers and the `with` Statement

## Error Handling and Debugging
- Debugging Techniques
- Logging
- Assertions
- Tracebacks


## Functions and Functional Programming

See [python-language-reference-nicola/functions-and-functional-programming.md](python-language-reference-nicola/functions-and-functional-programming.md) for more details on:

- Defining Functions
- Function Arguments: Positional, Keyword, Default, `*args`, `**kwargs`
- Anonymous Functions (`lambda`)
- Function Annotations
- Decorators
- Generators and Iterators
- Higher-Order Functions (e.g., `map`, `filter`, `reduce`)


> NOTE: Under "Functions and Functional Programming", you have "Function Arguments: Positional, Keyword, Default, *args, **kwargs" and "Anonymous Functions (lambda)".
> Some details around functions (like positional arguments, keyword arguments, default arguments) may also come up when discussing method definitions in "Classes and Objects". Consider cross-referencing instead of duplicating these concepts.

## Modules and Packages
   - Importing Modules: `import`, `from ... import`, `import ... as`
   - The Python Module Search Path
   - Creating Modules and Packages
   - The `__main__` Module


## Classes and Objects: Object-Oriented Programming
   - Defining Classes
   - Instance and Class Attributes
   - Methods: Instance, Class, and Static
   - Inheritance
   - Special Methods (Dunder Methods): `__init__`, `__str__`, etc.
   - Abstract Base Classes
   - Data Classes
   - Properties and Descriptors

### magic methods - dunder methods
In Python, [special methods](https://docs.python.org/3/glossary.html#term-special-method) are also called **magic methods**, or **dunder methods**. 

This latter terminology, [dunder](https://realpython.com/python-double-underscore/#dunder-names-in-python), refers to a particular naming convention that Python uses to name its [special  methods](https://realpython.com/python-classes/#providing-behavior-with-methods) and [attributes](https://realpython.com/python-classes/#attaching-data-to-classes-and-instances). The convention is to use double leading and trailing underscores in the name at hand, so it looks like `.__method__()`.

> [!NOTE] In this tutorial, you'll find the terms **special methods**, **dunder methods**, and **magic methods** used interchangeably.

The double underscores flag these methods as core to some Python features. They help avoid name collisions with your own methods and attributes. Some popular and well-known magic methods include the following:

| Special Method | Description |
| --- |  --- |
| [`.__init__()`](https://realpython.com/python-class-constructor/#object-initialization-with-__init__) | Provides an initializer in Python classes |
| --- |  --- |
| [`.__str__()` and `.__repr__()`](https://realpython.com/python-repr-vs-str/) | Provide string representations for objects |
| [`.__call__()`](https://realpython.com/python-callable-instances/) | Makes the instances of a class callable |
| [`.__len__()`](https://realpython.com/len-python-function/) | Supports the [`len()`](https://realpython.com/len-python-function/) function |


This is just a tiny sample of all the special methods that Python has. All these methods support specific features that are core to Python and its object-oriented infrastructure.

**Note:** For the complete list of magic methods, refer to the [special method section](https://docs.python.org/3/reference/datamodel.html#specialnames) on the data model page of Python's official documentation.

The Python documentation organizes the methods into several distinct groups:

-   [Basic customization](https://docs.python.org/3/reference/datamodel.html#basic-customization)
-   [Customizing attribute access](https://docs.python.org/3/reference/datamodel.html#customizing-attribute-access)
-   [Customizing class creation](https://docs.python.org/3/reference/datamodel.html#customizing-class-creation)
-   [Customizing instance and subclass checks](https://docs.python.org/3/reference/datamodel.html#customizing-instance-and-subclass-checks)
-   [Emulating generic types](https://docs.python.org/3/reference/datamodel.html#emulating-generic-types)
-   [Emulating callable objects](https://docs.python.org/3/reference/datamodel.html#emulating-callable-objects)
-   [Emulating container types](https://docs.python.org/3/reference/datamodel.html#emulating-container-types)
-   [Emulating numeric types](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types)
-   [`with` statement context managers](https://docs.python.org/3/reference/datamodel.html#with-statement-context-managers)
-   [Customizing positional arguments in class pattern matching](https://docs.python.org/3/reference/datamodel.html#customizing-positional-arguments-in-class-pattern-matching)
-   [Emulating buffer types](https://docs.python.org/3/reference/datamodel.html#emulating-buffer-types)
-   [Special method lookup](https://docs.python.org/3/reference/datamodel.html#special-method-lookup)

Take a look at the documentation for more details on how the methods work and how to use them according to your specific needs.

Here's how the Python documentation defines the term **special methods**:

> A method that is called implicitly by Python to execute a certain operation on a type, such as addition. Such methods have names starting and ending with double underscores. ([Source](https://docs.python.org/3/glossary.html#term-special-method))

There's an important detail to highlight in this definition. *Python implicitly calls special methods to execute certain operations in your code*. For example, when you run the addition `5 + 2` in a [REPL](https://realpython.com/python-repl/) session, Python internally runs the following code under the hood:

Python

```bash
`>>> (5).__add__(2)
7
`
```

The `.__add__()` special method of integer numbers supports the addition that you typically run as `5 + 2`.

Reading between the lines, you'll realize that even though you can directly call special methods, they're not intended for direct use. You shouldn't call them directly in your code. Instead, you should rely on Python to call them automatically in response to a given operation.

**Note:** Even though special methods are also called *magic methods*, some people in the Python community may not like this latter terminology. The only magic around these methods is that Python calls them implicitly under the hood. So, the official documentation refers to them as **special methods** instead.

Magic methods exist for many purposes. All the available magic methods support built-in features and play specific roles in the language. For example, built-in types such as [lists](https://realpython.com/python-list/), [strings](https://realpython.com/python-strings/), and [dictionaries](https://realpython.com/python-dicts/) implement most of their core functionality using magic methods. In your custom classes, you can use magic methods to make callable objects, define how objects are compared, tweak how you create objects, and more.

Note that because magic methods have special meaning for Python itself, you should avoid naming custom methods using leading and trailing double underscores. Your custom method won't trigger any Python action if its name doesn't match any official special method names, but it'll certainly confuse other programmers. New dunder names may also be introduced in future versions of Python.

Magic methods are core to Python's [data model](https://docs.python.org/3/reference/datamodel.html) and are a fundamental part of object-oriented programming in Python. In the following sections, you'll learn about some of the most commonly used special methods. They'll help you write better object-oriented code in your day-to-day programming adventure.

#### __init__ special method - controlling the object initialization

For example, the `__init__` method is used to initialize the object.

When creating custom classes in Python, probably the first and most common method that you implement is `.__init__()`. This method works as an **initializer** because it allows you to provide initial values to any [instance attributes](https://realpython.com/python-classes/#instance-attributes) that you define in your classes.

**Note:** To dive deeper into the object creation process in Python, check out [Python Class Constructors: Control Your Object Instantiation](https://realpython.com/python-class-constructor/).

The `.__new__()` special method also has a role in the class instantiation process. This method takes care of creating a new instance of a given class when you call the class constructor. The `.__new__()` method is less commonly implemented in practice, though.

In the following sections, you'll learn the basics of how these two methods work and how you can use them to customize the instantiation of your classes.

Python calls the `.__init__()` method whenever you call the constructor of a given class. The goal of `.__init__()` is to initialize any instance attribute that you have in your class. Consider the following `Point` class:


```python
`>>> class Point:
...     def __init__(self, x, y):
...         self.x = x
...         self.y = y
...

>>> point = Point(21, 42)
>>> point.x
21
>>> point.y
42
`
```

When you create the `point` instance by calling the class constructor, `Point()`, Python automatically calls `.__init__()` under the hood using the same arguments that you've passed to the constructor. You don't have to call `.__init__()` by yourself. You just rely on Python's implicit behavior. Note how the `.x` and `.y` attributes hold the values that you pass in when you call the constructor.


#### Creating Objects With .__new__()
The default implementation of .__new__() is enough for most practical use cases. So, you probably won’t need to write a custom implementation of .__new__() in most cases. However, you’ll find that this method is useful in some advanced use cases: [learn more](https://realpython.com/python-magic-methods/#creating-objects-with-__new__)


### Managing Attribute Access in Python: Special Methods vs. Decorators

In Python, controlling how attributes are accessed, assigned, and deleted within a class is crucial for maintaining data integrity and encapsulation. Two primary mechanisms facilitate this control: special methods (`__getattr__`, `__setattr__`, `__delattr__`) and decorators (notably `@property`). Understanding their differences and appropriate use cases is essential for effective class design.

#### Special Methods: `__getattr__`, `__setattr__`, and `__delattr__`

These dunder (double underscore) methods allow developers to customize attribute behavior dynamically:

- `__getattr__(self, name)`: Invoked when an attribute is accessed that doesn’t exist in the instance’s `__dict__`. It’s useful for defining dynamic attributes or handling missing attributes gracefully.
- `__setattr__(self, name, value)`: Called whenever an attribute assignment is attempted. This method can be overridden to enforce validation, type checking, or to implement computed properties.
- `__delattr__(self, name)`: Triggered when an attempt is made to delete an attribute. Overriding this method allows for custom behavior during attribute deletion.

#### Example: Implementing a Read-Only Attribute

```python
class ReadOnly:
    def __init__(self, value):
        self._value = value

    def __setattr__(self, name, value):
        if name == '_value' and hasattr(self, '_value'):
            raise AttributeError(f"{name} is read-only")
        super().__setattr__(name, value)

    def __getattr__(self, name):
        if name == 'value':
            return self._value
        raise AttributeError(f"{name} not found")
```

In this example, attempting to reassign `_value` after its initial set raises an `AttributeError`, effectively making it read-only.

#### Decorators: The `@property` Approach

Decorators provide a more declarative way to manage attribute access, especially when dealing with individual attributes. The `@property` decorator allows a method to be accessed like an attribute, enabling controlled access and mutation.

#### Example: Using `@property` for Attribute Validation

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
```

Here, accessing `circle.radius` retrieves the value, while setting `circle.radius = value` invokes the setter, allowing for validation.

#### Choosing Between Special Methods and Decorators

- **Use Special Methods** when you need to manage attribute access, assignment, or deletion dynamically across many attributes, especially when the attributes are not known in advance.
- **Use Decorators like `@property`** when you want to control access to a specific attribute, providing a clear and concise way to define managed attributes with optional validation or computation.

In summary, both approaches offer mechanisms to control attribute behavior in Python. The choice between them depends on the specific requirements of your class design and the level of control needed over attribute management.



## Input and Output
   - Reading from and Writing to Files
   - Working with Standard Input, Output, and Error
   - String Formatting
   - Serialization: `pickle`, `json`
   - Working with Binary Data
   - Handling File Exceptions

NOTE: The sections "Input and Output" and "Networking and Internet Data Handling" both mention serialization.
"Input and Output" contains "Serialization: pickle, json". "Networking and Internet Data Handling" has "Data Serialization (json, pickle)". To avoid redundancy, you could centralize the explanation of serialization under "Input and Output" and reference it in "Networking" for context.

#### More Common Magic Methods - WIP

Here are some more common magic methods:

-   [Representing Objects as Strings](https://realpython.com/python-magic-methods/#representing-objects-as-strings)
-   [Supporting Operator Overloading in Custom Classes](https://realpython.com/python-magic-methods/#supporting-operator-overloading-in-custom-classes)
-   [Introspecting Your Objects](https://realpython.com/python-magic-methods/#introspecting-your-objects)
-   [Controlling Attribute Access](https://realpython.com/python-magic-methods/#controlling-attribute-access)
-   [Managing Attributes Through Descriptors](https://realpython.com/python-magic-methods/#managing-attributes-through-descriptors)
-   [Supporting Iteration With Iterators and Iterables](https://realpython.com/python-magic-methods/#supporting-iteration-with-iterators-and-iterables)
-   [Making Your Objects Callable](https://realpython.com/python-magic-methods/#making-your-objects-callable)
-   [Implementing Custom Sequences and Mappings](https://realpython.com/python-magic-methods/#implementing-custom-sequences-and-mappings)
-   [Handling Setup and Teardown With Context Managers](https://realpython.com/python-magic-methods/#handling-setup-and-teardown-with-context-managers)


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

##  Glossary
   - Key Terms and Concepts



## Prompts


### Solution 1: start from the Diataxis Custom GTP


#### Context

We are going to create a complete language reference to the python language, you are an expert python teacher and developer that will help me defining the content of the full reference. For this reason, please don't be afraid to use technical terms and to be very specific.

#### Initial Prompt: build the outline

create a language reference from this, give me the initial outline in markdown. To find the initial list of topics look at this webpages: https://docs.python.org/3/tutorial/index.html and  https://learnxinyminutes.com/docs/python/



#### 

I want to build a page that summarizes the python language reference. I want to use the outline that I already have, but I want to add more details to each point.