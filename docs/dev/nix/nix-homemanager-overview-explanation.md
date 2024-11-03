# Nix Homemanager Overview and Explanation

## Scope of the document 

This document explains the scope of the homemanager and the main ideas behind it. It's not an howto and for certain it send you to other documents that explain certain aspects in more details:


## Related documents

### Installation

* [nix-homemanager-installation-explanation.md](nix-homemanager-installation-explanation.md): more about the different installation options available.


## What is home-manager ? Why and where is it useful?

Home Manager is a tool for managing user environments with the Nix package manager **declaratively**. It makes handling dotfiles and user-specific packages on nix-enabled machines seamless and consistent, ensuring your configuration is reproducible across environments.

The real advantage of Home Manager is for users who want a declaratively-managed setup that can be easily ported to a non-NixOS system, while also being usable on NixOS itself, making it **a very portable solution.** Rather than creating a custom solution, Home Manager allows you to simply and effectively manage programs and configurations right in your home directory. **It's compatible with Linux, macOS, and even NixOS**, making it highly versatile for different environments.

While Home Manager is ideal for user-level configurations, system-level settings should be managed using tools suited for each platform:

- **NixOS**: Use the NixOS configuration system.
- **macOS**: Utilize `nix-darwin` for system-level configurations.
- **Other Linux Distributions**: Manage system configurations using the native package manager or configuration tools.

By keeping system-level configurations separate and using Home Manager for user-specific settings, you maintain a clear separation of concerns, enhancing portability.One of the things that sets Home Manager apart is its abundance of configurable options, which help streamline the Nix experience. 

In summary, Home Manager is a powerful, cross-compatible choice for declarative user environment management, similar to nix-darwin but with a more user-level focus.

## Why use a module instead of a package and config file?

In Home Manager, using a module instead of directly configuring a package and using a config file has several benefits and some trade-offs, **TL;DR:**

Use a module when:

* You want a declarative, consistent, and version-controlled configuration.
* You want integration with the rest of your system and prefer sensible defaults provided by the module.
* You are okay with the configuration being static and needing a rebuild to apply changes.

Use a config file when:

* You need full flexibility to modify settings on-the-fly.
* You need options not available in the module.
* You prefer a more hands-on approach to managing configuration files, especially for frequently changing software.

In practice, many people use a mix of both. For software where configuration rarely changes, modules are preferred, while for software requiring frequent modifications, direct configuration files are more convenient.

### Benefits of Using a Module

1. **Declarative Configuration**: Modules allow you to manage software settings in a declarative way. This means you define the configuration in a Nix expression, which Home Manager uses to generate the necessary files and settings automatically. The benefit of a declarative approach is that your system configuration is consistent, repeatable, and can be version-controlled (e.g., in Git). You also gain the ability to easily rollback to previous configurations.

2. **Integration with System**: Modules often handle more than just installing the package. For example, the Kitty module ([https://github.com/nix-community/home-manager/blob/master/modules/programs/kitty.nix](https://github.com/nix-community/home-manager/blob/master/modules/programs/kitty.nix)) in Home Manager can automatically manage the configuration file (`~/.config/kitty/kitty.conf`). The Nix module approach means you can avoid manually managing these configuration files, which provides a more integrated and seamless setup for your environment.

3. Configuration is consolidated for easier management

4. **Consistency**: Modules provide a consistent interface for configuring software, all in the same language (Nix). Instead of having to learn the specific format of each program's configuration file (which could be YAML, JSON, TOML, etc.), you write everything in Nix. This can make it easier to understand and maintain your configuration.

5. **Defaults and Convenience**: Modules often come with sensible defaults, which means less work to get started. You can use the default options or adjust them to fit your needs. Moreover, modules often include useful abstractions that make setting options easier compared to editing a raw configuration file.

### When Not to Use a Module

1. **Flexibility**: If you prefer to make ad-hoc changes to the configuration file (i.e., modify settings on the fly), using a module might be less convenient. Changes made through a module require a rebuild (`home-manager switch`) to apply, whereas a direct configuration file edit takes effect immediately.

2. **Subset of Features**: There's a risk that a module may not expose all the options available in the actual config file of the program. Modules typically aim to provide easy access to the most commonly used settings, and if you need an obscure or highly specialized option, you might find the module lacking. In such cases, you may need to override or extend the module configuration or fall back to manual configuration.

3. **Customization**: For programs where you frequently tweak the configuration, like text editors (e.g., Neovim), using a module might be cumbersome since you need to rebuild each time to see changes. In these cases, some users prefer to manually manage the configuration file, optionally using symlinks to version-control it.

### Examples

Nix modules are designed to integrate a package with the entire system. For example, in that Kitty home-manager module, it defines xdg.configFile."kitty/kitty.conf", which manages the file \~/.config/kitty/kitty.conf in a declarative way. The Kitty Nix module allows you to manage all of the parts of Kitty scattered around the system (such as its configuration file) in a declarative way, with all of the benefits that declarative and immutable configuration files bring (rollbacks, easy saving in git, easy provisioning on new machines, ...). In this specific case of Kitty, that doesn't sound that helpful. However, for complicated services such as Nextcloud with many options, [the Nextcloud NixOS module]\([https://github.com/NixOS/nixpkgs/blob/nixos-22.05/nixos/modules/services/web-apps/nextcloud.nix](https://github.com/NixOS/nixpkgs/blob/nixos-22.05/nixos/modules/services/web-apps/nextcloud.nix)) allows you to easily declaratively specify Nextcloud settings without having to mess with random configuration files.\
\
However, sometimes declarative configuration files are not always desirable. For example, I mess around with my \~/.config/nvim a lot, and I don't want to have to rebuild my configuration every time I modify it. In this case, I wouldn't use a NixOS module to manage my neovim installation. you can work around this by using an out of store symlink. Meaning the file gets symlinked by home manager and doesn't require a rebuild to update. For my emacs config:



home.file \\= { 

    ".emacs.d/init.el".source \\= config.lib.file.mkOutOfStoreSymlink ./init.el;

    ".emacs.d/early-init.el".source \\= config.lib.file.mkOutOfStoreSymlink ./early-init.el; 

};

For example, in my configuration [I use the mpd home-manager module]\([https://github.com/virchau13/dots/blob/9eec548da8e72c5f2b41cdeb40e983dcc91aefd1/hosts/hexagon/home.nix#L70](https://github.com/virchau13/dots/blob/9eec548da8e72c5f2b41cdeb40e983dcc91aefd1/hosts/hexagon/home.nix#L70)), since that's not a configuration file I modify regularly, and therefore I don't want to go through the hassle of making it mutable. On the other hand, I make [my neovim configuration mutable by symlinking \~/.config/nvim to point to \$DOTS\\\_REPO/apps/nvim]\([https://github.com/virchau13/dots/blob/9eec548da8e72c5f2b41cdeb40e983dcc91aefd1/apps/nvim/default.nix#L7](https://github.com/virchau13/dots/blob/9eec548da8e72c5f2b41cdeb40e983dcc91aefd1/apps/nvim/default.nix#L7)), so I can modify it on-the-fly but still save it in my dotfile repository.\


### HOWTO Eject Home-manager

> [!WARNING]
> This section needs to be improved.

If you read most of those modules in home-manager, unless they also manage a systemd user service, they're mostly along the lines of if (cfg.enable) { environment.systemPackages = \\[ pkgs.kitty \\]; xdg.configFile."kitty/kitty.conf" = someParsedVersionOfCfg; } (pseudocode). Usually, the module will come with some sensible defaults for your kitty/kitty.conf.

\-   if you want to eject, just home-manager switch, find all the generated files, copy and paste themSummary


However, sometimes declarative configuration files are not always desirable. For example, I mess around with my ~/.config/nvim a lot, and I don't want to have to rebuild my configuration every time I modify it. In this case, I wouldn't use a NixOS module to manage my neovim installation. you can work around this by using an out of store symlink. Meaning the file gets symlinked by home manager and doesn't require a rebuild to update. For my emacs config:

```nix
home.file = { 
    ".emacs.d/init.el".source \= config.lib.file.mkOutOfStoreSymlink ./init.el;
    ".emacs.d/early-init.el".source \= config.lib.file.mkOutOfStoreSymlink ./early-init.el; 
};
```

For example, this configuration [uses the mpd home-manager module](https://github.com/virchau13/dots/blob/9eec548da8e72c5f2b41cdeb40e983dcc91aefd1/hosts/hexagon/home.nix#L70), since that's not a configuration file that is modified regularly, and therefore doesn't want to go through the hassle of making it mutable.

On the other hand, I make [my neovim configuration mutable by symlinking ~/.config/nvim to point to $DOTS\_REPO/apps/nvim](https://github.com/virchau13/dots/blob/9eec548da8e72c5f2b41cdeb40e983dcc91aefd1/apps/nvim/default.nix#L7), so I can modify it on-the-fly but still save it in my dotfile repository.

If you read most of those modules in home-manager, unless they also manage a systemd user service, they're mostly along the lines of if (cfg.enable) { environment.systemPackages = \[ pkgs.kitty \]; xdg.configFile."kitty/kitty.conf" = someParsedVersionOfCfg; } (pseudocode). Usually, the module will come with some sensible defaults for your kitty/kitty.conf.

The main advantages in picking home-manager module config over manual files:

-   configuration is grouped together

-   usually, sane defaults

-   learn one syntax (Nix), not a syntax per file (is this one YAML? TOML? custom? JSON?)

-   if you want to eject, just home-manager switch, find all the generated files, copy and paste them

In my 5+ year old home-manager config, I have both. There's dotfiles for programs that home-manager doesn't have modules for; there's dotfiles that home-manager didn't have modules for that I configured manually and haven't ported forward; there's dotfiles predating my use of home-manager; there's a growing number of home-manager configurations.

## Advanced topics
### Why Home Manager is not Part of NixOS or Nixpkgs

The best answer you may get comes from a [NixOS Discourse thread](https://discourse.nixos.org/t/why-isnt-more-of-home-manager-merged-into-nixpkgs/6096/13), with replies from Nix creator Eelco Dolstra and Home Manager creator Robert Helgesson (rycee).

Long story short: Robert Helgesson took inspiration from an already existing tool called nixuser which served a similar purpose, and, in his own words,

"As it turned out, the basic functionality of installing packages, generating configurations, linking files into $HOME, and so on is actually very simple and it was pretty easy to just implement everything from scratch."

So, for the historical reasons Home Manager exists as a separate project, and it was also later added to the [Nix Community GitHub Organization](https://github.com/nix-community) which is the umbrella org for the officially endorsed Nix tools.

Eelco Dolstra says, that many things in nixpkgs find themselves as they are because Nix/NixOS was (back then) lacking proper modularity (and it is now solved with flakes), that led to tightly-coupled systems. Having Home Manager as a separate project makes complete sense in that regard, and allows for "both quality and speed of development". Also think [Conway's Law](https://en.wikipedia.org/wiki/Conway%27s_law).

There are talks however that it would be beneficial to merge some parts of Home Manager into nixpkgs, e.g. some general utility functions.

**