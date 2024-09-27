---
layout: post
title: "Tmux"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["devops"]
---

# Tmux

## References

> **WARNING** This Markdown document supersedes the [GDOC GUIDE Tmux + iTerm2 + tmate; Teamviewer, Guacamole](https://docs.google.com/document/d/1EHUvoAgCCJvn9Jo1bXkELNAkJShNzJSWh4Reum-OAyQ/edit#heading=h.cr0ozfdz6c13). The Google Document is kept as a backup and archive only.

* https://www.ocf.berkeley.edu/~ckuehl/tmux/
* https://gist.github.com/MohamedAlaa/2961058

* `ctrl-b, %`	split the screen in half from top to bottom
        * `ctrl-b, "`	split the screen in half from left to right
* `ctrl-b, x`	kill the current pane
* `ctrl-b, <arrow key>`	switch to the pane in whichever direction you press
* `ctrl-b, d`	detach from tmux, leaving everything running in the background

* start new: `tmux`
* start new with session name: `tmux new -s myname`
* attach: `tmux a  #  (or at, or attach)`
* attach to named: `tmux a -t myname`
* list sessions: `tmux ls`
* kill session: `tmux kill-session -t myname`
* Kill all the tmux sessions: `tmux ls | grep : | cut -d. -f1 | awk '{print substr($1, 0, length($1)-1)}' | xargs kill`

# TMux Guide

[https://leanpub.com/the-tao-of-tmux/read](https://leanpub.com/the-tao-of-tmux/read)

## Cheatsheet

[tmux shortcuts & cheatsheet](https://gist.github.com/MohamedAlaa/2961058)

SEE [Addictive CheatSheet](https://docs.google.com/spreadsheets/d/1djRw_h59QMNhzqJwxE89USJsdWIq4QHy-13NbCT9uFA/edit#gid=0&range=1:1) 

**Close a specific session**  
use tmux list-sessions to identify the session you want to kill, and then use **tmux kill-session \-t targetSession** to kill that specific session. Also you can grossly kill all tmux processes with pkill \-f tmux.

To switch to the previous window (according to the order in your status bar) use C-b p, to switch to the next window use C-b n.  
use C-b \<number\> where \<number\> is the number in front of the window’s name in your status bar.

You can also use C-b D to have tmux give you a choice which of your sessions you want to detach. 

tmux ls

tmux attach \-t 0

your sessions a more meaningful name  
tmux new \-s database

Rename:  
tmux rename-session \-t 0 database  
tmux attach \-t database

C-b ? to see a list of all available commands and start experimenting.

Some of the commands that I’m using myself quite often are:

## Pane title and color

Color: [https://stackoverflow.com/questions/25532773/change-background-color-of-active-or-inactive-pane-in-tmux/33553372\#33553372](https://stackoverflow.com/questions/25532773/change-background-color-of-active-or-inactive-pane-in-tmux/33553372#33553372)  
Pane Title: [https://stackoverflow.com/questions/9747952/pane-title-in-tmux](https://stackoverflow.com/questions/9747952/pane-title-in-tmux) 

Tmuxp example:

See here for the below example [https://docs.google.com/document/d/1UNb7OPMHhYYCWbRWfjfUkawubjwQ7YstOG9-RRFKopY/edit\#heading=h.689q4xim9a3l](https://docs.google.com/document/d/1UNb7OPMHhYYCWbRWfjfUkawubjwQ7YstOG9-RRFKopY/edit#heading=h.689q4xim9a3l)

* gives a name to every pane

session\_name: red\_blue\_namespaces  
windows:  
  \- window\_name: dev window  
    layout: tiled  
    \#shell\_command\_before:  
    \#  \- cd \~/ \# run as a first command in all panes  
    panes:  
      \- shell\_command: \# pane TCPDUMP RED   
          \- tmux select-pane \-T "TCPDUMP veth-red"  
          \- sudo ip netns exec red bash  
          \- tcpdump \-ni veth-red \-v  \-l \-e  
      \- shell\_command: \# pane TCPDUMP RED BR  
          \- tmux select-pane \-T "TCPDUMP veth-red-br"  
          \- sudo tcpdump \-ni veth-red-br \-v  \-l \-e  
      \- shell\_command: \# pane TCPDUMP BLUE  
          \- tmux select-pane \-T "TCPDUMP veth-blue"  
          \- sudo ip netns exec blue bash  
          \- tcpdump \-ni veth-blue \-v  \-l \-e  
      \- shell\_command: \# pane TCPDUMP BLUE  
          \- tmux select-pane \-T "TCPDUMP veth-blue-br"  
          \- sudo tcpdump \-ni veth-blue-br \-v  \-l \-e  
      \- shell\_command: \# pane PING  
          \- tmux select-pane \-T "PING from blue to red"  
          \- sudo ip netns exec blue bash  
          \- ping 192.168.15.1

### Intro

Ref:

* man tmux

tmux is a terminal multiplexer. It enables a number of terminals to be created, accessed, and controlled from a single screen.

It is useful for system administrators for running more than one command-line program at the same time. One useful feature of tmux is that it can be [detached from a screen](https://www.tecmint.com/run-linux-command-process-in-background-detach-process/) and continue running in the background, then later reattached. In this regard, it allows [SSH sessions to remain active](https://www.tecmint.com/keep-remote-ssh-sessions-running-after-disconnection/) even after disconnecting from the console.  
   
In tmux:

* **Session** : is a container for individual consoles being managed by tmux. A session is a single collection of pseudo terminals (one per window) under the management of tmux.  
* **Window**: Each session has one or more windows linked to it and a window fills the entire screen. Each of which is a separate pseudo terminal. A window occupies the entire screen and may be split into rectangular panes, each of which is a separate pseudo terminal   
* **Pane** : you may split a window into several rectangular panes (either vertically or horizontally).

Each pane has a separate pseudo terminal:  
![][image1]

When tmux is started it creates a **new session** with a single window (and a single pane) and displays it on screen.  
Within one terminal window you can:

* create another window in the same session  
* create additional panes  (split-views)

tmux may be **detached** from a screen and continue running in the background, then later **reattached**.

Each pane will contain its own, independently running terminal instance.   
This allows you to have multiple terminal commands and applications running visually next to each other without the need to open multiple terminal emulator windows.

Any number of tmux instances may connect to the same session, and any number of windows may be present in the same session.

Once all sessions are killed, tmux exits.

Each session is persistent and will survive accidental disconnection (such as ssh(1) connection timeout) or intentional detaching (with the \`C-b d' key strokes).

You can **exit a session** at any point. This is called “**detaching**”. tmux will keep this session alive until you kill the tmux server (e.g. when you reboot)

At any later point in time you can pick that session up exactly from where you left it by simply “**attaching**” to that session.

SSH NOTE:  When you lose your ssh connection the tmux session will simply be detached but will keep running on the server in the background including all the processes that run within your session. 

Ref:  
[https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/](https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/)  

## Server

## Tmux Restoring Window

[https://unix.stackexchange.com/questions/61386/creating-launchable-tmux-configurations](https://unix.stackexchange.com/questions/61386/creating-launchable-tmux-configurations) 

### Tmuxp

#### Doc

#### Examples

Container debug session:  
[\[GUIDE\] Linux - Container, Namespaces](https://docs.google.com/document/d/1UNb7OPMHhYYCWbRWfjfUkawubjwQ7YstOG9-RRFKopY/edit#bookmark=id.9yvlt24suo7)

* pane naming and colors

## Install

sudo apt install tmuxp

## Load Session

[https://github.com/tmux-python/tmuxp\#load-a-tmux-session](https://github.com/tmux-python/tmuxp#load-a-tmux-session)

## Tmux resurrect

[https://github.com/tmux-plugins/tmux-resurrect](https://github.com/tmux-plugins/tmux-resurrect)

## Tmux continuum

[https://github.com/tmux-plugins/tmux-continuum](https://github.com/tmux-plugins/tmux-continuum) 

## Tmux.conf guide

[https://www.hamvocke.com/blog/a-guide-to-customizing-your-tmux-conf/](https://www.hamvocke.com/blog/a-guide-to-customizing-your-tmux-conf/) 

The appearance and behaviour of tmux may be modified by changing the value of various options.  There are three types of option: 

* server options,  
* session options  
* and window options.

tmate show-options \-s

## \[JOB\] Change binding and config for the current session or window

[https://devel.tech/tips/n/tMuXm4vP/reloading-config-from-inside-tmux/](https://devel.tech/tips/n/tMuXm4vP/reloading-config-from-inside-tmux/)

tmux set-option  
tmux set-window-option

## \[JOB\] increase scrollback buffer size in tmux

Open tmux configuration file with the following command:

vim \~/.tmux.conf  
In the configuration file add the following line:

set \-g **history-limit** 5000  
Log out and log in again, start a new tmux windows and your limit is 5000 now.

## Tmux iterm2 integration

[https://www.iterm2.com/documentation-tmux-integration.html](https://www.iterm2.com/documentation-tmux-integration.html)

\-C Start in control mode (see the CONTROL MODE section).

\-CC Given twice disables echo.

## Tmate

ref: [https://linuxhandbook.com/tmate/](https://linuxhandbook.com/tmate/)  
**WHY?** Teamviewer, Guacamole, and TigerVNC are good when you need to share your screen to your co-workers or friends. These programs will share your entire screen to others. But, if you want to share only the Terminal, you can just use Tmate. It is actually a fork of Tmux.

**HOW?** Tmate will establish a secure connection over SSH to tmate.io website and generate a random URL for each session. You can share the URL with someone you trust and they can use the Terminal as the way they use their own Terminal as long as the connection is active.

Ref [https://www.ostechnix.com/tmate-share-terminal-instantly-anyone-anywhere/](https://www.ostechnix.com/tmate-share-terminal-instantly-anyone-anywhere/)

**tmate** \# will open a tmux terminal  
**tmate show-messages** \# run from the tmate terminal will show the connection string

`Tue Jan 22 18:25:42 2019 [tmate] Connecting to ssh.tmate.io...`  
`Tue Jan 22 18:25:44 2019 [tmate] Note: clear your terminal before sharing readonly access`  
`Tue Jan 22 18:25:44 2019 [tmate] web session read only: https://tmate.io/t/ro-Hqo1o8tCUIl5KpljcToORDDMG`  
`Tue Jan 22 18:25:44 2019 [tmate] ssh session read only: ssh ro-Hqo1o8tCUIl5KpljcToORDDMG@ln2.tmate.io`  
`Tue Jan 22 18:25:44 2019 [tmate] web session: https://tmate.io/t/YGd2veOMwB6p3x7gCBaQ9t5mB`  
`Tue Jan 22 18:25:44 2019 [tmate] ssh session: ssh YGd2veOMwB6p3x7gCBaQ9t5mB@ln2.tmate.io`

Share the SSH session ID with your trusted teammates and they can access your terminal using this command in their own terminal.

ssh \<SSH\_Session\_ID\>  
For example, in my case, it would be:

ssh YKiCguXm84rZmTiv9PZlExUX1@sg2.tmate.io

