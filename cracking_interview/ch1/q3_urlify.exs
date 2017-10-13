ExUnit.start()

defmodule Ch1 do
  @moduledoc """
  Replace spaces with %20. In place in elixir... tuples?
  """

  def urlify(input) 
  when is_bitstring(input) do
    input = List.to_tuple(String.graphemes input)
    total = tuple_size(input) - 1
    find_end(input, total, total)
  end

  defp find_end(input, read, write)
  when elem(input, read) != " " do
    urlify(input, read, write)
  end

  defp find_end(input, read, write), do: find_end(input, read - 1, write)

  defp urlify(input, read, _)
  when read < 0 do
    List.to_string(Tuple.to_list input)
  end

  defp urlify(input, read, write)
  when elem(input, read) != " " do
    input = put_elem(input, write, elem(input, read))
    urlify(input, read - 1, write - 1)
  end

  defp urlify(input, read, write) do
    input
    |> put_elem(write, "0")
    |> put_elem(write - 1, "2")
    |> put_elem(write - 2, "%")
    |> urlify(read - 1, write - 3)
  end
end

defmodule Ch1Test do
  use ExUnit.Case, async: true

  test "urlifies 'a b  '" do
    assert Ch1.urlify("a b  ") === "a%20b"
  end

  test "urlifies ' b  a      '" do
    assert Ch1.urlify(" b  a      ") === "%20b%20%20a"
  end
end