---
layout: post
title: "Ansible Tutorials"
date: 2025-06-28 09:31:50 +0200
comments: true
categories: ["dev"]
---



## Tutorials

### Use Ansible Agentless to Get Uptime from Remote Machines

In this minimal tutorial, we’ll use Ansible in its agentless mode to connect to remote machines and retrieve their uptime.

Code: ~/SRC/ANSIBLE/example_ansible_with_devenv

**Step 1: Create an Inventory File**

Create a file named `hosts`:

```ini
[servers]
192.168.1.100 ansible_user=your_user
192.168.1.101 ansible_user=your_user
```

Replace the IPs and usernames with your actual remote machines and SSH users.

**Step 2: Run the Ad-Hoc Command**

Use Ansible’s command module to fetch the uptime: 

```bash
ansible -i hosts servers -m command -a "uptime"
```

This command uses SSH to connect to the servers, runs the uptime command, and returns the result.

What You Learned
	•	How to define an inventory of remote machines
	•	How to use Ansible agentlessly via SSH
	•	How to retrieve simple system info with an ad-hoc command

⸻

Let me know if you’d like a visual aid or a code block ready to copy into your editor.


### AWS and Ansible {#aws-and-ansible}

Use AWS Systems Manager to execute complex Ansible playbooks:  
[https://aws.amazon.com/about-aws/whats-new/2019/09/now-use-aws-systems-manager-to-execute-complex-ansible-playbooks/](https://aws.amazon.com/about-aws/whats-new/2019/09/now-use-aws-systems-manager-to-execute-complex-ansible-playbooks/) 
