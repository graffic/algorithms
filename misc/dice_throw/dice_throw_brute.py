SIDES = 6
LIMIT = SIDES + 1

def brute_count(dices, steps):
    """
    >>> brute_count(20, -5)
    0
    >>> brute_count(3, 0)
    0
    >>> brute_count(0, 0)
    1
    >>> brute_count(3, 3)
    1
    >>> brute_count(3, 10)
    27
    """
    if steps < 0:
        return 0

    if dices == 0:
        return 1 if steps == 0 else 0

    counter = 0
    for number in range(1, SIDES + 1):
        counter += brute_count(dices - 1, steps - number)
    return counter

def calculate_brute(steps):
    """
    >>> calculate_brute(13) 
    3840
    """
    start = steps // SIDES
    if steps % SIDES > 0:
        start += 1
    
    return sum(brute_count(n, steps) for n in range(start, steps + 1))