# Python Scopes and Namespaces

Let's begin with some definitions: 

* A **namespace** is a mapping from names to objects. Most namespaces are currently implemented as Python dictionaries, but that's normally not noticeable in any way (except for performance), and it may change in the future. Examples of namespaces are: 
  - the set of built-in names (containing functions such as [`abs()`](https://docs.python.org/3/library/functions.html#abs "abs"), and built-in exception names); 
  - the global names in a module; 
  - the local names in a function invocation. 
  - In a sense the set of attributes of an object also form a namespace. 
  - The important thing to know about namespaces is that there is absolutely no relation between names in different namespaces; for instance, two different modules may both define a function `maximize` without confusion --- users of the modules must prefix it with the module name.

* **attribute**: I use the word *attribute* for any name following a dot --- for example, in the expression `z.real`, `real` is an attribute of the object `z`. Strictly speaking, references to names in modules are attribute references: in the expression `modname.funcname`, `modname` is a module object and `funcname` is an attribute of it. In this case there happens to be a straightforward mapping between the module's attributes and the global names defined in the module: they share the same namespace! [1](https://docs.python.org/3/tutorial/classes.html#id2)

Attributes may be read-only or writable. In the latter case, assignment to attributes is possible. Module attributes are writable: you can write `modname.the_answer=42`. Writable attributes may also be deleted with the [`del`](https://docs.python.org/3/reference/simple_stmts.html#del) statement. For example, `del modname.the_answer` will remove the attribute `the_answer` from the object named by `modname`.


## Namespaces Lifetime

Namespaces are created at different moments and have different lifetimes:
- The namespace containing the built-in names is created when the Python interpreter starts up, and is never deleted. 
- The global namespace for a module is created when the module definition is read in; normally, module namespaces also last until the interpreter quits.
- The statements executed by the top-level invocation of the interpreter, either read from a script file or interactively, are considered part of a module called [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__), so they have their own global namespace. (The built-in names actually also live in a module; this is called [builtins](https://docs.python.org/3/library/builtins.html#module-builtins)).

- The local namespace for a function is created when the function is called, and deleted when the function returns or raises an exception that is not handled within the function. (Actually, forgetting would be a better way to describe what actually happens.) Of course, recursive invocations each have their own local namespace.

## Scopes

A **scope** is a textual region of a Python program where a namespace is directly accessible. "Directly accessible" here means that an unqualified reference to a name attempts to find the name in the namespace.

Although scopes are determined statically, they are used dynamically. At any time during execution, there are 3 or 4 nested scopes whose namespaces are directly accessible:

-   the innermost scope, which is searched first, contains the local names
-   the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contain non-local, but also non-global names
-   the next-to-last scope contains the current module's global names
-   the outermost scope (searched last) is the namespace containing built-in names

If a name is declared global, then all references and assignments go directly to the next-to-last scope containing the module's global names. To rebind variables found outside of the innermost scope, the [`nonlocal`](https://docs.python.org/3/reference/simple_stmts.html#nonlocal) statement can be used; if not declared nonlocal, those variables are read-only (an attempt to write to such a variable will simply create a *new* local variable in the innermost scope, leaving the identically named outer variable unchanged). See more examples here: [functions](functions.md#how-scopes-and-namespaces-apply-to-functions).

Usually, the local scope references the local names of the (textually) current function. Outside functions, the local scope references the same namespace as the global scope: the module's namespace. Class definitions place yet another namespace in the local scope.

It is important to realize that scopes are determined textually: the global scope of a function defined in a module is that module's namespace, no matter from where or by what alias the function is called. On the other hand, the actual search for names is done dynamically, at run time --- however, the language definition is evolving towards static name resolution, at "compile" time, so don't rely on dynamic name resolution! (In fact, local variables are already determined statically.)

A special quirk of Python is that -- if no [`global`](https://docs.python.org/3/reference/simple_stmts.html#global) or [`nonlocal`](https://docs.python.org/3/reference/simple_stmts.html#nonlocal) statement is in effect -- assignments to names always go into the innermost scope. Assignments do not copy data --- they just bind names to objects. The same is true for deletions: the statement `del x` removes the binding of `x` from the namespace referenced by the local scope. In fact, all operations that introduce new names use the local scope: in particular, [`import`](https://docs.python.org/3/reference/simple_stmts.html#import) statements and function definitions bind the module or function name in the local scope.

The [`global`](https://docs.python.org/3/reference/simple_stmts.html#global) statement can be used to indicate that particular variables live in the global scope and should be rebound there; the [`nonlocal`](https://docs.python.org/3/reference/simple_stmts.html#nonlocal) statement indicates that particular variables live in an enclosing scope and should be rebound there.

### 9.2.1. Scopes and Namespaces Example

This is an example demonstrating how to reference the different scopes and namespaces, and how [`global`](https://docs.python.org/3/reference/simple_stmts.html#global) and [`nonlocal`](https://docs.python.org/3/reference/simple_stmts.html#nonlocal) affect variable binding:

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```

The output of the example code is:

```bash
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam

```

Note how the *local* assignment (which is default) didn't change `scope_test` binding of `spam`. The [`nonlocal`](https://docs.python.org/3/reference/simple_stmts.html#nonlocal) assignment changed `scope_test`'s binding of `spam`, and the [`global`](https://docs.python.org/3/reference/simple_stmts.html#global) assignment changed the module-level binding.

You can also see that there was no previous binding for `spam` before the [`global`](https://docs.python.org/3/reference/simple_stmts.html#global) assignment.

## How scopes and namespaces apply to classes

See Nicola's notes [classes](classes-and-objects.md#how-scopes-and-namespaces-apply-to-classes)

## How scopes and namespaces apply to functions

See Nicola's notes [functions](functions.md#how-scopes-and-namespaces-apply-to-functions)