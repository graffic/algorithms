
#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

def hourglass_sum(arr, x, y):
    return arr[y][x] + arr[y][x+1] + arr[y][x+2] + arr[y+1][x+1] + arr[y+2][x] + arr[y+2][x+1] + arr[y+2][x+2]

def get_sums(arr):
    for x in range(4):
        for y in range(4):
            yield hourglass_sum(arr, x, y)

print(max(get_sums(arr)))
