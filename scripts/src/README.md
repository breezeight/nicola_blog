## Installation

To install the required dependencies, run:

```bash
poetry install
```

## Usage

You can use the script by running the following command:

```bash
poetry run move_and_update <source> <destination> <markdown_file>
```

### Parameters:
- `<source>`: The path to the file or directory you want to move.
- `<destination>`: The path to the new location where you want to move the file or directory.
- `<markdown_file>`: The path to the Markdown file that contains image links to be updated.

## Example

Assuming you have the following directory structure:

```
docs/
└── dev/
    └── markdown-editing-tools.md
images/
└── docs/
    └── dev/
        └── markdown-editing-tools/
            └── img22.png
```

And you want to move the `img22.png` file from `images/docs/dev/markdown-editing-tools/` to `images/docs/dev/` and update the links in `markdown-editing-tools.md`, you would run:

```bash
poetry run move_and_update images/docs/dev/markdown-editing-tools/img22.png images/docs/dev/ images/dev/markdown-editing-tools.md
```

This command will:
1. Move `img22.png` to `images/docs/dev/`.
2. Update the image link in `markdown-editing-tools.md` to reflect the new path.

## License

This project is licensed under the MIT License.
























# Install the tool with pipx

```bash
pipx install .
```

reopen a terminal and you can use the tool:

```bash
gdoc2md your_gdoc_file.docx your_gdoc_export.md
```

# Google Docs to Markdown Converter

## Context

In modern documentation workflows, especially with collaborative tools like Google Docs, it is often necessary to export documents in different formats, such as `.docx` (Word) and `.md` (Markdown). Unfortunately, both the Pandoc export of `.docx` to `.md` and the Google Docs Markdown export present limitations:
 
- **Pandoc Export**: While it provides excellent Markdown formatting, the image quality is good but often the Markdown structure can be complex or incomplete.
- **Google Docs Markdown Export**: Google Docs natively supports exporting a document as Markdown (`File > Download > Markdown`), but the images are low-resolution and embedded in base64 format, making the output difficult to manage.

### The Solution

This project proposes a Python script (`docx2md.py`) that combines the strengths of both exports:
- **High-quality images** from the Pandoc export.
- **Simpler Markdown formatting** from the Google Docs Markdown export.

The script takes a `.docx` file exported from Google Docs, uses Pandoc to convert it to Markdown, and then replaces the low-resolution base64 images from the Google Docs Markdown export with the high-quality images from the Pandoc export. By doing so, we leverage the strengths of both tools to achieve a good-quality Markdown file with well-formatted content and clear images.

## Installation

### 1. Install Pandoc

#### On Ubuntu
To install Pandoc on Ubuntu, you can use the following commands:

```bash
sudo apt update
sudo apt install pandoc
```

#### On macOS (with Homebrew)
If you're on macOS and using Homebrew, install Pandoc by running:

```bash
brew install pandoc
```

### 2. Install Python Dependencies
The script uses standard Python libraries, so there are no additional dependencies to install beyond Python itself.

To install Python on Ubuntu or macOS:

#### On Ubuntu:

```bash
sudo apt install python3
```

#### On macOS (with Homebrew):

```bash
brew install python3
```

## How to Export Documents from Google Docs

### Export `.docx` from Google Docs
1. Open your Google Doc.
2. Go to the menu `File > Download > Microsoft Word (.docx)`.
3. Save the `.docx` file to your local machine.

### Export Markdown from Google Docs
1. Google Docs natively supports exporting to Markdown as well.
2. Go to the menu `File > Download > Markdown (.md)`.
3. Save the Markdown file to your local machine.

## Script Usage

Once you have exported both the `.docx` file and the Markdown file from Google Docs, you can use the `docx2md.py` script to combine them into a final, well-formatted Markdown file with high-quality images.

### Steps:
1. Place the `.docx` file and `.md` file from Google Docs in the same directory as the script or any working directory of your choice.
2. Run the script from the command line:

```bash
poetry run python3 google_docs_to_md_converter/docx2md.py tests/mocks/document.docx tests/mocks/document.md
```

### Example:

```bash
poetry run python3 google_docs_to_md_converter/docx2md.py tests/mocks/document.docx tests/mocks/document.md
```

The script will:
1. Convert the `.docx` file to Markdown using Pandoc.
2. Extract the images from the Pandoc export.
3. Replace the low-quality base64-encoded images in the Google Docs Markdown export with the high-resolution images from the Pandoc export.
4. Save the final output to a new Markdown file named `your_exported_gdoc_imported.md`.

## Heuristic Approach Explanation

This script uses a heuristic approach to merge the advantages of both exports. Due to the limitations of both export methods, some compromises had to be made:
- **Pandoc Export**: Provides higher-quality images but may have more complex Markdown formatting, especially for tables and other structures.
- **Google Docs Export**: Has a simpler Markdown format but embeds low-resolution images as base64, which is not ideal for documentation repositories that prefer separate image files.

By combining the two approaches, we aim to create a Markdown file that is easy to work with and contains high-quality images. 

### Why This Is Necessary:
- **Pandoc’s formatting** is great, but it often overcomplicates some Markdown structures.
- **Google Docs Markdown Export** is simpler but its base64-embedded images are not practical and are of lower resolution. We use the simpler Markdown structure while replacing the low-res images with high-quality images extracted by Pandoc.

## Known Limitations
- The heuristic depends on the order of the images in the two files being the same. If the images are not in the same order, the script might not match them correctly.
- Complex Markdown elements like tables or very custom layouts may require some manual adjustments after running the script.

## Conclusion

This script allows you to get the best of both worlds when exporting Markdown from Google Docs. It is particularly useful when working with documentation systems that expect Markdown and separate media files, providing a clean output with high-quality images.

### Future Enhancements:
As Google Docs now supports Markdown export natively (`File > Download > Markdown`), future versions of this tool may further optimize based on newer Google Docs export features, reducing the reliance on Pandoc for simpler documents. However, for now, this approach gives you the best results when combining formatting and image quality.


# Problem with the Code Block Add-On

## Introduction

In the process of exporting code snippets from Google Docs to Markdown, users often encounter formatting issues. The Code Block Google Doc add-on, while useful, can produce exports that are not well-structured in Markdown. This can result in single-line outputs, strange characters, and code being placed within tables, making it difficult to read and use effectively. 

## Solution for a single code block
This can be easily fixed with the right prompt.


```markdown
# Context
The code block that I will provide you:
- was formatted with [Code Block Google doc add-on](https://workspace.google.com/u/1/marketplace/app/code\_blocks/100740430168):
- than it has been exported from google doc to markdown
- the resulting export is not well formatted in markdown: it is single line, it contains some strange chars, it is contained in table.

# Objective
I'll wiil paste below the exported markdown, please clean it up, detect the programming language and configure the markdown to use the right code highlight. Output only the code block in markdown, avoid explanations.

# The exported markdown
<MARKDOWN_CODE_BLOCK HERE>
```


## Solution For the whole document

If your Google Doc contains multiple code blocks, and you want to fix them all, you can adapt the prompt to handle an entire document with several code blocks. The following prompt should be used to automatically identify and clean all code blocks in the document:

```markdown
# Context
The markdown document that I will provide you:
- was exported from Google Docs where code blocks were formatted using [Code Block Google Doc add-on](https://workspace.google.com/u/1/marketplace/app/code_blocks/100740430168):
- then it was exported from Google Docs to Markdown.
- the resulting export contains multiple code blocks that are not well formatted: they are in single lines, contain strange characters, and are enclosed within tables.

# Objective
Please go through the entire markdown document, detect all the code blocks, clean them up, detect the programming language for each code block, and configure the markdown to use the appropriate code highlighting. Output only the cleaned-up code blocks in markdown with the correct code highlighting.

# The exported markdown document
<WHOLE_MARKDOWN_DOCUMENT_HERE>
```


# Development

## Mock Google Doc

To run the tests, you need to have a Google Doc ID. You can use the following command to download the Google Doc and save it as a mock document. The expoet mock are expoported in tests/mocks/ but you can change the DOC_ID to download other documents or modify the document and download it again and commit the changes.

```bash
poetry run python3 tests/download_and_mock.py
```

## Run tests

Run all tests:
```bash
PYTHONPATH=. poetry run pytest
```

Run a single test function in a file:
```bash
PYTHONPATH=. poetry run pytest tests/md-utils/tests/test_md-utils.py::TestMdUtils::test_move_and_update
```

Where:
* `PYTHONPATH=.` is used to tell pytest to use the current directory as the Python path.
* `poetry run` is used to tell pytest to use the Python interpreter managed by Poetry.
* `TestDocxToMdConverter` is the test class.
* `test_convert_docx_to_md` is the test function to run of the `TestDocxToMdConverter` class.
