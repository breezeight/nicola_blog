---
layout: post
title: "Ruby: Ruby On Rails"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["ruby"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# ActiveRecord


Conventions:

* has_any: use plural form of the model, example for model Post: `posts` 
* belongs_to: use the singlular form of the model, example for model Post: `post`

## HasMany woth a Legacy Database

Example: A legacy db that don't respect conventions

We need to:

* force the foreing_key of belongs_to and has_many
* we don't need to force the foreing_key of the "has_many through" because it uses the other relationship that already force the foreing_key

~~~

class PostPost < ActiveRecord::Base
  establish_connection(OLD_DB_CONFIG[:db])  
  
  belongs_to :user_user, foreign_key: :user_id
  
  has_many :kclub_accessories_posts, foreign_key: :post_id 
  has_many :kclub_accessories, through: :kclub_accessories_posts 
end

class KclubAccessory < ActiveRecord::Base
  establish_connection(OLD_DB_CONFIG[:db])
  
  self.inheritance_column = :ruby_type
  
end

class KclubAccessoriesPost < ActiveRecord::Base
  establish_connection(OLD_DB_CONFIG[:db])  
  
  belongs_to :post_post, foreign_key: :post_id
  belongs_to :kclub_accessory, foreign_key: :accessory_id
end

~~~


# Rails Admin

* Q: Labels: sulla tab ordinamento come faccio a cambiare la label ?
* A: definisci un metodo admin_label

~~~
  # Label methods for model instances:
  # config.label_methods << :description # Default is [:name, :title]
  config.label_methods = [:admin_label, :name, :title]
~~~

## Sortable Elements

TIP: use a float


Example:

* ~/SRC/KENWOOD/kenwoodclub/db/migrate/20150728163038_create_home_slides.rb
* ~/SRC/KENWOOD/kenwoodclub/app/model/home_slide.rb


# Link about Rails and ruby Collection

## Performances

* [rack-mini-profiler: The Secret Weapon of Ruby and Rails Speed](http://www.nateberkopec.com/2015/08/05/rack-mini-profiler-the-secret-weapon.html?utm_source=rubyweekly&utm_medium=email)
rack-mini-profiler provides an suite of tools for measuring the performance of Rack-enabled apps, including drill downs on SQL queries, server response times, execution times with flamegraphs, and memory leaks.

* Scaling: protection against slow client and slow response on HEROKU
  * http://www.nateberkopec.com/2015/07/29/scaling-ruby-apps-to-1000-rpm.html?utm_source=rubyweekly&utm_medium=email
  * Very nice


## RSpec

* [RubySpec Reborn](http://eregon.github.io/rubyspec/2015/07/29/rubyspec-is-reborn.html?utm_source=rubyweekly&utm_medium=email)
