---
layout: post
title: "Ruby: Testing webservices"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["ruby", "testing"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# References


# VCR VS WebMock

http://robots.thoughtbot.com/how-to-stub-external-services-in-tests

http://www.slideshare.net/kjbuckley/testing-http-calls-with-webmock-and-vcr

VCR gem:

* https://github.com/vcr/vcr
* https://groups.google.com/forum/#!forum/vcr-maintainers
* https://www.relishapp.com/vcr/vcr/docs

VCR:

* record request and response for you
* has the support for Fakeweb and WebMock
* Uses ERB to dynamically populate dynamic and secure staff

http://launchware.com/articles/use-vcr-to-make-your-api-integration-tests-more-deterministic


# IDEAs

https://pragprog.com/magazines/2011-03/testing-for-web-services

un po' di filosofia:
http://stackoverflow.com/questions/8485213/mocking-an-expensive-resource-in-acceptance-tests-rspec-cucumber

http://marnen.github.io/webmock-presentation/webmock.html#(1)



# AWS SDK Example

This paragraph is based on:
* `git@github.com:aws/aws-sdk-core-ruby.git`
* tag: `v2.0.14`




Uses JSON-SCHEMA https://github.com/ruby-json-schema/json-schema/tree/master

This repo has strange structure, it contains 3 gems.

The AWS SDK for Ruby is unit tested using RSpec.

To run unit test:

~~~ruby
    bundle install
    bundle exec rake test
~~~

To run integration tests:

* create a `integration-test-config.json` file at the root of this repository.
* It should contain a `"region"` and credentials.
* Running rake test when this file is present will enable integration tests.

The main `Rakefile` will load Rakefile contained into the subdirs:

~~~ruby
$REPO_ROOT = File.dirname(__FILE__)

$VERSION = ENV['VERSION'] || File.read(File.join($REPO_ROOT, 'VERSION')).strip

$GEM_NAMES = [
  'aws-sdk-core',
  'aws-sdk-resources',
  'aws-sdk',
]

$GEM_NAMES.each do |gem_name|
  $LOAD_PATH.unshift(File.join($REPO_ROOT, gem_name, 'lib'))
end

require 'aws-sdk'              ### Why we need to require this ??

task 'test:coverage:clear' do
  sh("rm -rf #{File.join($REPO_ROOT, 'coverage')}")
end

desc 'Runs unit tests'
task 'test:unit' => 'test:coverage:clear'

desc 'Runs integration tests'
task 'test:integration' => 'test:coverage:clear'

desc 'Runs unit and integration tests'
task 'test' => ['test:unit', 'test:integration']

task :default => :test

Dir.glob('**/*.rake').each do |task_file|
  load task_file
end

begin
  require 'coveralls/rake/task'
  Coveralls::RakeTask.new
rescue LoadError
end
~~~



aws-sdk-core/tasks/test.rake :

~~~ruby
require 'rspec/core/rake_task'  ### This file contains the RSpec rake task class

desc "aws-sdk-core unit tests"
RSpec::Core::RakeTask.new('test:unit:aws-sdk-core') do |t|
  t.rspec_opts = "-I #{$REPO_ROOT}/aws-sdk-core/lib"     ### tell rspec to add this dirs to $LOAD_PATH
  t.rspec_opts << " -I #{$REPO_ROOT}/aws-sdk-core/spec"
  t.pattern = "#{$REPO_ROOT}/aws-sdk-core/spec"          ### Load file matching pattern for rspec tests (default: "spec/**/*_spec.rb").
end
task 'test:unit' => 'test:unit:aws-sdk-core'

begin
  require 'cucumber/rake/task'
  desc = 'aws-sdk-core integration tests'
  Cucumber::Rake::Task.new('test:integration:aws-sdk-core', desc) do |t|
    t.cucumber_opts = 'aws-sdk-core/features -t ~@veryslow'  ### tell to cucumber where to find the integration tests
  end
  task 'test:integration' => 'test:integration:aws-sdk-core'
rescue LoadError
  desc 'aws-sdk-core integration tests'
  task 'test:integration' do
    puts 'skipping aws-sdk-core integration tests, cucumber not loaded'
  end
end
~~~

aws-sdk-resources/tasks/test.rake :
task 'test:unit' => 'test:unit:aws-sdk-resources'


## Integration tests
The integration test are performed using cucumber. They will be runned
only if the `integration-test-config.json` file is available or an ENV
variable is set, see here:

* aws-sdk-core/features/env.rb:cfg = './integration-test-config.json'
* aws-sdk-resources/features/env.rb:cfg = './integration-test-config.json'

Does these test hit the real server ? Yed, that's why you need also to
setup a credential file.

What is tested? Not too much, basically only idempotent query like:

* list all resources
* get a non existing resource to trigger and manage errors
* .....


## How they use webmock

They don't use webmock for everything:

~~~
aws-sdk-core/spec/aws/credential_provider_chain_spec.rb:97:      stub_request(:get, "http://169.254.169.254#{path}").
aws-sdk-core/spec/aws/credential_provider_chain_spec.rb:99:      stub_request(:get, "http://169.254.169.254#{path}profile-name").
aws-sdk-core/spec/aws/instance_profile_credentials_spec.rb:17:          stub_request(:get, "http://169.254.169.254#{path}").to_raise(error_class)
aws-sdk-core/spec/aws/instance_profile_credentials_spec.rb:54:        stub_request(:get, "http://169.254.169.254#{path}").
aws-sdk-core/spec/aws/instance_profile_credentials_spec.rb:56:        stub_request(:get, "http://169.254.169.254#{path}profile-name").
aws-sdk-core/spec/aws/instance_profile_credentials_spec.rb:119:        expected_request = stub_request(:get, "http://169.254.169.254#{path}").
aws-sdk-core/spec/aws/s3/client/region_detection_spec.rb:24:          stub_request(:put, 'https://bucket.s3.amazonaws.com/key').
aws-sdk-core/spec/aws/s3/client/region_detection_spec.rb:27:          stub_request(:put, 'https://bucket.s3-external-1.amazonaws.com/key').
aws-sdk-core/spec/aws/s3/client/region_detection_spec.rb:32:          stub_request(:put, 'https://bucket.s3.eu-central-1.amazonaws.com/key').
aws-sdk-core/spec/aws/s3/client/region_detection_spec.rb:90:          stub_request(:put, 'https://bucket.s3-us-west-2.amazonaws.com/key').
aws-sdk-core/spec/aws/s3/client/region_detection_spec.rb:93:          stub_request(:put, 'https://bucket.s3-external-1.amazonaws.com/key').
aws-sdk-core/spec/aws/s3/client/region_detection_spec.rb:98:          stub_request(:put, 'https://bucket.s3.eu-central-1.amazonaws.com/key').
aws-sdk-core/spec/aws/s3/client/region_detection_spec.rb:109:          stub_request(:put, 'https://bucket.s3-us-west-2.amazonaws.com/key').
aws-sdk-core/spec/aws/s3/client/region_detection_spec.rb:112:          stub_request(:put, 'https://bucket.s3.eu-central-1.amazonaws.com/key').
aws-sdk-core/spec/seahorse/client/net_http/handler_spec.rb:117:            stub_request(:any, endpoint)
aws-sdk-core/spec/seahorse/client/net_http/handler_spec.rb:123:            stub_request(:any, endpoint)
aws-sdk-core/spec/seahorse/client/net_http/handler_spec.rb:132:              stub_request(:any, 'http://foo.bar.com')
aws-sdk-core/spec/seahorse/client/net_http/handler_spec.rb:138:              stub_request(:any, 'http://foo.bar.com:9876')
aws-sdk-core/spec/seahorse/client/net_http/handler_spec.rb:144:              stub_request(:any, 'https://foo.bar.com')
aws-sdk-core/spec/seahorse/client/net_http/handler_spec.rb:154:              stub_request(:post, endpoint)
aws-sdk-core/spec/seahorse/client/net_http/handler_spec.rb:171:              stub_request(:any, endpoint).with(:headers => { 'abc' => 'xyz' })
aws-sdk-core/spec/seahorse/client/net_http/handler_spec.rb:177:              stub_request(:any, endpoint).
aws-sdk-core/spec/seahorse/client/net_http/handler_spec.rb:184:              stub_request(:any, endpoint).
aws-sdk-core/spec/seahorse/client/net_http/handler_spec.rb:191:              stub_request(:any, endpoint).
aws-sdk-core/spec/seahorse/client/net_http/handler_spec.rb:198:              stub_request(:any, endpoint).
aws-sdk-core/spec/seahorse/client/net_http/handler_spec.rb:209:              stub_request(:any, http_request.endpoint.to_s)
aws-sdk-core/spec/seahorse/client/net_http/handler_spec.rb:216:              stub_request(:any, http_request.endpoint.to_s)
aws-sdk-core/spec/seahorse/client/net_http/handler_spec.rb:226:              stub_request(:any, endpoint).with(body: 'request-body')
aws-sdk-core/spec/seahorse/client/net_http/handler_spec.rb:235:              stub_request(:any, endpoint).to_return(status: 200)
aws-sdk-core/spec/seahorse/client/net_http/handler_spec.rb:241:              stub_request(:any, endpoint).to_return(headers: { foo: 'bar' })
aws-sdk-core/spec/seahorse/client/net_http/handler_spec.rb:247:              stub_request(:any, endpoint).to_return(body: 'response-body')
aws-sdk-core/spec/seahorse/client/net_http/handler_spec.rb:254:              stub_request(:any, endpoint).to_raise(EOFError)
aws-sdk-core/spec/seahorse/client/net_http/handler_spec.rb:265:              stub_request(:any, endpoint).to_raise(SocketError.new(msg))
aws-sdk-core/spec/spec_helper.rb:25:    stub_request(:get, "http://169.254.169.254#{path}").to_raise(SocketError)
aws-sdk-resources/spec/spec_helper.rb:25:    stub_request(:get, "http://169.254.169.254#{path}").to_raise(SocketError)
~~~


## Resource abstraction

aws-sdk-resources/lib/aws-sdk-resources/resource.rb



#Include REPL

/Users/nicolabrisotto/.rvm/gems/ruby-2.1.2/gems/aws-sdk-core-2.0.14/bin/aws.rb




TODO:

* How to Use SimpleCov https://github.com/colszowka/simplecov
* How to test Waiters
  * from minute 18 to minute 26: https://www.youtube.com/watch?v=9-PS5LtLZ9g



# Google API Client 
https://github.com/google/google-api-ruby-client
