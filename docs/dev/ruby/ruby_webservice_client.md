---
layout: post
title: "Ruby: Http Clients and ORM"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["ruby"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# References


# HTTP clients

## Faraday

How to add a param to every request:

~~~
connection = Faraday.new(url: 'https://graph.facebook.com/v2.3') do |c| ... end
connection.params={access_token: "MYTOKEN"}
~~~

# ORM Client Examples

## Rest Client

* [HomePage](https://github.com/rest-client/rest-client)

## Active Resource

## Her

## Spyke

Home: https://github.com/balvig/spyke

Uses:

* ActiveModel
* Concerns

* To add the access_token query param to every request see the [faraday gem guide](#faraday)

~~~
Spyke::Base.connection.params={access_token: "My Token"}

campaign = AdCampaign.where(fields: "name").find(6025708368616)
campaign.ad_sets.where(fields: "name,buying_type").first
~~~



## Digital Ocean Client: Droplet Kit

* https://github.com/digitalocean/droplet_kit


## Github client by peter-murach

* https://github.com/peter-murach/github

Collections are returned as `Hashie::Mash` 

## Twitter client

* https://github.com/sferik/twitter
* git@github.com:sferik/twitter.git
* [DOC](http://www.rubydoc.info/gems/twitter)
* [Examples](https://github.com/sferik/twitter/tree/master/examples)

it parses response into classes 

# Test

See [my guide](ruby_testing_webservices.md)

