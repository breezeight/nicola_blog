# Exception Handling

Python exceptions are events that occur during the execution of a program and disrupt the normal flow of the program’s instructions. When an exception is raised, it indicates that an error has occurred. Python provides a way to handle these exceptions using try-except blocks, allowing developers to manage errors gracefully and ensure the program can continue or exit smoothly.

Resources:
- [official: Exceptions Documentation](https://docs.python.org/3/tutorial/errors.html#exceptions)
- [article: Python Exceptions: An Introduction](https://realpython.com/python-exceptions/)
- [article: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [article: Python Exception Handling](https://www.programiz.com/python-programming/exception-handling)
- [video: Exception Handling in Python](https://www.youtube.com/watch?v=V_NXT2-QIlE)

## Syntax Errors are not exceptions

Before learning about exceptions, it's important to understand the difference between syntax errors and exceptions.

Syntax errors, also known as parsing errors, occur when the Python interpreter encounters code that doesn’t conform to the language’s grammatical rules. These errors are detected during the parsing stage, before the code is executed. Common causes include missing colons, unmatched parentheses, or incorrect indentation.

```python
if True
    print("Hello, World!")
```

In this example, the `if` statement lacks a colon at the end, leading to a `SyntaxError`.

Key Differences:

- **Detection Time**: Syntax errors are identified before execution, during the parsing phase. Exceptions are identified during execution.
- **Handling Mechanism**: Syntax errors must be corrected in the code for successful execution. Exceptions can be caught and handled using try and except blocks.
- **Nature**: Syntax errors result from incorrect code structure. Exceptions arise from issues during program execution, even if the code structure is correct.

## Raising Exceptions

To raise an exception, you can use the `raise` keyword followed by an instance of an exception class:

```python
raise Exception(f"The number should not exceed 5. ({number=})")
```

## Handling Exceptions With the try and except Block

https://realpython.com/python-exceptions/#handling-exceptions-with-the-try-and-except-block

In Python, you use the try and except block to catch and handle exceptions. Python executes code following the try statement as a normal part of the program. 
The following all the possible syntax of try and except block:

```python
# Handle exceptions with a try/except block
try:
    # Use "raise" to raise an error
    raise IndexError("This is an index error")
except IndexError as e:
    .....                 
except (TypeError, NameError): # Multiple exceptions can be processed jointly.
    ....                 
else:                    # Optional clause to the try/except block. Must follow
                         # all except blocks.
    print("All good!")   # Runs only if the code in try raises no exceptions
finally:                 # Execute under all circumstances
    print("We can clean up resources here")
```

Now let's go through each:

### Basic Syntax of try and except

```python
try:
    # Code that might raise an exception
    risky_operation()
except ExceptionType:
    # Code to execute if the exception occurs
    log_error("an error occurred")
```

The above is the most naive way to handle exceptions: you catch an exception and log an error message. Generally, you should do more than just logging and be more specific about the type of exception you are catching.

### Catch Specific Exceptions - Best Practice

Catch Specific Exceptions: Always aim to catch specific exceptions rather than using a bare except: clause. This practice prevents unintended exception handling and makes debugging easier.

```python
try:
    risky_operation()
except (TypeError, ValueError) as e:
    handle_exception(e)
```

### Refrain from silent exception handling - Best Practice

Refrain from silent exception handling. For example in the example below, the exception is caught but nothing is done about it. This can mask actual issues and make debugging more difficult, because you might not notice that an exception is being raised.

```python
try:
    risky_operation()
except Exception as e:
    pass
```

### `finally` clause

The `finally` clause: Executes regardless of whether an exception occurred or not, often used for cleanup actions.

```python
try:
    resource = acquire_resource()
except ExceptionType:
    handle_exception()
else:
    print("Operation succeeded.")
finally:
    release_resource()
```

## `with`: predefined cleanup actions

Combining the usage of `with` with exception handling is a good practice. Basically, `with` is used automatically to clean up resources that could be left open otherwise. It will save from writing a lot of boilerplate code.

For example, when you open a file, you can use `with` to ensure that it is properly closed after the code that uses the file has finished executing, **even if an exception is raised**.

Let's consider a scenario where a file is successfully opened, but an error occurs during the reading process, such as encountering unexpected data that leads to a `ValueError`. By combining the `with` statement with `try` and `except` blocks, we can handle such exceptions gracefully while ensuring that the file is properly closed:

```python
try:
    with open("data.txt", "r") as file:
        for line in file:
            # Attempt to convert each line to an integer
            number = int(line.strip())
            print(f"Read number: {number}")

except ValueError as e:
    print(f"ValueError occurred: {e}")

except IOError as e:
    print(f"I/O error occurred: {e}")
```

**Scenario:**

Suppose `data.txt` contains the following lines:

```
123
456
abc
789
```

When running the above code, the program will:

1. Successfully read and convert `123` and `456` to integers.
2. Encounter a `ValueError` when attempting to convert `abc` to an integer.
3. The `except ValueError` block catches the exception and prints:

```
ValueError occurred: invalid literal for int() with base 10: 'abc'
```

4. The program continues to execute, and **the file is properly closed** due to the `with` statement.

**Key Points:**

- The with statement ensures that the file is closed after the block is executed, even if an exception occurs.
- The try and except blocks allow for specific handling of different exceptions, providing informative error messages and preventing the program from crashing.
- By handling exceptions appropriately, the program can manage unexpected data gracefully and maintain robustness.

By implementing such practices, you can ensure that your programs handle errors effectively while maintaining proper resource management.

## Choosing Exception Classes

Picking the right exception type can sometimes be tricky.

Python comes with [many built-in exceptions](https://docs.python.org/3/library/exceptions.html#concrete-exceptions) that are [hierarchically related](https://docs.python.org/3/library/exceptions.html#exception-hierarchy), so if you browse the documentation, you're likely to find a fitting one.

Python even groups some of the exceptions into categories, such as [warnings](https://docs.python.org/3/library/exceptions.html#warnings) that you should use to indicate warning conditions, and [OS exceptions](https://docs.python.org/3/library/exceptions.html#os-exceptions) that Python raises depending on system error codes.

If you still didn't find a fitting exception, then you can [create a custom exception](https://realpython.com/python-exceptions/#creating-custom-exceptions-in-python).