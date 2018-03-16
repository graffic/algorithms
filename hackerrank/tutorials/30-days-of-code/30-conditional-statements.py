#!/bin/python3

import sys

def convert(number):
    if number % 2 > 0 or 6 <= number <= 20:
        return "Weird"
    return "Not Weird"

N = int(input().strip())

print(convert(N))