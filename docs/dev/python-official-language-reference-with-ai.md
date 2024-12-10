## Document Scope  (AI Prompt)
This document is based on the official Python documentation: [The Python Language Reference](https://docs.python.org/3/reference/index.html), it is intended to act as a quick summary of the official documentation.

The idea is follow the official documentation structure and add a quick summary of each topic and make it more practical, highlighting the most important parts for me and keep out the rest.

For each section I will try to highlight:
* what is important to me
* when relevant, I will add a quick summary of the topic in my own words to make it more practical

### HOWTO use the AI Prompt

1. Copy the prompt below into your favorite AI assistant
2. Paste the content of the section you want to summarize
3. Review the output and make sure it is what you want
4. If you want to change something, just edit the prompt and run it again

Optionally you can save a specific prompt for a specific section in a file, so you can reuse it later.

Some useful follow up questions:
- you omitted the 3rd level subheadings, can you add them?


### AI Prompt: Python Language Reference (Practical Edition)

#### Objective:
Assist the user in creating a simplified, practical version of the official [Python Language Reference](https://docs.python.org/3/reference/index.html), focusing only on day-to-day usage of Python. This version should serve as a quick and easy-to-read summary, emphasizing what’s important for regular tasks and leaving out overly complex or rarely used aspects.

#### Instructions:
1. ALWAYS Ask to the user which section he want to summarize.
2. For each section **Follow the official Python documentation structure** and distill the content into concise, easy-to-understand summaries:
   - Provide a **brief summary** of the key concepts and syntax.
   - Highlight **what’s important** based on frequent use cases in daily coding tasks.
   - Include **useful code snippets** for practical examples.
   - if the topic is very common and needed by most of the python developer add a practical and complete reference
   - if the topic is very advanced add a brief summary and say to checkout the official doc
   - KEEP the original numbering from the official documentation.
   - add link to the official doc just after the heading 3 format of the subsection name with the format: [Link to the official doc](https://docs.python.org/3/reference/Link to the official doc)

3. **Simplify terminology** and focus on clarity, explaining terms in a way that a beginner or intermediate Python user can easily understand.
4. Exclude advanced or rarely used features unless they offer significant value for common workflows.
5. Add **personal summaries** or insights where necessary to make the content more relevant for regular usage scenarios.
6. Avoid making the reference exhaustive—focus on **practicality** and ease of use.
7. Minimize the use of subheading 4 format for examples and code snippets.

#### Output Format:
For each section:
- **Title**: Use the section name from the official Python documentation. This is mandatory and must be the first thing in the output in heading 2 format. Keep also the original numbering from the official documentation.
- **Quick Summary**: 1-2 sentences explaining the main idea of the section.
- **What’s Important**: A list or short description of key takeaways or frequently used parts.
- **Key Concepts**: Short definitions of important terms or concepts.
- **Examples**: Simple, practical code snippets to demonstrate typical usage.
- **Optional: Pitfalls to Avoid**: If there are common mistakes or tricky syntax, highlight them.
    
AVOID to respond with comments like "Here’s the practical edition for...", just output the content in a structured format.



## 2. Lexical Analysis

### Quick Summary
Lexical analysis in Python is about how the source code is broken down into tokens — the smallest elements like keywords, operators, identifiers, and literals. This section outlines how Python interprets code at this basic level.

### What’s Important
- Python code is divided into tokens such as identifiers, keywords, literals, and operators.
- Whitespace, comments, and line breaks play an important role.
- Python uses indentation to define code blocks, unlike most languages that use braces `{}`.
- String literals can span multiple lines and support different types like single, double, and triple quotes.
- Identifiers in Python are case-sensitive and must follow naming conventions.
  
### Key Concepts

1. **Tokens**:
   - Basic building blocks of Python code.
   - Include keywords (`if`, `else`, `for`), identifiers (variable names), literals (e.g., numbers, strings), and operators (`+`, `-`, `*`, `==`).

2. **Identifiers**:
   - Names for variables, functions, classes, etc.
   - Must begin with a letter (A-Z or a-z) or underscore (`_`), followed by letters, numbers, or underscores.
   - Case-sensitive (e.g., `Variable` and `variable` are different).

3. **Reserved Keywords**:
   - Cannot be used as identifiers.
   - Examples: `if`, `else`, `while`, `True`, `None`.

4. **Literals**:
   - Fixed values like numbers (`42`, `3.14`), strings (`"hello"`), and booleans (`True`, `False`).
   - String literals can be enclosed in single (`'`), double (`"`), or triple quotes (`'''` or `"""` for multi-line strings).

5. **Whitespace and Indentation**:
   - Python uses indentation (leading spaces or tabs) to define blocks of code (e.g., functions, loops).
   - A mix of spaces and tabs for indentation is not allowed.
   - Common indentation error: forgetting to properly align blocks of code.

6. **Comments**:
   - Single-line comments begin with `#` and are ignored by the interpreter.
   - Multi-line comments can be created by using triple quotes (`'''` or `"""`), though they are generally used for docstrings.

7. **Line Continuation**:
   - Implicit: Inside parentheses, brackets, or braces, line continuation is allowed without any special character.
   - Explicit: Outside of these contexts, a backslash (`\`) at the end of a line allows continuation.

### Examples

#### Tokens
```python
x = 10       # 'x' is an identifier, '=' is an operator, and '10' is a literal
if x > 5:    # 'if' is a keyword, '>' is an operator
    print("x is greater than 5")  # 'print' is a function, the string is a literal
```

#### Identifiers
```python
my_variable = 42  # valid identifier
_myVar123 = "hello"  # valid identifier with numbers and underscores
2nd_var = 10  # invalid identifier, cannot start with a number
```

#### String Literals
```python
# Single line strings
string1 = 'Hello'
string2 = "World"

# Multi-line string
multi_line_string = """This is
a multi-line
string."""
```

#### Indentation
```python
# Correct indentation
def my_function():
    print("Indented block")

# Incorrect indentation
def my_function():
print("No indentation")
```

#### Comments
```python
# This is a single-line comment

"""
This is a multi-line comment (usually used for documentation)
"""
```

#### Line Continuation
```python
total = 1 + 2 + 3 + \
        4 + 5 + 6  # Explicit line continuation

# Implicit line continuation inside parentheses
result = (1 + 2 + 3 +
          4 + 5 + 6)
```

### Optional: Pitfalls to Avoid

1. **Mixed indentation**:
   - Mixing tabs and spaces can cause `IndentationError`. Stick to one style (usually 4 spaces).
   
2. **Invalid identifiers**:
   - Starting an identifier with a number or using reserved keywords will raise `SyntaxError`.

3. **Improper string usage**:
   - Forgetting to close strings with matching quotes leads to syntax issues.

4. **Misuse of backslash for line continuation**:
   - Be careful when using a backslash to break lines—missing one or adding it in the wrong place can cause errors.



## 3. Data Model

**Quick Summary**

The data model defines how data structures and objects are represented and manipulated in Python. It outlines the behavior of Python objects, including their attributes, methods, and interactions.

**What's Important**

- **Everything is an object**: Numbers, strings, functions, and classes are all objects.
- **Standard types**: Understanding built-in types like numbers, sequences, mappings, and more.
- **Special methods**: Utilizing magic methods (dunder methods) to customize class behavior.
- **Mutability**: Knowing which objects can change after creation.

**Key Concepts**

- **Objects**: Fundamental units in Python with an identity, type, and value.
- **Types**: Define the operations an object supports and its possible values.
- **Mutability**: Indicates if an object's state can change (mutable) or not (immutable).
- **Special Methods**: Methods with double underscores (e.g., `__init__`, `__str__`) that enable custom behaviors.

### 3.1 Objects, Values, and Types
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)

**Quick Summary**

Every entity in Python is an object with a unique identity, a type that defines its behavior, and a value representing its data.

**What's Important**

- **Identity**: Unique and constant during an object's lifetime (`id()` function retrieves it).
- **Type**: Determines operations supported by the object (`type()` function retrieves it).
- **Value**: The actual data contained in the object.

**Examples**

```python
x = 42
print(id(x))    # Identity of x
print(type(x))  # <class 'int'>
print(x)        # 42 (Value)
```

### 3.2 The Standard Type Hierarchy
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy)

**Quick Summary**

Python provides a set of built-in types organized in a hierarchy, including numbers, sequences, mappings, classes, and exceptions.

**What's Important**

- **Immutable Types**: Cannot be altered after creation (e.g., numbers, strings, tuples).
- **Mutable Types**: Can be changed after creation (e.g., lists, dictionaries, sets).
- **Common Types**:
  - **Numbers**: `int`, `float`, `complex`
  - **Sequences**: `list`, `tuple`, `range`
  - **Mappings**: `dict`
  - **Sets**: `set`, `frozenset`
  - **Callable Types**: Functions, methods
  - **Modules and Classes**: Define namespaces and custom types

#### 3.2.1 None
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy)

**Quick Summary**

`None` is a special constant representing the absence of a value.

**Examples**

```python
def func():
    pass

result = func()
print(result)  # Output: None
```

#### 3.2.2 NotImplemented
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy)

**Quick Summary**

`NotImplemented` is a special value returned to indicate that an operation is not implemented for the given types.

**Examples**

```python
class MyNumber:
    def __add__(self, other):
        return NotImplemented
```

#### 3.2.3 Ellipsis
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy)

**Quick Summary**

`Ellipsis` (`...`) is used in slicing syntax and as a placeholder.

**Examples**

```python
def incomplete_function():
    ...

# Used in NumPy for advanced slicing
array[..., 0]
```

#### 3.2.4 Numbers
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy)

**Quick Summary**

Numbers are immutable data types representing numeric values.

**What's Important**

- **Integer (`int`)**: Whole numbers.
- **Floating Point (`float`)**: Numbers with decimal points.
- **Complex (`complex`)**: Numbers with real and imaginary parts.

**Examples**

```python
i = 10       # Integer
f = 3.14     # Float
c = 2 + 3j   # Complex
```

#### 3.2.5 Sequences
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy)

**Quick Summary**

Sequences are ordered collections of items, accessible by index.

##### 3.2.5.1 Immutable Sequences

- **Strings (`str`)**
- **Tuples (`tuple`)**
- **Bytes (`bytes`)**

*Examples:*

```python
s = "hello"
t = (1, 2, 3)
b = b"bytes"
```

##### 3.2.5.2 Mutable Sequences

- **Lists (`list`)**
- **Byte Arrays (`bytearray`)**

*Examples:*

```python
lst = [1, 2, 3]
lst[0] = 10  # Lists are mutable
```

#### 3.2.6 Set Types
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy)

**Quick Summary**

Sets are unordered collections of unique elements.

**What's Important**

- **Mutable Set**: `set`
- **Immutable Set**: `frozenset`
- **Operations**: Union (`|`), Intersection (`&`), Difference (`-`)

**Examples**

```python
s = {1, 2, 3}
s.add(4)
print(s)  # Output: {1, 2, 3, 4}
```

#### 3.2.7 Mappings
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy)

**Quick Summary**

Mappings are collections of key-value pairs.

**What's Important**

- **Dictionary (`dict`)**: The primary mapping type in Python.
- **Key Requirements**: Keys must be immutable and hashable.

**Examples**

```python
d = {'a': 1, 'b': 2}
print(d['a'])  # Output: 1
```

#### 3.2.8 Callable Types
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy)

**Quick Summary**

Objects that can be called like functions.

**What's Important**

- **Functions**: Defined using `def` or `lambda`.
- **Methods**: Functions associated with objects.
- **Classes**: Callable to create new instances.

**Examples**

```python
def func():
    print("Called")

func()  # Output: Called
```

#### 3.2.9 Modules
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy)

**Quick Summary**

Modules are files containing Python definitions and statements.

**Examples**

```python
import math
print(math.pi)  # Accessing module attributes
```

#### 3.2.10 Classes and Class Instances
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy)

**Quick Summary**

Classes define new types of objects, and instances are objects created from classes.

**Examples**

```python
class MyClass:
    pass

obj = MyClass()
print(type(obj))  # Output: <class '__main__.MyClass'>
```

### 3.3 Special Method Names
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#special-method-names)

**Quick Summary**

Special methods, also known as magic methods or dunder methods, allow you to define how objects of your class behave with built-in Python operations.

**What's Important**

- **Initialization**: `__init__` to initialize object state.
- **Representation**: `__str__` and `__repr__` for readable object representations.
- **Operator Overloading**: Methods like `__add__`, `__eq__` to define custom behavior for operators.
- **Context Management**: `__enter__` and `__exit__` for use with `with` statements.

#### 3.3.1 Basic Customization
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#basic-customization)

**Quick Summary**

Customize object creation, representation, and destruction.

**Key Methods**

- **`__init__(self, ...)`**: Initialize object's state.
- **`__new__(cls, ...)`**: Create a new instance; used in subclassing immutable types.
- **`__del__(self)`**: Called when an object is about to be destroyed.

**Examples**

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
```

#### 3.3.2 Customizing Attribute Access
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#customizing-attribute-access)

**Quick Summary**

Control how attributes are accessed, set, or deleted.

**Key Methods**

- **`__getattr__(self, name)`**: Called when an attribute is not found.
- **`__setattr__(self, name, value)`**: Called when an attribute assignment is attempted.
- **`__delattr__(self, name)`**: Called when an attribute deletion is attempted.
- **`__getattribute__(self, name)`**: Called for every attribute access.

**Examples**

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        if attr == 'age':
            return 30  # Default age
        raise AttributeError(f"{attr} not found")
```

#### 3.3.3 Customizing Class Creation
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#customizing-class-creation)

**Quick Summary**

Modify class creation behavior using metaclasses.

**Key Concepts**

- **Metaclasses**: Classes of classes that define how classes behave.
- **`__new__` and `__init__` in metaclasses**: Customize class creation.

*Advanced Topic*: Usually not needed for day-to-day coding.

#### 3.3.4 Customizing Instance and Subclass Checks
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#customizing-instance-and-subclass-checks)

**Quick Summary**

Customize behavior of `isinstance()` and `issubclass()`.

**Key Methods**

- **`__instancecheck__(self, instance)`**
- **`__subclasscheck__(self, subclass)`**

*Advanced Topic*: Useful when creating abstract base classes.

#### 3.3.5 Emulating Numeric Types
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types)

**Quick Summary**

Define numeric behavior for custom objects.

**Key Methods**

- **Arithmetic Operators**: `__add__`, `__sub__`, `__mul__`, etc.
- **Reflection Methods**: `__radd__`, `__rsub__`, etc.
- **Augmented Assignment**: `__iadd__`, `__isub__`, etc.

**Examples**

```python
class Counter:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return Counter(self.count + other)

counter = Counter(10)
new_counter = counter + 5
print(new_counter.count)  # Output: 15
```

#### 3.3.6 Emulating Container Types
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#emulating-container-types)

**Quick Summary**

Make custom objects behave like containers (e.g., lists, dictionaries).

**Key Methods**

- **`__len__(self)`**: Return the number of items.
- **`__getitem__(self, key)`**: Retrieve an item.
- **`__setitem__(self, key, value)`**: Set the value of an item.
- **`__delitem__(self, key)`**: Delete an item.
- **`__iter__(self)`**: Return an iterator.

**Examples**

```python
class MyList:
    def __init__(self):
        self.data = []

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data.insert(index, value)

my_list = MyList()
my_list[0] = 'a'
print(my_list[0])  # Output: 'a'
```

#### 3.3.7 Emulating Callables
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#emulating-callables)

**Quick Summary**

Allow instances of a class to be called as functions.

**Key Method**

- **`__call__(self, *args, **kwargs)`**

**Examples**

```python
class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x

add_five = Adder(5)
print(add_five(10))  # Output: 15
```

#### 3.3.8 Emulating Context Managers
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#emulating-context-managers)

**Quick Summary**

Enable objects to be used with the `with` statement.

**Key Methods**

- **`__enter__(self)`**: Called at the start of the `with` block.
- **`__exit__(self, exc_type, exc_value, traceback)`**: Called at the end of the `with` block.

**Examples**

```python
class FileOpener:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with FileOpener('test.txt') as f:
    content = f.read()
```

For more details, see [Context Managers in Python](../python-language-reference-nicola/context-managers.md).

#### 3.3.9 Special Method Lookup
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#special-method-lookup)

**Quick Summary**

Describes how special methods are resolved.

**What's Important**

- Special methods are looked up on the class, not the instance.
- Cannot be overridden at the instance level.

**Pitfalls to Avoid**

- Attempting to override special methods on an instance won't have the intended effect.

### 3.4 Coroutines
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#coroutines)

**Quick Summary**

Coroutines are generalizations of subroutines for non-preemptive multitasking.

**What's Important**

- **`async def` Functions**: Define coroutines.
- **Await Expression**: Use `await` to yield control.

**Examples**

```python
import asyncio

async def my_coroutine():
    await asyncio.sleep(1)
    print("Hello, World!")

asyncio.run(my_coroutine())
```

*Note*: This is an advanced topic; for daily use, understanding basic `asyncio` usage is sufficient.

### 3.5 Modules
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#modules)

**Quick Summary**

Modules are Python files containing definitions and statements.

**What's Important**

- **Namespaces**: Modules provide their own namespace.
- **Importing Modules**: Use `import` to include modules.

**Examples**

```python
import math
print(math.sqrt(16))  # Output: 4.0
```

### 3.6 Classes and Class Instances
[Link to the official doc](https://docs.python.org/3/reference/datamodel.html#classes-and-class-instances)

**Quick Summary**

Classes define new types, and instances are objects created from these classes.

**What's Important**

- **Class Definitions**: Use the `class` keyword.
- **Inheritance**: Classes can inherit from other classes.
- **Methods**: Functions defined within a class.

**Examples**

```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

dog = Dog()
dog.speak()  # Output: Bark
```

**Pitfalls to Avoid**

- **Method Resolution Order (MRO)**: Be cautious with multiple inheritance; Python uses C3 linearization for MRO.
- **Mutable Default Arguments**: Avoid using mutable objects as default values in methods.

**Example of Mutable Default Argument Pitfall:**

```python
class Example:
    def __init__(self, data=[]):
        self.data = data
```

*Correct Approach:*

```python
class Example:
    def __init__(self, data=None):
        if data is None:
            data = []
        self.data = data
```

---

**Note**

Understanding the data model is crucial for writing efficient and effective Python code. It allows you to leverage Python's object-oriented features and write code that integrates seamlessly with Python's built-in functions and operators.