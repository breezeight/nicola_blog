# SSH Tunneling - SSH port forwarding

[Official documentation](https://www.ssh.com/academy/ssh/tunneling)

SSH tunneling (also called SSH port forwarding) is a method of transporting arbitrary networking data over an encrypted SSH connection. 


## ProxyCommand and Jump Hosts (-W)

The `-W` option in SSH is a feature that facilitates direct connections through an intermediary host, commonly referred to as a jump host or bastion host.
This method is particularly useful when accessing remote servers that are not directly reachable from your local machine but are accessible from an intermediate server.


The `-W` option instructs the SSH client to forward standard input and output to a specified host and port. This effectively allows your local SSH client to act as a proxy, directing traffic through the intermediary host to the target destination.

Syntax:

```bash
ssh -W [destination_host]:[destination_port] [jump_host]
```

- `destination_host`: The target host you wish to reach.
- `destination_port`: The port on the target host (commonly 22 for SSH).
- `jump_host`: The intermediary server through which the connection is routed.


The sequence of events:

1. Establishing the Initial SSH Connection:
	- Your local machine initiates a secure, encrypted SSH connection to the jump host at 203.0.113.10 using the specified username (user).

2. Proxying Standard Input and Output:
	- After successful authentication, the -W option directs the SSH client to establish a direct channel from your local machine to the target host (192.168.2.20) on port 22.
	- Instead of opening a shell session on the jump host, the SSH client creates an SSH connection from the jump host to the target host, forwarding your local standard input (stdin) and standard output (stdout) streams through the jump host to a shell on the target host.

3. Direct Communication with the Target Host:
	- From your perspective, **it appears as though you’re directly connected to the target host**.
	- All data transmitted from your local machine is securely tunneled through the jump host to the target host, with responses from the target host similarly tunneled back through the jump host to your local machine.

This process ensures a seamless and secure connection to the target host via the jump host, leveraging SSH’s capabilities for encrypted communication.


### Practical Example

Suppose you need to connect to a remote server at `192.168.2.20` via SSH, but direct access is restricted. However, you can access this server through a jump host at `203.0.113.10`.

Establish the Connection Using `-W` from the command line:

```bash
ssh -W 192.168.2.20:22 user@203.0.113.10
```

In this command:
- `-W 192.168.2.20:22`: Directs the SSH client to forward the connection to `192.168.2.20` on port `22`.
- `user@203.0.113.10`: Specifies the username and jump host.

### Configure SSH for Seamless Connections

To streamline the process, you can define this setup in your SSH configuration file (`~/.ssh/projectx/config`):

```bash
Host bastion
  HostName 178.239.184.110
  User ubuntu
  IdentityFile ~/.ssh/projectx/bastion.pem

Host web3-0 
  HostName 10.2.0.20
  ProxyCommand ssh -W %h:%p -F ~/.ssh/projectx/config bastion
  User ubuntu
  IdentityFile ~/.ssh/projectx/projectx-prod.pem
```

Explanation:

1.	Host bastion Configuration:
- `HostName 178.239.184.110`: Specifies the public IP address of your bastion host.
- `User ubuntu`: Indicates the username to use when connecting to the bastion host.
- `IdentityFile ~/.ssh/projectx/bastion.pem`: Points to the private key file for authenticating with the bastion host.

2.	Host web3-0 Configuration:
- `HostName 10.2.0.20`: Specifies the internal IP address of your target server within the private network.
- `User ubuntu`: Indicates the username to use when connecting to the target server.
- `IdentityFile ~/.ssh/projectx/projectx-prod.pem`: Points to the private key file for authenticating with the target server.
- `ProxyCommand ssh -W %h:%p -F ~/.ssh/projectx/config bastion`: Instructs SSH to use the bastion host as an intermediary. The `%h` and `%p` placeholders represent the hostname and port of the target server (web3-0), respectively. The `-F ~/.ssh/projectx/config` option ensures that the SSH client uses the specified configuration file when connecting to the bastion host.

How It Works:
- When you initiate a connection to web3-0 by running `ssh -F ~/.ssh/projectx/config web3-0`, the SSH client consults the configuration file for connection details.
- The `ProxyCommand` directive tells SSH to first establish a connection to the bastion host.
- Once connected to the bastion, SSH uses the `-W` option to forward the connection to `10.2.0.20` on port `22`, effectively creating a secure tunnel through the bastion to the target server.

> [!NOTE]
> Every host can have a separate configuration file.


## Types of SSH port forwarding
There are three types of SSH port forwarding:

- **Local Port Forwarding**: Forwards a connection from the client host to the SSH server host and then to the destination host port.
- **Remote Port Forwarding**: Forwards a port from the server host to the client host and then to the destination host port.
- **Dynamic Port Forwarding**: Creates a SOCKS proxy server that allows communication across a range of ports.


### Local Port Forwarding (-L)

Purpose: This section explains how to forward traffic from a local port to a remote host and port through the SSH connection.

Local port forwarding allows you to forward a port on the local (ssh client) machine to a port on the remote (ssh server) machine, which is then forwarded to a port on the destination machine.

Suppose you want to access a remote web server (listening on port 80) via port 8080 on your local machine. The command to run is as follows:


In Linux, macOS, and other Unix systems, to create a local port forwarding, pass the -L option to the ssh client:

```bash
ssh -L [LOCAL_IP:]LOCAL_PORT:DESTINATION:DESTINATION_PORT [USER@]SSH_SERVER
```

The options used are as follows:

- `[LOCAL_IP:]LOCAL_PORT` - The local machine IP address and port number. When `LOCAL_IP` is omitted, the ssh client binds on the localhost.
- `DESTINATION:DESTINATION_PORT` - The IP or hostname and the port of the destination machine.
- `[USER@]SERVER_IP` - The remote SSH user and server IP address.

Example: 

- you have a MySQL database server running on machine `db001.host` on an internal (private) network, on port 3306, which is accessible from the machine `pub001.host`,
- and you want to connect using your local machine MySQL client to the database server. 

To do so, you can forward the connection using the following command:

```bash
ssh -L 3336:db001.host:3306 user@pub001.host
```

This command will create a secure tunnel from your local machine to the remote machine, and then forward the connection from the remote machine's port 3306 to your local machine's port 3336.

Once entered, you will be logged into the remote server, and the SSH tunnel will be established.

You can now connect to the database server using your local MySQL client, connecting to `localhost:3336`.

You can forward multiple ports to multiple destinations in a single ssh command: `ssh -L 3336:db001.host:3306 3337:db002.host:3306 user@pub001.host`

#### Troubleshooting

If you are having trouble setting up tunneling, check your remote SSH server configuration and make sure `AllowTcpForwarding` is not set to `no`. By default, forwarding is allowed.

### Remote Port Forwarding (-R)

Purpose: This section covers how to use SSH to forward a port from the remote server to the local machine.

Remote port forwarding is the reverse of local port forwarding. It allows you to forward a port on the remote (ssh server) machine to a port on the local (ssh client) machine, which is then forwarded to a port on the destination machine.

In Linux, macOS, and other Unix systems to create a remote port forwarding, pass the -R option to the ssh client:

```bash
ssh -R [REMOTE:]REMOTE_PORT:DESTINATION:DESTINATION_PORT [USER@]SSH_SERVER
```

The options used are as follows:

- `[REMOTE:]REMOTE_PORT` - The IP and the port number on the remote SSH server. An empty REMOTE means that the remote SSH server will bind on all interfaces.
- `DESTINATION:DESTINATION_PORT` - The IP or hostname and the port of the destination machine.
- `[USER@]SERVER_IP` - The remote SSH user and server IP address.

Remote port forwarding is mostly used to give access to an internal service to someone from the outside.

Example:
- you are developing a web application on your local machine, and you want to show a preview to your fellow developer. 
- You do not have a public IP, so the other developer can’t access the application via the Internet.

If you have access to a remote SSH server, you can set up a remote port forwarding as follows:

```bash
ssh -R 8080:127.0.0.1:3000 -N -f user@remote.host
```

The command above will make the ssh server listen on port 8080, and tunnel all traffic from this port to your local machine on port 3000.

Now your fellow developer can type `remote.host:8080` in his/her browser and preview your awesome application.

#### Troubleshooting
If you are having trouble setting up remote port forwarding, make sure `GatewayPorts` is set to `yes` in the remote SSH server configuration.


### Dynamic Port Forwarding (-D)
https://linuxize.com/post/how-to-setup-ssh-tunneling/#dynamic-port-forwarding

Purpose: This section covers how to use SSH to create a dynamic SOCKS proxy for routing traffic to multiple destinations.

TODO: non so bene come funziona e quando si usa... sembra un modo per fare tunneling di tutto ma richiede che il client supporti SOCKS... (per esempio alcuni browser supportano SOCKS)

#### Why Choose Remote Over SOCKS?

	1.	Exposing a Local Service to a Remote Machine: Remote port forwarding allows services running on your local machine to be accessible to the remote server. Example: Making a local web application available to a team or exposing a local development server.
	2.	Simplifying Access to a Single Destination: If you only need to forward traffic to a specific destination, remote port forwarding is simpler to configure.


#### Why Choose SOCKS Over Remote Forwarding?

Here are specific scenarios where a SOCKS proxy is the better option:
	1.	Dynamic Destinations: If you need to connect to multiple remote hosts and ports, SOCKS is much more flexible. Remote port forwarding would require separate SSH commands for each destination.
	2.	Application-Level Proxy Support: Many applications, such as browsers, can natively support SOCKS proxies, making configuration easy and seamless.
	3.	Web Browsing: SOCKS is ideal for secure and private web browsing, allowing you to route all traffic through a bastion or intermediary server.
	4.	Bypassing Geo-Restrictions: A SOCKS proxy is more versatile for bypassing restrictions because it allows dynamic routing to any destination through the SSH server.
	5.	Simpler Setup for Multiple Protocols: SOCKS supports a variety of protocols (TCP, UDP, DNS), whereas remote port forwarding typically supports only TCP.
