---
layout: post
title: "heroku-buildpack"
date: 2014-03-27 16:10:52 +0100
comments: true
categories: 
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# Intro

When you git push heroku, Heroku’s slug compiler prepares your code for execution by the Heroku dyno manager. At the heart of the slug compiler is a collection of scripts called a buildpack. Heroku’s Cedar stack has no native language or framework support; Ruby, Python, Java, Clojure, Node.js and Scala are all implemented as buildpacks.

The buildpack API is formed by three basic pieces:

* bin/detect
* `bin/compile BUILD_DIR CACHE_DIR ENV_DIR`
* bin/release

They're all bash scripts!. That means that can be written in any scripting language present on the system - Ruby, Perl, Bash, whatever



* Heroku doc about [using custom build pack](https://devcenter.heroku.com/articles/buildpacks)
* Heroku doc about [creating a custom build pack](https://devcenter.heroku.com/articles/buildpack-api)
* http://talks.codegram.com/heroku-buildpacks
http://www.petekeen.net/deploying-a-12-factor-app-with-capistrano


http://lee.hambley.name/2013/06/11/using-capistrano-v3-with-chef.html
http://www.petekeen.net/deploying-a-12-factor-app-with-capistrano
https://discussion.heroku.com/t/early-access-new-ruby-buildpack-with-faster-bundler/131
http://artsy.github.io/blog/2013/01/15/debugging-bundler-issues-with-heroku/



# Ruby Build Pack
The [source code](https://github.com/heroku/heroku-buildpack-ruby) is
available on github. This document is based on tag v111.

[Hatchet](https://github.com/heroku/hatchet) is a an integration testing library for developing Heroku buildpacks.

## Compile

language_pack.rb defines `LanguagePack.detect` which test the BUILD_DIR
with the `use?` method

~~~ruby
pack = [ NoLockfile, Rails41, Rails4, Rails3, Rails2, Rack, Ruby ].detect do |klass|
  klass.use?
end
~~~

lib/language_pack/base.rb:17:  VENDOR_URL = "https://s3-external-1.amazonaws.com/heroku-buildpack-ruby"
lib/language_pack/base.rb:32:      @fetchers     = {:buildpack => LanguagePack::Fetcher.new(VENDOR_URL) }
lib/language_pack/ruby.rb:296:            @fetchers[:buildpack].fetch_untar("#{ruby_version.version}.tgz")

EX: https://s3-external-1.amazonaws.com/heroku-buildpack-ruby/ruby-2.0.0.tgz


  # runs bundler to install the dependencies
  def build_bundler


issue:
export PATH=vendor/bundle/bin:vendor/bundle/ruby/2.1.0/bin:vendor/ruby-2.1.1/bin:/home/vagrant/.rvm/gems/ruby-2.1.1/bin:/home/vagrant/.rvm/gems/ruby-2.1.1@global/bin:/home/vagrant/.rvm/rubies/ruby-2.1.1/bin:/usr/local/heroku/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/home/vagrant/.rvm/bin:bin:/usr/local/bin:/usr/bin:/bin

causes:
Could not load OpenSSL.
You must recompile Ruby with OpenSSL support or change the sources in your Gemfile from 'https' to 'http'. Instructions for compiling with OpenSSL using RVM are available at
rvm.io/packages/openssl.

I've solved adding this packages from the dokku platform buildstep
docker image: 
https://github.com/progrium/buildstep/blob/master/stack/packages.txt


https://index.docker.io/u/progrium/buildstep/
https://index.docker.io/u/progrium/buildstep/

# Add Binaries
Binaries
When building and packaging dependencies, make sure they are compatible with Heroku’s runtime environment. One way to do that is to build dependencies in Heroku dynos, for example by using heroku run.

