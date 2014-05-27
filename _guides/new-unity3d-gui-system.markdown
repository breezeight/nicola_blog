---
layout: post
title: "New Unity3D GUI System"
date: 2014-03-07 18:54:09 +0100
comments: true
author: "Nicola Brisotto"
published: false
categories: ["Unity3D", "GUI"] 
---
# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# H1 header

## H2 header



We start by creating an Image Element, go to GameObject -> Create Other -> Image


{% comment %}   img right /images/new-unity3d-gui-system/unity3d-gui-canvas-hierarchy.png  {% endcomment %}
All the GUI elements must be children of the Canvas object, the Canvas
object is create if it doen's exist when you add the first element.

{% comment %}   img left /images/new-unity3d-gui-system/rect-transform-component.png  {% endcomment %}
The image has a component called "Rect component" instead of the regular
transform, it has additional field related to the layout.

TODO: documentare come usare i field nuovi

The element in the scene has handles to be rotated and translated,
similar to 2D sprites.

The canvas object is special because it has the Canvas Component. The
render mode option of this component affect how the GUI is rendered

* Screen Space: the Canvas object's rect transform is driven by the
  Canvas component. The Canvas object is always overlayed on top of the
entire screen. The size is automatically set to the size of the screen 
* World Space: the Canvas object can be placed anywhere just like a
  regular 3D object


https://www.youtube.com/watch?v=GMtQB4am3Kw&feature=youtu.be fino al
minuto 
