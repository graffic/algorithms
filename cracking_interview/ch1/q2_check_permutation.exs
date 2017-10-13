ExUnit.start()

defmodule Ch1 do
  @moduledoc """
  Given two string, check if one is permutation of the other
  """

  @doc "Using sorting"
  def permutation?(one, other) when length(one) != length(other), do: False
  def permutation?(one, other) do
    Enum.sort(String.graphemes one) == Enum.sort(String.graphemes other)
  end

  @doc "counting codepoints"
  def permutation2?(one, other) when length(one) != length(other), do: False
  def permutation2?(one, other), do: count(one) == count(other)
  
  defp count(string, counter \\ %{})
  defp count("", counter), do: counter
  defp count(<<point::utf8, rest::bitstring>>, counter) do
    counter = elem(Map.get_and_update(counter, point, fn
      nil -> {nil, 1}
      value -> {value, value + 1}
    end), 1)
    count(rest, counter)
  end
end

defmodule Ch1Test do
  use ExUnit.Case, async: true

  test "Is permutation" do
    assert Ch1.permutation?("abcd", "dcba")
  end

  test "Is not permutation length" do
    assert !Ch1.permutation?("abcd", "dcb")
  end

  test "Is not permutation" do
    assert !Ch1.permutation?("abcd", "dcbe")
  end

  test "Is permutation2" do
    assert Ch1.permutation2?("abcd", "dcba")
  end

  test "Is not permutation2 length" do
    assert !Ch1.permutation2?("abcd", "dcb")
  end

  test "Is not permutation2" do
    assert !Ch1.permutation2?("abcd", "dcbe")
  end
end