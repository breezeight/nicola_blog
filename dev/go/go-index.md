---
title: Go Lang
abstract: >
  Comprehensive Go language reference covering syntax, packages, functions, variables, 
  control flow, data structures, concurrency, and best practices for Go development.
---

# Go Lang

https://roadmap.sh/golang


## Getting Started

### Basic Syntax

#### Packages

https://go.dev/tour/basics/1

#### Import and Export

https://go.dev/tour/basics/2

```go
import (
	"fmt"
	"math"
)
// ...
// access the exported name Pi from the math package
fmt.Println(math.Pi)
```

A name is exported if it begins with a capital letter.
When importing a package, you can refer only to its exported names.

#### Functions

In Go, `func` is the keyword used to define a function.
A function is a named block of code that can take inputs, perform operations, and return outputs.

General syntax:

```go
func FunctionName(param1 Type1, param2 Type2, ...) ReturnType {
    // function body
    return value
}
```

- func → keyword
- FunctionName → identifier (must start with uppercase for export, lowercase for private)
- param1 Type1 → parameters with their types
- ReturnType → (optional) type of value(s) returned
- return → statement to send back result(s)



```go
//Function with no parameters, no return
func sayHello() {
    fmt.Println("Hello, Go!")
}
//Call it with: `sayHello()`

//Function with two parameters, one return
func add(x int, y int) int {
    return x + y
}
// sum := add(3, 4)
// fmt.Println(sum) // print the result: 7


// Multiple parameters of same type
// When two or more consecutive named function parameters share a type, you can omit the type from all but the last.
func multiply(x, y int) int {
    return x * y
}


// Multiple return values
func swap(a, b string) (string, string) {
    return b, a
}
//x, y := swap("left", "right")
//fmt.Println(x, y) // right left
```

https://go.dev/tour/basics/5

#### Functions Multiple Return Values

https://go.dev/tour/basics/6

```go
func swap(x, y string) (string, string) {
    return y, x
}
a, b := swap("hello", "world")
// print the result: "world hello"
```

#### Function Named return values

https://go.dev/tour/basics/7

In Go, you can name return values directly in the function signature. These names become pre-declared variables inside the function.

```go
package main

import "fmt"

// Named return values: sum and product
func calculate(a, b int) (sum int, product int) {
    sum = a + b
    product = a * b
    return // naked return
}

func main() {
    s, p := calculate(3, 4)
    fmt.Println("Sum:", s, "Product:", p)
}
```
Key points:

- Named returns are initialized to their zero values.
- A return without arguments returns those named variables.
- Use naked returns only for small, clear functions.
- For larger functions, explicitly return values for clarity.

#### Variables

https://go.dev/tour/basics/8

The var statement declares a list of variables; as in function argument lists, the type is last.

A var statement can be at package or function level. We see both in this example.

```go
package main

import "fmt"

var c, python, java bool

func main() {
	var i int
	fmt.Println(i, c, python, java)
}

// print the result: 0 false false false
```


#### Short variable declarations

https://go.dev/tour/basics/10

Inside a function, the := short assignment statement can be used in place of a var declaration with implicit type.

Outside a function, every statement begins with a keyword (var, func, and so on) and so the := construct is not available.

```go
package main

import "fmt"

func main() {
	var i, j int = 1, 2
	k := 3
	c, python, java := true, false, "no!"

	fmt.Println(i, j, k, c, python, java)
}
```

#### Basic Types

https://go.dev/tour/basics/11

The built-in types are:

```go
bool

string

int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr

byte // alias for uint8

rune // alias for int32
     // represents a Unicode code point

float32 float64

complex64 complex128
```

#### Zero values - no initial value
https://go.dev/tour/basics/12

Variables declared without an explicit initial value are given their zero value.

The zero value is:

- 0 for numeric types,
- false for the boolean type, and
- "" (the empty string) for strings.

```go
package main

import "fmt"

func main() {
	var i int
	var f float64
	var b bool
	var s string
	fmt.Printf("%v %v %v %q\n", i, f, b, s)
}

// print the result: 0 0 false ""
```

#### Type conversions
https://go.dev/tour/basics/13

The expression T(v) converts the value v to the type T.

Unlike in C, in Go assignment between items of different type requires an explicit conversion. Try removing the float64 or uint conversions in the example and see what happens.

```go
package main

import (
	"fmt"
	"math"
)

func main() {
	var x, y int = 3, 4
	var f float64 = math.Sqrt(float64(x*x + y*y))
	var z uint = uint(f) // var z uint = uint(f) // error: cannot use f (type float64) as type uint in assignment
	fmt.Println(x, y, z)
}
```

#### Type inference

https://go.dev/tour/basics/14

When declaring a variable without specifying an explicit type (either by using the := syntax or var = expression syntax), the variable's type is inferred from the value on the right hand side.

```go
package main

import "fmt"

func main() {
	v := 42 // change me!
	fmt.Printf("v is of type %T\n", v)
	y := 1.0
	fmt.Printf("y is of type %T\n", y)
}
// v is of type int
// y is of type float64
```

#### Constants

https://go.dev/tour/basics/15

Constants are declared like variables, but with the const keyword.

Constants can be **only basic types**: character, string, boolean, or numeric values.

Constants cannot be declared using the := syntax.

You cannot declare a struct itself as a constant in Go:

-	A struct is a composite type, so you must use var instead.
-	If you need an immutable struct, you can declare a package-level variable and avoid modifying it by convention.

Example:

```go
package main

import "fmt"

type Config struct {
    host string
}

// Getter
func (c Config) Host() string {
    return c.host //valid, internal access
}

var DefaultConfig = Config{host: "localhost"}

func main() {
    fmt.Println(DefaultConfig.Host())  // valid, uses getter method. prints "localhost"
    fmt.Println(DefaultConfig.host)    // error: invalid only inside same package
    fmt.Println(DefaultConfig.host())  // error: invalid, compile-time error
}
```

To enforce immutability, make the struct fields unexported and provide only getters. This prevents external code from modifying the data.


#### Numeric Constants

https://go.dev/tour/basics/16

TODO

#### Flow Control

##### For Loops

https://go.dev/tour/flowcontrol/1

Go has only one looping construct, the for loop (there is no while loop in Go).

```go
package main

import "fmt"

func main() {
	sum := 0
    // the init statement: executed before the first iteration
    // the condition expression: evaluated before every iteration
    // the post statement: executed at the end of every iteration
	for i := 0; i < 10; i++ {
		sum += i
	}
	fmt.Println(sum)
}
```


The init and post statements are optional:

```go
package main

import "fmt"

func main() {
	sum := 1
	for ; sum < 1000; {
		sum += sum
	}
	fmt.Println(sum)
}

// print the result: 1024
```


For is Go's "while" loop:

```go
package main

import "fmt"

func main() {
	sum := 1
	for sum < 1000 {
		sum += sum
	}
	fmt.Println(sum)
}
```


To loop forever you can omit the condition:

```go
package main

func main() {
	for {
	}
}
```

##### If/Else

https://go.dev/tour/flowcontrol/5

Go's if statements are like its for loops; the expression need not be surrounded by parentheses ( ) but the braces { } are required.

```go
package main

import (
	"fmt"
	"math"
)

func sqrt(x float64) string {
	if x < 0 {
		return sqrt(-x) + "i"
	}
	return fmt.Sprint(math.Sqrt(x))
}

func main() {
	fmt.Println(sqrt(2), sqrt(-4))
}
```

##### If with a short statement

https://go.dev/tour/flowcontrol/6

An `if` statement can include an **initialization statement** before its condition. This is called a **short statement**. It allows you to declare and initialize variables that are scoped only to that `if` block (and its optional `else` block):

```go
if initStatement; condition {
    // code that uses variables declared in initStatement
}

// example
if v := math.Pow(x, n); v < lim {
    return v
}
return lim
```

- initStatement runs first.
- The condition is evaluated next.
- Any variables declared in initStatement are only accessible within this if and its else.


Why Use a Short Statement:

- **Keeps scope small**: Variables declared here won’t leak into surrounding code.
- **Cleaner intent**: Puts “compute and check” logic in one place.
- **Idiomatic Go**: This pattern is widely used in the Go standard library.

##### else

https://go.dev/tour/flowcontrol/7

```go
	if v := math.Pow(x, n); v < lim {
		return v
	} else {
		fmt.Printf("%g >= %g\n", v, lim)
	}
```

##### Switch

https://go.dev/tour/flowcontrol/9
https://go.dev/tour/flowcontrol/10

Go's switch is:
- like the one in C, C++, Java, JavaScript, and PHP, 
- except that Go only runs the selected case, not all the cases that follow

```go
package main

import (
	"fmt"
	"runtime"
)

func main() {
	fmt.Print("Go runs on ")
	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("macOS.")
	case "linux":
		fmt.Println("Linux.")
	default:
		// freebsd, openbsd,
		// plan9, windows...
		fmt.Printf("%s.\n", os)
	}
}
```

Switch cases evaluate cases from top to bottom, stopping when a case succeeds, for example:

```go
switch i {
case 0:
case f():
}
```

does not call f if i==0.

##### Switch with no condition

Switch without a condition is the same as switch true.

```go
switch {
case condition1:
    // code
case condition2:
    // code
default:
    // fallback
}
```

This is functionally the same as:

```go
switch true {
case condition1:
    // code
case condition2:
    // code
default:
    // fallback
}
```

This construct can be a clean way to write long if-then-else chains with a cleaner, more readable structure.

```go
package main

import (
	"fmt"
	"time"
)

func main() {
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("Good morning!")
	case t.Hour() < 17:
		fmt.Println("Good afternoon.")
	default:
		fmt.Println("Good evening.")
	}
}
```

##### Defer

https://go.dev/tour/flowcontrol/12
https://go.dev/tour/flowcontrol/13

A defer statement defers the execution of a function until the surrounding function returns.

USAGE: Defer is commonly used to simplify functions that perform various clean-up actions.

The deferred call's arguments are evaluated immediately, but the function call is not executed until the surrounding function returns.

```go
package main

import "fmt"

func main() {
	defer fmt.Println("world")

	fmt.Println("hello")
}

// print the result:
// hello
// world
```

Deferred function calls are pushed onto a stack and are executed in **LIFO (Last In First Out)** order: 


```go
package main

import "fmt"

func main() {
	fmt.Println("counting")

	for i := 0; i < 10; i++ {
		defer fmt.Println(i)
	}

	fmt.Println("done")
}

// print the result:
// counting
// 9
// 8
// 7
// 6
// 5
// 4
// 3
// 2
// 1
// 0
// done
```

[LEARN MORE](https://go.dev/blog/defer-panic-and-recover) ==> Defer, Panic, and Recover


#### More types: structs, slices, and maps.

Define types based on existing ones with structs, arrays, slices, and maps.

If you just start learning Go, keep in mind that:

- Structs – core building block for data models and configs.

- Slices – primary collection type, used more than arrays.

- Maps – key-value storage, standard for lookups.

- Pointers – common for struct manipulation and avoiding copies.

- Closures / function values – used but less frequent, mostly in callbacks or concurrency patterns.

Most Go code heavily uses structs, slices, maps, and pointers. Arrays are rare outside low-level or fixed-size data cases.

##### Pointers
https://go.dev/tour/moretypes/1

A pointer holds the memory address of a value.

The type `*T` is a pointer to a `T` value. Its zero value is nil.

Example: `var p *int`

The `&` operator generates a pointer to its operand.

```go
i := 42
p = &i
```

The `*` operator denotes the pointer's underlying value.

```go
fmt.Println(*p) // read i through the pointer p
*p = 21         // set i through the pointer p
```

This is known as "dereferencing" or "indirecting".

Unlike C, Go has no pointer arithmetic.

```go
package main

import "fmt"

func main() {
	i, j := 42, 2701

	p := &i         // point to i
	fmt.Println(*p) // read i through the pointer
	*p = 21         // set i through the pointer
	fmt.Println(i)  // see the new value of i

	p = &j         // point to j
	*p = *p / 37   // divide j through the pointer
	fmt.Println(j) // see the new value of j
}

// print the result:
// 42
// 21
// 73
```


##### Structs
https://go.dev/tour/moretypes/2
https://go.dev/tour/moretypes/3

A struct is a collection of fields.

```go
type Vertex struct {
	X int
	Y int
}

func main() {
	fmt.Println(Vertex{1, 2})
}

// print the result:
// {1 2}
```

Struct fields are accessed using a dot.

```go
func main() {
	v := Vertex{1, 2}
	v.X = 4 //set 
	fmt.Println(v.X) //get
}
// print the result:
// 4
```


##### Pointer to a struct
https://go.dev/tour/moretypes/4

To access the field X of a struct when we have the struct pointer p we could write `(*p).X`.

However, that notation is cumbersome, so the language permits us instead to write just `p.X`, without the explicit dereference.

```go
package main

import "fmt"

type Vertex struct {
	X int
	Y int
}

func main() {
	v := Vertex{1, 2}
	p := &v
	p.X = 1e9 // ALLOWED
	fmt.Println(v)
}
```

##### Struct literals
https://go.dev/tour/moretypes/5

A literal is a fixed value written directly in code. It represents data exactly as it is.

Examples:

- 42 → integer literal
- "hello" → string literal
- true → boolean literal

A struct literal is the same idea but for structs. It directly creates a struct instance in place. No function call. No variables used to build it first. It is a direct value definition.

```go
type Point struct {
    X int
    Y int
}

p := Point{X: 10, Y: 20}  // struct literal
q := &Point{X: 5}          // pointer to struct literal
```

##### Arrays - Fixed Size
https://go.dev/tour/moretypes/6

The type `[n]T` is an array:
- of n values (length n) 
- of type `T`

The expression `var a [10]int` declares a variable `a` as an array of ten integers.

An array's length is part of its type, so arrays cannot be resized. This seems limiting, but don't worry; Go provides a convenient way of working with arrays.

```go
package main

import "fmt"

func main() {
	var a [2]string
	a[0] = "Hello"
	a[1] = "World"
	fmt.Println(a[0], a[1])
	fmt.Println(a)

	primes := [6]int{2, 3, 5, 7, 11, 13}
	fmt.Println(primes)
}

// print the result:
// Hello World
// [Hello World]
// [2 3 5 7 11 13]
```

Array literals: `[6]int{2, 3, 5, 7, 11, 13}` is an array literal, it directly creates an array of type `[6]int` with those exact values `{2, 3, 5, 7, 11, 13}`.

##### Slices - Dynamic Size
https://go.dev/tour/moretypes/7
https://go.dev/tour/moretypes/8

An array has a fixed size. A slice, on the other hand, is a dynamically-sized, flexible view into the elements of an array. In practice, slices are much more common than arrays.

- A slice does not store any data, it just describes a section of an underlying array.

- Changing the elements of a slice modifies the corresponding elements of its underlying array.

- Other slices that share the same underlying array will see those changes.

- The type `[]T` is a slice with elements of type `T`.

A slice is formed by specifying two indices, a low and high bound, separated by a colon:

`a[low : high]`

This selects a half-open range which includes the first element, but excludes the last one. 

The following expression creates a slice which includes elements 1 through 3 of `a`: `a[1:4]`

```go
package main

import "fmt"

func main() {
	primes := [6]int{2, 3, 5, 7, 11, 13}

	var s []int = primes[1:4]
	fmt.Println(s)
}

// print the result:
// [3 5 7]
```

In Go, slice indexing is:
- inclusive at the start, 
- exclusive at the end.

In the example above, `primes[1:4]`:
- `primes[1]` is included → `3`
- `primes[4]` is excluded → stops before index `4`

So `[start:end]` includes `start` and goes up to but not including `end`.

##### Slice literals
https://go.dev/tour/moretypes/9

A slice literal is like an array literal without the length.

This is an array literal: `[3]bool{true, true, false}`
And this creates the same array as above, then builds a slice that references it: `[]bool{true, true, false}`

```go
package main

import "fmt"

func main() {
	q := []int{2, 3, 5, 7, 11, 13}
	fmt.Println(q)

	r := []bool{true, false, true, true, false, true}
	fmt.Println(r)

	s := []struct {
		i int
		b bool
	}{
		{2, true},
		{3, false},
		{5, true},
		{7, true},
		{11, false},
		{13, true},
	}
	fmt.Println(s)
}

// print the result:
// [2 3 5 7 11 13]
// [true false true true false true]
// [{2 true} {3 false} {5 true} {7 true} {11 false} {13 true}]
```


##### Slice defaults
https://go.dev/tour/moretypes/10

When slicing, you may omit the high or low bounds to use their defaults instead.

The default is zero for the low bound and the length of the slice for the high bound.

For the array `var a [10]int` these slice expressions are equivalent:

```go
a[0:10]
a[:10]
a[0:]
a[:]
```

```go
package main

import "fmt"

func main() {
	s := []int{2, 3, 5, 7, 11, 13}

	s = s[1:4]
	fmt.Println(s)

	s = s[:2]
	fmt.Println(s)

	s = s[1:]
	fmt.Println(s)
}

// print the result:
// [3 5 7]
// [3 5]
// [5]
```

##### Slice length and capacity
https://go.dev/tour/moretypes/11

TODO

Q: Is the capacity always from start index to end index ?
A: Yes, the capacity is always from start to end. The capacity of a slice in Go is always calculated as:
```bash
capacity = total elements in underlying array - starting index of slice
```
So it’s from the slice’s current start index to the very end of the backing array, not just the visible length.

##### Appending to a slice
https://go.dev/tour/moretypes/15

It is common to append new elements to a slice, and so Go provides a built-in append function. The [documentation](https://go.dev/pkg/builtin/#append) of the built-in package describes append.

```go
func append(s []T, vs ...T) []T
```

- The first parameter s of append is a slice of type T. 
- The rest of the arguments are T values to append to the slice (variadic parameter).
- The result of append is a new slice with all the elements of the original slice followed by the elements of the new values.

The original slice s is not modified.

Example:

```go
package main

import "fmt"

func main() {
	var s []int
	printSlice(s)

	// append works on nil slices.
	s = append(s, 0)
	printSlice(s)

	// The slice grows as needed.
	s = append(s, 1)
	printSlice(s)

	// We can add more than one element at a time.
	s = append(s, 2, 3, 4)
	printSlice(s)
}

func printSlice(s []int) {
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}

// print the result:
// len=0 cap=0 []
// len=1 cap=1 [0]
// len=2 cap=2 [0 1]
// len=5 cap=8 [0 1 2 3 4]
```

##### Slice Modifications of the underlying array - append and capacity

Does the slice modify the underling array? Yes, it does but not always.

In this example, the slice part points to the same underlying array as nums, so changing part[0] also changes nums[1].

```go
nums := []int{10, 20, 30, 40}
part := nums[1:3]  // indexes 1 and 2 → [20, 30]

part[0] = 99       // modifies underlying array

fmt.Println(nums)  // [10 99 30 40]
fmt.Println(part)  // [99 30]
```

Explanation:

- nums and part point to the same array in memory.
- Changing part[0] also changes nums[1] because they reference the same element.


Depends on the operation, the backing array may be modified or not:

|Operation                    |Modifies backing array?    | Notes |
|-----------------------------|---------------------------|-------|
|`slice[i] = value`           | Yes                       |Element is changed directly.|
|`append(slice, x) within cap`| Yes                       |Adds x to the same underlying array if capacity not exceeded.|
|`append(slice, x) beyond cap`| No (old array unchanged)  |Allocates new array, old array stays the same.|
|`copy(dst, src)`             | Yes (destination side)    |Copies values into dst, which may share array with others.|


Example: append and capacity without exceeding the capacity

```go
// makecreates a slice with:
// Length = 2 → the number of elements you can access immediately.
// Capacity = 4 → total space reserved in the backing array.
// The backing array looks like this:
//
// Index:  0   1   2   3
// Value:  0   0   _   _
//
// First two elements are zero-initialized (0 for int).
// Slots 2 and 3 are reserved for future growth but not accessible yet.
nums := make([]int, 2, 4)

// Replace the first two elements:
// nums[0] = 1
// nums[1] = 2
nums[0], nums[1] = 1, 2

// createtwo slices (a and b) that share the same underlying array as nums
a := nums[:2]
b := nums[:2]

a = append(a, 3) // capacity not exceeded, same array
b[1] = 9         // affects both a and nums

fmt.Println(nums) // [1 9 3 0]
fmt.Println(a)    // [1 9 3]
fmt.Println(b)    // [1 9]
```

Now exceed capacity:

```go
a = append(a, 4, 5) // capacity exceeded, new array allocated
a[0] = 100

fmt.Println(nums) // [1 9 3 0]   (unchanged)
fmt.Println(a)    // [100 9 3 4 5] (new separate array)
```

##### Nil slices
https://go.dev/tour/moretypes/12

The zero value of a slice is nil.

A nil slice has a length and capacity of 0 and has no underlying array.

```go
package main

import "fmt"

func main() {
	var s []int
	fmt.Println(s, len(s), cap(s))
	if s == nil {
		fmt.Println("nil!")
	}
}

// print the result:
// [] 0 0
// nil!
```

##### Creating a slice with make
https://go.dev/tour/moretypes/13

Slices can be created with the built-in make function; this is how you create dynamically-sized arrays.

The `make` function allocates a zeroed array and returns a slice that refers to that array:

```go
a := make([]int, 5)  // len(a)=5
```
To specify a capacity, pass a third argument to make:

```go
b := make([]int, 0, 5) // len(b)=0, cap(b)=5

b = b[:cap(b)] // len(b)=5, cap(b)=5
b = b[1:]      // len(b)=4, cap(b)=4
```

##### Slices of slices
https://go.dev/tour/moretypes/14

Slices can contain any type, including other slices.

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	// Create a tic-tac-toe board.
	board := [][]string{
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
	}

	// The players take turns.
	board[0][0] = "X"
	board[2][2] = "O"
	board[1][2] = "X"
	board[1][0] = "O"
	board[0][2] = "X"

	for i := 0; i < len(board); i++ {
		fmt.Printf("%s\n", strings.Join(board[i], " "))
	}
}

// print the result:
// X _ X
// O _ X
// _ _ O
```


##### Range
https://go.dev/tour/moretypes/16
https://go.dev/tour/moretypes/17
https://go.dev/tour/moretypes/18


The range form of the for loop iterates over a slice or map.

When ranging over a slice, two values are returned for each iteration. The first is the index, and the second is a copy of the element at that index.

The `range` form of the `for` loop is used to **iterate over slices, arrays, maps, strings, and channels**.
When ranging over a slice or array, it returns **two values** each iteration:

1. **Index** – position of the current element.
2. **Value** – **copy** of the element at that index.

---

###### 1. **Basic Range with Index and Value**

```go
nums := []int{10, 20, 30}

for i, v := range nums {
    fmt.Printf("Index: %d, Value: %d\n", i, v)
}
```

**Output:**

```
Index: 0, Value: 10
Index: 1, Value: 20
Index: 2, Value: 30
```

---

###### 2. **Ignore the Index**

Use `_` (underscore) to ignore the index if you only need the value.

```go
nums := []int{5, 10, 15}

for _, v := range nums {
    fmt.Println(v)
}
```

**Output:**

```
5
10
15
```

---

###### 3. **Ignore the Value**

Use `_` to ignore the value if you only need the index.

```go
nums := []int{7, 8, 9}

for i, _ := range nums {
    fmt.Println(i)
}
```

Shorter form:

```go
for i := range nums {
    fmt.Println(i)
}
```

**Output:**

```
0
1
2
```

---

###### 4. **Modify Slice Elements**

The value returned by `range` is **a copy**, not a reference.
To modify the original slice, index into it directly.

**Incorrect:**

```go
nums := []int{1, 2, 3}

for _, v := range nums {
    v *= 2 // only modifies the copy
}
fmt.Println(nums) // [1 2 3] - no change
```

**Correct:**

```go
nums := []int{1, 2, 3}

for i := range nums {
    nums[i] *= 2
}
fmt.Println(nums) // [2 4 6]
```

---

###### 5. **Range Over Strings**

When iterating over a string, `range` returns **index and rune** (Unicode code point).

```go
s := "Go💻"

for i, r := range s {
    fmt.Printf("Index: %d, Rune: %c\n", i, r)
}
```

**Output:**

```
Index: 0, Rune: G
Index: 1, Rune: o
Index: 2, Rune: 💻
```

> Note: The rune `💻` is multi-byte, so its index jumps by more than 1.

---

###### 6. **Range Over Maps**

For maps, `range` returns **key and value**.

```go
scores := map[string]int{"Alice": 90, "Bob": 80}

for name, score := range scores {
    fmt.Printf("%s scored %d\n", name, score)
}
```

**Output (order is random):**

```
Alice scored 90
Bob scored 80
```

---

###### 7. **Nested Range Loops**

Example with a slice of slices:

```go
matrix := [][]int{
    {1, 2},
    {3, 4, 5},
}

for i, row := range matrix {
    for j, val := range row {
        fmt.Printf("Row %d Col %d = %d\n", i, j, val)
    }
}
```

**Output:**

```
Row 0 Col 0 = 1
Row 0 Col 1 = 2
Row 1 Col 0 = 3
Row 1 Col 1 = 4
Row 1 Col 2 = 5
```

###### Summary Table

| **Iterable**  | **First Value** | **Second Value** |
| ------------- | --------------- | ---------------- |
| Slice / Array | Index           | Copy of element  |
| Map           | Key             | Value            |
| String        | Byte index      | Rune             |
| Channel       | Element         | *None*           |

---

###### Key Takeaways

* Use `for i, v := range slice` for both index and value.
* Ignore unused values with `_`.
* To modify slice elements, use `slice[i]` directly.
* `range` makes code concise and works uniformly across slices, maps, strings, and channels.


##### Maps
https://go.dev/tour/moretypes/19

In Go, a map is a built-in data type that stores key-value pairs.

Think of it like a dictionary in Python or a hash table in other languages:

- Keys must be of a comparable type (string, int, struct without slices, etc.).
- Values can be any type (numbers, structs, slices, etc.).

Syntax: 

```go
map[KeyType]ValueType
```


Example:

```go
map[string]int   // keys are strings, values are ints
map[int]string   // keys are ints, values are strings
map[string]Vertex // keys are strings, values are Vertex structs
```

The zero value of a map is `nil`. A nil map has no keys, nor can keys be added: Trying to do m["key"] = value will panic.

The `make` function returns a map of the given type, initialized and ready for use.

```go
package main

import "fmt"

type Vertex struct {
	Lat, Long float64
}

var m map[string]Vertex // declared, but nil

func main() {
   	// must use make() to initialize before use
	m = make(map[string]Vertex)
	m["Bell Labs"] = Vertex{
		40.68433, -74.39967,
	}
	fmt.Println(m["Bell Labs"])
}

// print the result:
// {40.68433 -74.39967}
```

##### Map literals
https://go.dev/tour/moretypes/20
https://go.dev/tour/moretypes/21

Map literals are like struct literals, but the keys are required.

```go
package main

import "fmt"

type Vertex struct {
	Lat, Long float64
}

var m = map[string]Vertex{
	"Bell Labs": Vertex{
		40.68433, -74.39967,
	},
	"Google": Vertex{
		37.42202, -122.08408,
	},
}

func main() {
	fmt.Println(m)
}

// print the result:
// map[Bell Labs:{40.68433 -74.39967} Google:{37.42202 -122.08408}]
```


If the top-level type is just a type name, you can omit it from the elements of the literal.

```go
var m = map[string]Vertex{
	"Bell Labs": {40.68433, -74.39967},
	"Google":    {37.42202, -122.08408},
}
```

##### Mutating Maps
https://go.dev/tour/moretypes/22
https://go.dev/tour/moretypes/23

Insert or update an element in map m:

```go
m[key] = elem
```

Retrieve an element:

```go
elem = m[key]
```

Delete an element:

```go
delete(m, key)
```

Test that a key is present with a two-value assignment:

```go
value, ok := m["Google"]
if ok {
    fmt.Println("Found:", value)
} else {
    fmt.Println("Not found")
}
```

If key is in m, ok is true. If not, ok is false.

If key is not in the map, then elem is the zero value for the map's element type.

```go
package main

import "fmt"

func main() {
	m := make(map[string]int)

	m["Answer"] = 42
	fmt.Println("The value:", m["Answer"])

	m["Answer"] = 48
	fmt.Println("The value:", m["Answer"])

	delete(m, "Answer")
	fmt.Println("The value:", m["Answer"])

	v, ok := m["Answer"]
	fmt.Println("The value:", v, "Present?", ok)
}

// print the result:
// The value: 42
// The value: 48
// The value: 0
// The value: 0 Present? false
```

##### Function values
https://go.dev/tour/moretypes/24

In Go:

- A function can be assigned to a variable.
- A function can be passed as an argument.
- A function can be returned as a result.

This means functions behave like any other value (ints, strings, structs, etc.).

Function values may be used as function arguments and return values.

```go
package main

import (
	"fmt"
	"math"
)

// compute is a function that takes another function (fn) as a parameter.
// That parameter must have this signature: func(float64, float64) float64
// which means fn is a function that takes two float64 arguments and returns one float64.
func compute(fn func(float64, float64) float64) float64 {
	return fn(3, 4)
}

func main() {
	hypot := func(x, y float64) float64 {
		return math.Sqrt(x*x + y*y)
	}
	fmt.Println(hypot(5, 12))

	fmt.Println(compute(hypot))
	fmt.Println(compute(math.Pow))
}

// print the result:
// 13
// 5
// 81
```

So compute is a `higher-order function` (it operates on functions).

##### Anonymous function assigned to a variable

```go
hypot := func(x, y float64) float64 {
	return math.Sqrt(x*x + y*y)
}
```

- Here we define a function without a name (an anonymous function).
- We assign it to the variable hypot.
- Now hypot holds a function value.

So we can call:

```go

hypot(5, 12) // works like a normal function
```


##### Function closures
https://go.dev/tour/moretypes/25
https://go.dev/tour/moretypes/26

Go functions may be closures. A closure is a function value that references variables from outside its body. The function may access and assign to the referenced variables; in this sense the function is "bound" to the variables.

For example, the adder function returns a closure. Each closure is bound to its own sum variable.

```go
package main

import "fmt"

func adder() func(int) int {
	sum := 0
	return func(x int) int {
		sum += x
		return sum
	}
}

func main() {
	pos, neg := adder(), adder()
	for i := 0; i < 10; i++ {
		fmt.Println(
			pos(i),
			neg(-2*i),
		)
	}
}
// print the result:
// 1 -2
// 3 -6
// 6 -12
// 10 -20
// 15 -30
// 21 -42
// 28 -56
// 36 -72
// 45 -90
```

### Methods and interfaces

##### Methods
https://go.dev/tour/methods/1

Go does not have classes. However, you can define methods on types.

A method is a function with a special **receiver argument**.

The receiver appears in its own argument list between the func keyword and the method name.

> [!IMPORTANT]
> You can only declare a method with a receiver whose type is defined in the same package as the method. 
> You cannot declare a method with a receiver whose type is defined in another package (which includes the built-in types such as int).

In this example, the Abs method has a receiver of type Vertex named v.

```go
package main

import (
	"fmt"
	"math"
)

type Vertex struct {
	X, Y float64
}

func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
	v := Vertex{3, 4}
	fmt.Println(v.Abs())
}

// print the result:
// 5
```

##### Methods are functions
https://go.dev/tour/methods/2

Methods are functions
Remember: a method is just a function with a receiver argument.

Here's Abs written as a regular function with no change in functionality.

```go
package main

import (
	"fmt"
	"math"
)

type Vertex struct {
	X, Y float64
}

func Abs(v Vertex) float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
	v := Vertex{3, 4}
	fmt.Println(Abs(v))
}

// print the result:
// 5
```

##### Methods on non-struct types
https://go.dev/tour/methods/3

You can also declare methods on non-struct types.

```go
package main

import (
	"fmt"
	"math"
)

type MyFloat float64

func (f MyFloat) Abs() float64 {
	if f < 0 {
		return float64(-f)
	}
	return float64(f)
}

func main() {
	f := MyFloat(-math.Sqrt2)
	fmt.Println(f.Abs())
}
```

#### Pointer receivers: Copy vs Reference and Methods in Go
https://go.dev/tour/methods/4


##### 1. Copy vs Reference in Go

* **Go is pass-by-value**: when you assign or pass a variable, you copy its value.
* For **simple types** (int, float, string), this is obvious: a new independent value is made.
* For **composite types** (slices, maps, channels, functions), the copy still points to the same underlying data, so changes may be visible elsewhere.


Examples by copy of value:

```go
x := 10
y := x   // copy of value
y = 20
fmt.Println(x) // 10 (unchanged)
```

```go
a := []int{1, 2, 3}
b := a   // copy of slice header
b[0] = 99
fmt.Println(a) // [99 2 3] (both see the same array)
```

Examples by copy of Pointers (A **pointer** stores the memory address of a value):

```go
v := 42
p := &v     // p points to v
fmt.Println(*p) // 42 (dereference)
*p = 100
fmt.Println(v)  // 100 (changed through pointer)
```

Pointers let you share and modify the **original value**.



##### 2. Methods in Go

You can attach methods to types.
The receiver comes **before** the method name.

```go
type Vertex struct {
    X, Y float64
}

// Value receiver
func (v Vertex) Length() float64 {
    return math.Sqrt(v.X*v.X + v.Y*v.Y)
}
```

##### 3. Value Receiver
https://go.dev/tour/methods/5

```go
func (v Vertex) Scale(f float64) {
    v.X *= f
    v.Y *= f
}
```

* `v` is a **copy** of the `Vertex`.
* Changes affect only the copy, **not** the original.

```go
v := Vertex{3, 4}
v.Scale(2)
fmt.Println(v) // {3 4} (unchanged)
```

##### 4. Pointer Receiver
https://go.dev/tour/methods/6

https://go.dev/tour/methods/4

You can declare methods with pointer receivers.

This means the receiver type has the literal syntax `*T` for some type `T`. (Also, `T` cannot itself be a pointer such as `*int`.)

For example, the Scale method here is defined on `*Vertex`:

```go
func (v *Vertex) Scale(f float64) {
    v.X *= f
    v.Y *= f
}
```

* `v` is a **pointer to the original Vertex**.
* Changes affect the original.

```go
v := Vertex{3, 4}
v.Scale(2)
fmt.Println(v) // {6 8} (modified)
```

> [!NOTE]
> Since methods often need to modify their receiver, pointer receivers are more common than value receivers.

##### Interfaces

An interface type is defined as a set of method signatures.

A value of interface type can hold any value that implements those methods.

```go
package main

import (
	"fmt"
	"math"
)

type Abser interface {
	Abs() float64
}

type MyFloat float64

func (f MyFloat) Abs() float64 {
	if f < 0 {
		return float64(-f)
	}
	return float64(f)
}

type Vertex struct {
	X, Y float64
}

func (v *Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
	var a Abser
	f := MyFloat(-math.Sqrt2)
	v := Vertex{3, 4}

	a = f  // a MyFloat implements Abser
	a = &v // a *Vertex implements Abser

	// In the following line, v is a Vertex (not *Vertex)
	// and does NOT implement Abser. ==> Compiler error: cannot use v (variable of struct type Vertex) as Abser value in assignment: Vertex does not implement Abser (method Abs has pointer receiver)
	a = v

	fmt.Println(a.Abs())
}
```

https://go.dev/tour/methods/10

**Interfaces are implemented implicitly**:

- A type implements an interface by implementing its methods. There is no explicit declaration of intent, no "implements" keyword.

- Implicit interfaces decouple the definition of an interface from its implementation, which could then appear in any package without prearrangement.


> [!NOTE]
> to better understand interfaces, we will need to understand method sets in the next sections.

###### Interface values

Mental Model

An interface value in Go can be thought of as a tuple: `(value, type)` :

- `type` = the concrete type stored inside the interface.
- `value` = the actual data of that type.

When you call a method on the interface, Go looks at the type part and runs that type’s method.

```go
package main

import "fmt"

type I interface{ M() }

type T struct{ S string }
func (t T) M() { fmt.Println("T:", t.S) }

type F float64
func (f F) M() { fmt.Println("F:", f) }

func describe(i I) {
    // %v → shows the value part.
    // %T → shows the concrete type part.
	fmt.Printf("(%v, %T)\n", i, i)
}

func main() {
	var i I

	i = T{"hello"}
	describe(i) // prints: ({hello}, main.T)
	i.M()

	i = F(3.14)
	describe(i) // prints: (3.14, main.F)
	i.M()
}

// print the result:
// ({hello}, main.T)
// T: hello
// (3.14, main.F)
// F: 3.14
```
###### Interface values with nil underlying values
If the concrete value inside the interface itself is nil, the method will be called with a nil receiver.

In some languages this would trigger a null pointer exception, but in Go it is common to write methods that **gracefully handle being called with a nil receiver** (as with the method M in this example.)

Note that an interface value that holds a nil concrete value is itself non-nil.

```go
package main

import "fmt"

type I interface {
	M()
}

type T struct {
	S string
}

func (t *T) M() {
	if t == nil {
		fmt.Println("<nil>")
		return
	}
	fmt.Println(t.S)
}

func main() {
	var i I

	var t *T
	i = t
	describe(i)
	i.M()

	i = &T{"hello"}
	describe(i)
	i.M()
}

func describe(i I) {
	fmt.Printf("(%v, %T)\n", i, i)
}

// print the result:
// (<nil>, *main.T)
// <nil>
// (&{hello}, *main.T)
// hello
```

###### Nil interface values
https://go.dev/tour/methods/13

A nil interface value holds neither value nor concrete type.

Calling a method on a nil interface is a **run-time error** because there is no type inside the interface tuple to indicate which concrete method to call.

```go
package main

import "fmt"

type I interface {
	M()
}

func main() {
	var i I
	describe(i)
	i.M()
}

func describe(i I) {
	fmt.Printf("(%v, %T)\n", i, i)
}

// print the result:
// (<nil>, <nil>)
// panic: runtime error: invalid memory address or nil pointer dereference
// [signal SIGSEGV: segmentation violation code=0x1 addr=0x0 pc=0x499219]

// goroutine 1 [running]:
// main.main()
// 	/tmp/sandbox2119689334/prog.go:12 +0x19

// Program exited.
```

###### The empty interface
https://go.dev/tour/methods/14

The interface type that specifies zero methods is known as the empty interface:

```go
interface{}
```

An empty interface may hold values of any type. (Every type implements at least zero methods.)

Empty interfaces are used by code that handles values of unknown type. For example, `fmt.Print` takes any number of arguments of type `interface{}`.

```go
package main

import "fmt"

func main() {
	// Declare a variable of type "interface{}"
	// This is the empty interface — it can hold any value
	var i interface{}

	// Right now i holds nothing → (value=nil, type=nil)
	describe(i)

	// Assign an int to i → (value=42, type=int)
	i = 42
	describe(i)

	// Assign a string to i → (value="hello", type=string)
	i = "hello"
	describe(i)
}

// describe shows both the VALUE and the TYPE
// - %v prints the stored value
// - %T prints the concrete type of that value
func describe(i interface{}) {
	fmt.Printf("(%v, %T)\n", i, i)
}

// print the result:
// (<nil>, <nil>)
// (42, int)
// (hello, string)
```


##### 5. Method Sets and Interfaces in Go
https://go.dev/tour/methods/7

**What is a Method Set?** A method set is the collection of methods that belong to a type.

It depends on whether you are dealing with a `value type (T)` or a `pointer type (*T)`.

- For a value type T: Method set includes only methods with value receivers.
- For a pointer type *T: Method set includes methods with value receivers and pointer receivers.

**Why Method Sets Matter?**

- In Go, whether a type implements an interface depends entirely on its method set.
- If you don’t understand method sets, interfaces will feel unpredictable:
- sometimes a value satisfies an interface, sometimes only a pointer does.

Example:

```go
type Vertex struct {
    X, Y float64
}

func (v Vertex) ValueMethod() {}
func (v *Vertex) PointerMethod() {}

// Vertex (a value) has method set: { ValueMethod }
// *Vertex (a pointer) has method set: { ValueMethod, PointerMethod }
```

**Why Can Values Call Pointer Methods?**

In regular code:

```go
v := Vertex{} // v is a value of type Vertex
v.PointerMethod() // ✅  Pointer method called on a value works because compiler rewrites it as: (&v).PointerMethod()

p := &Vertex{3, 4} // p is a pointer to a Vertex
p.ValueMethod()   // ✅  Value Method called on a pointer works because compiler rewrites to (*p).ValueMethod())
```

> [!IMPORTANT]
> this is syntactic sugar, not a real part of the method set:
> 1. So in direct calls, values feel like they can use both value and pointer methods.
> 2. But in interface checks, the compiler uses the official method set.

##### 6. Method Sets and Interfaces


```go
package main

import "fmt"

// Define a struct
type Vertex struct {
	X, Y float64
}

// Define two methods: one with a value receiver, one with a pointer receiver
func (v Vertex) ValueMethod() {
	fmt.Println("ValueMethod called on:", v)
}

func (v *Vertex) PointerMethod() {
	fmt.Println("PointerMethod called on:", v)
}

// Define two interfaces
type Valuer interface {
	ValueMethod()
}

type Pointerer interface {
	PointerMethod()
}

func main() {
	v := Vertex{3, 4}
	p := &v

	// --- Direct method calls ---
	v.ValueMethod()    // OK: value receiver
	v.PointerMethod()  // OK: compiler rewrites to (&v).PointerMethod()

	p.ValueMethod()    // OK: compiler rewrites to (*p).ValueMethod()
	p.PointerMethod()  // OK: pointer receiver

	// --- Interfaces ---
	var iv Valuer
	var ip Pointerer

	iv = v // OK: Vertex has ValueMethod
	iv.ValueMethod()

	iv = p // OK: *Vertex also has ValueMethod
	iv.ValueMethod()

	// ip = v // ❌ compile error: Vertex does not implement Pointerer
	ip = p // ✅ *Vertex has PointerMethod
	ip.PointerMethod()
}

```

What happens?

- `Vertex` method set = { ValueMethod }

- `*Vertex` method set = { ValueMethod, PointerMethod }

So:

- `v.ValueMethod()` ✅ works

- `v.PointerMethod()` ✅ works (compiler auto &v)

- `p.ValueMethod()` ✅ works (compiler auto *p)

- `p.PointerMethod()` ✅ works

But with interfaces:

- `Valuer` requires `ValueMethod` → both `Vertex` and `*Vertex` satisfy it.

- `Pointerer` requires `PointerMethod` → only `*Vertex` satisfies it.


##### 7. Maps refresher (since they’re reference-like)

Maps behave like references: if you pass a map into a function, modifications affect the caller’s map.




##### ✅ Key Takeaways

* **Everything in Go is passed by value.** But the value of a slice/map/pointer is itself a descriptor/reference, so modifications may affect the underlying data.
* **Value receiver** = method works on a copy, original unchanged.
* **Pointer receiver** = method works on original, can modify it.
* **Go auto-converts** between value and pointer receivers when calling methods.
* **Functions are values too**, making higher-order programming possible.
* **Maps, slices, and channels** act like references because their “value” contains a pointer to data.


#### Type assertions

A type assertion provides access to an interface value's underlying concrete value.

```go
value := i.(T)
```

This statement:
- asserts that the interface value `i` holds the concrete type `T` 
- and assigns the underlying `T` value to the variable `value`.

If `i` does not hold a `T`, the statement will trigger a **panic**.

To test whether an interface value holds a specific type, a type assertion can return two values: the underlying value and a boolean value that reports whether the assertion succeeded.

```go
value, ok := i.(T)
```

If `i` holds a `T`, then `t` will be the underlying value and `ok` will be true.

If not, `ok` will be false and `value` will be the zero value of type `T`, and **no panic occurs**.


> [!NOTE]
> Note the similarity between this syntax and that of reading from a map.

```go
package main

import "fmt"

func main() {
	var i interface{} = "hello"

	s := i.(string)
	fmt.Println(s) // print: hello

	s, ok := i.(string)
	fmt.Println(s, ok) // print: hello true

	f, ok := i.(float64)
	fmt.Println(f, ok) // print: 0 false

	f = i.(float64) //panic: interface conversion: interface {} is string, not float64
	fmt.Println(f) 
}
```
#### Type switches
https://go.dev/tour/methods/16

A type switch is a construct that permits several type assertions in series, it has the same syntax as a type assertion but the specific type T is replaced with the keyword `type`: `my_variable.(type)`.

A type switch:
- is like a regular switch statement, 
- but the cases in a type switch specify types (not values), and those values are compared against the type of the value held by the given interface value.

```go
switch v := i.(type) {
case T:
    // here v has type T
case S:
    // here v has type S
default:
    // no match; here v has the same type as i
}
```

This switch statement tests whether the `interface value i` holds a value of type `T` or `S`. In each of the `T` and `S` cases, the variable `v` will be of type `T` or `S` respectively and hold the value held by `i`. In the default case (where there is no match), the variable `v` is of the same interface type and value as `i`.

```go
package main

import "fmt"

func describe(i interface{}) {
	switch v := i.(type) {
	case int:
		fmt.Println("int:", v)
	case string:
		fmt.Println("string:", v)
	case fmt.Stringer: // interface type!
		fmt.Println("Stringer:", v.String())
	default:
		fmt.Printf("unknown type %T\n", v)
	}
}

type Person struct{ Name string }

// Person implements fmt.Stringer
func (p Person) String() string { return "Person(" + p.Name + ")" }

func main() {
	describe(42)  // print: int: 42
	describe("hello") // print: string: hello
	describe(Person{"Alice"}) // print: Stringer: Person(Alice)
}
```

#### Stringers interface
https://go.dev/tour/methods/17

One of the most ubiquitous interfaces is Stringer defined by the fmt package.

```go
type Stringer interface {
    String() string
}
```

A Stringer is a type that can describe itself as a string. The fmt package (and many others) look for this interface to print values.

```go
package main

import "fmt"

type Person struct {
	Name string
	Age  int
}

func (p Person) String() string {
	return fmt.Sprintf("%v (%v years)", p.Name, p.Age)
}

func main() {
	a := Person{"Arthur Dent", 42}
	z := Person{"Zaphod Beeblebrox", 9001}
	fmt.Println(a, z) // Arthur Dent (42 years) Zaphod Beeblebrox (9001 years)
}
```

#### Error interface
https://go.dev/tour/methods/19

Go programs express error state with error values.

The error type is a built-in interface similar to `fmt.Stringer`:

```go
type error interface {
    Error() string
}
```

(As with `fmt.Stringer`, the `fmt` package looks for the error interface when printing values.)

Functions often return an error value, and calling code should handle errors by testing whether the error equals `nil`.

```go
i, err := strconv.Atoi("42")
if err != nil {
    fmt.Printf("couldn't convert number: %v\n", err)
    return
}
fmt.Println("Converted integer:", i)
```

A nil error denotes success; a non-nil error denotes failure.

##### errors.New → simplest, fixed message.

Using errors.New — simple failure (file open)

This fits a common case: operation fails, no extra details needed.

package main

import (
	"errors"
	"fmt"
	"os"
)

func readConfig() error {
	// pretend the config file must exist
	if _, err := os.Stat("config.json"); errors.Is(err, os.ErrNotExist) {
		return errors.New("config file not found")
	}
	return nil
}

func main() {
	if err := readConfig(); err != nil {
		fmt.Println("Error:", err)
		return
	}
	fmt.Println("Config loaded successfully")
}


Possible Output (if config.json missing)

Error: config file not found


This feels real: you’re checking for a file, and if it doesn’t exist, you fail with a clear error.

##### Example with fmt.Errorf add context with formatting.

```go
package main

import (
	"fmt"
)

func divide(a, b int) (int, error) {
	if b == 0 {
		return 0, fmt.Errorf("cannot divide %d by zero", a)
	}
	return a / b, nil
}

func main() {
	if result, err := divide(10, 0); err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Println("Result:", result)
	}
}
```

key points:

- `func divide(a, b int) (int, error)` is a function that divides two numbers and returns an error if the division is by zero.
- `fmt.Errorf` is used to create an error value with a formatted message.
- `result, err := divide(10, 0)` is used to divide two numbers and return an error if the division is by zero.

##### Example with custom error type

When you want to attach structured data (time, operation, code, etc.) to an error, define a struct and make it satisfy the error interface with `Error()`.

```go
package main

import (
	"fmt"
	"time"
)

type TimeoutError struct {
	Op   string    // what operation we were doing
	When time.Time // when it happened
}

func (e *TimeoutError) Error() string {
	return fmt.Sprintf("operation %q timed out at %v", e.Op, e.When)
}

func connectToServer() error {
	// pretend the server didn't respond
	return &TimeoutError{
		Op:   "dial tcp server:8080",
		When: time.Now(),
	}
}

func main() {
	if err := connectToServer(); err != nil {
		fmt.Println("Error:", err)
	}
}
// print the result: Error: operation "dial tcp server:8080" timed out at 2025-09-26 18:45:03 +0000 UTC
```


##### errors.Is and errors.As

Since Go 1.13, you should prefer errors.Is and errors.As for checking errors.
They work with wrapped errors (fmt.Errorf("...: %w", err)) and with custom error types.

1. errors.Is — check for a specific sentinel error

The os package defines sentinel errors like os.ErrNotExist.

package main

import (
	"errors"
	"fmt"
	"os"
)

func main() {
	_, err := os.Open("missing.txt")

	if errors.Is(err, os.ErrNotExist) {
		fmt.Println("file does not exist")
	} else if err != nil {
		fmt.Println("some other error:", err)
	}
}


Output

file does not exist


👉 Why not just err == os.ErrNotExist?
Because os.Open may wrap the error with more context.
errors.Is works through the wrapping chain.

2. errors.As — extract a specific error type

Some libraries return custom error types. For example, the standard library’s *os.PathError holds info about the failing operation, path, and underlying error.

package main

import (
	"errors"
	"fmt"
	"os"
)

func main() {
	_, err := os.Open("missing.txt")

	var pathErr *os.PathError
	if errors.As(err, &pathErr) {
		fmt.Println("PathError details:")
		fmt.Println(" Op:", pathErr.Op)     // "open"
		fmt.Println(" Path:", pathErr.Path) // "missing.txt"
		fmt.Println(" Err:", pathErr.Err)   // "no such file or directory"
	}
}


Output

PathError details:
 Op: open
 Path: missing.txt
 Err: no such file or directory

✅ Teaching Payoff

errors.Is = “does this error (possibly wrapped) equal a known error value?”

errors.As = “does this error (possibly wrapped) have this type? If so, extract it.”

Realistic because:

os.Open is a real standard library call.

`os.ErrNotExist` and `*os.PathError` are real-world errors you’ll encounter often.





##### Error handling best practices

Most real-world Go functions return a value and an error.

This combines both useful results and error handling.

When to use what:

- `errors.New` → simplest, fixed message.
- `fmt.Errorf` → add context with formatting.
- `Custom struct` → attach extra fields (time, operation, codes).

#### Readers
https://go.dev/tour/methods/21
TODO

#### Images
https://go.dev/tour/methods/24


### Generics

#### Type parameters
https://go.dev/tour/generics/1

#### Generic types
https://go.dev/tour/generics/2


### Concurrency

#### Goroutines

https://go.dev/tour/concurrency/1

#### Channels
https://go.dev/tour/concurrency/2

#### Buffered Channels
https://go.dev/tour/concurrency/3

#### Range and Close
https://go.dev/tour/concurrency/4

#### Select
https://go.dev/tour/concurrency/5

#### Default Selection
https://go.dev/tour/concurrency/6

#### sync.Mutex
https://go.dev/tour/concurrency/9

### Where to go from here

https://go.dev/tour/concurrency/11


## How to organize your code

{{ link_with_abstract("go-organizing-code") }}