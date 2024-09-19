#!/bin/bash

define_not_local_var ()
{
  not_local_variable="bar"
}

define_not_local_var

echo "not_local_variable is global: $not_local_variable"

