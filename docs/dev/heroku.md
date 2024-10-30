---
layout: post
title: "Heroku"
date: 2014-03-16 20:48:22 +0100
comments: true
categories: 
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

This is a short internal guide to the AWS service we use most.

# Bower rails

# Setup for deploy to an existing app


* Ref: https://devcenter.heroku.com/articles/git#creating-a-heroku-remote
* `heroku login`
* heroku git:remote -a kenwood-staging -r kenwood-staging
* `git push kenwood-staging  develop:master`



# Passenger

NOTE: passenger5 on Heroku is much less memory hungry than Puma, less perfomance but much more stable.

* Passenger status on Heroku: https://blog.phusion.nl/2015/05/26/introducing-the-passenger-status-service-for-heroku/
* passenger demo app on Heroku: https://github.com/phusion/passenger-ruby-heroku-demo
* Optimize: https://www.phusionpassenger.com/library/config/standalone/optimization/#minimizing-process-spawning


