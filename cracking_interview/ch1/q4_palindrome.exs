ExUnit.start()

defmodule Ch1 do
  @moduledoc """
  Check if a string is a permutation of a palindome
  """
  use Bitwise

  @doc "Using a map"
  def pp?(input) do
    input
    |> String.downcase()
    |> map_odd()
    |> Map.values()
    |> Enum.count(&(&1)) < 2
  end

  defp map_odd(data, map \\ %{})
  defp map_odd(<<>>, map), do: map
  defp map_odd(<<" ", rest::bitstring>>, map), do: map_odd(rest, map)
  defp map_odd(<<item::utf8, rest::bitstring>>, map) do
    {_, map} = Map.get_and_update(map, item, fn 
      nil -> {nil, True}
      value -> {value, !value}
    end)
    map_odd(rest, map)
  end
  

  @doc "Using bits"
  def pp2?(input) do 
    input
    |> String.downcase()
    |> mark_odd()
    |> :binary.encode_unsigned()
    |> sum_bits() < 2
  end

  defp mark_odd(data, accum \\ 0)
  defp mark_odd(<<>>, accum), do: accum
  defp mark_odd(<<" ", rest::bitstring>>, accum), do: mark_odd(rest, accum)
  defp mark_odd(<<item::utf8, rest::bitstring>>, accum),
    do: mark_odd(rest, accum ^^^ (1 <<< item)) 

  defp sum_bits(bits, sum \\ 0)
  defp sum_bits(<<>>, sum), do: sum
  defp sum_bits(<<bit::1, rest::bitstring>>, sum), do: sum_bits(rest, sum + bit)
end

defmodule Ch1Test do
  use ExUnit.Case, async: true

  test "is pp 'Tact Coa'" do
    assert Ch1.pp?("Tact Coa")
  end

  test "is pp 'Tact Coaa'" do
    assert !Ch1.pp?("Tact Coaa")
  end

  test "is pp2 'Tact Coa'" do
    assert Ch1.pp2?("Tact Coa")
  end

  test "is pp2 'Tact Coaa'" do
    assert !Ch1.pp2?("Tact Coaa")
  end
end