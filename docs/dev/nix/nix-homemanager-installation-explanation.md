# Home Manager Installation with Flakes Explanation
Home Manager can be used in three main ways:

1. **Standalone**: The only option for non-NixOS and non-Darwin systems, and recommended for users wanting independent home directory management.
2. **NixOS Module**: Integrates with NixOS, building user profiles along with the system using nixos-rebuild.
3. **nix-darwin Module**: An alternative to the standalone option on macOS, integrating with nix-darwin to build user profiles with the system using darwin-rebuild.

> [!WARNING]
> The official documentation [Home Manager installation](https://home-manager.dev/manual/23.05/index.html#ch-installation) proposes as first alternative to install Home Manager in the standard way using channels. **I use Flakes instead.**

> [!NOTE]
> Even if this tutorial [simple-homemanager](https://github.com/Evertras/simple-homemanager/tree/main) is only about the standalone option, it's a good introduction to Home Manager with Flakes for new users that want to understand how to use Home Manager with Flakes.


## Home Manager with nix-darwin and Flakes

This explanation complements the [nix-breezeight-config-osx-and-linux-overview.md](nix-breezeight-config-osx-and-linux-overview.md) and the README.md file in the [breezeight-nix-darwin-config](https://github.com/breezeight/breezeight-nix-darwin-config) repo. In this section we try to be more generic and explain the different parts of the configuration are related to each other:
- flake.nix
- basic homemanager configuration
- nix-darwin configuration for home manager

Prerequisites to experiment with the ideas in this explanation:
- Enable experimental features `nix-command` and `flakes` which is the default if you use Determinate Systems Nix installer.
- A minimal [example of minimal configuration](https://home-manager.dev/manual/23.05/index.html#sec-usage-configuration) called `home.nix`


In the [nix-darwin-overview.md](nix-darwin-overview.md) file you can find more details on how to set up the nix-darwin configuration we show how to create a minimal flake with nix-darwin usinge the default template: `nix flake init -t nix-darwin`

Will explain how to add the homemanager configuration to the resulting flake, which at the time of writing is:
```nix
{
  description = "Example Darwin system flake";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    nix-darwin.url = "github:LnL7/nix-darwin";
    nix-darwin.inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = inputs@{ self, nix-darwin, nixpkgs }:
  let
    configuration = { pkgs, ... }: {
      # List packages installed in system profile. To search by name, run:
      # $ nix-env -qaP | grep wget
      environment.systemPackages =
        [ pkgs.vim
        ];
      # Auto upgrade nix package and the daemon service.
      services.nix-daemon.enable = true;
      # nix.package = pkgs.nix;

      # Necessary for using flakes on this system.
      nix.settings.experimental-features = "nix-command flakes";

      # Enable alternative shell support in nix-darwin.
      # programs.fish.enable = true;

      # Set Git commit hash for darwin-version.
      system.configurationRevision = self.rev or self.dirtyRev or null;

      # Used for backwards compatibility, please read the changelog before changing.
      # $ darwin-rebuild changelog
      system.stateVersion = 5;

      # The platform the configuration will be used on.
      nixpkgs.hostPlatform = "x86_64-darwin";
    };
  in
  {
    # Build darwin flake using:
    # $ darwin-rebuild build --flake .#simple
    darwinConfigurations."simple" = nix-darwin.lib.darwinSystem {
      modules = [ configuration ];
    };

    # Expose the package set, including overlays, for convenience.
    darwinPackages = self.darwinConfigurations."simple".pkgs;
  };
}
```

To extend this basic nix-darwin flake to install and configure Home Manager, you’ll need to:

1. Add Home Manager as an input.
2. Modify the darwinConfigurations section to include Home Manager as a module.
3. Define any user-specific Home Manager settings.

Here’s how to do it:

```nix linenums="1" hl_lines="8-9 42-49 56-57"
{
  description = "Example Darwin system flake with Home Manager";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    nix-darwin.url = "github:LnL7/nix-darwin";
    nix-darwin.inputs.nixpkgs.follows = "nixpkgs";
    home-manager.url = "github:nix-community/home-manager";
    home-manager.inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = inputs@{ self, nix-darwin, nixpkgs, home-manager, ... }:
  let
    configuration = { pkgs, ... }: {
      # List packages installed in system profile. To search by name, run:
      # $ nix-env -qaP | grep wget
      environment.systemPackages =
        [ pkgs.vim
        ];
      # Auto upgrade nix package and the daemon service.
      services.nix-daemon.enable = true;
      # nix.package = pkgs.nix;

      # Necessary for using flakes on this system.
      nix.settings.experimental-features = "nix-command flakes";

      # Enable alternative shell support in nix-darwin.
      # programs.fish.enable = true;

      # Set Git commit hash for darwin-version.
      system.configurationRevision = self.rev or self.dirtyRev or null;

      # Used for backwards compatibility, please read the changelog before changing.
      # $ darwin-rebuild changelog
      system.stateVersion = 5;

      # The platform the configuration will be used on.
      nixpkgs.hostPlatform = "x86_64-darwin";
    };

    # Additional configuration to set up Home Manager
    homeManagerConfig = { pkgs, ... }: {
      # Enable Home Manager
      home-manager.useGlobalPkgs = true;
      home-manager.useUserPackages = true;

      # Define user-specific configuration
      home-manager.users.myusername = import ./home.nix;  # Assumes you have a home.nix file with user config
    };
  in
  {
    darwinConfigurations."simple" = nix-darwin.lib.darwinSystem {
      system = "x86_64-darwin";
      modules = [
        configuration
        home-manager.darwinModules.home-manager  # Adds the Home Manager module
        homeManagerConfig  # Adds user-specific configuration
      ];
    };

    darwinPackages = self.darwinConfigurations."simple".pkgs;
  };
}
```

Explanation of Changes:

- **Home Manager Input:** We added the Home Manager repository as an input under home-manager, following the same version of nixpkgs.
- **Home Manager Module:** In darwinConfigurations, we included home-manager.darwinModules.home-manager to enable Home Manager alongside nix-darwin.
- **User-Specific Configuration:** In the homeManagerConfig section, home-manager.users.simple imports a home.nix file that defines settings for the user “simple.” This file (`home.nix`) should contain Home Manager options for user-specific packages, settings, and dotfiles.

[`home-manager.users`](https://nix-community.github.io/home-manager/nix-darwin-options.xhtml#nix-darwin-opt-home-manager.users) is an attribute set that define the Home Manager configuration for each user.

`home.nix` is typically used as the main entrypoint for a user's Home Manager configuration, See [Home Manager Configuration Overview and Options](nix-homemanager-configuration-overview-and-options.md) for more details.

 but for larger configurations, it's recommended to split it into multiple files for better organization. Here's a common structure:

```bash
└── home
    ├── home.nix          # Main entrypoint
    ├── programs          # Directory for program-specific configs
    │   ├── git.nix
    │   ├── neovim.nix
    │   └── zsh.nix
    └── packages.nix      # Package installations
```



It's important to note that the `home-manager.users.myusername` is the username of the user that we want to configure. In the example above it's `myusername`.


> [!WARNING]
> I've found that you need to explicitly set the username and home directory in the nix-darwin configuration expecially if you are using home-manager, adding the following lines to your nix-darwin configuration:
>```nix
>      # Add these lines to explicitly set your username and system
>      users.users.nicolabrisotto = {
>        name = "nicolabrisotto";
>        home = "/Users/nicolabrisotto";
>      };
>```




## Home Manager Standalone on Linux with Flakes

This tutorial [simple-homemanager](https://github.com/Evertras/simple-homemanager/tree/main) 


## Advanced topics

### Understanding what the different installation methods do

TODO: Explain where in the general architecture each installation method is doing what and what are 

