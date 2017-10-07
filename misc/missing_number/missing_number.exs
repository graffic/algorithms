defmodule FindMissing do
  def for(items) do
    last = tuple_size(items) - 1
    _middle(items, div(last, 2), 0, last)
  end

  defp _middle(items, middle, first, last) 
    when elem(items, middle) === middle + 1 and middle > first,
    do: _middle(items, div(last + middle, 2), middle, last)
  defp _middle(items, middle, first, last) 
    when elem(items, middle) !== middle + 1 and middle < last,
    do: _middle(items, div(first + middle, 2), first, middle)

  defp _middle(items, _, _, last)
    when elem(items, last) === last + 1,
    do: last + 2
  defp _middle(_, _, _, last), do: last + 1
end

IO.puts FindMissing.for({2,3,4,5,6,7,8,9})
IO.puts FindMissing.for({1,3,4,5,6,7,8,9})
IO.puts FindMissing.for({1,2,4,5,6,7,8,9})
IO.puts FindMissing.for({1,2,3,5,6,7,8,9})
IO.puts FindMissing.for({1,2,3,4,6,7,8,9})
IO.puts FindMissing.for({1,2,3,4,5,7,8,9})
IO.puts FindMissing.for({1,2,3,4,5,6,8,9})
IO.puts FindMissing.for({1,2,3,4,5,6,7,9})
IO.puts FindMissing.for({1,2,3,4,5,6,7,8})
