## HOWTO: Remote Bootstrap of a NixOS Physical Machine (laptop)
> [!NOTE] 
> Explanation of the process: can be found [here](nix-bootstrap-nixos-explanation.md)

Definitions:

* `CONTROL_HOST`: the hostname of the host from where we are going to run the bootstrap process (you main laptop, a ci server, ...).
* `TARGET_SYSTEM`: the hostname of the target system where we are going to bootstrap NixOS.
* `IP_OF_TARGET_SYSTEM`: the IP address of the target system

**Prerequisites:**

> [!WARNING]
>  the below prerequisites are very important to follow, otherwise the bootstrap process will fail.

* If `CONTROL_HOST` is an OSX system and the `TARGET_SYSTEM` is linux, you need to setup a remote builder on the `CONTROL_HOST`. See [Nix Linux Remote Builder VM on OSX Howto](nix-linux-remote-builder-vm-on-osx-howto.md) for details. Depends on the architecture of the target system you may need the x86_64 or aarch64 version of the builder.

**Boot and ssh setup:**

* Create a bootable USB stick of NixOS from Minimal ISO image choosing the architecture of the target system.
* Boot the target system from the bootable USB stick of NixOS and choose the installer option from the GRUB menu. Now you should see a shell prompt and you should be logged as `nixos` user, the standard user created by nixos-installation process.
* Set the password for the `root` (you can use a simple password, it will be used only for the bootstrap process).:
```bash
sudo su
passwd
```
* use `ip addr` to find the current `IP_OF_TARGET_SYSTEM`.
* deploy your public ssh key to connect to the target system from the control host using the `root` user:

```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub nixos@IP_OF_TARGET_SYSTEM
```

* Now try logging into the target system without password: `ssh nixos@IP_OF_TARGET_SYSTEM`

**Bootstrap:**

* cd to the folder of the repo: `cd SRC/NIX/nixos-homemanager-examples/misterio77-nix-config/`, it contains the flake we are going to use to bootstrap the target system.
* enter the development shell defined shell.nix: `nix develop`
* run the bootstrap command: `scripts/nix-anywhere-bootstrap.sh`


scripts/nixos-anywhere-bootstrap.sh . precision root 192.168.1.62


## HOWTO: create a bootable USB stick of NixOS

* install balenaEtcher
* download the ISO of NixOS from https://nixos.org/download/
* insert the USB stick
* select the ISO and click on Flash

