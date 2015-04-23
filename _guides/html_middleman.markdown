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



# Use LESS with custom botstrap theme

**WARNING** : don't use full path `@import "source/stylesheets/custom.less";` but  `@import "custom.less";` otherwise the wather don't work (is it a bug?).

You should EDIT source/stylesheets/all.css:

~~~
/*
*= require site
*/
ADD  source/stylesheets/site.less
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
+gem 'therubyracer'

NOTE: the @import directive uses the sprocket PATH
check that you include bower_components path in config.rb:
# Add bower's directory to sprockets asset path
after_configuration do
  sprockets.append_path File.join root.to_s, "bower_components"
end
~~~


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

## Create Blog Post summary

The blogging extension looks for the string `READMORE` in your article body and shows only the content before this text on the homepage.

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



# Deploy with GH-Pages

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








