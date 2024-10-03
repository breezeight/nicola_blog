# Google App Script

## Why Apps Script? Usaca and Examples

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

- [AWESOME LIST](https://github.com/oshliaer/google-apps-script-awesome-list)
- [Facebook Group](https://www.facebook.com/groups/googleappsscript)

Open Source Add-ons examples:

- [Project Aid for Jira](https://github.com/ljay79/jira-tools)
- [Date Add and Subtract](https://github.com/gsuitedevs/apps-script-samples/tree/master/sheets/dateAddAndSubtract)

## Getting Started with Apps Script

[Your First Script](https://developers.google.com/apps-script/overview#your_first_script)

## Type of Script - Manage and reuse appscript code

### Standalone Scripts


#### What is a standalone script?
A _standalone script_ is any script that is **not bound** to Google Sheets, Docs, Slides, Forms, or Google Sites. These scripts appear as separate files in your Google Drive and are great for managing code that works independently from any specific Google product.

Learn more: [Standalone Scripts Official Documentation](https://developers.google.com/apps-script/guides/standalone)

#### Common Applications of Standalone Google Apps Scripts

1. **Automating Google Drive File Management** – Automatically organize files in Google Drive, such as moving files to specific folders based on criteria.
2. **Sending Automated Emails with Gmail** – Automate scheduled or event-triggered emails using Gmail.
3. **Generating and Managing Calendar Events** – Automate Google Calendar event creation for recurring meetings or from a list of dates.
4. **Scheduled Reports and Notifications** – Generate reports or notifications on a regular schedule.
5. **Interacting with External APIs** – Integrate with third-party services using their APIs to automate tasks.
6. **Automating Backup of Google Drive Files** – Automatically back up specific folders or files in Google Drive to another location.
7. **Monitoring and Managing Google Group Membership** – Automate group management by adding or removing members in Google Groups based on external data.
8. **Creating Custom Google Forms** – Programmatically generate Google Forms for surveys, registrations, or quizzes, and process responses.
9. **Generating Documents (Docs, Sheets, Slides)** – Automatically generate and populate Google Docs, Sheets, or Slides from external data sources.
10. **Managing Google Contacts** – Automate contact creation, deletion, or updates in Google Contacts.
11. **Scheduling Tasks via Google Tasks API** – Automate task creation in Google Tasks based on project management workflows.
12. **Data Synchronization Between Google Services** – Sync data between different Google services like Sheets, Drive, and Calendar.

#### Tutorial list all files in your Google Drive


#### How to create a standalone script


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


