# Nix Index

Breezeight NixOS Config on OSX:

- [**Breezeight Nix Config**](nix-breezeight-config-osx-and-linux-overview.md)
- [Nix Darwin Overview](nix-darwin-overview.md)

Home Manager Day by Day Usage:

- [Home Manager Configuration Overview and Options](nix-homemanager-configuration-overview-and-options.md)
- [Home Manager Nix Darwin Module Docs](nix-homemanager-nix-darwin-module-docs.md): links to the official docs + some notes.

[Nix Ecosystem : Community - People - Companies](https://docs.google.com/document/d/1rIRtmH7mKLIsa83Lv5ghYriYPpYNMRm9MPRg3qgnWm4)

[Nix and NixOS](https://docs.google.com/document/d/1eKSLcL8UKoEa1qa-gOUcGelrWqxYT1cZ2-gINrW5xGc)
- Nix installer overview
- Overview and Purpose: Explains what Nix is, its benefits (especially for reproducibility), and its potential uses for Addictive, highlighting differences and considerations regarding Docker, ASDF, and the choice between NixOS and Nixpkgs.
- Learning Resources: Provides a curated list of materials for learning Nix, including official and unofficial documentation, books, tutorials, and insights from community talks.
- Nix Core Concepts: Details fundamental concepts such as the Nix language, Nix store, dependencies, closures, and the package manager's features like multiple versions, atomic upgrades, and garbage collection.
- Flakes: A significant portion dedicated to Nix flakes, covering their purpose, structure, usage (e.g., nix shell, nix develop, nix run), and integration with tools like direnv and CI/CD platforms like GitHub Actions.
- NixOS: Explores NixOS as a declarative operating system, its installation, configuration management through modules, and deployment options.
- Development Environments: Discusses how to set up reproducible development environments for different languages (Python, Node, Elixir, Rust, Yarn) using Nix and tools like devenv.sh.
- Deployment and Virtualization: Addresses deployment strategies, including remote installations, secret management with sops-nix, and the use of VMs (Quickemu, Microvm, VirtManager) for testing and production.
- Docker Integration: Explains how Nix interacts with Docker, including installing Docker on NixOS and using Nix to build Docker images.
- Troubleshooting and Debugging: Offers guidance on debugging Nix and NixOS configurations, including tracing and using the Nix REPL.
Community and Companies: Lists key people and companies within the Nix ecosystem that offer consultancy and training.

Nix Language and generic explanations:
- [GUIDE Nix Language and Nixpkgs](https://docs.google.com/document/d/1zOHnCCcLPbwVHm3E-DmVudWRdH83_LCY85UrlOJw1L4/edit?tab=t.0#heading=h.zfqjlk312a9c)
  - Nix Language: The declarative language used to define packages and system configurations.
  - Nixpkgs: A large collection of packages defined in the Nix language, serving as the primary source for software in the Nix ecosystem.
  - Purity and Reproducibility: Core tenets of Nix, ensuring that builds are isolated from the host system and produce identical results every time.
  - Derivations: The fundamental unit of computation in Nix, describing how to build a package or component.
  - default.nix and shell.nix: Common file names for defining Nix expressions, typically used for package definitions and development environments, respectively.
  - Nix Store: The immutable content-addressable store where all built derivations (packages, configurations, etc.) are placed.
  - Garbage Collection: The process of removing unused derivations from the Nix store to free up space.
  - Nix Shell: A command-line tool for creating isolated development environments based on Nix expressions.
  - Nix Build: A command-line tool for building derivations defined in Nix expressions.
  - Nix Develop: A command-line tool for setting up a development environment, often used in conjunction with shell.nix.
  - Overlays: A mechanism to extend or modify the Nixpkgs set of packages, allowing for custom versions or additions without directly altering Nixpkgs.
  - FHS Environments (Filesystem Hierarchy Standard Environments): A way to create environments that mimic the traditional Linux filesystem layout, which can be useful for software that expects specific file paths.
  - Common Issues and Debugging: Discussions and solutions for frequently encountered problems when working with Nix.


Home Manager Explanations and introductions:

- [Home Manager Overview](nix-homemanager-overview-explanation.md): good to explain the big picture and to undestand the usage context, good for new users.
- [GOOGLE DOC : Home Manager Configuration Overview and Options](https://docs.google.com/document/d/1UN77X-g7uTlgCRNU03Tnw4ao74hmc1oUxqYR-4kH6SA/edit?tab=t.0):
  - Document Overview
  - Installation
  - General overview of Home-Manager
  - Home-Manager internals
  - Home-manager modules notes
  - Frequent Jobs
  - [JOB]
  - Home-Manager for Darwin
  - darwin-rebuild
  - Install OSX in UTM
  - Connect via ssh
  - mac configuration
  - nix-darwin config
  - Understanding nix-darwin and Home Manager
  - [Darwin] Homebrew Module
  - [Darwin] system.defaults
  - Home-manager config
  - Home Manager Modules
  - nixos-hardware
  - Direnv
  - Home Module
  - Packages vs modules
  - home.stateVersion
  - Module to install DEVENV using flake
  - Upgrading Home-Manager
  - Impermanence and Home-Manager
  - Home Manager Standalone Internals
  - Profiles
  - The Flake Structure and how it's used
  - The Breezeight Parent module
  - Global Module
  - Session Settings
  - Persistence Configuration
  - Features Modules
  - Features Modules - CLI - Overview
  - Features Modules - CLI - git.nix
  - Features Modules - CLI - gpg.nix
  - Features Modules - CLI - ssh.nix
  - Tooling and applications
  - Misterio77's Configurations

Remote Linux Builders:

- [Nix Linux Remote Builder VM](nix-linux-remote-builder-vm-on-osx-howto.md)

Bootstrap a Nixos system:

- [Nix Bootstrap NixOS](nix-bootstrap-nixos-howto.md)
- [Nix Bootstrap NixOS Explanation](nix-bootstrap-nixos-explanation.md)


Nix and Docker:

- [Nix Nixpaks](nix-nixpacks.md)
