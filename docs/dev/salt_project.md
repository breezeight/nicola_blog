---
layout: post
title: "Salt Stack"
date: 2014-03-16 19:59:15 +0100
comments: true
categories: ["orchestration"]
---


# Salt


> **⚠️ Important Notice:**
>
> **Salt has been acquired by VMware, and there are concerns about the community's decline. It is strongly advised to consider alternative solutions for configuration management and orchestration. DO NOT USE Salt for new projects.**

> **Consider exploring other tools such as Ansible, Puppet, or Chef, which have robust community support and active development.**




## Reference

Official Salt Projects docs:

- [Docs](https://docs.saltproject.io/en/latest/contents.html)


## Intro

Salt is:

* a configuration management system, capable of maintaining remote nodes in defined states (for example, ensuring that specific packages are installed and specific services are running)
* a distributed remote execution system used to execute commands and query data on remote nodes, either individually or by arbitrary selection criteria


* Salt execution routines can be written as plain Python modules.


* For the ssh config see the roster part below 


## Roster: host configuration

### SSH config

To parse an existing "ssh config" file, you can use the `ssh_config` module: https://docs.saltproject.io/en/master/ref/roster/all/salt.roster.sshconfig.html


#### 🔧 How to Choose Between `sshconfig` and `ssh_options` in Salt SSH

This guide shows you how to select the appropriate SSH configuration method for your Salt SSH setup — either using the `sshconfig` roster plugin or defining `ssh_options` in a flat `hosts.yml` roster.

##### 🧭 Choose Based on Your Setup

> Warning: we got many issues with the `sshconfig` roster plugin (not finding the host, cannot list hosts, etc).
> 
> We use the `ssh_options` roster plugin instead.

✅ Use `sshconfig` If:

* You already have a well-structured `~/.ssh/config` file.
* You want Salt to automatically parse options like `Host`, `User`, `ProxyCommand`, `IdentityFile`, etc.
* You prefer to avoid writing YAML for host definitions.

To use:

```bash
salt-ssh --roster=sshconfig ...
```

2. Create or edit a master config file

In ~/.salt/pdb/master, add this:

```yaml
ssh_config_file: $HOME/.ssh/pdb/config
```

> *Tip: Best suited for existing SSH setups and environments with bastion hosts.*

---

✅ Use `ssh_options` If:

* You need to manually override or add SSH options for each host.
* You're working with a minimal or test environment.
* You're not using an SSH config file.

Define `ssh_options` in your `hosts.yml` file, for example:

```yaml
myhost:
  host: 192.168.1.10
  user: saltuser
  ssh_options:
    - "-o LogLevel=DEBUG"
    - "-o ConnectTimeout=10"
```

> *Tip: Use this method for custom testing or to inject advanced SSH flags per host.*

---

##### ⚠️ Don’t Mix Them

* If you use `--roster=sshconfig`, any `ssh_options` in `hosts.yml` will be ignored.
* If you're using a flat YAML roster, only `ssh_options` in that file are respected.

---

##### 📋 Summary Comparison

| Feature                 | Flat YAML Roster (`ssh_options`) | `sshconfig` Roster |
| ----------------------- | -------------------------------- | ------------------ |
| Uses `~/.ssh/config`    | ❌                                | ✅                  |
| Uses `ssh_options`      | ✅                                | ❌ (ignored)        |
| Manual per-host setup   | ✅                                | ❌ (automatic)      |
| Good for simple testing | ✅                                | ✅                  |
| Good for bastion setups | 🚫 painful                       | ✅ seamless         |

---

Choose the style that matches your environment. For flexibility, you can script Salt to switch between rosters as needed.

### HOWTO - Debug the actual SSH command used by salt-ssh

grep the actual SSH command used by salt-ssh:

```bash
salt-ssh --config-dir=./etc '*' -i cmd.run 'uptime' -l trace 2>&1 | grep "\[TRACE   \] Terminal Command:"
```


## TUTORIAL - 

Convetions:

- `$PRJ_ROOT` is the root of your project

### 🧰 Requirements

- Python 3 installed
- salt-ssh installed

#### Requirement with devenv.sh

```bash
cd $PRJ_ROOT
devenv init
git add devenv.* devenv.* .gitignore .envrc
```

Add salt package to devenv:

```nix
  # https://devenv.sh/packages/
  packages = [
    pkgs.git
    pkgs.salt
  ];
```

If you have `direnv` configured the deven shell should be rebuilt automatically. 
Otherwise test your env with `devenv test`.

Test you have salt installed in the `devenv shell`: `salt-ssh -V`


### 🪜 Step-by-Step Setup

1. Create a working subdir for salt in your project

```bash
mkdir -p salt/{etc,roster,log}
cd salt
salt-ssh
```

2. Create master config in `$PRJ_ROOT/salt/etc/master`

```yaml
# $PRJ_ROOT/salt/etc/master
root_dir: .
ssh_log_file: ./log/ssh.log
roster_file: ./roster/hosts.yml
```

3. Create a roster file in `$PRJ_ROOT/salt/roster/hosts.yml`

Simple:

```yaml
# $PRJ_ROOT/salt/roster/hosts.yml
```

If you need more advanced configuration see the [roster file documentation](https://docs.saltproject.io/en/latest/ref/roster/all/salt.roster.yaml.html).







## TUTORIAL - 


