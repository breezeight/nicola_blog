# Linking Between Pages

The site is built with Zensical, which reads `mkdocs.yml`. Link pages with **plain, relative Markdown links**, so the same files work on GitHub, in Obsidian and in any editor.

### Index pages: title + abstract

Index pages list each linked page with its title and a one-line abstract, written as static text:

```markdown
- [Tutorial - Organizing Go Code](go-organizing-code.md): Develop a simple Go package inside a module and use the go tool to fetch, build and install it.
```

- Use the target page's `title` from its front matter as the link text.
- Follow it with `: ` and a short abstract (1–2 sentences), usually the page's `abstract`.
- Paths are relative to the current page (`../other-folder/page.md` is fine).

### Do not use

- `{{ link_with_abstract(...) }}` — removed. It needed the current page from the macros environment, which Zensical does not provide.
- Wikilinks (`[[Page]]`) or embeds (`![[image.png]]`) — not rendered.
- Absolute site URLs for internal pages.

### Checking links

`just check` builds the site and reports links whose target page or anchor does not exist. Run it after moving or renaming files.

## Available Macros

`main.py` still defines one macro (the macros plugin is enabled in `mkdocs.yml` with `module_name: main`):

### `github_code_ref(repo_path, start_line=None, end_line=None, language="c")`
Creates a GitHub code reference with optional line highlighting.

```markdown
{{ github_code_ref("/ruby/ruby/blob/v2_2_0_preview2/include/ruby/ruby.h", 771, 774) }}
```

Pages that show `{{ ... }}` literally (for example Helm templates) must disable macros in their front matter:

```yaml
---
render_macros: false
---
```

## Front Matter

Pages should include a `title` and an `abstract`; index pages reuse them as link text and description:

```yaml
---
title: Page Title
abstract: >
  Brief description of the page content, reused in index pages.
---
```
