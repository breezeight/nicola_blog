# Decorators
Decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. 

Decorators are basically a syntax sugar that make **easy to define** functions that make **easy to use** functions. What it means is that we can pass functions as arguments to other functions. In a Decorator we actually override the callable with a new callable.

Decorators are usually associated with the definition of a function you want to decorate.

```python
@my_decorator
def function():
    pass
```

This is equivalent to:

```python
def function():
    pass

function = my_decorator(function)
```

Decorators are one of the most useful and heavily utilised feature of python. May it be libraries or the API which you are developing currently. They can be found anywhere and everywhere.

Few of the most used decorators used include `@staticmethod`, `@classmethod` and `@property`.

To understand decorators, you need this prerequisite knowledge:

- Functions in Python are [first class citizens](https://en.wikipedia.org/wiki/First-class_citizen). This means that they support operations such as being passed as an argument, returned from a function, modified, and assigned to a variable. This property is crucial as it allows functions to be treated like any other object in Python, enabling greater flexibility in programming. [Learn more about first class functions](functions.md#python-has-first-class-functions)

- [Variable Scope in Python](functions.md#variable-scope-in-python)
- [Closures in Python](functions.md#closures-in-nested-functions)

With this knowledge, you are ready to understand decorators see [here](https://www.datacamp.com/tutorial/decorators-python)

DEFINITION: A **function-based decorator** is a function that takes another function or class as an argument, adds some functionality, and returns the modified function or class. let's see how this works.

> [!NOTE]
> This explanation is based on the following resources:
> - [PEP 318 -- Decorators for Functions and Methods](https://www.python.org/dev/peps/pep-0318/)
> - [article - Under the hood with Python Decorators](https://medium.com/@sandeephukku/python-decorators-a82db70e677e)
> - [article - Learn Decorators in Python](https://pythonbasics.org/decorators/)
> - [article - Python Decorators](https://www.datacamp.com/tutorial/decorators-python)
> - [video - Decorators in Python](https://www.youtube.com/watch?v=FXUUSfJO_J4)
> - [videoPython Decorators in 1 Minute](https://www.youtube.com/watch?v=BE-L7xu8pO4)

## Implementing a Function-Based Decorator

Now hopping on to the implementation of a very basic decorator.

```python
print("1. Decorator implementation")
def decorator(callable_func):   # (1)
    def inner():
        # Additional behavior (e.g., logging, validation) (2)
        print("2. Inside the decorator inner function")
        callable_func()         # Call the original function (3)
    print("5. Inside the decorator definition")  # (5)
    print(f"5. id(inner): {id(inner)}")
    return inner

print("4. Applying decorator to function definition")
@decorator # (4)
def test():
    print("7. Hello Inside the test function") # (7)

print("6. Decorated function usage")
test()  # (6)
```

If you run the code above, you will get:

```bash
1. Decorator implementation
4. Applying decorator to function definition
5. Inside the decorator definition
5. id(inner): 4298448448
6. Decorated function usage"
2. Inside the decorator inner function
7. Hello Inside the test function
```

It's important to notice that the `test` function is now overridden with the `inner` function.

Explanation:

1.	Defining the Decorator:
    - The decorator function is defined to accept a callable (`callable_func`) as its argument. This function will wrap the target function to enhance or modify its behavior.
2.	Inner Function. Within decorator, the inner function is defined. This function:
    - Executes additional behavior (e.g., logging, authentication) before calling the original function.
3.	Calling the Original Function:
    - Inside inner, `callable_func()` is invoked to ensure the original function’s behavior is executed.
4. Applying the Decorator:
    - When interpreter encounters the `@decorator` line, the decorator function is called with `test` function as its argument.
5.	Decorator Execution:
    - The decorator function returns the inner function, which replaces the original `test` function.
    - When you use the `@decorator` syntax above a function definition, the decorator function is applied immediately during the function’s definition, not at runtime when the function is called. This means that the decorator function is executed, and it returns a new function that replaces the original one in the current namespace.
6.	Using the decorated function:
    - Calling `test()` now executes the inner function, which includes the additional behavior and then calls the original `test` function.

The final result is that the **`test` function is overridden with the `inner` function**: when `test()` is called, the interpreter executes the `inner` function instead.

The `@decorator` syntax is syntactic sugar for applying a decorator to a function:

```python
@decorator
def test():
    print("Hello Inside the test function")
```

Is equivalent to:

```python
def test():
    print("Hello Inside the test function")

test = decorator(test)
```

In both cases, the test function is passed to the decorator function, and the result is assigned back to test. This means that test now refers to the function returned by decorator.


> [!KEY POINTS]
> - The decorator is initialised not at the run time but at the compile time and the decorator is executed when the function is defined, not when it is called.
> - Decorators are applied to functions using the `@decorator` syntax.
> - The function returned by the decorator is assigned back to the original function. This means that the original function is **overridden** (**replaced**) by the function returned by the decorator.

## Manage Arguments

### Arguments for the Decorated Function

How do we pass positional and keyword arguments to the decorated function? It's quite simple:
- we add the `*args` and `**kwargs` syntax to the `inner` function.
- we pass the `*args` and `**kwargs` to the decorated function as they are provided to the `inner` function.

```python
def decorator(callable_func):
    def inner(*args, **kwargs):         #------> 1
        #do something 
        print ("Decorator was called")
        callable_func(*args, **kwargs)  #------> 2
    return inner
@decorator
def test(a, b, optional_message="Hello"):
    print(optional_message)
    print(f"{a} + {b} = {a + b}")
```

Result:

```bash
>>> test(2,5, optional_message="Ciao!")
Decorator was called
Ciao!
2 + 5 = 7
```
What happens in the new implementation is that the inner function has started taking the arguments, which can then be passed to the `callable_func` (the original function that is being decorated-overridden).

The basic working concept for the new implementation remains the same as the previous one.


### Arguments for Decorators - Decorator Factory

In Python, decorators are a powerful feature that allows you to modify the behavior of functions or classes. When you need a decorator that accepts its own arguments, you can achieve this by defining a decorator factory — a function that returns a decorator. This approach enables you to pass arguments to the decorator itself, which can then influence its behavior.


Let’s create a decorator that adds a custom message before calling the original function. The message will be specified as an argument to the decorator.

```python
def add_message_from(name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{name} picked some items.")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@add_message_from("Zeek")
def prettify(msg):
    print(msg)

prettify("flowers for you")  # Output: Zeek picked some items.
```

This is equivalent to:

```python
prettify = add_message_from(name)(prettify) 
```

Here’s a step-by-step breakdown of how this works:

1.	Decorator Factory Call: `add_message_from("Zeek")` is executed first. This call returns the actual decorator function, which we’ll refer to as `decorator`.
2.	Decorator Application: The returned decorator function is then called with the original `prettify` function as its argument: `decorator(prettify)`. This call returns the `wrapper` function.
3.	Function Reassignment: The `prettify` name is then reassigned to refer to this `wrapper` function: `prettify = wrapper`.

Therefore, using the @add_message_from("Zeek") syntax is a concise and readable way to achieve the same result as the more verbose assignment statement.


## Decorating Classes

There are two different ways that you can use decorators on classes:

1. The first one is very close to what you've already done with functions: you can **decorate the methods of a class**. This was [one of the motivations](https://www.python.org/dev/peps/pep-0318/#motivation) for introducing decorators back in the day.
2. The second one is to decorate the class definition itself.

### Decorating Class Methods using function-based decorators

Some commonly used decorators are even built-ins in Python:
- [`@classmethod`, `@staticmethod`](https://realpython.com/instance-class-and-static-methods-demystified/), 
- [`@property`](https://realpython.com/python-property/). 

The `@classmethod` and `@staticmethod` decorators are used to define methods inside a class [namespace](https://realpython.com/python-namespaces-scope/) that aren't connected to a particular instance of that class. The `@property` decorator is used to customize [getters and setters](https://realpython.com/python-getter-setter/) for [class attributes](https://realpython.com/python-classes/#class-attributes). Expand the box below for an example using these decorators:

Example using built-in class decorators: The following definition of a Circle class uses the `@classmethod`, `@staticmethod`, and `@property` decorators:

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        """Get value of radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("radius must be non-negative")

    @property
    def area(self):
        """Calculate area inside circle"""
        return self.pi() * self.radius**2

    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)

    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535
```

Inside Circle you can see several different kinds of methods. Decorators are used to distinguish them:

- `.cylinder_volume()` is a regular method.
- `.radius` is a mutable property. It can be set to a different value. However, by defining a setter method, you do some error testing to make sure `.radius` isn’t set to a nonsensical negative number. Properties are accessed as attributes without parentheses.
- `.area` is an immutable property. Properties without `.setter()` methods can’t be changed. Even though it’s defined as a method, it can be retrieved as an attribute without parentheses.
- `.unit_circle()` is a class method. It’s not bound to one particular instance of Circle. Class methods are often used as factory methods that can create specific instances of the class.
- `.pi()` is a static method. It’s not really dependent on the Circle class, except that it’s part of its namespace. You can call static methods on either an instance or the class.

You can use Circle as follows:

```python
>>> from circle import Circle

>>> c = Circle(5)
>>> c.radius
5

>>> c.area
78.5398163375

>>> c.radius = 2
>>> c.area
12.566370614

>>> c.area = 100
Traceback (most recent call last):
    ...
AttributeError: can't set attribute

>>> c.cylinder_volume(height=4)
50.265482456

>>> c.radius = -1
Traceback (most recent call last):
    ...
ValueError: radius must be non-negative

>>> c = Circle.unit_circle()
>>> c.radius
1

>>> c.pi()
3.1415926535

>>> Circle.pi()
3.1415926535
```

You can also decorate some of its methods using a `@timer` decorator that you define:

```python
import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value
    return wrapper_timer

class Circle:
    ...

    @timer
    def area(self):
        return self.pi() * self.radius**2
```


### Decorating Class using function-based decorators

A function-based decorator is a function that takes another function or class as an argument, adds some functionality, and returns the modified function or class.

When you use the the `@decorator` syntax on a **class**, the decorator:
-  will receive a class and not a function as an argument and
-  will return a class.

Example:

```python
def add_method(cls):
    def new_method(self):
        return "This is a new method added to the class."
    cls.new_method = new_method
    return cls

@add_method
class MyClass:
    def original_method(self):
        return "This is the original method."

# Usage
obj = MyClass()
print(obj.original_method())  # Output: This is the original method.
print(obj.new_method())       # Output: This is a new method added to the class.
```

In fact, all the decorators that you saw above will work as class decorators. When you’re using them on a class instead of a function, their effect might not be what you want. In the following example, the @timer decorator is applied to a class:

```python
from decorators import timer

@timer
class TimeWaster:
    def __init__(self, max_num):
        self.max_num = max_num

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])
```

Decorating a class doesn’t decorate its methods. Recall that `@timer` is just shorthand for `TimeWaster = timer(TimeWaster)`. Here, `@timer` only measures the time that it takes to instantiate the class:

```bash
>>> from class_decorators import TimeWaster

>>> tw = TimeWaster(1000)
Finished TimeWaster() in 0.0000 secs

>>> tw.waste_time(999)
```

The output from `@timer` is only shown as `tw` is created. The call to `.waste_time()` isn’t timed.


### Decorating Class using class-based decorators

Class-Based Decorators Applied to Classes

A class-based decorator involves defining a class with a __call__ method, allowing its instances to be used as decorators. This approach is beneficial when the decoration requires maintaining state or involves complex behavior.

Example:

```python
class AddMethodDecorator:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self):
        class WrappedClass(self.cls):
            def new_method(self):
                return "This is a new method added to the class."
        return WrappedClass

@AddMethodDecorator
class MyClass:
    def original_method(self):
        return "This is the original method."

# Usage
obj = MyClass()
print(obj.original_method())  # Output: This is the original method.
print(obj.new_method())       # Output: This is a new method added to the class.
```

Explanation:

* The AddMethodDecorator class is initialized with the class `cls` to be decorated.
* The `__call__` method defines a new class `WrappedClass` that inherits from `cls` and adds the `new_method`.
* Applying `@AddMethodDecorator` to `MyClass` replaces `MyClass` with `WrappedClass`, which includes the `new_method`.

### Key Differences

- State Management: Class-based decorators can maintain state across multiple calls using instance attributes, making them suitable for scenarios where the decorator needs to keep track of information between function calls.
- Complexity: Function-based decorators are simpler and more concise, ideal for straightforward modifications. Class-based decorators provide better organization and flexibility for more complex behavior.
- Readability: Function-based decorators are generally easier to read and understand, while class-based decorators can encapsulate more intricate logic, enhancing code maintainability.

### Real-World Examples from Existing Libraries

- Function-Based Decorator: The **dataclasses module in Python's standard library** uses the `@dataclass` decorator to automatically generate special methods like `__init__()` and `__repr__()` for user-defined classes. This decorator is function-based and simplifies class definitions by reducing boilerplate code.

- Class-Based Decorator: The **contextlib module** provides the `@contextmanager` decorator, which allows a function to be used in a `with` statement. This decorator is implemented as a class that defines the `__call__` method, enabling it to manage resources efficiently. See also [Context Managers in Python](context-managers.md).

## Order of Multiple Decorators

When you apply multiple decorators to a single function, the order in which you apply them matters. Decorators are applied from the innermost to the outermost. Consider this when designing your decorators, as changing the order can lead to different behavior.

```python
def decorator_1(func):
    def wrapper():
        print("Decorator 1: Before")
        func()
        print("Decorator 1: After")
    return wrapper

def decorator_2(func):
    def wrapper():
        print("Decorator 2: Before")
        func()
        print("Decorator 2: After")
    return wrapper

@decorator_1
@decorator_2
def my_function():
    print("Original function")

my_function()
# Output:
# Decorator 1: Before
# Decorator 2: Before
# Original function
# Decorator 2: After
# Decorator 1: After
```

In this example, decorator_1 is applied first, followed by decorator_2.

## Use `functools.wraps` to Preserve Metadata

When you create a decorator, it's essential to preserve the metadata (e.g., function name, docstring, and arguments) of the original function. You can achieve this by using the functools.wraps decorator, which is provided by Python's functools module.

```python
import functools

def my_decorator(func):
    @functools.wraps(func)  # Use functools.wraps to preserve metadata
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    """This function says hello."""
    print("Hello!")

print(say_hello.__name__)  # Outputs: "say_hello"
print(say_hello.__doc__)   # Outputs: "This function says hello."
```

By using `functools.wraps`, you ensure that the decorated function retains its original identity and documentation, making it easier to understand and debug your code.

## Practical Example


- [Get the Execution Time of a Function](https://www.freecodecamp.org/news/the-python-decorator-handbook/#heading-get-the-execution-time-of-a-function)



## TODO under the hood of Static Method decorator

What is a Static Method?

https://data-ai.theodo.com/blog-technique/re-code-staticmethod-decorator