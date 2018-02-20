#!/bin/python3

import sys

def diagonalDifference(a):
    size = len(a)
    one = 0
    two = 0
    for i in range(size):
        one += a[i][i]
        two += a[i][size-i-1]
    return abs(one - two)

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)
