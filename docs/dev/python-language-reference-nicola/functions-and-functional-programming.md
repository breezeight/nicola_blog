## Functions and Functional Programming

### Defining Functions
In Python, functions are defined using the `def` keyword followed by the function name, parentheses containing any parameters, and a colon. The function body is indented, and an optional `return` statement specifies the output.

```python
def greet(name):
    return f"Hello, {name}!"
```

The above defines a function `greet` that takes one argument, `name`, and returns a greeting string.

### Function Arguments: Positional, Keyword, Default, `*args`, `**kwargs`
Functions in Python can accept a variety of argument types to provide flexibility.

1. **Positional Arguments**  
   These are the most basic form of arguments. The values are passed in order, and the number of arguments must match the number of parameters.

   ```python
   def add(a, b):
       return a + b

   result = add(3, 5)  # Positional arguments: a = 3, b = 5
   ```

2. **Keyword Arguments**  
   You can specify arguments using their parameter names. This allows passing arguments in a different order.

   ```python
   result = add(b=5, a=3)  # Keyword arguments: a = 3, b = 5
   ```

3. **Default Arguments**  
   Parameters can have default values, which are used if no argument is provided.

   ```python
   def greet(name="World"):
       return f"Hello, {name}!"

   print(greet())       # Output: Hello, World!
   print(greet("Alice"))  # Output: Hello, Alice!
   ```

4. **Variable-Length Arguments (`*args` and `**kwargs`)**  
   - `*args` allows a function to accept any number of positional arguments, packed into a tuple.
   - `**kwargs` allows passing keyword arguments as a dictionary.

   ```python
   def summarize(*args, **kwargs):
       print("Positional arguments:", args)
       print("Keyword arguments:", kwargs)

   summarize(1, 2, 3, key1="value1", key2="value2")
   # Output:
   # Positional arguments: (1, 2, 3)
   # Keyword arguments: {'key1': 'value1', 'key2': 'value2'}
   ```

For details on arguments in methods, see [Classes and Objects - Method Definitions](#classes-and-objects-method-definitions).

### Anonymous Functions (`lambda`)
Lambda functions are small anonymous functions defined using the `lambda` keyword. They can have any number of arguments but only a single expression.

```python
square = lambda x: x ** 2
print(square(5))  # Output: 25
```

Lambdas are often used for short, throwaway functions or as arguments to higher-order functions like `map` or `filter`.

### Function Annotations
Python allows adding metadata to function parameters and return values through annotations. Annotations do not affect program behavior but can be used for type checking or documentation.

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

In this example, `name` is annotated as a `str`, and the function is expected to return a `str`.

### Decorators
Decorators are a powerful feature in Python for modifying the behavior of functions or methods. They are functions that take another function as an argument and extend its behavior without modifying the original function.

```python
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "Hello, world!"

print(greet())  # Output: HELLO, WORLD!
```

### Generators and Iterators
Generators provide a convenient way to create iterators using the `yield` keyword. They generate values on-the-fly and allow for lazy evaluation.

```python
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)
print(list(counter))  # Output: [1, 2, 3, 4, 5]
```

### Higher-Order Functions (e.g., `map`, `filter`, `reduce`)
Higher-order functions are functions that take other functions as arguments or return them as results.

1. **`map`**: Applies a function to each item of an iterable.
   
   ```python
   numbers = [1, 2, 3, 4]
   squares = map(lambda x: x ** 2, numbers)
   print(list(squares))  # Output: [1, 4, 9, 16]
   ```

2. **`filter`**: Filters items from an iterable based on a function that returns `True` or `False`.
   
   ```python
   evens = filter(lambda x: x % 2 == 0, numbers)
   print(list(evens))  # Output: [2, 4]
   ```

3. **`reduce`**: Applies a function of two arguments cumulatively to the items of an iterable (requires `functools`).
   
   ```python
   from functools import reduce
   product = reduce(lambda x, y: x * y, numbers)
   print(product)  # Output: 24
   ```

Use these functions to work with collections and apply functional programming concepts in Python.
