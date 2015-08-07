---
layout: post
title: "Html CSS"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["javascript", "html", "css"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# References:

* [HTML Mozilla Reference](https://developer.mozilla.org/en/docs/Web/HTML/Element)

# TODO

html tags:

* button

html attributes:

* data-toggle
* role

bootstrap classes:

# Html

* `HTML` HyperText Markup Language, gives content structure and meaning by defining that content as, for example, headings, paragraphs, or images.
* `CSS` or Cascading Style Sheets, is a presentation language created to style the appearance of content—using, for example, fonts or colors.

The two languages—HTML and CSS—are independent of one another and should remain that way.

## Basic Html Intro

http://learn.shayhowe.com/html-css/building-your-first-web-page/

* tags
* attributes
* `<!DOCTYPE html>`, `<html>`, `<head>`, `<meta>` and `<body>`
* [semantic of html5 tags](http://learn.shayhowe.com/html-css/getting-to-know-html/): header, nav, article, ....
* Links (href): http://learn.shayhowe.com/html-css/getting-to-know-html/

### By Browser default element property

It's different for each browser, so:

* Firefox (Gecko): http://mxr.mozilla.org/mozilla-central/source/layout/style/html.css. Or, browse to resource://gre-resources/ and look at html.css.
* Chrome/Safari (WebKit): http://trac.webkit.org/browser/trunk/Source/WebCore/css/html.css
* Internet Explorer (Trident), all versions: http://www.iecss.com/

A lot of frameworks use a reset css that try to fix inconsistencies

REF: http://stackoverflow.com/questions/6867254/browsers-default-css-for-html-elements

## ARIA attributes

https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA

Accessible Rich Internet Applications (ARIA) defines ways to make Web content and Web applications (especially those developed with Ajax and JavaScript) more accessible to people with disabilities.

# CSS

* CSS Basic syntax https://developer.mozilla.org/en-US/docs/CSS/Syntax
  * [Intro guide](http://learn.shayhowe.com/html-css/building-your-first-web-page/): properties, selectors (type, class, id....)
* Glossary: http://webdesign.about.com/od/cssglossary/CSS_Glossary.htm


References:

* [w3school CSS properties](http://www.w3schools.com/cssref/default.asp)
* [w3schools CSS selector](http://www.w3schools.com/cssref/css_selectors.asp)

## Cascade

http://learn.shayhowe.com/html-css/getting-to-know-css/#cascade

Within CSS, all styles cascade from the top of a style sheet to the bottom, allowing different styles to be added or overwritten as the style sheet progresses.

## Selectors

Html example for basic selector types `<p class="key" id="principal">`:

* tag selector `p {}`: select all p elements
* multi tag selecto `div, p {}` : Selects all div and p elements
* id selector `#principal {}`
* pseudo class selector: `selector:pseudo-class`
* class selector `.key {}`: any element with `key` class
* `.class1.class2` matches any element with both classes, ex: `<div class="class1 class2">...</div>` 
* ... 

Attributes selectors:

* `[attribute]` Selects all elements with the specified attribute
* `[attribute=value]` Selects all elements where the specified attribute is equal to value
* `[attribute*=value]` matches every element whose attribute value containing a specified value.
  * ex: Set a background color on all elements that have a class attribute value containing "test": `[class*="test"] { background: #ffff00; }` 
* ...

Selector based on relationships:

* `A E` : Any E element that is a descendant of an A element (that is: a child, or a child of a child, etc.)
* `A, E` : will apply to any element that matches either of the selectors, each selector is separated by comma `,`
* `A > E` : Any E element that is a child of an A element
* `E:first-child` : Any E element that is the first child of its parent
* `A + E` : Any E element that is the next sibling of a A element (that is: the next child of the same parent)
* ....


* more selector : http://www.cheetyr.com/css-selectors


relationship rules:

* When selectors are combined they should be read from right to left.
* `key selector` : The selector farthest to the right, directly before the opening curly bracket, is known as the `key selector`.
  * The key selector identifies exactly which element the styles will be applied to.
  * Any selector to the left of the key selector will serve as a prequalifier.
 

Spaces Within Selectors:

* The use, and omission, of spaces makes a large difference in selectors.
* best practice is to not prefix a class selector with a type selector.

More about selectors:

* http://www.cheetyr.com/css-selectors
* https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Getting_started/Selectors
* [Combining selectors](http://learn.shayhowe.com/html-css/getting-to-know-css/#combining-selectors)
* [w3schools CSS selector](http://www.w3schools.com/cssref/css_selectors.asp)

### Selector Specificity (or selector weight)

* https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity
* http://stackoverflow.com/questions/12743458/efficient-algorithm-to-compare-specificity-of-css-rules
* http://css-tricks.com/specifics-on-css-specificity/

The following list of selectors is by **decreasing specificity** :

* Inline style
* ID selectors
* Class selectors, Attributes selectors, Pseudo-classes
* Type selectors

Use the calculator to test: [Specifity Calculator](http://specificity.keegan.st/)

Specificity Within Combined Selectors:

* When selectors are combined, so are the specificity weights of the individual selectors. 
* Example `.hotdog p`
  * `.hotdog` has specificity `0-0-1-0`
  * `p` has specificity `0-0-0-1`
  * total combined point value would be `0-0-1-1`

Example, for `ul#nav li.active a` the points are `0-1-1-3`:

0 - Not a style attribute.
1 - 1 ID found.
1 - 1 Classname found.
3 - 3 type found.

Comparison algorithm:

* Go from **left to right** on the ranks.
* Compare the ranks on both selectors.
* The rank with the higher amount of point, wins.
* If the ranks are equal, continue right to the next (less specific) rank.
* If all ranks are equal, the one which comes later in the CSS document, wins.

### The !important bad practice

When an !important rule is used on a style declaration, this declaration overrides any other declaration made in the CSS, wherever it is in the declaration list. Although, !important has nothing to do with specificity.  Using !important is bad practice because it makes debugging hard since you break the natural cascading in your stylesheets.

https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity#The_!important_exception

### Selector examples

* `.container div` Select any div element that is a child of any element with a class name of "container" [exmaple](https://css-tricks.com/whats-the-difference/)

* `div.container` Select any div element that has a class name of "container" [exmaple](https://css-tricks.com/whats-the-difference/)


## Replaced and non replaced elements 

* https://developer.mozilla.org/en-US/docs/Web/CSS/Replaced_element
* http://stackoverflow.com/questions/12468176/what-is-a-non-replaced-inline-element

Most elements in CSS are `non-replaced`. A non-replaced element is simply an element that is not a replaced element.

A `replaced element` is an element whose representation is outside the scope of CSS. These are kind of external objects whose representation is independent of the CSS.

Typical replaced elements are:

* `<img>`
* `<object>`
* `<video>`
* `<textarea>`
* `<input>`

Some elements, like <audio> or <canvas> are replaced elements only in specific cases. Objects inserted using the CSS content properties are anonymous replaced elements.

CSS handles replaced elements specifically in some cases, like when calculating margins and some auto values.

Note that some replaced elements, but not all, have intrinsic dimensions or a defined baseline, which is used by some CSS properties like vertical-align.

## CSS Visual Formatting Model

Ref:

* [W3C CSS 2.1](http://www.w3.org/TR/2011/REC-CSS2-20110607/visuren.html)
* [W3C CSS 3](CSS level 3) **TODO** rileggerlo bene 
  * This module describes the basic types of boxes, with their padding and margin, and the normal “flow” (i.e., the sequence of blocks of text with margins in-between).
  * It also defines “floating” boxes, but other kinds of layout, such as tables, absolute positioning, ruby annotations, grid layouts, columns and numbered pages, are described by other modules.
  * Also, the layout of text inside each line (including the handling of left-to-right and right-to-left scripts) is defined elsewhere.
* [MDN](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Visual_formatting_model)


The **CSS visual formatting model** is the algorithm used to process a document and display it on a visual media.

In the visual formatting model, each element in the document tree generates zero or more boxes according to the box model. The layout of these boxes is governed by:

* its box dimensions: precisely defined or constrained, or not;
* its box type: an inline, inline-level, atomic inline-level, block box;
* the positioning scheme: in the normal flow, a float or absolute positioning;
* the other elements in the tree: its children and neighbours;
* the viewport size and position;
* intrinsic dimensions of contained images;
* other external information.

A box is rendered relatively to the edge of its containing block. Usually a box establishes the containing block for its descendants. Note that a box is not constrained by its containing block; when its layout goes outside it, it is said to `overflow`.



### Box Model

Refs: 

* http://learn.shayhowe.com/html-css/box-model
* https://developer.mozilla.org/en-US/docs/CSS/box_model

According to the box model concept:

* **every element** on a page is a rectangular box
* and may have width, height, padding, borders, and margins.

Box generation is the part of the CSS visual formatting model that creates boxes from the document's elements. Generated boxes are of different types, which will affect how the visual formatting is done.

The `type of the box` generated depends of the value of the `display` CSS property.


`Total width and height` of an element can be calculated using the following formula: 

* `margin-right + border-right + padding-right + width + padding-left + border-left + margin-left`
* `margin-top + border-top + padding-top + height + padding-bottom + border-bottom + margin-bottom`

Example:

![box-model.png]({{ site.url }}/guides/images/html_box_model.jpg)

Using the formulas, we can find the total height and width of our example code.

Width: 492px = 20px + 6px + 20px + 400px + 20px + 6px + 20px
Height: 192px = 20px + 6px + 20px + 100px + 20px + 6px + 20px


The [Normal Flow](http://webdesign.about.com/od/cssglossary/g/bldefnormalflow.htm) is the way that elements are displayed in a web page with super basic html:

* `block boxes` : occupy any available width, regardless of their content, and begin on a new line, placed one below the other.
* `inline boxes` : are laid out on the page horizontally, one after the other beginning at the top of the container element. Occupy only the width their content requires and line up on the same line, one after the other

`display` property:

* determines how elements are displayed.
*  Every element has a default display property value.
*  There are quite a few values for the display property, but the most common are
  *  `block`: This value causes an element to generate a block box.
  *  `inline`: This value causes an element to generate one or more inline boxes.
  *  `inline-block`: This value causes an element to generate an inline-level block container. The inside of an inline-block is formatted as a block box, and the element itself is formatted as an atomic inline-level box.
  *  `none` : hide an element and render the page as if that element doesn’t exist.  Descendant elements do not generate any boxes either; the element and its content are removed from the formatting structure entirely. This behavior cannot be overridden by setting the 'display' property on the descendants.
  *  `list-item`: This value causes an element (e.g., LI in HTML) to generate a principal block box and a marker box.
  *  `table, inline-table, table-row-group, table-column, table-column-group, table-header-group, table-footer-group, table-row, table-cell, and table-caption`: These values cause an element to behave like a table element

### Controlling box generation

Ref: http://www.w3.org/TR/CSS2/visuren.html#block-boxes

Box's type affects its behavior in the visual formatting model.

The `display` property specifies a box's type.

The following values of the 'display' property make an element block-level:

* `block`
* `list-item` 
* `table`

`Block-level boxes` are boxes that participate in a block formatting context.

Each block-level element generates:

* a `principal block-level box` that contains descendant boxes and generated content and is also the box involved in any positioning scheme. 
* may generate additional boxes in addition to the principal box: 'list-item' elements. These additional boxes are placed with respect to the principal box.

a `Block formatting context`:

* is a part of a visual CSS rendering of a Web page.
* It is the region in which the layout of block boxes occurs and in which floats interact with each other.
* https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Block_formatting_context

* Except for table boxes, which are described in a later chapter, and replaced elements, a block-level box is also a block container box.
* Not all block container boxes are block-level boxes: non-replaced inline blocks and non-replaced table cells are block containers but not block-level boxes
* Block-level boxes that are also block containers are called block boxes.

a `Block container box`:

* contains only block-level boxes 
* or establishes an inline formatting context and thus contains only inline-level boxes.

~~~html
<DIV>
  Some text
  <P>More text</P>
</DIV>
~~~

![html_block_boxes.png]({{ site.url }}/guides/images/html_block_boxes.png)

This diagram illustrates how anonymous block boxes may spring into existence around anonymous content.

It shows two rectangular boxes that contain text, the first being anonymous. It has a light grey background and contains the words "Some text". Just below it is a P box with a dark grey background that contains the words "More text". The boxes are both within a DIV box.

`Inline-level elements` are:

* those elements of the source document that do not form new blocks of content;
* the content is distributed in lines.
* Inline-level elements generate inline-level boxes

The following values of the 'display' property make an element inline-level:

* `inline`
* `inline-table`
* `inline-block`

`Inline-level boxes` are boxes that participate in an inline formatting context.

`atomic inline-level boxes`: Inline-level boxes that do not participate in an inline formatting context 

`Line boxes` is one that is both:

* inline-level 
* and whose contents participate in its containing inline formatting context

A non-replaced element with a 'display' value of 'inline' generates an inline box. Inline-level boxes that are not inline boxes (such as replaced inline-level elements, inline-block elements, and inline-table elements) are called atomic inline-level boxes because they participate in their inline formatting context as a single opaque box.

`anonymous inline element` :

* Any text that is directly contained inside a block container element (not inside an inline element) is an anonymous inline element
* inherit inheritable properties from their block parent box.

In a document with HTML markup like this:

~~~html
<p>Some <em>emphasized</em> text</p>
~~~

the `<p>` generates a block box, with several inline boxes inside it. The box for "emphasized" is an inline box generated by an inline element (`<em>`), but the other boxes ("Some" and "text") are inline boxes generated by a block-level element (`<p>`). The latter are called anonymous inline boxes, because they do not have an associated inline-level element.

Summary:

* Inline-level elements
* Inline-level boxes
* Inline formatting context
* Anonymous block boxes
* Block-level elements
* Block-level boxes
* Block formatting context
* Anonymous block boxes


### Viewport

http://www.w3.org/TR/2011/REC-CSS2-20110607/visuren.html#viewport

### FAQ

#### What Does “width: 100%” Do in CSS?

http://www.impressivewebs.com/width-100-percent-css/

* First Things First: Blocks Don’t Need 100% Width, block element (such as a <div>, <p>, or <ul>, to name a few) will, by default expand to fit the width of its containing, or parent, element (minus any margins it has or padding its parent has).
* In 99% of cases, applying width: 100% to a block level element is either unnecessary or will bring undesirable results.

#### What is the difference between width 100% and width inherit

http://stackoverflow.com/questions/9374509/100-vs-inherit

Inherit copies the literal expression rather than the value.




### Positioning

* https://developer.mozilla.org/en-US/docs/Web/CSS/position

Once boxes are generated, the CSS engine needs to position them on the layout. In order to do that, it will use one of the following algorithm: normal, float, absolute

The `normal flow` in which it will lay each box one after the other:

* In a block formatting context, they are laid out vertically
* in an inline formatting context, they are laid out horizontally
* The normal flow is triggered when the CSS position is set to the value `static` or `relative`, and if the CSS `float` is set to the value `none`.
* when position is `static` (default): A static positioned element is always positioned according to the normal flow of the page.
* when position is `relative`: positioned relative to its normal position (normal flow). The boxes are drawn with an offset defined by the top, bottom, left and right CSS properties.


The `floats algorithm` which will extract the box from the normal flow and put it to the side of the containing box.

The `absolute positioning` scheme in which a box is absolutely positioned within a coordinate system established by its containing element. An absolutely positioned element can cover other elements. The `position` property has one of these value:

* `fixed`: is positioned relative to the browser window, and will not move even if the window is scrolled.
* `absolute`: boxes are entirely removed from the flow and don't interact with it at all. They are positioned relative to their containing block using the top, bottom, left and right CSS properties.

Note: Elements that are positioned relatively are still considered to be in the normal flow of elements in the document. In contrast, an element that is positioned absolutely is taken out of the flow and thus takes up no space when placing other elements.

Overlapping Elements: `z-index: -1;`
Note: If two positioned elements overlap without a z-index specified, the element positioned last in the HTML code will be shown on top.

### CSS Float

* [W3C float definition](http://www.w3.org/TR/CSS2/visuren.html#floats)
* http://alistapart.com/article/css-floats-101
* http://www.w3schools.com/css/css_float.asp
* http://www.smashingmagazine.com/2007/05/01/css-float-theory-things-you-should-know/
* NICE ARTICLE with practical usecases: http://designshack.net/articles/css/everything-you-never-knew-about-css-floats/
* Another nice article with a lot of examples: http://www.richinstyle.com/proposals/floatproposal.html

~~~
.sidebar {
  float: right;			
}
~~~

Why does floats exists? 
Floats are used to create the appearance of elements flowing around one another. They can be used in three main ways:

* To create effects with text flowing around content; e.g., drop caps.
* To ensure that inline text is aligned with the left or right of its block.
* To have block elements side-by-side; e.g., to achieve column effects.

What is a float?

* A float is a box that is shifted to the left or right on the current line.
* The most interesting characteristic of a float (or “floated” or “floating” box) is that content may flow along its side (or be prohibited from doing so by the “clear” property).
* Content flows down the right side of a left-floated box and down the left side of a right-floated box.
* The basic principle of floats is that they are withdrawn from the normal flow of the document, and do not affect the position of subsequent block elements.
* However, inline elements, including line boxes, do take the position of floats into account - they flow around them (text for example).
* As a result, although floats overlap with block elements, they do not overlap with their inline content - it is displaced to one side.
* In addition, although block elements do not take into account previous floats, floats themselves do take into account previous block elements, as well as the horizontal (but not vertical position) of previous floats.
* In addition, floats are moved as far to the left (if float: left) or right (if float: right) as possible; and when floats were originally inline, they are aligned with the top of the line box from which they were displaced.

Elements are floated horizontally, this means that an element can only be floated left or right, not up or down.

In a nutshell floats can be summarized thus:

* floating an element causes subsequent non-floating block elements to overlap with it, with their inline content flowing around the float, and
* floating an element causes subsequent floating elements to flow next to the float.

The `float property` has four values that we can apply to it: 

* `left` : the element will move to the left-most boundary of its parent element
* `right` :  the element will move to the right-most boundary of its parent element
* `inherit` : tells an element to inherit the float value of its parent element.
* `none` (default) : is the default value and tells an element not to float at all.

In other words:

* floated elements go from stacking on top of each other to sitting next to each other
* given that there is enough room in the parent element for each floated element to sit.

What is the parent element? It is the box from which the float were displaced

Example:

~~~html
<body>
  <div id="pink" class="block pink"></div>
  <div id="container">
    <div id="blue" class="block blue"></div>
  </div>
</body>
~~~

~~~
document.getElementById("pink").parentNode
=> body

document.getElementById("blue").parentNode
=> div id="container"
~~~

#### Float rules for humans

Ref: http://designshack.net/articles/css/everything-you-never-knew-about-css-floats/

* Floated elements are pushed to the edge of their containers, no further.

* Any floated element will either appear next to or below a previous floated element. If the elements are floated left, the second element will appear to the right of the first. If they’re floated right, the second element will appear to the left of the first.

* A left-floating box can’t be further right than a right-floating box.

* Floated elements can’t go higher than their container’s top edge (this gets more complicated when collapsing margins are involved, see original rule).

* A floated element can’t be higher than a previous block level or floated element.

* A floated element can’t be higher than a previous line of inline elements.

* One floated element next to another floated element can’t stick out past the edge of its container.

* A floating box must be placed as high as possible. (No translation necessary)

* A left-floating box must be put as far to the left as possible, a right-floating box as far to the right as possible. A higher position is preferred over one that is further to the left/right. (No translation necessary)

### The clear property

Ref and example: http://alistapart.com/article/css-floats-101#section3

The `clear property` has five values available: 

* `left` : the top edge of the element must sit below any element that has the `float: left` property applied to it
* `right`: the top edge of the element must sit below any element that has the `float: right` property applied to it
* `both` : the top edge of the element must sit below any element floated either left or right. 
* `inherit`: takes on the clear property from its parent element
* `none` (default): follow the normal flow

### Float examples

* 2 column layout with header and footer: http://alistapart.com/article/css-floats-101#section4
* right column’s background color to extend all the way down the page http://alistapart.com/article/fauxcolumns
*


### CSS3 Box Sizing

`box-sizing` property: allows us to change exactly how the box model works and how an element’s size is calculated. 

* `content-box` value: is the default value, leaving the box model as an additive design.

* `padding-box` value: 
  * When using the padding-box value, if an element has a width of 400 pixels and a padding of 20 pixels around every side, the actual width will remain 400 pixels. As any padding values increase, the content size within an element shrinks proportionately. I
  * f we add a border or margin, those values will be added to the width or height properties to calculate the full box size. For example, if we add a border of 10 pixels and a padding of 20 pixels around every side of the element with a width of 400 pixels, the actual full width will become 420 pixels.

* `border-box` value:
  * 


The best box-sizing value to use is border-box:

* If we want an element to be 400 pixels wide, it is, and it will remain 400 pixels wide no matter what padding or border values we add to it.
* we can easily mix length values.
* say we want our box to be 40% wide, adding a padding of 20 pixels and a border of 10 pixels around every side of an element isn’t difficult, and we can still guarantee that the actual width of our box will remain 40% despite using pixel values elsewhere.

The only drawback to using the box-sizing property is that as part of the CSS3 specification, it isn’t supported in every browser; it especially lacks support in older browsers. Fortunately this is becoming less and less relevant as new browsers are released. Chances are we’re safe to use the box-sizing property, but should we notice any issues, it’s worth looking into which browser those issues are occurring with

### Common CSS properties

* http://learn.shayhowe.com/html-css/getting-to-know-css/#css-property-values
  * colors
  * lenght (pixels, Percentages, ... )

#### Margin

https://css-tricks.com/almanac/properties/m/margin/

`margin: <margin-top> || <margin-right> || <margin-bottom> || <margin-left>`

~~~
  margin-top: 20px;
  margin-right: 10px;
  margin-bottom: 20px;
  margin-left: 10px;
~~~

`auto` is handy for horizontal centering.

### CSS media queries

* https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Media_queries

When a media query is true, the corresponding style sheet or style rules are applied

In this example the style sheet is applied only if the viewport is less than 800px 

~~~html
<!-- CSS media query on a link element -->
<link rel="stylesheet" media="(max-width: 800px)" href="example.css" />
~~~





## Browser-Specific Properties & Values: moz, ms, webkit

As CSS3 was introduced, browsers gradually began to support different properties and values, including the box-sizing property, by way of vendor prefixes. As parts of the CSS3 specification are finalized and new browser versions are released, these vendor prefixes become less and less relevant. As time goes on, vendor prefixes are unlikely to be a problem; however, they still provide support for some of the older browsers that leveraged them. We may run across them from time to time, and we may even want to use them should we wish to support older browsers.

# Advanced CSS

## Clearfix Trick

The Problem: When a float is contained within a container box that has a visible border or background, that float does not automatically force the container's bottom edge down as the float is made taller. Instead the float is ignored by the container and will hang down out of the container bottom like a flag. 

[Example](http://themergency.com/clearfix/clearfix_demo_1_none.htm)

There are a lot of different solution to this issue, bootstrap 3.x uses the one called "Micro clearfix hack" described [here](http://nicolasgallagher.com/micro-clearfix-hack/)

* http://perishablepress.com/lessons-learned-concerning-the-clearfix-css-hack/
* https://css-tricks.com/all-about-floats/

Solution: using the `:after` pseudo-selector 

Refs: 

* https://developer.mozilla.org/en-US/docs/Web/CSS/::after


## Tooltip using pure CSS

* https://developer.mozilla.org/en-US/docs/Web/CSS/::after#Tooltips

## Boostrap vertical space between stacked columns

https://coderwall.com/p/0jezca/vertical-spacing-for-bootstrap-columns

## Columns with the same height

* Use `padding-bottom: %XX`: the padding will force the height of the column's content, for eexample if you need a ratio of 2:1, use 50% bottom-padding
* Position absolute for elements within the columns

Example: see Kenwood user public profile

# BootStrap

* CSS: http://getbootstrap.com/css/
* list of tutorials: http://www.quora.com/Are-there-any-good-tutorials-on-using-Twitter-Bootstrap
* [Github Repo](https://github.com/twbs/bootstrap)
* Full Tutorial guide: http://www.w3resource.com/twitter-bootstrap/CSS-overview.php

## Workflows to work with Bootstrap

### Use Boostrap with Less 

**THIS IS MY PREFERRED WORKFLOW**

REF: http://www.helloerik.com/bootstrap-3-less-workflow-tutorial

Just create a less file that only imports other Less files:

In this example we call it site.less:

~~~
@import "bootstrap/bootstrap.less";
@import "font-awesome/font-awesome.less";
 
@import "myproject-variables.less";
@import "myproject-mixins.less";
@import "myproject-nav.less";
@import "myproject-header.less";
@import "myproject-footer.less";
~~~

It almost always goes the Bootstrap folder first, then font-awesome, then my own variables and mixins.

* When importing my own files, variables are first, so they can be used on anything below.
* Even though this file is named the same as the Bootstrap variables.less file, it won’t overwrite anything unless you specifically name the variable the same. 
* You can override existing Bootstrap variables with your own, or just start creating what you need. 

#### EX: Middleman + Less + Bootstrap

I used it also with middleman which use sprocket, just add:

* `gem "sprockets-less"` : merge the sprocket dependency graph with the less `@import` dependency graph. This allow you to use livereload with less files and to use mixins. Sprocket will now detect the less file extention and use the proper compiler.
* `gem "less"` : less compiler to compile less files

Ask sprocket to require your `source/stylesheets/all.css`

~~~
/*
*= require site
*/
~~~

### Use Bootstrap dist

pro: 

* super fast implementation (just import bootstrap.css, no dependencies for less)

cons:

* cannot override less variables
* cannot use bootstrap mixin


## Mobile

* Viewport
* Zoomable content

## Typography and links

Bootstrap sets basic global display, typography, and link styles. They can be found within scaffolding.less


## Grid System

* http://www.helloerik.com/the-subtle-magic-behind-why-the-bootstrap-3-grid-works
* [Bootstrap doc](http://getbootstrap.com/css/#grid)
* https://scotch.io/tutorials/understanding-the-bootstrap-3-grid-system
* [Simple tutorial](http://blog.jetstrap.com/2013/08/bootstrap-3-grids-explained/)



TODO:

* gutter (grondaia)
* default VS fluid layout
* breakpoint media query
* Offsetting columns http://getbootstrap.com/css/#grid-offsetting

### The grid system is mobile First

The grid is made of rows and columns classes. 

"Mobile First", meaning that almost everything has been designed to start from a lower screen size and scale up. Columns classes are designed to cascades up from mobile devices.


There are four family of classes, each defines a Grid Systems.
The width of the viewport is the parameter that trigger the switch from a grid to another ( it uses media queries, see [internals]({{site.url}}/guides/html_css.html#internals)).

The default widths that set the frontiers between one grid and another are the follows:

* Extra small devices - Phones `(< 768px)`
* Small devices - Tablets `(>= 768px)`
* Medium devices - Desktops `(>= 992px)`
* Large devices - Desktops `(>= 1200px)`

All these widths are less variable that can be customized.


Each of the different supported viewports have a particular class prefix to address it, as follows:

* `col-xs-*` - Extra small devices
* `col-sm-*` - Small devices
* `col-md-*` - Medium devices
* `col-lg-*` - Large devices

Each of this family provide a set of 

To make use of the Grid System you'd need a container element, with a class "container", and inside a second container with a class "row"



### Internals

#### Mobile first and media queries

Bootstrap 3 is a mobile-first front-end framework. I’ve included the correct order for the Media Queries below, but I’ve also included at the bottom of them the non-mobile first breakpoints in case some people aren’t used to the mobile-first methodology since technically both will work.

To understand how Bootstrap uses media query remember that :

* `Min-Width` media query: Refers to everything greater than or equal to the amount given.
* `Max-Width` media query: Refers to everything less than or equal to the amount given.
* The order in which stylesheet properties are declared can determine which is applied: 
  * if two declarations have the same weight, origin and specificity, the latter specified wins.
  * Declarations in imported style sheets are considered to be before any declarations in the style sheet itself.
  * Ref: [W3C: cascading order](http://www.w3.org/TR/2011/REC-CSS2-20110607/cascade.html#cascading-order)

Responsive classes are declared:

* from the smaller class to the larger class 
* guarded from media queries that are true only on devices greater than the grid break point

For example each column class redefine the 

~~~
/*==========  Mobile First Method  ==========*/
 
	/* Custom, iPhone Retina */
	@media only screen and (min-width : 320px){
    ....  class declaration .....
	}
 
	/* Extra Small Devices, Phones */
	@media only screen and (min-width : 480px){
    ....  class declaration ..... 
	}
 
	/* Small Devices, Tablets */
	@media only screen and (min-width : 768px){
    ....  class declaration ..... 
	}
 
	/* Medium Devices, Desktops */
	@media only screen and (min-width : 992px){
    ....  class declaration ..... 
	}
 
	/* Large Devices, Wide Screens */
	@media only screen and (min-width : 1200px){
    ....  class declaration .....
	}


 
/*==========  Non-Mobile First Method  ==========*/
 
	/* Large Devices, Wide Screens */
	@media only screen and (max-width : 1200px){
    ....  class declaration .....
	}
 
	/* Medium Devices, Desktops */
	@media only screen and (max-width : 992px){
    ....  class declaration .....
	}
 
	/* Small Devices, Tablets */
	@media only screen and (max-width : 768px){
    ....  class declaration .....
	}
 
	/* Extra Small Devices, Phones */
	@media only screen and (max-width : 480px){
    ....  class declaration .....
	}
 
	/* Custom, iPhone Retina */
	@media only screen and (max-width : 320px){
    ....  class declaration .....
	}
~~~

#### Container, rows and cols

`grid.less` defines the `.container*` classes, that MUST contains all the grid system classes:

* elements of the `.container` contain element of class `.row`
* elements of class `.row` contain elements of class `.col-*-*`
* elements of class  `.col-*-*` may contain other element of class `.row`  


Bootstrap uses the following media queries to create the key breakpoints in the grid system:

~~~
/* Extra small devices (phones, less than 768px) */
/* No media query since this is the default in Bootstrap */

/* Small devices (tablets, 768px and up) */
@media (min-width: @screen-sm-min) { ... }

/* Medium devices (desktops, 992px and up) */
@media (min-width: @screen-md-min) { ... }

/* Large devices (large desktops, 1200px and up) */
@media (min-width: @screen-lg-min) { ... }
~~~


The `.container` class has a fixed width that depends on the viewport size, this relationship is implemented using media queries. Because `@screen-sm-min` > ` @screen-md-min` > ` @screen-lg-min` on larger viewport the latest width value will override the previous one:

~~~
.container {
  .container-fixed();

  @media (min-width: @screen-sm-min) { // this query is true only if width > @screen-sm-min
    width: @container-sm;
  }
  @media (min-width: @screen-md-min) { // 
    width: @container-md;
  }
  @media (min-width: @screen-lg-min) {
    width: @container-lg;               
  }
}

.container-fixed(@gutter: @grid-gutter-width) {
  margin-right: auto;            //auto margin to center the container horizontally
  margin-left: auto;             
  padding-left:  (@gutter / 2);  // padding to compensate the row negative margin
  padding-right: (@gutter / 2);
  &:extend(.clearfix all);
}
~~~

The `.row` class is quite simple, it add only a negative margin:

~~~
.row {
  .make-row();
}

// Creates a wrapper for a series of columns
.make-row(@gutter: @grid-gutter-width) {
  margin-left:  (@gutter / -2);
  margin-right: (@gutter / -2);
  &:extend(.clearfix all);
}
~~~


Col-*-* classes are defined here by two functions `.make-grid-columns()` and `.make-grid(...);` :

~~~

// Common styles for small and large grid columns
.make-grid-columns();

// Columns, offsets, pushes, and pulls for extra small devices
.make-grid(xs);


//small device range
@media (min-width: @screen-sm-min) {
  .make-grid(sm);
}
// desktop device range.
@media (min-width: @screen-md-min) {
  .make-grid(md);
}
//large desktop device range.
@media (min-width: @screen-lg-min) {
  .make-grid(lg);
}
~~~


`.make-grid-columns()` doesn't use media queries and defines all the properties available also below the breakpoint of each grid. Note that the `float` property is not set here so below the breakpoint all col classes behave like normal blocks and will stack one below the other. 


Below there is a self contained version of `.make-grid-columns()` that you can compile for test:

~~~
@grid-columns: 12;      //added to be selfcontained
@grid-gutter-width: 15; //added to be selfcontained

.make-grid-columns() {
  // Common styles for all sizes of grid columns, widths 1-12
  .col(@index) { // initial
    @item: ~".col-xs-@{index}, .col-sm-@{index}, .col-md-@{index}, .col-lg-@{index}";
    .col((@index + 1), @item);
  }
  .col(@index, @list) when (@index =< @grid-columns) { // general; "=<" isn't a typo
    @item: ~".col-xs-@{index}, .col-sm-@{index}, .col-md-@{index}, .col-lg-@{index}";
    .col((@index + 1), ~"@{list}, @{item}");
  }
  .col(@index, @list) when (@index > @grid-columns) { // terminal
    @{list} {
      position: relative;
      // Prevent columns from collapsing when empty
      min-height: 1px;
      // Inner gutter via padding
      padding-left:  (@grid-gutter-width / 2);
      padding-right: (@grid-gutter-width / 2);
    }
  }
  .col(1); // kickstart it
}

.make-grid-columns(); //added to be selfcontained

~~~

compiled will output all the common properties for column classes:

~~~
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 7.5;
  padding-right: 7.5;
}
~~~


Then the `.make-grid(...)` function will compile each grid system, example `.make-grid(xs)`:

~~~
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
....
.col-xs-1 {
  width: 8.33333333%;
}


.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
....
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}


.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
....
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}


.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
....
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}

~~~


Note that for col class `width` is a percentage calculated as `@index / @grid-columns`:
~~~
  .col-@{class}-@{index} {
    width: percentage((@index / @grid-columns));
  }
~~~

A row will always have space for the maximum number of colums (`@grid-columns`). For example, if `@grid-columns=12`, and you put a `.col-xs-10` and a `.col-xs-2` in a row the total width will be `83.33333333 + 16.666667 = (10/12 + 2/12) = 100%`


Pull and Push classes use `auto` for the index 0 and `left` or `right` for the the other indexes:

* `.col-@{class}-pull-0` and `.col-@{class}-push-0` will reset to auto (which means no offset)
* `right` and `left` will offset the floated div from the its computed position [see here](http://stackoverflow.com/questions/2635426/css-position-relative-and-float-left) 

~~~
  .col-@{class}-pull-@{index} {
    right: percentage((@index / @grid-columns));
  }

.calc-grid-column(@index, @class, @type) when (@type = push) and (@index > 0) {
  .col-@{class}-push-@{index} {
    left: percentage((@index / @grid-columns));
  }
}
~~~

Offset classes use a `margin-left` in percentage:

~~~
  .col-@{class}-offset-@{index} {
    margin-left: percentage((@index / @grid-columns));
  }
~~~






### Container

* `.container` : Fixed width
* `.container-fluid` : Fluid full width

### Column classes

* xs classes target mobile devices
* sm targets tablets
* md targets laptops and smaller desktop screens
* lg targets large desktop screens.


The best way to think about the new grid classes is that they work from mobile up, rather than from desktop down: For example, using .col-lg-4 means your grid will stay stacked on mobile, tablet, and small desktop screens. Only until the large desktop breakpoint is reached will the grid go horizontal.

### Column Wrapping: more than 12 columns

Column wrapping: http://getbootstrap.com/css/#grid-example-wrapping

### Nesting grids

One nice side effect of the 100% fluid grid on Bootstrap 3 is that nesting grids is now incredibly easy.

With the new grid (and the old fluid one), you just use the same grid column sizes, and think of percentages of the parent column. For example, .col-xs-6 inside of a .col-xs-6 is just 50% of that 50% column. Much more intuitive!


### Offset

* [doc](http://getbootstrap.com/css/#grid-offsetting)

The .col-xs=* classes don’t support offsets, but they are easily replicated by using an empty cell.

To use offsets on large displays, use the .col-md-offset-* classes.

### Column Ordering : push/pull

http://getbootstrap.com/css/#grid-column-ordering

* `push` classes use the `right` property to offset a column, you can reset this property to the defaul `auto` value using the `push-0` class.
* viceversa the `pull` class uses `left` 

Use case: the 500x500 pixel imagese in this [example](http://getbootstrap.com/examples/carousel/) are positioned using push and pull classes.

### Grid examples

4 column layout on desktop, 2 on tablet, 1 on mobile : http://blog.jetstrap.com/2013/08/bootstrap-3-grids-explained/

## How Bootstrap use less to calculate column class

http://www.helloerik.com/bootstrap-3-less-workflow-tutorial

## Components

### Navs

Doc:

* http://getbootstrap.com/components/#nav
* http://getbootstrap.com/components/#navbar
* [what's the difference between using NAV and DIV around Bootstrap 3 navbars](http://stackoverflow.com/questions/18628097/whats-the-difference-between-using-nav-and-div-around-bootstrap-3-navbars)

With bootstrap you can create:

* static navbars with simple navigation
* navbars with dropdown menus and search boxes.

What is the difference between the navbar and nav pills?

* Navbar aims to be common to all pages of your site ("support for a project name" is the link to homepage) whereas nav pills may be a navbar specific to a page or a section.
* Basically, navbar is unique and provides links to main parts of your site. Nav pills may provide internal links to your page anchors...
* But this is your decision anyway, depending on your preferences for menu rendering.
* http://stackoverflow.com/questions/14022135/in-twitter-bootstrap-what-is-the-difference-between-the-navbar-and-nav-pills

### Navbar


### TODO

Capire meglio:

* classes:  navbar navbar-default, "navbar-header", "navbar-brand"
* classes: collapse navbar-collapse
* attributes: data-target, data-toggle

## Custom Bootstrap Theme

* [Tutorial](https://divshot.com/blog/open-source/bootstrap3/themestrap-lightweight-theme-kit-for-bootstrap-3/)

## Bootstrap Themes

Worthy:

* https://github.com/Html-Coder/Worthy
* http://htmlcoder.me/preview/worthy/v.1.0/
* http://bootstrapzero.com/bootstrap-template/worthy

# Responsive Designs Gallery

* http://mediaqueri.es/
