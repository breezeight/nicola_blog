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
