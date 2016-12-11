---
layout: post
title: "Ruby: RSpec"
date: 2014-04-20 09:31:50 +0200
comments: true
categories: ["ruby"]
---

# Contents
{:.no_toc}

* Will be replaced with the ToC, excluding the "Contents" header
{:toc}

# Intro

RSpec is a tool to make Test-Driven Development. It is a multi-gem project:

* `rspec`:  a rich command line program
* `rspec-core`: textual descriptions of examples and groups
* `rspec-mocks`: built-in mocking/stubbing framework
* `rspec-expectations`: extensible expectation language
* `rspec-rails`: integration with rails

[Full documentation](https://relishapp.com/rspec/rspec-core/docs) generated
by cucumber features (`rspec-core/features`) is published on Relishapp

RSpec rubydoc is available here:

* [rspec-core](http://www.rubydoc.info/gems/rspec-core)
* [rspec-mocks](http://www.rubydoc.info/gems/rspec-mocks)
* [rspec-expectations](http://www.rubydoc.info/gems/rspec-expectations)
* [rspec-rails](http://www.rubydoc.info/github/rspec/rspec-rails)

# References

* https://www.relishapp.com/rspec/rspec-core/docs
* Intro:      http://rspec.info/
* rspec binary DOC: https://www.relishapp.com/rspec/
* http://www.intridea.com/blog/2012/3/23/polishing-rubies-part-iii
* RSPEC3 matcher for double number: http://wegowise.github.io/blog/2014/09/03/rspec-verifying-doubles/
* http://betterspecs.org/


# RSpec Quick Guide

## Other cheatsheets

* http://www.anchor.com.au/wp-content/uploads/rspec_cheatsheet_attributed.pdf

## Project directories conventions

* `**{,/*/**}/*_spec.rb` default spec pattern
* `spec/spec_helper.rb`  put configuration in and require assorted support files from here
* `require 'spec_helper`  It is also conventional to require that file from the spec files using require 'spec_helper'. This works because RSpec implicitly adds the spec directory to the LOAD_PATH.
* `lib`  added my rspec so your implementation files will be on the LOAD_PATH as well.


To start with a new project add to the root of the project the `Rakefile`:

~~~ruby
require 'rspec/core/rake_task'
RSpec::Core::RakeTask.new
task :default => :spec
~~~

and the `Gemfile`:

~~~ruby
source "http://rubygems.org"
group :development do
  gem 'rake'
  gem 'rspec'
end
~~~

### Getting start RAILS

see http://www.webascender.com/Blog/ID/566/Testing-Rails-4-Apps-With-RSpec-3-Part-I#.VUi_rlOUflA


~~~
group :development, :test do
  gem 'rspec-rails', '~> 3.0.0'
end

#RSpec generator to create the initial skeleton
rails generate rspec:install
~~~



## Run the test suite

* `bundle exec rake spec`
* `SPEC=spec/integration_spec.rb:109 rake spec` run the one spec at line 109

## ExampleGroups and Examples classes. DSL: describe, it, etc 

Ref: 
* official rspec doc about [ExampleGroup](http://www.rubydoc.info/gems/rspec-core/RSpec/Core/ExampleGroup) is well written and clear.

`describe` and `it` are the main keyword of the RSpec DSL, they create and configures instances of `ExampleGroup` an `Example` class. 

ExampleGroup and Example are the main structural elements of rspec-core. Consider this example:

~~~ruby
describe Thing do          ### return a subclass of ExampleGroup
  it "does something" do   ### return an instance of Example
  end
end
~~~

* Example group bodies (e.g. describe or context blocks) are evaluated in the context of a new subclass of ExampleGroup using `module_exec`
* Individual examples are evaluated in the context of an instance of the specific ExampleGroup subclass to which they belong.

In the next paragraph I will describe the code that create the DSL in details.


## Main concept and relationship

* the `describe` (alias: `context`) creates an `ExampleGroup`
* it  <-> Example
* let <->
* subject <->
* expect <->   ExpectationTarget
* to, to_not  <->   PositiveExpectationHandler,  NegativeExpectationHandler
* Expectations are the “left-side” part of the example. The “right-side” part is the Matcher.
* ExpectationHandler  <-> Matcher


## Hooks

Read the official rspec doc about
[hooks](http://www.rubydoc.info/gems/rspec-core/RSpec/Core/Hooks)

Hooks have scopes:

~~~ruby
describe MyClass do
  before(:each) { } # runs before each example in this group
  before(:all)  { } # runs once before the first example in this group
end
~~~

~~~ruby
RSpec.configure do |c|
  c.before(:each)  { } # runs before each example in the entire test suite
  c.before(:all)   { } # runs before the first example of each top-level group
  c.before(:suite) { } # runs once after all spec files have been loaded, before the first spec runs
end
~~~


In this context, the term :all suggests that this hook will run once before all examples in the suite — but that is what :suite is for.
In RSpec 3, :each and :all have aliases that make their scope more explicit: :example is an alias of :each and :context is an alias of :all. Note that :each and :all are not deprecated and we have no plans to do so.

## SharedExamples

Ref: http://modocache.svbtle.com/shared-examples-in-rspec

Shared examples make testing compositions of objects much easier. In a
nutshell, they allow us to execute the same group of expectations
against several classes:

Use-Case: maintain a large class composed of many small modules (Mixin)

* `#it_behaves_like`
* `shared_examples`

### Example: Test Acceleratable mixin

Example: Using the `Acceleratable` mixin, it’s easy to create two
classes which can accelerate: a `Car` and a `Motorcycle`:

~~~ruby
acceleratable.rb

module Acceleratable
  attr_reader :speed

  def initialize
    @speed = 0
  end

  def accelerate!
    @speed += 10
  end
end

car.rb

require 'acceleratable'

class Car
  include Acceleratable
end

motorcycle.rb

require 'acceleratable'

class Motorcycle
  include Acceleratable

  def wheelie!
    puts 'Check out this sick wheelie, bro!'
    @speed -= 5
  end
end
~~~

The tests for the `#accelerate!` method are practically identical in Car and Motorcycle. Using the #shared_examples method, we can extract these tests into a single location:

~~~ruby
acceleratable_spec_helper.rb

shared_examples 'an acceleratable' do
  let(:acceleratable) { described_class.new }

  describe 'speed' do
    it 'is initially zero' do
      acceleratable.speed.should == 0
    end
  end
end

car_spec.rb

require 'car'
require 'acceleratable_spec_helper'

describe Car do
  it_behaves_like 'an acceleratable' execute the expectations against Car
end

motorcycle_spec.rb

require 'motorcycle'
require 'acceleratable_spec_helper'

describe Motorcycle do
  it_behaves_like 'an acceleratable' ### execute the expectations against Motorcycle
  describe 'other methods' do
    ...
  end
end
~~~

## RSpec-Mock

Ref: https://semaphoreci.com/community/tutorials/mocking-with-rspec-doubles-and-expectations

* `Double`  is a simplified object which takes the place of another object in a test.* `allow()`
* `receive()` 
* .... 
* Full doc: https://relishapp.com/rspec/rspec-mocks/v/3-5/docs/configuring-responses


# RSPEC Under the HOOD: Internals and how to extend RSpec

References:

* http://modocache.svbtle.com/rspec-under-the-covers
* http://modocache.svbtle.com/code-reading-shared-examples-in-rspec
* http://blog.endpoint.com/2014/09/some-metaprogramming-examples-from-rspec.html?m=1

RSpec is a DSL for creating executable examples of how code is expected to behave, organized in groups.


## The RSpec Binary, RSpec::Configuration and spec files loading

RSPEC VERSION: `v3.1.7`

When you start the [rspec command line tool](https://github.com/rspec/rspec-core/blob/v3.1.7/exe/rspec), it delegates everything to the `RSpec::Core::Runner.invoke` method of the `Runner` class [RSpec::Core::Runner.invoke](https://github.com/rspec/rspec-core/blob/v3.1.7/lib/rspec/core/runner.rb#L35), it will:

* Create an instance of Runner
* call `RSpec::Core::Runner#run` on it, it will execute the suite of RSpec examples.

The execution of a spec suite is divided in 2 phases:

* setup
  * All the DSL methods alias of ExampleGroup are executed, they will setup Example for later execution 

* run_specs
  * All Example are executed

### Setup

The Runner delegates the options parsing from command line, configuration file, etc... to `ConfigurationOptions`

`RSpec::Core::Runner#setup` wires together the various configuration objects and state holders:

~~~ruby
def setup(err, out)
  @configuration.error_stream = err
  @configuration.output_stream = out if @configuration.output_stream == $stdout
  @options.configure(@configuration)
  @configuration.load_spec_files
  @world.announce_filters
end
~~~

The `RSpec::Core::Configuration` Class is responsible for loading spec file: [RSpec::Core::Configuration#load_spec_files](https://github.com/rspec/rspec-core/blob/v3.1.7/lib/rspec/core/configuration.rb#L1104). This method will use the ruby `Kernel#load` method to load all spec files listed in the configuration:

~~~ruby
def load_spec_files
  files_to_run.uniq.each {|f| load File.expand_path(f) }
  @spec_files_loaded = true
end
~~~

`RSpec::configuration` keeps the global configuration object.

### Run

* Fa qualceh mageggio con gli hook
* Call the `ExampleGroup#run` on every ExampleGroup registered in `@world.ordered_example_groups`
* use the `RSpec::Core::Reporter` specified in the configuration (See for details about Reporter and Listeners)
* more comments is provided inline below

~~~ruby
def run_specs(example_groups)
  @configuration.reporter.report(@world.example_count(example_groups)) do |reporter|
    begin
      hook_context = SuiteHookContext.new
      @configuration.hooks.run(:before, :suite, hook_context)
      example_groups.map { |g| # RUN all the exa
        g.run(reporter) # return 0 if the example_group pass
      }.all? ? 0 : @configuration.failure_exit_code # return 0 only if 
    ensure
      @configuration.hooks.run(:after, :suite, hook_context)
    end
  end
end
~~~


`ExampleGroup#run` runs all the examples in this group and in the children groups

~~~ruby
def self.run(reporter)
  if RSpec.world.wants_to_quit
    RSpec.world.clear_remaining_example_groups if top_level?
    return
  end
  reporter.example_group_started(self)

  begin
    run_before_context_hooks(new)
    result_for_this_group = run_examples(reporter) # Run example in the group
    results_for_descendants = ordering_strategy.order(children).map { |child| child.run(reporter) }.all? #Run children
    result_for_this_group && results_for_descendants
  rescue Pending::SkipDeclaredInExample => ex
    for_filtered_examples(reporter) { |example| example.skip_with_exception(reporter, ex) }
  rescue Exception => ex
    RSpec.world.wants_to_quit = true if fail_fast?
    for_filtered_examples(reporter) { |example| example.fail_with_exception(reporter, ex) }
  ensure
    run_after_context_hooks(new)
    before_context_ivars.clear
    reporter.example_group_finished(self)
  end
end
~~~


~~~ruby
def self.run_examples(reporter)
  ordering_strategy.order(filtered_examples).map do |example|
    next if RSpec.world.wants_to_quit
    instance = new
    set_ivars(instance, before_context_ivars)
    succeeded = example.run(instance, reporter)
    RSpec.world.wants_to_quit = true if fail_fast? && !succeeded
    succeeded
  end.all?
end
~~~


NOTE: Enumerable#All? without a block return true when none of the collection members are
false or nil.

## Reporter

A reporter will send notifications to listeners, usually formatters for the spec suite run.

* the `#report` method is important
  * notify listener when it start and when it finish the execution of the block


The interface of the reporter is used by Example groups to log:

* `reporter.example_group_started(self)`
* `reporter.example_group_finished(child)`
* ....

## The DSL Module

`RSpec::Core::DSL` Module defines helper methods to add the rspec DSL to the RSpec module and globally.

For example `RSpec::Core::DSL::expose_example_group_alias(name)` is used to define `describe`, `context`, etc...

~~~ruby
def self.expose_example_group_alias(name)
  example_group_aliases << name

  (class << RSpec; self; end).__send__(:define_method, name) do |*args, &example_group_block|
    RSpec.world.register RSpec::Core::ExampleGroup.__send__(name, *args, &example_group_block)   # TopLevel ExampleGroup instances are registered into RSpec.world
  end

  expose_example_group_alias_globally(name) if exposed_globally?
end
~~~

`(class << RSpec; self; end)` returns the `RSpec` singleton class, so the `:define_method` will add a class method to the RSpec module.
 

### DSL: Methods to define ExampleGroups and Examples

Most of the RSpec DSL keywords are mapped to few internal classes. Each
keyword is implemented as a ruby method.

`example_group`, `describe`, `context`, `xdescribe`, `xcontext`, `fdescribe`,`fcontext`
keywords are defined using the
[ExampleGroup.define_example_group_method](https://github.com/rspec/rspec-core/blob/v3.1.7/lib/rspec/core/example_group.rb#L197).

This is a simplified version:

~~~ruby
class ExampleGroup

  def self.define_example_group_method(name, metadata={})
    define_singleton_method(name) do |*args, &example_group_block|          # Define the DSL method
      subclass(self, description, args, &example_group_block).tap do |child|
        children << child
      end
    end
    RSpec::Core::DSL.expose_example_group_alias(name)
  end

  ...
  define_example_group_method :example_group
  define_example_group_method :describe
  define_example_group_method :context
  ... 
end
~~~

All ExampleGroup methods return subclasses of ExampleGroup created by the `ExampleGroup::subclass` method.

~~~ruby
class ExampleGroup
  def self.subclass(parent, description, args, &example_group_block)
    subclass = Class.new(parent)                                        # instantiate a new subclass of parent
    subclass.set_it_up(description, *args, &example_group_block) 
    ExampleGroups.assign_const(subclass)                                # Generate the class const from the description
    subclass.module_exec(&example_group_block) if example_group_block   # evaulate the example group block 

    # The LetDefinitions module must be included _after_ other modules
    # to ensure that it takes precedence when there are name collisions.
    # Thus, we delay including it until after the example group block
    # has been eval'd.

    MemoizedHelpers.define_helpers_on(subclass)

    subclass
  end
end
~~~

* Each example group create an ExampleGroup subclass
* The block argument of each example group is evaluated in the contect of the class created
* `ExampleGroup::children` is an `Array` of all the ExampleGroup defined by the block.

~~~ruby
describe "My Dream" do      # create the RSpec::ExampleGroups::MyDream class
  # This is evauated in the context of RSpec::ExampleGroups::MyDream
  describe "My First Nested dream"  do
    # This is evauated RSpec::ExampleGroups::MyDream::MyFirstNestedDream
    it "make me rich" do
    end
  end

  describe "My Second Nested dream"  do
    it "make me happy" do
    end
  end

  # children => [ RSpec::ExampleGroups::MyDream::MyFirstNestedDream,  RSpec::ExampleGroups::MyDream::MySecondNestedDream ]
end
~~~

There is a very important difference between the top level `describe My Dream` and the nested  `describe My First Nested dream`.

The former is a class method of RSpec module defined here:

~~~ruby
    Module DSL
      def self.expose_example_group_alias(name)
        example_group_aliases << name

        (class << RSpec; self; end).__send__(:define_method, name) do |*args, &example_group_block|
          RSpec.world.register RSpec::Core::ExampleGroup.__send__(name, *args, &example_group_block)  #The exposed alias also register each ExmapleGroup in RSpec.world
        end

        expose_example_group_alias_globally(name) if exposed_globally?
      end
~~~

While the second is a class method of the `ExampleGroup` class. The only difference is that the first will register top-level ExampleGroups in the global `RSpec.world` into an array of all top-level ExampleGroup: `RSpec.world.example_groups`. When rspec runs the test suite, it iterates these array and for each ExampleGroup executes the nested ExampleGroup.


Each example group is associated with a set of examples and holds a reference to any child example groups it may contain (`ExampleGroup::children`).



`example_group.rb` uses the `define_example_method` [ExampleGroup.define_example_method](https://github.com/rspec/rspec-core/blob/v3.1.7/lib/rspec/core/example_group.rb#L109)
to define these keywords: `example` , `it`, `specify`, `focus`, `fexample`, `fit`,
`fspecify`, `xexample`, `xit`, `xspecify`, `skip`, `pending`. This
method use ruby metaprogramming `define_method` to define a method for
each keyword, thes methods will be added to the `ExampleGroup` class.

All these method return an instance of `RSpec::Core::Example`:

~~~ruby
      def self.define_example_method(name, extra_options={})
        define_singleton_method(name) do |*all_args, &block|
          desc, *args = *all_args

          options = Metadata.build_hash_from(args)
          options.update(:skip => RSpec::Core::Pending::NOT_YET_IMPLEMENTED) unless block
          options.update(extra_options)

          examples << RSpec::Core::Example.new(self, desc, options, block)    ### NEW Example INSTANCE ###
          examples.last
        end
      end

      # Defines an example within a group.
      define_example_method :example
      # Defines an example within a group.
      # This is the primary API to define a code example.
      define_example_method :it
~~~

## How ExampleGroups and Example are executed

Under the hood, an `ExampleGroup` is a class in which the block passed to the `describe` (or equivalent) is evaluated.

The blocks passed to it are evaluated in the context of an instance of that class.

~~~ruby
burrito_spec.rb

describe "burrito" do
  it "is delicious" do end

  describe "just how delicious" do
    it "is so very delicious"
  end

  describe "spiciness" do end
end
~~~


The “burrito” ExampleGroup holds a reference to

* the "is delicious" Example
* child ExampleGroups "just how delicious" and "spiciness"

RSpec iterates over each ExampleGroup list of Examples and for each one invokes hooks and the `Example#run(example_group_instance, reporter)` method.

## Hooks

Read the official rspec doc about
[hooks](http://www.rubydoc.info/gems/rspec-core/RSpec/Core/Hooks)

The module `RSpec::Core::Hooks` is extended into `ExampleGroup`

Each ExampleGroup subclass has a public `HookCollections`:

* `RSpec::Core::Hooks#hooks`
* `ExampleGroup::hooks`

Defined as:

~~~ruby
      def hooks
        @hooks ||= HookCollections.new(
          self,
          :around => { :example => AroundHookCollection.new },     ##THIS HASH will be accessible from HookCollections#[]
          :before => { :example => HookCollection.new, :context => HookCollection.new, :suite => HookCollection.new },
          :after  => { :example => HookCollection.new, :context => HookCollection.new, :suite => HookCollection.new }
        )
      end
~~~


## Custom Output formatting

`ExampleGroup#run` takes an instance of `RSpec::Core::Reporter` as an
argument. This class maintains an array of `#listeners` which are
expected to respond to methods such as `#example_group_started` or
`#example_failed`. This is the key to RSpec’s extensible output formatting system. Kiwi could borrow this technique to address issue #306, which specifically requests custom formatting.

## Shared Example Groups

Shared example groups are stored in a registry separate from normal
example groups: the singleton object
`RSpec::Core::SharedExampleGroup.registry` maintains a hash of shared examples, using the shared example name as a key.

Shared examples are registered by using the `RSpec::Core::TopLevelDSL`
method ` #shared_examples` in your spec file. This method stores the block of code associated with the shared example in the registry.

Later, when each example group is run by `RSpec.world`, any
`#it_behaves_like` methods encountered during execution cause a lookup
to the corresponding shared example group in the registry. If found, the
block of code mapped to that key is executed. In this sense,
`#it_behaves_like` acts like a placeholder for a shared example group.

## Expectation

## Matchers

http://danielchangnyc.github.io/blog/2014/01/15/tdd2-RSpecMatchers/




## RSpec3 Zero Monkey-Patching Mode

http://modocache.svbtle.com/rspec-under-the-covers



# Live Documentation

## RelishApp

free for OpenSource projects

Relish lets you mix pages of documentation pages made from executable Cucumber features, or plain old Markdown files. You can use a special .nav file to control the order in which pages are displayed in the left-hand navigation menu to give you more editorial control.

https://www.relishapp.com/relish/relish/docs/living-documentation


# MISC

## Upgrade from RSpec2 to RSpec3

One of the may news is the new "expect" syntax, it allows RSpec to avoid monkey-patching the Ruby Object class.

* ref: Upgrade guide from rspec2: https://relishapp.com/rspec/docs/upgrade
* ref: Notable Changes in RSpec 3 http://myronmars.to/n/dev-blog/2014/05/notable-changes-in-rspec-3
* RSPEC3 composable matcher: http://myronmars.to/n/dev-blog/2014/01/new-in-rspec-3-composable-matchers

* `should` syntax is deprecated
* monkey pathching can be disabled

## Example yield

~~~ruby
describe MyClass do
  before(:example) { |ex| puts ex.metadata }
  let(:example_description) { |ex| ex.description }

  it 'accesses the example' do |ex|
    # use ex
  end
end
~~~
