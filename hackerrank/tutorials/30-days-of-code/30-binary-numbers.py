#!/bin/python3

import sys

def max_consecutive_ones(num):
    max_consecutive = 0
    current_consecutive = 0
    for bit in format(num, 'b'):
        if bit == '0':
            max_consecutive = max(current_consecutive, max_consecutive)
            current_consecutive = 0
        else:
            current_consecutive += 1
    return max(max_consecutive, current_consecutive)

n = int(input().strip())



print(max_consecutive_ones(n))