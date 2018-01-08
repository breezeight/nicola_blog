defmodule BehavioursDefoverridableExampleTest do
  use ExUnit.Case
  doctest BehavioursDefoverridableExample

  test "greets the world" do
    assert BehavioursDefoverridableExample.hello() == :world
  end
end
