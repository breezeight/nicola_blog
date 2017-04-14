defmodule Cashy.Prova do

  @spec test_remote_type(Range.t) :: Range.t
  def test_remote_type(a) do
    a
  end

  @spec p(arg1, arg1) :: [arg1] when arg1: integer
  def p(arg1, arg2) do
    cond do
      arg1 >= arg2 ->
        IO.puts "maggiore"
      arg1 <= arg2 ->
        IO.puts "minore"
    end
  end

  def run do
    test_remote_type(1..2)

    p(1,2)
  end
end
