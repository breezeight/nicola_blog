## Mkdocs

https://www.mkdocs.org/getting-started/

This project uses `uv` for dependency management instead of Poetry.

### Setup

Install dependencies:
```bash
uv sync
```

### Development

Preview your site:
```bash
uv run mkdocs serve
uv run mkdocs serve --dev-addr=0.0.0.0:8001
```

Open `http://localhost:8000` in your browser

### Building

Build the site:
```bash
uv run mkdocs build
```

## Markdown Conventions and Editing Tips 
 
For images and vscode see: [docs/dev/markdown-editing-tools.md](docs/dev/markdown-editing-tools.md)


Tips to move a page from one location to another in the docs and keep all the images in the same relative path.

### Use the AD internal docs cli to move and update the links

See [ADDICTIVE/ad-internal-docs-cli](https://github.com/addictivedev/ad-internal-docs-cli) for more details.
