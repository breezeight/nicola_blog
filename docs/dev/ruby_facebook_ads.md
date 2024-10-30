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

# Ideas

Facebook SDK AdAccount.php

~~~
  public function getAdCampaigns(
    array $fields = array(), array $params = array()) {
    return $this->getManyByConnection(
      AdCampaign::className(), $fields, $params);
  }
~~~



# Facebook PHP SDK

* ~/SRC/ADDICTIVE/test_php-sdk


composer.json 

~~~
{
    "name" : "pippo",
    "autoload" : {
      "psr-0": { "" : "src/" }
    },
    "require": {
        "facebook/php-ads-sdk": "2.2.*"
    }
}

~~~


cat src/pippo.php 

~~~
<?php

$loader = require_once __DIR__.'/../vendor/autoload.php';

use FacebookAds\Api;
use FacebookAds\Object\AdAccount;
use FacebookAds\Object\Fields\AdAccountFields;

$app_id = "";
$app_secret = "";
$access_token = "";
$account_id = "293595400818280";

// Initialize a new Session and instanciate an Api object
Api::init($app_id, $app_secret, $access_token);

// The Api object is now available trough singleton
$api = Api::instance();

$account = new AdAccount($account_id);

var_dump($account);
~~~

php src/pippo.php

