from itertools import takewhile
from math import sqrt

from euler import primes


def problem():
    """
    >>> problem()
    6857
    """
    number = 600851475143
    limit = int(sqrt(number))
    res = 1
    for prime in takewhile(lambda x: x<= limit, primes()):
        if number % prime == 0:
            res = prime
    return res
