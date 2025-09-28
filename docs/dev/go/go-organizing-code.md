---
title: Tutorial – Organizing Go Code
abstract: >
  In this tutorial, you'll build your first Go program inside a module, organize your code into packages, and use the `go` tool to build, run, and test your code. By the end, you'll have a working program, a custom package, and tests — all organized using Go's module system.
---

# Tutorial – Organizing Go Code

## What you'll learn

In this tutorial, we will:

- Create a new Go module
- Build a simple Go program
- Organize code into a reusable package
- Import external packages
- Run tests for your code

By the end, you'll have a fully working Go project with local and external packages.

---

## Step 1: Set up your Go module

Let's start by creating a folder for your project and initializing it as a Go module.

```bash
$ mkdir hello
$ cd hello
$ go mod init example/user/hello
````

Let’s check the `go.mod` file:

```bash
$ cat go.mod
module example/user/hello
```

Great — your module is ready.

---

## Step 2: Write your first Go program

Inside your `hello` directory, create a file called `hello.go`:

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, world.")
}
```

Now, let's build and install it:

```bash
$ go install
```

Try running the program:

```bash
$ hello
Hello, world.
```

✅ You’ve just written and run your first Go program.

---

## Step 3: Add a reusable package

Let’s organize our code by creating a new package called `morestrings`.

```bash
$ mkdir morestrings
$ touch morestrings/reverse.go
```

Paste this code into `reverse.go`:

```go
package morestrings

func ReverseRunes(s string) string {
    r := []rune(s)
    for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
        r[i], r[j] = r[j], r[i]
    }
    return string(r)
}
```

This function reverses a string.

Now let’s use it in your main program. Modify `hello.go`:

```go
package main

import (
    "fmt"
    "example/user/hello/morestrings"
)

func main() {
    fmt.Println(morestrings.ReverseRunes("!oG ,olleH"))
}
```

Rebuild and run:

```bash
$ go install
$ hello
Hello, Go!
```

✅ You've created and used your first custom package.

---

## Step 4: Import an external package

Now let's use a package from GitHub: [`go-cmp`](https://github.com/google/go-cmp).

Update your `hello.go`:

```go
package main

import (
    "fmt"
    "example/user/hello/morestrings"
    "github.com/google/go-cmp/cmp"
)

func main() {
    fmt.Println(morestrings.ReverseRunes("!oG ,olleH"))
    fmt.Println(cmp.Diff("Hello World", "Hello Go"))
}
```

Tidy up and install:

```bash
$ go mod tidy
$ go install
$ hello
Hello, Go!
  string(
-     "Hello World",
+     "Hello Go",
  )
```

✅ You’ve successfully imported and used an external Go module.

---

## Step 5: Write a test

Let’s write a test for `ReverseRunes`.

Create `morestrings/reverse_test.go`:

```go
package morestrings

import "testing"

func TestReverseRunes(t *testing.T) {
    cases := []struct {
        in, want string
    }{
        {"Hello", "olleH"},
        {"世界", "界世"},
    }
    for _, c := range cases {
        got := ReverseRunes(c.in)
        if got != c.want {
            t.Errorf("ReverseRunes(%q) == %q, want %q", c.in, got, c.want)
        }
    }
}
```

Run the test:

```bash
$ cd morestrings
$ go test
PASS
ok  	example/user/hello/morestrings
```

✅ You've written and run your first Go test.

---

## Next steps

You now have:

* A working Go module and command
* A reusable package
* An external dependency
* A test suite

Next, you could:

* Add more features
* Explore Go’s testing framework
* Publish your module

To clean up downloaded dependencies:

```bash
$ go clean -modcache
```

---

> For more details, see:
>
> * [Go Modules](https://golang.org/ref/mod)
> * [Go Command Reference](https://golang.org/cmd/go/)
> * [Go Testing](https://golang.org/pkg/testing/)













---
title: Tutorial – Organizing Go Code
abstract: >
  In this tutorial, you'll build your first Go program inside a module, organize your code into packages, and use the `go` tool to build, run, and test your code. By the end, you'll have a working program, a custom package, and tests — all organized using Go's module system.
---

# Tutorial – Organizing Go Code

## What you'll learn

In this tutorial, we will:

- Create a new Go module
- Build a simple Go program
- Organize code into a reusable package
- Import external packages
- Run tests for your code

By the end, you'll have a fully working Go project with local and external packages.

---

## Step 1: Set up your Go module

Let's start by creating a folder for your project and initializing it as a Go module.

```bash
mkdir hello
cd hello
go mod init example/user/hello
```

Let’s check the `go.mod` file:

```bash
cat go.mod
# module example/user/hello
# go 1.23
```

Great — your module is ready.

---

## Step 2: Write your first Go program

Inside your `hello` directory, create a file called `hello.go`:

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, world.")
}
```

Now, let's build it:

```bash
go build
```

Try running the program:

```bash
./hello
# Hello, world.
```

✅ You’ve just written and run your first Go program.

---

## Step 3: Add a reusable package

Let’s organize our code by creating a new package called `morestrings`.

```bash
$ mkdir morestrings
$ touch morestrings/reverse.go
```

Paste this code into `reverse.go`:

```go
package morestrings

func ReverseRunes(s string) string {
    r := []rune(s)
    for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
        r[i], r[j] = r[j], r[i]
    }
    return string(r)
}
```

This function reverses a string.

Now let’s use it in your main program. Modify `hello.go`:

```go
package main

import (
    "fmt"
    "example/user/hello/morestrings"
)

func main() {
    fmt.Println(morestrings.ReverseRunes("!oG ,olleH"))
}
```

Rebuild and run:

```bash
go install
./hello
Hello, Go!
```

✅ You've created and used your first custom package.

---

## Step 4: Import an external package

Now let's use a package from GitHub: [`go-cmp`](https://github.com/google/go-cmp).

Update your `hello.go`:

```go
package main

import (
    "fmt"
    "example/user/hello/morestrings"
    "github.com/google/go-cmp/cmp"
)

func main() {
    fmt.Println(morestrings.ReverseRunes("!oG ,olleH"))
    fmt.Println(cmp.Diff("Hello World", "Hello Go"))
}
```

Tidy up and install:

```bash
go mod tidy
go build
./hello
# Hello, Go!
#   string(
# -     "Hello World",
# +     "Hello Go",
# )
```

✅ You’ve successfully imported and used an external Go module.

---

## Step 5: Write a test

Let’s write a test for `ReverseRunes`.

Create `morestrings/reverse_test.go`:

```go
package morestrings

import "testing"

func TestReverseRunes(t *testing.T) {
    cases := []struct {
        in, want string
    }{
        {"Hello", "olleH"},
        {"世界", "界世"},
    }
    for _, c := range cases {
        got := ReverseRunes(c.in)
        if got != c.want {
            t.Errorf("ReverseRunes(%q) == %q, want %q", c.in, got, c.want)
        }
    }
}
```

Run the test:

```bash
cd morestrings
go test
# PASS
# ok  	example/user/hello/morestrings 0.322s
```

✅ You've written and run your first Go test.

---

## Next steps

You now have:

* A working Go module and command
* A reusable package
* An external dependency
* A test suite

Next, you could:

* Add more features
* Explore Go’s testing framework
* Publish your module

To clean up downloaded dependencies:

```bash
$ go clean -modcache
```

---

> For more details, see:
>
> * [Go Modules](https://golang.org/ref/mod)
> * [Go Command Reference](https://golang.org/cmd/go/)
> * [Go Testing](https://golang.org/pkg/testing/)

