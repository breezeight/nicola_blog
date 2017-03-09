---
layout: post
title: "Ruby"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["embedded"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# References

Compare Yocto and BuildRoot: https://lwn.net/Articles/682540/

* Buildroot puts all configuration information in one file, which can be edited using any of the interfaces from the kernel's kconfig tool (e.g., xconfig or menuconfig)

# Intro

Intro: 
http://www.jann.cc/2013/08/31/porting_linux_to_a_new_board.html

https://buildroot.org/downloads/manual/manual.html#_buildroot_quick_start


# Docker BuildRoot

https://github.com/Docker-nano/Buildroot  -> carino ma non ha funzionato...
 
https://github.com/AdvancedClimateSystems/docker-buildroot


## BUILDROOT IN A DOCKER IMAGE


* http://github.com/AdvancedClimateSystems/docker-buildroot

clone https://github.com/AdvancedClimateSystems/docker-buildroot


Script: http://slides.com/aukewillem/minimal-docker#/17


Step 1: Config Buildroot http://slides.com/aukewillem/minimal-docker#/18
Step 2: DEFCONFIG http://slides.com/aukewillem/minimal-docker#/19
Step 3: build rootfs

