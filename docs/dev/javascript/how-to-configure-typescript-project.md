---
title: How to Configure TypeScript Project
abstract: Comprehensive guide to initializing and configuring TypeScript projects for different use cases including libraries, CLI tools, and build systems.
type: how-to
---

# How to Configure TypeScript Project

## 📘 Purpose & Scope

This guide covers setting up TypeScript projects for different scenarios: libraries, CLI tools, and build systems. You'll learn when to use different build tools and how to configure them properly.

## Choosing the Right Setup Approach

### Frontend Projects → Use Vite
**When**: Building web applications, SPAs, or frontend-heavy projects
**Why**: Fast development server, excellent TypeScript support, modern tooling

**Setup Guide**: {{ link_with_abstract("how-to-configure-vite-typescript.md") }}

### Libraries → Use tsup or Rollup
**When**: Creating npm packages, reusable components, or libraries
**Why**: Optimized bundling, tree-shaking, multiple output formats

### CLI Applications → Use esbuild or tsc directly
**When**: Command-line tools, scripts, or Node.js applications
**Why**: Fast compilation, minimal dependencies, direct execution

## Manual TypeScript Compilation

For learning purposes or simple projects, you can use the TypeScript compiler directly:

**Tutorial**: {{ link_with_abstract("tutorial-typescript-compilation.md") }}

### Basic Setup

```bash
npm init -y
npm install -D typescript
npx tsc --init
```

### Essential tsconfig.json Options

```json
{
  "compilerOptions": {
    "target": "ES2020",           // Output JavaScript version
    "module": "ESNext",           // Module system
    "moduleResolution": "bundler", // How to resolve modules
    "strict": true,               // Enable all strict checks
    "esModuleInterop": true,      // Better CommonJS interop
    "skipLibCheck": true,         // Skip type checking .d.ts files
    "forceConsistentCasingInFileNames": true,
    "declaration": true,          // Generate .d.ts files
    "declarationMap": true,       // Source maps for .d.ts files
    "sourceMap": true,            // Generate source maps
    "outDir": "./dist",           // Output directory
    "rootDir": "./src"            // Source directory
  }
}
```

## Library Projects with tsup

### Setup

```bash
npm init -y
npm install -D tsup typescript
npm install -D @types/node
```

### Package.json Scripts

```json
{
  "scripts": {
    "build": "tsup",
    "dev": "tsup --watch",
    "type-check": "tsc --noEmit"
  }
}
```

### tsup Configuration

Create `tsup.config.ts`:

```typescript
import { defineConfig } from 'tsup'

export default defineConfig({
  entry: ['src/index.ts'],
  format: ['cjs', 'esm'],
  dts: true,
  splitting: false,
  sourcemap: true,
  clean: true,
})
```

### TypeScript Configuration for Libraries

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "declaration": true,
    "declarationMap": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "**/*.test.ts"]
}
```

## CLI Applications with esbuild

### Setup

```bash
npm init -y
npm install -D esbuild typescript @types/node
```

### Build Script

Create `build.js`:

```javascript
const esbuild = require('esbuild')

esbuild.build({
  entryPoints: ['src/index.ts'],
  bundle: true,
  platform: 'node',
  target: 'node16',
  outfile: 'dist/index.js',
  format: 'cjs',
  sourcemap: true,
}).catch(() => process.exit(1))
```

### Package.json Scripts

```json
{
  "scripts": {
    "build": "node build.js",
    "dev": "node build.js --watch",
    "start": "node dist/index.js"
  }
}
```

## tsconfig.json Configuration

### Understanding Compilation Context

The *compilation context* defines what TypeScript compiles and how:

- **Files to compile**: Specified via `include`, `exclude`, or `files`
- **Compiler options**: Target JS version, module system, strictness settings

### File Inclusion Patterns

Use `include` and `exclude` for flexible file selection:

```json
{
  "include": [
    "./src/**/*"
  ],
  "exclude": [
    "./src/**/*.spec.ts",
    "./src/**/*.test.ts",
    "./node_modules"
  ]
}
```

### Glob Patterns

- `**/*` means all folders and files
- TypeScript assumes `.ts`/`.tsx` extensions
- Use `allowJs: true` to include `.js`/`.jsx` files

### Essential Compiler Options

```json
{
  "compilerOptions": {
    "target": "ES2020",           // Output JavaScript version
    "module": "ESNext",           // Module system
    "moduleResolution": "bundler", // How to resolve modules
    "strict": true,               // Enable all strict checks
    "esModuleInterop": true,      // Better CommonJS interop
    "skipLibCheck": true,         // Skip type checking .d.ts files
    "forceConsistentCasingInFileNames": true,
    "declaration": true,          // Generate .d.ts files
    "declarationMap": true,       // Source maps for .d.ts files
    "sourceMap": true,            // Generate source maps
    "outDir": "./dist",           // Output directory
    "rootDir": "./src"            // Source directory
  }
}
```

### Project References

For monorepos or complex projects:

```json
{
  "references": [
    { "path": "./packages/core" },
    { "path": "./packages/ui" }
  ]
}
```

## Development Workflow

### Type Checking

```bash
# Check types without emitting files
tsc --noEmit

# Watch mode for continuous checking
tsc --noEmit --watch
```

### Building

```bash
# Standard TypeScript compilation
tsc

# With specific config
tsc --project tsconfig.prod.json
```

### Testing Setup

For projects with tests:

```json
{
  "exclude": [
    "node_modules",
    "dist",
    "**/*.spec.ts",
    "**/*.test.ts"
  ]
}
```

## Best Practices

### File Organization

```
src/
├── index.ts          # Main entry point
├── types/            # Type definitions
├── utils/            # Utility functions
└── components/       # Reusable components
```

### Configuration Management

- Use separate configs for development and production
- Leverage `extends` for shared configurations
- Keep build-specific options in build tools (Vite, tsup, etc.)

### Performance Optimization

- Use `skipLibCheck: true` for faster compilation
- Enable `incremental: true` for faster rebuilds
- Use project references for large codebases

## References

- [TypeScript Project Configuration](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html)
- [tsup Documentation](https://tsup.egoist.sh/)
- [esbuild TypeScript](https://esbuild.github.io/content-types/#typescript)
