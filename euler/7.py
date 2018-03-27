from .euler import primes
from itertools import islice

if __name__ == "__main__":
    print(next(islice(primes(), 10000, 10001)))
