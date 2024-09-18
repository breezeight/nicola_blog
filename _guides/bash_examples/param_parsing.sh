#!/bin/bash


COMMAND="${1-}"


case $COMMAND in
  'help' | '--help' )
    echo "help"
  ;;
  'install' | '--install' )
    echo "install"
  ;;
esac


