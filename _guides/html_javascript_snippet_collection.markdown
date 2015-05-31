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

# YouTube Video Modal

http://fancyapps.com/fancybox/ Used by:

* landing page Kenwood

# Responsive Carousel

http://kenwheeler.github.io/slick/ Used by:

* landing page Kenwood



# Vertically allign

## 

REF: See the checked answer here http://stackoverflow.com/questions/17818976/text-vertically-and-horizontally-centered-over-a-responsive-image

This jsfiddle uses 


## Using CSS3 translate

REF: http://zerosixthree.se/vertical-align-anything-with-just-3-lines-of-css/

The idea here is to move the top at 50% of the container and then Translating the elements along the Y axis 50% will move it down 50% of its own height,

~~~
.slider-copy {
  position: absolute;
  top: 50%;
  -webkit-transform: translateY(-50%);
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
}
~~~

or

~~~
@mixin vertical-align {
  position: relative;
  top: 50%;
  -webkit-transform: translateY(-50%);
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
}
~~~
