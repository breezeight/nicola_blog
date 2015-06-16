---
layout: post
title: "Middleman"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["html", "css"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# Intro

https://middlemanapp.com/
https://github.com/emberjs/website/blob/master/Rakefile
http://directory.middlemanapp.com/#/templates/all
https://github.com/emberjs/website

Enable blogging:
gem "middleman-blog"
Tutorial: http://willschenk.com/building-sites-with-middleman/#building-a-blog

Enable i18n and multiple languages:
https://middlemanapp.com/advanced/localization/
http://blog.berylliumwork.com/2013/07/use-middleman-to-write.html

bundle exec middleman
bundle exec middleman deploy
bundle exec middleman console

Enable bootstrap and deploy:
http://willschenk.com/building-sites-with-middleman/

# Why Static?

https://www.discovermeteor.com/blog/three-middleman-hacks-were-using-on-this-site/

Easy to host, but you can still save data in yml files.

Use case:

* promo code with middleman: https://www.discovermeteor.com/blog/three-middleman-hacks-were-using-on-this-site/

# Best practices

* blog.default_extension = ".markdown.erb"   to use haml block into the markdown engine
* put  `activate :directory_indexes` after all `activate blog`, it doen't work otherwise https://coderwall.com/p/qgnwzw/directory-indexes-with-middleman-blog
* Use `![Amazing picture](<%= current_page.url %>some-image.png)` in markdown, see the warning [here](https://middlemanapp.com/advanced/pretty_urls/)
* You are using `directory_indexes` you could easly add each post images into `<blog_dir>/<post_dir>/image.png`


# Debug

To debug a page compilation you can use `pry-byebug`. For example this is a markdown.erb blog entry:

~~~
![The Purchase Funnel](<%= current_page.url
binding.pry
%> purchase_funnel.jpg)
~~~

# Use LESS with custom bootstrap theme

**WARNING** : don't use full path `@import "source/stylesheets/custom.less";` but  `@import "custom.less";` otherwise the wather don't work (is it a bug?).

REF: https://middlemanapp.com/advanced/asset_pipeline/

SEE this README: https://github.com/middleman/middleman-sprockets

If you want to use middleman-sprockets with bower, you need to import assets first. The path is relative to your bower-directory.

sprockets.import_asset <path>
Given vendor/assets/components as bower-directory and jquery as component-name, you would import the jquery production version with:

sprockets.append_path 'vendor/assets/components'
sprockets.import_asset 'jquery/dist/jquery'


You should EDIT source/stylesheets/all.css and import all the less file you need:

~~~
/*
*= require _site
*/

ADD  source/stylesheets/_site.less
@import "bootstrap/less/bootstrap.less";
@import "bootstrap-theme-pitchtarget/less/pitchtarget-theme.less";
@import "bootstrap-theme-pitchtarget/less/pitchtarget-variables.less";
@import "bootstrap-theme-pitchtarget/less/pitchtarget-bootstrap.less";
~~~

You should EDIT Gemfile:

~~~
+#Less
+gem "sprockets-less"
+gem "less"
+gem 'therubyracer' # this is needed because the less compiler uses V8 engine included by this gem

check that you include bower_components path in config.rb, so you can use the @import directive with paths relative to the sprocket PATH :


+ # Add bower's directory to sprockets asset path
after_configuration do
  sprockets.append_path File.join root.to_s, "bower_components"
end
~~~

JS: TODO `source/javascripts/all.js`

~~~
//= require_tree .
//= require "jquery/dist/jquery"
//= require "bootstrap/dist/js/bootstrap"
~~~

FONTS:

~~~
after_configuration do
  ....
  sprockets.append_path File.join root.to_s, "bower_components/bootstrap/fonts"
  sprockets.import_asset "glyphicons-halflings-regular.eot"
  sprockets.import_asset "glyphicons-halflings-regular.svg"
  sprockets.import_asset "glyphicons-halflings-regular.ttf"
  sprockets.import_asset "glyphicons-halflings-regular.woff"
  sprockets.import_asset "glyphicons-halflings-regular.woff2" 
  ....
end
~~~


I don't understand how middleman choose the fonts directory so I hacked a little the bootstrap font config (See Kenwood landing): `@icon-font-path: "../../../fonts/bootstrap/fonts/";`

# Multi-language

https://middlemanapp.com/advanced/localization/

Middleman support translation using dictionary files ( locales dir ). Each template in "source/localizable" can use the i18n helper and produce one output version for each language
Middleman can localize entire templates if you them in "source/localizable".  Following this pattern: index.en.html.erb and index.es.html.erb. When the site is built, you'll get:
build/en/index.html is English
build/es/index.html is Spanish


activate :i18n, :mount_at_root => :en

Locale aware blog:
https://github.com/middleman/middleman-guides/blob/master/source/basics/blogging.html.markdown#locale-specific-articles-and-localization

# Header and footer

https://middlemanapp.com/basics/partials/
Partial files are prefixed with an underscore

# Sitemap

https://middlemanapp.com/advanced/sitemap/

# Calendar

[Doc]("https://middlemanapp.com/basics/blogging/#sts=Calendar Pages")


# Pretty URLs (Directory Indexes)

* [Doc](https://middlemanapp.com/advanced/pretty_urls/)

**Warning** : put  `activate :directory_indexes` after all `activate blog`, it doen't work otherwise https://coderwall.com/p/qgnwzw/directory-indexes-with-middleman-blog


It makes `about-us.html.erb` accessible both at: `http://example.com/about-us.html` and `http://example.com/about-us`.

**Warning about assets path**

# Redirect support

https://github.com/middleman/middleman/commit/d86dffa7c64e64eff77eb24b9b34ad22960d7d8c


redirect "2014/10/09/pitchtarget-wins-openaxel-madrid.html", :to => "blog/2014/10/09/pitchtarget-wins-openaxel-madrid.html"
redirect "2014/09/11/measuring-success.html", :to => 
redirect "2014/09/04/its-all-about-funnels.html", :to => 
redirect "2014/08/28/bid-high-spend-less.html", :to => 
redirect "2014/08/21/pitchtarget-is-all-new.html", :to => 


# Blog

https://github.com/middleman/middleman-guides/blob/master/source/basics/blogging.html.markdown

Locale aware blog:
https://github.com/middleman/middleman-guides/blob/master/source/basics/blogging.html.markdown#locale-specific-articles-and-localization
you can use helpers like t() inside them

multiple blogs:
https://github.com/middleman/middleman-guides/blob/master/source/basics/blogging.html.markdown#multiple-blogs-in-a-single-site
The blog "name" is also the name of the source directory that contains articles:

~~~
activate :blog do |blog|
  # The blog helper use the name: blog('news')
  blog.name = "news"
end
~~~

will read its articles from `source/news`

To create articles in the news blog:

~~~
middleman article --blog news "Prova Articolo" 
~~~

Listing all articles:

~~~
%ul#articles
  - blog("news").articles.each do |article|
    %li= article.title
~~~

## Crete a new article

* `middleman article TITLE`
* `middleman article -b BLOG TITLE`

If you are using `directory_indexes` you could easly add each post images into `<blog_dir>/<post_dir>/image.png`

Options:

* -d, [--date=DATE]  # The date to create the post with (defaults to now)
* -l, [--lang=LANG]  # The language to create the post with (defaults to I18n.default_locale if avaliable)
* -b, [--blog=BLOG]  # The name of the blog to create the post inside (for multi-blog apps, defaults to the only blog in single-blog apps)

## Mix HAML and Markdown

Haml support filters:
http://haml.info/docs/yardoc/file.REFERENCE.html#markdown-filter

## Create Blog Post summary

The blogging extension looks for the string `READMORE` in your article body and shows only the content before this text on the homepage.

And use the `summary` method.

## Multiblog pagination example

In Middleman, blog pagination uses dynamic pages, which are exactly like typical server side dynamic pages might be, except the result is evaluated ahead of time and saved as static HTML.

https://github.com/middleman/middleman-blog/tree/master/fixtures/paginate-multiblog-app

blog index: https://github.com/middleman/middleman-blog/blob/master/fixtures/paginate-multiblog-app/source/blog1/index.html.erb

A template will be split into pages if it has:

~~~

---
pageable: true
blog: name_of_the_blog
---

~~~


NOTE: the `blog` key in the header will set the default for multiple pager, for example `paginate()`. This is much more DRY than pass the param to each method call 


Here’s the code for the blog index page, in HAML. To find the URL to previous and subsequent pages we follow the chain of prev_page and next_page until we get to the one we want. This allows this pagination code to be reused for paginating tags (as opposed to if we had used a hardcoded URL pattern for the numbers page links.)

(NOTE: the code below uses bootstrap 2)

~~~

---
pageable: true
per_page: 10
layout: blog
---

%h1.header
  Blog
  %hr
- page_articles.each do |current_article|
  .post
    .row
      .span4
        %a{:href => current_article.url}
          %h3= current_article.title
        %p= current_article.summary
        .post_info
          .date
            = current_article.date.strftime('%b %d, %Y')
    %a.btn{:href => current_article.url} Read

.pagination
  %ul
    %li{:class => prev_page ? "" : "disabled"}
      - if prev_page
        =link_to "Prev", prev_page.url
      - else
        %span Prev
    - (page_number - 2 .. page_number + 2).select{|i| i > 0 && i <= num_pages}.each do |i|
      - if i == page_number
        %li.active
          %span= i
      - else
        %li
          - p = nil
          - (i ... page_number).each do p = p ? p.metadata[:locals]['prev_page'] : prev_page; end
          - (page_number ... i).each do p = p ? p.metadata[:locals]['next_page'] : next_page; end
          =link_to "#{i}", p && p.url
    %li{:class => next_page ? "" : "disabled"}
      - if next_page
        =link_to "Next", next_page.url
      - else
        %span Next

~~~


## Multiblog

Each blog must:

* you must create a dir `source/name_of_the_blog`
* you must create an index for your blog; `source/name_of_the_blog/index.html`


Blog index for a multiproduct example:

 * https://github.com/middleman/middleman-blog/blob/master/fixtures/paginate-multiblog-app/source/blog1/index.html.erb
 * https://github.com/middleman/middleman-blog/blob/master/fixtures/paginate-multiblog-app/source/blog2/index.html.erb
 
 
## Haml Templates

http://haml.info/
http://tutorials.jumpstartlab.com/topics/better_views/erb_and_haml.html

The HAML engine assumes that if the content starts with an =, that the entire rest of the line is Ruby

~~~
%ul#articles
  - blog("news").articles.each do |article|
    %li= article.title
~~~

NOTE: non printing lines must start with "-"



# Deploy 

## on GH-Pages

On github you can host the 

https://help.github.com/articles/creating-project-pages-manually/
https://help.github.com/articles/setting-up-a-custom-domain-with-github-pages/

~~~
activate :deploy do |deploy|
  deploy.method = :git
  # Optional Settings
  deploy.remote   = 'git@github.com:breezeight/test_middleman_deploy.git' # remote name or git url, default: origin
  # deploy.branch   = 'custom-branch' # default: gh-pages
  # deploy.strategy = :submodule      # commit strategy: can be :force_push or :submodule, default: :force_push
  # deploy.commit_message = 'custom-message'      # commit message (can be empty), default: Automated commit at `timestamp` by middleman-deploy `version`
  deploy.build_before = true # default: false
end
~~~

## on S3 (with cloudfront)


* This gem for s3 only: https://github.com/fredjean/middleman-s3_sync
* This gem for cloudfront:  https://github.com/alienfast/middleman-aws 


# Bower: install bootstrap

https://github.com/headcanon/middleman-bower-template

Add an empty bower.json:
{
  "name": "middleman",
  "version": "0.0.0",
  "dependencies": {
  }
}

bower install --save-dev bootstrap

add " bower_components" to .gitignore

add to config.rb
#Add bower's directory to sprockets asset path
after_configuration do
  sprockets.append_path File.join root.to_s, "bower_components"
end








