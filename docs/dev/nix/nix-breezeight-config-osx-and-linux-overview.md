## Overview

At the moment of writing this, the NixOS configuration for Breezeight is based on the following repos:

* [misterio77-nix-config](https://github.com/breezeight/misterio77-nix-config) Branch `breezeight` for the nixOS configuration
* [breezeight-nix-darwin-config](https://github.com/breezeight/breezeight-nix-darwin-config) for the darwin configuration. The Darwin configuration has been inspired by [nixcademy.com](https://nixcademy.com/posts/nix-on-macos/)

Why we have two repos?
* for the Nixos I wanted to learn from a complete example and I have been inspired by [misterio77-nix-config](https://github.com/misterio77/nix-config). Then I tried to customize it to my needs but it is way too much code to understand for a beginner and add the darwin configuration.
* For this reason I have created the `breezeight-nix-darwin-config` repo to have a minimal darwin configuration and learn from it.

Aim for the future:
* merge the nixos configuration into the `misterio77-nix-config` repo and make it easier to understand and maintain.

## Nix Darwin Configuration

See the README.md file in the [breezeight-nix-darwin-config](https://github.com/breezeight/breezeight-nix-darwin-config) repo for more details on how to set up the darwin configuration.




