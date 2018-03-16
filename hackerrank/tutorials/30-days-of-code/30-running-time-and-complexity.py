from math import sqrt

def get_cases():
    num = int(input())
    while num > 0:
        yield int(input())
        num -= 1

def prime_check(case):
    if case == 1:
        return "Not prime"
    limit = int(sqrt(case))
    for x in range(2, limit + 1):
        if case % x == 0:
            return "Not prime"
    return "Prime"
        
for case in get_cases():
    print(prime_check(case))