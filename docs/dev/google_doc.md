---
layout: post
title: "Google Doc"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["google"]
---

# Google App Script

ref: https://developers.google.com/apps-script/guides/sheets/functions#using_a_custom_function

Google Sheets offers hundreds of built-in functions like AVERAGE, SUM, and VLOOKUP. When these aren’t enough for your needs, you can use Google Apps Script to write custom functions — say, to convert meters to miles or fetch live content from the Internet — then use them in Google Sheets just like a built-in function.

If you don't know how to write JavaScript and don't have time to learn, check the add-on store to see whether someone else has already built the custom function you need. https://developers.google.com/apps-script/guides/sheets/functions#getting_a_custom_function_from_the_add-on_store

NOTE: Custom functions are created using standard JavaScript.

Once you've written a custom function or installed one from the add-on store, it's as easy to use as a built-in function:

- Click the cell where you want to use the function.
- Type an equals sign (=) followed by the function name and any input value — for example, =DOUBLE(A1) — and press Enter.
- The cell will momentarily display Loading..., then return the result.
- Ref: https://developers.google.com/apps-script/guides/sheets/functions#using_a_custom_function

## References

- AWESOME LIST https://github.com/oshliaer/google-apps-script-awesome-list
- Facebook Group https://www.facebook.com/groups/googleappsscript/

Open Source Add-ons examples:

- Project Aid for Jira - https://github.com/ljay79/jira-tools
- Date Add and Subtract - https://github.com/gsuitedevs/apps-script-samples/tree/master/sheets/dateAddAndSubtract

## Getting Started

https://developers.google.com/apps-script/overview#your_first_script

## Type of Script - Manage and reuse appscript code

https://developers.google.com/apps-script/guides/standalone

A _standalone script_ is any script that is not bound to a Google Sheets, Docs, Slides, or Forms file or Google Sites. These scripts appear among your files in Google Drive.

The easiest way to create a standalone script is to visit script.google.com

_Bound Script_
https://developers.google.com/apps-script/guides/bound

Google Cloud Platform Console:

https://console.cloud.google.com

Google AddOns

Another way to create a reusable apps script is to publish it as a private add-on in the marketplace and ask the admin to install it in domain wide. Now everyone will get it in the Add-ons menu of any sheets.

Here is a guideline for setting up a private add-on. Note you will get advantage of publish a private add-on without being reviewed by Google as well as maintaining the code in one place. You could deploy it in a few hours. 

https://developers.google.com/gsuite/add-ons/how-tos/publishing-editor-addons



https://developers.google.com/apps-script/add-ons/

Add-ons can be restricted to a specific domanin: https://stackoverflow.com/questions/28990006/google-apps-script-publishing-addon-for-internal-use

https://developers.google.com/apps-script/guides/sheets/functions#using_a_custom_function

### Add-ons



### Libraries

Ref:

- http://www.mousewhisperer.co.uk/drivebunny/create-a-library-in-google-apps-script/

If you want to share your script between document Libraries avoid to copy and paste code between projects/documents.

Just create a library of useful code and access it from (or share it for use in) other projects just by referencing the script ID.

Now in my new project, in which I intend to use the library, I can go to Resources > Libraries… from the menu … and add the script ID

NOTE: project key is deprecated
Use the script ID it's not deprecated and it works
https://stackoverflow.com/questions/28990006/google-apps-script-publishing-addon-for-internal-use

I’ve called my script "Example", which will become the default name for the library. Firstly I use File > Manage Versions to save a version of my library:

https://developers.google.com/apps-script/guides/libraries

### 3rd parties Libraries

#### Import JS libraries

https://stackoverflow.com/questions/18646554/importing-external-javascript-to-google-apps-script

```js
eval(
  UrlFetchApp.fetch(
    "https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.17.1/moment.min.js"
  ).getContentText()
);
```

#### Oauth2

https://github.com/googlesamples/apps-script-oauth2

The token is stored for each user using PropertiesService.getUserProperties()

- https://developers.google.com/apps-script/guides/properties

## Logging

Google reference: https://developers.google.com/apps-script/reference/base/logger
Google guide: https://developers.google.com/apps-script/guides/logging

Logger.log('You are a member of %s Google Groups.', 1);

Menu -> view -> Log

## Git and app script

http://www.postscapes.com/waste-management-sensor-company-enevo-collects-158m-in-funding/

`npm install -g node-google-apps-script`

## Connect with oauth2 services

- https://github.com/googlesamples/apps-script-oauth2
- samples: https://github.com/googlesamples/apps-script-oauth2/tree/master/samples

## [GUIDE] HTML Service: Create and Serve HTML

Refs:
* [GUIDES -> User intefaces](https://developers.google.com/apps-script/reference/html)
* [HTML Service Reference](https://developers.google.com/apps-script/reference/html)

With the HTML service you can create:
* a dialog or sidebar in Google Docs, Sheets, Slides, or Forms if your script is container-bound to the file: https://developers.google.com/apps-script/guides/html#code.gs
* a web app (you can also choose to embed it in a Google Site)

If your script is container-bound to the file:
* you do not need to save a version of your script or deploy it.
*  the function that opens the user interface must pass your HTML file as an [HtmlOutput](https://developers.google.com/apps-script/reference/html/html-output) object to the `showModalDialog()` or `showSidebar()` methods of the [Ui](https://developers.google.com/apps-script/reference/base/ui) object for the active document, form, or spreadsheet.

An instance of the `Ui object` for a Google App that allows the script to add features like menus, dialogs, and sidebars. For example `code.gs` and `Index.html`:

```js
// You can Use this code for Google Docs, Slides, Forms, or Sheets.
function onOpen() {
  SpreadsheetApp.getUi() //  Get the current Ui Object in a SpreadSheetApp (Or similarly DocumentApp or SlidesApp or FormApp).
      .createMenu('Dialog')
      .addItem('Open', 'openDialog')
      .addToUi();
}

function openDialog() {
  var html = HtmlService.createHtmlOutputFromFile('Index');
  SpreadsheetApp.getUi()
      .showModalDialog(html, 'Dialog title'); // Get the current Ui Object and show a modal
}
```

Index.html:

```html 
<!DOCTYPE html>
<html>
  <head>
    <base target="_top">
  </head>
  <body>
    Hello, World!
    <input type="button" value="Close"
        onclick="google.script.host.close()" />
  </body>
</html>
```

### Debugging and Logs

You can print debug logs in different ways:
* in your `.html` files use `console.log(....)` , because these code is executed client side, and check you browser console
* in you `.gs` files use `Logger.log` : Extensions -> App Scrips -> Executions (on the left pane)




### HTML Service: Communicate with Server Functions: google.script.run

[Guide](https://developers.google.com/apps-script/guides/html/communication)

[google.script.run](https://developers.google.com/apps-script/guides/html/reference/run) is an asynchronous client-side JavaScript API that allows HTML-service pages to call server-side Apps Script functions. For example:

```js
function doGet() {
  return HtmlService.createHtmlOutputFromFile('Index');
}

function doSomething() {     //INVOKED BY google.script.run
  Logger.log('I was called!');
}
```

```html
<!DOCTYPE html>
<html>
  <head>
    <base target="_top">
    <script>
      google.script.run.doSomething(); //
    </script>
  </head>
</html>
```


Server-side functions are asynchronous, to control the flow use:
* [withSuccessHandler(function)](https://developers.google.com/apps-script/guides/html/reference/run#withSuccessHandler(Function))
* [withFailureHandler(function)](https://developers.google.com/apps-script/guides/html/reference/run#withFailureHandler(Function))




# Spreadsheet

Query Language doc: https://developers.google.com/chart/interactive/docs/querylanguage?hl=en

Super fast intro : https://www.youtube.com/watch?v=GcsBFEbMuIA

ADD-ONS: https://developers.google.com/gsuite/add-ons/editors/sheets

Tutorial:

- Spreadsheet Service - Removing Duplicate Rows in a Spreadsheet https://developers.google.com/apps-script/articles/removing_duplicates

## VS Advanced Sheets Service

- Advanced Sheets Service: https://developers.google.com/apps-script/advanced/sheets
- Spreadsheet Service: https://developers.google.com/apps-script/reference/spreadsheet

Qua https://developers.google.com/gsuite/add-ons/editors/sheets dicono: "You can use the Apps Script advanced Sheets service to access the Sheets REST API directly.". Forse Advanced Sheets Service riguarda le api mentre l'altro è quello che puoi fare dagli script a cui accedi dal menù?!

## Shortcut

To drag a formula to the last row or colum:

- select the cell: cmd + C
- cmd+shift+right arrow or left arrov
- cmd + v

## [JOB] Reset clear certain cells in sheets when a button is pressed

https://support.google.com/docs/thread/5809954?hl=en

Snippet: https://google-apps-script-snippets.contributor.pw/snippets/spreadsheet_reset-sheets/

Example: https://docs.google.com/spreadsheets/d/1zdrgTiOFiZlKO5QN94NiGg6zd-By278nhH2XOmNtUTI/edit#gid=0

```js
function reset() {
  // Clear Both Format and Content
  SpreadsheetApp.getActiveSheet().getDataRange().clear();

  // Clear Format
  //SpreadsheetApp.getActiveSheet().getDataRange().clearFormat();

  // Clear Content
  //SpreadsheetApp.getActiveSheet().getDataRange().clearContent();
}

function onOpen() {
  let ui = SpreadsheetApp.getUi();
  ui.createMenu("Test Input and Locale").addItem("reset", "reset").addToUi();
}
```

## ArrayFormula

https://www.benlcollins.com/formula-examples/array-formula-intro/

In a nutshell: whereas a normal formula outputs a single value, array formulas output a range of cells!

## Query

Remove label: http://stackoverflow.com/questions/26867775/google-spreadsheet-query-can-i-remove-column-header
Tutorial: https://www.benlcollins.com/spreadsheets/google-sheets-query-sql/

Sample Usage

```
QUERY(A2:E6,"select avg(A) pivot B")
QUERY(A2:E6,F2,FALSE)
```

In Google `select` statement above uses this query language:

- intro: https://support.google.com/docs/answer/3093343?hl=en
- Query Language Reference (Version 0.7): https://developers.google.com/chart/interactive/docs/querylanguage

WARNING Language clauses must be in a specif order:

- https://developers.google.com/chart/interactive/docs/querylanguage

### Group By Year and Month

https://infoinspired.com/google-docs/spreadsheet/group-data-by-month-and-year-in-google-sheets/

## Date

Incremente date by month: `=EDATE(B37;1)` will increment the date stored in B37 by one month

NOTE: see the pararaph "Set Values" for usefull guideline about how to manage Dates in Google App Script.

### Date in JavaScript

SEE "## Standard Library: Date" in javascipt.markdown

### Example using moment.js with ADD-ON

https://github.com/gsuitedevs/apps-script-samples/blob/master/sheets/dateAddAndSubtract/dateAddAndSubtract.gs

TODO: si può usare anche con uno script?

- Ho provato a copiare i file nello script e ha funzionato https://docs.google.com/spreadsheets/d/1QmrxuF8zzUAOR3RiNVrH4yV7BnyakVTQw3EyxEbh2jU/edit#gid=1937347657

### Date Time Range

https://stackoverflow.com/questions/18636997/calculate-time-range-and-parse-date

See this example script usign `moment-range`

https://script.google.com/d/13kYXXRBjiWLguw5_SF25k8wtq4i9y_LWm-r90XaIq788C5N_Zjs6Tlm9/edit?mid=ACjPJvEVIWX3PO3_Da3AW5h-gE2WMqc3PWfsaGVnJc4SSu3msl9f8-qVKlm-20MUMobDr3fuzulp_cyhk-tItGQzuKXUV9iaRbi-SN6vJS_IJZdDHh-KzTOYUlG8_gStWauRKh3D9W3mDEM&uiv=2

```js
function testRange() {
  eval(
    UrlFetchApp.fetch(
      "https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.24.0/moment-with-locales.min.js"
    ).getContentText()
  );
  eval(
    UrlFetchApp.fetch(
      "https://cdnjs.cloudflare.com/ajax/libs/moment-range/2.2.0/moment-range.min.js"
    ).getContentText()
  );

  var range = moment.range(
    new Date(2020, 05, 25, 09, 00),
    new Date(2020, 05, 25, 13, 00)
  );
  var range2 = moment.range(
    new Date(2020, 05, 25, 09, 00),
    new Date(2020, 05, 25, 11, 00)
  );
  var range3 = moment.range(
    new Date(2020, 05, 25, 13, 00),
    new Date(2020, 05, 25, 15, 00)
  );
  var t = range.overlaps(range2); // expect true
  var f = range.overlaps(range3); // expect false
  //a = range.toString();
  a = 0;
}
```

## Conditional Formatting

Colors:
https://yagisanatode.com/2019/08/06/google-apps-script-hexadecimal-color-codes-for-google-docs-sheets-and-slides-standart-palette/

## Data Validation

Ref: https://infoinspired.com/google-docs/spreadsheet/data-validation-examples-in-google-sheets/#Limit_Text_Entry_in_Google_Sheets_Using_Data_Validation

### Scripting Data Validation

DOC:

- Access Rules: https://developers.google.com/apps-script/reference/spreadsheet/data-validation
- Create Rules: https://developers.google.com/apps-script/reference/spreadsheet/data-validation-builder

### Google Sheets | Three Alternatives for Multi-Select Dropdowns

Solution 1: Use a custom Script

- https://www.youtube.com/watch?v=Gsnzgvvx2y8&t=32s
- Link to Sheet with multi-select using of Apps Script - http://bit.ly/app-script-dd
- https://www.youtube.com/watch?v=dm4z9l26O0I

### Basic Example Script with Custom Formula

Set the data validation for cell K1 to equal L1 and K2 to equal L2 with a custom formula:

```js
function setDataValidation() {
  // Set the data validation for cell K1 to equal L1 and K2 to equal L2 with a custom formula.
  var cell = SpreadsheetApp.getActive().getRange("K1:K2");
  var rule = SpreadsheetApp.newDataValidation()
    .requireFormulaSatisfied("=EQ(K1,L1)")
    .build();
  cell.setDataValidation(rule);
}
```

### Regexp

- Intro RegExp in Google Sheet: https://www.distilled.net/how-to-use-regex-in-google-sheets/
- Tutorial RegExp: https://www.regular-expressions.info/tutorial.html
- Editor online RegExp: https://regex101.com/

```js
function setDataValidation() {
  // Doesn't allow _ and any uppercase
  var cell = SpreadsheetApp.getActive().getRange("B2:F");
  var rule = SpreadsheetApp.newDataValidation()
    .requireFormulaSatisfied('=NOT(REGEXMATCH(B2:F2,".*_.*|[A-Z]+"))')
    .build();
  cell.setDataValidation(rule);
}
```

### Allow Data Entry in a Range if Adjoining Column Contains “Yes”.

REF: https://infoinspired.com/google-docs/spreadsheet/data-validation-examples-in-google-sheets/

Here I am applying a custom formula to the range A1:A5

Steps:

- Select the range A1:A5.
- Go to the Data menu Data Validation.
- Select “Custom formula is” against Criteria.
- Enter the formula: `=B1="Yes"`

The above formula is an example to relative cell reference in Data Validation in Google Sheets. Just test it on your Sheet to understand the behavior. I have promised you to provide you the best Data Validation examples in Google Sheets. So here are a few more examples with custom formulas.

### Restrict/Allow Odd/Even Numbers in a Range

I am applying this restriction to the range A1:B10. So first select this range and use the below formula. Change the function ISODD with ISEVEN to only allow even numbers.

=isodd(A1)
Conditionally Allow ODD/EVEN Numbers in a Range

I want to only allow even numbers in the range A1:A5 if the range B1:B5 contains “Yes”.

To set the rule as follow, select the range A1:A5 and use the below data validation formula.

=and(iseven(A1),B1="Yes")
Data Validation to Restrict Duplicates in Google Sheets

You can restrict the entry of duplicates in Google Sheets using the Data Validation custom formula feature. Read that here – How Not to Allow Duplicates in Google Sheets.

Further, I have a tutorial that details how to use Regex in Data Validation in Google Sheets – Restrict Entering Special Characters in Google Sheets Using Regex.

Time to wind up this tutorial on best Data Validation examples in Google Sheets. Post your views in the comment. Enjoy!

## Cell Range

Doc Class Range: https://developers.google.com/apps-script/reference/spreadsheet/range#setBorder(Boolean,Boolean,Boolean,Boolean,Boolean,Boolean)

- Access and modify spreadsheet ranges. A range can be a single cell in a sheet or a group of adjacent cells in a sheet.

  let headers = sheet.getRange("A1:C1");

  //getDataRange is a handy shortcut to capture all the data in the sheet.
  let allData = sheet.getDataRange();

An entire column
E.g.: A:A , i.e. omit the start and end row numbers from the range.

An entire column starting with a particular row
E.g. A2:A , i.e. omit the ending row number from the range

An entire row
E.g. 2:2 , i.e. omit the start and end column characters from the range.

An entire row starting with a particular column
E.g. B2:2 , i.e. omit the ending column character from the range

A group of contiguous full columns
E.g. B:D , i.e. omit the start and end row numbers from the range.

A group of contiguous full columns starting with a particular row
E.g. B2:D , i.e. omit the ending row number from the range

A group of contiguous rows
E.g. 2:5 , i.e. omit the start and end column characters from the range.

A group of contiguous rows starting with a particular column
E.g. B2:5 , i.e. omit the ending column character from the range

### [JOB] Get a Range corresponding to the dimensions in which data is present

https://developers.google.com/apps-script/reference/spreadsheet/sheet#getdatarange

### How Google SpreadSheet interprets your input

NOTE: When set an input it depends on the default locale of your spreadsheet. To change it, go to File > Spreadsheet settings. You'll see a pop-up window where you can set your region under the General tab > Locale. Thus, you'll ensure those date and time formats you're accustomed to.

Ref: https://www.ablebits.com/office-addins-blog/2017/10/12/date-time-google-sheets/

### Get Values contained in the range

https://developers.google.com/apps-script/reference/spreadsheet/range#getvalues

The value may be of type Number, Boolean, Date, or String depending on the value of the cell. Empty cells return an empty string.

https://developers.google.com/apps-script/reference/spreadsheet/range#getdisplayvalues

Returns the displayed value of the top-left cell in the range. The value is a String. The displayed value takes into account date, time and currency formatting formatting, including formats applied automatically by the spreadsheet's locale setting. Empty cells return an empty string.

### Set Values

https://developers.google.com/apps-script/reference/spreadsheet/range#setvaluevalue

Sets the value of the range. The value can be numeric, string, boolean or date. If it begins with '=' it is interpreted as a formula.

WARNING: The Cell Format is IMPORTANT. Google Spreadsheet will parse your input differently, based on the cell format (and Locale=?)

Example: If you set a number

### Configure Cell Date-Number Format

https://developers.google.com/apps-script/reference/spreadsheet/range#setNumberFormat(String)

Formats: https://developers.google.com/sheets/api/guides/formats

### [JOB] Sorting Columns and Transferring Row to Another Sheet

https://www.google.com/search?q=google+spreadsheet+get+range+from+another+sheet&oq=google+spreadsheet+get+range+from+another+sheet&aqs=chrome..69i57j69i64.17511j0j1&sourceid=chrome&ie=UTF-8

## Style

Borders: https://developers.google.com/apps-script/reference/spreadsheet/range#setBorder(Boolean,Boolean,Boolean,Boolean,Boolean,Boolean)
NOTE: Return Range — This range, for chaining.

- vertical Boolean true for internal vertical borders, false for none, null for no change.
- horizontal Boolean true for internal horizontal borders, false for none, null for no change.
