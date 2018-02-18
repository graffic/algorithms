# Dice Throw / Sum of Dice Thrown

Imagine you are playing a board game. You roll a 6-faced dice and move forward the same number of spaces that you rolled. If the finishing point is “n” spaces away from the starting point, please implement a program that calculates how many possible ways are there to arrive exactly at the finishing point.

## If order matters

Meaning, for example, that two dices giving `{1, 2}` and `{2, 1}` count as two different combinations and not one.

### Brute force

For the specific `m` you want to achieve, you can throw a range of dices:
 * The minimum being almost-all 6: m // 2 plus one if the rest is not zero.
 * The maximum being all one: m itself

Brute force implies trying from the minimum amount of dices, to the maximum, how many combinations give us the right `m`. The time it needs is exponential.

Sum, for x from min to max, of number of nodes of a tree of x levels and degree 6. with one dice, we get 6 leaves, but with 2, we get 6*6, and even if we can cut some branches, still there is a lot of branching to do.

Although for a small m, it works:
| *m* | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 
|-----|---|---|---|---|---|---|---|---|---|----|----|----|----|
| *combinations* |1|2|4|8|16|32|63|125|248|492|976|1936|3840|



### The pattern

After running the brute force an interesting pattern arises:
* From 1 to 6, the combinations are 2^(0 to 5)
* From 7 onwards:
  * Sum of the previous six: 
  * Simplified in operations: (previous * 2) - results[:-7] Meaning if we're on the 7, we need to use the result fo 0 (special case, it is one), 8 we use the result for 1, and so on.

| *m* | 0 |1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 
|-----|---|---|---|---|---|---|---|---|---|---|----|----|----|----|
| *combinations* |1|1|2|4|8|16|32|63|125|248|492|976|1936|3840|
| *pattern* |1|1|2|4|8|16|32| 32\*2-1 | 63\*2-1 | 125\*2-2 | 248\*2-4 | 492\*2-8 | 976\*2-16 | 1936\*2-32 |

Why the 7 is the sum of the previous 6? Because 7 to get to seven we can do it by:
 * combinations to get to 6 + 1 in the last dice.
 * combinations to get to 5 + 2 in the last dice.
 * ...
 * combinations to get to 1 + 6 in the last dice.

So getting to 6 plus one in the last dice, is just the combinations of getting to 6.

The simplified calculation is because the sum of the previous six can be simplified:
  * `sum = x6 + x5 + x4 + x3 + x2 + x1`
  * `x6 = x5 + x4 + x3 + x2 + x1 + x0`
  * Now we can replace `x5 + x4 + x3 + x2 + x1` with `x6 - x0`
  * `sum = x6 + x6 - x0`


## If order does not matter

ToDo
