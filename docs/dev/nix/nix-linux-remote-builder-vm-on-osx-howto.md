
# NixOS Linux Remote Builder VM on macOS

## HOW to setup a NixOS Linux Remote Builder VM on macOS
GOAL: Run a NixOS VM in the background on your macOS system to build `aarch64-linux` and `x86_64-linux` derivations.


Prerequisites:

* macOS version 12.4 or later.
* macOS system with Nix installed.
* Administrative privileges to configure system settings.

To set up a remote Linux builder VM on macOS using Nix, you can alternatively:

* Version 1: use the nix-darwin module that makes enabling the linux-builder VM and doing all the setup a declarative one-liner. If are already using nix-darwin, **this is the preferred solution**.
* Version 2: use the `darwin.linux-builder` package from Nixpkgs. This package simplifies the creation and management of a Linux VM on macOS, enabling you to build Linux packages directly from your Mac.

### VERSION 1: using the nix-darwin configuration

see [nix-linux-remote-builder-vm-on-osx-explanation.md](nix-linux-remote-builder-vm-on-osx-explanation.md) for more details about the variables.

In July 2023, NixOS contributor [Enzime](https://github.com/enzime) [upstreamed a nix-darwin module](https://github.com/LnL7/nix-darwin/commit/d2b01ab455cb3fcae531fecc5fd23947dd102065) that makes enabling the linux-builder VM and doing all the setup a declarative one-liner.

Just add the following to your nix-darwin configuration file:

```nix
 nix = {
        # Enable Linux builder support in nix-darwin.
        linux-builder = {
            enable = true;
            # ephemeral VM removes the VM after a reboot
            ephemeral = true;
        };
        # This line is a prerequisite for linux-builder
        settings.trusted-users = [ "@admin" ];
      };
```

#### Check the setup is working

for aarch64-linux:

```
$ nix build \
  --impure \
  --expr '(with import <nixpkgs> { system = "aarch64-linux"; }; runCommand "foo" {} "uname -a > $out")'
$ cat result
Linux localhost 6.1.72 #1-NixOS SMP Wed Feb 12 16:10:37 UTC 2024 aarch64 GNU/Linux
```

for x86_64-linux:

```
$ nix build \
  --impure \
  --expr '(with import <nixpkgs> { system = "x86_64-linux"; }; runCommand "foo" {} "uname -a > $out")'

$ cat result
Linux localhost 6.1.72 #1-NixOS SMP Wed Feb 12 16:10:37 UTC 2024 x86_64 GNU/Linux
```

#### Tune the setup of the linux-builder VM

> [!NOTE] 
> Now that we have a linux-builder VM running, we can tune its setup because we can now use the VM to build new versions of the VM.

You can make the builder faster by giving it more CPUs, RAM, and a bigger disk image (the defaults are 1 CPU core, 3GB RAM, and 20GB disk), we can simply extend our nix-darwin configuration:

```nix
nix.linux-builder = {
    enable = true;
    # ephemeral VM removes the VM after a reboot
    ephemeral = true;
    # enable the linux-builder for the systems aarch64-linux and x86_64-linux
    systems = [ "aarch64-linux" "x86_64-linux" ];
    maxJobs = 4;
    config = {
      virtualisation = {
        darwin-builder = {
          diskSize = 40 * 1024;
          memorySize = 8 * 1024;
        };
        cores = 6;
      };
    };
  };
}
```
In this example, we give the Linux builder 6 CPU cores, 8GB RAM, and 40GB disk size
The `maxJobs` variable sets the [`nix.buildMachines.linux-builder.maxJobs`](https://daiderd.com/nix-darwin/manual/index.html#opt-nix.buildMachines._.maxJobs) config attribute that defines how many jobs may be delegated to this builder concurrently.

see [nix-linux-remote-builder-vm-on-osx-explanation.md](nix-linux-remote-builder-vm-on-osx-explanation.md) for more details about the variables.

### VERSION 2: The Linux Builder in nixpkgs
 
see [nix-linux-remote-builder-vm-on-osx-explanation.md](nix-linux-remote-builder-vm-on-osx-explanation.md) for more details about the variables and the internal of the module.

As the official [NixOS documentation of the `darwin.linux-builder` package](https://nixos.org/manual/nixpkgs/stable/#sec-darwin-builder) states, it just needs to be run and can then be set up as a remote builder.

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


## 