
#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

def bubble_swipe(items):
    swaps = 0
    
    for i in range(len(items) - 1):
        if items[i] > items[i+1]:
            swaps += 1
            items[i], items[i+1] = items[i+1], items[i]
    return swaps
    
def bubble_sort(items):
    total_swaps = 0
    for _ in range(len(items)):
        swaps = bubble_swipe(items)
        total_swaps += swaps
        if swaps == 0:
            break
    return total_swaps

swaps = bubble_sort(a)
print("Array is sorted in {} swaps.\nFirst Element: {}\nLast Element: {}".format(
    swaps, a[0], a[-1]))

        
