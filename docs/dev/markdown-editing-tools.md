# Markdown Organization and Editing Tools Explanation
 
## Images

We keep all the images in the `docs/images` directory and we reference them with relative paths that are easy to manage.

Basically we want to keep the following folder structure:

```bash
└── docs
    ├── dev
    │    └── markdown-editing-tools.md
    └── images
        └── docs
            └── dev
                └── markdown-editing-tools
                    └── img22.png
```

in pseudocode:
- given a markdown file in `documentRelativeFilePath = docs/dev/markdown-editing-tools.md`
- documentRelativeFilePathWithoutExt = remove the `.md` from documentRelativeFilePath
- we copy the image a image in `docs/images/${documentRelativeFilePathWithoutExt}/img22.png`

This behaviour can be automatically implemented with a VSCode workspace configuration:

```json
    "markdown.copyFiles.destination": {
        "/docs/**/*": "/docs/images/${documentRelativeDirName}/${documentBaseName}/${fileName}"
    },
```

Or this neovim configuration: TODO

### EXPLANATION OF ALL ALTERNATIVE WE TESTED WITH PROS AND CONS

#### Constraints imposed by mkdocs
First we considered all the constraints imposed by mkdocs:

1. Images must be in a subdirectory of the `docs_dir`

For example with `docs_dir: docs`, this works:

```bash
└── docs
    ├── dev
    │   └── markdown-editing-tools-explanation.md
    └── images
        └── docs
            └── dev
                └── markdown-editing-tools
                    └── img22.png
```

This doesn't work it's out of the `docs_dir` and is not built or exposed by `mkdocs serve` or `mkdocs build`:

```bash
└── docs
│   └── dev
│       └── markdown-editing-tools-explanation.md
└── images
    └── docs
        └── dev
            └── markdown-editing-tools
                └── img22.png
```

#### Constraints imposed by VSCODE

```bash
└── docs
    ├── dev
    │   └── markdown-editing-tools-explanation.md
    └── images
        └── docs
            └── dev
                └── markdown-editing-tools
                    └── img22.png
```



## VSCode support for Markdown

### Link Management
[Official documentation](https://code.visualstudio.com/docs/languages/markdown#_inserting-images-and-links-to-files)

When you paste a file, a link to a file, or a URL, you can choose to insert a Markdown link or to include the link as plain text:
* drag hold shift key to....

### Image Management
[Official documentation](https://code.visualstudio.com/docs/languages/markdown#_inserting-images-and-links-to-files)

VSCode offers practical support for managing images in Markdown documents. This functionality allows users to insert and reference images effectively while maintaining a structured approach to file organization:

- **Automatic Image Copying**: With specific settings, VSCode can copy image files to designated directories when referenced in Markdown, helping to keep the project organized.

- **Dynamic Path Management**: Users can define patterns for image placement, ensuring that images are stored based on the Markdown document they are associated with.


You can copy paste image in VSCode (using cmd+c, cmd+v). The `markdown.copyFiles.destination` setting controls where the new image file should be created. Example:

```json
    "markdown.copyFiles.destination": {
        "/docs/**/*": "/docs/images/${documentRelativeDirName}/${documentBaseName}/${fileName}"
    },
```

Let’s see how this works in practice with the configuration we discussed, given your file paths:

Example Scenario
* File Path of the Markdown Document: `/Users/me/myProject/docs/dev/markdown-editing-tools.md`
* Workspace Folder: `/Users/me/myProject`
* Image File: `img22.png`

Glob: `/docs/**/*`, our file path relative to the workspace folder is `/docs/dev/markdown-editing-tools.md` so it matches the glob.

Expected Copy Destination based on your configuration:
- **Document Relative Directory Name**: This would be `docs/dev` because it's the directory of the Markdown file relative to the workspace folder.
- **Document Base Name**: This would be `markdown-editing-tools` since it’s the name of the Markdown file without the `.md` extension.
- **File Name**: This would be `img22.png` as this is the name of the image file you're copying.

Substituting the placeholders:

- `${documentRelativeDirName}` → `docs/dev`
- `${documentBaseName}` → `markdown-editing-tools`
- `${fileName}` → `img22.png`

Thus, the destination path for the copied image would be:

```
/Users/me/myProject/docs/images/docs/dev/markdown-editing-tools/img22.png
```

Which will create the following folder structure relative to the workspace folder:

```bash
└── docs
    ├── dev
    │    └── markdown-editing-tools.md
    └── images
        └── docs
            └── dev
                └── markdown-editing-tools
                    └── img22.png
```


**GLOBS**

This setting maps globs that match on the current Markdown document to image destinations, for example:

- `"/docs/**/*"`: Matches all files in the `docs` directory and its subdirectories.
- `"/**/*"`: Matches all files in the entire workspace.


**DESTINATION PATH**


⚠️⭐️ IMPORTANT ⭐️⚠️: when you use Absolute path in the destination path, the part is interpreted as starting at the document workspace folder (which is the path return by the `${documentWorkspaceFolder}` variable described below), *NOT* at the root of your system.

The image destination path, "/docs/images/${documentBaseName}/${fileName}" in the example above, can use some simple variables available to customize the destination path based on the Markdown document path you are working on. This is a list of variables we use most of the time:

/Users/me/SRC/nicola_blog/docs/dev/markdown-editing-tools.md
        "/**/*": "/docs/images/${documentRelativeFilePath}/${fileName}"



- `${documentRelativeDirName}`: path of directory containing the markdown file, relative to the workspace folder (`${documentWorkspaceFolder}`)
    - e.g. if the file path is `/Users/me/myProject/docs/dev/markdown-editing-tools.md` and the workspace folder is `/Users/me/myProject` then `${documentRelativeDirName}` will be `docs/dev`.

- `${documentFileName}`: The full filename of the Markdown document
    - e.g. if the file path is `/Users/me/myProject/docs/dev/markdown-editing-tools.md`, `${documentFileName}` will be `markdown-editing-tools.md`.
- `${documentBaseName}`: The basename of the Markdown document
    - e.g. if the file path is `/Users/me/myProject/docs/dev/markdown-editing-tools.md`, `${documentBaseName}` will be `markdown-editing-tools`. It is the name of the markdown file without the path and the extension, it could be useful if you want to create a folder that is independent from the nesting of the markdown file in the project directory structure.

- `${fileName}`: The file name of the dropped file
    - e.g.  if you paste an image named `image.png` whatever the path the file path is, `${fileName}` will be `image.png`.


These are other variables that can be used but we didn't discover yet how to use them:
- `${documentFilePath}`: Absolute path of the Markdown document
    - e.g. if the file path is `/Users/me/myProject/docs/dev/markdown-editing-tools.md`, `${documentFilePath}` will be `/Users/me/myProject/docs/dev/markdown-editing-tools.md`.

- `${documentDirName}`: Absolute parent directory path containing the Markdown document
    - e.g. if the file path is `/Users/me/myProject/docs/dev/markdown-editing-tools.md`, `${documentDirName}` will be `/Users/me/myProject/docs/dev`.
    - This kind of variable considers the absolute path and not the relative path, this means that will contain the home folder path of the current user. This is not very useful for us in our case of local development. May be it can be useful for other kind of projects that are not local development but happens on the server.

- `${documentRelativeFilePath}`: Relative path of the Markdown document
    - e.g. if the file path is `/Users/me/myProject/docs/dev/markdown-editing-tools.md` and the current workspace is `/Users/me/myProject` then `${documentRelativeFilePath}` will be `docs/dev/markdown-editing-tools.md`.

- `${documentExtName}`: The extension of the Markdown document
    - e.g. if the file path is `/Users/me/myProject/docs/dev/markdown-editing-tools.md`, `${documentExtName}` will be `md`.


- `${fileExtName}`: The extension of the dropped file, e.g. png.
    - e.g.  if you paste an image named `image.png` whatever the path the file path is, `${fileExtName}` will be `png`.

- `${documentWorkspaceFolder}`:refers to the root directory of the currently active workspace in Visual Studio Code, which contains the files and folders opened in the editor.
    - e.g. If I open the project in `/Users/me/myProject`, no matter what file I am editing, `${documentWorkspaceFolder}` will always be `/Users/me/myProject`.

#### Advanced usage of variables

[VSCode variable transforms](https://code.visualstudio.com/docs/editor/userdefinedsnippets#_variable-transforms)

