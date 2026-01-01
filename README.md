## Mkdocs

https://www.mkdocs.org/getting-started/

### Quick Start

Install dependencies and start the development server:

```bash
just install
just serve
```

Open `http://localhost:8000` in your browser

### Development

TODO review the development guide

## Task Management

This project uses ClickUp for task management via the MCP server. Tasks are automatically created in the configured ClickUp list. The default list and integration settings are configured in [`.cursor/clickup-config.json`](.cursor/clickup-config.json). For details on how the ClickUp integration works, see [`.cursor/rules/clickup-integration.mdc`](.cursor/rules/clickup-integration.mdc).

### Finding Tasks in ClickUp

To locate tasks created for this project in the ClickUp web interface:

1. Navigate to the **"Nicola Personal"** workspace
2. Open the **"Nicola Personal"** space
3. Find the list named **"Nicola Nix Config"** (or use ClickUp search: Cmd/Ctrl + K)
4. **Direct link**: [https://app.clickup.com/2194902/v/l/li/901519282810](https://app.clickup.com/2194902/v/l/li/901519282810)

## Content Guidelines

SEE [CONTENT GUIDELINES](CONTENT.md) for more details.

This project follows structured content guidelines to maintain consistency and quality across all documentation:

### Core Guidelines
- **[Content Guidelines - Diátaxis Framework](.cursor/rules/content-guidelines-diataxis.mdc)** - Document classification and structure using the Diátaxis framework
- **[Content Guidelines - Cross-Language](.cursor/rules/content-guidelines-cross-language.mdc)** - Rules for cross-language documentation and comparison tables
- **[Content Guidelines - Language Structure](.cursor/rules/content-guidelines-language-structure.mdc)** - Standardized structure for programming language documentation

### Specialized Guidelines
- **[Content Guidelines - Linking](.cursor/rules/content-guidelines-linking.mdc)** - Dynamic content generation and cross-project linking with MkDocs macros
- **[Content Guidelines - TypeScript Docs](.cursor/rules/content-guidelines-typescript-docs.mdc)** - Specific guidelines for TypeScript documentation

### Development Guidelines
- **[MkDocs Development](.cursor/rules/mkdocs.mdc)** - Development workflow with uv package management and justfile commands
- **[MkDocs Theme Customization](.cursor/rules/mkdocs-theme-customization.mdc)** - Theme customization and styling guidelines

## Markdown Conventions and Editing Tips 
 
For images and vscode see: [docs/dev/markdown-editing-tools.md](docs/dev/markdown-editing-tools.md)


Tips to move a page from one location to another in the docs and keep all the images in the same relative path.

### Use the AD internal docs cli to move and update the links

See [ADDICTIVE/ad-internal-docs-cli](https://github.com/addictivedev/ad-internal-docs-cli) for more details.
