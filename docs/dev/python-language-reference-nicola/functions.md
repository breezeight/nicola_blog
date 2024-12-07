# Functions

[Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/)

## Defining functions and calling them

```python
# Use "def" to create new functions
def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y  # Return values with a return statement

# Calling functions with parameters
add(5, 6)  # => prints out "x is 5 and y is 6" and returns 11

# Another way to call functions is with keyword arguments
add(y=6, x=5)  # Keyword arguments can arrive in any order.
```

## Manage a variable number of arguments

* `args`: positional arguments
* `kwargs`: keyword arguments

```python
# You can define functions that take a variable number of
# positional arguments
def varargs(*args):
    return args

varargs(1, 2, 3)  # => (1, 2, 3)

# You can define functions that take a variable number of
# keyword arguments, as well
def keyword_args(**kwargs):
    return kwargs

# Let's call it to see what happens
keyword_args(big="foot", loch="ness")  # => {"big": "foot", "loch": "ness"}

# You can do both at once, if you like
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)
"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""
```

## Unpacking

In Python, **unpacking** refers to the process of assigning elements from:

* an **iterable** (like a list or tuple)
* or a **dictionary**

to multiple variables in a single statement. This technique enhances code readability and efficiency by allowing concise assignments and function calls.

### Unpacking Iterables

When you have an iterable (e.g., list or tuple), you can unpack its elements into variables directly:

```python
# Unpacking a tuple into variables
my_tuple = (1, 2, 3)

a, b, c = my_tuple

print(a)  # Outputs: 1

print(b)  # Outputs: 2

print(c)  # Outputs: 3
```

In this example, `a`, `b`, and `c` are assigned the values 1, 2, and 3 from `my_tuple`, respectively.

### Extended Unpacking with the `*` Operator

Python's extended unpacking allows capturing multiple elements into a list using the `*` operator:

```python
# Unpacking with the * operator
my_list = [1, 2, 3, 4, 5]
first, *middle, last = my_list

print(first)  # Outputs: 1
print(middle)  # Outputs: [2, 3, 4]
print(last)  # Outputs: 5
```

Here, `first` gets the value 1, `last` gets 5, and `middle` captures the remaining list `[2, 3, 4]`.

### Unpacking Dictionaries with the `**` Operator

For dictionaries, the `**` operator unpacks key-value pairs, which is particularly useful when merging dictionaries or passing keyword arguments:

```python
# Merging dictionaries using ** unpacking
dict1 = {'a': 1, 'b': 2}

dict2 = {'c': 3, 'd': 4}

merged_dict = {**dict1, **dict2}

print(merged_dict)  # Outputs: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

In this case, `merged_dict` combines the key-value pairs from both `dict1` and `dict2`.

### Unpacking in Function Calls

Unpacking is also beneficial when passing arguments to functions. The `*` operator unpacks iterables into positional arguments, and the `**` operator unpacks dictionaries into keyword arguments:

```python
def func(a, b, c):
    print(a, b, c)

args = (1, 2, 3)

kwargs = {'a': 1, 'b': 2, 'c': 3}

func(*args)  # Equivalent to func(1, 2, 3)

func(**kwargs)  # Equivalent to func(a=1, b=2, c=3)
```

Here, `func(*args)` unpacks the tuple `args` into positional arguments, while `func(**kwargs)` unpacks the dictionary `kwargs` into keyword arguments.

Understanding unpacking in Python allows for more flexible and readable code, especially when dealing with functions that accept varying numbers of arguments or when manipulating collections of data.

## Returning multiple values from a function

```python
# Returning multiple values (with tuple assignments)
def swap(x, y):
    return y, x  # Return multiple values as a tuple without the parenthesis.
                 # (Note: parenthesis have been excluded but can be included)

x = 1
y = 2
x, y = swap(x, y)     # => x = 2, y = 1
# (x, y) = swap(x,y)  # Again the use of parenthesis is optional.
```

## Python has first class functions

```python
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3)   # => 13
```

### Lambda - anonymous functions

In Python, lambda functions:
* are small, anonymous functions defined **without a name**.
* are created using the `lambda` keyword.
* can have any number of input parameters but only one expression.
* are often used for short, throwaway functions that are not intended to be reused elsewhere in the code.

Syntax of Lambda Functions:

```python
lambda arguments: expression
```

* `arguments`: A comma-separated list of input parameters.
* `expression`: An expression executed and returned when the lambda function is called.

As you see the evaluation of the lambda expression is a function that can be called with the given arguments:

```python
(lambda x: x > 2)(3)  # Outputs: True
```

#### Lambda usage examples

Lambda functions are often used as the key function in sorting operations.

```python
# List of tuples
data = [('apple', 3), ('banana', 2), ('cherry', 5)]

# Sort by the second element of each tuple
sorted_data = sorted(data, key=lambda item: item[1])
print(sorted_data)  # Outputs: [('banana', 2), ('apple', 3), ('cherry', 5)]
```
In this example, the lambda function lambda item: item[1] extracts the second element from each tuple, and sorted() uses this value to sort the list.

Other  examples:
```python
# There are built-in higher order functions
list(map(add_10, [1, 2, 3]))          # => [11, 12, 13]
list(map(max, [1, 2, 3], [4, 2, 1]))  # => [4, 2, 3]

list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))  # => [6, 7]

# We can use list comprehensions for nice maps and filters
# List comprehension stores the output as a list (which itself may be nested).
[add_10(i) for i in [1, 2, 3]]         # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]

# You can construct set and dict comprehensions as well.
{x for x in "abcddeef" if x not in "abc"}  # => {'d', 'e', 'f'}
{x: x**2 for x in range(5)}  # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Higher-Order Functions with Lambda

Python provides built-in higher-order functions like map(), filter(), and reduce() that can take lambda functions as arguments to process iterables in a concise way.
	•	map(function, iterable, ...): Applies the given function to all items in the provided iterable(s) and returns a map object (which can be converted into a list, set, etc.).

# Using map to add 10 to each element in the list
print(list(map(lambda x: x + 10, [1, 2, 3])))  # Outputs: [11, 12, 13]

# Using map to find the maximum between elements of two lists
print(list(map(lambda x, y: max(x, y), [1, 2, 3], [4, 2, 1])))  # Outputs: [4, 2, 3]


	•	filter(function, iterable): Constructs an iterator from elements of the iterable for which the function returns True.

# Using filter to get elements greater than 5
print(list(filter(lambda x: x > 5, [3, 4, 5, 6, 7])))  # Outputs: [6, 7]



List Comprehensions:

List comprehensions provide a concise way to create lists. They consist of brackets containing an expression followed by a for clause, and can include multiple for or if clauses.

# Using list comprehension to add 10 to each element
print([x + 10 for x in [1, 2, 3]])  # Outputs: [11, 12, 13]

# Using list comprehension to filter elements greater than 5
print([x for x in [3, 4, 5, 6, 7] if x > 5])  # Outputs: [6, 7]

Set and Dictionary Comprehensions:

Similar to list comprehensions, Python supports set and dictionary comprehensions for creating sets and dictionaries in a concise way.

# Set comprehension to get unique characters not in 'abc'
print({x for x in "abcddeef" if x not in "abc"})  # Outputs: {'d', 'e', 'f'}

# Dictionary comprehension to map numbers to their squares
print({x: x**2 for x in range(5)})  # Outputs: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

Key Points:
	•	Lambda Functions: Useful for creating small, unnamed functions on the fly.
	•	Higher-Order Functions: Functions like map() and filter() can take other functions (including lambdas) as arguments to process iterables.
	•	Comprehensions: List, set, and dictionary comprehensions provide a concise and readable way to create new collections by transforming and filtering elements from existing iterables.

By combining lambda functions with higher-order functions and comprehensions, Python allows for writing clean and efficient code for data processing tasks.




## Variable Scope in Python

- **Global Scope**: Variables defined outside of any function are in the global scope. They can be accessed from any part of the code, including within functions.
- **Local Scope**: Variables defined within a function are in the local scope of that function. They can only be accessed within that function and are not visible outside of it.

### global scope and `global` keyword

In Python, understanding variable scope and the use of the global keyword is essential for managing how variables are accessed and modified within different parts of a program.

By default, variables assigned within a function are treated as local to that function. To modify a global variable inside a function, you must declare it as global using the global keyword. This tells Python that the variable refers to the globally scoped variable, not a new local one.

> [!NOTE] `global` is only necessary when you need to reassign such variables within the inner function not when you are just reading them. See the exaple in [Python has first class functions](#python-has-first-class-functions)


```python
x = 5  # Global variable

def read_x():
    print(x)  # Accesses the global 'x' without the global keyword. Global is relevant only when reassigning such variables within the inner function.

def set_x(num):
    x = num  # This creates a new local variable 'x'
    print(x)  # Prints the local 'x'

def set_global_x(num):
    global x  # Declares that we are using the global 'x'
    print(x)  # Accesses the global 'x'
    x = num   # Modifies the global 'x'
    print(x)  # Prints the modified global 'x'

read_x()  # => prints 5
set_x(43) # => prints 43
set_global_x(6) # => first prints 5, then prints 6

read_x()  # => prints 6 because the global x was modified by set_global_x
print(x)  # => prints 6 because the global x was modified by set_global_x
```

Explanation:

1. **Global Variable** x: Initially, x is set to 5 in the global scope.

2. `set_x` function:

- Assigning `x = num` creates a new local variable `x` within the function's scope.
- This local `x` shadows the global `x` within the function.
- The global `x` remains unchanged after the function executes.

3. `set_global_x` function:

- The global `x` declaration tells Python to use the global `x` variable.
- The function first prints the current value of the global `x`.
- It then modifies the global `x` to the new value `num`.

- Finally, it prints the updated value of the global `x`.

4. **Final Print Statement**:

- After calling `set_global_x`, the global `x` has been updated to 6.
- The final print statement confirms this change.

**Key Points:**

- Without the global keyword, assigning a value to a variable inside a function creates a new local variable, leaving the global variable unchanged.
- Using the global keyword allows a function to modify a variable that exists in the global scope.
- It's generally advisable to minimize the use of global variables to maintain clear and predictable code behavior.

For more detailed information on Python's variable scope and the global keyword, refer to the [official Python documentation](https://docs.python.org/3/reference/simple_stmts.html#the-global-statement).


## Closures in nested functions
In Python, closures are a powerful feature that allows inner functions to capture and remember variables from their enclosing scopes, even after those scopes have finished execution. This capability is particularly useful for creating functions with persistent states or for data encapsulation.

### Understanding Closures with Nested Functions

In Python, the `nonlocal` keyword is used within nested functions to indicate that a variable refers to one in the nearest enclosing scope that is not global. This allows the inner function to modify variables from its enclosing function. 

However, `nonlocal`, like `global`, is only necessary when you need to reassign such variables within the inner function not when you are just reading them.

### The `nonlocal` Keyword

In Python, the `nonlocal` keyword is used within a nested function to indicate that a variable refers to a previously bound variable in the nearest enclosing scope that is not global. This allows the inner function to modify variables in the outer function’s scope.

Example: Creating an Averaging Function Using a Closure: 

```python
def create_avg():
    total = 0
    count = 0
    def avg(n):
        nonlocal total, count
        total += n
        count += 1
        return total / count
    return avg

avg = create_avg()
avg(3)  # => 3.0
avg(5)  # (3+5)/2 => 4.0
avg(7)  # (8+7)/3 => 5.0
```

Explanation:
1. Outer Function (create_avg):
- Initializes `total` and `count` to zero.
- Defines the inner function `avg(n)`.

2. Inner Function (avg):
- Uses the `nonlocal` keyword to indicate that `total` and `count` are not local to `avg` but are in the nearest enclosing scope (`create_avg`).
- Updates `total` and `count` with the new value `n`.
- Calculates and returns the average.

3. Closure Creation:
- `create_avg()` returns the inner function `avg`, which retains access to `total` and `count` from its enclosing scope.
- Assigning `avg = create_avg()` creates a closure where `avg` has access to `total` and `count` even after `create_avg` has finished execution.

4. Using the Closure:
- Each call to `avg(n)` updates `total` and `count`, and computes the new average.
- The state (`total` and `count`) is preserved across calls, demonstrating the closure’s ability to maintain state.

Benefits of Using Closures:
- Data Encapsulation: Closures allow for encapsulating data within a function, providing a way to hide variables from the global scope.
- Stateful Functions: They enable the creation of functions that maintain state between calls without relying on global variables or class instances.
- Functional Programming: Closures support functional programming paradigms by allowing functions to be treated as first-class citizens with preserved environments.

Key Points:
- The `nonlocal` keyword is essential for modifying variables in the nearest enclosing scope that is not global. Without `nonlocal`, assigning to a variable inside a nested function would create a new local variable, leaving the outer variable unchanged.
- Closures capture variables by reference, not by value. This means they reflect the most recent value of the captured variables.
- Proper use of closures can lead to more concise and expressive code, especially when functions need to maintain state or when implementing decorators and factory functions.




