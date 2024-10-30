defmodule KeywordListExample do
  @moduledoc """
  Documentation for TypeSpecDemo.
  """


  @spec hello([bar: String.t, baaz: String.t]) :: {:world, list}
  def hello(opts \\ []) do
    {:world, opts}
  end

  # correct usage
  def default_to_empty_list, do: hello()
  def call_with_empty_list, do: hello([])
  def first_key_only, do: hello(bar: "bar")
  def second_key_only, do: hello([baaz: "baaz"])
  def both_keys_in_order, do: hello([bar: "bar", baaz: "baaz"])
  def both_keys_reversed, do: hello([baaz: "baaz", bar: "bar"])

  # incorrect usage
  def bad_arg, do: hello("world")
  def unknown_key, do: hello(foo: "foo")
  def wrong_value, do: hello(baaz: 15)

end
