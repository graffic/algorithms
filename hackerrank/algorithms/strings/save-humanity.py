
#!/bin/python3

import sys

def virusIndices(p, v):
    # Print the answer for this test case in a single line
    results = []
    for index in range(len(p)):
        allowed_fails = 1
        for i2 in range(len(v)):
            if index + i2 >= len(p):
                break
            if v[i2] != p[index + i2]:
                if allowed_fails == 0:
                    break
                allowed_fails -= 1
        else:
            results.append(str(index))
    
    if len(results) > 0:
        print(" ".join(results))
    else:
        print("No Match!")
        

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        p, v = input().strip().split(' ')
        p, v = [str(p), str(v)]
        virusIndices(p, v)

