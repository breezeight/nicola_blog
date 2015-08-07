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

# Command line utilities

## JQ to filter JSON

Ref:

* http://stedolan.github.io/jq/manual/#ConditionalsandComparisons
* https://github.com/stedolan/jq/wiki/Cookbook#filter-objects-based-on-the-contents-of-a-key
