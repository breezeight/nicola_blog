# Google Apps Script File System - JSON Tutorial

## Objective:
In this tutorial, we will learn how to create a Google Apps Script that generates a hierarchical JSON representation of your Google Drive folder structure. By the end, you will be able to output a JSON object that reflects the folder and file arrangement in your Google Drive.

## Prerequisites:
- Basic understanding of Google Apps Script
- Access to a Google account with Google Drive enabled

## Step 1: Setting Up Your Script
Let’s begin by creating a new Google Apps Script project.

1. Open **Google Drive**.
2. Create a new folder for testing purposes:
   - Click on **New** > **Folder**.
   - Name the folder `tmp` (or any name you prefer).
3. Inside the `tmp` folder, create a few test files:
   - Click on **New** > **Google Docs** or **Google Sheets**, create a couple of files, and name them appropriately. For example, create files such as "Untitled document 1," "Untitled document 2," and "dati per test" (a spreadsheet).
4. Go back to the `tmp` folder.
5. Create a new Apps Script project:
   - Click on **New** > **More** > **Google Apps Script**.
   - Name your project something like `google-app-script-file-system-json-tutorial`.
6. Copy the following code into your Google Apps Script editor:

```javascript
function getFileSystemAsJSONInCurrentDirectory() {
  // Get the folder where the script is stored
  var scriptFile = DriveApp.getFileById(DriveApp.getFileById(ScriptApp.getScriptId()).getId());
  var currentFolder = scriptFile.getParents().next(); // Get the parent folder of the script
  
  // Build the JSON hierarchy
  var fileSystem = getFolderContents(currentFolder);
  
  // Log the resulting JSON
  Logger.log(JSON.stringify(fileSystem, null, 2));
}

// Function to recursively get the contents of a folder
function getFolderContents(folder) {
  var folderData = {
    title: folder.getName(),
    slug: generateSlug(folder.getName()),
    url: folder.getUrl(),
    type: 'folder',
    children: []
  };
  
  // Get all files in the folder
  var files = folder.getFiles();
  while (files.hasNext()) {
    var file = files.next();
    folderData.children.push({
      title: file.getName(),
      slug: generateSlug(file.getName()),
      url: file.getUrl(),
      type: 'file'
    });
  }
  
  // Get all subfolders in the folder
  var subfolders = folder.getFolders();
  while (subfolders.hasNext()) {
    var subfolder = subfolders.next();
    folderData.children.push(getFolderContents(subfolder)); // Recursively get contents
  }
  
  return folderData;
}

// Function to generate a slug from a title
function generateSlug(name) {
  return name
    .toLowerCase()
    .replace(/[^\w\s-]/g, '') // Remove non-word characters
    .replace(/\s+/g, '-')      // Replace spaces with dashes
    .trim();
}
```

## Step 2: Understanding the Code
Now, let’s walk through the key parts of the script.

- **`getFileSystemAsJSONInCurrentDirectory()`**: This is the main function that starts the process by selecting the current folder and calling another function to build the JSON structure.
- **`getFolderContents(folder)`**: This function takes a folder as input, gathers its contents (files and subfolders), and recursively does the same for all subfolders.

## Step 3: Running the Script
1. Save your script by clicking the **Save** button.
2. To run the script:
   - Click on the **Select function** dropdown (in the toolbar) and choose `getFileSystemAsJSON`.
   - Click the **Run** button.
   - You will need to authorize the script to access your Google Drive.
	   - A pop-up will appear saying: `Authorization required - This project requires your permission to access your data.`
	   - Click `Review Permissions`.
	   - If you see a warning that says `Google hasn’t verified this app`, click `Advanced` and then click `Go to google-app-script-file-system-json-tutorial (unsafe)`.
	   - After that, review the permissions and allow the necessary access.

3. Once the script runs, open the **Logs** by selecting **View** > **Logs**. The JSON representation of your file system hierarchy will be printed here.

## Step 4: Viewing the Output
The output will be a structured JSON object similar to the example below:

```json
{
  "name": "My Drive",
  "url": "https://drive.google.com/drive/u/0/folders/xxxxxx",
  "type": "folder",
  "children": [
    {
      "name": "Subfolder 1",
      "url": "https://drive.google.com/drive/u/0/folders/yyyyyy",
      "type": "folder",
      "children": [
        {
          "name": "File 1.txt",
          "url": "https://drive.google.com/file/d/zzzzzz/view",
          "type": "file"
        }
      ]
    },
    {
      "name": "File 2.txt",
      "url": "https://drive.google.com/file/d/aaaaaa/view",
      "type": "file"
    }
  ]
}
```

## Step 5: Experimentation
- Try running the script on different folders in your Google Drive.
- Modify the script to output additional metadata (e.g., file size or creation date).

## Conclusion
By following this tutorial, you’ve learned how to build a script that traverses the folder structure of your Google Drive and outputs a JSON object representing the hierarchy. You can now extend this to fit your specific needs or further explore Google Apps Script capabilities!
