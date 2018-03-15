
#!/bin/python3

import sys

def points(a, b):
    if a > b:
        return 1, 0
    if a == b:
        return 0, 0
    return 0, 1

def solve(a_points, b_points):
    total_a = 0
    total_b = 0 
    for a_point, b_point in zip(a_points, b_points):
        a, b = points(a_point, b_point)
        total_a += a
        total_b += b
    
    return (total_a, total_b)
    

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve([a0, a1, a2], [b0, b1, b2])
print (" ".join(map(str, result)))



