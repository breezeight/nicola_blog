# Development Guide

This documentation site is built with [Zensical](https://zensical.org/), the successor to Material for MkDocs. Zensical reads the existing `mkdocs.yml`, so the configuration format is unchanged. Python dependencies are managed with [uv](https://docs.astral.sh/uv/), and common tasks run through [just](https://github.com/casey/just).

## Prerequisites

- Python 3.12+
- uv
- just (optional, for convenience commands)

## Setup

```bash
just install   # uv sync + enable the git hooks
```

## Running the Site

```bash
just serve              # http://127.0.0.1:8000
just serve 8080         # custom port
just serve-external     # listen on 0.0.0.0:8001 (reachable from other devices)
just dev                # uv sync + serve
```

## Building and Validating

```bash
just build          # uv run zensical build --clean
just check          # build and report broken links and missing anchors
just check-strict   # build with --strict (aborts on warnings)
just clean          # remove site/ and .cache/
```

Run `just check` after moving or renaming pages: it reports every link whose target page or anchor no longer exists. `just check-strict` fails on any warning.

## Automatic Checks

The same strict build (`zensical build --clean --strict`) runs in two places, so broken links and missing anchors can't land:

- **Pre-commit hook** — [.githooks/pre-commit](.githooks/pre-commit) runs when a commit touches `docs/`, `mkdocs.yml` or `main.py`, and blocks the commit if the build has warnings. Enable it once per clone with `just install-hooks` (`just install` does it too); it sets `git config core.hooksPath .githooks`. Skip it for a single commit with `git commit --no-verify`.
- **GitHub Actions** — [.github/workflows/docs-check.yml](.github/workflows/docs-check.yml) runs on pushes to `develop` and `main`, on every pull request, and on demand. Because `pyproject.toml` contains a local-path dependency (`ad-docs`) that only exists on the author's machine, CI doesn't run `uv sync`: it installs only Zensical, at the version pinned in `uv.lock`.

## Available Just Commands

The root `justfile` imports `justfile.zensical`, which holds the site recipes. Run `just` with no arguments to list them all.

| Command | What it does |
|---------|--------------|
| `just install` | Install Python dependencies (`uv sync`) and enable the git hooks |
| `just install-hooks` | Enable the git hooks only |
| `just serve [port]` | Start the development server |
| `just serve-external` | Start the server on all interfaces |
| `just build` | Build the site into `site/` |
| `just check` / `just check-strict` | Validate the build |
| `just update` | Upgrade dependencies (`uv sync --upgrade`) |
| `just deps` | Show installed Python packages |
| `just clean` | Remove build artifacts |
| `just dev [port]` | Install and serve |
| `just deploy [branch]` | Manual deploy to Cloudflare Pages (preview by default; `main` = production) |

## Configuration

- **`mkdocs.yml`** — site configuration, theme, Markdown extensions, plugins and the `nav` tree. When you move or rename a page, update its `nav` entry too.
- **`.mkdocsignore`** — legacy files excluded from the build.
- **`.cache/`** — Zensical build cache (git-ignored).
- **`pyproject.toml`** / **`uv.lock`** — Python dependencies.

Plugins configured in `mkdocs.yml`, all implemented natively by Zensical:

- `search`
- `tags` — tags from page front matter, listed on [docs/tags.md](docs/tags.md)
- `gh-admonitions` — renders GitHub-style alerts (`> [!NOTE]`, `> [!WARNING]`, …) as admonitions
- `macros` — loads macros from `main.py`

## Links and Macros

Link pages with plain, relative Markdown links. Index pages add the target's title and a one-line abstract as static text:

```markdown
- [How-to: Pull images in K8S clusters from Amazon ECR](k8s-registry-auth-howto.md): Pull ECR images from EKS and non-AWS clusters.
```

The former `link_with_abstract` macro has been removed: Zensical's macros environment does not expose the current page, so relative paths could not be resolved. Plain links also work on GitHub and in Obsidian. See [the linking rule](.cursor/rules/content-guidelines-linking.mdc).

`main.py` still defines `github_code_ref(repo_path, start_line, end_line, language)`, which renders a link to lines in a GitHub repository. Pages that contain literal `{{ ... }}` (for example Helm templates) need `render_macros: false` in their front matter.

## Tags

Add tags in the page front matter:

```yaml
---
tags:
  - content/howto
  - tech/kubernetes
---
```

Tagged pages are listed on the [Tags](docs/tags.md) page.

## Project Structure

```
.
├── docs/                 # Documentation source (Markdown)
│   ├── dev/              # Technical notes, grouped by topic (aws/, kubernetes/, nix/, ...)
│   ├── nicola-routines/  # Personal routines system
│   ├── images/           # Images
│   ├── stylesheets/      # extra.css
│   ├── index.md          # Home page
│   └── tags.md           # Tags index
├── .cursor/rules/        # Cursor rules (content guidelines, MkDocs conventions)
├── main.py               # Macros (github_code_ref)
├── mkdocs.yml            # Site configuration (read by Zensical)
├── justfile              # Entry point, imports justfile.zensical
├── justfile.zensical     # Site recipes
├── pyproject.toml        # Python dependencies
└── site/                 # Generated site (build output)
```

## Contributing Content

Follow the content guidelines listed in [CONTENT.md](CONTENT.md). In short:

1. Classify each page using the Diátaxis framework (tutorial, how-to, reference, explanation) and name it accordingly (for example `*-howto.md`, `*-explanation.md`).
2. Use GitHub Flavored Markdown and GitHub-style alerts.
3. Add the page to `nav` in `mkdocs.yml` when it should appear in the navigation.
4. Use plain relative Markdown links (no `[[wikilinks]]`).
5. Preview with `just serve` and validate with `just check`.

## Deployment

The site is deployed to [Cloudflare Pages](https://developers.cloudflare.com/pages/) and protected with [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/applications/), so only allowed people can open it.

- **Production branch:** `main`. GitHub Actions builds the site and, on every push to `main`, uploads `site/` with `wrangler pages deploy` (job `deploy` in [.github/workflows/docs-check.yml](.github/workflows/docs-check.yml)).
- **Safety switch:** the deploy job runs only when the repository variable `CLOUDFLARE_PAGES_DEPLOY` is `true`. Turn it on only after Access protects the domain, so the site is never published unprotected.
- **Manual deploy:** `just deploy` publishes a preview (`just deploy main` publishes production). It needs `npx wrangler login` once.

### One-time setup

Do these steps in order. The site must be protected before the first deployment.

1. **Create the Pages project** (direct upload, no Git integration: GitHub Actions does the build):
   ```bash
   npx wrangler login
   npx wrangler pages project create nik-kh --production-branch main
   ```
   Production URL: `https://nik-kh.pages.dev`.
2. **Set up Cloudflare Zero Trust**: in the dashboard open *Zero Trust*, pick a team name and the Free plan (up to 50 users).
3. **Protect the site with Access**: *Zero Trust → Access → Applications → Add an application → Self-hosted*.
   - Destinations: `nik-kh.pages.dev` and `*.nik-kh.pages.dev` (the wildcard covers preview deployments).
   - Policy: action *Allow*, include *Emails* with the addresses allowed to read the site.
   - Login method: *One-time PIN* (code by email) works out of the box; GitHub or Google can be added under *Settings → Authentication*.
4. **Create an API token**: *My Profile → API Tokens → Create Token → Custom token*, permission *Account → Cloudflare Pages → Edit*.
5. **Add GitHub secrets and variables** (*Settings → Secrets and variables → Actions*):
   - Secret `CLOUDFLARE_API_TOKEN`: the token from step 4.
   - Secret `CLOUDFLARE_ACCOUNT_ID`: shown in the dashboard under *Workers & Pages*.
   - Variable `CLOUDFLARE_PAGES_PROJECT`: optional, defaults to `nik-kh`.
   - Variable `CLOUDFLARE_PAGES_DEPLOY` = `true`: set this last, after checking step 3.
6. **Deploy**: merge `develop` into `main` and push. Then open `https://nik-kh.pages.dev` in a private window: it must ask for the Cloudflare Access login.
