## Intro and design choices

These are the main commands we are going to use during and after bootstrap:

* `nixos-rebuild --flake .` To build system configurations
* `home-manager --flake .` To build user configurations
* `nix build (or shell or run)` To build and use packages

To manage secrets we use:

* `sops`

We started from the repo of Misterio77, we adapted it to our needs, this a list of what we keep and what we changed:

* we keep the same structure of the hosts
* we added `nixos-anywhere` to bootstrap remote servers and laptops
(we have been inspired by [quickstart](https://github.com/nix-community/nixos-anywhere/blob/main/docs/quickstart.md) which introduce to disko). `nixos-anywhere` is used to bootstrap remote servers and laptops and it uses `disko` to manage disks layout in a NixOS system


Related documentation:
* [\[GUIDE\] Disko and nixos-anywhere](https://docs.google.com/document/d/179hsAkcmAp6d3KSqKcLyY1Io40wSnDWM-NelOseD8SU/edit#heading=h.2lcldkbbkoly)

## Remote Bootstrap of a NixOS Physical Machine (laptop)

This section is the explanation of the process: [Nix Bootstrap NixOS](nix-bootstrap-nixos-howto.md)

As stated in the introduction, this procedure is based on `nixos-anywhere` and which is usefult both to bootstrap remote servers and laptop.

It expects that the target system where we are going to bootstrap NixOS is booted from a NixOS installation:
* for laptops we can use the live ISO of NixOS
* for servers ????



scripts/nixos-anywhere-bootstrap.sh
scripts/nixos-anywhere-bootstrap-common.sh

TODO: explain why the remote builder is needed: if you want to build NixOS images on your local machine, you need a remote builder because the disko derivation does not work on macOS:
```bash
derivation: zfr6nbjcfm3qwm0lskmn0md73frln4nb-disko.drv
required (system, features): (x86_64-linux, [])
1 available machines:
(systems, maxjobs, supportedFeatures, mandatoryFeatures)
([aarch64-linux], 1, [benchmark, big-parallel, kvm], [])
error: a 'x86_64-linux' with features {} is required to build '/nix/store/zfr6nbjcfm3qwm0lskmn0md73frln4nb-disko.drv', but I am a 'aarch64-darwin' with features {apple-virt, benchmark, big-parallel, nixos-test}
```




https://nixos.org/download/


Possible future improvements:
* https://github.com/users/breezeight/projects/4/views/2?pane=issue&itemId=85625765




