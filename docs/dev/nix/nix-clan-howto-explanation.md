# Clan — Personal Notes & Howtos

Personal, opinionated notes on using **Clan** in real projects.  
Focus: mental model, operational safety, and my conventions.

---

## TODO

- `clan templates list` ??

## Cheatsheet

```sh
clan machines create <machine-hostname>
clan profiles create <profile-name>
clan modules create <module-name>
clan secrets create <secret-name>
clan secrets decrypt <secret-name>
```

## Document Scope and Assumptions

- Clan is used as an **opinionated Nix-based infrastructure tool**
- Secrets are managed with **sops + age**
- Configuration is reproducible; **secrets are not**
- This document complements official docs and prioritizes survivability

## Getting Started with Clan

See https://docs.clan.lol/getting-started/creating-your-first-clan/

The official documentation explains how to create your first clan using the `default template` and how to use the different concepts: machines, profiles, modules, secrets, etc.

### Clan installation

The official documentation sugge to use the following command to create a new clan:

```sh
nix run "https://git.clan.lol/clan/clan-core/archive/main.tar.gz#clan-cli" --refresh -- flakes create
```

It means:
- downloads and runs the Clan CLI directly from the Git archive
- forces a fresh fetch (--refresh)
- does not install anything globally
- executes clan flakes create to bootstrap a new Clan repository

This is a one-shot command used only to create the initial flake; afterward, the repo manages its own Clan version via flake + direnv. When you create a clan using existing templates, the **flake defines a development shell that already includes `clan`** and all required tooling.

The template wires this shell to **direnv**, as recommended by the official documentation. In practice:

- the repository provides a `.envrc`
- entering the directory activates the flake-defined shell via `direnv`
- `clan` is available without any global installation
- the Clan version is pinned by the repository

Implications:

- `direnv allow` is required once
- tooling is repo-scoped and reproducible
- if `clan` is not found, check `direnv status` or run `direnv reload`

The `.envrc` and flake should be treated as part of the infrastructure, not as a local convenience.





## Core Concepts (Mental Model)

### What Clan is (for me)

- A structured way to manage **machines** with Nix
- A system that binds configuration, secrets, and deployment
- A workflow where **secret loss = total loss**

### Key building blocks

- **Clan**: the whole configuration universe (repo)
- **Machine**: a concrete host (VM, server, laptop)
- **Module**: reusable Nix logic
- **Profile**: opinionated composition of modules
- **Secrets**: encrypted, versioned, mandatory

Rules:
- Configuration is cheap
- Secrets are priceless
- Backups are mandatory

## Secrets Management (sops + age)

Clan relies on **age** keys.

```
~/.config/sops/age/keys.txt
```

Properties:
- user-specific
- never committed
- absolutely critical

### ⚠️ IMPORTANT — Secret Key Backup Management

Losing this key means **permanent loss** of access to all encrypted Clan secrets.

### Backup strategy (mandatory)

I keep **two independent backups** of the same key material:

1. **1Password**
   - Vault: `employee`
   - Entry title: `CLAN AGE KEY`
   - Stored as a document

2. **KeePassXC**
   - Entry title: `CLAN AGE KEY`
   - Stored as an attachment

Requirements:
- encrypted
- accessible independently
- kept in sync

Restore script for 1Password

```sh
#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="$HOME/.config/sops/age"
TARGET_FILE="$TARGET_DIR/keys.txt"

mkdir -p "$TARGET_DIR"

op document get "CLAN AGE KEY" \
  --vault "employee" \
  --out-file "$TARGET_FILE"

chmod 600 "$TARGET_FILE"
```

Post-conditions:
- file exists
- permissions are strict
- `sops -d` works

Never commit this file.

---

## Machines

What a "machine" means in practice:

- An entry in the clan inventory file (clan.nix): inventory.machines.<machine-hostname> that is used to define metadata about the machine (ex of metadata: deploy.targethost or machineClass or tags).
- A configuration (nixos or nix-darwin), that can be specified in 1) The option: machines.<machine-hostname> (clan.nix) or 2) A directory containing the configuration in `machines/<machine-hostname>`. Created with: `clan machines create <machine-hostname>`
- A concrete host with a stable name (machines describe all client devices from cloud VMs to bare metal laptops and are defined using Nix code inside the flake).

Expectations: A machine is fully reproducible **except secrets** and only the secrets are disposable by design

The creation of machines will be the same process for all kinds of devices and only later branch into specific steps.

Learn more about machines: [Add Machines](https://docs.clan.lol/getting-started/add-machines/)



## Profiles and Modules

### When to create a module

Create a module when:
- logic is reusable
- more than one machine needs it
- copy-paste would otherwise occur

### When to use a profile

Use a profile to:
- group modules
- define a role (web, infra, workstation)
- enforce opinionated defaults

Rule of thumb:
- modules = capability
- profiles = intent

---

## Common Workflows

### New laptop / workstation

- Restore age key
- Verify decryption works
- Clone clan repo
- Deploy local configuration

### New server

- Bootstrap OS
- Ensure SSH access
- Restore age key locally
- Add machine definition
- Deploy

### Add a new secret

- Encrypt with sops
- Commit encrypted file only
- Minimize plaintext exposure

---

## Debugging & Recovery

### Secret decryption fails

Check:
- key exists
- file permissions
- correct user
- correct age recipient

### Deployment fails

Common causes:
- secrets not decryptable
- missing profile/module wiring
- state mismatch

Always verify secrets first.

---

## Cheatsheet

Paths:
- age key: `~/.config/sops/age/keys.txt`

Golden rule:
> If the age key is lost, the clan is dead.

---

## Notes for Future Me

- Split this file only when it becomes unwieldy
- Add failure stories and recovery notes
- Prefer clarity over completeness
