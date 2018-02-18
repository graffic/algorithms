import sys

SIDES = 6
LIMIT = SIDES + 1

def calculate(steps):
    """
    >>> calculate(610)
    14527490260516100855695859704819627818108010882741117227956927412305738742399171256642436462028811566617818991926058940988565927870172608545709804976244851391054850231415387973537361
    """
    precalculated = [1] + [2**x for x in range(0, SIDES)]
    if steps < LIMIT:
        return precalculated[steps]

    for _ in range(LIMIT, steps + 1):
        previous = precalculated[-1]
        total = previous + previous - precalculated[-LIMIT]
        precalculated.append(total)
    return total
