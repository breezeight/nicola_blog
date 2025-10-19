---
title: "Python Reference"
abstract: >
  Comprehensive reference covering Python's type system, async model, error handling, 
  and core programming concepts for experienced developers.
type: reference
---

# Python Reference

## 📘 Purpose & Scope

This reference provides a structured overview of Python's core concepts, designed to help experienced developers refresh their understanding and compare approaches across different programming languages. Each section includes brief explanations, key characteristics, and links to detailed documentation.

## References

- [Official Python Documentation](https://docs.python.org/3/)
- {{ link_with_abstract("python-language-reference-nicola/python-learning.md") }}

---

## 1. Overview & Philosophy

Python is a high-level, interpreted programming language that emphasizes code readability and simplicity. It follows the principle of "There should be one—and preferably only one—obvious way to do it" (The Zen of Python). Python's design philosophy prioritizes developer productivity through clean syntax, extensive standard library, and strong community support.

**Key characteristics:**
- Interpreted language with dynamic typing
- Indentation-based syntax (no braces)
- Extensive standard library and third-party ecosystem
- Strong support for multiple programming paradigms (OOP, functional, procedural)

**Compare with:**
- [Go's philosophy](go/go-index.md#1-overview--philosophy)
- [TypeScript's philosophy](javascript/typescript-index.md#1-overview--philosophy)
- [Ruby's philosophy](ruby/ruby-index.md#1-overview--philosophy)

**Learn more:** {{ link_with_abstract("python-overview-and-learning-paths.md") }}

---

## 2. Type Systems

Python uses dynamic typing with optional static type hints introduced in Python 3.5+. The type system is structural rather than nominal, allowing duck typing. Type hints are checked by external tools like mypy but don't affect runtime behavior.

**Python approach:**
- Dynamic typing with runtime type checking
- Optional static type hints via `typing` module
- Duck typing: "if it walks like a duck and quacks like a duck, it's a duck"
- Structural typing with `typing.Protocol`

**Compare with:**
- [Go's type system](go/go-index.md#2-type-systems)
- [TypeScript's type system](javascript/typescript-index.md#2-type-systems)
- [Ruby's type system](ruby/ruby-index.md#2-type-systems)

**Learn more:** {{ link_with_abstract("python-language-reference-nicola/stdlib-devtools-typing-explanation.md") }}

---

## 3. Functions and Closures

Python treats functions as first-class objects, supporting closures, higher-order functions, and decorators. Functions can be defined with `def`, assigned to variables, passed as arguments, and returned from other functions.

**Python approach:**
- First-class functions with `def` keyword
- Support for closures and lexical scoping
- Decorators for function modification
- Lambda expressions for simple anonymous functions

**Compare with:**
- [Go's functions](go-index.md#3-functions-and-closures)
- [TypeScript's functions](typescript.md#3-functions-and-closures)
- [Ruby's functions](ruby-index.md#3-functions-and-closures)

**Learn more:** {{ link_with_abstract("python-language-reference-nicola/functions.md") }}

---

## 4. Variables and Scoping

Python uses lexical scoping with explicit `global` and `nonlocal` keywords. Variables are created on first assignment and follow LEGB (Local, Enclosing, Global, Built-in) resolution order.

**Python approach:**
- Dynamic variable creation (no declaration required)
- LEGB scoping rule
- `global` and `nonlocal` keywords for scope modification
- Namespace-based scoping system

**Compare with:**
- [Go's scoping](go-index.md#4-variables-and-scoping)
- [TypeScript's scoping](typescript.md#4-variables-and-scoping)
- [Ruby's scoping](ruby-index.md#4-variables-and-scoping)

**Learn more:** {{ link_with_abstract("python-language-reference-nicola/scopes-and-namespaces.md") }}

---

## 5. Data Types and Literals

Python provides rich built-in data types including numeric types, sequences (strings, lists, tuples), mappings (dictionaries), sets, and boolean types. All types are objects with methods and attributes.

**Python approach:**
- Rich set of built-in types
- Everything is an object (including types)
- Immutable types: numbers, strings, tuples, frozensets
- Mutable types: lists, dictionaries, sets

**Compare with:**
- [Go's data types](go-index.md#5-data-types-and-literals)
- [TypeScript's data types](typescript.md#5-data-types-and-literals)
- [Ruby's data types](ruby-index.md#5-data-types-and-literals)

**Learn more:** {{ link_with_abstract("python-language-reference-nicola/data-types-and-literals.md") }}

---

## 6. Control Flow

Python provides standard control flow constructs including if/elif/else, for/while loops, and comprehensions. Python 3.10+ introduced structural pattern matching with `match/case`.

**Python approach:**
- Indentation-based block structure
- `if/elif/else` conditionals
- `for` loops with iterables
- List/dict/set comprehensions
- `match/case` pattern matching (Python 3.10+)

**Compare with:**
- [Go's control flow](go-index.md#6-control-flow)
- [TypeScript's control flow](typescript.md#6-control-flow)
- [Ruby's control flow](ruby-index.md#6-control-flow)

**Learn more:** {{ link_with_abstract("python-language-reference-nicola/control-flow.md") }}

---

## 7. Error Handling

Python uses exceptions for error handling with try/except/finally blocks. The philosophy is "Easier to Ask for Forgiveness than Permission" (EAFP), encouraging exception handling over defensive programming.

**Python approach:**
- Exception-based error handling
- `try/except/finally/else` blocks
- Custom exception classes
- Context managers for resource cleanup

**Compare with:**
- [Go's error handling](go-index.md#7-error-handling)
- [TypeScript's error handling](typescript.md#7-error-handling)
- [Ruby's error handling](ruby-index.md#7-error-handling)

**Learn more:** {{ link_with_abstract("python-language-reference-nicola/exception-handling-and-with.md") }}

---

## 8. Object-Oriented Programming

Python supports full object-oriented programming with classes, inheritance, polymorphism, and encapsulation. Classes are objects themselves, enabling dynamic class creation and modification.

**Python approach:**
- Class-based OOP with `class` keyword
- Multiple inheritance support
- Method resolution order (MRO) with C3 linearization
- Properties and descriptors for attribute access control

**Compare with:**
- [Go's OOP](go-index.md#8-object-oriented-programming)
- [TypeScript's OOP](typescript.md#8-object-oriented-programming)
- [Ruby's OOP](ruby-index.md#8-object-oriented-programming)

**Learn more:** {{ link_with_abstract("python-language-reference-nicola/classes-and-objects.md") }}

---

## 9. Asynchronous Programming

Python supports asynchronous programming through `asyncio`, coroutines, and async/await syntax. The Global Interpreter Lock (GIL) limits true parallelism but enables efficient I/O-bound concurrency.

**Python approach:**
- `asyncio` library for async programming
- `async/await` syntax for coroutines
- Event loop-based concurrency
- GIL limitations for CPU-bound tasks

**Compare with:**
- [Go's concurrency](go-index.md#9-asynchronous-programming)
- [TypeScript's async model](typescript.md#9-asynchronous-programming)
- [Ruby's async model](ruby-index.md#9-asynchronous-programming)

**Learn more:** {{ link_with_abstract("python-language-reference-nicola/functions-and-functional-programming.md") }}

---

## 10. Modules and Packages

Python's module system allows code organization through files and packages. The import system supports relative and absolute imports, with `__init__.py` files defining packages.

**Python approach:**
- File-based modules
- Package hierarchy with `__init__.py`
- `import` statement for module loading
- `pip` and `uv` for package management

**Compare with:**
- [Go's packages](go-index.md#10-modules-and-packages)
- [TypeScript's modules](typescript.md#10-modules-and-packages)
- [Ruby's modules](ruby-index.md#10-modules-and-packages)

**Learn more:** {{ link_with_abstract("python-language-reference-nicola/modules-and-packages.md") }}

---

## 11. Memory Management

Python uses automatic memory management with reference counting and cyclic garbage collection. Memory is managed transparently, with no manual memory allocation/deallocation required.

**Python approach:**
- Automatic garbage collection
- Reference counting with cycle detection
- Memory pools for small objects
- No manual memory management

**Compare with:**
- [Go's memory management](go-index.md#11-memory-management)
- [TypeScript's memory management](typescript.md#11-memory-management)
- [Ruby's memory management](ruby-index.md#11-memory-management)

**Learn more:** {{ link_with_abstract("python-language-reference-nicola/python-learning.md") }}

---

## 12. Pattern Matching

Python 3.10 introduced structural pattern matching with `match/case` statements, enabling powerful pattern-based control flow similar to switch statements in other languages.

**Python approach:**
- `match/case` statements (Python 3.10+)
- Destructuring patterns
- Guard conditions with `if`
- Type and value pattern matching

**Compare with:**
- [Go's pattern matching](go-index.md#12-pattern-matching)
- [TypeScript's pattern matching](typescript.md#12-pattern-matching)
- [Ruby's pattern matching](ruby-index.md#12-pattern-matching)

**Learn more:** {{ link_with_abstract("python-language-reference-nicola/control-flow.md") }}

---

## 13. Metaprogramming

Python provides extensive metaprogramming capabilities through introspection, decorators, metaclasses, and dynamic code execution. The language's dynamic nature enables powerful runtime code modification.

**Python approach:**
- `inspect` module for introspection
- Decorators for function/class modification
- Metaclasses for class creation control
- `exec()` and `eval()` for dynamic code execution

**Compare with:**
- [Go's metaprogramming](go-index.md#13-metaprogramming)
- [TypeScript's metaprogramming](typescript.md#13-metaprogramming)
- [Ruby's metaprogramming](ruby-index.md#13-metaprogramming)

**Learn more:** {{ link_with_abstract("python-language-reference-nicola/decorators.md") }}

---

## 14. Standard Library Highlights

Python's "batteries included" philosophy provides an extensive standard library covering file I/O, networking, data structures, algorithms, and more. The library is organized into modules with clear APIs.

**Python approach:**
- Comprehensive standard library
- `os`, `sys`, `pathlib` for system interaction
- `json`, `csv`, `xml` for data formats
- `unittest` for testing framework

**Compare with:**
- [Go's standard library](go-index.md#14-standard-library-highlights)
- [TypeScript's standard library](typescript.md#14-standard-library-highlights)
- [Ruby's standard library](ruby-index.md#14-standard-library-highlights)

**Learn more:** {{ link_with_abstract("python-language-reference-nicola/python-learning.md") }}

---

## 15. Compilation and Runtime

Python is an interpreted language that compiles source code to bytecode, which is then executed by the Python Virtual Machine (PVM). The compilation process is transparent to developers.

**Python approach:**
- Source code → Bytecode → PVM execution
- `.pyc` files for bytecode caching
- No separate compilation step required
- Cross-platform bytecode compatibility

**Compare with:**
- [Go's compilation](go-index.md#15-compilation-and-runtime)
- [TypeScript's compilation](typescript.md#15-compilation-and-runtime)
- [Ruby's compilation](ruby-index.md#15-compilation-and-runtime)

**Learn more:** {{ link_with_abstract("python-language-reference-nicola/python-learning.md") }}

---

## 16. Testing and Debugging

Python provides built-in testing support through `unittest` and external frameworks like `pytest`. Debugging tools include `pdb` debugger and various IDE integrations.

**Python approach:**
- `unittest` framework in standard library
- `pytest` for advanced testing features
- `pdb` command-line debugger
- Rich ecosystem of testing tools

**Compare with:**
- [Go's testing](go-index.md#16-testing-and-debugging)
- [TypeScript's testing](typescript.md#16-testing-and-debugging)
- [Ruby's testing](ruby-index.md#16-testing-and-debugging)

**Learn more:** {{ link_with_abstract("python-language-reference-nicola/python-learning.md") }}

---

## 17. Best Practices and Idioms

Python follows PEP 8 style guidelines and has established idioms for common patterns. The community emphasizes readability, explicit over implicit, and following the Zen of Python principles.

**Python approach:**
- PEP 8 style guide
- "Explicit is better than implicit"
- List comprehensions over loops
- Context managers for resource management

**Compare with:**
- [Go's best practices](go-index.md#17-best-practices-and-idioms)
- [TypeScript's best practices](typescript.md#17-best-practices-and-idioms)
- [Ruby's best practices](ruby-index.md#17-best-practices-and-idioms)

**Learn more:** {{ link_with_abstract("python-language-reference-nicola/python-learning.md") }}

---

## 18. Python Specific Features

### List Comprehensions
Python's list comprehensions provide a concise way to create lists based on existing iterables, combining mapping and filtering operations in a single expression.

**Learn more:** {{ link_with_abstract("python-language-reference-nicola/control-flow.md") }}

### Context Managers
Context managers enable proper resource management through the `with` statement, ensuring cleanup code runs even if exceptions occur.

**Learn more:** {{ link_with_abstract("python-language-reference-nicola/context-managers.md") }}

### Decorators
Decorators are a powerful metaprogramming feature that allows modification of functions or classes without changing their source code.

**Learn more:** {{ link_with_abstract("python-language-reference-nicola/decorators.md") }}

### Generators and Iterators
Python's generator functions and iterator protocol provide memory-efficient iteration over large datasets without loading everything into memory.

**Learn more:** {{ link_with_abstract("python-language-reference-nicola/iterators-iterables-generators.md") }}

### Package Management with uv
Modern Python package management using `uv`, a fast Python package installer and resolver written in Rust.

**Learn more:** {{ link_with_abstract("python-language-reference-nicola/uv-explanation.md") }}

---

## References

- [Official Python Documentation](https://docs.python.org/3/)
- [Python Learning Paths](python-nicola-personal-learning-path.md)
- {{ link_with_abstract("languages-concept-comparison.md") }}
