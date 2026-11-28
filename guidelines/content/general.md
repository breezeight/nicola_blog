# General Project Rules

## Repository Purpose
This is a personal knowledge base containing markdown notes on various technical topics, organized for easy reference and learning.

## Code Style
- Use consistent formatting for markdown files
- Wrap regex patterns in backticks to prevent MkDocs warnings
- Use proper markdown syntax for links and code blocks
- Use proper header hierarchy (H1, H2, H3, etc.)
- Include code blocks with appropriate syntax highlighting
- Use tables for structured information
- Add images and diagrams where helpful
- Include anchor links for easy navigation

## File Organization

### Directory Structure
- **docs/dev/** - Development and technical topics
- **docs/yoga_poses/** - Yoga-related content
- **docs/images/** - Supporting images and diagrams
- **docs/downloads/** - Downloadable resources
- Keep documentation files in `docs/` directory

### Naming Conventions
- Use descriptive, lowercase filenames with hyphens or underscores (e.g., `python-learning.md`)
- Group related topics in subdirectories (e.g., `aws/`, `dev/python/`)
- Use consistent naming patterns within topic areas
- Organize content by topic in subdirectories

## Content Guidelines

### File Structure
1. **Title/Header** - Clear, descriptive title
2. **Introduction** - Brief overview of the topic
3. **Main Content** - Organized with proper headers
4. **Examples** - Code snippets, configurations, or practical examples
5. **References** - Links to external resources, documentation

### Content Creation

#### Clarity and Readability
- Write clear, concise explanations
- Use simple language when possible
- Break complex topics into digestible sections
- Include practical examples to illustrate concepts
- Use bullet points and numbered lists for readability

#### Structure and Organization
- Use consistent header hierarchy
- Group related information together
- Include table of contents for long documents
- Use lists and tables for structured information
- Organize content logically with clear sections

#### Accuracy and Maintenance
- Keep information current and accurate
- Verify technical information before publishing
- Update content when technologies change
- Include version numbers and dates where relevant
- Review and update links regularly
- Add troubleshooting sections where relevant

#### Accessibility
- Use descriptive link text
- Include alt text for images
- Ensure proper contrast in code examples
- Use semantic HTML elements in markdown

### Cross-References and Collaboration
- Link between related notes using relative paths
- Maintain consistent terminology across documents
- Cross-reference related content
- Update links when files are moved or renamed
- Maintain a logical flow between topics
- Update indexes and navigation when adding content
- Add front matter with title and description when needed

## Git Workflow
- Commit changes with descriptive messages
- Use conventional commit format when possible
- Test builds before committing major changes

## Markdown Syntax you must follow

### GitHub Flavored Markdown (GFM) Documentation

Follow GitHub's markdown conventions for formatting, including: [GitHub Flavored Markdown (GFM) Documentation](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

In these section you can find the syntax you must follow.

#### Headings

To create a heading, add one to six `#` symbols before your heading text. The number of `#` you use will determine the hierarchy level and typeface size of the heading.

```markdown
# A first-level heading
## A second-level heading
### A third-level heading
```

When you use two or more headings, GitHub automatically generates a table of contents that you can access by clicking within the file header.

#### Styling Text

You can indicate emphasis with bold, italic, strikethrough, subscript, or superscript text in comment fields and `.md` files.

| Style                  | Syntax                 | Keyboard shortcut                         | Example                                      | Output                                 |
| ---------------------- | ---------------------- | ----------------------------------------- | -------------------------------------------- | -------------------------------------- |
| Bold                   | `** **` or `__ __`     | Command+B (Mac) or Ctrl+B (Windows/Linux) | `**This is bold text**`                      | **This is bold text**                  |
| Italic                 | `* *` or `_ _`         | Command+I (Mac) or Ctrl+I (Windows/Linux) | `_This text is italicized_`                 | _This text is italicized_              |
| Strikethrough          | `~~ ~~` or `~ ~`       | None                                      | `~~This was mistaken text~~`                 | ~~This was mistaken text~~            |
| Bold and nested italic | `** **` and `_ _`      | None                                      | `**This text is _extremely_ important**`     | **This text is _extremely_ important** |
| All bold and italic    | `*** ***`              | None                                      | `***All this text is important***`          | _**All this text is important**_       |
| Subscript              | `<sub> </sub>`         | None                                      | `This is a <sub>subscript</sub> text`        | This is a <sub>subscript</sub> text    |
| Superscript            | `<sup> </sup>`         | None                                      | `This is a <sup>superscript</sup> text`      | This is a <sup>superscript</sup> text  |
| Underline              | `<ins> </ins>`         | None                                      | `This is an <ins>underlined</ins> text`     | This is an <ins>underlined</ins> text  |

#### Quoting Text

You can quote text with a `>`.

```markdown
Text that is not a quote

> Text that is a quote
```

Quoted text is indented with a vertical line on the left and displayed using gray type.

#### Quoting Code

You can call out code or a command within a sentence with single backticks. The text within the backticks will not be formatted. You can also press the Command+E (Mac) or Ctrl+E (Windows/Linux) keyboard shortcut to insert the backticks for a code block within a line of Markdown.

```markdown
Use `git status` to list all new or modified files that haven't yet been committed.
```

To format code or text into its own distinct block, use triple backticks.

```markdown
Some basic Git commands are:
```
git status
git add
git commit
```
```

#### Links

You can create an inline link by wrapping link text in brackets `[ ]`, and then wrapping the URL in parentheses `( )`.

```markdown
This site was built using [GitHub Pages](https://pages.github.com/).
```

**Section links:** You can link directly to a section in a rendered file by hovering over the section heading to expose the link.

**Relative links:** You can define relative links and image paths in your rendered files to help readers navigate to other files in your repository.

**Custom anchors:** GitHub automatically generates anchors for headings. Custom anchors are not supported.

#### Line Breaks

You can create a new line by ending a line with two or more spaces, and then typing return.

#### Images

You can display an image by adding `!` and wrapping the alt text in `[ ]`. Then wrap the link for the image in parentheses `()`.

```markdown
![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](https://myoctocat.com/assets/images/base-octocat.svg)
```

#### Lists

You can make an unordered list by preceding one or more lines of text with `-`, `*`, or `+`.

```markdown
- George Washington
- John Adams
- Thomas Jefferson
```

To order your list, precede each line with a number.

```markdown
1. First list item
2. Second list item
3. Third list item
```

You can create nested lists by indenting list items by two spaces.

```markdown
1. First list item
   - First nested list item
     - Second nested list item
```

#### Task Lists

To create a task list, preface list items with a hyphen and space followed by `[ ]`. To mark a task as complete, use `[x]`.

```markdown
- [x] #739
- [ ] https://github.com/octo-org/octo-repo/issues/740
- [ ] Add delight to the experience when all tasks are complete :tada:
```

If a task list item description begins with a parenthesis, you'll need to escape it with `\`:

```markdown
- [ ] \(Optional) Open a followup issue
```

#### Mentioning People and Teams

You can mention a person or team on GitHub by typing `@` plus their username or team name. This will trigger a notification and bring their attention to the conversation.

```markdown
@github/support What do you think about these updates?
```

#### Referencing Issues and Pull Requests

You can bring up a list of suggested issues and pull requests within the repository by typing `#`. Type the issue or pull request number or title to filter the list, and then press either tab or enter to complete the highlighted result.

#### Using Emojis

You can add emoji to your writing by typing `:EMOJICODE:`, a colon followed by the name of the emoji.

```markdown
@octocat :+1: This PR looks great - it's ready to merge! :shipit:
```

Typing `:` will bring up a list of suggested emoji. The list will filter as you type, so once you find the emoji you're looking for, press **Tab** or **Enter** to complete the highlighted result.

#### Paragraphs

You can create a new paragraph by leaving a blank line between lines of text.

#### Footnotes

You can add footnotes to your content by using this bracket syntax:

```markdown
Here is a simple footnote[^1].

A footnote can also have multiple lines[^2].

[^1]: My reference.
[^2]: To add line breaks within a footnote, add 2 spaces to the end of a line.  
This is a second line.
```

#### Alerts

**Alerts**, also sometimes known as **callouts** or **admonitions**, are a Markdown extension based on the blockquote syntax that you can use to emphasize critical information. On GitHub, they are displayed with distinctive colors and icons to indicate the significance of the content.

Use alerts only when they are crucial for user success and limit them to one or two per article to prevent overloading the reader. Additionally, you should avoid placing alerts consecutively. Alerts cannot be nested within other elements.

To add an alert, use a special blockquote line specifying the alert type, followed by the alert information in a standard blockquote. Five types of alerts are available:

```markdown
> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.
```

#### Hiding Content with Comments

You can tell GitHub to hide content from the rendered Markdown by placing the content in an HTML comment.

```markdown
<!-- This content will not appear in the rendered Markdown -->
```

#### Ignoring Markdown Formatting

You can tell GitHub to ignore (or escape) Markdown formatting by using `\` before the Markdown character.

```markdown
Let's rename \*our-new-project\* to \*our-old-project\*.
```

**Note:** The Markdown formatting will not be ignored in the title of an issue or a pull request.

#### Disabling Markdown Rendering

When viewing a Markdown file, you can click **Code** at the top of the file to disable Markdown rendering and view the file's source instead.

Disabling Markdown rendering enables you to use source view features, such as line linking, which is not possible when viewing rendered Markdown files.

#### Further Reading

- [GitHub Flavored Markdown Spec](https://github.github.com/gfm/)
- [About writing and formatting on GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/about-writing-and-formatting-on-github)
- [Working with advanced formatting](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting)
- [Quickstart for writing on GitHub](https://docs.github.com/en/get-started/writing-on-github/quickstart-for-writing-on-github)
