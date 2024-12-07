# Control Flow

## if Statements

The [Real Python article on Python Conditional Statements](https://realpython.com/python-conditional-statements/) covers:
- `if` Statements: Conditional execution based on true expressions.
- Indentation and Blocks: Code grouping defined by indentation.
- `else` and `elif` Clauses: Alternatives and multiple conditions.
- One-Line if Statements - ternary operators: For simple conditions.
- Conditional Expressions: Inline evaluation with ternary operators `s = 'minor' if age < 21 else 'adult'`.
- `pass` Statement: Placeholder for empty blocks.

> [!NOTE] This is a good resource for people who want to learn about conditional statements in general. It explain the general concept of conditional statements and how they work in Python.

## Python does not have a `switch` statement


[Alternative to Switch Case Statement in Python](https://www.guru99.com/if-loop-python-conditional-structures.html):

1. Dictionary based alternative to switch case statement.
```python
def SwitchExample(argument):
    switcher = {
        0: " This is Case Zero ",
        1: " This is Case One ",
        2: " This is Case Two ",
    }
    return switcher.get(argument, "nothing")
```

2. `match` statement (see below). Available from Python 3.10.

## Match Statement

[Python Switch Case Statement](https://www.datacamp.com/tutorial/python-switch-case)
- Note: this site has AI integrated to explain the code.

[Real Python: Structural Pattern Matching](https://realpython.com/structural-pattern-matching/)

Basic example:
```python
# Take user input for the day of the week
day = input("Enter the day of the week: ").capitalize()

# Match the day to predefined patterns
match day:
    case "Saturday" | "Sunday":
        print(f"{day} is a weekend.")  # Match weekends
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print(f"{day} is a weekday.")  # Match weekdays
    case _:
        print("That's not a valid day of the week.")  # Default case
```


### Pattern Matching

#### Simple constant matching

API status codes handling:
```python
# Example: API response status code handling
status_code = 200

match status_code:
    case 200:
        print("Request succeeded.")
    case 404:
        print("Resource not found.")
    case 500:
        print("Server error. Please try again later.")
    case _:
        print("Unknown status code.")
```

#### Complex pattern matching

When working with structured data (e.g., dictionaries, sequences), match-case can extract and manipulate data efficiently.

```python
config = {"type": "database", "name": "PostgreSQL", "version": 13}

match config:
    case {"type": "database", "name": name, "version": version}:
        print(f"Database: {name} (Version {version})")
    case {"type": "cache", "name": name}:
        print(f"Cache system: {name}")
    case _:
        print("Unknown configuration.")
```

Explanation:

-   The first `case` extracts `name` and `version` from the dictionary, making it easier to work with structured data.
-   This showcases the true power of Python's structural pattern matching, far beyond what traditional switch-case implementations can achieve.

#### Guarded Patterns

A guard is a condition specified after case that further refines when a case should match. For example:

```python
match value:
    case x if x > 10:
        print("Value is greater than 10.")
```

#### Advanced Pattern Matching


https://realpython.com/structural-pattern-matching/#digging-into-more-advanced-structural-patterns
