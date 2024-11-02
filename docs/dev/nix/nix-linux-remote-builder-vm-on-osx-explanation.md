Macbooks stand out with their long battery life and the “just works” experience with meeting multimedia. Developing for Linux and deploying to Linux machines with Nix, however, was a pretty much reduced experience until lately. In this article we’re going to look closer at how easy it is to configure a macOS system with a “local remote builder” so it can build NixOS images and also remote deploy to Linux systems without the need for external remote builders.

It is generally possible to cross-compile between different architectures, but not all software packages can be cross-compiled. So sometimes, we need a Linux machine to delegate Linux builds to. This article is about running a NixOS VM in the background on your macOS system.

The story unfolds in chronological order: At first, there was the pkgs.darwin.linux-builder package which worked well from the beginning, but was laborious to set up. Then, a nix-darwin module was created that made the setup a literal one-liner. Let’s see how that works and how to improve it.


## nix-darwin configuration

This module is available in the `nix-darwin` package and it helps you set up a Linux builder VM on macOS, it reduce the manual steps described in [The Linux Builder in nixpkgs](#the-linux-builder-in-nixpkgs). So also if you are using `nix-darwin`, the next is relevant to you.

* [`nix.linux-builder.package`](https://daiderd.com/nix-darwin/manual/index.html#opt-nix.linux-builder.package): The default is `pkgs.darwin.linux-builder`, the same package as in [The Linux Builder in nixpkgs](#the-linux-builder-in-nixpkgs). 


* [`nix.linux-builder.config`](https://daiderd.com/nix-darwin/manual/index.html#opt-nix.linux-builder.config) this is the configuration of the VM an example configuratio is available in the [nix-linux-remote-builder-vm-on-osx-howto.md](nix-linux-remote-builder-vm-on-osx-howto.md)

* [`nix.linux-builder.ephemeral`](https://daiderd.com/nix-darwin/manual/index.html#opt-nix.linux-builder.ephemeral). With these config enable you can more easly change the VM on the fly and you don't pile up status build after build.



This module adds the following things to our system setup:

-   A new [launchd](https://en.wikipedia.org/wiki/Launchd) service called `org.nixos.linux-builder` that keeps SSH keys and VM disk image in `/var/lib/darwin-builder` (Run `sudo launchctl list org.nixos.linux-builder` to inspect it)
-   A new file `/etc/ssh/ssh_config.d/100-linux-builder.conf` that creates an SSH host-alias `linux-builder` (this one is needed for TCP port bending reasons)
-   `/etc/nix/machines` gets the needed remote builder entry

It's not fully documented but if you check the configuration you can find the ssh configuration to connect to the VM, which is at the time of writing (november 2024):

```bash
sudo ssh linux-builder
```

> [!NOTE] 
> Sources:
> * https://nixcademy.com/posts/macos-linux-builder/


### Supporting multiple architectures (aarch64 and x86_64)

In june 2024 a `PR linux-builder: make compatible with cross-arch builder package` was merged.

* https://github.com/NixOS/nixpkgs/issues/313784
* https://github.com/LnL7/nix-darwin/pull/974

this make it possible to configure the VM to support `x86_64

```nix
      nix = {
        # Enable Linux builder support in nix-darwin.
        linux-builder = {
          enable = true;

          # enable the linux-builder for the systems aarch64-linux and x86_64-linux
          package = pkgs.darwin.linux-builder-x86_64;
          ;
          # ephemeral VM removes the VM after a reboot
          ephemeral = true;
        };
        # This line is a prerequisite for linux-builder
        settings.trusted-users = [ "@admin" ];
      };
```

I still don't know if we can use the same VM to build `aarch64-linux` and `x86_64-linux` images at the same time... It looks like its not supported yet. 

> [!ALERT]
> We dont know what `systems` is used for in the `linux-builder` package.
          




## The Linux Builder in nixpkgs

In December 2022, Gabriella Gonzalez [upstreamed her streamlined version of a Linux builder](https://github.com/NixOS/nixpkgs/commit/edd1cbf5d4d3379a123cc138fe9787d67247ac9f) that runs on macOS and [blogged about it](https://www.haskellforall.com/2022/12/). It consists of a [NixOS profile module that sets up a minimal qemu NixOS VM](https://github.com/NixOS/nixpkgs/blob/master/nixos/modules/profiles/nix-builder-vm.nix) along with a ready-to-use SSH key pair. As the official [NixOS documentation of the `darwin.linux-builder` package](https://nixos.org/manual/nixpkgs/stable/#sec-darwin-builder) states, it just needs to be run and can then be set up as a remote builder.

As this VM is a Linux image, we would technically first have to find a way to build a Linux system on macOS, which is what we wanted from the beginning. As it is upstream now, it can be obtained from the official NixOS binary cache without having to bootstrap it first.

To run this VM, we do not need to install Qemu or any other virtualization solution first, as this package itself is a script that runs Qemu for us:

```bash
nix run nixpkgs#darwin.linux-builder
```

Our local Nix daemon still needs to be educated about the availability of this runner. To achieve that, we need to perform the following changes to our system:

* Add ourselves to the extra-trusted-users variable in the nix settings
* Add the builder to the builders variable in the [nix settings](https://nixos.org/manual/nix/stable/command-ref/conf-file)
* Add a new SSH config file that maps the hostname linux-builder to localhost but with the builder’s port
* Restart the nix daemon

Unfortunately, this way we have to take care of the process and its setup ourselves. This seems laborious and is surely not the declarative workflow that we’re used to from Nix(OS) otherwise already.
