---
layout: post
title: "Networking Intro"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["networking"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# References

* [Easy intro](http://www.linuxhomenetworking.com/wiki/index.php/Quick_HOWTO_:_Ch02_:_Introduction_to_Networking#.VT0cJ1OUdLM)


# TCP/IP

* All TCP/IP enabled devices connected to the Internet have an Internet Protocol (IP) address
* `NIC` Network Interface Cards. Your network interface card is also frequently called a NIC.
* `MAC Address` can be equated to the serial number of the NIC.
* Every IP packet is sent out of your NIC wrapped inside an Ethernet frame that uses MAC addresses to direct traffic on your locally attached network. MAC addresses therefore have significance only on the locally attached network. As the packet hops across the Internet, its source/destination IP address stays the same, but the MAC addresses are reassigned by each router on the way using a process called ARP.

## ARP

TODO: http://www.linuxhomenetworking.com/wiki/index.php/Quick_HOWTO_:_Ch02_:_Introduction_to_Networking#.VT0cJ1OUdLM

## Router

By connecting its NIC cards to multiple LANs, a correctly configured router is capable of relaying traffic between networks.

In the broader networking sense, a `route` refers to the path data takes to traverse from its source to its destination.

Each router along the way may also be referred to as a `hop`.

# NAT

* network address translation (NAT). Is often also called IP masquerading in the Linux world.

New connections initiated from the Internet to the public IP address of the router/firewall face a problem. The router/firewall has no way of telling which of the many home PCs behind it should receive the relayed data. `Port forwarding` is a method of counteracting this. For example, you can configure your router/firewall to forward TCP port 80 (Web/HTTP) traffic destined to the outside NAT IP to be automatically relayed to a specific server on the inside home network

# DNS

See "[Guide] Networking" on my evernote

## DNSmasq Local DNS for development

Ref:

* http://davebaker.me/articles/setting-up-a-local-dns-server-on-osx
* https://mallinson.ca/osx-web-development/

$ brew install dnsmasq
$ echo 'address/.loc/127.0.0.1' > /usr/local/etc/dnsmasq.conf

To configure dnsmasq, copy the example configuration to /usr/local/etc/dnsmasq.conf and edit to taste.

cp /usr/local/opt/dnsmasq/dnsmasq.conf.example `/usr/local/etc/dnsmasq.conf`

To have launchd start dnsmasq at startup:

*  sudo cp -fv /usr/local/opt/dnsmasq/*.plist /Library/LaunchDaemons
*  sudo chown root /Library/LaunchDaemons/homebrew.mxcl.dnsmasq.plist

Then to load dnsmasq now:

*  sudo launchctl load /Library/LaunchDaemons/homebrew.mxcl.dnsmasq.plist

To manually start and debug: `/usr/local/opt/dnsmasq/sbin/dnsmasq --keep-in-foreground -C /usr/local/etc/dnsmasq.conf`

* `System Preferences -> Network -> Advanced -> DNS`

* To print your dns resolver config: `scutil --dns`

* To restart : 
  * `sudo launchctl unload /Library/LaunchDaemons/homebrew.mxcl.dnsmasq.plist && sudo launchctl load /Library/LaunchDaemons/homebrew.mxcl.dnsmasq.plist`

* To check the status:
  * `sudo launchctl list | grep dnsmasq`
  * `homebrew.mxcl.dnsmasq`

### DNSmasq Config

* `domain-needed`:  This tells dnsmasq to never pass short names to the upstream DNS servers. If the name is not in the local /etc/hosts file then "not found" will be returned.
* `bogus-priv` All reverse IP (192.168.x.x) lookups that are not found in /etc/hosts will be returned as "no such domain" and not forwarded to the upstream servers.

## DNS query tools

Dig:

* use a specific DNS server, ex: 8.8.8.8: `dig @8.8.8.8 +short NS domain.com`

To lookup MX records for a domain:

* host -t mx mydomain.com
* nslookup -q=mx mydomain.com
* dig -t mx mydomain.com




# Linux Networking

http://www.linuxhomenetworking.com/wiki/index.php/Quick_HOWTO_:_Ch03_:_Linux_Networking

## IPTables

## Testing Network services with netcat

http://www.rackspace.com/knowledge_center/article/testing-network-services-with-netcat

To see if the port accepts connections: `nc -vz IP_Address Port` it will respond:

* if he connection is successfully made: `Connection to 203.0.113.96 21 port [tcp/ftp] succeeded!`
* if the connection is refused: `nc: connect to 203.0.113.96 port 80 (tcp) failed: Connection refused`
  * You'll usually see this response when the service isn’t running or a firewall is rejecting the connection or the service is not running
* if there is no response to the connection request: `nc: connect to 203.0.113.96 port 80 (tcp) failed: Connection timed out`

