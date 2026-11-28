# nik-kh Knowledge Hub Constitution

## Core Principles

### I. Portable Plain-Markdown Content

Content in `docs/` MUST stay readable and navigable outside the site generator (GitHub,
Obsidian, any editor).

- Internal links MUST be relative Markdown links to `.md` files; absolute site URLs, wikilinks
  (`[[Page]]`) and embeds (`![[file]]`) MUST NOT be used.
- Every page MUST have `title` and `abstract` in its front matter; index pages list linked pages
  as `[Title](path.md): abstract` written as static text.
- Macros are limited to those defined in `main.py` (currently `github_code_ref`). Pages that
  show literal `{{ ... }}` MUST set `render_macros: false`.

Rationale: link macros that depended on generator internals broke during the Zensical migration;
plain Markdown survives tool changes.

### II. The Strict Build Is Always Green

`zensical build --clean --strict` MUST pass on every commit that reaches `develop` or `main`.

- Broken links, missing anchors and macro errors are failures, not warnings.
- The pre-commit hook (`.githooks/pre-commit`) and the GitHub Actions `build` job enforce this;
  `--no-verify` is allowed only for commits that do not touch `docs/`, `mkdocs.yml` or `main.py`,
  or as a stop-gap fixed in the same branch before merge.
- Moving or renaming a page MUST update every link to it in the same change.

Rationale: a zero-warning baseline is the only way new breakage stays visible.

### III. Private by Default

The published site is personal and MUST NOT be reachable without authentication.

- Every hostname that serves the site (`nik-kh.pages.dev`, `*.nik-kh.pages.dev`, and any future
  custom domain) MUST be covered by a Cloudflare Access application before content is deployed
  to it.
- Automated deploys run only from `main` and only while the repository variable
  `CLOUDFLARE_PAGES_DEPLOY` is `true`; it MUST be turned off if Access protection is ever removed.
- Secrets (API tokens, account IDs) MUST live in GitHub secrets or local environment variables,
  never in the repository or in chat transcripts. Tokens MUST carry only the permissions their
  job needs.

Rationale: the content mixes notes that are not meant to be public; one unprotected deploy is
enough to leak them.

### IV. Reproducible, Minimal Tooling

- Python tooling MUST be managed with `uv`; the Zensical version is pinned by `uv.lock` and CI
  MUST build with that exact version.
- CI MUST NOT depend on paths that exist only on the author's machine (e.g. the local `ad-docs`
  dependency).
- Common tasks MUST be exposed as `just` recipes and documented in `DEVELOPMENT.md`.
- New tools or dependencies MUST solve a concrete, current problem; prefer configuration of
  existing tools over adding new ones.

Rationale: a docs site should build identically on a laptop and in CI with as few moving parts
as possible.

### V. Process Proportional to Change

- Changes to tooling, build, CI, deployment or site structure SHOULD go through the Spec Kit
  flow (`specify` → `plan` → `tasks` → `implement`).
- Writing or editing content pages does NOT require a spec; Principles I and II still apply.
- Every change MUST be the simplest one that meets its goal; complexity MUST be justified in
  the plan.

Rationale: this is primarily a content repository; heavyweight process belongs where mistakes are
expensive.

### VI. Every Page Has One Diátaxis Type

- Every page in `docs/` MUST be exactly one of: tutorial, how-to guide, reference, explanation,
  following `guidelines/content/diataxis.md`; its name and tone MUST match that type (for example
  `*-howto.md`, `*-explanation.md`, `*-index.md` for references).
- Content that mixes types MUST be split into separate pages that link to each other.
- Plans that add or restructure pages MUST state the type of each page.

Rationale: a predictable type tells the reader what to expect and keeps reference material free of
narrative, and narrative free of exhaustive detail.

## Technology and Deployment Constraints

- Site generator: Zensical, configured through `mkdocs.yml`; content lives in `docs/`.
- Hosting: Cloudflare Pages project `nik-kh`, direct upload from GitHub Actions
  (`cloudflare/wrangler-action`); no Cloudflare Git integration.
- Authentication: Cloudflare Zero Trust team `brisotto`, One-time PIN login, reusable Allow policy
  listing permitted emails. Access is managed with the `cf` CLI or the API, as documented in
  `DEVELOPMENT.md`.
- Manual deploys (`just deploy`) publish previews unless `main` is passed explicitly.

## Development Workflow

- `develop` is the integration branch; `main` is the production branch and only receives
  fast-forwards or merges from `develop`.
- Work happens on topic branches merged into `develop` through pull requests with merge commits;
  the `build` check MUST pass before merge.
- Commits are signed; signing failures MUST be resolved, not bypassed.
- A work session ends only when its commits are pushed (see `AGENTS.md`, "Session completion").

## Governance

- This constitution takes precedence over other practice documents. `DEVELOPMENT.md`,
  `AGENTS.md`, `CONTENT.md` and `guidelines/` provide runtime guidance and MUST NOT contradict it.
- Amendments are made with `/speckit-constitution` in a pull request that states the reason and
  updates dependent guidance files in the same change.
- Versioning follows semantic versioning: MAJOR for removed or redefined principles, MINOR for
  new principles or materially expanded guidance, PATCH for clarifications.
- Plans and reviews MUST check compliance with these principles; deviations MUST be recorded in
  the plan's complexity tracking with a justification.

**Version**: 1.1.0 | **Ratified**: 2026-11-26 | **Last Amended**: 2026-11-28
