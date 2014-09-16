---
layout: post
title: "Javascript"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["javascript"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}




References:
[SOJS] /Volumes/ArchiveDisk/Archive/Misc/ebook/javascript/Secrets_of_the_JavaS.pdf    http://www.manning.com/resig/


TODO
typeof -> how does it works?


BASIC CONCEPTS
Functions
Function, not objects are at the core of JavaScript
JS is Functional language, functions are first-class objects


Anonymous functions:
function(){return "test"}


Functions can be arguments of other functions.



All Functions have the "name" property, if it's anonymous name is an empty string.
Functions can be referenced by variables (var canFly = function(){ return true; }; )
A Function can be invoked through a variable that reference the function (var canFly = function(){ return true; }; canFly() )


To Declare functions: see [SOJS] pag 40



Scope:
named global functions are property of the window object


http://www.smashingmagazine.com/2009/08/01/what-you-need-to-know-about-javascript-scope/


Event Loop: it's executed by the browser.
Browser event loop processing is single thread (events processed in FIFO order) but the mechanism that manage events before their handlers are executed are not on the same thread








Window Object
http://www.w3schools.com/js/js_window.asp

The window object is supported by all browsers. It represent the browser's window.

All global JavaScript objects, functions, and variables automatically become members of the window object.
Global variables are properties of the window object.
Global functions are methods of the window object.
Even the document object (of the HTML DOM) is a property of the window object:

window.document.getElementById("header");
is the same as:
document.getElementById("header");
