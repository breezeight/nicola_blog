---
layout: post
title: "Ruby: Crawler"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["ruby"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# References

* XPath syntax: http://www.w3schools.com/xpath/xpath_syntax.asp

#

Compare:

support JS:

* wombat: no
*


# Mechanize

~~~
agent = Mechanize.new { |agent| agent.user_agent_alias = 'Mac Safari' }
page = agent.get('http://www.kelkoo.it/mp-12469913-amazon-electronics')
page.search('//p[@class="store-name"]/a/@href')
~~~


# Wombat

Is a DSL based on Mechanize.

You need to know the XPath syntax to take full advantage of wombat.

TIP: To test XPath use the Mechanize example below
