
## Nicola's Day by Day Usage ⭐⭐⭐


[Personal NixOS Config](https://github.com/breezeight/breezeight-nix-darwin-config/blob/main/README.md): 
  - `cd ~/breezeight-nix-darwin-config && nix run nix-darwin -- switch --flake .`

[Tmux](dev/tmux.md)



## Development Best Practices

Very important ⭐⭐⭐:

* [DevOps And DevSecOps Culture Explanation](dev/development_best_practices/devops_and_devsecops_culture_explanation.md)


## Authentication and Authorization

Services:

* [Keycloak](dev/authetication_and_authorization/keycloak-explanation.md)
* [OAuth2 Proxy](dev/authetication_and_authorization/oauth2-proxy.md)

Protocols:

* [OAuth 2 Explanation](dev/authetication_and_authorization/oauth2-explanation.md)
* [OIDC Explanation](dev/authetication_and_authorization/oidc-protocol-explanation.md)

## AWS

[AWS](dev/aws.md)

### HOWTOS

Credentials:

* [AWS IAM Credentials 1Password](dev/aws/aws-howto-iam-credentials-1password.md): How to Use 1Password to Securely Store Your AWS credentials

S3:

* [AWS S3](dev/aws/aws-howto-s3-download-upload-files.md)


## Python

[NICOLA's LEGACY GOOGLE docs](https://drive.google.com/drive/u/1/folders/1E5SPSk__OBUlzkI0crqYYpp00ZtX702W):

- [\[GUIDE\] Python Libraries for AI and Data Science](https://drive.google.com/open?id=1g21eheWYwJ5cmx7aBnUP1tb8273QiWuau8l5B4Mcm5A&usp=drive_copy)
- [\[GUIDE\] Python Optimization and Profilers](https://drive.google.com/open?id=1vYvuQ0ysCib_QUqEnqSNxvc8jwOMKseMQFsbRua3rQQ&usp=drive_copy)
- [Python Ecosystem Addictive Best Practices.md](https://drive.google.com/open?id=10hcTGoiNRBIGbrFAThwi2SP2LCexFjlr&usp=drive_copy)
- [\[GUIDE\] Django](https://drive.google.com/open?id=1lKWZD3xmjfkkxQRjPl1jw_D4cWT65T9jEtE-alYozHo&usp=drive_copy)
- [\[GUIDE\] Python - DevOps](https://drive.google.com/open?id=1ieHAj7gzka9vSHhiSwOkyuyq_4UpAheN9QjJKQTiQ_8&usp=drive_copy)
- [\[GUIDE\] FastAPI: rest and grapql](https://drive.google.com/open?id=1d3F_p_xT-88ybr0DuZfgM6QwyezfcSK3F1F-90wOH7o&usp=drive_copy)
- [\[GUIDE\] Python Learning Path](https://drive.google.com/open?id=1EHLEXq6bvdgOrvUPGygXsUeAf4azMKYuHaaZWxbDeNw&usp=drive_copy)
- [Django Learning Materials](https://drive.google.com/open?id=1aAuy55LzI5xI1RF8Fv67TBJOc1ArRFGm&usp=drive_copy)

### Learning Python Language and Standard Library

[🌟 SEE NICOLA'S NOTES about python language and standard library 🌟](dev/python-language-reference-nicola/python-learning.md)
- This is my personal notes about python language and standard library. The one that I use to learn python and to understand the big picture.


These links are tentative of make AI summarize the python language reference. THE PROBLEM is that the original text is meant to be read by developers of the core of language, so it **is too technical**:
- [python-official-language-reference-with-ai](python-official-language-reference-with-ai.md): this is tentative of make AI summarize the python language reference. THE PROBLEM is that the original text is meant to be read by developers of the core of language, so it **is too technical**.

### Pythons Devops - Packaging - Dependencies management

* [Python Devops](https://docs.google.com/document/d/1ieHAj7gzka9vSHhiSwOkyuyq_4UpAheN9QjJKQTiQ_8/edit?tab=t.0#heading=h.v1qbc2g302w8)

General explanation:
* [Python Packaging Explanation](dev/python-language-reference-nicola/python-packaging-explanation.md)

Specific tools:

* [uv explanation](dev/python-language-reference-nicola/uv-explanation.md)

### Python Webserver

* [Python Webserver Explanation](dev/python-language-reference-nicola/python-webserver-explanation.md)

### Django

* [Django](dev/django/django-settings-best-practices-explanation.md)
* [Django Celery](dev/python/celery-explanation.md)

### Distributed Systems

* [Django Celery](dev/python/celery-explanation.md)


### Python Type Hints

* [Python Type Hints Explanation](dev/python-language-reference-nicola/stdlib-devtools-typing-explanation.md): this is a high level explanation of type hints, a good starting point to understand the big picture.
* [Python Type Hints HOWTO](dev/python-language-reference-nicola/stdlib-devtools-typing-howto.md): how to use type hints in practice.
* [Python Type Hints Reference](dev/python-language-reference-nicola/stdlib-devtools-typing-reference.md): reference of all type hints.
* [Python Type Hints Tutorial](dev/python-language-reference-nicola/stdlib-devtools-typing-tutorial.md): tutorial to learn type hints.

## Virtualization and Containers

[Docker](dev/docker.md)

[Docker Compose](dev/docker-compose.md)

[Docker and Docker Compose arguments and environment variables management in complex projects](dev/docker-and-docker-compose-arg-env-management-in-complex-project.md)

## Nix

[Nix](dev/nix/nix.md)

Breezeight NixOS Config on OSX:

* **[Breezeight Nix Config](dev/nix/nix-breezeight-config-osx-and-linux-overview.md)**
* [Nix Darwin Overview](dev/nix/nix-darwin-overview.md)

Home Manager Day by Day Usage:

* [Home Manager Configuration Overview and Options](dev/nix/nix-homemanager-configuration-overview-and-options.md)
* [Home Manager Nix Darwin Module Docs](dev/nix/nix-homemanager-nix-darwin-module-docs.md): links to the official docs + some notes.

Home Manager Explanations and introductions:

* [Home Manager Overview](dev/nix/nix-homemanager-overview-explanation.md): good to explain the big picture and to undestand the usage context, good for new users.
* [GOOGLE DOC : Home Manager Configuration Overview and Options](https://docs.google.com/document/d/1UN77X-g7uTlgCRNU03Tnw4ao74hmc1oUxqYR-4kH6SA/edit?tab=t.0): 
    * Document Overview
    * Installation
    * General overview of Home-Manager
    * Home-Manager internals
    * Home-manager modules notes
    * Frequent Jobs
    * [JOB]
    * Home-Manager for Darwin
    * darwin-rebuild
    * Install OSX in UTM
    * Connect via ssh
    * mac configuration
    * nix-darwin config
    * Understanding nix-darwin and Home Manager
    * [Darwin] Homebrew Module
    * [Darwin] system.defaults
    * Home-manager config
    * Home Manager Modules
    * nixos-hardware
    * Direnv
    * Home Module
    * Packages vs modules
    * home.stateVersion
    * Module to install DEVENV using flake
    * Upgrading Home-Manager
    * Impermanence and Home-Manager
    * Home Manager Standalone Internals
    * Profiles
    * The Flake Structure and how it’s used
    * The Breezeight Parent module
    * Global Module
    * Session Settings
    * Persistence Configuration
    * Features Modules
    * Features Modules - CLI - Overview
    * Features Modules - CLI - git.nix
    * Features Modules - CLI - gpg.nix
    * Features Modules - CLI - ssh.nix
    * Tooling and applications
    * Misterio77’s Configurations



Remote Linux Builders:

* [Nix Linux Remote Builder VM](dev/nix/nix-linux-remote-builder-vm-on-osx-howto.md)


Bootstrap a Nixos system:

* [Nix Bootstrap NixOS](dev/nix/nix-bootstrap-nixos-howto.md)
* [Nix Bootstrap NixOS Explanation](dev/nix/nix-bootstrap-nixos-explanation.md)

## Security and cryptography

Explanations:

* [Cryptography, passwords, hashing, salting, encryption](dev/cryptography-passwords-hashing-salting-encryption.md)

* [PGP GPG](dev/cryptography-pgp-gpg.md)

* [SSH](dev/cryptography-ssh.md): 
  
    - Main Topics: SSH Protocol and SSH Keys concepts, Public-key cryptography explanation, SSH host keys, Best practices for SSH keys, SSH Agent overview and usage
    - HOWTOs **SSH Keys**: How to get SSH Key Fingerprint, How to use a specific private key to SSH into a remote server, How to generate Ed25519 Key, How to organize SSH keys and config in subfolder `~/.ssh/my_project`
    - HOWTOs **SSH Agent**: How to configure the ssh-agent, How to add a key to your ssh-agent, How to use SSH Agent with AWS SSM (marked as TODO)
    - **Security Best Practices**: How to keep private keys private, How to use 1Password to protect private keys, How to use passphrases and add keys to ssh-agent, How to keep track of actively used SSH keys, How to rotate SSH keys
    - Additional Topics: SSH host key verification, SSH Agent Forwarding, Git SSH configuration, Specific SSH Agents (1Password Agent), SSH agent on OSX, Tailscale SSH key generation (marked as WIP)

* [SSH Tunneling - SSH port forwarding](dev/cryptography-ssh-tunneling-ssh-port-forwarding.md)



## Most important HOWTOs

* [SSH](dev/cryptography-ssh-basic-howto.md)
  * create and use SSH keys with 1Password or other tools
