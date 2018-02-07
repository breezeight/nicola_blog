---
layout: post
title: "Google Doc"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["google"]
---

# Google App Script

## References

https://github.com/oshliaer/google-apps-script-awesome-list

## Getting Started

https://developers.google.com/apps-script/overview#your_first_script

## Type of Script

https://developers.google.com/apps-script/guides/standalone

A *standalone script* is any script that is not bound to a Google Sheets, Docs, Slides, or Forms file or Google Sites. These scripts appear among your files in Google Drive.

The easiest way to create a standalone script is to visit script.google.com


*Bound Script*
https://developers.google.com/apps-script/guides/bound


Google Cloud Platform Console:

https://console.cloud.google.com


Google AddOns

https://developers.google.com/apps-script/add-ons/


Add-ons can be restricted to a specific domanin: https://stackoverflow.com/questions/28990006/google-apps-script-publishing-addon-for-internal-use

### Libraries

Ref:

* http://www.mousewhisperer.co.uk/drivebunny/create-a-library-in-google-apps-script/

If you want to share your script between document Libraries avoid to copy and paste code between projects/documents.

Just create a library of useful code and access it from (or share it for use in) other projects just by referencing the script ID.

Now in my new project, in which I intend to use the library, I can go to Resources > Libraries… from the menu … and add the script ID


NOTE: project key is deprecated
Use the script ID it's not deprecated and it works
https://stackoverflow.com/questions/28990006/google-apps-script-publishing-addon-for-internal-use


I’ve called my script "Example", which will become the default name for the library. Firstly I use File > Manage Versions to save a version of my library:


https://developers.google.com/apps-script/guides/libraries


### 3rd parties Libraries

#### Oauth2


https://github.com/googlesamples/apps-script-oauth2

The token is stored for each user using PropertiesService.getUserProperties()
* https://developers.google.com/apps-script/guides/properties

## Logging

Google reference: https://developers.google.com/apps-script/reference/base/logger
Google guide:     https://developers.google.com/apps-script/guides/logging




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
