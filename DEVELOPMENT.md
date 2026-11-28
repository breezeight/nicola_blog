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

The former `link_with_abstract` macro has been removed: Zensical's macros environment does not expose the current page, so relative paths could not be resolved. Plain links also work on GitHub and in Obsidian. See [the linking rule](guidelines/content/linking.md).

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
├── guidelines/           # Content and site rules for humans and agents (index: CONTENT.md)
├── .cursor/rules/        # Cursor pointer rules (front matter + @guidelines/...)
├── .agents/skills/       # Agent skills: source (Codex reads it directly)
├── .claude/skills/       # Claude Code skills (symlinks to .agents/skills, plus speckit-*)
├── .specify/             # Spec Kit: constitution, templates, scripts
├── specs/                # Spec Kit feature specs, plans, tasks
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

## AI Agents Setup

Agent instructions live in [AGENTS.md](AGENTS.md): what each agent must read, where the skills are,
and which MCP servers to connect. This section explains how to set them up.

### Connect the MCP servers

The list of servers and their purpose is in the MCP table in [AGENTS.md](AGENTS.md#mcp-servers).

- **Claude Code**: servers such as ClickUp are claude.ai connectors. Connect them once in claude.ai
  under *Settings → Connectors*. If a session starts with a connector unauthenticated, run `/mcp`,
  pick the server (e.g. *claude.ai ClickUp*) and log in. `claude mcp list` shows the status.
- **Codex**: add and log in to each server (OAuth):
  ```bash
  codex mcp add clickup --url https://mcp.clickup.com/mcp
  codex mcp login clickup
  codex mcp list
  ```

### Skills

- Project skills have **one source**: `.agents/skills/<name>/SKILL.md`, which Codex reads.
- Claude Code reads `.claude/skills/`, where each project skill is a relative symlink:
  ```bash
  ln -s ../../.agents/skills/<name> .claude/skills/<name>
  ```
- `speckit-*` skills are installed by Spec Kit as separate copies in both folders. Do not edit them
  by hand; update them with the Specify CLI.
- To add a skill: create `.agents/skills/<name>/SKILL.md` (front matter `name` and `description`,
  then the instructions, in English), add the symlink, and list it in [AGENTS.md](AGENTS.md#skills).

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
2. **Set up Cloudflare Zero Trust**: in the dashboard open *Zero Trust*, pick a team name (ours: `brisotto`, login page `brisotto.cloudflareaccess.com`) and the Free plan (up to 50 users). Then add the *One-time PIN* login method (code by email): *Zero Trust → Integrations → Identity providers → Add new identity provider → One-time PIN*. New organizations do not have it by default.
3. **Protect the site with Access**, using the [`cf` CLI](https://developers.cloudflare.com/cf/). The dashboard form for self-hosted applications only lists domains in your own zones, so it cannot select `*.pages.dev`; the API accepts it.
   ```bash
   npx cf auth login                               # separate login from wrangler
   npx cf zero-trust identity-providers list       # note the id of the "onetimepin" provider

   # Reusable Allow policy: who may read the site
   npx cf zero-trust access policies create --body '{
     "name": "nik-kh: allow Nicola", "decision": "allow", "session_duration": "24h",
     "include": [{"email": {"email": "nicola@brisotto.me"}}]}'

   # One application for production and every preview deployment
   npx cf zero-trust access applications create --body '{
     "name": "nik-kh", "type": "self_hosted", "domain": "nik-kh.pages.dev",
     "destinations": [{"type": "public", "uri": "nik-kh.pages.dev"},
                      {"type": "public", "uri": "*.nik-kh.pages.dev"}],
     "allowed_idps": ["<one-time-pin id>"], "auto_redirect_to_identity": true,
     "session_duration": "24h", "policies": [{"id": "<policy id>", "precedence": 1}]}'
   ```
   To allow more people, add `{"email": {"email": "..."}}` entries to the policy with `npx cf zero-trust access policies update`.
   Check: `curl -sI https://nik-kh.pages.dev` must answer `302` to `brisotto.cloudflareaccess.com`.
4. **Create an API token**: *My Profile → API Tokens → Create Token → Custom token*, permission *Account → Cloudflare Pages → Edit*.
5. **Add GitHub secrets and variables** (*Settings → Secrets and variables → Actions*):
   - Secret `CLOUDFLARE_API_TOKEN`: the token from step 4.
   - Secret `CLOUDFLARE_ACCOUNT_ID`: shown in the dashboard under *Workers & Pages*.
   - Variable `CLOUDFLARE_PAGES_PROJECT`: optional, defaults to `nik-kh`.
   - Variable `CLOUDFLARE_PAGES_DEPLOY` = `true`: set this last, after checking step 3.
6. **Deploy**: merge `develop` into `main` and push. Then open `https://nik-kh.pages.dev` in a private window: it must ask for the Cloudflare Access login.
