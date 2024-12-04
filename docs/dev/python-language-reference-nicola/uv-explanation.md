## Key Features Nicola's uses

## Features Overview
This is the official list of features: https://docs.astral.sh/uv/getting-started/features/

Additional notes:
- `uv` is a tool to manage Python projects.
- `uv python list`: shows available Python versions installed in the system also by other tools like pyenv or asdf.
- `uv python list --all-versions`: shows all available and installable Python versions.


## Project configuration Best practices


* `.python-version`: The `.python-version` file contains the project's default Python version. This file tells uv which Python version to use when creating the project's virtual environment.

https://docs.astral.sh/uv/guides/projects/#python-version

## HOWTO Getting started with uv

```bash
# install the Python version 3.12 if not already installed
uv python install 3.12

# list the Python versions available
uv python list

# create the virtual environment for the current project
uv venv

uv add flask

# sync the dependencies in the virtual environment
uv sync

# run the Flask application
uv run -- flask run -p 3000

# OR ALTERNATIVELY activate the virtual environment
source .venv/bin/activate
flask run -p 3000
```


## HOWTO optional dependencies

`uv` respect the `pyproject.toml standard configuration file` used in Python packaging. This standard is described in the [Pyproject standard explanation](pyproject-stardard-explanation.md), the relevant part to better understand how `uv` manage optional dependencies are:

* dependency-groups
* project.optional-dependencies
* [Dependencies specifiers](pyproject-stardard-explanation.md#dependencies-specifiers)


### dependency-groups

Add a dependency to a specific group:

```bash
uv add --group docs mkdocs
uv add --group dev black
```

> [!NOTE] `uv add --dev black` is a shortcut for `uv add --group dev black`

Install the dependencies in specific groups:

```bash
uv sync --group testing --group linting
```

> [!WARNING] If you want to skip the installation of dev dependencies you must use `uv sync --no-group dev` (see the next section to understand why)

#### Default groups

TL;DR: you can be confused by the default groups. Let's clarify this.

It's important to understand that:
* Every project has default groups: https://docs.astral.sh/uv/reference/settings/#default-groups
* The default value of `default-groups` is `[dev]`

So by default the `uv sync` command installs the dependencies in the `dev` group.
Basically the default behavior of `uv` is to execute `uv sync --group dev`

So if you want to 

### project.optional-dependencies

Example:

```toml
[project.optional-dependencies]
dev = ["pytest", "black"]
docs = ["sphinx", "myst-parser"]
```

Dependencies are specified in [project.optional-dependencies] in a TOML-compatible format. Each key represents a group name, and the value is a list of dependencies for that group.

To installs the dependencies in the `dev` group.

```bash
uv sync --extra dev
```

To install multiple optional dependency groups simultaneously:

```bash
uv sync --extra dev --extra docs
```

If you want to include all optional dependencies, use:

```bash
uv sync --all-extras
```

## HOWTO Lock dependencies

https://docs.astral.sh/uv/concepts/projects/sync/

## HOWTO create a new project

```bash
uv init myproject
cd myproject
# Add django package
uv add django
```

## TUTORIAL explore the project dependencies

```bash
uv tree

# myproject v0.1.0
# └── django v5.1.3
#     ├── asgiref v3.8.1
#     └── sqlparse v0.5.2
```
Now let's see how `uv` helps with dependency management when two Python packages require the same dependency.
A great example of two Python packages requiring the same dependency is `requests` and `httpx`, both of which may depend on `certifi`, a package that provides Mozilla’s CA Bundle for SSL/TLS verification.

```bash
uv add requests httpx
uv tree
# myproject v0.1.0
# ├── django v5.1.3
# │   ├── asgiref v3.8.1
# │   └── sqlparse v0.5.2
# ├── httpx v0.28.0
# │   ├── anyio v4.6.2.post1
# │   │   ├── idna v3.10
# │   │   └── sniffio v1.3.1
# │   ├── certifi v2024.8.30         ##### <<<<< SAME DEPENDENCY
# │   ├── httpcore v1.0.7
# │   │   ├── certifi v2024.8.30     ##### <<<<< SAME DEPENDENCY
# │   │   └── h11 v0.14.0
# │   └── idna v3.10
# └── requests v2.32.3
#     ├── certifi v2024.8.30         ##### <<<<< SAME DEPENDENCY
#     ├── charset-normalizer v3.4.0
#     ├── idna v3.10
#     └── urllib3 v2.2.3
```

If you need to find which package is requiring a dependency, you can use the `uv tree --invert` command:

```bash
uv tree --invert
# asgiref v3.8.1
# └── django v5.1.3
#     └── myproject v0.1.0
# certifi v2024.8.30
# ├── httpcore v1.0.7
# │   └── httpx v0.28.0
# │       └── myproject v0.1.0
# ├── httpx v0.28.0 (*)
# └── requests v2.32.3
#     └── myproject v0.1.0
# charset-normalizer v3.4.0
# └── requests v2.32.3 (*)
# h11 v0.14.0
# └── httpcore v1.0.7 (*)
# idna v3.10
# ├── anyio v4.6.2.post1
# │   └── httpx v0.28.0 (*)
# ├── httpx v0.28.0 (*)
# └── requests v2.32.3 (*)
# sniffio v1.3.1
# └── anyio v4.6.2.post1 (*)
# sqlparse v0.5.2
# └── django v5.1.3 (*)
# urllib3 v2.2.3
# └── requests v2.32.3 (*)
# (*) Package tree already displayed
```

From the tree above you can see that `certifi` is a dependency of `httpx`, `requests` and `httpcore`.


