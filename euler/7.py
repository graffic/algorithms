from euler import primes
from itertools import islice

def problem():
    """
    >>> problem()
    104743
    """
    print(next(islice(primes(), 10000, 10001)))
