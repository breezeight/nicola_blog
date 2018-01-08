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

* Short intro e-book for developer with some bash internal, written by a bash author: http://aosabook.org/en/bash.html



# Bash History

unset HISTFILE: If HISTFILE is unset, or if the history file is unwritable, the history is not saved.

If you want to toggle it off:

* Turn Off: `set +o history`
* Turn on: `set -o history`

# Bash Libraries

* https://dberkholz.com/2011/04/07/bash-shell-scripting-libraries/

# Bash Unit Testing

* Bats: https://github.com/sstephenson/bats
* urchin: https://github.com/tlevine/urchin   NVM uses Urchin to run test 

# Bash linter



https://github.com/koalaman/shellcheck

brew install shellcheck

# Bash complex projects



## Dokku

https://github.com/dokku/dokku

* use the bats test framework

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

* `Global variables or environment variables`: are available in all sub-shells.
* `Local variables`: are only available in the current shell. 

* By default all variables are global.
* Variables are case sensitive
* Convention: local variables are lowercase
* global variable cannot not be modified in the parent shell from a sub-shell because they are copied, not referenced.

Each and every shell has its own environment.

**There's no Universal environment that will magically appear in all console windows.**

* An environment variable created in one shell cannot be accessed in another shell.
* If one shell spawns a subshell, that subshell has access to the parent's environment variables, but if that subshell creates an environment variable, it's not accessible in the parent shell.

* TIPS: If all of your shells need access to the same set of variables, you can create a startup file that will set them for you. This is done in BASH via the $HOME/.bash_profile and $HOME/.bashrc files and through $HOME/.profile if $HOME/.bash_profile doesn't exist).

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

#### Example.1 Simple Bash Variable Assignment Usage

The following script creates a variable called LIST and assigns the value “/var/opt/bin”. To access the variables, just prefix the variable name with $, which will give you the value stored in that variable.

```
$ cat sample.sh
#!/bin/bash
LIST="/var/opt/bin/"
ls -l $LIST
```

Execute the above script, which will list the /var/opt/bin in long format as shown below.

```
$ ./sample.sh
total 8
drwxrwsr-x 2 bin  bin 4096 Jan 29 06:43 softwares
drwxr-sr-x 5 root bin 4096 Sep  2  2009 llist
```

#### Example 2. Blank values in bash variables

```
$ cat var1.sh
#!/bin/sh
echo "Variable value is: $VAR1"
VAR1="GEEKSTUFF"
echo "Variable value is: $VAR1"

$ ./var1.sh
Variable value is:
Variable value is: GEEKSTUFF
```

As shown above, initially the variable will have a blank value, after assigning, you can get your values. export command is used to export a variables from an interactive shell. export shows the effect on the scope of variables.

#### Example 3. Bash Variables without export

Assign a variable with a value in an interactive shell, and try to access the same in your shell script.

```
$ VAR2=LINUX

$ cat var2.sh
#!/bin/bash
echo "VAR2=$VAR2"
VAR2=UNIX
echo "VAR2=$VAR2"
```

Now, execute the above script as shown below.

```
$ ./var2.sh
VAR2=
VAR2=UNIX
```

Still you will get blank value for variable VAR2. The shell stores variable VAR2 with the LINUX only in the current shell. During the execution of var2.sh, it spawns the shell and it executes the script. So the variable VAR2 will not have the value in the spawned shell. You need to export the variable for it to be inherited by another program – including a shell script, as shown below.

#### Example 4. Exporting a Bash Variable

```
$ export VAR2=LINUX

$ cat var2.sh
#!/bin/bash
echo "VAR2=$VAR2"
VAR2=UNIX
echo "VAR2=$VAR2"
```

Now execute the above script.

```
$ export VAR2=LINUX

$ ./var2.sh
VAR2=LINUX
VAR2=UNIX
$
$echo $VAR2 # VAR2 is not modified in the parent shell:
LINUX
```

Now, you can notice that after execution of the shell script var2.sh, the value of VAR2 is LINUX. 

NOTE:

* VAR2 is not modified in the parent shell: it's a copy, you can't get that value up to the parent shell 
* Because the variables will not be passed back to your interactive shell, unless you execute the script in the current shell.

#### Example 5: 

https://unix.stackexchange.com/questions/79064/how-to-export-variables-from-a-file

set -a causes variables defined from now on to be automatically exported. It's available in any Bourne-like shell. . is the standard and Bourne name for the source command so I prefer it for portability (source comes from csh and is now available in most modern Bourne-like shells including bash though (sometimes with a slightly different behaviour)).

In POSIX shells, you can also use set -o allexport as a more descriptive alternative way to write it (set +o allexport to unset).

```
set -a
. ./tmp.txt
set +a
```


tmp.txt file contains the variables to be exported, for e.g.

```
a=123
b="hello world"
c="one more variable"
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

Syntax: `declare option variablename`

* declare is a keyword
* option could be:
  * `-r` read only variable
  * `-i` integer variable
  * `-a` array variable
  * `-f` for funtions
  * `-x` declares and export to subsequent commands via the environment.

Examples:

```
declare -r var1=1
echo $var1   # print: 1
var1 = 2     # print: bash: declare: var1: readonly variable
echo $var1   # stil print: 1
```


```
declare -i number
# The script will treat subsequent occurrences of "number" as an integer.		

number=3
echo "Number = $number"     # Number = 3

number=three
echo "Number = $number"     # Number = 0
# WARNING: Tries to evaluate the string "three" as an integer. It evaluate to 0.

number=3.4 # syntax error: invalid arithmetic operator (error token is ".4")
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

### bashrc VS profile

ISSUE: Suppose I have export MY_VAR=0 in ~/.bashrc: it is overridden in every new shell


That's your mistake right there. You should define your environment variables in ~/.profile, which is read when you log in. ~/.bashrc is read each time you start a shell; when you start the inner shell, it overrides MY_VAR. If you hadn't done that, your environment variable would propagate downards.

* http://unix.stackexchange.com/questions/8342/export-an-env-variable-to-be-available-at-all-sub-shells-and-possible-to-be-mod
* http://superuser.com/questions/183870/difference-between-bashrc-and-bash-profile

### Reserved Variables and positional params

* `$@`	Expands to the positional parameters, starting from one. When the expansion occurs within double quotes, each parameter expands to a separate word.
* `$*`	(similar to $@ but less used) Expands to the positional parameters, starting from one. When the expansion occurs within double quotes, it expands to a single word with the value of each parameter separated by the first character of the IFS special variable.
* `$#`	Expands to the number of positional parameters in decimal.
* `$?`	Expands to the exit status of the most recently executed foreground pipeline.
* `$-`	A hyphen expands to the current option flags as specified upon invocation, by the set built-in command, or those set by the shell itself (such as the -i).
* `$$`	Expands to the PID of the shell.
* `$!`	Expands to the PID of the most recently executed background (asynchronous) command.
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


# Simple commands

REF: http://wiki.bash-hackers.org/syntax/basicgrammar#simple_commands

# Pipelines

REF: http://wiki.bash-hackers.org/syntax/basicgrammar#pipelines

# Command List

REF: http://wiki.bash-hackers.org/syntax/basicgrammar#lists

A list is a sequence of one or more pipelines separated by one of the operators:

``` 

;
&
&&
││

```

and optionally terminated by one of

```
;
&
<newline>
```

# Compound Commands

Compound commands have the following characteristics:

* they begin and end with a specific keyword or operator (e.g. `for … done` )
* they can be redirected as a whole

For a list See REF: http://wiki.bash-hackers.org/syntax/basicgrammar#compound_commands




# Input parsing and execution flow

Advanced Ref, with some internals: http://aosabook.org/en/bash.html
Nice Graphical example: http://stuff.lhunath.com/parser.png
Really nice intro: http://mywiki.wooledge.org/BashParser

Before fork-exec, a shell analyze the it's input:

1) The shell reads its input from a file, from a string or from the user's terminal.

2) Perform lexical analysis and parsing:

* Input is broken up into words and operators, obeying the quoting rules

* Token are separated by metacharacter http://www.angelfire.com/mi/genastorhotz/reality/computers/linux/bashmetachars.html

3) Perform expansions and substitutions:

* Brace expansion
* Tilde expansion
* Variable and parameter expansion
* Command substitution
* Process substitution
* Arithmetic substitution
* Word splitting
* Filename generation


4) The shell parses (analyzes and substitutes) the tokens into simple and compound commands, breaking the expanded tokens into lists of filenames and commands and arguments.

* Redirection is performed if necessary, redirection operators and their operands are removed from the argument list.

* Commands are executed.

* Optionally the shell waits for the command to complete and collects its exit status.

### Examples

https://stackoverflow.com/questions/31252710/how-does-bash-tokenize-scripts

Why isn't there a space necessary between ] and ;?

```
if [$x = $y];
if [ $x = $y ];
```

`if` checks the status code of the command to the right `[` is a command; thus, `[foo` tries to find a command (named, say, `/usr/bin/[foo`), requiring whitespace.



## Metacharacter

 http://www.angelfire.com/mi/genastorhotz/reality/computers/linux/bashmetachars.html

* `<`
* `>`
* `>>`
* `|`
* `?`
* `*`
* `[]`
* `$`
* ` \ `
* `( )`
* ` { } `
* " "
* ' '
* ` ` 
* ` && `
* ` || `
* ` & `
* ` ; `
* ` = ` 


## Quoting Character

Ref:

* http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_03.html
* Posix standard: http://pubs.opengroup.org/onlinepubs/009695399/utilities/xcu_chap02.html#tag_02_02

Quoting is used to remove the special meaning of characters or words: quotes can disable special treatment for special characters

Quoting can be used to:

* preserve the literal meaning of the special characters in the next paragraph,
* prevent reserved words from being recognized as such,
* prevent parameter expansion and command substitution within here-document processing (see [Here-Document](http://pubs.opengroup.org/onlinepubs/009695399/utilities/xcu_chap02.html#tag_02_07_04)).

The application shall quote the following characters if they are to represent themselves:

```
|  &  ;  <  >  (  )  $  `  \  "  '  <space>  <tab>  <newline>
```

and the following may need to be quoted under certain circumstances. That is, these characters may be special depending on conditions described elsewhere in this volume of IEEE Std 1003.1-2001:

```
*   ?   [   #   ˜   =   %
```

The various quoting mechanisms are

* the escape character,
* single-quotes,
* double-quotes.
* The here-document represents another form of quoting; 


### Escape Characters

`\ ` :  is used as an escape character in Bash. It preserves the literal value of the next character that follows, with the exception of newline.

```
franky ~> date=20021226

franky ~> echo $date
20021226

franky ~> echo \$date
$date
```

### Single quotes

Single quotes ('') are used to preserve the literal value of each character enclosed within the quotes.

Single quotes protect all characters except the backslash (\).

```
franky ~> echo '$date'
$date
```

A single quote may not occur between single quotes:

```
echo ''$date''
20021226
```

even when preceded by a backslash:

### Double quotes

Double quotes protect all characters except the backslash (\), dollar sign ($) and grave accent (` `).

* The dollar sign and the backticks retain their special meaning within the double quotes.

* The backslash retains its meaning only when followed by dollar, backtick, double quote, backslash or newline. Within double quotes, the backslashes are removed from the input stream when followed by one of these characters.
* Backslashes preceding characters that don't have a special meaning are left unmodified for processing by the shell interpreter.
* A double quote may be quoted within double quotes by preceding it with a backslash.

```
franky ~> echo "$date"
20021226

franky ~> echo "`date`"
Sun Apr 20 11:22:06 CEST 2003

franky ~> echo "I'd say: \"Go for it!\""
I'd say: "Go for it!"

franky ~> echo "\"
More input>"

franky ~> echo "\\"
\
```

### Single and double quotes protect each other.

For example:

```
$ echo 'Hi "Intro to Unix" Class'
Hi "Intro to Unix" Class

$ echo "Hi 'Intro to Unix' Class"
Hi 'Intro to Unix' Class
```

# Shell Expansion and Substitutions

Ref:

* http://wiki.bash-hackers.org/syntax/pe
* CHEATSHEET: http://www.tldp.org/LDP/abs/html/refcards.html#AEN22728

## Brace expansion

Is a mechanism by which arbitrary strings may be generated.

Syntax: `PREAMBLE{ ... , ... }POSTSCRIPT`

* PREAMBLE: prefixed to each string contained within the braces
* POSTSCRIPT: appended to each resulting string

* The results of each expanded string are not sorted; left to right order is preserved
* To avoid conflicts with parameter expansion, the string "${" is not considered eligible for brace expansion.
* must contain unquoted opening and closing braces, and at least one unquoted comma.
* ORDER: performed before any other expansions
* characters special to other expansions are preserved in the result
* strictly textual: not apply any syntactic interpretation to the context of the expansion or the text between the braces

Examples:

```

echo \"{These,words,are,quoted}\"   # " prefix and suffix
# "These" "words" "are" "quoted"


cat {file1,file2,file3} > combined_file
# Concatenates the files file1, file2, and file3 into combined_file.

cp file22.{txt,backup}
# Copies "file22.txt" to "file22.backup"
```

## Extended Brace Expansion

Syntax: `{a..z}`

```
echo {a..z} # a b c d e f g h i j k l m n o p q r s t u v w x y z
# Echoes characters between a and z.

echo {0..3} # 0 1 2 3
# Echoes characters between 0 and 3.


base64_charset=( {A..Z} {a..z} {0..9} + / = )
# Initializing an array, using extended brace expansion.
# From vladz's "base64.sh" example script.

```

## Tilde expansion

* `~+` the value of PWD replaces the tilde-prefix.
* `~-` the value of the shell variable OLDPWD, if it is set, is substituted.
* .... etc see here https://www.gnu.org/software/bash/manual/html_node/Tilde-Expansion.html


## Exapansions with $

The `$` character introduces:

* parameter expansion,
* command substitution,
* arithmetic expansion.


### Shell parameter

### Variable expansion

### Aritmethic expansion

Allows the evaluation of an arithmetic expression and the substitution of the result.

Syntax:

* `$(( EXPRESSION ))`
* `$[]`

All tokens in the expression undergo parameter expansion, command substitution, and quote removal, Example:

```
echo $( wc -w package.json| awk '{print $1}' ) # packge.json count 169 words
echo $(( $( wc -w package.json| awk '{print $1}' ) + 1 )) # print 170 add 1 after cmd substitution

a=3
b=7

echo $[$a+$b]   # 10
echo $[$a*$b]   # 21
```

Arithmetic substitutions may be nested:


```
echo $(( $(( 3 + 2 )) * 3 )) # prints 15
```

The operators are roughly the same as in the C programming language. In order of decreasing precedence, the list looks like this:

* `VAR++` and `VAR--` :	variable post-increment and post-decrement
* `++VAR` and `--VAR` :	variable pre-increment and pre-decrement
* `-`, `+`, `*`, `/` multiplication, division,	addition, subtraction
* `%` remainder
* `!` and `~`	logical and bitwise negation
* `**`	exponentiation
* `<<` and `>>`	left and right bitwise shifts
* `<=`, `>=`, `<` and `>`	comparison operators
* `==` and `!=`	equality and inequality
* `&`	bitwise AND
* `^`	bitwise exclusive OR
* `|`	bitwise OR
* `&&`	logical AND
* `||`	logical OR
* `expr ? expr : expr`	conditional evaluation
* `=`, `*=`, `/=`, `%=`, `+=`, `-=`, `<<=`, `>>=`, `&=`, `^=` and `|=`	assignments
* `,`	separator between expressions

Within an expression, shell variables may also be referenced by name without using the parameter expansion syntax:

```
n=4
echo  $(( 10%n )) # prints 2
```

See also `expr` and `let`: http://tldp.org/LDP/abs/html/internal.html#LETREF


### Command substitution

Ref: http://tldp.org/LDP/abs/html/commandsub.html  With a lot of examples!


Bash performs the expansion by executing COMMAND and replacing the command substitution with the **standard output** of the command ( with any trailing newlines deleted, embedded newlines are not deleted ).

The execution is done in a separate process with fork-exec

Syntax: `$(command)` or `command`

NOTE: The `$(...)` form has superseded backticks for command substitution. It permit nesting:

```
word_count=$( wc -w $(echo * | awk '{print $8}') )
```

### Substring Manipulations

Keep in mind that the substitutions etc are expanded, not literals, so you can use wildcards and other pattern syntaxes in them (for example, the “he*l” below used to strip “hell” from the value).

```
$ echo ${param1:2} llo substring from 2
$ echo ${param1:2:2} ll substring from 2, len 2
$ echo ${param1#he} llo strip shortest match from start
$ echo ${param1#hel*} lo strip shortest match from start
$ echo ${param1#he*l} lo strip shortest match from start
$ echo ${param1##he*l} o strip longest match from start
$ echo ${param1%l*o} hel strip shortest match from end
$ echo ${param1%%l*o} he strip longest match from end
$ echo ${param1/l/p} heplo replace as few as possible
$ echo ${param1//l/p} heppo replace as many as possible
```

Miscellaneous:

```
$ echo ${!param*} param1 param2 param3 parameter names starting with...
$ echo ${#param1} 5 length of parameter value
```

Example Uses:

```
# Rename all .GIF files to .gif
for file in *.GIF; do mv $file ${file%GIF}gif; done
# Now number the files sequentially
cnt=0;
for file in *.gif; do mv $file $cnt$file; let cnt=cnt++; done
# Oops, I didn't mean that... get rid of the numbers.
for file in *.gif; do mv $file ${file##[0-9]}; done
```


### Default Values

$ echo ${param2:-file*} file1 file2 file3 all files in the directory
$ echo ${param2:-$param1} hello uses $param1's value...
$ echo $param2 (nothing) ... but didn't change $param2
$ echo ${param3:=$param1} hello uses $param1's value...
$ echo $param3 hello ... and assigns it to $param3

## Process Substitution

REF:
 
* http://aosabook.org/en/bash.html
* http://wiki.bash-hackers.org/syntax/expansion/proc_subst

One of the problems with command substitution is that it runs the enclosed command immediately and waits for it to complete: there's no easy way for the shell to send input to it.

Bash uses a feature named process substitution, a sort of combination of command substitution and shell pipelines, to compensate for these shortcomings. Like command substitution, bash runs a command, but lets it run in the background and doesn't wait for it to complete. The key is that bash opens a pipe to the command for reading or writing and exposes it as a filename, which becomes the result of the expansion.




Process substitution is a form of redirection where the input or output of a process (some sequence of commands) appear as a temporary file.

Syntax:

```
<( <LIST> )

>( <LIST> )
```

LIST is a command list (ex: `command || command` )

The command list <LIST> is executed and its

* standard output filedescriptor in the `<( … )` form or
* standard input filedescriptor in the `>( … )`  form

is connected to a FIFO or a file in /dev/fd/. The filename (where the filedescriptor is connected) is then used as a substitution for the `<(…)-construct`.

Basically you will end up with a tmp file you can use to read or write.

SCOPE:

* If a process substitution is expanded as an argument to a function, expanded to an environment variable during calling of a function, or expanded to any assignment within a function, the process substitution will be "held open" for use by any command within the function or its callees, until the function in which it was set returns.

* If the same variable is set again within a callee, unless the new variable is local, the previous process substitution is closed and will be unavailable to the caller when the callee returns.

In essence, process substitutions expanded to variables within functions remain open until the function in which the process substitution occured returns - even when assigned to locals that were set by a function's caller. Dynamic scope doesn't protect them from closing.


PRO:

* You can use to avoid to spawn new subshell with pipe (see here http://wiki.bash-hackers.org/syntax/expansion/proc_subst#avoiding_subshells)


Example: use redirection and process substitution

```
counter=0
 
while IFS= read -rN1 _; do
    ((counter++))
done < <(find /etc -printf ' ')
 
echo "$counter files"
```

## Word Splitting (or field splitting)

Ref: http://wiki.bash-hackers.org/syntax/expansion/wordsplit

Word splitting occurs once any of the following expansions are done (and only then!):

* Parameter expansion
* Command substitution
* Arithmetic expansion

Bash will scan the results of these expansions for special `IFS`(Internal Field Separator) characters that mark word boundaries. This is only done on results that are not double-quoted!

The IFS variable holds the characters that Bash sees as word boundaries in this step. The default contains the characters:

* space
* tab
* newline

These characters are also assumed when IFS is unset. When IFS is empty (nullstring), no word splitting is performed at all.

Q: IFS is typically discussed in the context of "field splitting". Is field splitting the same as word splitting ?
A: yes

Q: The POSIX specification says: "If the value of IFS is null, no field splitting shall be performed."
Is setting IFS= the same as setting IFS to null? Is this what is meant by setting it to an empty string too?
A: yes

Q: Say I want to restore the default value of IFS. How do I do that? (more specifically, how do I refer to <tab> and <newline>?)
A: you could do something like `IFS=$' \t\n'` . However, it's better to use another variable to temporarily store the old IFS value, and then restore it afterwards (or temporarily override it for one command by using the var=foo command syntax).

Ref: https://unix.stackexchange.com/questions/26784/understanding-ifs

### IFS examples

```
while IFS= read -r line
do    
    echo $line
done < /path_to_text_file
```

The first code snippet will put the entire line read, verbatim, into $line, as there are no field separators to perform word splitting for. Bear in mind however that since many shells use cstrings to store strings, the first instance of a NUL may still cause the appearance of it being prematurely terminated.


The behaviour if we we change the first line to

```
while read -r line # Use the default IFS value
```

is: put an exact copy of the input into $line. For example, if there are multiple consecutive field separators, they will be made into a single instance of the first element. This is often recognised as loss of surrounding whitespace

The behaviour if we we change the first line to:

```
while IFS=' ' read -r line
```

will do the same as the second, except it will only split on a space (not the usual space, tab, or newline).

## File name expansion

occurs once any of the following expansions are done (and only then!):

* Parameter expansion
* Command substitution
* Arithmetic expansion
* Word Splitting

unless the -f option has been set (see Section 2.3.2), Bash scans each word for the characters:

* `*`
* `?`
* `[`

If one of these characters appears:

* the word is regarded as a PATTERN, and replaced with an alphabetically sorted list of file names matching the pattern.
* If no matching file names are found, and the shell option nullglob is disabled, the word is left unchanged. 
* If the `nullglob` option is set, and no matches are found, the word is removed.
* If the shell option `nocaseglob`<D-`>s is enabled, the match is performed without regard to the case of alphabetic characters.

NOTE; `set -f` or `set -o noglob`	Disable file name generation using metacharacters (globbing).

## Common issue and and examples

### Spaces

http://unix.stackexchange.com/questions/100945/word-splitting-when-parameter-is-used-within-command-substitution

```
file="/home/1_cr/xy z"
basename $file # prints: xy

basename "$file" # prints: xy z

```


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

## Parameters

* positional parameters passed to a function are not the same as the ones passed to a command or script.

When a function is executed:

* the arguments to the function become the positional parameters during its execution.
* The special parameter `#` that expands to the number of positional parameters is updated to reflect the change.
* Positional parameter 0 is unchanged. The Bash variable `FUNCNAME` is set to the name of the function, while it is executing.


```
ciao(){ echo $0; echo $FUNCNAME $1; echo $#; true; };
21:07 ~/SRC/nicola_blog/_guides (master)$ ciao Nicola
-bash
ciao Nicola
1
```

## return values from a function

REF: http://www.linuxjournal.com/content/return-values-bash-functions


Bash functions, unlike functions in most programming languages **do not allow you to return a value to the caller**. When a bash function ends its return value is its status: zero for success, non-zero for failure. 

To return values, you can:

* set a global variable with the result,
* or use command substitution,
* or you can pass in the name of a variable to use as the result variable. 

### Return an integer

If you only want to return an integer value from a bash function, use `return`:

```
#!/bin/bash

function return_code_test ()
{
return 50
}

return_code_test
echo "return_code_test returned $?"
```

When the `return` built-in is executed in a function:

* the function completes and execution resumes with the next command after the function call.
* When a function completes, the values of the positional parameters and the special parameter # are restored to the values they had prior to the function's execution.
* If a numeric argument is given to return, that status is returned. 

### Return: set a global variable with the result

```
function myfunc()
{
    myresult='some value'
}

myfunc
echo $myresult 
```

but as we all know, using global variables, particularly in large programs, can lead to difficult to find bugs.

### Return: use command substitution

A better approach is to use local variables in your functions. The problem then becomes how do you get the result to the caller. One mechanism is to use command substitution:

```
function myfunc()
{
    local  myresult='some value'
    echo "$myresult"
}

result=$(myfunc)   # or result=`myfunc`
echo $result
```

Here the result is output to the stdout and the caller uses command substitution to capture the value in a variable. The variable can then be used as needed.

### Return: can pass in the name of a variable to use as the result variable

The other way to return a value is to write your function so that it accepts a variable name as part of its command line and then set that variable to the result of the function:

```
function myfunc()
{
    local  __resultvar=$1
    local  myresult='some value'
    eval $__resultvar="'$myresult'"
}

myfunc result
echo $result
```

When you store the name of the variable passed on the command line, make sure you store it in a local variable with a name that won't be (unlikely to be) used by the caller (which is why I used `__resultvar` rather than just resultvar). If you don't, and the caller happens to choose the same name for their result variable as you use for storing the name, the result variable will not get set. For example, the following does not work:

```
function myfunc()
{
    local  result=$1
    local  myresult='some value'
    eval $result="'$myresult'"
}

myfunc result
echo $result
```

Since we have the name of the variable to set stored in a variable, we can't set the variable directly, we have to use eval to actually do the setting. The eval statement basically tells bash to interpret the line twice, the first interpretation above results in the string result='some value' which is then interpreted once more and ends up setting the caller's variable.

The reason it doesn't work is because when eval does the second interpretation and evaluates result='some value', result is now a local variable in the function, and so it gets set rather than setting the caller's result variable.

For more flexibility, you may want to write your functions so that they combine both result variables and command substitution:

```
function myfunc()
{
    local  __resultvar=$1
    local  myresult='some value'
    if [[ "$__resultvar" ]]; then
        eval $__resultvar="'$myresult'"
    else
        echo "$myresult"
    fi
}

myfunc result
echo $result
result2=$(myfunc)
echo $result2
```

Here, if no variable name is passed to the function, the value is output to the standard output.

## Functions and variable scope

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

# Regular Expression

Ref: http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_04_01.html

Certain commands and utilities commonly used in scripts interpret and use REs, such as:

* grep
* expr
* sed
* awk
* As of version 3, Bash has acquired its own RE-match operator: `=~` .

Operators:

* `.`	Matches any single character.
* `?`	The preceding item is optional and will be matched, at most, once.
* `*`	The preceding item will be matched zero or more times.
* `+`	The preceding item will be matched one or more times.
* `{N}`	The preceding item is matched exactly N times.
* `{N,}`	The preceding item is matched N or more times.
* `{N,M}`	The preceding item is matched at least N times, but not more than M times.
* `-`	represents the range if it's not first or last in a list or the ending point of a range in a list.
* `^`	Matches the empty string at the beginning of a line; also represents the characters not in the range of a list.
* `$`	Matches the empty string at the end of a line.
* `\b`	Matches the empty string at the edge of a word.
* `\B`	Matches the empty string provided it's not at the edge of a word.
* `\<`	Match the empty string at the beginning of word.
* `\>`	Match the empty string at the end of word.

REF: http://www.zytrax.com/tech/web/regex.htm

## Bash =~ Example

In addition to doing simple matching, bash regular expressions support sub-patterns surrounded by parenthesis for capturing parts of the match. The matches are assigned to an array variable `BASH_REMATCH`.

The entire match is assigned to `BASH_REMATCH[0]`, the first sub-pattern is assigned to `BASH_REMATCH[1]`, etc..

TODO: http://www.linuxjournal.com/content/bash-regular-expressions




```
#!/bin/bash

variable="This is a fine mess."

echo "$variable"

# Regex matching with =~ operator within [[ double brackets ]].
if [[ "$variable" =~ T.........fin*es* ]]
# NOTE: As of version 3.2 of Bash, expression to match no longer quoted.
then
  echo "match found"
      # match found
fi
```


## Grep Examples

```
grep root /etc/passwd
root:x:0:0:root:/root:/bin/bash
operator:x:11:0:operator:/root:/sbin/nologin
```

we now exclusively want to display lines starting with the string "root":

```
cathy ~> grep ^root /etc/passwd
root:x:0:0:root:/root:/bin/bash
```

If we want to see which accounts have no shell assigned whatsoever, we search for lines ending in ":":

```
cathy ~> grep :$ /etc/passwd
news:x:9:13:news:/var/spool/news:
```

To check that PATH is exported in ~/.bashrc, first select "export" lines and then search for lines starting with the string "PATH", so as not to display MANPATH and other possible paths:


```
cathy ~> grep export ~/.bashrc | grep '\<PATH'
  export PATH="/bin:/usr/lib/mh:/lib:/usr/bin:/usr/local/bin:/usr/ucb:/usr/dbin:$PATH"
```

Similarly, \> matches the end of a word.

If you want to find a string that is a separate word (enclosed by spaces), it is better use the -w, as in this example where we are displaying information for the root partition:

```
cathy ~> grep -w / /etc/fstab
LABEL=/                 /                       ext3    defaults        1 1
```

If this option is not used, all the lines from the file system table will be displayed.



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

# Bash Patterns and best practices

http://stackoverflow.com/questions/78497/design-patterns-or-best-practices-for-shell-scripts

## Bash Package Manager

http://www.bpkg.io/

# Conditional: if then else

* Basic intro:
  * http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-6.html
  * http://tldp.org/LDP/abs/html/testconstructs.html#EX11 
* string and file operators `help test`

An if/then construct tests whether the exit status of a list of commands is 0 (since 0 means "success" by UNIX convention), and if so, executes one or more commands.


~~~bash
if [ "foo" = "foo" ]; then
   echo expression evaluated as true
else
   echo expression evaluated as false
fi
~~~


To represent multiple conditions: https://stackoverflow.com/questions/3826425/how-to-represent-multiple-conditions-in-a-shell-if-statement

The 'portable shell' guidelines for the autoconf tool or related packages, this notation — using '||' and '&&' — is what they recommend.

```
if [ "$g" -eq 1 ] && [ "$c" = "123" ]
then echo abc
elif [ "$g" -eq 2 ] && [ "$c" = "456" ]
then echo abc
else echo efg
fi
```

NOTE: enclosed the references to $g in double quotes; that's good practice, in general.

## Is test or [ or [[ more portable both between bash shells and between other shells?

Ref: http://mywiki.wooledge.org/BashFAQ/031

https://unix.stackexchange.com/questions/168255/is-test-or-or-more-portable-both-between-bash-shells-and-between-other-shel

For portability between [ and [[ use [ only.

## Command exit code conventions

Ususally when a command finish the execution without errors the exit code is 0, otherwise it is an error code.


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

## eval

Ref: http://wiki.bash-hackers.org/commands/builtin/eval

syntax `eval [arg ...]`

eval takes its arguments, concatenates them separated by spaces, and executes the resulting string as Bash code in the current execution environment.

*it's similar to `-c "bash code…"` from a script,
* **except** in the case of eval, the given code is executed in the current shell environment rather than a child process.



## exec

### Use exec to redirect outputs from within a script

REF: http://stackoverflow.com/questions/8888251/understanding-bash-exec-12-command

Example:

```
function example()
{
    exec 1>&2  # from this point one stdout will be directed to stderr
    cat <<EOT
Script requires at least one parameter.
EOT
    exit 1
} 
```

## set

Ref:

* `man set`  https://www.gnu.org/software/bash/manual/bashref.html#index-set
* http://unix.stackexchange.com/questions/255581/what-does-set-command-without-arguments-do
* http://faculty.salina.k-state.edu/tim/unix_sg/bash/set.html
* Bash options: http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_06.html

`set` allows you:

* to change the values of shell options
  * Use - (dash) for enabling an option, + for disabling
  * `set -o noclobber`
  * `set +o noclobber`
* set the positional parameters
* to display the names and values of shell variables (Without arguments, set will print all shell variables (both environment variables and variables in current session) sorted in current locale).


* Without options, the name and value of each shell variable are displayed in a format that can be reused as input.

* `set -e` : Exit immediately if a command exits with a non-zero status.
* `set -o pipefail` : the return value of a pipeline is the status of the last command to exit with a non-zero status, or zero if no command exited with a non-zero status

* `set -- ` If no arguments follow this option, then the positional parameters are unset
* `set -- one two three`  set positional params $1 $2 $3 

## read

http://wiki.bash-hackers.org/commands/builtin/read
http://tldp.org/LDP/abs/html/x17837.html


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

## How to handle paramenter when you write command wrapper 

If you want to 

Ref:

* https://stackoverflow.com/questions/29378566/i-just-assigned-a-variable-but-echo-variable-shows-something-else
* https://stackoverflow.com/questions/29378566/i-just-assigned-a-variable-but-echo-variable-shows-something-else
* 


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


# Examples

## asdf

https://github.com/asdf-vm/asdf

Extendable version manager with support for Ruby, Node.js, Elixir, Erlang & more.

Use Bats for bash testing.

## NVM

https://github.com/creationix/nvm

Parameter parsing

```
      local nobinary
      nobinary=0
      local LTS
      while [ $# -ne 0 ]
      do
        case "$1" in
          -s)
            shift # consume "-s"
            nobinary=1
          ;;
          -j)
            shift # consume "-j"
            nvm_get_make_jobs "$1"
            shift # consume job count
          ;;
          --lts)
            LTS='*'
            shift
          ;;
          --lts=*)
            LTS="${1##--lts=}"
            shift
          ;;
          *)
            break # stop parsing args
          ;;
        esac
      done

```

## Common mistakes

http://wiki.bash-hackers.org/scripting/newbie_traps

Quoting errors: http://wiki.bash-hackers.org/scripting/newbie_traps#expanding_using_variables
