---
layout: post
title: "Bash"
date: 2014-03-16 19:59:15 +0100
comments: true
categories: 
---
# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}


# References

* Bash on Evernote: https://www.evernote.com/shard/s106/nl/11497273/917f4214-9719-438b-b9ea-6a58f43e968f/
* Bash Guide for Beginners, with real-life instead of theoretical examples:
  * HTML: http://tldp.org/LDP/Bash-Beginners-Guide/html/
  * PDF : ~/Dropbox/Books/Bash-Beginners-Guide.pdf
* Advanced Bash-Scripting Guide http://tldp.org/LDP/abs/html/

# Bash History

unset HISTFILE: If HISTFILE is unset, or if the history file is unwritable, the history is not saved.

If you want to toggle it off:

* Turn Off: `set +o history`
* Turn on: `set -o history`

# The Bash Environment

Ref: http://tldp.org/LDP/Bash-Beginners-Guide/html/chap_03.html

## Shell Initialization Files

Ref: http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_01.html

* `/etc/profile`
* `/etc/bashrc`
* `~/.bash_profile`
* `~/.bash_login`
* `~/.profile`
* `~/.bashrc`
* `~/.bash_logout`

## Variables


Ref:

* http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_02.html
* http://tldp.org/LDP/Bash-Beginners-Guide/html/chap_10.html


### local VS global

* `Global variables or environment variables`: are available in all shells.
* `Local variables`: are only available in the current shell. 

* Variables are case sensitive
* Convention: local variables are lowercase

Each and every shell has its own environment.

**There's no Universal environment that will magically appear in all console windows.**

An environment variable created in one shell cannot be accessed in another shell.
It's even more restrictive. If one shell spawns a subshell, that subshell has access to the parent's environment variables, but if that subshell creates an environment variable, it's not accessible in the parent shell.

If all of your shells need access to the same set of variables, you can create a startup file that will set them for you. This is done in BASH via the $HOME/.bash_profile and $HOME/.bashrc files and through $HOME/.profile if $HOME/.bash_profile doesn't exist).

`export` governs which variables will be available to subshells

```
FOO=1
export BAR=2
./runScript.sh
```

then $BAR will be available in the environment of runScript.sh, but $FOO will not.


Let say we have this script that print the `name` variable:

```
# print_name.sh
echo My name is $name
```

And we run it:

```
name="nicola"
echo "My name is $name" # prints "My name is nicola"
./print_name.sh         # prints "My name is " beacuse name is local
export name="nicola"
./print_name.sh         # prints "My name is " beacuse now name is global

```


### Creating variables

`VARNAME="value"`

* spaces around the equal sign will cause error
* good habit to quote content strings when assigning values to variables
* Only ASCII letters (of either case), _ and digits are supported, 
* The first character must not be a digit (ex: 1myname is not allowed).

### Variables in a function

* By default all variables are global.
* Setting or modifying a variable in a function changes it in the whole script.
* You can create a local variables using the `local` command
  * makes the variable name have a visible scope restricted to that function and its children only.
  * syntax is:

```
function name(){
   local var=$1
}
```


Ex of set without local: bash_examples/function_local_vars.sh

```
#!/bin/bash

define_not_local_var ()
{
  not_local_variable="bar"
}

define_not_local_var

echo "not_local_variable is global: $not_local_variable"

# print:
# not_local_variable is global: bar

```

Ex of modify without local: bash_examples/function_local_vars_2.sh

```
#!/bin/bash

not_local_variable="foo"

echo "not_local_variable is global: $not_local_variable"

define_not_local_var ()
{
  not_local_variable="bar"
}

define_not_local_var

echo "not_local_variable is modified by the function: $not_local_variable"

# print:
# not_local_variable is global: foo
# not_local_variable is modified by the function: bar
```

Ex of modify with local: bash_examples/function_local_vars_3.sh


```
#!/bin/bash

my_var="foo"

echo "my_var is global: $my_var"

define_local_var ()
{
  local my_var="bar"
}

define_local_var

echo "my_var is NOT modified by the function: $my_var"
```


### Typing variables: declare or typeset

Ref: http://tldp.org/LDP/abs/html/declareref.html

The declare or typeset builtins, which are exact synonyms, permit modifying the properties of variables. This is a very weak form of the typing

* readonly variables: `declare -r`

```
declare -r var1=1
echo $var1   # print: 1
var1 = 2     # print: bash: declare: var1: readonly variable
echo $var1   # stil print: 1
```

* integer variables: `declare -i`

```
declare -i number
# The script will treat subsequent occurrences of "number" as an integer.		

number=3
echo "Number = $number"     # Number = 3

number=three
echo "Number = $number"     # Number = 0
# Tries to evaluate the string "three" as an integer.
```


### env command

* `env`
  * run a program in a modified environment

```
env name=value name2=value2 program and args
```

Runs the command program and args with an environment formed by extending the current environment with the environment variables and values designated by name=value and name2=value2. If you do not include any arguments like name=value, then the current environment is passed along unmodified.

NOTE env VS printenv: 

* env is POSIX 7, printenv is not (GNU Coreutils in Ubuntu 15.10)
* printenv can only print variables
* TIP: use always env

### Reserved Variables and positional params

* `$@`	Expands to the positional parameters, starting from one. When the expansion occurs within double quotes, each parameter expands to a separate word.
* `$*`	(similar to $@ but less used) Expands to the positional parameters, starting from one. When the expansion occurs within double quotes, it expands to a single word with the value of each parameter separated by the first character of the IFS special variable.
* `$#`	Expands to the number of positional parameters in decimal.
* `$?`	Expands to the exit status of the most recently executed foreground pipeline.
* `$-`	A hyphen expands to the current option flags as specified upon invocation, by the set built-in command, or those set by the shell itself (such as the -i).
* `$$`	Expands to the process ID of the shell.
* `$!`	Expands to the process ID of the most recently executed background (asynchronous) command.
* `$0`	Expands to the name of the shell or shell script.
* `$_`	The underscore variable is set at shell startup and contains the absolute file name of the shell or script being executed as passed in the argument list. Subsequently, it expands to the last argument to the previous command, after expansion. It is also set to the full pathname of each command executed and placed in the environment exported to that command. When checking mail, this parameter holds the name of the mail file.

Some examples: on the other special parameters:

```
franky ~> grep dictionary /usr/share/dict/words
dictionary

franky ~> echo $_
/usr/share/dict/words

franky ~> echo $$
10662

franky ~> mozilla &
[1] 11064

franky ~> echo $!
11064

franky ~> echo $0
bash

franky ~> echo $?
0  # Ok

franky ~> ls doesnotexist
ls: doesnotexist: No such file or directory

franky ~> echo $?
1  # Error
```


The positional parameters are the words following the name of a shell script: `$1`, `$2`, etc

```
#!/bin/bash

# positional.sh
# This script reads 3 positional parameters and prints them out.

POSPAR1="$1"
POSPAR2="$2"
POSPAR3="$3"

echo "$1 is the first positional parameter, \$1."
echo "$2 is the second positional parameter, \$2."
echo "$3 is the third positional parameter, \$3."
echo
echo "The total number of positional parameters is $#."
eche
echo "The list of params is: $@"
```

Upon execution one could give any numbers any arguments:

```
franky ~> positional.sh one two three four five
one is the first positional parameter, $1.
two is the second positional parameter, $2.
three is the third positional parameter, $3.

The total number of positional parameters is 5.
The list of params is: one two three four five
```

```
franky ~> positional.sh one two
one is the first positional parameter, $1.
two is the second positional parameter, $2.
 is the third positional parameter, $3.

The total number of positional parameters is 2.
The list of params is: one two
```

Other variables:

* `CDPATH` A colon-separated list of directories used as a search path for the cd built-in command.
* `HOME` The current user's home directory; the default for the cd built-in. The value of this variable is also used by tilde expansion.
* `IFS`	A list of characters that separate fields; used when the shell splits words as part of expansion.
* `MAIL` If this parameter is set to a file name and the MAILPATH variable is not set, Bash informs the user of the arrival of mail in the specified file.
* `MAILPATH` A colon-separated list of file names which the shell periodically checks for new mail.
* `OPTARG` The value of the last option argument processed by the getopts built-in.
* `OPTIND` The index of the last option argument processed by the getopts built-in.
* `PATH` A colon-separated list of directories in which the shell looks for commands.
* `PS1` The primary prompt string. The default value is "'\s-\v\$ '".
* `PS2` The secondary prompt string. The default value is "'> '".
* `auto_resume`	This variable controls how the shell interacts with the user and job control.
* `BASH`	The full pathname used to execute the current instance of Bash.
* `BASH_ENV`	If this variable is set when Bash is invoked to execute a shell script, its value is expanded and used as the name of a startup file to read before executing the script.
* `BASH_VERSION`	The version number of the current instance of Bash.
* `BASH_VERSINFO`	A read-only array variable whose members hold version information for this instance of Bash.
* `COLUMNS`	Used by the select built-in to determine the terminal width when printing selection lists. Automatically set upon receipt of a SIGWINCH signal.
* `COMP_CWORD`	An index into ${COMP_WORDS} of the word containing the current cursor position.
* `COMP_LINE`	The current command line.
* `COMP_POINT`	The index of the current cursor position relative to the beginning of the current command.
* `COMP_WORDS`	An array variable consisting of the individual words in the current command line.
* `COMPREPLY`	An array variable from which Bash reads the possible completions generated by a shell function invoked by the programmable completion facility.
* `DIRSTACK`	An array variable containing the current contents of the directory stack.
* `EUID`	The numeric effective user ID of the current user.
* `FCEDIT`	The editor used as a default by the -e option to the fc built-in command.
* `FIGNORE`	A colon-separated list of suffixes to ignore when performing file name completion.
* `FUNCNAME`	The name of any currently-executing shell function.
* `GLOBIGNORE`	A colon-separated list of patterns defining the set of file names to be ignored by file name expansion.
* `GROUPS`	An array variable containing the list of groups of which the current user is a member.
* `histchars`	Up to three characters which control history expansion, quick substitution, and tokenization.
* `HISTCMD`	The history number, or index in the history list, of the current command.
* `HISTCONTROL`	Defines whether a command is added to the history file.
* `HISTFILE`	The name of the file to which the command history is saved. The default value is ~/.bash_history.
* `HISTFILESIZE`	The maximum number of lines contained in the history file, defaults to 500.
* `HISTIGNORE`	A colon-separated list of patterns used to decide which command lines should be saved in the history list.
* `HISTSIZE`	The maximum number of commands to remember on the history list, default is 500.
* `HOSTFILE`	Contains the name of a file in the same format as /etc/hosts that should be read when the shell needs to complete a hostname.
* `HOSTNAME`	The name of the current host.
* `HOSTTYPE`	A string describing the machine Bash is running on.
* `IGNOREEOF`	Controls the action of the shell on receipt of an EOF character as the sole input.
* `INPUTRC`	The name of the Readline initialization file, overriding the default /etc/inputrc.
* `LANG`	Used to determine the locale category for any category not specifically selected with a variable starting with LC_.
* `LC_ALL`	This variable overrides the value of LANG and any other LC_ variable specifying a locale category.
* `LC_COLLATE`	This variable determines the collation order used when sorting the results of file name expansion, and determines the behavior of range expressions, equivalence classes, and collating sequences within file name expansion and pattern matching.
* `LC_CTYPE`	This variable determines the interpretation of characters and the behavior of character classes within file name expansion and pattern matching.
* `LC_MESSAGES`	This variable determines the locale used to translate double-quoted strings preceded by a "$" sign.
* `LC_NUMERIC`	This variable determines the locale category used for number formatting.
* `LINENO`	The line number in the script or shell function currently executing.
* `LINES`	Used by the select built-in to determine the column length for printing selection lists.
* `MACHTYPE`	A string that fully describes the system type on which Bash is executing, in the standard GNU CPU-COMPANY-SYSTEM format.
* `MAILCHECK`	How often (in seconds) that the shell should check for mail in the files specified in the MAILPATH or MAIL variables.
* `OLDPWD`	The previous working directory as set by the cd built-in.
* `OPTERR`	If set to the value 1, Bash displays error messages generated by the getopts built-in.
* `OSTYPE`	A string describing the operating system Bash is running on.
* `PIPESTATUS`	An array variable containing a list of exit status values from the processes in the most recently executed foreground pipeline (which may contain only a single command).
* `POSIXLY_CORRECT`	If this variable is in the environment when bash starts, the shell enters POSIX mode.
* `PPID`	The process ID of the shell's parent process.
* `PROMPT_COMMAND`	If set, the value is interpreted as a command to execute before the printing of each primary prompt (PS1).
* `PS3`	The value of this variable is used as the prompt for the select command. Defaults to "'#? '"
* `PS4`	The value is the prompt printed before the command line is echoed when the -x option is set; defaults to "'+ '".
* `PWD`	The current working directory as set by the cd built-in command.
* `RANDOM`	Each time this parameter is referenced, a random integer between 0 and 32767 is generated. Assigning a value to this variable seeds the random number generator.
* `REPLY`	The default variable for the read built-in.
* `SECONDS`	This variable expands to the number of seconds since the shell was started.
* `SHELLOPTS`	A colon-separated list of enabled shell options.
* `SHLVL`	Incremented by one each time a new instance of Bash is started.
* `TIMEFORMAT`	The value of this parameter is used as a format string specifying how the timing information for pipelines prefixed with the time reserved word should be displayed.
* `TMOUT`	If set to a value greater than zero, TMOUT is treated as the default timeout for the read built-in. In an interative shell, the value is interpreted as the number of seconds to wait for input after issuing the primary prompt when the shell is interactive. Bash terminates after that number of seconds if input does not arrive.
* `UID`	The numeric, real user ID of the current user.

# Array

* http://tldp.org/LDP/abs/html/arrays.html#ARRAYREF
* http://mywiki.wooledge.org/BashGuide/Arrays

# Functions

Ref: http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_11_01.html

* Shell functions are a way to group commands for later execution, using a single name for this group, or routine.
* A function is executed within the shell in which it has been declared: no new process is created to interpret the commands.
* exit status is the exit status of the last command executed in the body.
* The body of a function should end in a semicolon or a newline.
* The curly braces must be separated from the body by spaces, otherwise they are interpreted in the wrong way.

Syntax:

```
function function_name { 
  command...
} 
```

or (with this syntax parenthesis are needed):

```
function_name () { 
  command... 
} 
```

A function may be "compacted" into a single line :

* `fun () { echo "This is a function"; echo; }` # OK
* `fun () { echo "This is a function"; echo }`  # Error!
*  semicolon must follow the final command in the function.

Functions are called, triggered, simply by invoking their names. A function call is equivalent to a command.

Parameters:



Functions and variable scope:

```
define_local (){
  local local_variable="foo"
}

define_not_local ()
{
  not_local_variable="bar"
}

define_local
define_not_local

echo "local_variable is empty: $local_variable"
echo "not_local_variable: $not_local_variable"
```


# Server side management

## Logs

### Read compressed Logs

http://www.cyberciti.biz/tips/decompress-and-expand-text-files.html

* `zless data.txt.gz`
* `zmore data.txt.gz`
* `zcat file.gz`
* `zegrep -w '^word1|word2' file.gz`
* `zgrep 'wordToSearch' file.gz`

NOTE: use gzcat on OSX

### Log Rotation

TODO

# Write and debugging shell scripts

If you don't want to start a new shell but execute the script in the current shell, you source it: source script_name.sh

`#!`: The first line of the script determines the shell to start. The first two characters of the first line should be #!, then follows the path to the shell that should interpret the commands that follow. EX: `#!/bin/bash`

Debug with `bash -x`: (or add in your script set -x) The most common is to start up the subshell with the -x option, which will run the entire script in debug mode. Traces of each command plus its arguments are printed to standard output after the commands have been expanded but before they are executed.

## Examples: one line script

while true; echo "AA"; sleep 2; done

# Conditional: if then else

* Basic intro: http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-6.html
* string and file operators `help test`

~~~bash
if [ "foo" = "foo" ]; then
   echo expression evaluated as true
else
   echo expression evaluated as false
fi
~~~

# Alias

* Aliases allow a string to be substituted for a word when it is used as the first word of a simple command.
* Aliases are expanded when a function definition is read, not when the function is executed,

# Directory Stack

* `pushd`
* `popd`
* `dirs`

# Execution Programs

When the program being executed is a shell script bash will use Fork-and-exec mechanism:

* This child process has the same environment as its parent, only the process ID number is different. This procedure is called forking.
* The address space of the child process is overwritten with the new process data. This is done through an exec call to the system.
* reads the lines from the shell script one line at a time: Commands on each line are read, interpreted and executed as if they would have come directly from the keyboard.
* the parent shell waits for its child process to finish.

NOTE: built-in commands are executed without creating a new process.



# Bash built in commands

Built-in commands are necessary to implement functionality impossible or inconvenient to obtain with separate utilities.

Bash supports 3 types of built-in commands:

Bourne Shell built-ins: `:, ., break, cd, continue, eval, exec, exit, export, getopts, hash, pwd, readonly, return, set, shift, test, [, times, trap, umask and unset`.

Bash built-in commands: `alias, bind, builtin, command, declare, echo, enable, help, let, local, logout, printf, read, shopt, type, typeset, ulimit and unalias`

Special built-in commands, When Bash is executing in POSIX mode, the special built-ins differ from other built-in commands in three respects:

1. Special built-ins are found before shell functions during command lookup.
2. If a special built-in returns an error status, a non-interactive shell exits.
3. Assignment statements preceding the command stay in effect in the shell environment after the command completes.

The POSIX special built-ins are :`, ., break, continue, eval, exec, exit, export, readonly, return, set, shift, trap and unset`.


## exec

### Use exec to redirect outputs from within a script

REF: http://stackoverflow.com/questions/8888251/understanding-bash-exec-12-command

Example:

~~~bash
function example()
{
    exec 1>&2  # from this point one stdout will be directed to stderr
    cat <<EOT
Script requires at least one parameter.
EOT
    exit 1
} 
~~~

## set

Ref:

* `man set`  https://www.gnu.org/software/bash/manual/bashref.html#index-set
* http://unix.stackexchange.com/questions/255581/what-does-set-command-without-arguments-do

`set` allows you:

* to change the values of shell options
* set the positional parameters
* to display the names and values of shell variables (Without arguments, set will print all shell variables (both environment variables and variables in current session) sorted in current locale).


# Parsing bash script options from command line 

* http://sookocheff.com/post/bash/parsing-bash-script-arguments-with-shopts/
* http://dustymabe.com/2013/05/17/easy-getopt-for-a-bash-script/


* http://stackoverflow.com/questions/78497/design-patterns-or-best-practices-for-shell-scripts

## GETOPTS

* `help getopts`
* `getopts` tutorial: http://wiki.bash-hackers.org/howto/getopts_tutorial

Getopts is used by shell procedures to parse positional parameters as options.

Syntax: `getopts: getopts optstring name [arg]`

* OPTSTRING contains the option letters to be recognized; if a letter is followed by a colon, the option is expected to have an argument, which should be separated from it by white space.
* Each time it is invoked, getopts will place the next option in the shell variable $name, initializing name if it does not exist, and the index of the next argument to be processed into the shell variable OPTIND.
* When an option requires an argument, getopts places that argument into the shell variable OPTARG.

BEST PRACTICE: The common way is that the processing of all arguments precedes the actual job of the program/script. 

# Config File: read a config file in bash without using source

http://stackoverflow.com/questions/4434797/read-a-config-file-in-bash-without-using-source

# Get the Script source file path

ref: http://www.ostricher.com/2014/10/the-right-way-to-get-the-directory-of-a-bash-script/

~~~
get_script_dir () {
     SOURCE="${BASH_SOURCE[0]}"
     # While $SOURCE is a symlink, resolve it
     while [ -h "$SOURCE" ]; do
          DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
          SOURCE="$( readlink "$SOURCE" )"
          # If $SOURCE was a relative symlink (so no "/" as prefix, need to resolve it relative to the symlink base directory
          [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE"
     done
     DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
     echo "$DIR"
}
~~~

# Command line utilities

## JQ to filter JSON

Ref:

* http://stedolan.github.io/jq/manual/#ConditionalsandComparisons
* https://github.com/stedolan/jq/wiki/Cookbook#filter-objects-based-on-the-contents-of-a-key
