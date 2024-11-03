# Nix Darwin Overview

Nix alone can be used for toolchain management, it is easier to manage per project with the single command `nix develop`.

In addition to that **nix-darwin** helps with the configuration of macOS:

* Declarative configuration of all your macOS system settings
* Installation of packages and configuration of those (It’s better than homebrew)
* Seamless integration into launchd for configuration of additional daemons
* Painless management of local Linux builder VMs


To use a metaphor, nix-darwin is the closest equivalent to NixOS that we can have on macOS. It brings the module system and declarative approach to macOS configuration.

## Nix darwin commands

* cd to your repo and run `darwin-rebuild switch --flake .` to apply new configuration

## Nix Darwin Configuration

See the README.md file in the [breezeight-nix-darwin-config](https://github.com/breezeight/breezeight-nix-darwin-config) repo for my personal configuration .

WARNING I've found that you need to explicitly set the username and home directory in the nix-darwin configuration expecially if you are using home-manager:
```nix
      # Add these lines to explicitly set your username and system
      users.users.nicolabrisotto = {
        name = "nicolabrisotto";
        home = "/Users/nicolabrisotto";
      };
```

If you to start with a minimal configuration, you can use the [nixcademy.com](https://nixcademy.com/posts/nix-on-macos/) configuration as a base.


## Building Linux binaries

See [Nix Linux Remote Builder VM on OSX Howto](dev/nix/nix-linux-remote-builder-vm-on-osx-howto.md) for details.

