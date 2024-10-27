## Data Types and Literals



### Built-in Types Overview
Python provides a rich set of built-in data types to accommodate various data-handling needs. The main categories include:
- **Numeric Types**: For representing numbers (integers, floating-point, complex).
- **Sequence Types**: Such as strings, lists, tuples, and ranges.
- **Mapping Types**: Dictionaries for key-value associations.
- **Set Types**: For handling collections of unique items.
- **Boolean Type**: Represents truth values.
- **Special Type**: `NoneType` to represent the absence of a value.

#### Boolean (`bool`)
Represents truth values: `True` or `False`. Can be used in logical operations and conditions.

```python
is_active = True
is_empty = not is_active  # False
```

#### `NoneType`
Represents a null or "no value" state. Commonly used as a default parameter value in functions. The `None` object is the sole instance of this type.

```python
result = None
if result is None:
    print("No result available")
```

#### Integers (`int`)
Represents whole numbers without a fractional component. Supports operations like addition, subtraction, multiplication, division, and modulo. Python allows large integers, limited only by available memory.

```python
a = 42
b = -7
c = 0
d = 1_000_000  # Underscores for readability
```

#### Floating-Point Numbers (`float`)
Represents real numbers with a fractional part, using double-precision (64-bit) format. Supports arithmetic operations and rounding functions.

```python
pi = 3.14159
x = 1.0e-3  # Scientific notation
```

#### Complex Numbers (`complex`)
Contains a real and an imaginary part, denoted as `a + bj`. Useful in scientific computing for operations involving imaginary numbers.

```python
z = 2 + 3j
w = complex(5, -1)
```

### Sequence Types

#### Strings (`str`)
Immutable sequences of characters enclosed in single, double, or triple quotes. Supports concatenation, slicing, and built-in methods like `upper()`, `find()`, and `replace()`. Can use formatted string literals (f-strings) for interpolation.

```python
greeting = "Hello, World!"
name = "Alice"
message = f"Welcome, {name}!"
```

#### Lists (`list`)
Lists in Python are mutable sequences that allow for flexible data handling. They support various operations such as appending, accessing, slicing, and modifying elements.

##### Creating Lists
Lists can be initialized as empty or pre-filled with values.
```python
li = []  # Empty list
other_li = [4, 5, 6]  # Prefilled list
```

##### Adding and Removing Elements
- **Appending Elements**: Use `append()` to add items to the end of the list.
```python
li.append(1)  # li is now [1]
li.append(2)  # li is now [1, 2]
li.append(4)  # li is now [1, 2, 4]
li.append(3)  # li is now [1, 2, 4, 3]
```

- **Removing Elements**: Use `pop()` to remove the last element and `remove()` to delete the first occurrence of a specific value.
```python
li.pop()  # => 3, li is now [1, 2, 4]
li.append(3)  # Restore the list to [1, 2, 4, 3]
li.remove(2)  # li is now [1, 4, 3]
```

- **Deleting Elements by Index**: Use `del` to remove an item at a specific index.
```python
del li[2]  # li is now [1, 4]
```

##### Accessing Elements
Lists can be accessed using zero-based indexing and negative indexing for reverse access, like you would with any array.
```python
first = li[0]  # => 1
last = li[-1]  # => 4
```

**Out-of-Bounds Access**: Accessing an index that doesn't exist raises an `IndexError`.
```python
li[4]  # Raises an IndexError
```

##### Finding Elements

**Get the Index of an Element**: Use `index()` to find the index of the first occurrence of a value in the list. If the value is not found, it raises a `ValueError`.

```python
li = [1, 2, 3, 2, 4]
idx = li.index(2)  # => 1 (first occurrence of 2)

# If the element is not present, a ValueError is raised.
li.index(5)  # Raises ValueError: 5 is not in list
```

##### Slicing
Slicing extracts a portion of a list using the syntax `list[start:end:step]`.
```python
li = [1, 2, 3, 4]
sublist = li[1:3]  # [2, 3]
li[2:]     # [3, 4] # From index 2 to the end
li[:3]     # [1, 2, 3] # Up to index 3
li[::2]    # [1, 3] # Every second element
li[::-1]   # [4, 3, 2, 1] # Reversed list
```

##### Copying Lists
Use slicing or the `copy()` method to create a shallow copy.
```python
li2 = li[:]  # li2 is a copy of li
li2 is li  # False
```

Using `copy()`:
```python
li2 = li.copy()
li2 is li  # False
```

##### Inserting Elements
Use `insert()` to add an element at a specific index, the first argument is the index, the second is the value:

```python
li = [1, 4]
li.insert(1, 2)  # li is now [1, 2, 4]
```

##### Combining Lists with `+`
- **Concatenating Lists**: Use the `+` operator to concatenate two lists, creating a new list without modifying the original lists.
  ```python
  li = [1, 2, 3]
  other_li = [4, 5, 6]
  combined = li + other_li  # => [1, 2, 3, 4, 5, 6]
  
  # The original lists remain unchanged
  print(li)  # Output: [1, 2, 3]
  print(other_li)  # Output: [4, 5, 6]

  # The combined list is a new copy
  print(combined is li)  # Output: False
  print(combined is other_li)  # Output: False
  ```

The resulting list is a new list that contains references to the elements from the original lists. This means that `combined` is a separate list stored in a different memory location than `li` or `other_li`.

- **Behavior with Non-Basic Types**:
  If the lists being concatenated contain mutable objects (such as other lists, dictionaries, or custom objects), the new list will contain references to the original objects rather than creating deep copies of them. As a result, modifications to the original elements will be reflected in the new concatenated list.

  ```python
  li = [[1, 2], [3, 4]]
  other_li = [[5, 6]]

  # Concatenating the lists
  combined = li + other_li  # => [[1, 2], [3, 4], [5, 6]]

  # Modifying an element in the original list
  li[0][0] = 99

  # The change is reflected in the combined list
  print(combined)  # Output: [[99, 2], [3, 4], [5, 6]]
  ```

  In the example above:
  - `combined` is a new list, but it holds references to the same nested lists as `li` and `other_li`.
  - Since these nested lists are mutable, changes made to their elements through `li` will also be seen in `combined`.

- **Deep Copy for Independent Lists**:
  If an independent copy is needed (where all nested objects are also copied), use the `copy` module's `deepcopy()` function to create a deep copy of the concatenated list.

  ```python
  import copy

  deep_copied_list = copy.deepcopy(li + other_li)

  # Now modifying the original will not affect the deep-copied list
  li[0][0] = 42
  print(deep_copied_list)  # Output: [[99, 2], [3, 4], [5, 6]]
  ```

By using `deepcopy()`, the new list is entirely independent of the original, ensuring that changes to any elements do not affect the copied list.


##### Combining Lists with `extend()`

Use `extend()` to add multiple elements from another list to the end of the list.
```python
combined = li + other_li  # [1, 2, 4, 4, 5, 6]
li.extend(other_li)       # li becomes [1, 2, 4, 4, 5, 6]
```

Modifies the original list `li` in place by appending the elements from `other_li`.

##### Checking Membership
Use `in` to verify if an element exists in the list.
```python
li = [1, 2, 3, 4]
exists = 1 in li  # True
not_exists = 5 in li  # False
```


##### Length of a List

Use `len()` to get the number of elements.
```python
length = len(li)  # => 6
```

##### Unpacking Lists
Python supports unpacking, where elements of a list can be assigned to multiple variables in a single operation.

- **Basic Unpacking**: Assign each element of a list to a corresponding variable.
```python
li = [1, 2, 3]
a, b, c = li
# a = 1, b = 2, c = 3
```

- **Extended Unpacking**: Use `*` to collect multiple elements into a list during unpacking.

```python
li = [1, 2, 3, 4, 5]
a, *middle, b = li
# a = 1, middle = [2, 3, 4], b = 5
```

Unpacking is useful for swapping values or for functions that return multiple outputs.
```python
# Swapping values
x, y = 5, 10
x, y = y, x  # Now x = 10, y = 5
```

#### Tuples (`tuple`)
Tuples in Python are similar to lists but are **immutable**, meaning that once created, their elements cannot be changed. This immutability makes tuples useful for representing fixed collections of items.

##### Creating Tuples
- Tuples are created by placing elements within parentheses, separated by commas.
- To create a tuple with a single element, include a trailing comma to distinguish it from a basic type.
- Parentheses are optional; tuples can also be created by separating values with commas.

```python
tup = (1, 2, 3)
single_element = (1,)  # Tuple with one element
empty_tuple = ()       # An empty tuple

# Without parentheses (tuple packing)
implicit_tuple = 1, 2, 3

# Note that a tuple of length one has to have a comma after the last element but
# tuples of other lengths, even zero, do not.
type((1))   # => <class 'int'>
type((1,))  # => <class 'tuple'>
type(())    # => <class 'tuple'>
```
##### Immutablity

Tuples are immutable, meaning that once created, their elements cannot be changed:

```python
tup[0] = 3  # Raises TypeError
```

##### Accessing Elements
You can do most of the list operations on tuples too:
- Tuples support indexing and slicing, similar to lists.
- Indexing starts at 0, and negative indices can be used to access elements from the end.

```python
first = tup[0]  # => 1
last = tup[-1]  # => 3

# Tuples are immutable, so attempting to change a value raises an error
tup[0] = 3  # Raises TypeError
```

##### Tuple Length
Use `len()` to get the number of elements in a tuple.
```python
length = len(tup)  # => 3
```

##### Tuple Operations
- **Concatenation**: Use the `+` operator to join two tuples, creating a new tuple.
- **Slicing**: Supports slicing operations like lists.
- **Membership Testing**: Use the `in` operator to check if an element is present.

```python
concatenated = tup + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)
sliced = tup[:2]  # => (1, 2)
exists = 2 in tup  # => True
```

##### Unpacking Tuples
Tuples can be unpacked into variables, which assigns each element to a corresponding variable.

- **Basic Unpacking**:
  ```python
  a, b, c = (1, 2, 3)  # a is 1, b is 2, c is 3
  ```

- **Extended Unpacking**: Use `*` to capture remaining elements.
  ```python
  a, *b, c = (1, 2, 3, 4)  # a is 1, b is [2, 3], c is 4
  ```

##### Implied Tuples
If you leave out the parentheses, Python still creates a tuple by default when separating values with commas.
```python
d, e, f = 4, 5, 6  # Creates a tuple (4, 5, 6)
```

##### Swapping Values
Tuples make it easy to swap variables in one line.
```python
e, d = d, e  # Swap the values of d and e
```

##### Notes on Single-Element Tuples
A tuple with a single element must include a comma, otherwise, it is interpreted as a basic type.
```python
type((1))   # => <class 'int'>
type((1,))  # => <class 'tuple'>
```

Tuples are a powerful feature in Python for working with immutable data structures and can be used in many situations where a list would be inappropriate due to the need for immutability.


#### Ranges (`range`)
Represents an immutable sequence of numbers. Commonly used in `for` loops.

```python
for i in range(5):
    print(i)  # Outputs: 0, 1, 2, 3, 4
```

### Mapping Types

#### Dictionaries (`dict`)
Dictionaries in Python are mutable, unordered collections that store data as key-value pairs. They are highly efficient for lookups, insertions, and deletions when using unique, immutable keys.

##### Creating Dictionaries
- **Using Curly Braces (`{}`)**: The most common way to create a dictionary.
- **Using the `dict()` Constructor**: Useful for creating dictionaries from sequences of key-value pairs or for initializing with keyword arguments.

```python
# Using curly braces
empty_dict = {}
person = {"name": "Alice", "age": 30, "location": "New York"}

# Using the dict() constructor
employee = dict(name="John", role="Manager", salary=50000)

# From a list of tuples
pairs = [("apple", 1), ("banana", 2)]
fruit_dict = dict(pairs)
```

> Note keys for dictionaries have to be immutable types. This is to ensure that the key can be converted to a constant hash value for quick look-ups. Immutable types include ints, floats, strings, tuples.

```python
invalid_dict = {[1,2,3]: "123"}  # => Yield a TypeError: unhashable type: 'list'
valid_dict = {(1,2,3):[1,2,3]}   # Values can be of any type, however.
```

##### Accessing and Modifying Elements
- **Accessing Values**: Use square brackets with the key to retrieve a value. If the key is not found, a `KeyError` is raised.
- **Using `get()`**: Allows for a default value if the key does not exist.
- **Modifying Values**: Assign a new value to an existing key, or add a new key-value pair if the key does not exist.

```python
person = {"name": "Alice", "age": 30, "location": "New York"}

# Accessing values
name = person["name"]  # => "Alice"
age = person.get("age", 25)  # Returns 30, or 25 if "age" were not a key

# Use "get()" method to avoid the KeyError
person.get("name")      # => "Alice"
# The job key does not exist, so None is returned
person.get("job")     # => None 

# The get method supports a default argument when the value is missing
person.get("job", "Engineer")   # => "Engineer"

# Modifying values
person["age"] = 31  # Update age to 31

# Adding a new key-value pair
person["job"] = "Engineer"
```

- `setdefault()` inserts into a dictionary only if the given key isn't present:
```python
person.setdefault("job", "Engineer")  # person["job"] is set to "Engineer"
person.setdefault("job", "Manager")  # person["job"] is still "Engineer"
```

- `update()` is a common and versatile way to add or update key-value pairs in a dictionary. It allows you to modify a dictionary by merging it with another dictionary or an iterable of key-value pairs. If the specified keys already exist, their values are updated; if they don't exist, they are added to the dictionary.

    - `update()` is especially useful for adding multiple key-value pairs at once, which is more concise than doing so one by one. For example, `person.update({"job": "Engineer", "city": "Boston"})` adds two new items to the dictionary. Additionally, you can use `update()` with an iterable, such as a list of tuples, to achieve the same effect.

    - When merging two dictionaries, `update()` is a straightforward way to combine their contents. For instance, merging `{"a": 1, "b": 2}` with `{"b": 3, "c": 4}` results in `{"a": 1, "b": 3, "c": 4}` after updating the first dictionary with the second.

    - If you're only adding or updating a single key-value pair, direct assignment (e.g., `person["key"] = value`) is simpler and more efficient. However, `update()` shines when dealing with multiple entries, avoiding repetitive code and improving readability, particularly when data is sourced from another dictionary or iterable.

- **Dictionary Unpacking (Python 3.5+)**
Dictionary unpacking allows you to merge dictionaries and create new ones using the `**` operator. This approach can be used to combine multiple dictionaries, where later keys will overwrite earlier ones if there are duplicates.

Basic Unpacking: The `**` operator unpacks key-value pairs from a dictionary into a new dictionary.

```python
combined = {"a": 1, **{"b": 2}}
# combined is {'a': 1, 'b': 2}
```

Handling Duplicate Keys: When merging dictionaries, if the same key appears in more than one dictionary, the value from the last dictionary will be used.

```python
result = {"a": 1, **{"a": 2}}
# result is {'a': 2}
```

Merging Multiple Dictionaries: You can combine multiple dictionaries using unpacking. This is especially useful when you want to merge configurations or combine data from different sources.

```python
dict1 = {"x": 1, "y": 2}
dict2 = {"y": 3, "z": 4}
merged = {**dict1, **dict2}
# merged is {'x': 1, 'y': 3, 'z': 4}
```

Dictionary unpacking is a flexible way to update or merge dictionaries, complementing other methods like direct assignment and the `update()` method.

##### Accessing Keys, Values, and Items

**Dictionary Views**: When you use `keys()`, `values()`, or `items()` on a dictionary, they return view objects that provide a dynamic view of the dictionary’s contents. These views reflect changes made to the dictionary in real time. While they are iterable, they do not support indexing or slicing like lists.

- **`keys()`**: Returns a view object displaying the dictionary's keys. This object can be used in loops and supports membership testing (e.g., `"key" in dict.keys()`). However, if you need to access a specific key by index, you must convert the view to a list first.

```python
keys_view = person.keys()
keys_list = list(keys_view)  # Converts the view to a list for indexing
first_key = keys_list[0]  # Access the first key
```

- **`values()`**: Returns a view object of the dictionary's values. Like the keys view, it can be used in loops but does not support direct indexing.
```python
values_view = person.values()
for value in values_view:
    print(value)  # Prints each value in the dictionary
```

- **`items()`**: Returns a view object containing key-value tuple pairs. It is suitable for iteration but does not support indexing.
```python
items_view = person.items()
for key, value in items_view:
    print(f"{key}: {value}")  # Prints each key-value pair
```

- **When to Convert to a List**: If you need to perform list-specific operations (e.g., indexing, slicing, sorting), you must convert the dictionary view to a list.

```python
# Example of indexing after conversion
keys_list = list(person.keys())
second_key = keys_list[1]  # Access the second key

# Example where failing to convert would cause an error
# person.keys()[1]  # Raises TypeError: 'dict_keys' object is not subscriptable
```

##### Removing Elements
- **Using `del`**: Deletes a key-value pair.
- **Using `pop()`**: Removes a key and returns its value. Raises a `KeyError` if the key is not found unless a default is provided.
- **Using `popitem()`**: Removes and returns the last inserted key-value pair. Useful for treating the dictionary like a stack.

```python
# Removing a specific key
del person["location"]

# Using pop() to remove a key and get its value
role = person.pop("job", "No job found")

# popitem() example
last_item = person.popitem()
```

- **`clear()`**: Removes all items from the dictionary.
```python
person.clear() # person is now {}
```

##### Checking Membership
- **Using `in`**: Check if a key is present in the dictionary. This operation checks for keys only, not values.
```python
exists = "name" in person  # True
not_exists = "salary" not in person  # True
```

##### Iterating Over Dictionaries
You can loop through keys, values, or key-value pairs.
```python
# Looping through keys
for key in person:
    print(key)

# Looping through values
for value in person.values():
    print(value)

# Looping through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
```

##### Dictionary Comprehensions
Similar to list comprehensions, dictionary comprehensions allow you to create dictionaries in a concise way.
```python
squared = {x: x * x for x in range(6)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

##### Immutability of Keys
- Keys must be immutable types (e.g., strings, numbers, tuples).
- Mutable types like lists or dictionaries cannot be used as keys because they do not have a consistent hash value.
```python
valid_key = {("apple", "banana"): 5}
invalid_key = {[1, 2, 3]: "value"}  # Raises TypeError
```

##### Merging Dictionaries (Python 3.9+)
Python 3.9 introduced new operators for merging and updating dictionaries:
- **Union (`|`)**: Creates a new dictionary by merging two dictionaries.
- **In-place Update (`|=`)**: Updates the original dictionary with another dictionary.

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = dict1 | dict2  # => {"a": 1, "b": 3, "c": 4}
dict1 |= dict2  # dict1 is now {"a": 1, "b": 3, "c": 4}
```

### Set Types

Sets in Python are unordered collections of unique elements, designed for fast membership testing and eliminating duplicate entries. Python provides two types of sets: mutable (`set`) and immutable (`frozenset`).

#### `set`
A `set` is a mutable, unordered collection that supports adding and removing elements. The elements must be hashable (immutable types like numbers, strings, tuples), but the set itself is mutable.

- **Creating a Set**:
  Sets can be created using curly braces `{}` or the `set()` constructor.
  ```python
  #empty set
  empty_set = set()

  # Using curly braces
  fruit_set = {"apple", "banana", "cherry"}

  # Using the set() constructor
  number_set = set([1, 2, 3, 4])

  # Similar to keys of a dictionary, elements of a set have to be immutable.
  invalid_set = {[1], 1}  # => Raises a TypeError: unhashable type: 'list'
  valid_set = {(1,), 1}
  ```

- **Common Set Operations**:
  Sets support several built-in operations, such as union, intersection, difference, and symmetric difference.
  
  ```python
  a = {1, 2, 3}
  b = {3, 4, 5}

  # Union: combines all unique elements
  union_set = a | b  # => {1, 2, 3, 4, 5}

  # Intersection: elements present in both sets
  intersection_set = a & b  # => {3}

  # Difference: elements in a but not in b
  difference_set = a - b  # => {1, 2}

  # Symmetric Difference: elements in either a or b, but not both
  sym_diff_set = a ^ b  # => {1, 2, 4, 5}
  ```

- **Adding and Removing Elements**:
  Use `add()` to add an element and `remove()` or `discard()` to remove an element.
  ```python
  fruit_set.add("orange")
  fruit_set.remove("banana")  # Raises KeyError if "banana" is not found
  fruit_set.discard("pear")   # Does nothing if "pear" is not found
  ```

- **Set Comprehensions**:
  Similar to list comprehensions, sets support comprehension for generating new sets.
  ```python
  squared = {x * x for x in range(6)}  # => {0, 1, 4, 9, 16, 25}
  ```

#### `frozenset`
A `frozenset` is an immutable version of a set. Once created, elements cannot be added or removed. This makes `frozenset` suitable for use as dictionary keys or elements of another set.

- **Creating a `frozenset`**:
  The `frozenset()` function is used to create an immutable set.
  ```python
  immutable_set = frozenset([1, 2, 3, 4])
  ```

- **Operations on `frozenset`**:
  While you cannot modify a `frozenset`, you can perform set operations (e.g., union, intersection) that produce new sets.
  ```python
  a = frozenset([1, 2, 3])
  b = frozenset([3, 4, 5])

  # Union, intersection, and difference operations are allowed
  union_fs = a | b  # => frozenset({1, 2, 3, 4, 5})
  intersection_fs = a & b  # => frozenset({3})
  ```

#### When to Use `set` vs. `frozenset`
- Use `set` when you need a collection of unique items that may change over time.
- Use `frozenset` when you need an immutable set, such as for creating keys in dictionaries or elements in other sets.

Sets are useful for mathematical operations, fast membership testing, and eliminating duplicates from data.

