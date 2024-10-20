---
layout: post
title: "Alpine"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["linux"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

![alt text](images/docs/alpine/manifestoevento.jpg)


Alpine instructions are for creating a new repository for custom packages:
https://www.linkedin.com/pulse/creating-alpine-linux-package-repository-afam-agbodike


http://wiki.alpinelinux.org/wiki/Apkindex_format

# Release Cycle

# Package management

This [Guide](https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management) contains:

* Search for Packages 
* Info on Packages (size, depends, required by, contains, ...)
* Listing installed packages:
  * apk -vv info|sort
  * apk -v info|sort

`Software packages for Alpine Linux` are digitally signed tar.gz archives containing programs, configuration files, and dependency metadata.

They have the extension `.apk`, and are often called "a-packs".

The packages are stored in one or more `repositories`. A repository is

* a directory with a collection of *.apk files.
* The directory must include a special index file, named `APKINDEX.tar.gz`.




# Jobs

## Keep a specific package version

to hold the asterisk package to the 1.6.2 level or lower:

```
apk add asterisk=1.6.0.21-r0
```

or

```
apk add asterisk<1.6.1
```


after which a `apk upgrade` will upgrade the entire system, keeping the asterisk package at the 1.6.0 or lower level

To later upgrade to the current version `apk add 'asterisk>1.6.1'`



## Audit Versions and Packages

/etc/os-release:

```
NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.5.2
PRETTY_NAME="Alpine Linux v3.5"
HOME_URL="http://alpinelinux.org"
BUG_REPORT_URL="http://bugs.alpinelinux.org"
```

/etc/alpine-release:  3.5.2


/etc/apk/repositories

http://dl-cdn.alpinelinux.org/alpine/v3.5/main
http://dl-cdn.alpinelinux.org/alpine/v3.5/community
