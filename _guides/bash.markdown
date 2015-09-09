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

Bash on Evernote: https://www.evernote.com/shard/s106/nl/11497273/917f4214-9719-438b-b9ea-6a58f43e968f/

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

# Array

http://mywiki.wooledge.org/BashGuide/Arrays

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

# Bash built in commands

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

# Parsing bash script options from command line 

* http://sookocheff.com/post/bash/parsing-bash-script-arguments-with-shopts/
* http://dustymabe.com/2013/05/17/easy-getopt-for-a-bash-script/


## GETOPTS

* `help getopts`
* `getopts` tutorial: http://wiki.bash-hackers.org/howto/getopts_tutorial

Getopts is used by shell procedures to parse positional parameters as options.

Syntax: `getopts: getopts optstring name [arg]`

* OPTSTRING contains the option letters to be recognized; if a letter is followed by a colon, the option is expected to have an argument, which should be separated from it by white space.
* Each time it is invoked, getopts will place the next option in the shell variable $name, initializing name if it does not exist, and the index of the next argument to be processed into the shell variable OPTIND.
* When an option requires an argument, getopts places that argument into the shell variable OPTARG.

BEST PRACTICE: The common way is that the processing of all arguments precedes the actual job of the program/script. 


# Command line utilities

## JQ to filter JSON

Ref:

* http://stedolan.github.io/jq/manual/#ConditionalsandComparisons
* https://github.com/stedolan/jq/wiki/Cookbook#filter-objects-based-on-the-contents-of-a-key
