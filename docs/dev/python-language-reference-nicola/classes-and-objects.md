# Classes and Objects in Python

A class is a user-defined blueprint or prototype from which objects are created. Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by their class) for modifying their state.


Compared with other programming languages, Python’s class mechanism adds classes with a **minimum of new syntax and semantics**. It is a mixture of the class mechanisms found in C++ and Modula-3.
Python classes provide all the standard features of Object Oriented Programming:
- the class inheritance mechanism allows **multiple base classes**, 
- a derived class can **override any methods** of its base class or classes,
- and a method can call the method of a base class with the same name,
- Objects can contain arbitrary amounts and kinds of data, 
- As is true for modules, classes partake of the dynamic nature of Python: they are created at runtime, and can be modified further after creation.
- class members (attributes and methods) are **public by default**, meaning they can be accessed from outside the class. To indicate that a member is intended to be private, you can prefix its name with double underscores (`__`), which triggers name mangling to make it harder to access from outside the class. However, this is only a convention, and such members can still be accessed if necessary.
- All methods in Python are **virtual by default**, allowing derived classes to override them as needed.
- **classes themselves are objects**, which allows for dynamic creation and modification of classes at runtime. This means you can assign classes to variables, pass them as arguments to functions, and even modify their attributes dynamically.
- Python allows user-defined classes to inherit from built-in types. For example, you can create a custom class that extends the functionality of a built-in type like list or dict.
- Python supports **multiple inheritance**, allowing a class to inherit from multiple parent classes. This can be useful for creating classes that inherit attributes and methods from multiple sources.
- Python provides **abstract base classes** (ABCs) through the `abc` module, which define a common interface for a set of subclasses. This allows for more flexible and modular code, as well as runtime checking of class implementations.
- Python allows for **class decorators**, which are functions that modify the behavior of a class at runtime. This can be useful for adding functionality to a class without modifying its definition.
- Python supports **class-level attributes**, which are attributes that are shared among all instances of a class. These attributes are defined at the class level and are shared by all instances of the class.
- Python supports **class-level methods**, which are methods that are defined at the class level and are shared among all instances of a class. These methods are defined using the `@classmethod` decorator and can be used to access class-level attributes and methods.
- Python supports **static methods**, which are methods that are defined at the class level and are not associated with any particular instance of the class. These methods are defined using the `@staticmethod` decorator and can be used to define utility functions that are related to the class but do not require access to any particular instance of the class.
- Python supports **data classes**, which are simple classes that are primarily used to store data. Data classes automatically generate special methods like `__init__`, `__repr__`, and `__eq__`, making it easier to create classes that behave like simple data containers.
- Python supports operator overloading, enabling you to define how operators like +, -, or [] behave for instances of your custom classes. This is achieved by defining special methods in your class, such as __add__ for addition or __getitem__ for indexing.
- Special Methods (Dunder Methods): `__init__`, `__str__`, etc.
- Properties and Descriptors


Visit the following resources to learn more:

- [official Classes in Python](https://docs.python.org/3/tutorial/classes.html): not the best, but it's the official documentation
- [Classes in Python](https://realpython.com/python-classes/): a good article

## Cheat Sheet

```python
####################################################
## 6. Classes
####################################################

# We use the "class" statement to create a class
class Human:

    # A class attribute. It is shared by all instances of this class
    species = "H. sapiens"

    # Basic initializer, this is called when this class is instantiated.
    # Note that the double leading and trailing underscores denote objects
    # or attributes that are used by Python but that live in user-controlled
    # namespaces. Methods(or objects or attributes) like: __init__, __str__,
    # __repr__ etc. are called special methods (or sometimes called dunder
    # methods). You should not invent such names on your own.
    def __init__(self, name):
        # Assign the argument to the instance's name attribute
        self.name = name

        # Initialize property
        self._age = 0   # the leading underscore indicates the "age" property is
                        # intended to be used internally
                        # do not rely on this to be enforced: it's a hint to other devs

    # An instance method. All methods take "self" as the first argument
    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))

    # Another instance method
    def sing(self):
        return "yo... yo... microphone check... one two... one two..."

    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    @classmethod
    def get_species(cls):
        return cls.species

    # A static method is called without a class or instance reference
    @staticmethod
    def grunt():
        return "*grunt*"

    # A property is just like a getter.
    # It turns the method age() into a read-only attribute of the same name.
    # There's no need to write trivial getters and setters in Python, though.
    @property
    def age(self):
        return self._age

    # This allows the property to be set
    @age.setter
    def age(self, age):
        self._age = age

    # This allows the property to be deleted
    @age.deleter
    def age(self):
        del self._age


# When a Python interpreter reads a source file it executes all its code.
# This __name__ check makes sure this code block is only executed when this
# module is the main program.
if __name__ == "__main__":
    # Instantiate a class
    i = Human(name="Ian")
    i.say("hi")                     # "Ian: hi"
    j = Human("Joel")
    j.say("hello")                  # "Joel: hello"
    # i and j are instances of type Human; i.e., they are Human objects.

    # Call our class method
    i.say(i.get_species())          # "Ian: H. sapiens"
    # Change the shared attribute
    Human.species = "H. neanderthalensis"
    i.say(i.get_species())          # => "Ian: H. neanderthalensis"
    j.say(j.get_species())          # => "Joel: H. neanderthalensis"

    # Call the static method
    print(Human.grunt())            # => "*grunt*"

    # Static methods can be called by instances too
    print(i.grunt())                # => "*grunt*"

    # Update the property for this instance
    i.age = 42
    # Get the property
    i.say(i.age)                    # => "Ian: 42"
    j.say(j.age)                    # => "Joel: 0"
    # Delete the property
    del i.age
    # i.age                         # => this would raise an AttributeError


####################################################
## 6.1 Inheritance
####################################################

# Inheritance allows new child classes to be defined that inherit methods and
# variables from their parent class.

# Using the Human class defined above as the base or parent class, we can
# define a child class, Superhero, which inherits variables like "species",
# "name", and "age", as well as methods, like "sing" and "grunt"
# from the Human class, but can also have its own unique properties.

# To take advantage of modularization by file you could place the classes above
# in their own files, say, human.py

# To import functions from other files use the following format
# from "filename-without-extension" import "function-or-class"

from human import Human


# Specify the parent class(es) as parameters to the class definition
class Superhero(Human):

    # If the child class should inherit all of the parent's definitions without
    # any modifications, you can just use the "pass" keyword (and nothing else)
    # but in this case it is commented out to allow for a unique child class:
    # pass

    # Child classes can override their parents' attributes
    species = "Superhuman"

    # Children automatically inherit their parent class's constructor including
    # its arguments, but can also define additional arguments or definitions
    # and override its methods such as the class constructor.
    # This constructor inherits the "name" argument from the "Human" class and
    # adds the "superpower" and "movie" arguments:
    def __init__(self, name, movie=False,
                 superpowers=["super strength", "bulletproofing"]):

        # add additional class attributes:
        self.fictional = True
        self.movie = movie
        # be aware of mutable default values, since defaults are shared
        self.superpowers = superpowers

        # The "super" function lets you access the parent class's methods
        # that are overridden by the child, in this case, the __init__ method.
        # This calls the parent class constructor:
        super().__init__(name)

    # override the sing method
    def sing(self):
        return "Dun, dun, DUN!"

    # add an additional instance method
    def boast(self):
        for power in self.superpowers:
            print("I wield the power of {pow}!".format(pow=power))


if __name__ == "__main__":
    sup = Superhero(name="Tick")

    # Instance type checks
    if isinstance(sup, Human):
        print("I am human")
    if type(sup) is Superhero:
        print("I am a superhero")

    # Get the "Method Resolution Order" used by both getattr() and super()
    # (the order in which classes are searched for an attribute or method)
    # This attribute is dynamic and can be updated
    print(Superhero.__mro__)    # => (<class '__main__.Superhero'>,
                                # => <class 'human.Human'>, <class 'object'>)

    # Calls parent method but uses its own class attribute
    print(sup.get_species())    # => Superhuman

    # Calls overridden method
    print(sup.sing())           # => Dun, dun, DUN!

    # Calls method from Human
    sup.say("Spoon")            # => Tick: Spoon

    # Call method that exists only in Superhero
    sup.boast()                 # => I wield the power of super strength!
                                # => I wield the power of bulletproofing!

    # Inherited class attribute
    sup.age = 31
    print(sup.age)              # => 31

    # Attribute that only exists within Superhero
    print("Am I Oscar eligible? " + str(sup.movie))

####################################################
## 6.2 Multiple Inheritance
####################################################


# Another class definition
# bat.py
class Bat:

    species = "Baty"

    def __init__(self, can_fly=True):
        self.fly = can_fly

    # This class also has a say method
    def say(self, msg):
        msg = "... ... ..."
        return msg

    # And its own method as well
    def sonar(self):
        return "))) ... ((("


if __name__ == "__main__":
    b = Bat()
    print(b.say("hello"))
    print(b.fly)


# And yet another class definition that inherits from Superhero and Bat
# superhero.py
from superhero import Superhero
from bat import Bat

# Define Batman as a child that inherits from both Superhero and Bat
class Batman(Superhero, Bat):

    def __init__(self, *args, **kwargs):
        # Typically to inherit attributes you have to call super:
        # super(Batman, self).__init__(*args, **kwargs)
        # However we are dealing with multiple inheritance here, and super()
        # only works with the next base class in the MRO list.
        # So instead we explicitly call __init__ for all ancestors.
        # The use of *args and **kwargs allows for a clean way to pass
        # arguments, with each parent "peeling a layer of the onion".
        Superhero.__init__(self, "anonymous", movie=True,
                           superpowers=["Wealthy"], *args, **kwargs)
        Bat.__init__(self, *args, can_fly=False, **kwargs)
        # override the value for the name attribute
        self.name = "Sad Affleck"

    def sing(self):
        return "nan nan nan nan nan batman!"


if __name__ == "__main__":
    sup = Batman()

    # The Method Resolution Order
    print(Batman.__mro__)     # => (<class '__main__.Batman'>,
                              # => <class 'superhero.Superhero'>,
                              # => <class 'human.Human'>,
                              # => <class 'bat.Bat'>, <class 'object'>)

    # Calls parent method but uses its own class attribute
    print(sup.get_species())  # => Superhuman

    # Calls overridden method
    print(sup.sing())         # => nan nan nan nan nan batman!

    # Calls method from Human, because inheritance order matters
    sup.say("I agree")        # => Sad Affleck: I agree

    # Call method that exists only in 2nd ancestor
    print(sup.sonar())        # => ))) ... (((

    # Inherited class attribute
    sup.age = 100
    print(sup.age)            # => 100

    # Inherited attribute from 2nd ancestor whose default value was overridden.
    print("Can I fly? " + str(sup.fly))  # => Can I fly? False


```


## Python Scopes and Namespaces
Before introducing classes, I first have to tell you something about Python's scope rules. Class definitions play some neat tricks with namespaces, and you need to know how scopes and namespaces work to fully understand what's going on. 
See Nicola's notes [scopes and namespaces](scopes-and-namespaces.md)

## Class Definition Syntax and Namespace

Ref: https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes

To define a class, you need to use the `class` keyword followed by the class name and a colon, just like you'd do for other [compound statements](https://docs.python.org/3/reference/compound_stmts.html) in Python. Then you must define the class body, which will start at the next indentation level:

```python
class ClassName:
    <statement-1> # Class body
    .
    .
    .
    <statement-N>
```

Class definitions, like function definitions (def statements) must be executed before they have any effect.

In practice, the statements inside a class definition will usually be function definitions, but other statements are allowed, and sometimes useful — we’ll come back to this later. The function definitions inside a class normally have a peculiar form of argument list, dictated by the calling conventions for methods — again, this is explained later.

An example of a class definition:

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36) # This creates a new instance of the Person class
p1.myfunc() # This calls the myfunc method on the p1 instance
```
[Try yourself](https://www.w3schools.com/python/trypython.asp?filename=demo_class4)

When a class definition is entered, **a new namespace is created**, and used as the local scope — thus, all assignments to local variables go into this new namespace. In particular, function definitions bind the name of the new function here.

When a class definition is left normally (via the end):
- a **class object** is created. This is basically a wrapper around the contents of the namespace created by the class definition; 
- the original local scope (the one in effect just before the class definition was entered) is reinstated, 
- and the class object is bound here to the class name given in the class definition header (ClassName in the example).

In fact you can see that methods are defined in the class namespace, and can be accessed from the class object:

```python
print(Person.myfunc)
# <function Person.myfunc at 0x150cc0d30f70>
```

## Class Objects

Now that we have the a class object, what can we do with it? Class objects support two kinds of operations: **attribute references** and **instantiation**.

### ClassAttribute References

**Attribute references** use the standard syntax used for all attribute references in Python: `obj.name`. Valid attribute names are all the names that were in the class's namespace when the class object was created. So, if the class definition looked like this:

```python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```

then `MyClass.i` and `MyClass.f` are valid attribute references, returning an integer and a function object, respectively. 

Class attributes can also be assigned to, so you can change the value of `MyClass.i` by assignment. 

> [!NOTE] Also `MyClass.__doc__` is a valid attribute, returning the docstring belonging to the class: `"A simple example class"`. It's automatically created by Python when the class is defined.


### Class Instantiation the `__init__` method

Class instantiation uses function notation. Just pretend that the class object is a parameterless function that returns a new instance of the class. For example (assuming the above class):

```python
x = MyClass()
```

creates a new instance of the class and assigns this object to the local variable `x`.

If you want to instantiate an object in Python with specific attributes or initial settings, you define an `__init__` method within your class. 
This special method, known as the **initializer**, is automatically invoked when a new instance of the class is created, allowing you to set up the object’s initial state.

In the previous example, `MyClass` has a class attribute `i` and a method `f`. However, it doesn’t initialize any instance-specific attributes. To allow each instance of `MyClass` to have its own `i` value, you can define an `__init__` method:

```python
class MyClass:
    """A simple example class"""

    def __init__(self, i):
        self.i = i

    def f(self):
        return f"hello world i = {self.i}"
```

This allows you to create instances of `MyClass` with different `i` values:

```python
x = MyClass(10)
y = MyClass(20)
print(x.i)  # Output: 10
print(y.i)  # Output: 20
print(x.f())  # Output: hello world i = 10
print(y.f())  # Output: hello world i = 20
```


The `self` parameter is a reference to the current instance of a class and is used to access variables and methods associated with that instance. It must be the first parameter of any method in the class, including the `__init__` method, which is the constructor.

In the above example, `self` is used to access the `i` attribute of the instance.

When you call a method on an instance of a class, the instance is automatically passed as the first argument to the method. This is why you need to include `self` as a parameter in your method definitions.


> [!NOTE] By convention, self is used as the name for this parameter, but you can choose any name you prefer. However, using self is a widely accepted practice and makes the code more readable.

Key Points
- **Automatic Invocation:** The `__init__` method is called automatically when a new instance of a class is created.
- **Initialization, Not Construction:** While often called a constructor, `__init__` doesn’t create the object; it initializes the object’s attributes after it’s been created.
- **Self Parameter:** The `self` parameter allows access to the instance’s attributes and methods within the class.


## Instance Objects

What can we do with instance objects? The only operations understood by instance objects are attribute references.
There are two kinds of valid attribute names: **data attributes** and **methods**.

### Data Attributes

Data attributes in Python are akin to “instance variables” in Smalltalk or “data members” in C++. 
They are unique to each instance of a class and are dynamically created when assigned a value—there’s no need for prior declaration. This flexibility makes it easy to add or modify attributes directly for an instance.
For example, if `x` is the instance of `MyClass` created above, the following piece of code will print the value 16, without leaving a trace:

```python
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
```

Key Points:
- **Dynamic Creation:** Data attributes are created as soon as they are assigned a value.
- **Instance-Specific:** Each instance of a class has its own set of attributes, independent of other instances.
- **Deletion:** Attributes can be deleted using the del statement.

#### Data Attributes in practice with the `__init__` method

While Python allows dynamic assignment of attributes, the common and preferred way to define and initialize attributes is through the `__init__` method. This ensures all instances of a class start with a well-defined set of attributes, making the code more predictable and easier to maintain.

```python
class Person:
    def __init__(self, name, age):
        # Initialize instance attributes
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Create instances of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Access instance attributes
print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.
print(person2.greet())  # Output: Hello, my name is Bob and I am 25 years old.

# Modify attributes
person1.age += 1
print(f"{person1.name} is now {person1.age} years old.")  # Output: Alice is now 31 years old.
```

Output:

```bash
Hello, my name is Alice and I am 30 years old.
Hello, my name is Bob and I am 25 years old.
Alice is now 31 years old.
```

Why Use the `__init__` Method?
- **Predictability:** All instances have the same set of attributes initialized at creation.
- **Readability:** It’s clear what attributes are expected for the class.
- **Maintainability:** Centralized initialization reduces bugs and makes the class easier to update.
- **Custom Initialization:** You can define default values or enforce required attributes.

### Instance Methods

The other kind of instance attribute reference is a **method**. A method is a function that “belongs to” an object.

All attributes of a class that are function objects define corresponding methods of its instances.

So in our example:
```python
class MyClass:
    i = 12345
    def f(self):
        return 'hello world'

x = MyClass()

print(x.i) # 12345
print(MyClass.i) # 12345
print(x.f) # <bound method MyClass.f of <__main__.MyClass object at 0x150cc0d30f70>>
print(MyClass.f) # <function MyClass.f at 0x150cc0d30f70>

```

`x.f` is a valid method reference, since `MyClass.f` is a function, but `x.i` is not, since `MyClass.i` is not. But `x.f` is not the same thing as `MyClass.f` — it is a method object, not a function object.

Usually, a method is called right after it is bound:

In the MyClass example, `x.f()` will return the string 'hello world'.

However, it is not necessary to call a method right away: `x.f` is a method object, and can be stored away and called at a later time. For example:

```python
xf = x.f
while True:
    print(xf())
```

will continue to print hello world until the end of time.

What exactly happens when a method is called?
- You may have noticed that `x.f()` was called without an argument above, even though the function definition for `f()` specified an argument.
- What happened to the argument? Surely Python raises an exception when a function that requires an argument is called without any — even if the argument isn’t actually used…
- Actually, you may have guessed the answer: the special thing about methods is that **the instance object is passed as the first argument of the function**. 

In our example, the call `x.f()` is exactly equivalent to `MyClass.f(x)`. 

```python
class MyClass:
    def f(self):
        return 'hello world'

x = MyClass()

MyClass.f(x) # Output: 'hello world'
MyClass.f() # ERROR: TypeError: MyClass.f() missing 1 required positional argument: 'self'
```

In general, calling a method with a list of n arguments is equivalent to calling the corresponding function with an argument list that is created by inserting the method’s instance object before the first argument.

In general, methods work as follows:
- When a **non-data attribute** of an instance is referenced, the instance’s class is searched. 
- If the name denotes a valid class attribute that is a **function object**, references to both the instance object and the function object are packed into a **method object** ( `bound method`).

```python
x.f # <bound method MyClass.f of <__main__.MyClass object at 0x150cc0d30f70>>
```

- When the method object is called with an argument list: a new argument list is constructed from the instance object and the argument list, and the function object is called with this new argument list.

```python
class MyClass:
    def greet(self, name):
        print(f"Hello, {name}!")

# Creating an instance of MyClass
obj = MyClass()

# Calling the method on the instance
obj.greet("Alice")

# Equivalent function call!!
MyClass.greet(obj, "Alice")
```

## Class Variables

Generally speaking:
- instance variables are for data unique to each instance and 
- class variables are for attributes and methods shared by all instances of the class.

Shared data can have possibly surprising effects with involving mutable objects such as lists and dictionaries.
For example, the tricks list in the following code should not be used as a class variable because just a single list would be shared by all Dog instances:

```python
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']
```

Correct design of the class should use an instance variable instead:

```python
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```

## Special or dunder or magic Methods

ref: https://realpython.com/python-classes/#special-methods-and-protocols

Python supports what it calls [special methods](https://docs.python.org/3/glossary.html#term-special-method), which are also known as **dunder** or **magic** methods. 

These methods are typically **instance methods**, and they're a fundamental part of Python's internal class mechanism.

🌟 They have an important feature in common: **Python calls them automatically in response to specific operations.**

The official documentation define them as: A method that is called implicitly by Python to execute a certain operation on a type, such as addition. Such methods have names starting and ending with double underscores. ([Source](https://docs.python.org/3/glossary.html#term-special-method))

There's an important detail to highlight in this definition. *Python implicitly calls special methods to execute certain operations in your code*. For example, when you run the addition `5 + 2` in a [REPL](https://realpython.com/python-repl/) session, Python internally runs the following code under the hood:

Python

```bash
`>>> (5).__add__(2)
7
`
```

The `.__add__()` special method of integer numbers supports the addition that you typically run as `5 + 2`.

Reading between the lines, you'll realize that even though you can directly call special methods, they're not intended for direct use. You shouldn't call them directly in your code. Instead, you should rely on Python to call them automatically in response to a given operation.

> [!NOTE] Even though special methods are also called *magic methods*, some people in the Python community may not like this latter terminology. The only magic around these methods is that Python calls them implicitly under the hood. So, the official documentation refers to them as **special methods** instead.

Python uses these methods for many different tasks. They provide a great set of tools that will allow you to unlock the power of classes in Python.

You'll recognize special methods because their names start and end with a double underscore, which is the origin of their other name, [dunder methods](https://realpython.com/python-double-underscore/#dunder-names-in-python) (**d**ouble **under**score). 

Arguably, `.__init__()` is the most common special method in Python classes. As you already know, this method works as the instance initializer. Python automatically calls it when you call a class constructor.

> [!NOTE] To dive deeper into special methods, check out the [Python's Magic Methods: Leverage Their Power in Your Classes](https://realpython.com/python-magic-methods/) tutorial.

> [!NOTE] In this tutorial, you'll find the terms **special methods**, **dunder methods**, and **magic methods** used interchangeably.

The double underscores flag these methods as core to some Python features.
They help avoid name collisions with your own methods and attributes.
Some popular and well-known magic methods include the following:

* [`.__init__()`](https://realpython.com/python-class-constructor/#object-initialization-with-__init__):  Provides an initializer in Python classes
* [`.__str__()` and `.__repr__()`](https://realpython.com/python-repr-vs-str/): Provide string representations for objects
* [`.__call__()`](https://realpython.com/python-callable-instances/): Makes the instances of a class callable
* [`.__len__()`](https://realpython.com/len-python-function/): Supports the [`len()`](https://realpython.com/len-python-function/) function


This is just a tiny sample of all the special methods that Python has. All these methods support specific features that are core to Python and its object-oriented infrastructure.

> [!NOTE] For the complete list of magic methods, refer to the [special method section](https://docs.python.org/3/reference/datamodel.html#specialnames) on the data model page of Python's official documentation.

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


Magic methods exist for many purposes. All the available magic methods support built-in features and play specific roles in the language. For example, built-in types such as [lists](https://realpython.com/python-list/), [strings](https://realpython.com/python-strings/), and [dictionaries](https://realpython.com/python-dicts/) implement most of their core functionality using magic methods. In your custom classes, you can use magic methods to make callable objects, define how objects are compared, tweak how you create objects, and more.

Note that because magic methods have special meaning for Python itself, you should avoid naming custom methods using leading and trailing double underscores. Your custom method won't trigger any Python action if its name doesn't match any official special method names, but it'll certainly confuse other programmers. New dunder names may also be introduced in future versions of Python.

Magic methods are core to Python's [data model](https://docs.python.org/3/reference/datamodel.html) and are a fundamental part of object-oriented programming in Python. 

This section was meant to be an overview of the special methods. There are so many special methods that it would be impractical to list them all here and we decided to explain them when need by the specific topic.

## Protocols

Python protocols are another fundamental topic that’s closely related to special methods. 
Protocols consist of one or more special methods that support a given feature or functionality.

Common examples of protocols include:

**Iterator Protocol**:
- Allows you to create iterator objects
- magic methods: `.__iter__()` and `.__next__()`

**Iterable Protocol**:
- Makes your objects iterable
- magic method: `.__iter__()`

**Descriptor Protocol**:
- Lets you write managed attributes
- magic methods: `.__get__()`, `.__set__()`, `.__delete__()`, and `.__set_name__()`

**Context manager Protocol**:
- Enables an object to work on with statements
- magic methods: `.__enter__()` and `.__exit__()`

### Example of Iterator Protocol

Here’s an example of a minimal ThreeDPoint class that implements the iterable protocol:

```python
>>> class ThreeDPoint:
...     def __init__(self, x, y, z):
...         self.x = x
...         self.y = y
...         self.z = z
...     def __iter__(self):
...         yield from (self.x, self.y, self.z)
...

>>> list(ThreeDPoint(4, 8, 16))
[4, 8, 16]
```

This class takes three arguments representing the space coordinates of a given point. 
The `.__iter__()` method is a generator function that returns an [iterator](iterators-iterables-generators.md#iterators). The resulting iterator yields the coordinates of ThreeDPoint on demand.

The `list()` function constructs a list from an iterable. It iterates over the provided iterable and adds each element to a new list. It iterates over the attributes `.x`, `.y`, and `.z`, returning a list object.

🌟 The key point 🌟 is that you don’t need to call `.__iter__()` directly.  Python calls it automatically when you use an instance of ThreeDPoint in an [iteration](iterators-iterables-generators.md#understanding-iteration-in-python).


## Class Methods

A class method is a method that **takes the class object as its first argument** instead of taking self.
CONVENTION: In this case, the argument should be called `cls`, which is also a strong convention in Python.


You can create class methods using the [`@classmethod`](https://docs.python.org/3/library/functions.html#classmethod) decorator. 

In Python, methods within a class are instance methods by default, meaning they operate on instances of the class and require an instance (self) as their first parameter. To define a method that operates on the class itself rather than its instances, you use the @classmethod decorator, which changes the method’s behavior to receive the class (cls) as its first parameter.

A class method can be called either on the class (such as `C.f()`) or on an instance (such as `C().f()`).
The instance is ignored except for its class.
If a class method is called for a derived class, the derived class object is passed as the implied first argument.

### what happens if you don't use the `@classmethod` decorator

If you define a method without the @classmethod decorator and intend for it to operate on the class, it will not function as expected. Such a method will be treated as an instance method, requiring an instance of the class to be called. Attempting to call it on the class itself will result in a TypeError because the method expects an instance (`self`) but receives the class instead.

```python
class MyClass:
    def regular_method(self):
        print(f"Called by instance {self}")

# Creating an instance
obj = MyClass()

# Calling the method on the instance
obj.regular_method()  # Output: Called by instance <__main__.MyClass object at 0x...>

# Attempting to call the method on the class
MyClass.regular_method()
# Raises TypeError: regular_method() missing 1 required positional argument: 'self'
```

In this example, `regular_method` is defined without the `@classmethod decorator`, so it expects an instance (`self`) as its first argument:

- Calling `obj.regular_method()` works correctly because `obj` is an instance of `MyClass` and the first positional argument is automatically passed as `self`. 
- However, calling `MyClass.regular_method()` raises a `TypeError` because by default the method of a class (NOT THE INSTANCE) is treated as regular function and not a method.

### Using the `@classmethod` decorator

By adding the `@classmethod` decorator, the method is treated as a method of the class and not a regular function. This means that the first positional argument is automatically passed as the class object (`cls`).

A class method can be called either on the class:
- `C.f()`:
- `C().f()`: in this case self is ignored and the class is used instead.

```python
class MyClass:
    @classmethod
    def class_method(cls):
        print(f"Called by class {cls}")

# Calling the class method on the class
MyClass.class_method()  # Output: Called by class <class '__main__.MyClass'>

# Calling the class method on an instance
obj = MyClass()
obj.class_method()  # Output: Called by class <class '__main__.MyClass'>
```


### Example - Providing your classes with multiple constructors

Providing your classes with [multiple constructors](https://realpython.com/python-multiple-constructors/#providing-multiple-constructors-with-classmethod-in-python) is one of the most common use cases of class methods in Python.

For example, say you want to add an alternative constructor to your `ThreeDPoint` so that you can quickly create points from tuples or lists of coordinates:

```python
class ThreeDPoint:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self):
        yield from (self.x, self.y, self.z)

    @classmethod
    def from_sequence(cls, sequence):
        return cls(*sequence)
    def __repr__(self):
        return f"{type(self).__name__}({self.x}, {self.y}, {self.z})"
```

In the `.from_sequence()` class method, you take a sequence of coordinates as an argument, create a `ThreeDPoint` object from it, and return the object to the caller.
To create the new object, you use the `cls` argument, which holds an implicit reference to the current class, which Python injects into your method automatically.

Here's how this class method works:

```python
>>> from point import ThreeDPoint

>>> ThreeDPoint.from_sequence((4, 8, 16))
ThreeDPoint(4, 8, 16)

>>> point = ThreeDPoint(7, 14, 21)
>>> point.from_sequence((3, 6, 9))
ThreeDPoint(3, 6, 9)
```

In this example, you use the `ThreeDPoint` class directly to access the class method `.from_sequence()`. 
Note that you can also access the method using a concrete instance, like `point` in the example. 
In each of the calls to `.from_sequence()`, you'll get a completely new instance of `ThreeDPoint`. 
However, class methods should be accessed through the corresponding class name for better clarity and to avoid confusion.

REF: https://realpython.com/python-classes/#class-methods-with-classmethod

## Static Methods

In Python, methods defined within a class are instance methods by default, meaning they operate on instances of the class and require an instance (self) as their first parameter.
To define a method that doesn’t operate on an instance or the class itself, you use the `@staticmethod` decorator.
This decorator indicates that the method doesn’t receive an implicit first argument (self or cls) and can be called on the class or its instances without requiring instantiation.

So, they’re regular functions defined within a class. You could’ve also defined them outside the class as stand-alone function.
Typycally you define a static method instead of a regular function outside the class when that function is closely related to your class, and you want to bundle it together for convenience or for consistency with your code’s API. 

REF: https://realpython.com/python-classes/#static-methods-with-staticmethod

### Defining a Method WITHOUT the `@staticmethod` Decorator

If you define a method within a class without the `@staticmethod` decorator and omit the `self` parameter, it will not function as intended. 
Attempting to call such a method on an instance will result in a `TypeError` because Python automatically passes the instance as the first argument to instance methods.

```python
class MyClass:
    def regular_method():
        print("This is a regular method.")

# Calling the method on the class works as expected
MyClass.regular_method()  # Output: This is a regular method.

obj = MyClass()
obj.regular_method()
# Raises TypeError: regular_method() takes 0 positional arguments but 1 was given
```
In this example, `regular_method` is defined without the `self` parameter. 
When `obj.regular_method()` is called, Python tries to pass `obj` as the first argument, leading to a `TypeError` because `regular_method` doesn’t accept any arguments.


Explanation:
- When `MyClass.regular_method()` is called, it works as expected because no instance is involved, and the method doesn’t expect any parameters.
- When `obj.regular_method()` is called, Python implicitly passes the instance `self` as the first argument. Since `regular_method` doesn’t accept any arguments, this results in a `TypeError`.

Key Points:
- Defining a method without self and without the `@staticmethod` decorator allows it to be called directly on the class but not on its instances.
- To define a method that can be called on both the class and its instances, you must use the `@staticmethod` decorator (see belows).

### Defining a Method WITH the `@staticmethod` Decorator

By using the `@staticmethod` decorator, you define a method that doesn’t operate on an instance or the class itself. 
Such methods don’t receive an implicit first argument and can be called on the class or its instances. Basically it "disables" the standard instance method behavior.

```python
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")

# Calling the static method on the class
MyClass.static_method()  # Output: This is a static method.

# Calling the static method on an instance
obj = MyClass()
obj.static_method()  # Output: This is a static method.
```

## Naming Conventions

Before continuing diving into classes, you’ll need to be aware of some important naming conventions that Python uses in the context of classes. 

### Public vs Non-Public Members

Python **doesn’t distinguish** between private, protected, and public attributes like Java and other languages do. 
In Python, all attributes are accessible in one way or another.

However, Python has a well-established naming convention that you should use to communicate that an attribute or method isn’t intended for use from outside its containing class or object. The naming convention consists of adding a leading underscore to the member’s name. So, in a Python class, you’ll have the following conventions:

- **Public Members**: Use the normal naming pattern (`radius`, `calculate_area()`)
- **Non-public Members**: Include a leading underscore in names (`_radius`, `_calculate_area()`)

> [!WARNING] 
> - This is just a convention. It doesn’t actually prevent access to the members.
> - Nonetheless, it’s a good practice to follow this convention to communicate that an attribute or method isn’t intended for use from outside its containing class or object. 
> - Non-public members exist only to support the internal implementation of a given class and the owner of the class may remove them at any time, so you shouldn’t rely on such attributes and methods.


### Name Mangling

In Python, name mangling is a mechanism that alters the names of class attributes with double leading underscores to include the class name. This process helps prevent accidental access and modification of private attributes, especially in the context of inheritance.

How Name Mangling Works:

When you define a class attribute with two leading underscores (e.g., __attribute), Python transforms its name by prefixing it with a single underscore and the class name. For instance, in a class named MyClass, an attribute __attribute becomes _MyClass__attribute. This transformation makes it harder to access the attribute directly from outside the class, promoting encapsulation.

Example:

```python
class MyClass:
    def __init__(self):
        self.__private_attr = "I am private"

    def get_private_attr(self):
        return self.__private_attr

obj = MyClass()
print(obj.get_private_attr())  # Output: I am private
print(obj.__private_attr)      # Raises AttributeError
```

While name mangling adds a layer of protection, it doesn’t make the attribute completely inaccessible. You can still access it using its mangled name:

```python
print(obj._MyClass__private_attr)  # Output: I am private
```

However, doing so is generally discouraged as it breaks the intended encapsulation.

### Purpose of Name Mangling

The primary purpose of name mangling is to prevent naming conflicts in subclasses. For example, if both a parent class and a child class define an attribute with the same name prefixed by double underscores, name mangling ensures that they are treated as distinct attributes.

Example with Inheritance:

```python
class Parent:
    def __init__(self):
        self.__attr = "Parent attribute"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__attr = "Child attribute"

obj = Child()
print(obj._Parent__attr)  # Output: Parent attribute
print(obj._Child__attr)   # Output: Child attribute
```

In this scenario, Parent and Child each have their own __attr attribute, and name mangling prevents them from clashing.

Important Considerations:
- Name mangling applies only to attributes with at least two leading underscores and at most one trailing underscore. Attributes with a single leading underscore (e.g., `_attribute`) are not mangled and are considered protected by convention.
- Attributes with double leading and trailing underscores (e.g., `__init__`) are special methods or “dunder” methods and are not subject to name mangling.

By understanding and utilizing name mangling, you can create classes with private attributes that are less prone to accidental access or modification, especially in complex inheritance hierarchies.

## Deciding When to Avoid Classes

Python classes are pretty cool and powerful tools that you can use in multiple scenarios. Because of this, some people tend to overuse classes and solve all their coding problems using them. However, sometimes using a class isn't the best solution. Sometimes, a [module](https://realpython.com/python-modules-packages/) with a couple of functions is enough.

In practice, you'll encounter a few situations in which you should avoid classes. For example, you shouldn't use regular classes when you need to:

-   Store **only data**. Use a [data class](https://realpython.com/python-data-classes/), [enumeration](https://realpython.com/python-enum/), or a [named tuple](https://realpython.com/python-namedtuple/) instead.
-   Provide a **single method**. Use a [function](https://realpython.com/defining-your-own-python-function/) instead.

Data classes, enumerations, and named tuples are specially designed to store data. So, they might be the best solution if your class doesn't have any behavior attached.

If your class has a single method in its API, then you may not require a class. Instead, use a function unless you need to retain a certain state between calls. If more methods appear later, then you can always create a class. Remember this principle from the [Zen of Python](https://realpython.com/zen-of-python/):

> [!NOTE] Simple is better than complex. ([Source](https://peps.python.org/pep-0020/))

Additionally, you should avoid creating custom classes to wrap up functionality that's available through built-in types or third-party classes. Use the type or third-party class directly.

You'll find many other situations where you may not need to use classes in your Python code. For example, classes may be unnecessary when you're working with:

-   A small and **simple program** or **script** that doesn't require complex data structures or logic. In this case, using classes may be overkill.
-   A **performance-critical** program. Classes add overhead to your program, especially when you need to create many objects. This may affect your code's general performance.
-   A **legacy codebase**. If an existing codebase doesn't use classes, then you shouldn't introduce them. This will break the current coding style and disrupt the code's consistency.
-   A team with a **different coding style**. If your current team doesn't use classes, then stick with their coding style. This will ensure consistency across the project.
-   A codebase that uses **functional programming**. If a given codebase is currently written with a [functional](https://realpython.com/python-functional-programming/) approach, then you shouldn't introduce classes. This will break the underlying coding paradigm.

You may find yourself in many other situations where using classes will be overkill. Classes are great, but don't turn them into a one-size-fits-all type of tool. Start your code as simply as possible. If the need for a class appears, then go for it.


## The `__dict__` Attribute

> [!TODO]: Are there practical examples of using `__dict__`? The Django settings codebase uses it.

In Python, both classes and instances have a special attribute called [`.__dict__`](https://docs.python.org/3/library/stdtypes.html#object.__dict__).
It is a dictionary containing the **writable members** of the underlying class or instance. 
Remember, these members can be attributes or methods. Each key in `.__dict__` represents an attribute name. 

The value associated with a given key represents the value of the corresponding attribute.

In a class, `.__dict__` will contain class attributes and methods. In an instance, `.__dict__` will hold instance attributes.

When you access a **class member through the class object**, Python automatically searches for the member's name in the class `.__dict__`.

If the name isn't there, then you get an `AttributeError`.

Similarly, when you access an **instance member through a concrete instance of a class**:
- Python looks for the member's name in the instance `.__dict__`.
- If the name doesn't appear there, then Python looks in the class `.__dict__`.
- If the name isn't found, then you get a `NameError`.

Here's a toy class that illustrates how this mechanism works:

```python
# sample_dict.py
class SampleClass:
    class_attr = 100

    def __init__(self, instance_attr):
        self.instance_attr = instance_attr

    def method(self):
        print(f"Class attribute: {self.class_attr}")
        print(f"Instance attribute: {self.instance_attr}")
`
```

In this class, you define a class attribute with a value of `100`. In the `.__init__()` method, you define an instance attribute that takes its value from the user's input. Finally, you define a method to print both attributes.

Now it's time to check the content of `.__dict__` in the class object. Go ahead and run the following code:

Python

```python
>>> from sample_dict import SampleClass

>>> SampleClass.class_attr
100

>>> SampleClass.__dict__
mappingproxy({
    '__module__': '__main__',
    'class_attr': 100,
    '__init__': <function SampleClass.__init__ at 0x1036c62a0>,
    'method': <function SampleClass.method at 0x1036c56c0>,
    '__dict__': <attribute '__dict__' of 'SampleClass' objects>,
    '__weakref__': <attribute '__weakref__' of 'SampleClass' objects>,
    '__doc__': None
})

>>> SampleClass.__dict__["class_attr"]
100
```

Both the class attribute `class_attr` and the `method` are in the class `.__dict__` dictionary. 

Note how you can use `.__dict__` to access the value of class attributes by specifying the attribute's name in square brackets, as you usually access keys in a [dictionary](https://realpython.com/python-dicts/#accessing-dictionary-values).

**Note:** You can access the same dictionary by calling the built-in [`vars()`](https://realpython.com/python-built-in-functions/#checking-names-and-attributes-dir-and-vars) function on your class or instance, as you did before.

```python
>>> vars(SampleClass)
mappingproxy({'__module__': '__main__', 'class_attr': 100, 'method': <function SampleClass.method at 0x1036c56c0>, '__dict__': <attribute '__dict__' of 'SampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'SampleClass' objects>, '__doc__': None})
```

In instances, the `.__dict__` dictionary will contain instance attributes only:

```python
>>> instance = SampleClass("Hello!")

>>> instance.instance_attr
'Hello!'
>>> instance.method()
Class attribute: 100
Instance attribute: Hello!

>>> instance.__dict__
{'instance_attr': 'Hello!'}
>>> instance.__dict__["instance_attr"]
'Hello!'

>>> instance.__dict__["instance_attr"] = "Hello, Pythonista!"
>>> instance.instance_attr
'Hello, Pythonista!'
```

The instance `.__dict__` dictionary in this example holds `.instance_attr` and its specific value for the object at hand. 

Again, you can access any existing instance attribute using `.__dict__` and the attribute name in square brackets.

You can modify the instance `.__dict__` dynamically. This means that you can change the value of existing instance attributes through `.__dict__`, as you did in the final example above. 

You can even add new attributes to an instance using its `.__dict__` dictionary.

Using `.__dict__` to change the value of instance attributes will allow you to avoid [`RecursionError`](https://realpython.com/python-built-in-exceptions/#recursionerror) exceptions when you're wiring [descriptors](https://realpython.com/python-descriptors/) in Python. You'll learn more about descriptors in the [Property and Descriptor-Based Attributes](https://realpython.com/python-classes/#property-and-descriptor-based-attributes) section.


## Dynamic Class and Instance Attributes

In Python, you can add new attributes to your classes and instances dynamically: 

For example, say that you’ve read a row of data from an employees.csv file using csv.DictReader. This class reads the data and returns it in a dictionary-like object. Now suppose that you have the following dictionary of data:

```python
>>> john = {
...     "name": "John Doe",
...     "position": "Python Developer",
...     "department": "Engineering",
...     "salary": 80000,
...     "hire_date": "2020-01-01",
...     "is_manager": False,
... }
```

Next, you want to add this data to an instance of your Record class, and you need to represent each data field as an instance attribute. Here’s how you can do it:

```python
>>> john_record = Record()

>>> for field, value in john.items():
...     setattr(john_record, field, value)
...

>>> john_record.name
'John Doe'
>>> john_record.department
'Engineering'

>>> john_record.__dict__
{
    'name': 'John Doe',
    'position': 'Python Developer',
    'department': 'Engineering',
    'salary': 80000,
    'hire_date': '2020-01-01',
    'is_manager': False
}
```

For detailed explanation: [SEE HERE](https://realpython.com/python-classes/#dynamic-class-and-instance-attributes)

## TBD

### Property and Descriptor-Based Attributes

For detailed explanation: [SEE HERE](https://realpython.com/python-classes/#property-and-descriptor-based-attributes)

Python allows you to add function-like behavior on top of existing instance attributes and turn them into managed attributes. This type of attribute prevents you from introducing breaking changes into your APIs.

In other words, with managed attributes, you can have function-like behavior and attribute-like access at the same time. You don’t need to change your APIs by replacing attributes with method calls, which can potentially break your users’ code.

To create a managed attribute with function-like behavior in Python, you can use either a property or a descriptor, depending on your specific needs.

Note: To dive deeper into Python properties, check out Python’s property(): Add Managed Attributes to Your Classes.

As an example, get back to your Circle class and say that you need to validate the radius to ensure that it only stores positive numbers. How would you do that without changing your class interface? The quickest approach to this problem is to use a property and implement the validation logic in the setter method.

Here’s what your new version of Circle can look like:

circle.py
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("positive number expected")
        self._radius = value

    def calculate_area(self):
        return math.pi * self._radius**2
To turn an existing attribute like .radius into a property, you typically use the @property decorator to write the getter method. The getter method must return the value of the attribute. In this example, the getter returns the circle’s radius, which is stored in the non-public ._radius attribute.

Note: The pipe sign (|) in the call to isinstance() expresses union types. You can use this syntax in Python 3.10 or greater. If you’re using a lower version of Python, then you can use a tuple of types (int, float).

To define the setter method of a property-based attribute, you need to use the decorator @attr_name.setter. In the example, you use @radius.setter. Then you need to define the method itself. Note that property setters need to take an argument providing the value that you want to store in the underlying attribute.

Inside the setter method, you use a conditional to check whether the input value is an integer or a floating-point number. You also check if the value is less than or equal to 0. If either is true, then you raise a ValueError with a descriptive message about the actual issue. Finally, you assign value to ._radius, and that’s it. Now, .radius is a property-based attribute.

Here’s an example of this new version of Circle in action:

>>> from circle import Circle

>>> circle_1 = Circle(100)
>>> circle_1.radius
100
>>> circle_1.radius = 500
>>> circle_1.radius = 0
Traceback (most recent call last):
    ...
ValueError: positive number expected

>>> circle_2 = Circle(-100)
Traceback (most recent call last):
    ...
ValueError: positive number expected

>>> circle_3 = Circle("300")
Traceback (most recent call last):
    ...
ValueError: positive number expected
The first instance of Circle in this example takes a valid value for its radius. Note how you can continue working with .radius as a regular attribute rather than as a method. If you try to assign an invalid value to .radius, then you get a ValueError exception.

Note: Remember to reload the circle.py module if you’re working on the same REPL session as before. This recommendation will also be valid for all the examples in this tutorial where you change modules that you defined in previous examples.

It’s important to note that the validation also runs at instantiation time when you call the class constructor to create new instances of Circle. This behavior is consistent with your validation strategy.

Using a descriptor to create managed attributes is another powerful way to add function-like behavior to your instance attributes without changing your APIs. Like properties, descriptors can also have getter, setter, and other types of methods.

Note: To learn more about descriptors and how to use them, check out Python Descriptors: An Introduction.

To explore how descriptors work, say that you’ve decided to continue creating classes for your drawing application, and now you have the following Square class:

square.py
class Square:
    def __init__(self, side):
        self.side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("positive number expected")
        self._side = value

    def calculate_area(self):
        return self._side**2
This class uses the same pattern as your Circle class. Instead of using radius, the Square class takes a side argument and computes the area using the appropriate expression for a square.

This class is pretty similar to Circle, and the repetition starts looking odd. Then you think of using a descriptor to abstract away the validation process. Here’s what you come up with:

shapes.py
import math

class PositiveNumber:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("positive number expected")
        instance.__dict__[self._name] = value

class Circle:
    radius = PositiveNumber()

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

class Square:
    side = PositiveNumber()

    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side**2
The first thing to notice in this example is that you moved all the classes to a shapes.py file. In that file, you define a descriptor class called PositiveNumber by implementing the .__get__() and .__set__() special methods, which are part of the descriptor protocol.

Next, you remove the .radius property from Circle and the .side property from Square. In Circle, you add a .radius class attribute, which holds an instance of PositiveNumber. You do something similar in Square, but the class attribute is appropriately named .side.

Here are a few examples of how your classes work now:

>>> from shapes import Circle, Square

>>> circle = Circle(100)
>>> circle.radius
100
>>> circle.radius = 500
>>> circle.radius
500
>>> circle.radius = 0
Traceback (most recent call last):
    ...
ValueError: positive number expected

>>> square = Square(200)
>>> square.side
200
>>> square.side = 300
>>> square.side
300
>>> square = Square(-100)
Traceback (most recent call last):
    ...
ValueError: positive number expected
Python descriptors provide a powerful tool for adding function-like behavior on top of your instance attributes. They can help you remove repetition from your code, making it cleaner and more maintainable. They also promote code reuse.


### Lightweight Classes With `.__slots__`

For detailed explanation: [SEE HERE](https://realpython.com/python-classes/#lightweight-classes-with-__slots__)

In a Python class, using the .__slots__ attribute can help you reduce the memory footprint of the corresponding instances. This attribute prevents the automatic creation of an instance .__dict__. Using .__slots__ is particularly handy when you have a class with a fixed set of attributes, and you’ll use that class to create a large number of objects.

In the example below, you have a Point class with a .__slots__ attribute that consists of a tuple of allowed attributes. Each attribute will represent a Cartesian coordinate:

>>> class Point:
...     __slots__ = ("x", "y")
...     def __init__(self, x, y):
...         self.x = x
...         self.y = y
...

>>> point = Point(4, 8)
>>> point.__dict__
Traceback (most recent call last):
    ...
AttributeError: 'Point' object has no attribute '__dict__'
This Point class defines .__slots__ as a tuple with two items. Each item represents the name of an instance attribute. So, they must be strings holding valid Python identifiers.

Note: Although .__slots__ can hold a list object, you should use a tuple object instead. Even if changing the list in .__slots__ after processing the class body had no effect, it’d be misleading to use a mutable sequence there.

Instances of your Point class don’t have a .__dict__, as the code shows. This feature makes them memory-efficient. To illustrate this efficiency, you can measure the memory consumption of an instance of Point. To do this, you can use the Pympler library, which you can install from PyPI using the python -m pip install pympler command.

Once you’ve installed Pympler with pip, then you can run the following code in your REPL:

>>> from pympler import asizeof

>>> asizeof.asizeof(Point(4, 8))
112
The asizeof() function from Pympler says that the object Point(4, 8) occupies 112 bytes in your computer’s memory. Now get back to your REPL session and redefine Point without providing a .__slots__ attribute. With this update in place, go ahead and run the memory check again:

>>> class Point:
...     def __init__(self, x, y):
...         self.x = x
...         self.y = y

>>> asizeof.asizeof(Point(4, 8))
528
The same object, Point(4, 8), now consumes 528 bytes of memory. This number is over four times greater than what you got with the original implementation of Point. Imagine how much memory .__slots__ would save if you had to create a million points in your code.

The .__slots__ attribute adds a second interesting behavior to your custom classes. It prevents you from adding new instance attributes dynamically:

>>> class Point:
...     __slots__ = ("x", "y")
...     def __init__(self, x, y):
...         self.x = x
...         self.y = y
...

>>> point = Point(4, 8)
>>> point.z = 16
Traceback (most recent call last):
    ...
AttributeError: 'Point' object has no attribute 'z'
Adding a .__slots__ to your classes allows you to provide a series of allowed attributes. This means that you won’t be able to add new attributes to your instances dynamically. If you try to do it, then you’ll get an AttributeError exception.

A word of caution is in order, as many of Python’s built-in mechanisms implicitly assume that objects have the .__dict__ attribute. When you use .__slots__(), then you waive that assumption, which means that some of those mechanisms might not work as expected anymore.






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
