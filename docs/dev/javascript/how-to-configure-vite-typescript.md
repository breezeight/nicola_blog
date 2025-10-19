---
title: How to Configure Vite with TypeScript
abstract: Step-by-step guide to setting up Vite projects with TypeScript for modern frontend development with fast HMR and optimized builds.
type: how-to
---

# How to Configure Vite with TypeScript

## 📘 Purpose & Scope

This guide covers setting up Vite projects with TypeScript for frontend applications. Vite provides fast development server, excellent TypeScript support, and modern tooling for web applications.

## Quick Setup

### Create New Vite Project

```bash
# Create new Vite project with TypeScript
npm create vite@latest my-app -- --template vanilla-ts
cd my-app
npm install
```

### Some of the Available Templates

- `vanilla-ts` - Vanilla JavaScript with TypeScript
- `vue-ts` - Vue.js with TypeScript
- `react-ts` - React with TypeScript
- `preact-ts` - Preact with TypeScript
- `lit-ts` - Lit with TypeScript
- `svelte-ts` - Svelte with TypeScript

## Manual Setup

### Initialize Project

```bash
npm init -y
npm install -D vite typescript @types/node
npm install -D @vitejs/plugin-react # for React projects
```

### Vite Configuration

Create `vite.config.ts`:

```typescript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  build: {
    target: 'esnext',
    minify: 'esbuild'
  }
})
```

### TypeScript Configuration

Create `tsconfig.json`:

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
```

### tsconfig.node.json

Create `tsconfig.node.json` for Vite configuration:

```json
{
  "compilerOptions": {
    "composite": true,
    "skipLibCheck": true,
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true
  },
  "include": ["vite.config.ts"]
}
```

## Development Workflow

### Start Development Server

```bash
npm run dev
```

### Build for Production

```bash
npm run build
```

### Preview Production Build

```bash
npm run preview
```

## Advanced Configuration

### Environment Variables

Create `.env` files:

```bash
# .env
VITE_API_URL=https://api.example.com
VITE_APP_TITLE=My App
```

Use in TypeScript:

```typescript
const apiUrl = import.meta.env.VITE_API_URL
const appTitle = import.meta.env.VITE_APP_TITLE
```

### Custom Plugins

```typescript
import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
  plugins: [/* your plugins */],
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src'),
      '@components': resolve(__dirname, 'src/components'),
    }
  },
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          utils: ['lodash', 'date-fns']
        }
      }
    }
  }
})
```

## Best Practices

### File Organization

```
src/
├── main.tsx          # Entry point
├── App.tsx           # Main component
├── components/        # Reusable components
├── hooks/            # Custom hooks
├── utils/            # Utility functions
├── types/            # Type definitions
└── assets/           # Static assets
```

### Type Safety

- Use strict TypeScript configuration
- Enable `noUnusedLocals` and `noUnusedParameters`
- Use proper type definitions for environment variables
- Leverage Vite's built-in TypeScript support

### Performance

- Use dynamic imports for code splitting
- Configure manual chunks for vendor libraries
- Optimize asset loading with proper formats

## References

- [Vite TypeScript Guide](https://vitejs.dev/guide/features.html#typescript)
- [Vite Configuration Reference](https://vitejs.dev/config/)
- [TypeScript Project Configuration](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html)
