
`pyproject.toml` is a standard configuration file used in Python packaging. It was introduced to streamline the way Python projects declare their metadata and dependencies, replacing older methods like `setup.py` and `setup.cfg`.


The format is defined by PEP 518 and PEP 621, [PEP 735](https://peps.python.org/pep-0735/) establishing it as a formal standard within the Python community for specifying project metadata and build system requirements. PEP are not easy to read and understand, but these official documents you can find more about the standard:

* [Writing pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
* [pyproject.toml specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)

`pip` is the official tool to install Python packages and can be used to install dependencies declared in `pyproject.toml` but also other tools like `uv` use this standard to manage dependencies. Other tools requires a different format, for example poetry uses a `pyproject.toml` file with a slightly different syntax.


## Dependencies and requirements

This the official documentation about dependencies and requirements: [Dependencies and requirements](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#dependencies-and-requirements)

### Dependencies specifiers

We didn't find a very handy reference to understand the dependencies specifiers, but these are some of the official documentation: 

* [pip dependency resolution](https://pip.pypa.io/en/stable/topics/dependency-resolution/)
* [Dependencies specifiers](https://packaging.python.org/en/latest/specifications/dependency-specifiers/#dependency-specifiers)

Here is the list of the specifiers:

* `>`: Any version greater than the specified version. Example: `>3.1` means any version greater than 3.1.

* `<`: Any version less than the specified version. Example: `<3.1` means any version less than 3.1.

* `<=`: Any version less than or equal to the specified version. Example: `<=3.1` means any version less than or equal to 3.1.

* `>=`: Any version greater than or equal to the specified version. Example: `>=3.1` means any version greater than or equal to 3.1.

* `==`: Exactly the specified version. Example: `==3.1` means only version 3.1.

* `!=`: Any version not equal to the specified version. Example: `!=3.1` means any version other than 3.1.

* `~=`: Any version compatible with the specified version. Example: `~=3.1` means any version compatible with 3.1. Compatible versions are higher versions that only differ in the final segment. `~=3.1.2` is equivalent to `>=3.1.2,==3.1.*`. `~=3.1` is equivalent to `>=3.1,==3.*`.

* `*`: Any version. Example: `*` means any version.




### Required dependencies - `dependencies`

Required dependencies are those necessary for your package to function correctly. They should be declared in the dependencies key within the [project] table of your pyproject.toml file. For example:

```toml
[project]
name = "examplePy"
dependencies = [
    "rioxarray",
    "geopandas",
]
```

These dependencies will be installed automatically when users install your package via a package manager.



### Optional extras dependencies

Optional dependencies are commonly referred to as `extras` in Python, particularly in the context of package management. This terminology comes from the standard defined in PEP 508, which specifies a mechanism for declaring and installing optional features or extensions for a package. 

These extras are specified in the `[project.optional-dependencies]`, a subtable of the `[project]` table.

A common use case for extras is when a package provides optional features that are not required for the core functionality. For example, a web framework might define a `database` extra for users who need database functionality:

```toml
[project.optional-dependencies]
database = ["sqlalchemy"]
```

**Extras vs. Regular Dependencies**: 

The term “extras” is derived from the syntax and behavior used to specify these optional dependencies when installing a package. For example:

* Regular Dependencies: Always installed with the package and are required for the core functionality.
* Extras: Optional and installed only if explicitly requested.

```bash
pip install my_project[extra_name]
```

> [!NOTE] extras are not the recommended way to manage development dependencies. Instead, dependency groups or similar mechanisms provided by modern tools like poetry, pdm, or uv are considered better practices [LEARN MORE HERE](#dependency-groups-in-pyproject). 


### Dependency Groups in pyproject

Dependency groups are an alternative to extras to manage development dependencies.

In this section of the PEP you can find the motivation for the introduction of dependency groups: [Motivation](https://peps.python.org/pep-0735/#motivation), TL;DR: In modern Python development, it’s crucial to clearly distinguish between:

* dependencies required by the **end-users** of a package (commonly referred to as extras as [defined above](#optional-extras-dependencies))
* and those needed by the **developers** of the package. 

Dependency groups offer a clear solution to this problem.

They are defined in the `[dependency-groups]` table of the `pyproject.toml` file.


By maintaining this clear separation, you enhance the developer experience (DX) and ensure that end-users receive a streamlined, dependency-efficient package.

> [!NOTE] Official documentation: [Dependency groups in pyproject.toml](https://peps.python.org/pep-0735)

To better understand how dependency groups work, let's compare them with extras:

#### When to use extras

When your package is meant to be used by other developers and you want to make some dependencies optional, the only way to do it is by using extras. Consumer of your package will have to install them explicitly:

```bash
pip install example-package[featureX]
uv add example-package[featureX]
```

In both cases, the specified extra dependencies are installed alongside the main package, providing additional functionality.

> [!WARNING] When you are a Consumer of a package, you have no way to use dependency groups.

#### When to use dependency groups

The use of dependency groups is primarily intended for the developers of a package. These groups allow developers to organize and manage dependencies needed during the development process, such as testing frameworks, documentation tools, or linters. By defining these dependencies in groups, developers can install them as needed without including them in the package’s core dependencies, ensuring that end-users are not burdened with unnecessary packages.

The typical workflow is:

1. clone the repo
2. install the dependencies with the groups you need:
3. run your tests or develop your packages

Examples can be:
* you are the author of a library
* you developing a web app with django and you need to install the django dependencies and the testing framework

#### Example: PDM package

The [PDM project](https://github.com/pdm-project/pdm) on GitHub provides a practical example of using **dependency groups** in its `pyproject.toml` file. This approach organizes dependencies into specific categories, enhancing clarity and manageability.

Example from PDM's `pyproject.toml`:

```toml
[dependency-groups]

test = [

  "pdm[pytest]",

  "pytest-cov",

  "pytest-xdist>=1.31.0",

  "pytest-rerunfailures>=10.2",

    "pytest-httpserver>=1.0.6",
]

tox = [
    "tox",
    "tox-pdm>=0.5",
]

doc = [
    "mkdocs>=1.1",
    "mkdocs-material>=7.3",
    "mkdocstrings[python]>=0.18",
    "setuptools>=62.3.3",
    "markdown-exec>=0.7.0",
    "mkdocs-redirects>=1.2.0",
    "mkdocs-version-annotations>=1.0.0",
]

workflow = [
    "parver>=0.3.1",
    "towncrier>=20",
    "pycomplete~=0.3",
]
```

In this configuration:

- test **Group**: Contains testing-related dependencies like pytest and its plugins.

- tox **Group**: Includes tox and related plugins for automation.

- doc **Group**: Lists documentation tools such as mkdocs and its extensions.

- workflow **Group**: Comprises tools for release management and versioning.

By defining these groups, developers can install specific sets of dependencies as needed, streamlining the development process and ensuring that only relevant packages are included in different environments.
