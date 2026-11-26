---
title: Intro to Nix Course
description: >
  Course taxonomy, competency matrix, ESCO-style learning outcomes, and modular syllabus
  for an introductory Nix track.
abstract: >
  Structured outline of an intro Nix course: skill taxonomy, certification-style competency
  levels, learning outcomes, and eight-module syllabus with links to slide decks.
type: tutorial, explanation
---

# Intro to Nix Course

##  CV Skill Taxonomy (Nix)

Slides: [Course intro](https://docs.google.com/presentation/d/1Z55_tI26B76XUQcYt9M6g63n0yI-Q320L93H940Q20)

### What is a Taxonomy

We are going to quickly see the course taxonomy: a structured way to organize what you will learn, grouping concepts, skills, and tools so you can clearly see how everything fits together.

A **taxonomy** is just a way to **organize things into clear groups so they are easy to understand**.

If you had to explain it very simply:

> It’s like sorting everything in your kitchen:
> fruits in one basket, vegetables in another, spices in a drawer.
> You’re not changing anything — you’re just **putting order so you can find and understand things quickly**.

---

Applied to a course:

> “This is the course taxonomy” means:
> **this is how we group together what you will learn**, grouping skills and topics so everything is clear and structured.

---

### The Nix Taxonomy

**Domain:** DevOps / Infrastructure as Code / Reproducible Systems

**Core Areas**
- Nix language (DSL, expressions, functions)
- Nix package manager (CLI, builds, store)
- Flakes (inputs/outputs, project structuring)
- Dev environments (`mkShell`, `nix develop`)
- Package definition (`mkDerivation`)
- System configuration (nix-darwin / NixOS)
- User environment (Home Manager)

**Practices**
- Declarative configuration
- Reproducible builds
- Dependency closure reasoning
- Binary cache usage

**Tools & Commands**
- `nix search`, `nix run`, `nix shell`, `nix develop`, `nix build`
- `nix eval`, `nix repl`
- `nix profile` (ad-hoc usage awareness)

---

### Certification-Style Competency Matrix (Nix)

| Area                 | Beginner                    | Intermediate                          | Advanced                                      |
|----------------------|-----------------------------|---------------------------------------|-----------------------------------------------|
| Concepts             | Understand Nix components   | Explain reproducibility & store       | Design system architecture with Nix           |
| CLI Usage            | Run/search/build packages   | Use shells and dev environments       | Optimize workflows and caching                |
| Nix Language         | Read basic expressions      | Write functions and configs           | Build reusable abstractions                   |
| Flakes               | Use existing flakes         | Create simple flakes                  | Architect multi-output, multi-system flakes   |
| Dev Environments     | Enter `nix shell`           | Create `mkShell` setups               | Compose complex multi-env workflows           |
| Packaging            | Build existing packages     | Modify derivations                    | Author and maintain custom packages           |
| System Configuration | Use nix-darwin / NixOS      | Configure system/user environments    | Design full declarative infra setups          |
| Best Practices       | Avoid basic mistakes        | Use declarative approach consistently | Enforce reproducibility across teams/projects |
| Dependency Reasoning | Basic awareness             | Understand closures                   | Debug and optimize dependency graphs          |

**Certification outcome:**  
Ability to design, implement, and maintain reproducible development and system environments using Nix across different setup combinations.



## Lesson 0

[Breezeight Version of NixCon 2025 - Getting Started with Nix: Common Mistakes and How to Dodge Them](https://docs.google.com/presentation/d/1i0HjWPlNErlPEEaYzzuj8gF0R9JZ0TRpAtKk7o2uPf4)

## ESCO-style learning outcomes for Nix

**Knowledge**
- Nix = language (DSL), package manager, and OS (NixOS)
- Declarative + reproducible systems (Nix store, hashing, binary cache)
- Ecosystem basics: nixpkgs, flakes, dev environments, Home Manager, nix-darwin

**Skills**
- Use core commands: `nix search`, `nix run`, `nix shell`, `nix develop`, `nix build`
- Write Nix expressions (attrs, lists, functions, `let`)
- Create dev environments with `mkShell`
- Use flakes (`flake.nix`, `flake.lock`)
- Build/customize packages (`mkDerivation`)
- Evaluate/debug with `nix eval` / `nix repl`

**Competences**
- Choose correct setup (standalone, nix-darwin, NixOS, +/− Home Manager)
- Design reproducible environments
- Distinguish declarative vs ad-hoc (`nix profile`)
- Structure projects with flakes
- Reason about dependencies and closures

**Outcome**
- Configure and manage reproducible environments using Nix, selecting appropriate setups and applying declarative principles.

### Lessson 0 - Training Syllabus (Nix)

**Module 1 — Foundations**
- What is Nix (language, package manager, OS)
- Declarative vs imperative model
- Nix store and reproducibility

**Module 2 — Basic CLI**
- Searching, running, and building packages
- Temporary environments (`nix run`, `nix shell`)
- Intro to `nix profile` (and limitations)

**Module 3 — Nix Language**
- Syntax: attributes, lists, functions
- `let ... in`, interpolation
- Evaluation tools (`nix eval`, `nix repl`)

**Module 4 — Flakes**
- Structure: `flake.nix`, `flake.lock`
- Inputs/outputs model
- Building and running flake outputs

**Module 5 — Dev Environments**
- `mkShell`
- Multi-language environments
- `nix develop` workflows

**Module 6 — Packaging**
- `mkDerivation`
- Fetching sources
- Basic customization

**Module 7 — System & User Config**
- nix-darwin / NixOS overview
- Home Manager
- Composition patterns

**Module 8 — Best Practices**
- Declarative setups vs ad-hoc installs
- Common mistakes
- Choosing the right architecture


## Lesson Garbage Collection


nix config show | grep -i gc
gc-reserved-space = 8388608
nix store gc --dry-run


add nix.gc to darwin config

```
 84 +            # Garbage collection via launchd (since nix.gc requires nix.enable = true)
 85 +            launchd.daemons.nix-gc = {
 86 +              script = ''
 87 +                /nix/var/nix/profiles/default/bin/nix-collect-garbage --delete-older-than 30d
 88 +              '';
 89 +              serviceConfig = {
 90 +                RunAtLoad = false;
 91 +                StartCalendarInterval = [{ Weekday = 0; Hour = 3; Minute = 0; }];  # Sunday 3am
 92 +                StandardOutPath = "/var/log/nix-gc.log";
 93 +                StandardErrorPath = "/var/log/nix-gc.log";
 94 +              };
 95 +            };
```




## Lesson XYZ

Explanation:



Tutorial: Package a CLI written in python, another in TS (https://github.com/alexfazio/hermes-fly/tree/main), another in GO


You can try filtering all GitHub repositories with a package.json file with a keyword like this: next-mdx-enhanced path:package.json
commander path:package.json


commander path:package.json stars:>100

https://github.com/search/advanced

Find established repositories with more than 100 stars.
https://www.reddit.com/r/github/comments/1hx7iej/how_can_i_find_github_repositories_with_more_than/


https://github.com/NixOS/nixpkgs/blob/master/pkgs/README.md#quick-start-to-adding-a-package


Flake Packaging for small projects: 
claude "nixify this repo to make it easy to be included in another repo based on nix":
- explore the codebase to understand its structure and what needs to be packaged for Nix

 ● What outputs do you need from the flake?
   → 1 + devenv.sh config....
 ● Which Node.js version should be used?
   → Node.js 22 (Recommended)
 ● Should the flake provide an overlay for easy integration?
   → What is an overlay?


Execution Steps:

 1. Create flake.nix with:
   - nixpkgs, flake-utils, devenv inputs
   - buildNpmPackage for the CLI
   - devShell using devenv
   - overlay for composition
 2. Run nix flake lock to generate flake.lock
 3. Compute npmDepsHash by running build (Nix will tell us the correct hash)
 4. Create devenv.nix with Node.js 22 and dev tools
 5. Create .envrc for direnv integration
 6. Test with:
   - nix build - verify package builds
   - nix develop - verify devShell works
   - nix flake check - verify flake is valid

Files Modified/Created:

 - Create: flake.nix
 - Create: devenv.nix
 - Create: .envrc
 - Create: flake.lock (auto-generated)
 - Update: .gitignore (add .direnv/, .devenv/, .devenv.flake.nix)


Persona di OpenAI

Sergio:
- Progetto unique value prop => unica banca 
- Progetto AI interno, un buddy per ogni persona