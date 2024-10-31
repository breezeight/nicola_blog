## Howto generate SSH keys

### With 1password 

See the addictive internal docs or the official [1Password docs](https://developer.1password.com/docs/ssh). Benefits:

* 1Password will automatically add the key to the ssh-agent
* 1Password will keep your keys synced across all your devices
* private keys are encrypted with a master password, so they can be safely stored in the cloud
* private keys never touch your local disk **unencrypted**, so the security is better.

### Locally using standard open source tools

Ref: [How to generate SSH keys · Tailscale](https://tailscale.com/learn/generate-ssh-keys/#ssh-host-keys)  SSH keys are integral to distributed teams’ security and ability to collaborate, but setting them up for the first time can be troublesome. In this article, you’ll learn how to generate SSH keys, both with and without Tailscale.

Why do we use keys instead of passwords?  
A common and simple way to log into a remote computer via SSH is to use a password. However, passwords can be weak or insecure, and they can be brute-forced or guessed. It’s also challenging to create a new password for every single machine you log into, and using the same password repeatedly is not recommended. A more secure approach is to use SSH keys to access your computers.
