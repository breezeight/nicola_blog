---
title: How to Configure VS Code for TypeScript
abstract: Step-by-step guide to setting up VS Code with TypeScript extensions and TSServer integration for optimal development experience.
type: how-to
---

# How to Configure VS Code for TypeScript

## 📘 Purpose & Scope

This guide walks you through configuring VS Code for optimal TypeScript development, including essential extensions, TSServer integration, and practical techniques for leveraging type inference inspection.

## Essential Extensions

### Total TypeScript Extension

**Installation**: Search for "Total TypeScript" in VS Code Extensions marketplace

**Description**: Learn TypeScript in VSCode with a TypeScript error translator and syntax guide.

**VS Marketplace Link**: [https://marketplace.visualstudio.com/items?itemName=mattpocock.ts-error-translator](https://marketplace.visualstudio.com/items?itemName=mattpocock.ts-error-translator)

This extension provides:
- Clear error explanations
- Interactive TypeScript learning
- Syntax guidance

### Additional Recommended Extensions

For a comprehensive setup, consider these extensions:
- **TypeScript Importer**: Auto-imports TypeScript modules
- **Bracket Pair Colorizer**: Improves code readability
- **Error Lens**: Shows errors inline
- **TypeScript Hero**: Advanced TypeScript utilities

Reference: [9 Essential VS Code Extensions for TypeScript](https://blog.logrocket.com/9-essential-vs-code-extensions-typescript/)

## TSServer Integration

VS Code has excellent built-in TypeScript support through TSServer, the TypeScript standalone server. It provides:

- **Autocomplete**: Intelligent code completion
- **Inspection**: Real-time type checking and error detection
- **Navigation**: "Go to Definition" feature (F12 or right-click)
- **Refactoring**: Safe code transformations

### Type Inference Inspection

One of the most powerful features is seeing inferred types on hover. This helps build confidence in TypeScript's type system:

#### 1. Type Narrowing in Conditionals

```typescript
function logMessage(message: string | null) {
  if (message) { // Hover: message is now type 'string'
    console.log(message);
  }
} // Hover: function type is (message: string | null) => void
```

#### 2. Object Property Inspection

```typescript
const foo = {
  x: [1, 2, 3], // Hover: (property) x: number[]
  bar: {
    name: 'Fred'
  }
};
// Hover: foo type is { x: number[]; bar: { name: string } }
```

#### 3. Generic Type Inference

```typescript
function restOfPath(path: string) {
  return path.split("/").slice(1).join("/");
  // Hover: Array<string>.slice() returns string[]
} // Hover: function type is (path: string) => string
```

## VS Code Settings for TypeScript

### Recommended Settings

Add these to your VS Code `settings.json`:

```json
{
  "typescript.preferences.includePackageJsonAutoImports": "auto",
  "typescript.suggest.autoImports": true,
  "typescript.updateImportsOnFileMove.enabled": "always",
  "typescript.preferences.importModuleSpecifier": "relative",
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  }
}
```

### Workspace Configuration

For project-specific settings, create `.vscode/settings.json`:

```json
{
  "typescript.preferences.includePackageJsonAutoImports": "on",
  "typescript.suggest.completeFunctionCalls": true
}
```

## Practical Tips

### Using Type Inspection Effectively

1. **Hover over variables** to see their inferred types
2. **Use Ctrl+Space** for autocomplete suggestions
3. **Right-click → Go to Definition** (F12) for navigation
4. **Ctrl+Shift+P → TypeScript: Restart TS Server** if issues arise

### Debugging Type Issues

1. Enable TypeScript errors in Problems panel
2. Use the TypeScript output channel for detailed logs
3. Restart TSServer when configuration changes

## References

- [VS Code TypeScript Documentation](https://code.visualstudio.com/docs/languages/typescript)
- [TypeScript Error Translator](https://marketplace.visualstudio.com/items?itemName=mattpocock.ts-error-translator)
- [Essential VS Code Extensions for TypeScript](https://blog.logrocket.com/9-essential-vs-code-extensions-typescript/)
