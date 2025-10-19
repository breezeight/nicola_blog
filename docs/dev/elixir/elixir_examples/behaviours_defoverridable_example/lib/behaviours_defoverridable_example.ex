defmodule MyBehaviour do
  @callback handle_call(String.t) :: {:ok, term}
  @callback handle_call_optional(String.t) :: {:ok, term}

  @optional_callbacks handle_call_optional: 1

  defmacro __using__(_) do
    quote do
      @behaviour MyBehaviour

    end
  end
end



##########  CASE 1

defmodule MyCallbackModuleWarning1 do
  use MyBehaviour

  @impl MyBehaviour
  def handle_call(string), do: string

  def handle_call_optional(string), do: string  # This will trigger a warning because we used   @impl MyBehaviour on handle_call
end

defmodule MyCallbackModuleWarning1FIX do
  use MyBehaviour

  @impl MyBehaviour
  def handle_call(string), do: string

  @impl MyBehaviour
  def handle_call_optional(string), do: string
end




##########  CASE 2 : We are not using @impl; it's correct but it's not a best practice

defmodule MyCallbackModule2 do
  use MyBehaviour

  def handle_call(string), do: string
  def handle_call_optional(string), do: string
end

##########  CASE 3 : We are not using @impl; it's correct but it's not a best practice

defmodule MyCallbackModule3 do
  use MyBehaviour

  def handle_call(string), do: string
  def handle_call_optional(), do: "FOO"  # The intention was to implement the optional callback but we used the wrong arity;  See the fix below
end


defmodule MyCallbackModule3FIX do
  use MyBehaviour

  @impl MyBehaviour
  def handle_call(string), do: string

  @impl MyBehaviour
  def handle_call_optional(), do: "FOO"  # Using @impl is more safe, now the compiler will emit a warning
end
