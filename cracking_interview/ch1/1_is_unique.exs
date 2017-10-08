ExUnit.start()

defmodule Ch1 do
  @moduledoc """
  Check if a string has all unique characters
  """
  use Bitwise, only_operators: true

  @doc "Is unique using a bitstring"
  def unique?(input), do: unique?(input, 0, 1)

  defp unique?(_, _, 0), do: false

  defp unique?("", _, _), do: true

  defp unique?(<<item::utf8, rest::bitstring>>, current, _) do
    mask = 1 <<< item
    next = current ^^^ mask
    unique?(rest, next, next &&& mask)
  end

  @doc "Is unique using sorting"
  def unique2?(input), do: unique2? Enum.sort(String.graphemes input), ""

  defp unique2?([current | _], current), do: false

  defp unique2?([], _), do: true

  defp unique2?([current | tail], _), do: unique2? tail, current
end

defmodule Ch1Test do
  use ExUnit.Case, async: true

  test "Is unique" do
    assert Ch1.unique?("abcd")
  end

  test "Is not unique" do
    assert !Ch1.unique?("abcda")
  end

  test "Is unique2" do
    assert Ch1.unique2?("abcd")
  end

  test "Is not unique2" do
    assert !Ch1.unique2?("abcda")
  end
end