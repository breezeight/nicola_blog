---
layout: post
title: "Vim"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["vim"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# References



# Window, Buffer, Tab

Refs:

* http://vim.wikia.com/wiki/Vim_buffer_FAQ
* `:help windows.txt`
* `:help buffers` 

Definitions:

* A buffer is the in-memory text of a file.
* A window is a viewport on a buffer.
* A tab page is a collection of windows.

Vim buffers are identified using one of these:

* `The name of the buffer`:  is the name of the file associated with that buffer.
* `The buffer number`:  is a unique sequential number assigned by Vim. This buffer number will not change in a single Vim session.


# Mapping command to keys

http://vim.wikia.com/wiki/Mapping_keys_in_Vim_-_Tutorial_%28Part_1%29



# let set

`:set` is for setting options.

`:let` for assigning a value to a variable.

Reference: http://vim.wikia.com/wiki/Displaying_the_current_Vim_environment


## Print the option value

`:set options_name?`

NOTE: Vim toggle options (booleans, options that are on/off), like
autoindent, are `prefixed with no` to indicate that they're turned off

To see where the option was last set: `:verbose set textwidth?` 



Examples: `:set textwidth?`

## Toggle boolean options

Vim toggle options (booleans, options that are on/off), like autoindent, are prefixed with no to indicate that they're turned off, so the result of :set autoindent will be autoindent or noautoindent.

To Toggle options:

* `:set options_name!` inverts the option. `options_name` becomes `options_name`.


## Revert to default

`:set optiont&`


## Set number or string options

`:set option=value`
