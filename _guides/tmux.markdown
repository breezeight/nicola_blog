---
layout: post
title: "Vim"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["tmux"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# References

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
