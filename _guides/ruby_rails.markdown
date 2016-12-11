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

# Rails Command line

REF: 
* INTRO http://guides.rubyonrails.org/command_line.html#rails-generate
* MODELs
  * http://edgeguides.rubyonrails.org/active_record_migrations.html#model-generators 
  * http://railsguides.net/advanced-rails-model-generators/

* destroy example:
  * bin/rails generate model Oops
  * bin/rails destroy model Oops

# Getting started and basic development tools

https://gorails.com/setup/osx/10.10-yosemite

OSX + Postgres:

## railroady

Ruby on Rails 3/4/5 model and controller UML class diagram generator.

https://rubygems.org/gems/railroady


# RSpec Rails

## Reset Test DB

```
bundle exec rake db:drop RAILS_ENV=test
bundle exec rake db:create RAILS_ENV=test
bundle exec rake db:schema:load RAILS_ENV=test
```


# Custom 404

https://mattbrictson.com/dynamic-rails-error-pages

# Controllers

## Rails Routing from the Outside In

http://guides.rubyonrails.org/routing.html

### Resource Routing

#### Resources

* `resources :photos`

```
# PhotosController:
# index  =>    GET /photos
# new    =>    GET /photos/new
# create =>   POST /photos/new
# show   =>    GET /photos/:id
# edit   =>    GET /photos/:id/edit
# update =>    PUT /photos/:id
# delete => DELETE /photos/:id
#
# Helpers:
# new_book_path
# book_path(id)
# edit_book_path(id)
```

#### Singular Resources

http://guides.rubyonrails.org/routing.html#singular-resources

* `get 'profile', to: 'users#show'` using the `controller#action` format
* `get 'profile', to: :show, controller: 'users'`
* `resource :geocoder`

#### Adding More Restful Actions

http://guides.rubyonrails.org/routing.html#adding-more-restful-actions :

* `member`
* `collection`
* `on`

A member route will require an ID, because it acts on a member. A collection route doesn't because it acts on a collection of objects.

On members:

```
resources :photos do
  member do
    get 'preview'
  end
end

# PhotosController#preview  =>    GET /photos/:id/preview
# create the preview_photo_url and preview_photo_path helpers

```

If you don't have multiple member routes, you can also pass `:on` to a route, eliminating the block:

```
resources :photos do
  get 'preview', on: :member
end
```

On collections:

```
resources :photos do
  collection do
    get 'search'
  end
end

# PhotosController#search => GET /photos/search
# create search_photos_url and search_photos_path route helpers.
```

#### Controller Namespaces and Routing

http://guides.rubyonrails.org/routing.html#controller-namespaces-and-routing


Scope gives you great control over each aspect, while namespace takes one argument for everything.



The `namespace` method is the simple case — it prefixes everything.

```
namespace :foo do
  resources :posts
end
```

produces:

```
$ rake routes
       Prefix Verb   URI Pattern                   Controller#Action
    foo_posts GET    /foo/posts(.:format)          foo/posts#index
              POST   /foo/posts(.:format)          foo/posts#create
 new_foo_post GET    /foo/posts/new(.:format)      foo/posts#new
edit_foo_post GET    /foo/posts/:id/edit(.:format) foo/posts#edit
     foo_post GET    /foo/posts/:id(.:format)      foo/posts#show
              PATCH  /foo/posts/:id(.:format)      foo/posts#update
              PUT    /foo/posts/:id(.:format)      foo/posts#update
              DELETE /foo/posts/:id(.:format)      foo/posts#destroy
```

The `scope` method gives you fine-grained control:

```
scope 'url_path_prefix', module: 'module_prefix', as: 'named_route_prefix' do
  resources :posts
end
For example:

scope 'foo', module: 'bar', as: 'baz' do
  resources :posts
end
```

produces these routes:

```
$ rake routes
       Prefix Verb   URI Pattern                   Controller#Action
    baz_posts GET    /foo/posts(.:format)          bar/posts#index
              POST   /foo/posts(.:format)          bar/posts#create
 new_baz_post GET    /foo/posts/new(.:format)      bar/posts#new
edit_baz_post GET    /foo/posts/:id/edit(.:format) bar/posts#edit
     baz_post GET    /foo/posts/:id(.:format)      bar/posts#show
              PATCH  /foo/posts/:id(.:format)      bar/posts#update
              PUT    /foo/posts/:id(.:format)      bar/posts#update
              DELETE /foo/posts/:id(.:format)      bar/posts#destroy
```


### Customizing Resourceful Routes

#### Restricting the Routes Created

http://guides.rubyonrails.org/routing.html#restricting-the-routes-created

`resources :photos, only: [:index, :show]`

### Non-Resourceful Routes

Support for routing arbitrary URLs to actions

#### Naming Routes

http://guides.rubyonrails.org/routing.html#naming-routes


# ActiveRecord

Conventions:

* has_any: use plural form of the model, example for model Post: `posts` 
* belongs_to: use the singlular form of the model, example for model Post: `post`

## Validations

http://edgeguides.rubyonrails.org/active_record_validations.html

## Queries

* NOT NULL: `User.where("address IS NOT NULL")`

## Migrations

REF: 

* http://guides.rubyonrails.org/active_record_migrations.html


* `db/migrate`
* File name: `YYYYMMDDHHMMSS_create_products.rb` : UTC timestamp _  name of the migration class (CamelCased version)
  * name of the migration class (CamelCased version) should match the latter part of the file name. For example 20080906120000_create_products.rb should define class CreateProducts and 20080906120001_add_details_to_products.rb should define AddDetailsToProducts. 

### Cheatsheet Migration and generator

* To generate an empty migration: `bin/rails generate migration AddPartNumberToProducts`

~~~
class AddPartNumberToProducts < ActiveRecord::Migration
  def change
  end
end
~~~

* To add/remove a column use this naming `AddXXXToYYY` or `RemoveXXXFromYYY` followed by a list of column names and types then a migration containing the appropriate add_column and remove_column statements:
  * `XXX` is the the name of the field  CammelCased
  * `YYY` is the name of the table

`bin/rails generate migration AddPartNumberToProducts part_number:string` :

~~~
class AddPartNumberToProducts < ActiveRecord::Migration
  def change
    add_column :products, :part_number, :string
  end
end
~~~

To create a new table `CreateXXX`, followed by a list of column names and types.

## Change data in migrations

http://railsguides.net/change-data-in-migrations-like-a-boss/

## HasMany with a Legacy Database

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

# Rails API

## Documenting your API

### Generate Documentation through Testing

https://blog.codeship.com/producing-documentation-for-your-rails-api/

It looks similar to the DSL provided by RSpec by default but introduces a few extra methods:

* header
* parameter
* explanation
* among others

# Link about Rails and ruby Collection

## Performances

* [rack-mini-profiler: The Secret Weapon of Ruby and Rails Speed](http://www.nateberkopec.com/2015/08/05/rack-mini-profiler-the-secret-weapon.html?utm_source=rubyweekly&utm_medium=email)
rack-mini-profiler provides an suite of tools for measuring the performance of Rack-enabled apps, including drill downs on SQL queries, server response times, execution times with flamegraphs, and memory leaks.

* Scaling: protection against slow client and slow response on HEROKU
  * http://www.nateberkopec.com/2015/07/29/scaling-ruby-apps-to-1000-rpm.html?utm_source=rubyweekly&utm_medium=email
  * Very nice


## RSpec

* [RubySpec Reborn](http://eregon.github.io/rubyspec/2015/07/29/rubyspec-is-reborn.html?utm_source=rubyweekly&utm_medium=email)



# SEO

## Fix Trailing slash issue

Use rack rewrite:
https://eric-schaefer.com/blog/2015/07/24/removing-trailing-slashes-rails-app-heroku/

