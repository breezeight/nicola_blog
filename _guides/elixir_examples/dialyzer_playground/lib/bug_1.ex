defmodule Cashy.Bug1 do
  def convert(:sgd, :usd, amount) do
    {:ok, amount * 0.70}
  end

  def run do
    convert(:sgd, :usd, :one_million_dollars) # :one_million_dollars * 0.70 causes ArithmeticError
  end
end
