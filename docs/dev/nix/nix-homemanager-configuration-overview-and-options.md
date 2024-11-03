# Home Manager Configuration Structure

## Scope

Independently of the installation mode you use (standalone, NixOS module, or nix-darwin), you will end up creating a set of modules for each user. These modules define the user's home environment configuration. The integration is consistent across systems, typically defined as:

```nix
{
  home-manager.users.yourusername = import ./home/home.nix;
}
```

## Common Structure

`home.nix` is typically used as the main entrypoint for a user's Home Manager configuration. For larger configurations, it's recommended to split it into multiple files for better organization. Here's a common structure:

```bash
└── home
    ├── home.nix          # Main entrypoint
    ├── programs          # Directory for program-specific configs
    │   ├── git.nix
    │   ├── neovim.nix
    │   └── zsh.nix
    └── packages.nix      # Package installations
```

## TUTORIAL: Adding a file to your home directory
This is a good example to understand how to add a file to your home directory and get used to the structure:
[Adding a file to your home directory](https://github.com/Evertras/simple-homemanager/blob/main/06-explain-home-nix.md#adding-a-file-to-your-home-directory)



## Share Darwin Linux configuration

TODO:

- [ ] let's say you have a configuration that works on Linux, how do you share it with Darwin? There are some options, let's see what they are and what are the pros and cons.

## Multiple users

TODO


## Common 