defmodule Solution do
  def main() do
    a = read_int()
    b = read_int()
    IO.puts a+b
  end
  
  defp read_int() do
    IO.gets(nil) |> Integer.parse() |> elem(0)
  end
end

Solution.main()