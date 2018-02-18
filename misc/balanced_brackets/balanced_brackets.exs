defmodule BalancedBrackets do
  @doc """
  Checks if a series of brackets are correctly balanced
  """
  def isBalanced(input) when is_binary(input), do:
    isBalanced(String.graphemes(input), [])
  
  def isBalanced(["(" | rest], pending), do:
    isBalanced(rest, [")" | pending])
  
  def isBalanced(["{" | rest], pending), do:
    isBalanced(rest, ["}" | pending])
  
  def isBalanced(["[" | rest], pending), do:
    isBalanced(rest, ["]" | pending])
  
  def isBalanced(["}" | rest], ["}" | pending]), do:
    isBalanced(rest, pending)
  
  def isBalanced([")" | rest], [")" | pending]), do:
    isBalanced(rest, pending)
  
  def isBalanced(["]" | rest], ["]" | pending]), do:
    isBalanced(rest, pending)
  
  def isBalanced([], []), do: true
  def isBalanced(_, _), do: false
end

ExUnit.start()

defmodule BalancedBracketsTest do
  use ExUnit.Case, async: true

  test "{{[[(())]]}}", do:
    assert BalancedBrackets.isBalanced("{{[[(())]]}}")
  test "{[(])}", do:
    refute BalancedBrackets.isBalanced("{[(])}")
  test "()", do:
    assert BalancedBrackets.isBalanced("()")
  test "[({})](", do:
    refute BalancedBrackets.isBalanced("[({})](")
end