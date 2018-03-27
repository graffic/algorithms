from itertools import takewhile
from math import sqrt

from .euler import primes


if __name__ == "__main__":
    number = 600851475143
    limit = int(sqrt(number))
    res = 1
    for prime in takewhile(lambda x: x<= limit, primes()):
        if number % prime == 0:
            res = prime
    print(res)
