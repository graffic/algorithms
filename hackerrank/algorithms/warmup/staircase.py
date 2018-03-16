#!/bin/python3

import sys

def staircase(n):
    for index in range(1, n+1):
      spaces = " " * (n-index)
      hashes = "#" * index
      print(spaces+hashes)

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)
