# Python typing - Overview

Python’s typing system enhances code quality by allowing developers to annotate code with type information, improving readability and enabling static type checking.

Key highlights include Python’s evolution from dynamic typing to supporting type hints while remaining dynamically typed:

1. [Dynamic Typing in Python](#dynamic-typing-in-python-vs-static-typing-in-other-languages-vs-type-hints-in-python): Python determines variable types at runtime, offering flexibility but risking runtime errors.

2. [Reccomendation in Modern Python](#reccomendation-for-modern-python)

3. [Introduction: Hello Types and Annotations ](#introduction-hello-types-and-annotations)

4. [Type Alias VS Distinct Types - NewType](#type-aliases-vs-distinct-types---newtype)

5.	**Runtime Type Checking Tools**: Libraries like Pydantic, Typeguard, and Runtime Type Checker enforce type validation during execution, aiding error handling and data validation.

5.	[Pros and Cons of type hints](#pros-and-cons-of-type-hints):
* 	Pros: Improved documentation, tooling support, and architectural clarity.
* 	Cons: Added development effort and slight performance overhead.

6.	**Best Practices**:
* 	Gradual adoption in critical areas.
* 	Use simplified syntax from Python 3.12.
* 	Employ runtime checking libraries where necessary.

These features and practices make Python’s typing system a powerful tool for writing maintainable and robust code.

> [!TIP] For a more practical introduction see [Real Python - Python Type Checking](https://realpython.com/python-type-checking/)

Related official and community documentation:


* **Typing cheat sheet by MyPy** (summarized here and integrated by me in [Python Type Hints Reference](dev/python-language-reference-nicola/stdlib-devtools-typing-reference.md)): A quick reference of type hints.

* ["Static Typing with Python"](https://typing.readthedocs.io/en/latest/): Type-checker-agnostic documentation written by the community detailing type system features, useful typing related tools and typing best practices. **it's also linked in the official documentation**.

* [Python typing documentation](https://docs.python.org/3/library/typing.html) a complete official reference of type hints. It's not a good starting point but a good reference for details and edge cases. Probably the best and up to date reference for details and edge cases.


## Dynamic Typing in Python VS Static Typing in other languages VS Type Hints in Python

### Python is a dynamically typed language
Python is a dynamically typed language, which means that the type of a variable **is determined at runtime rather than at compile time**. 
This flexibility allows for more dynamic and flexible code, but it can also lead to runtime errors if not handled properly.

The following dummy examples demonstrate that Python has dynamic typing:

```python
if False:
    1 + "two"  # This line never runs, so no TypeError is raised
else:
...     1 + 2
...
3

>>> 1 + "two"  # Now this is type checked, and a TypeError is raised
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

In the first example, the branch `1 + "two"` never runs so it’s never type checked. The second example shows that when `1 + "two"` is evaluated it raises a `TypeError`  since you can’t add an integer and a string in Python.

Next, let’s see if variables can change type:

```python
>>> thing = "Hello"
>>> type(thing)
<class 'str'>

>>> thing = 28.1
>>> type(thing)
<class 'float'>
type() returns the type of an object. These examples confirm that the type of thing is allowed to change, and Python correctly infers the type as it changes.
```

### Static Typing (in other languages)

Static typing is a feature of some programming languages (for instance C and Java) where **variables are assigned a type at compile time, and the type of a variable cannot be changed at runtime**. 
This approach provides more predictable behavior and can catch errors at compile time, but it may require more explicit type annotations and can be less flexible than dynamic typing.

### Python Type hints

Python will always [remain a dynamically typed language](https://www.python.org/dev/peps/pep-0484/#non-goals). 
However, [PEP 484](https://www.python.org/dev/peps/pep-0484/) introduced type hints, which make it possible to also do static type checking of Python code.

Unlike how types work in most other statically typed languages, type hints by themselves don't cause Python to enforce types. As the name says, type hints just suggest types. There are other tools, which [you'll see later](https://realpython.com/python-type-checking/#static-type-checking), that perform static type checking using type hints.

### Duck Typing

Duck typing is a concept in Python where the type of an object is determined by its behavior rather than its explicit type. In duck typing, an object's suitability for a task is based on its methods and properties, not its declared type. This approach emphasizes the dynamic nature of Python and allows for more flexibility in code design.

Understanding Python’s nature, particularly its reliance on duck typing, is essential to grasping its typing system. Python’s type hints are designed to complement its dynamic, behavior-driven approach rather than impose the strict constraints typical of statically typed languages. This flexibility underscores how type hints enhance code clarity and safety without compromising the language’s dynamic essence.

Another term that is often used when talking about Python is duck typing. This moniker comes from the phrase “if it walks like a duck and it quacks like a duck, then it must be a duck” (or any of its variations).

Duck typing is a concept related to dynamic typing, where **the type or the class of an object is less important than the methods it defines**. Using duck typing you do not check types at all. Instead you check for the presence of a given method or attribute.

As an example, you can call `len()` on any Python object that defines a `.__len__()` method:

```python
>>> class TheHobbit:
...     def __len__(self):
...         return 95022
...
>>> the_hobbit = TheHobbit()
>>> len(the_hobbit)
95022
```

Note that the call to `len()` gives the return value of the `.__len__()` method. In fact, the implementation of `len()` is essentially equivalent to the following:

```python
def len(obj):
    return obj.__len__()
```

In order to call `len(obj)`, the only real constraint on `obj` is that it must define a `.__len__()` method. Otherwise, the object can be of types as different as `str`, `list`, `dict`, or `TheHobbit`.

Duck typing is somewhat supported when doing static type checking of Python code, using structural subtyping. You’ll learn more about duck typing later.


## Reccomendation for Modern Python
To fully leverage Python’s modern typing system, it’s important to adopt best practices and take advantage of the latest enhancements introduced in recent versions, particularly Python 3.12. While older syntax remains valid and supported for backward compatibility, the new streamlined syntax simplifies usage and is recommended for consistency and future-proofing in modern Python development. For example, you can now use `list[int]` instead of `List[int]`:

```python
# Old syntax (still valid) 👎:
from typing import List
numbers: List[int] = [1, 2, 3]

# New syntax 👍:
numbers: list[int] = [1, 2, 3]
```

### Key Improvements in Python 3.12 Type Hints

1.  **Simplified Syntax for Generics**:

    -   The new syntax allows developers to define generic types without importing from the `typing` module. For example, instead of using `List[int]`, you can now use `list[int]`.
    -   This change reduces boilerplate code and aligns Python's generics more closely with those in other programming languages, enhancing readability and maintainability ([1](https://arjancodes.com/blog/python-generics-syntax/), [2](https://www.infoworld.com/article/2338514/the-best-new-features-and-fixes-in-python-3-12.html)).

2.  **Type Variables**:

    -   Type variables can now be declared directly in function signatures using a cleaner syntax. For instance:
        ```python
        def func[T](a: T, b: T)-> T:
            return a + b
        ```

    -   This eliminates the need for importing `TypeVar`, streamlining the process of creating generic functions and classes ([2](https://www.infoworld.com/article/2338514/the-best-new-features-and-fixes-in-python-3-12.html), [3](https://realpython.com/python312-typing/)).

3.  **Bounded and Constrained Types**:

    -   Python 3.12 simplifies bounding and constraining generic types with a more straightforward syntax. For example:
        
        ```python
        classContainer[T: Mapping]:...
        ```

    -   This allows developers to specify constraints directly in the type variable declaration, making it easier to ensure that types conform to specific interfaces or sets of types ([1](https://arjancodes.com/blog/python-generics-syntax/), [3](https://realpython.com/python312-typing/)).

4.  **TypedDict Enhancements**:

    -   The introduction of `TypedDict` allows for more precise typing of keyword arguments (`**kwargs`). This enables developers to define varying types for each keyword argument, increasing flexibility and clarity in function signatures.
    -   Example:
        ```python
        from typing import TypedDict
        classMovie(TypedDict):
            name: str
            year: int

        def foo(**kwargs: Unpack[Movie]) -> None:
            ...
        ```

    -   This feature addresses limitations in previous versions where all keyword arguments were treated as a single type[2
        ](https://www.infoworld.com/article/2338514/the-best-new-features-and-fixes-in-python-3-12.html)[5
        ](https://hackernoon.com/whats-new-in-python-312).

5.  **Improved Error Messages**:

    -   Python 3.12 enhances error messages related to type hints, providing clearer guidance on what might be wrong when type errors occur. This improvement helps developers quickly identify and fix issues in their code[2
        ](https://www.infoworld.com/article/2338514/the-best-new-features-and-fixes-in-python-3-12.html).

#### Recommendations for Using Type Hints in Python 3.12


-   **Adopt the New Syntax**: Use the simplified syntax for generics and type variables to reduce verbosity and improve code clarity.
-   **Utilize TypedDict for Keyword Arguments**: When defining functions that accept keyword arguments with varying types, leverage `TypedDict` to specify exact types for each argument.
-   **Be Explicit with Constraints**: Clearly define any constraints on type variables to enhance type safety and improve IDE support for autocompletion and error detection.
-   **Maintain Consistency**: Follow consistent naming conventions and formatting styles throughout your codebase to enhance readability.

#### Example of New Syntax


Here's a complete example demonstrating some of the new features:

``` python
from collections.abc import Mapping
from typing import TypedDict

class Movie(TypedDict):
    name: str
    year: int

def add[T](a: T, b: T)-> T:
    return a + b

class Container[T: Mapping]:
    def __init__(self):
        self.items: list[T] = []
    def add_item(self, item: T)-> None:
        self.items.append(item)
    def process_movie(**kwargs: Unpack[Movie])-> None:
        print(f"Processing movie: {kwargs['name']} ({kwargs['year']})")

# Usage examples
result = add(5,10)
container = Container[str]()
container.add_item("Hello")
process_movie(name="Inception", year=2010)
```

#### Conclusion

The enhancements in Python 3.12 regarding typing make it easier for developers to write clear, maintainable code while taking full advantage of static typing features. By adopting these new practices, you can improve both the quality and readability of your codebase



## Introduction: Hello Types and Annotations

Let’s see for example how to add type hints to a function using . Consider this example:

```python
def greet(name, uppercase=False):
    if uppercase:
        return f"HELLO, {name.upper()}!"
    else:
        return f"Hello, {name.capitalize()}!"
```

This function takes a name and an optional uppercase flag. By default, it returns a properly capitalized greeting. If uppercase is True, the greeting is in uppercase:

```python
>>> print(greet("alice"))
Hello, Alice!

>>> print(greet("bob", uppercase=True))
HELLO, BOB!

Now, let’s add type hints to the function:

```python
def greet(name: str, uppercase: bool = False) -> str:
    ...
```

Here:
* `name: str` means the `name` argument should be a string, 
* `uppercase: bool = False` specifies that `uppercase` is an optional boolean with a default value of `False`, 
* `-> str` indicates the function returns a string.

Type hints are not enforced at runtime but can be checked with tools like `mypy`. For example, if you accidentally pass a non-boolean value to `uppercase`, the program will run but may behave incorrectly:

```python
>>> print(greet("alice", uppercase="yes"))  
Hello, Alice!  # Incorrect behavior
```

A static type checker like mypy would catch this issue:

```bash
$ mypy greet_example.py
greet_example.py:5: error: Argument "uppercase" to "greet" has incompatible
                          type "str"; expected "bool"
```

Using type hints ensures your code is easier to understand and less error-prone.

## Pros and Cons of type hints
Pros and Cons of Static Type Checking in Python

Pros:
* **Improved Documentation**: Type hints act as in-code documentation, reducing reliance on docstrings for describing argument types.
* **Enhanced Tooling**: IDEs and linters, like PyCharm, provide better code completion and error detection with type hints.
* **Cleaner Architecture**: Writing type hints encourages thoughtful design, reducing over-reliance on dynamic typing or overloaded methods.

Cons:
* **Increased Effort**: Adding type hints requires additional developer time, though it often saves debugging effort later.
* **Compatibility**: Type hints work best in Python 3.6+ due to improvements in annotations, though older versions offer limited support.
* **Startup Overhead**: Using the typing module can slightly increase startup time, which may impact short scripts.

When to Use Type Hints:
* **Libraries**: They add significant value for libraries, ensuring compatibility for other developers’ type-checked code.
* **Large Projects**: Highly recommended for understanding type flow, especially in collaborative projects.
* **Skip for Beginners**: New Python learners can wait to add type hints but adding them is a good practice to get used to since the beginning.
* **Not Essential for Scripts**: Short, disposable scripts don’t benefit much from type hints.

> [!TIP] Final Thoughts:
> Type hints improve code quality, much like unit tests, and **should be introduced gradually**. Start with critical components and expand where it adds value. In larger projects or public libraries, type hints are particularly beneficial.

## Python type checking at runtime

**Runtime Behavior**: Type hints are not enforced at runtime; they are for static analysis only but some lib like `Pydantic`, `Runtime Type Checker`, `Typeguard` can enforce them at runtime.

While static type checkers like **mypy** can analyze code for type consistency before execution, they do not enforce type constraints during runtime. To address this, several libraries have been developed to perform runtime type checking:

- **Pydantic**: This library validates data against defined types and raises errors when the data does not conform. It uses Python's type hints for validation and can automatically cast types where possible.

  ```python
  from pydantic import BaseModel
  
  class User(BaseModel):
      id: int
      name: str

  user = User(id=1, name="Alice")  # Valid
  user = User(id="not_an_int", name="Alice")  # Raises validation error
  ```

- **Runtime Type Checker**: This package allows you to check types using decorators or functions like `check_type`, which raises a `TypeError` if the provided data does not match the expected type.

  ```python
  from runtime_type_checker import check_type
  
  check_type("example", str)  # OK
  check_type(123, str)        # Raises TypeError
  ```

- **Typeguard**: Another library that checks function arguments against their annotations at runtime.

### Benefits
- **Data Validation**: Runtime type checking helps ensure that data received from external sources (e.g., user input) conforms to expected types.
- **Error Handling**: By catching type mismatches early in the execution flow, developers can provide more informative error messages and handle exceptions more gracefully.

### Drawbacks
- **Performance Overhead**: Adding runtime checks can slow down execution compared to relying solely on static analysis.
- **Complexity**: Introducing additional libraries for runtime checks can complicate codebases and increase dependencies.

### Conclusion

While Python's dynamic typing offers significant flexibility, it also necessitates careful handling of types at runtime to prevent errors. Libraries like Pydantic and Runtime Type Checker provide mechanisms for enforcing type constraints during execution, enhancing code reliability. However, developers should weigh the benefits of these checks against potential performance impacts and code complexity.

Citations:
- [1] https://testdriven.io/blog/python-type-checking/
- [2] https://pypi.org/project/runtime-type-checker/
- [3] https://discuss.python.org/t/proposal-for-enhancing-runtime-type-checking-in-python-using-pattern-matching-and-type-hints-in-function-definitions/59391
- [4] https://stackoverflow.com/questions/57002686/using-python-type-hints-as-runtime-type-checking-raise-typeerror-if-different
- [5] https://mypy.readthedocs.io/en/stable/runtime_troubles.html
- [6] https://www.reddit.com/r/Python/comments/9f335d/has_anyone_tried_enforcing_python_type_hints_at/
- [7] https://realpython.com/python-type-checking/
- [8] https://www.reddit.com/r/Python/comments/17dpmll/are_you_using_types_in_python/

## Write TypeHints using Annotations or Type Comments

The main way to add type hints is using `annotations` the other way is using `type comments`.

[PEP 484](https://www.python.org/dev/peps/pep-0484/) defined how to add type hints using **annotations** to your Python code, based off work that Jukka Lehtosalo had done on his Ph.D. project--- [mypy](https://mypy.readthedocs.io/en/stable/).

Here are some examples of how to use type annotations in Python:

```python
# A function that adds two numbers
def add(a: int, b: int) -> int:
    return a + b

# A function that returns a list of strings
def get_names() -> list[str]:
    return ["Alice", "Bob", "Charlie"]

# A function that takes a dictionary and returns a value
def get_value(data: dict[str, int], key: str) -> int:
    return data.get(key, 0)
```

For a more detailed list of annotations see [stdlib-devtools-typing-reference.md](stdlib-devtools-typing-reference.md)


### Type Comments Example

Type comments are useful for codebases that need to remain compatible with Python versions older than 3.6. They place type information in comments rather than annotations:

```python
# Type comment for a variable
names = ["Alice", "Bob", "Charlie"]  # type: list[str]

# Type comment for a function
def add(a, b):  # type: (int, int) -> int
    return a + b
```

### General Recommendations 

1.	**Prefer Annotations**: Use annotations for all new codebases or projects, as they are more readable and provide better tooling support.
2.	**Use Type Comments for Legacy Code**: In legacy codebases that must support Python versions earlier than 3.6, type comments are a practical alternative.
3.	**Stick to Modern Syntax**: Use updated syntax, such as `list[int]` instead of `List[int]`, for clarity and future compatibility.
4.	**Validate with Tools**: Run static type checkers like mypy to ensure consistency and identify issues early in the development process.
5.	**Document Complex Types**: For complex or custom types, define and document them using TypeAlias or TypedDict for clarity and reuse.


## Type Aliases VS Distinct Types - NewType

**Type aliases** provide a way to assign meaningful names to complex or repetitive type definitions, while **distinct types (via NewType)** create separate types for stricter logical constraints.

Since Python 3.12, the new `type` statement replaces `TypeAlias` for defining type aliases, offering native support for forward references and a clearer syntax and is the recommended way to define type aliases.

1. **Type aliases** are a way to **create new names for existing types**, making code more readable and maintainable. They were introduced in Python 3.5 with the typing module, which allows for type hints and annotations. 

2. **NewType** is a helper function that **creates a distinct type** from an existing type. It was introduced in Python 3.5 with the typing module, which allows for type hints and annotations.

The purpose of type aliases is to simplify complex type annotations.

Type aliases look like this:

```python
type Vector = list[float]
#or
Vector = list[float]
# in python 3.12+: Vector is a typing.TypeAliasType
# before python 3.12: Vector is a types.GenericAlias
#or (deprecated since python 3.12)
Vector = typing.TypeAlias("Vector", list[float])
```

Using the NewType helper looks like this:

```python
from typing import NewType

Vector = NewType("Vector", list[float])
```

In either case, you now have a type called `Vector` that you can use in your code.

```python
def min(v: Vector) -> float:
    # TODO: write implementation
    return 0.0
```

So, which should you use, and when?

* For a reference see [stdlib-devtools-typing-reference.md](stdlib-devtools-typing-reference.md#type-aliases-reference)
* for a detailed explanation read below.

Other useful resources:
* [Official Type Aliases documentation](https://docs.python.org/3/library/typing.html)
* [Semi-official community doc (easier to read)](https://typing.readthedocs.io/en/latest/spec/aliases.html): Type Aliases

### Type Aliases 

Purpose: Use type aliases to add clarity to your code.

Type aliases are exactly that; simply an alias for a type. Anywhere you refer to the original type (e.g. `list[float]`), you can now also refer to it as the alias (e.g. `Vector`) instead; they are interchangeable synonyms.

Type aliases are useful for simplifying and clarifying code that deals with complex types.

For example, in 2D geometry software it's common to deal with **points** in two-dimensional space, represented as a pair of floats:

```python
origin = (0.0, 0.0)
```

In that example, the type of `origin` is `tuple[float, float]`. So to write a function that takes a point as input, you'd write:

```python
def move_to(point: tuple[float, float]) -> None:
    # TODO: write implementation
    pass
```

Similarly, it's common to define **sizes** as a width and a height, also represented as a pair of floats:

```py
size = (3.0, 4.0)
```

And finally, it's common to define a **rectangle** as a point, defining the origin of the rectangle, and a size:

```py
origin = (0.0, 0.0)
size = (3.0, 4.0)
rect = (origin, size)
```

Here `origin` is of type `tuple[float, float]`, and `size` is also of type `tuple[float, float]`, so `rect`, which is a tuple containing `origin` and `size`, is of type `tuple[tuple[float, float], tuple[float, float]]`. This starts to become cumbersome. For example, let's look at a function that takes a rectangle as input:

```python
def get_area(rect: tuple[tuple[float, float], tuple[float, float]]) -> float:
    # TODO: write implementation
    return 0.0
```

Ugh, that's messy! And it gets worse. Let's say we have a function that takes a point and a rectangle, and determines whether the point lies within the rectangle:

```py
def point_is_in_rect(
    point: tuple[float, float], 
    rect: tuple[tuple[float, float], tuple[float, float]]
) -> bool:
    # TODO: write implementation
    return False
```

Your function definitions start to look less like function definitions and more like type soup. Ugh.

**This is exactly the problem that type aliases solve.**

Let's see how type aliases can make this code much more readable:

```py
# Declare some type aliases to make sense of the chaos
Point2D = tuple[float, float]
Size2D = tuple[float, float]
Rectangle = tuple[Point2D, Size2D]

def get_area(rect: Rectangle) -> float:
    # TODO: write implementation
    return 0.0

def point_is_in_rect(point: Point2D, rect: Rectangle) -> bool:
    # TODO: write implementation
    return False

rect = ((0.0, 0.0), (3.0, 4.0))
print(get_area(rect))

x = (2.0, 5.0)
print(point_is_in_rect(x, rect))
```

Much better!

Note that these type aliases are just that: aliases. There's nothing special about `Point2D`, you can use it anywhere you would use `tuple[float, float]`. You can even pass a `Point2D` to a function expecting a `Size2D` and vice versa, since they're both synonyms for the same type. This may or may not be your intention.

### Distinct Types (NewType): for catching more logical errors

Unlike type aliases, the NewType helper creates a completely new type. It is not a synonym, and cannot be used interchangeably with its underlying type.

A good example of where this might be useful is in our code from the previous section. Consider this snippet of code:

```python
Point2D = tuple[float, float]
Size2D = tuple[float, float]
Rectangle = tuple[Point2D, Size2D]

def get_area(rect: Rectangle) -> float:
    _, size = rect
    width, height = size
    return width * height

origin = (0.0, 0.0)
size = (3.0, 4.0)
rect = (size, origin) # ERROR not catched by the type checker with type alias: I've passed the size and origin in the wrong order 
print(get_area(rect)) # prints 0.0
```

There is a semantic error in this code. In the line where I instantiate the `rect` variable, I've passed the size and origin in the wrong order. The syntax is correct, and the code runs just fine, but the output is not as expected.

In its current form, the type checker cannot help me here, because `Point2D` and `Size2D` are **exactly the same type**. They are both just aliases for `tuple[float, float]`.

Is there a way the type checker could have caught this bug at type-checking time, rather than allowing it to misbehave at runtime?

Yes. **This is exactly the problem that NewType solves.**

Let's rewrite the code, but this time declare `Point2D` and `Size2D` as new types.

```python
from typing import NewType

Point2D = NewType("Point2D", tuple[float, float])
Size2D = NewType("Size2D", tuple[float, float])
Rectangle = tuple[Point2D, Size2D]

def get_area(rect: Rectangle) -> float:
    _, size = rect
    width, height = size
    return width * height

# To instantiate types declared with NewType with 
# literal values, wrap the values in TypeName(...)
origin = Point2D((0.0, 0.0))
size = Size2D((3.0, 4.0))

rect = (size, origin)
print(get_area(rect))
```

Now let's type-check this code. There are a number of type checkers available for Python; I'm using Microsoft's [pyright](https://github.com/microsoft/pyright), which is the default Python type checker in VS Code.

```sh
$ pyright demo.py 

  /Users/simon/demo.py:18:16 - error: Argument of type "tuple[Size2D, Point2D]" cannot be assigned to parameter "rect" of type "Rectangle" in function "get_area"
    Tuple entry 1 is incorrect type
      "Size2D" is incompatible with "Point2D" (reportGeneralTypeIssues)
1 error, 0 warnings, 0 informations 
```

Great! This error is also highlighted for me in VS Code, so I can see the error immediately as I type my code.

<img width="909" alt="Screenshot 2022-07-29 at 11 32 34 am" src="https://user-images.githubusercontent.com/116432/181767541-dededfc5-02bb-4baa-a04a-2473cf14e216.png">

### Should I just use NewType everywhere?

Probably not. NewType adds a small overhead for developers, namely having to wrap literal values in `TypeName(...)` every time you instantiate a value of a type created with NewType. (There's also a minuscule runtime overhead to using NewType, but you almost certainly don't need to worry about that.)

I like to use these two approaches together, as described above. I use NewType when I need to enforce type correctness, and type aliases where I want to avoid repeating complex types.

### IMPORTANT recommendation for Python 3.12+ 

Python 3.12 has introduced several significant improvements to the typing system, making it more intuitive, less verbose, and enhancing the overall developer experience. Here's an overview of the key enhancements and recommendations for using type hints effectively in Python 3.12.


## Beyond the Basics: Complex Type Hints in Python

This section just list advanced type annotations, addressing complex scenarios and enabling developers to express intricate type relationships and constraints effectively.

### Special typing primitives

* See the Official documentation: [Special typing primitives](https://docs.python.org/3/library/typing.html#special-typing-primitives)

Here we collect some examples of advanced typing usage from real-world Python projects, demonstrating their practical applications:


#### Any

Example from [Django REST Framework](https://github.com/encode/django-rest-framework):

```python
from typing import Any

def get_renderer_context(self) -> dict[str, Any]:
    return {
        'view': self,
        'request': self.request,
        'response': self.response,
    }
```

In Django REST Framework, `Any` is used to indicate that the dictionary values can be of any type, providing flexibility in the renderer context.

#### AnyStr

Example from [Tornado](https://github.com/tornadoweb/tornado):

```python
from typing import AnyStr

def write(self, chunk: AnyStr) -> None:
    if isinstance(chunk, bytes):
        chunk = chunk.decode('utf-8')
    # Process the chunk
```

Tornado uses `AnyStr` to allow the write method to accept both `str` and `bytes`, accommodating different data types for writing responses.

#### LiteralString

See the [Official documentation](https://docs.python.org/3/library/typing.html#typing.LiteralString)

Example from [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy):

```python
from typing import LiteralString

def execute_query(query: LiteralString) -> None:
    # Execute the SQL query
    pass
```

SQLAlchemy uses `LiteralString` to ensure that only literal strings are passed to the `execute_query` function, enhancing security by preventing SQL injection.

#### Never and NoReturn
Never and NoReturn have the same meaning in the type system and static type checkers treat both equivalently.

Example from [FastAPI](https://github.com/tiangolo/fastapi):

```python
from typing import Never

def fatal_error() -> Never:
    raise RuntimeError("This function never returns")
```

In FastAPI, `Never` is used to annotate functions that are not expected to return, such as those that raise exceptions unconditionally.


#### Self

Example from [Pydantic](https://github.com/pydantic/pydantic):

```python

from typing import Self

class Config:
    def set_option(self, key: str, value: str) -> Self:
        setattr(self, key, value)
        return self
```

Pydantic uses `Self` to indicate that the method returns an instance of the same class, facilitating method chaining.

#### TypeAlias

Example from [Pandas](https://github.com/pandas-dev/pandas):

```python
from typing import TypeAlias

DataFrameOrSeries: TypeAlias = 'DataFrame | Series'
```

Pandas defines a `TypeAlias` to represent a type that can be either a `DataFrame` or a `Series`, simplifying type annotations.

#### Union

Example from [Flask](https://github.com/pallets/flask):

```python
from typing import Union

def get_value(key: str) -> Union[str, None]:
    return session.get(key)
```

Flask uses `Union` to indicate that the `get_value` function can return either a `str` or `None`, depending on the session data.

#### Optional

Example from [Requests](https://github.com/psf/requests):

```python
from typing import Optional

def fetch_data(url: str, timeout: Optional[int] = None) -> Response:
    return requests.get(url, timeout=timeout)
```

Requests uses `Optional` to specify that the `timeout` parameter can be an `int` or `None`, providing flexibility in function calls.

#### Concatenate

Example from [Starlette](https://github.com/encode/starlette):

```python
from typing import Callable, Concatenate, ParamSpec

P = ParamSpec('P')

def add_logging(func: Callable[Concatenate[str, P], None]) -> Callable[P, None]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> None:
        print("Logging")
        func("INFO", *args, **kwargs)

    return wrapper
```

Starlette uses `Concatenate` to define decorators that add parameters to the wrapped function, enhancing flexibility in function signatures.

#### Literal

Example from [Pydantic](https://github.com/pydantic/pydantic):


```python
from typing import Literal

from pydantic import BaseModel

class User(BaseModel):

    role: Literal['admin', 'user', 'guest']
```

*Comment:* 
Pydantic uses `Literal` to restrict the `role` field to specific string values, ensuring data integrity.

#### ClassVar

Example from [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy):

```python
from typing import ClassVar

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):

    __tablename__: ClassVar[str] = 'users'

    id = Column(Integer, primary_key=True)
```
 
SQLAlchemy uses `ClassVar` to indicate that `__tablename__` is a class variable, not an instance variable, defining the table name for the ORM model.

#### Final

Example from [FastAPI](https://github.com/tiangolo/fastapi):

```python
from typing import Final

API_VERSION: Final = "1.0"
```

FastAPI uses `Final` to indicate that `API_VERSION` is a constant value that should not be reassigned.
































### Building generic types and type aliases


#### Generic

See the [Official documentation](https://docs.python.org/3/library/typing.html#typing.Generic)

TODO: READ [Python Generics Syntax](https://arjancodes.com/blog/python-generics-syntax/)

##### What is a generic?
A generic is a type of object whose behavior doesn’t depend on the type it is handling and instead can be used in the same way for many types. An example of a generic is the built-in `list[T]` object, where `T` is the generic type. This means we can type hint the object as being a list of strings, integers, or any other object we desire, as the functionality of a list does not depend on its contents.

Generics are essential for creating reusable components. They allow us to write functions, classes, and data structures that can work with any data type while maintaining type consistency.

For instance, consider a **stack data structure**. Using generics, we can implement a stack that works uniformly with integers, strings, or any other type.

Type-hinting generics in Python got a whole lot easier with the release of Python 3.12. No longer do we need to define `TypeVars` and `ParamSpecs`  . 


`Generic` is a base class provided by the typing module that allows the creation of generic classes and functions. It enables the definition of classes and functions that can operate with different data types while maintaining type safety.

Usage:
By subclassing `Generic` and specifying type variables, you can create classes that are type-agnostic. This is particularly useful for data structures like linked lists, trees, or custom containers.

Example:
In the Pydantic library, Generic is used to define models that can handle various data types:

from typing import Generic, TypeVar
from pydantic import BaseModel

T = TypeVar('T')

class ResponseModel(BaseModel, Generic[T]):
    data: T
    error: str | None

Explanation:
Here, ResponseModel is a generic class that can encapsulate any data type T. This design allows for flexible API responses where the data attribute can be of any type, such as str, int, or even another model.

2. TypeVar with __bound__

Definition:
TypeVar is used to define a generic type variable. The bound parameter restricts the type variable to a specific base class or interface, ensuring that the type variable is a subtype of the specified bound.

Usage:
This feature is useful when you want to create functions or classes that operate on a specific subset of types that share a common interface or base class.

Example:
In the Django framework, TypeVar with bound is used to ensure type safety:

from typing import TypeVar

ModelType = TypeVar('ModelType', bound='Model')

def save_instance(instance: ModelType) -> None:
    instance.save()

Explanation:
Here, ModelType is a type variable bound to the Model class. The save_instance function accepts any instance of a subclass of Model, ensuring that the save method is available on the instance.

3. TypeVar with __constraints__

Definition:
TypeVar can also accept a list of types as constraints, meaning the type variable can be any one of the specified types.

Usage:
This is useful when a function or class should operate on a limited set of types, enforcing type safety by restricting the possible types that can be used.

Example:
In the Pandas library, TypeVar with constraints is used to define functions that operate on numeric types:

from typing import TypeVar

Number = TypeVar('Number', int, float)

def add(a: Number, b: Number) -> Number:
    return a + b

Explanation:
Here, Number is a type variable constrained to int and float. The add function can accept and return either of these types, ensuring that only numeric types are used.

4. TypeVarTuple

Definition:
TypeVarTuple is a feature introduced in Python 3.11 that allows the definition of variadic type variables. It enables the creation of generic classes and functions that can accept an arbitrary number of type parameters.

Usage:
This is particularly useful for defining functions or classes that need to handle a variable number of types, such as tuples of varying lengths.

Example:
In the TensorFlow library, TypeVarTuple is used to define layers that can accept multiple input types:

from typing import TypeVarTuple, Generic

Ts = TypeVarTuple('Ts')

class Layer(Generic[*Ts]):
    def __init__(self, *args: *Ts):
        self.args = args

Explanation:
Here, Layer is a generic class that can accept a variable number of type parameters, allowing for flexible layer configurations in neural networks.

5. ParamSpec

Definition:
ParamSpec is a feature introduced in Python 3.10 that allows the capture of callable parameter specifications. It enables the creation of higher-order functions that can accept and return functions with the same signature.

Usage:
This is useful for defining decorators or wrapper functions that need to preserve the signature of the functions they wrap.

Example:
In the FastAPI framework, ParamSpec is used to create decorators that maintain the original function’s signature:

from typing import Callable, ParamSpec, TypeVar

P = ParamSpec('P')
R = TypeVar('R')

def add_logging(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

Explanation:
Here, add_logging is a decorator that adds logging functionality to any function while preserving its original signature, thanks to ParamSpec.

6. TypeAliasType

Definition:
TypeAliasType is used to define type aliases, providing a way to create more readable and maintainable type annotations.

Usage:
This is useful when you have complex type annotations that are used multiple times, allowing you to define a simpler alias for them.

Example:
In the Mypy type checker, TypeAlias is used to define aliases for complex types:

from typing import TypeAlias

Vector: TypeAlias = list[float]

Explanation:
Here, Vector is defined as an alias for list[float], simplifying type annotations in mathematical computations.

These examples illustrate how advanced typing features in Python’s typing module are utilized across various projects to enhance type safety, code clarity, and developer productivity.




### Structural Subtyping with Protocol

TODO: WIP

**Purpose:** Implements static duck typing, allowing type checking based on attributes and methods instead of explicit inheritance.
**Use Case:** Defining interfaces for APIs or abstract behaviors.

Example:

```python
from typing import Protocol

class Serializable(Protocol):
    def serialize(self) -> str:
        ...
```

