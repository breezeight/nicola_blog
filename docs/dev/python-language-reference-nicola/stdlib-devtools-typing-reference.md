
Reference:
* [Mypy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

## Scope of this document

This document is a quick cheat sheet showing how to use type annotations for various common types in Python. It's intended to be used as a quick reference for what we used more and integrate the official documentation without replacing it.

## Complete reference

* [See the Mypy documentation](https://mypy.readthedocs.io/en/stable/type_inference_and_annotations.html)

* [Official typing module documentation](https://docs.python.org/3/library/typing.html#module-contents)

-   [Module contents](https://docs.python.org/3/library/typing.html#module-contents)
    -   [Special typing primitives](https://docs.python.org/3/library/typing.html#special-typing-primitives)
        -   [Special types](https://docs.python.org/3/library/typing.html#special-types)
            -   [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)
            -   [`AnyStr`](https://docs.python.org/3/library/typing.html#typing.AnyStr)
            -   [`LiteralString`](https://docs.python.org/3/library/typing.html#typing.LiteralString)
            -   [`Never`](https://docs.python.org/3/library/typing.html#typing.Never)
            -   [`NoReturn`](https://docs.python.org/3/library/typing.html#typing.NoReturn)
            -   [`Self`](https://docs.python.org/3/library/typing.html#typing.Self)
            -   [`TypeAlias`](https://docs.python.org/3/library/typing.html#typing.TypeAlias)
        -   [Special forms](https://docs.python.org/3/library/typing.html#special-forms)
            -   [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)
            -   [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)
            -   [`Concatenate`](https://docs.python.org/3/library/typing.html#typing.Concatenate)
            -   [`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal)
            -   [`ClassVar`](https://docs.python.org/3/library/typing.html#typing.ClassVar)
            -   [`Final`](https://docs.python.org/3/library/typing.html#typing.Final)
            -   [`Required`](https://docs.python.org/3/library/typing.html#typing.Required)
            -   [`NotRequired`](https://docs.python.org/3/library/typing.html#typing.NotRequired)
            -   [`ReadOnly`](https://docs.python.org/3/library/typing.html#typing.ReadOnly)
            -   [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated)
            -   [`TypeIs`](https://docs.python.org/3/library/typing.html#typing.TypeIs)
            -   [`TypeGuard`](https://docs.python.org/3/library/typing.html#typing.TypeGuard)
            -   [`Unpack`](https://docs.python.org/3/library/typing.html#typing.Unpack)
        -   [Building generic types and type aliases](https://docs.python.org/3/library/typing.html#building-generic-types-and-type-aliases)
            -   [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic)
            -   [`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar)
                -   [`__name__`](https://docs.python.org/3/library/typing.html#typing.TypeVar.__name__)
                -   [`__covariant__`](https://docs.python.org/3/library/typing.html#typing.TypeVar.__covariant__)
                -   [`__contravariant__`](https://docs.python.org/3/library/typing.html#typing.TypeVar.__contravariant__)
                -   [`__infer_variance__`](https://docs.python.org/3/library/typing.html#typing.TypeVar.__infer_variance__)
                -   [`__bound__`](https://docs.python.org/3/library/typing.html#typing.TypeVar.__bound__)
                -   [`__constraints__`](https://docs.python.org/3/library/typing.html#typing.TypeVar.__constraints__)
                -   [`__default__`](https://docs.python.org/3/library/typing.html#typing.TypeVar.__default__)
                -   [`has_default()`](https://docs.python.org/3/library/typing.html#typing.TypeVar.has_default)
            -   [`TypeVarTuple`](https://docs.python.org/3/library/typing.html#typing.TypeVarTuple)
                -   [`__name__`](https://docs.python.org/3/library/typing.html#typing.TypeVarTuple.__name__)
                -   [`__default__`](https://docs.python.org/3/library/typing.html#typing.TypeVarTuple.__default__)
                -   [`has_default()`](https://docs.python.org/3/library/typing.html#typing.TypeVarTuple.has_default)
            -   [`ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec)
                -   [`args`](https://docs.python.org/3/library/typing.html#typing.ParamSpec.args)
                -   [`kwargs`](https://docs.python.org/3/library/typing.html#typing.ParamSpec.kwargs)
                -   [`__name__`](https://docs.python.org/3/library/typing.html#typing.ParamSpec.__name__)
                -   [`__default__`](https://docs.python.org/3/library/typing.html#typing.ParamSpec.__default__)
                -   [`has_default()`](https://docs.python.org/3/library/typing.html#typing.ParamSpec.has_default)
            -   [`ParamSpecArgs`](https://docs.python.org/3/library/typing.html#typing.ParamSpecArgs)
            -   [`ParamSpecKwargs`](https://docs.python.org/3/library/typing.html#typing.ParamSpecKwargs)
            -   [`TypeAliasType`](https://docs.python.org/3/library/typing.html#typing.TypeAliasType)
                -   [`__name__`](https://docs.python.org/3/library/typing.html#typing.TypeAliasType.__name__)
                -   [`__module__`](https://docs.python.org/3/library/typing.html#typing.TypeAliasType.__module__)
                -   [`__type_params__`](https://docs.python.org/3/library/typing.html#typing.TypeAliasType.__type_params__)
                -   [`__value__`](https://docs.python.org/3/library/typing.html#typing.TypeAliasType.__value__)
        -   [Other special directives](https://docs.python.org/3/library/typing.html#other-special-directives)
            -   [`NamedTuple`](https://docs.python.org/3/library/typing.html#typing.NamedTuple)
            -   [`NewType`](https://docs.python.org/3/library/typing.html#typing.NewType)
                -   [`__module__`](https://docs.python.org/3/library/typing.html#typing.NewType.__module__)
                -   [`__name__`](https://docs.python.org/3/library/typing.html#typing.NewType.__name__)
                -   [`__supertype__`](https://docs.python.org/3/library/typing.html#typing.NewType.__supertype__)
            -   [`Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol)
            -   [`runtime_checkable()`](https://docs.python.org/3/library/typing.html#typing.runtime_checkable)
            -   [`TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict)
                -   [`__total__`](https://docs.python.org/3/library/typing.html#typing.TypedDict.__total__)
                -   [`__required_keys__`](https://docs.python.org/3/library/typing.html#typing.TypedDict.__required_keys__)
                -   [`__optional_keys__`](https://docs.python.org/3/library/typing.html#typing.TypedDict.__optional_keys__)
                -   [`__readonly_keys__`](https://docs.python.org/3/library/typing.html#typing.TypedDict.__readonly_keys__)
                -   [`__mutable_keys__`](https://docs.python.org/3/library/typing.html#typing.TypedDict.__mutable_keys__)
    -   [Protocols](https://docs.python.org/3/library/typing.html#protocols)
        -   [`SupportsAbs`](https://docs.python.org/3/library/typing.html#typing.SupportsAbs)
        -   [`SupportsBytes`](https://docs.python.org/3/library/typing.html#typing.SupportsBytes)
        -   [`SupportsComplex`](https://docs.python.org/3/library/typing.html#typing.SupportsComplex)
        -   [`SupportsFloat`](https://docs.python.org/3/library/typing.html#typing.SupportsFloat)
        -   [`SupportsIndex`](https://docs.python.org/3/library/typing.html#typing.SupportsIndex)
        -   [`SupportsInt`](https://docs.python.org/3/library/typing.html#typing.SupportsInt)
        -   [`SupportsRound`](https://docs.python.org/3/library/typing.html#typing.SupportsRound)
    -   [ABCs for working with IO](https://docs.python.org/3/library/typing.html#abcs-for-working-with-io)
        -   [`IO`](https://docs.python.org/3/library/typing.html#typing.IO)
        -   [`TextIO`](https://docs.python.org/3/library/typing.html#typing.TextIO)
        -   [`BinaryIO`](https://docs.python.org/3/library/typing.html#typing.BinaryIO)
    -   [Functions and decorators](https://docs.python.org/3/library/typing.html#functions-and-decorators)
        -   [`cast()`](https://docs.python.org/3/library/typing.html#typing.cast)
        -   [`assert_type()`](https://docs.python.org/3/library/typing.html#typing.assert_type)
        -   [`assert_never()`](https://docs.python.org/3/library/typing.html#typing.assert_never)
        -   [`reveal_type()`](https://docs.python.org/3/library/typing.html#typing.reveal_type)
        -   [`dataclass_transform()`](https://docs.python.org/3/library/typing.html#typing.dataclass_transform)
        -   [`overload()`](https://docs.python.org/3/library/typing.html#typing.overload)
        -   [`get_overloads()`](https://docs.python.org/3/library/typing.html#typing.get_overloads)
        -   [`clear_overloads()`](https://docs.python.org/3/library/typing.html#typing.clear_overloads)
        -   [`final()`](https://docs.python.org/3/library/typing.html#typing.final)
        -   [`no_type_check()`](https://docs.python.org/3/library/typing.html#typing.no_type_check)
        -   [`no_type_check_decorator()`](https://docs.python.org/3/library/typing.html#typing.no_type_check_decorator)
        -   [`override()`](https://docs.python.org/3/library/typing.html#typing.override)
        -   [`type_check_only()`](https://docs.python.org/3/library/typing.html#typing.type_check_only)
    -   [Introspection helpers](https://docs.python.org/3/library/typing.html#introspection-helpers)
        -   [`get_type_hints()`](https://docs.python.org/3/library/typing.html#typing.get_type_hints)
        -   [`get_origin()`](https://docs.python.org/3/library/typing.html#typing.get_origin)
        -   [`get_args()`](https://docs.python.org/3/library/typing.html#typing.get_args)
        -   [`get_protocol_members()`](https://docs.python.org/3/library/typing.html#typing.get_protocol_members)
        -   [`is_protocol()`](https://docs.python.org/3/library/typing.html#typing.is_protocol)
        -   [`is_typeddict()`](https://docs.python.org/3/library/typing.html#typing.is_typeddict)
        -   [`ForwardRef`](https://docs.python.org/3/library/typing.html#typing.ForwardRef)
        -   [`NoDefault`](https://docs.python.org/3/library/typing.html#typing.NoDefault)
    -   [Constant](https://docs.python.org/3/library/typing.html#constant)
        -   [`TYPE_CHECKING`](https://docs.python.org/3/library/typing.html#typing.TYPE_CHECKING)
    -   [Deprecated aliases](https://docs.python.org/3/library/typing.html#deprecated-aliases)
        -   [Aliases to built-in types](https://docs.python.org/3/library/typing.html#aliases-to-built-in-types)
            -   [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)
            -   [`List`](https://docs.python.org/3/library/typing.html#typing.List)
            -   [`Set`](https://docs.python.org/3/library/typing.html#typing.Set)
            -   [`FrozenSet`](https://docs.python.org/3/library/typing.html#typing.FrozenSet)
            -   [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)
            -   [`Type`](https://docs.python.org/3/library/typing.html#typing.Type)
        -   [Aliases to types in `collections`](https://docs.python.org/3/library/typing.html#aliases-to-types-in-collections)
            -   [`DefaultDict`](https://docs.python.org/3/library/typing.html#typing.DefaultDict)
            -   [`OrderedDict`](https://docs.python.org/3/library/typing.html#typing.OrderedDict)
            -   [`ChainMap`](https://docs.python.org/3/library/typing.html#typing.ChainMap)
            -   [`Counter`](https://docs.python.org/3/library/typing.html#typing.Counter)
            -   [`Deque`](https://docs.python.org/3/library/typing.html#typing.Deque)
        -   [Aliases to other concrete types](https://docs.python.org/3/library/typing.html#aliases-to-other-concrete-types)
            -   [`Pattern`](https://docs.python.org/3/library/typing.html#typing.Pattern)
            -   [`Match`](https://docs.python.org/3/library/typing.html#typing.Match)
            -   [`Text`](https://docs.python.org/3/library/typing.html#typing.Text)
        -   [Aliases to container ABCs in `collections.abc`](https://docs.python.org/3/library/typing.html#aliases-to-container-abcs-in-collections-abc)
            -   [`AbstractSet`](https://docs.python.org/3/library/typing.html#typing.AbstractSet)
            -   [`ByteString`](https://docs.python.org/3/library/typing.html#typing.ByteString)
            -   [`Collection`](https://docs.python.org/3/library/typing.html#typing.Collection)
            -   [`Container`](https://docs.python.org/3/library/typing.html#typing.Container)
            -   [`ItemsView`](https://docs.python.org/3/library/typing.html#typing.ItemsView)
            -   [`KeysView`](https://docs.python.org/3/library/typing.html#typing.KeysView)
            -   [`Mapping`](https://docs.python.org/3/library/typing.html#typing.Mapping)
            -   [`MappingView`](https://docs.python.org/3/library/typing.html#typing.MappingView)
            -   [`MutableMapping`](https://docs.python.org/3/library/typing.html#typing.MutableMapping)
            -   [`MutableSequence`](https://docs.python.org/3/library/typing.html#typing.MutableSequence)
            -   [`MutableSet`](https://docs.python.org/3/library/typing.html#typing.MutableSet)
            -   [`Sequence`](https://docs.python.org/3/library/typing.html#typing.Sequence)
            -   [`ValuesView`](https://docs.python.org/3/library/typing.html#typing.ValuesView)
        -   [Aliases to asynchronous ABCs in `collections.abc`](https://docs.python.org/3/library/typing.html#aliases-to-asynchronous-abcs-in-collections-abc)
            -   [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)
            -   [`AsyncGenerator`](https://docs.python.org/3/library/typing.html#typing.AsyncGenerator)
            -   [`AsyncIterable`](https://docs.python.org/3/library/typing.html#typing.AsyncIterable)
            -   [`AsyncIterator`](https://docs.python.org/3/library/typing.html#typing.AsyncIterator)
            -   [`Awaitable`](https://docs.python.org/3/library/typing.html#typing.Awaitable)
        -   [Aliases to other ABCs in `collections.abc`](https://docs.python.org/3/library/typing.html#aliases-to-other-abcs-in-collections-abc)
            -   [`Iterable`](https://docs.python.org/3/library/typing.html#typing.Iterable)
            -   [`Iterator`](https://docs.python.org/3/library/typing.html#typing.Iterator)
            -   [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)
            -   [`Generator`](https://docs.python.org/3/library/typing.html#typing.Generator)
            -   [`Hashable`](https://docs.python.org/3/library/typing.html#typing.Hashable)
            -   [`Reversible`](https://docs.python.org/3/library/typing.html#typing.Reversible)
            -   [`Sized`](https://docs.python.org/3/library/typing.html#typing.Sized)
        -   [Aliases to `contextlib` ABCs](https://docs.python.org/3/library/typing.html#aliases-to-contextlib-abcs)
            -   [`ContextManager`](https://docs.python.org/3/library/typing.html#typing.ContextManager)
            -   [`AsyncContextManager`](https://docs.python.org/3/library/typing.html#typing.AsyncContextManager)
-   [Deprecation Timeline of Major Features](https://docs.python.org/3/library/typing.html#deprecation-timeline-of-major-features)


## Type hints cheat sheet

This document is a quick cheat sheet showing how to use type annotations for various common types in Python.

### Variables

Technically many of the type annotations shown below are redundant, since mypy can usually infer the type of a variable from its value. See [Type inference and type annotations](https://mypy.readthedocs.io/en/stable/type_inference_and_annotations.html#type-inference-and-annotations) for more details.

```python
# This is how you declare the type of a variable
age: int = 1

# You don't need to initialize a variable to annotate it
a: int  # Ok (no value at runtime until assigned)

# Doing so can be useful in conditional branches
child: bool
if age < 18:
    child = True
else:
    child = False
```

### Useful built-in types

```python
# For most types, just use the name of the type in the annotation
# Note that mypy can usually infer the type of a variable from its value,
# so technically these annotations are redundant
x: int = 1
x: float = 1.0
x: bool = True
x: str = "test"
x: bytes = b"test"

# For collections on Python 3.9+, the type of the collection item is in brackets
x: list[int] = [1]
x: set[int] = {6, 7}

# For mappings, we need the types of both keys and values
x: dict[str, float] = {"field": 2.0}  # Python 3.9+

# For tuples of fixed size, we specify the types of all the elements
x: tuple[int, str, float] = (3, "yes", 7.5)  # Python 3.9+

# For tuples of variable size, we use one type and ellipsis
x: tuple[int, ...] = (1, 2, 3)  # Python 3.9+

# On Python 3.10+, use the | operator when something could be one of a few types
x: list[int | str] = [3, 5, "test", "fun"]  # Python 3.10+
# On earlier versions, use Union
x: list[Union[int, str]] = [3, 5, "test", "fun"]

# Use X | None for a value that could be None on Python 3.10+
# Use Optional[X] on 3.9 and earlier; Optional[X] is the same as 'X | None'
x: str | None = "something" if some_condition() else None
if x is not None:
    # Mypy understands x won't be None here because of the if-statement
    print(x.upper())
# If you know a value can never be None due to some logic that mypy doesn't
# understand, use an assert
assert x is not None
print(x.upper())

```

### Functions

```python
from collections.abc import Iterator, Callable
from typing import Union, Optional

# This is how you annotate a function definition
def stringify(num: int) -> str:
    return str(num)

# And here's how you specify multiple arguments
def plus(num1: int, num2: int) -> int:
    return num1 + num2

# If a function does not return a value, use None as the return type
# Default value for an argument goes after the type annotation
def show(value: str, excitement: int = 10) -> None:
    print(value + "!" * excitement)

# Note that arguments without a type are dynamically typed (treated as Any)
# and that functions without any annotations are not checked
def untyped(x):
    x.anything() + 1 + "string"  # no errors

# This is how you annotate a callable (function) value.
# The Callable type allows you to annotate a variable or parameter that represents a function or any other callable object.
# This is especially useful when you want to specify the types of arguments a function accepts and the type of value it returns.
# Callable[[int, float], float] specifies that x is a callable (e.g., a function).
# It takes two arguments:
# 1.	The first argument is an int.
# 2.	The second argument is a float.
#
# The callable returns a float.

# register(x) will fail the type check because the type of x is incompatible with the expected type of the callback parameter in the register function.
x: Callable[[int, float], float] = f
def register(callback: Callable[[str], int]) -> None: ...

# A generator function that yields ints is secretly just a function that
# returns an iterator of ints, so that's how we annotate it
def gen(n: int) -> Iterator[int]:
    i = 0
    while i < n:
        yield i
        i += 1

# You can of course split a function annotation over multiple lines
def send_email(
    address: str | list[str],
    sender: str,
    cc: list[str] | None,
    bcc: list[str] | None,
    subject: str = '',
    body: list[str] | None = None,
) -> bool:
    ...

# Mypy understands positional-only and keyword-only arguments
# Positional-only arguments can also be marked by using a name starting with
# two underscores
def quux(x: int, /, *, y: int) -> None:
    pass

quux(3, y=5)  # Ok
quux(3, 5)  # error: Too many positional arguments for "quux"
quux(x=3, y=5)  # error: Unexpected keyword argument "x" for "quux"

# This says each positional arg and each keyword arg is a "str"
def call(self, *args: str, **kwargs: str) -> str:
    reveal_type(args)  # Revealed type is "tuple[str, ...]"
    reveal_type(kwargs)  # Revealed type is "dict[str, str]"
    request = make_request(*args, **kwargs)
    return self.do_api_query(request)

```

### Classes

```python
from typing import ClassVar

class BankAccount:
    # The "__init__" method doesn't return anything, so it gets return
    # type "None" just like any other method that doesn't return anything
    def __init__(self, account_name: str, initial_balance: int = 0) -> None:
        # mypy will infer the correct types for these instance variables
        # based on the types of the parameters.
        self.account_name = account_name
        self.balance = initial_balance

    # For instance methods, omit type for "self"
    def deposit(self, amount: int) -> None:
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        self.balance -= amount

# User-defined classes are valid as types in annotations
account: BankAccount = BankAccount("Alice", 400)
def transfer(src: BankAccount, dst: BankAccount, amount: int) -> None:
    src.withdraw(amount)
    dst.deposit(amount)

# Functions that accept BankAccount also accept any subclass of BankAccount!
class AuditedBankAccount(BankAccount):
    # You can optionally declare instance variables in the class body
    audit_log: list[str]

    def __init__(self, account_name: str, initial_balance: int = 0) -> None:
        super().__init__(account_name, initial_balance)
        self.audit_log: list[str] = []

    def deposit(self, amount: int) -> None:
        self.audit_log.append(f"Deposited {amount}")
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        self.audit_log.append(f"Withdrew {amount}")
        self.balance -= amount

audited = AuditedBankAccount("Bob", 300)
# audited is of class AuditedBankAccount a subclass of BankAccount, so it is compatible with the transfer function
transfer(audited, account, 100)  # type checks!

# You can use the ClassVar annotation to declare a class variable
class Car:
    seats: ClassVar[int] = 4
    passengers: ClassVar[list[str]]

# If you want dynamic attributes on your class, have it
# override "__setattr__" or "__getattr__"
class A:
    # This will allow assignment to any A.x, if x is the same type as "value"
    # (use "value: Any" to allow arbitrary types)
    def __setattr__(self, name: str, value: int) -> None: ...

    # This will allow access to any A.x, if x is compatible with the return type
    def __getattr__(self, name: str) -> int: ...

a = A()
a.foo = 42  # Works
a.bar = 'Ex-parrot'  # Fails type checking
```

###  When you're puzzled or when things are complicated ==> `reveal_type()` 

```python
from typing import Union, Any, Optional, TYPE_CHECKING, cast

# To find out what type mypy infers for an expression anywhere in
# your program, wrap it in reveal_type().  Mypy will print an error
# message with the type; remove it again before running the code.
reveal_type(1)  # Revealed type is "builtins.int"

# If you initialize a variable with an empty container or "None"
# you may have to help mypy a bit by providing an explicit type annotation
x: list[str] = []
x: str | None = None

# Use Any if you don't know the type of something or it's too
# dynamic to write a type for
x: Any = mystery_function()
# Mypy will let you do anything with x!
x.whatever() * x["you"] + x("want") - any(x) and all(x) is super  # no errors

# Use a "type: ignore" comment to suppress errors on a given line,
# when your code confuses mypy or runs into an outright bug in mypy.
# Good practice is to add a comment explaining the issue.
x = confusing_function()  # type: ignore  # confusing_function won't return None here because ...

# "cast" is a helper function that lets you override the inferred
# type of an expression. It's only for mypy -- there's no runtime check.
a = [4]
b = cast(list[int], a)  # Passes fine
c = cast(list[str], a)  # Passes fine despite being a lie (no runtime check)
reveal_type(c)  # Revealed type is "builtins.list[builtins.str]"
print(c)  # Still prints [4] ... the object is not changed or casted at runtime

# Use "TYPE_CHECKING" if you want to have code that mypy can see but will not
# be executed at runtime (or to have code that mypy can't see)
if TYPE_CHECKING:
    import json
else:
    import orjson as json  # mypy is unaware of this
```

In some cases type annotations can cause issues at runtime, see [Annotation issues at runtime](https://mypy.readthedocs.io/en/stable/runtime_troubles.html#runtime-troubles) for dealing with this.

See [Silencing type errors](https://mypy.readthedocs.io/en/stable/type_inference_and_annotations.html#silencing-type-errors) for details on how to silence errors.

### Standard "duck types": `Iterable`, `Sequence`, `Mapping`, `MutableMapping`

In typical Python code, many functions that can take a list or a dict as an argument only need their argument to be somehow "list-like" or "dict-like". A specific meaning of "list-like" or "dict-like" (or something-else-like) is called a "duck type", and several duck types that are common in idiomatic Python are standardized.

```python
from collections.abc import Mapping, MutableMapping, Sequence, Iterable
# or 'from typing import ...' (required in Python 3.8)

# Use Iterable for generic iterables (anything usable in "for"),
# and Sequence where a sequence (supporting "len" and "__getitem__") is
# required
def f(ints: Iterable[int]) -> list[str]:
    return [str(x) for x in ints]

f(range(1, 3))

# Mapping describes a dict-like object (with "__getitem__") that we won't
# mutate, and MutableMapping one (with "__setitem__") that we might
def f(my_mapping: Mapping[int, str]) -> list[int]:
    my_mapping[5] = 'maybe'  # mypy will complain about this line...
    return list(my_mapping.keys())

f({3: 'yes', 4: 'no'})

def f(my_mapping: MutableMapping[int, str]) -> set[str]:
    my_mapping[5] = 'maybe'  # ...but mypy is OK with this.
    return set(my_mapping.values())

f({3: 'yes', 4: 'no'})

import sys
from typing import IO

# Use IO[str] or IO[bytes] for functions that should accept or return
# objects that come from an open() call (note that IO does not
# distinguish between reading, writing or other modes)
def get_sys_IO(mode: str = 'w') -> IO[str]:
    if mode == 'w':
        return sys.stdout
    elif mode == 'r':
        return sys.stdin
    else:
        return sys.stdout
```

You can even make your own duck types using [Protocols and structural subtyping](https://mypy.readthedocs.io/en/stable/protocols.html#protocol-types).

### Forward references

```python
# You may want to reference a class before it is defined.
# This is known as a "forward reference".
def f(foo: A) -> int:  # This will fail at runtime with 'A' is not defined
    ...

# However, if you add the following special import:
from __future__ import annotations
# It will work at runtime and type checking will succeed as long as there
# is a class of that name later on in the file
def f(foo: A) -> int:  # Ok
    ...

# Another option is to just put the type in quotes
def f(foo: 'A') -> int:  # Also ok
    ...

class A:
    # This can also come up if you need to reference a class in a type
    # annotation inside the definition of that class
    @classmethod
    def create(cls) -> A:
        ...

```

See [Class name forward references](https://mypy.readthedocs.io/en/stable/runtime_troubles.html#forward-references) for more details.

### Decorators

Decorator functions can be expressed via generics. See [Declaring decorators](https://mypy.readthedocs.io/en/stable/generics.html#declaring-decorators) for more details. Example using Python 3.12 syntax:

```python
from collections.abc import Callable
from typing import Any

def bare_decorator[F: Callable[..., Any]](func: F) -> F:
    ...

def decorator_args[F: Callable[..., Any]](url: str) -> Callable[[F], F]:
    ...

```

The same example using pre-3.12 syntax:

```python
from collections.abc import Callable
from typing import Any, TypeVar

F = TypeVar('F', bound=Callable[..., Any])

def bare_decorator(func: F) -> F:
    ...

def decorator_args(url: str) -> Callable[[F], F]:
    ...
```

### Coroutines and asyncio

See [Typing async/await](https://mypy.readthedocs.io/en/stable/more_types.html#async-and-await) for the full detail on typing coroutines and asynchronous code.

```python
import asyncio

# A coroutine is typed like a normal function
async def countdown(tag: str, count: int) -> str:
    while count > 0:
        print(f'T-minus {count} ({tag})')
        await asyncio.sleep(0.1)
        count -= 1
    return "Blastoff!"
```


## Type Aliases Reference

* [Official Type Aliases documentation](https://docs.python.org/3/library/typing.html#typing.TypedDict)
* [Semi-official community doc (easier to read)](https://typing.readthedocs.io/en/latest/spec/aliases.html): Type Aliases
* [See the Type Hints Reference](stdlib-devtools-typing-reference.md) for more examples and details on type aliases.

### TypeAlias

#### Type Statement - typing.TypeAliasType

Recommended way to define type aliases since `Python 3.12`:

```python
# type is avaliable only on python 3.12+
type Vector = list[float]

# You can inspect the type alias
print(type(Vector))  # Output: <class 'typing.TypeAliasType'>
print(Vector.__name__)  # Output: 'Vector'
print(Vector.__value__)  # Output: list[float]

# Implicit type alias
Vector = list[float]

# You can inspect the type alias
print(type(Vector))  # Output: <class 'typing.TypeAliasType'>
print(Vector.__name__)  # Output: 'Vector'
print(Vector.__value__)  # Output: list[float]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]
```

### NewType

* Create distinct types for logical separation.

```python
from typing import NewType

UserId = NewType('UserId', int)

def get_user_name(user_id: UserId) -> str:
    return f"User ID: {user_id}"
```

## The `Any` Type

* Represents a dynamically typed value.

```python
from typing import Any

def foo(x: Any) -> int:
    return len(x)
```

## Structural Subtyping

* Use `Protocol` to define interfaces based on structure (not inheritance).

```python
from typing import Protocol

class SupportsAdd(Protocol):
    def __add__(self, other: int) -> int: ...

def add_five(x: SupportsAdd) -> int:
    return x + 5

3. Special Forms

3.1 Union

	•	Represents multiple possible types.

x: Union[int, str] = 42  # or 'hello'

3.2 Optional

	•	Shortcut for Union[X, None].

x: Optional[int] = None

3.3 Literal

	•	Represents specific values.

from typing import Literal

def open_file(mode: Literal["r", "w", "a"]) -> None:
    ...

3.4 Final

	•	Prevents reassignment or subclassing.

from typing import Final

MAX_SPEED: Final = 120

3.5 Annotated

	•	Adds metadata to type annotations.

from typing import Annotated

T = Annotated[int, "positive"]

4. Advanced Typing Constructs

4.1 TypedDict

	•	Used to define dictionary-like objects with a fixed set of keys and types.

from typing import TypedDict

class Movie(TypedDict):
    title: str
    year: int

4.2 ParamSpec and Concatenate

	•	Used for higher-order functions like decorators.

from typing import Callable, ParamSpec

P = ParamSpec('P')

def log_args(func: Callable[P, int]) -> Callable[P, int]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> int:
        print(args, kwargs)
        return func(*args, **kwargs)
    return wrapper

4.3 Generators and Coroutines

	•	Annotate generators and asynchronous generators.

from typing import Generator, AsyncGenerator

def infinite() -> Generator[int, None, None]:
    yield from range(10)

5. Deprecated Features

	•	Certain typing features are deprecated in favor of newer syntax:
	•	List, Dict, etc. → Use built-in types list, dict.
	•	AnyStr → Replaced by type parameter syntax.
	•	@no_type_check_decorator → Deprecated in Python 3.13.

6. Introspection Helpers

	•	Functions for working with types at runtime.
	•	get_type_hints()
	•	get_origin()
	•	get_args()

7. Future-Proofing

	•	New syntax and features are continually added (e.g., ParamSpec, TypeVarTuple).
	•	Use the typing_extensions package to backport features to older Python versions.

For more details, refer to the official Python documentation or type system specifications (PEPs).