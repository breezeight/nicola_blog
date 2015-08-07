---
layout: post
title: "Ruby: Bundler"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["ruby"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# References

* [Matz: Gem Versioning and Bundler: Doing it Right](http://yehudakatz.com/2011/05/30/gem-versioning-and-bundler-doing-it-right/)
* 


# Intro

Essentially Bundler is a smart way to puts all the gems need by your project "on the load path".
It also provide a quick way to require all gems in your Gemfile.
Bundle uses a Gemfile to list all the project dependencies.


http://bundler.io/rationale.html :

* `require 'bundler/setup'`
* `Bundler.require(:default)`

# Basic Versioning Rules for Apps

* After bundling, always check your `Gemfile.lock` into version control. If you do this, you do not need to specify exact versions of gems in your Gemfile. Bundler will take care of ensuring that all systems use the same versions.

* After updating your Gemfile, always run bundle install first. This will conservatively update your Gemfile.lock. This means that except for the gem that you changed in your Gemfile, no other gem will change.

* If a conservative update is impossible, bundler will prompt you to run bundle update [somegem]. This will update the gem and any necessary dependencies. It will not update unrelated gems.

* If you want to fully re-resolve all of your dependencies, run bundle update. This will re-resolve all dependencies from scratch.

* When running an executable, ALWAYS use bundle exec [command]. Quoting from the bundler documentation: In some cases, running executables without bundle exec may work, if the executable happens to be installed in your system and does not pull in any gems that conflict with your bundle. However, this is unreliable and is the source of considerable pain. Even if it looks like it works, it may not work in the future or on another machine. See below, "Executables" for more information and advanced usage.

* Remember that you can always go back to your old Gemfile.lock by using git checkout Gemfile.lock or the equivalent command in your version control.

# How does Bundler change the ruby LOAD PATH

`bundler/setup` does a few things:

* It removes all paths to gems from the `$LOAD_PATH` (which reverses any load path work that RubyGems did).
* Then, it adds the load paths of just the gems in your `Gemfile.lock` back to the `$LOAD_PATH`.

## Example: What’s the Difference Between `irb`, `bundle exec irb`, `bundle console`, and `rails console`?

http://www.justinweiss.com/blog/2014/11/17/what-are-the-differences-between-irb/

# Executables

When you install a gem to the system, Rubygems creates wrappers for every executable that the gem makes available.

When you run an executable from the command line without bundle exec, this wrapper invokes Rubygems, which then uses the normal Rubygems activation mechanism to invoke the gem's executable.



# How does Rails use Bundler?

tl;dr : In `config/application.rb` Rails does `Bundler.require(*Rails.groups)`, where by default Rails.groups is:

* `[:default, :development, :assets]` for Rails.env == "development"
* `[:default, :production]`           for Rails.env == "production"

Long explanation, ref http://www.justinweiss.com/blog/2014/10/13/how-does-rails-handle-gems/

## The Rails commnand

REF: http://yehudakatz.com/2011/05/30/gem-versioning-and-bundler-doing-it-right/

As of Rails 3.0, the executable simply looks for a `script/rails` file, and execs that file. The generated script/rails loads the local boot environment, which invokes bundler immediately

NOTE: not sure for rails 4 

# Gemfile and Gemfile.lock documentation

TODO

## The `require` option

Example: `gem 'rack-cache', require: 'rack/cache'`. 

By default `Bundler.require(:default)` will require the exact name of the gem, but some gem doesn't follow this convetion.

In this example, without the option it would require `rack-cache`, which is not right, we must override this behaviour.

## Gemfile groups and Gemfile.lock

* Is the Gemfile.lock affected by `--with` and `--without` bundle install options? NO:
  * All gems of every group will be added to the Gemfile.lock, regardless the option you specify
  * instead  `--with` and `--without` will affect your local config `.bundle/config` ---->>>> TODO: how does this affect the load path on `budle.setup` ??



# Bundle configuration

Bundle configuration variable are set on different places:

* env
* local: a `.bundle/config` file in the Gemfile directory
* global: a `~/.bundle/config` in the home of the directory


`bundle config` with no parameters will print a list of all bundler configuration for the current bundle, and where that configuration was set.





* BUNDLE_PATH and `--path` 
* http://bundler.io/v1.10/deploying.html
* You can run `bundle check` before deploying your application to make sure that your Gemfile.lock is up-to-date.


Ref: http://bundler.io/v1.2/bundle_config.html

* `BUNDLE_GEMFILE`: The name of the file that bundler should use as the Gemfile. 
* `BUNDLE_JOBS`:
* `BUNDLE_PATH`: The location on disk to install gems. Defaults to $GEM_HOME in development and vendor/bundle when --deployment is used.


# Bundle Install and Package

Ref:

* http://bundler.io/bundle_package.html
* http://bundler.io/v1.10/bundle_install.html

The package command will copy the .gem files for your gems in the bundle into ./vendor/cache. Afterward, when you run bundle install, Bundler will use the gems in the cache in preference to the ones on rubygems.org.


* `bundle pack` don't have the option to exclude groups of gems, it always cache and/or install all gems listed in the Gemfile

* `--with` and `--without` will affect your local config `.bundle/config` ---->>>> TODO: how does this affect the load path on `budle.setup` ??



The `--deployment` flag activates a number of deployment- and CI-friendly conventions:

* Isolate all gems into vendor/bundle (equivalent to --path vendor/bundle)
* Require an up-to-date Gemfile.lock (equivalent to --frozen)
* Disable ANSI color output
* If bundle package was run, do not fetch gems from rubygems.org. Instead, only use gems in the checked in `vendor/cache`

## Examples

This is a basic rails 4 Gemfile generated with `rails new my_app` 

~~~
source 'https://rubygems.org'

gem 'rails', '4.2.3'
gem 'sqlite3'
gem 'sass-rails', '~> 5.0'
gem 'uglifier', '>= 1.3.0'
gem 'coffee-rails', '~> 4.1.0'
gem 'jquery-rails'
gem 'turbolinks'
gem 'jbuilder', '~> 2.0'
gem 'sdoc', '~> 0.4.0', group: :doc

group :bla do
  gem 'unicorn'
end

group :development, :test do
  gem 'byebug'
  gem 'web-console', '~> 2.0'
  gem 'spring'
end
~~~

### bundle install --path=/tmp/install_dir --deployment


### install --path=/tmp/install_dir --without bla --deployment

In this case gems from the `bla` group will be excluded both from the cache and the install dir:

* `ls vendor/bundle/ruby/2.2.0/cache/` : 54 gem
* vendor/bundle/ruby/2.2.0/gems


### bundle pack --path

if you run `bundle pack --path /tmp/pack_dir`, The config is saved into `.bundle/config` :

~~~
BUNDLE_PATH: "/tmp/pack_dir"
BUNDLE_DISABLE_SHARED_GEMS: '1'
~~~

all subsequent commands without a `--path` option will reuse the value used by this command invokation because its stored in the local config.




### bundle pack --no-install --path 

When you use the `--no-install` option, only the `.gem` file will be added to the cache directory, no extension is built, and gems are not unpacked:

`.bundle/config`:

~~~
BUNDLE_PATH: "/tmp/pack_dir3"
BUNDLE_DISABLE_SHARED_GEMS: '1'
BUNDLE_NO_INSTALL: true
~~~

The resulting path directory is:

~~~
.
├── ruby
│   └── 2.2.0
│       └── cache
│           ├── actionmailer-4.2.3.gem
|           ......
│           ├── unicorn-4.9.0.gem
│           └── web-console-2.2.1.gem
└── vendor
    └── cache
        ├── actionmailer-4.2.3.gem
        ......
        ├── unicorn-4.9.0.gem
        └── web-console-2.2.1.gem


~~~


# FAQ

* What bundle commands change the local config? 
  * pack
  * install --deployment

* Bundler: two caches in the vendor folder, why run bundle package then?
http://stackoverflow.com/questions/8929775/bundler-two-caches-in-the-vendor-folder-why-run-bundle-package-then      

