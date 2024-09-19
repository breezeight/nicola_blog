#!/bin/bash

my_var="foo"

echo "my_var is global: $my_var"

define_local_var ()
{
  local my_var="bar"
}

define_local_var

echo "my_var is NOT modified by the function: $my_var"

