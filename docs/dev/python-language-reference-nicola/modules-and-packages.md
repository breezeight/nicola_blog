
# Modules and Packages in Python

In Python, a **module** is a file containing Python code, such as functions, classes, and variables, that can be reused in other programs. Modules help organize and structure your code, making it easier to maintain and reuse functionality. A module is typically a single .py file, and you can import it into your program using the import statement:

```python
# Example of importing and using a module   
import math
print(math.sqrt(16))  # Outputs: 4.0
```

In addition to single-file modules, Python also supports **packages**, which are directories that group multiple related modules together under a common namespace. A package allows you to organize code hierarchically for larger projects. A directory is treated as a package if it contains an `__init__.py` file (in Python 3.3 and later, this file is optional but recommended for clarity).

**Example of a Package Structure:**

```bash
my_package/
    __init__.py
    module1.py
    module2.py
    sub_package/
        __init__.py
        sub_module.py
```

- `my_package` is a package (a directory containing Python modules).
- `module1` and `module2` are modules within the package.
- `sub_package` is a sub-package within `my_package`, containing its own module (`sub_module`).

Importing from a package works exactly like importing from a module:

```python
# Importing a module from a package
import my_package.module1

# Using a function or variable from the module
my_package.module1.some_function()

# Importing directly from a package
from my_package import module2
module2.another_function()

# Accessing sub-packages
import my_package.sub_package.sub_module
my_package.sub_package.sub_module.some_sub_function()
```

Some real-world examples:

```python
# You can import modules
import math
print(math.sqrt(16))  # => 4.0

# You can get specific functions from a module
from math import ceil, floor
print(ceil(3.7))   # => 4
print(floor(3.7))  # => 3

# You can import all functions from a module.
# Warning: this is not recommended
from math import *

# You can shorten module names
import math as m
math.sqrt(16) == m.sqrt(16)  # => True

# Python modules are just ordinary Python files. You
# can write your own, and import them. The name of the
# module is the same as the name of the file.

# You can find out which functions and attributes
# are defined in a module.
import math
dir(math)

# If you have a Python script named math.py in the same
# folder as your current script, the file math.py will
# be loaded instead of the built-in Python module.
# This happens because the local folder has priority
# over Python's built-in libraries.
```


ref: [https://realpython.com/python-modules-packages/](https://realpython.com/python-modules-packages/)

There are actually three different ways to define a module in Python:

1. A module can be written in Python itself.
2. A module can be written in C and loaded dynamically at run-time, like the re ([regular expression](https://realpython.com/regex-python/)) module.
3. A built-in module is intrinsically contained in the interpreter, like the [itertools](https://realpython.com/python-itertools/) module.

A module's contents are accessed the same way in all three cases: with the import statement.

Here, the focus will mostly be on modules that are written in Python. The cool thing about modules written in Python is that they are exceedingly straightforward to build. All you need to do is create a file that contains legitimate Python code and then give the file a name with a .py extension. That's it! No special syntax or voodoo is necessary.

## Create and use a basic module

For example, suppose you have created a file called `mod.py` containing the following:

```python
# mod.py
s = "If Comrade Napoleon says it, it must be right."
a = [100, 200, 300]

def foo(arg):
    print(f'arg = {arg}')

class Foo:
    pass
```

Several objects are defined in mod.py:

- `s` (a string)
- `a` (a list)
- `foo()` (a function)
- `Foo` (a class)

Let's write a `main.py` that import `mod.py` and uses `foo()`. Assuming `mod.py` is in an appropriate location, which you will learn more about shortly (**for now keep both in the same folder**), these objects can be accessed by importing the module as follows:

```python
import mod

print(mod.s)
print(mod.a)
mod.foo(['quux', 'corge', 'grault'])
x = mod.Foo()
print(x)
```

Running `python main.py` will print:

```
If Comrade Napoleon says it, it must be right.
[100, 200, 300]
arg = ['quux', 'corge', 'grault']
<mod.Foo object at 0x1054c7010>
```

## Python Packages

Ref: [https://docs.python.org/3/tutorial/modules.html#packages](https://docs.python.org/3/tutorial/modules.html#packages)

A **Python package** is a way of organizing related modules into a single directory hierarchy. Essentially, a package is a directory containing one or more modules and a special file `__init__.py` (which can be empty and was required until python 3.3). This structure allows for a modular, easily navigable namespace for the modules.

Essentially in modern python, creating a Python package is as simple as creating a directory with Python modules.

Packages are a way of structuring Python's module namespace by using **dotted module names**. For example, the module name `A.B` designates a submodule named `B` in a package named `A`. 

Just like the use of modules saves the authors of different modules from having to worry about each other's global variable names, the use of dotted module names saves the authors of multi-module packages like NumPy or Pillow from having to worry about each other's module names.

Suppose you want to design a collection of modules (a "package") for the uniform handling of sound files and sound data. There are many different sound file formats (usually recognized by their extension, for example: .wav, .aiff, .au), so you may need to create and maintain a growing collection of modules for the conversion between the various file formats. There are also many different operations you might want to perform on sound data (such as mixing, adding echo, applying an equalizer function, creating an artificial stereo effect), so in addition you will be writing a never-ending stream of modules to perform these operations. Here's a possible structure for your package (expressed in terms of a hierarchical filesystem):

```bash
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...

      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```
When importing the package, Python searches through the directories on sys.path looking for the package subdirectory.

### Usage of Packages

Users of the package can import individual modules from the package, for example:

```python
import sound.effects.echo
```

This loads the submodule `sound.effects.echo`. It must be referenced with its full name.

```python
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

An alternative way of importing the submodule is:

```python
from sound.effects import echo
```

This also loads the submodule echo, and makes it available without its package prefix, so it can be used as follows:

```python
echo.echofilter(input, output, delay=0.7, atten=4)
```

Yet another variation is to import the desired function or variable directly:

```python
from sound.effects.echo import echofilter
```

Again, this loads the submodule echo, but this makes its function echofilter() directly available:

```python
echofilter(input, output, delay=0.7, atten=4)
```

Note that when using `from package import item`, the item can be either a submodule (or subpackage) of the package, or some other name defined in the package, like a function, class or variable. The import statement first tests whether the item is defined in the package; if not, it assumes it is a module and attempts to load it. If it fails to find it, an [ImportError](https://docs.python.org/3/library/exceptions.html#ImportError) exception is raised.

Contrarily, when using syntax like import item.subitem.subsubitem, each item except for the last must be a package; the last item can be a module or a package but can't be a class or function or variable defined in the previous item.

### 6.1.2. The Module Search Path -  sys.path

How It Works:

When a module named spam is imported, the interpreter first searches for a built-in module with that name. These module names are listed in [sys.builtin_module_names](https://docs.python.org/3/library/sys.html#sys.builtin_module_names). If not found, it then searches for a file named spam.py in a list of directories given by the variable [sys.path](https://docs.python.org/3/library/sys.html#sys.path).

Python's import machinery looks through the directories on **sys.path** for a module or package name. If it finds a directory with the matching name and:

* if an `__init__.py` is available it is used.

* it has **no** `__init__.py`, it creates a namespace package automatically.

`sys.path` is initialized from these locations:

* The directory containing the input script (or the current directory when no file is specified).

* [PYTHONPATH](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH) (a list of directory names, with the same syntax as the shell variable PATH).

* The installation-dependent default (by convention including a site-packages directory, handled by the [site](https://docs.python.org/3/library/site.html#module-site) module).

```python
>>> import sys
>>> sys.path
['', '/Users/nicolabrisotto/.asdf/installs/python/3.10.4/lib/python310.zip', '/Users/nicolabrisotto/.asdf/installs/python/3.10.4/lib/python3.10', '/Users/nicolabrisotto/.asdf/installs/python/3.10.4/lib/python3.10/lib-dynload', '/Users/nicolabrisotto/.asdf/installs/python/3.10.4/lib/python3.10/site-packages']
```

More details are at [The initialization of the sys.path module search path](https://docs.python.org/3/library/sys_path_init.html#sys-path-init).

> [!NOTE] On file systems which support symlinks, the directory containing the input script is calculated after the symlink is followed. In other words the directory containing the symlink is **not** added to the module search path.

After initialization, Python programs can modify [sys.path](https://docs.python.org/3/library/sys.html#sys.path). The directory containing the script being run is placed at the beginning of the search path, ahead of the standard library path. This means that scripts in that directory will be loaded instead of modules of the same name in the library directory. This is an error unless the replacement is intended. See section [Standard Modules](https://docs.python.org/3/tutorial/modules.html#tut-standardmodules) for more information.

### What is `__init__.py` ?

ref: [https://betterstack.com/community/questions/what-is-init-py-for/](https://betterstack.com/community/questions/what-is-init-py-for/)

In Python, the `__init__.py` file is used to **mark a directory as a Python package**. It is used to initialize the package when it is imported.

The `__init__.py` file can contain code that will be executed when the package is imported, as well as function definitions and variable assignments. It is a good place to put any code that you want to run when the package is first imported.

For example, suppose you have a package called mypackage with the following structure:

```bash
mypackage/
    __init__.py
    module1.py
    module2.py
    ...
```

If you want to import module1 from mypackage, you can do so using the following import statement:

```python
import mypackage.module1
```

When you run this import statement, Python will execute the code in `__init__.py` before it executes the import statement for module1. This can be useful if you want to do some initialization or setup before the other modules in the package are imported.

#### Use-case: Namespace Management

`__init__.py` can be used to define what symbols the package exports. This is done using the `__all__` variable, which lists the names of modules and subpackages that should be imported when `from package import *` is used.

```python
# In __init__.py
__all__ = ["module1", "module2"]
```

More on this on the official guide ⇒\[https://docs.python.org/3/tutorial/modules.html\\#importing-from-a-package\](https://docs.python.org/3/tutorial/modules.html#importing-from-a-package)

Convenience Imports: It's common to use \\\_\\\_init\\\_\\\_.py to facilitate easier imports for the package users. For instance, if your package has a module module1, you can import its classes or functions in \\\_\\\_init\\\_\\\_.py so that users can access them directly from the package level.

```python
# In __init__.py
from .module1 import SomeClass, some_function
```

This allows users to do `from package import SomeClass, some_function` instead of `from package.module1 import SomeClass, some_function`.

#### Multiple `__init__.py`

It is also possible to have multiple levels of packages, with \\\_\\\_init\\\_\\\_.py files at each level. For example:

```bash
mypackage/
    __init__.py
    subpackage1/
        __init__.py
        module1.py
        module2.py
        ...
    subpackage2/
        __init__.py
        module1.py
        module2.py
        ...
```
In this case, you would import a module from subpackage1 using the following import statement:

```python
import mypackage.subpackage1.module1
```

Again, the code in the `__init__.py` files for mypackage and subpackage1 would be executed before the import statement for module1 is executed.

#### Best Practices

* **Keep it Light**: Typically, it's a good practice to keep `__init__.py` lightweight to avoid unnecessary loading of additional dependencies when parts of the package are imported.

* **Explicit is Better Than Implicit**: Following the Zen of Python, explicit imports in `__init__.py` can make it clear what the package is providing.

### Changes in Python 3.3 and Later

With Python 3.3 and the introduction of Implicit Namespace Packages (PEP 420), the `__init__.py` file is no longer required to define a directory as a package. This change allows for the creation of namespace packages, which are a way to spread a package across multiple directories. However, `__init__.py` is still widely used for the reasons mentioned above and remains a key part of structuring traditional Python packages.
