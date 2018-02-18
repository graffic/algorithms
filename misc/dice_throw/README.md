# Dice Throw / Sum of Dice Thrown

Imagine you are playing a board game. You roll a 6-faced dice and move forward the same number of spaces that you rolled. If the finishing point is “n” spaces away from the starting point, please implement a program that calculates how many possible ways are there to arrive exactly at the finishing point.

## Explanation

The number of times sum of n dice (6 sides) rollings is m can be found as coefficient of x^m when calculating (x+x^2+x^3+x^4+x^5+x^6)^n
