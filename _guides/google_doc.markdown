---
layout: post
title: "Google Doc"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["google"]
---

# App Script

## Git and app script

http://www.postscapes.com/waste-management-sensor-company-enevo-collects-158m-in-funding/

`npm install -g node-google-apps-script`

## Connect with oauth2 services

* https://github.com/googlesamples/apps-script-oauth2
* samples: https://github.com/googlesamples/apps-script-oauth2/tree/master/samples



# Spreadsheet

Query Language doc: https://developers.google.com/chart/interactive/docs/querylanguage?hl=en


* `toDate()`

# Shortcut

To drag a formula to the last row or colum:

* select the cell: cmd + C
* cmd+shift+right arrow or left arrov
* cmd + v

## Query 

Remove label: http://stackoverflow.com/questions/26867775/google-spreadsheet-query-can-i-remove-column-header

## Date

Incremente date by month: `=EDATE(B37;1)` will increment the date stored in B37 by one month


## Range

An entire column
E.g.: A:A , i.e. omit the start and end row numbers from the range.

An entire column starting with a particular row
E.g. A2:A , i.e. omit the ending row number from the range

An entire row
E.g. 2:2  , i.e. omit the start and end column characters from the range.

An entire row starting with a particular column
E.g. B2:2 , i.e. omit the ending column character from the range

A group of contiguous full columns
E.g. B:D , i.e. omit the start and end row numbers from the range.

A group of contiguous full columns starting with a particular row
E.g. B2:D , i.e. omit the ending row number from the range

A group of contiguous rows
E.g. 2:5  , i.e. omit the start and end column characters from the range.

A group of contiguous rows starting with a particular column
E.g. B2:5 , i.e. omit the ending column character from the range
