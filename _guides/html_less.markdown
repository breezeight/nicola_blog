---
layout: post
title: "CSS: Less"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: [ "html", "css"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# References:

* http://lesscss.org/
* [Guide to the language](http://lesscss.org/features/)
* [Function Reference](http://lesscss.org/functions/)

# Less Compiler from command line

~~~
npm install less -g
lessc my_file.less
~~~

# Cheatsheet

## Nested rules

[Bootstrap Doc](http://lesscss.org/features/#features-overview-feature-nested-rules)

* The basic usage of nested rules is to easily compile `descendant CSS selector`.
* Basically the container selector is appended to each nested selector

Example:

~~~
.header {
  color: black;
  .navigation {
    font-size: 12px;
  }
  .logo {
    width: 300px;
  }
}
~~~

compiles to

~~~
.header {
  color: black;
}
.header .navigation {
  font-size: 12px;
}
.header .logo {
  width: 300px;
}
~~~

In the next paragraph we will see how we can modify this default behavior with the **parent selector** `&`

### Single Parent Selector &

* `&` is a parent selector
* [Bootstrap doc](http://lesscss.org/features/#parent-selectors-feature)
* [LESS: Secrets of the Ampersand](http://blog.slaks.net/2013-09-29/less-css-secrets-of-the-ampersand/)

* If you use a **single** `&` in a nested selector it will be replaced by the parent selector at compile time.
* `&` can be insered in any position of the selector ex: `.highlight & .navigation`, [see doc](http://lesscss.org/features/#parent-selectors-feature-changing-selector-order)


You can think that in the previous paragraph the `&` was implicit, the example below produce the same result with or without `&`: 

~~~
.header {
  color: black;
  & .navigation {
    font-size: 12px;
  }
  & .logo {
    width: 300px;
  }
}
~~~

But if you want to compile into a pseudo selector you must use `&`

~~~
a {
  color: blue;
  &:hover {
    color: green;
  }
}
~~~

compiles to:

~~~
a {
  color: blue;
}

a:hover {
  color: green;
}
~~~

### Multiple nesting

`&` represents **all parent selectors** (not just the nearest ancestor) so the following example:

~~~
.nav {
  list-style: none;

  > li {
    position: relative;
    display: block;

    > a {
      position: relative;
      display: block;
      &:hover,
      &:focus {
        text-decoration: none;
      }
    }

    // Disabled state sets text to gray and nukes hover/tab effects
    &.disabled > a {
      color: #FFFFFF;

      &:hover,
      &:focus {
        text-decoration: none;
        background-color: transparent;
      }
    }
  }
}
~~~

will compile to:

~~~
.nav {
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
}
.nav > li.disabled > a {
  color: #FFFFFF;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
}
~~~


### Multiple Parent Selector &

If you use multiple `&` within a single selector different rules applies, see here: 

* []http://lesscss.org/features/#parent-selectors-feature
* http://blog.slaks.net/2013-09-29/less-css-secrets-of-the-ampersand/


## Extend

### Intro

With extends I can say that one class wants to have the properties of another.

E.g. I write the following code:

~~~
.button {
  background: white;
  display: block;
  width: 120px;
}
.blue-button {
  &:extend(.button);
  background: blue;
}
~~~

It compiles to:

~~~
.button, .blue-button {
  background: white;
  display: block;
  width: 120px;
}
.blue-button {
  background: blue;
}
~~~

Notice how the extend has copied the selector it is on, into the selector for `.button`, so the `.blue-button` class definition is compiled in two rule. The comma combined seletor is used to apply the rule set of `.button` also to `.blue-button`.


The extend is either:

 * attached to a selector or 
 * placed into a ruleset.

Placing extend into a body is a shortcut for placing it into **every**  single selector of that ruleset.

### Syntax

This the the full [documentation](http://lesscss.org/features/#extend-feature), but the most common syntax are: 

* The basic selector syntax is `.e:extend(.f)`  which means the class `.e` extend `.f`



* into a ruleset: `&:extend(div pre);`: extends every single selector of that ruleset.



* Extend "all" syntax [doc](http://lesscss.org/features/#extend-feature-extend-all-): it tells Less to match that selector as part of another selector. The selector will be copied and the matched part of the selector only will then be replaced with the extend, making a new selector.


### Use case : bootstrap


Bootstrap makes an heavy use of extend with the clearfix hack

~~~
~/tmp/bootstrap/less (master)$ grep -r extend * 
button-groups.less:  &:extend(.clearfix all);
button-groups.less:.btn-group-xs > .btn { &:extend(.btn-xs); }
button-groups.less:.btn-group-sm > .btn { &:extend(.btn-sm); }
button-groups.less:.btn-group-lg > .btn { &:extend(.btn-lg); }
button-groups.less:    &:extend(.clearfix all);
carousel.less:      &:extend(.img-responsive);
mixins/grid.less:  &:extend(.clearfix all);
mixins/grid.less:  &:extend(.clearfix all);
modals.less:  &:extend(.clearfix all); // clear it in case folks use .pull-* classes on buttons
navbar.less:  &:extend(.clearfix all);
navbar.less:  &:extend(.clearfix all);
navbar.less:  &:extend(.clearfix all);
navs.less:  &:extend(.clearfix all);
pager.less:  &:extend(.clearfix all);
panels.less:  &:extend(.clearfix all);
thumbnails.less:    &:extend(.img-responsive);
type.less:    &:extend(.clearfix all); // Clear the floated `dt` if an empty `dd` is present
~~~



## Mixin

## Extend VS Mixin

http://transmission.vehikl.com/less-extend/

## Namespace

~~~
.bundle {
  .button {
~~~

~~~
.header a {
  color: orange;
  .bundle > .button;
}
~~~

# Intro

Less is a CSS pre-processor, meaning that it extends the CSS language, adding features that allow variables, mixins, functions and many other techniques that allow you to make CSS that is more maintainable, themable and extendable.

# Command line

* `npm install -g less`
* `lessc styles.less > styles.css`


