from itertools import takewhile, count
from math import sqrt


def primes():
    """
    Generates an infinite amount of primes
    time O(N)
    space O(logN)
    """
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def prime_factorization(number, primes):
    """
    Prime factorization using a precalculated prime list

    >>> number = 1002
    >>> primes = tuple(primes_limit(number))
    >>> prime_factorization(number, primes)
    [(2, 1), (3, 1), (167, 1)]
    >>> prime_factorization(1000, primes)
    [(2, 3), (5, 3)]
    """
    result = []
    for prime in primes:
        amount = 0
        while number % prime == 0:
            amount += 1
            number = number // prime
        if amount:
            result.append((prime, amount))
        if number == 1:
            break
    return result


def primes_limit(limit):
    is_prime = [False] * limit
    sqlimit = int(sqrt(limit)) + 1

    # Optimization 1:
    # If 4x^2 + y^2 <= limit, being y positive, then this is also true
    # 4x^2 <= limit, x <= sqrt(limit/4)
    # So that is a smaller limit for the loop
    for x in range(1, int(sqrt(limit/4)) + 1):
        mult = 4 * x * x
        # Optimization 2:
        # Now we know x, so: 4x^2 + y^2 <= limit becomes:
        # y <= sqrt(limit - 4x^2)
        # Another smaller limit for y
        for y in range(1, int(sqrt(limit - mult)) + 1, 2):
            k = mult + y * y
            if k < limit and (k % 12 == 1 or k % 12 == 5):
                is_prime[k] = not is_prime[k]

    # Optimization like 1
    # Optimization 3, x must be odd (from observation)
    for x in range(1, int(sqrt(limit/3)) + 1, 2):
        mult = 3 * x * x
        # Optimization like 2
        y_limit = int(sqrt(limit - mult)) + 1
        # Optimization 4, numbers start from 2 and go +2+4+2+4...
        # from observation
        y = 2
        use_two = True
        while y < y_limit:
            k = mult + y * y
            if k < limit and k % 12 == 7:
                is_prime[k] = not is_prime[k]
            y += 2 if use_two else 4
            use_two ^= True

    for x in range(1, sqlimit):
        # yy >= 3xx-limit
        # y >= sqrt(3xx-limit)
        mult = 3 * x * x
        y = 1
        check = mult - limit
        if check > 0:
            y = int(sqrt(check))
        # If x is odd y should be even and viceversa
        if x % 2 == y % 2:
            y += 1
        while y < x:
            k = mult - y * y
            if k < limit and k % 12 == 11:
                is_prime[k] = not is_prime[k]
            y += 2

    is_prime[2] = True
    is_prime[3] = True
    for n in range(5, sqlimit):
        if is_prime[n]:
            mult = n * n
            for k in range(mult, limit, mult):
                is_prime[k] = False

    for n in range(2, limit):
        if is_prime[n]:
            yield n


def primes_limit_orig(limit):
    is_prime = [False] * limit
    sqlimit = int(sqrt(limit)) + 1

    for x in range(1, sqlimit):
        for y in range(1, sqlimit):
            k = 4 * x * x + y * y
            if k < limit and (k % 12 == 1 or k % 12 == 5):
                is_prime[k] = not is_prime[k]
            k = 3 * x * x + y * y
            if k < limit and k % 12 == 7:
                is_prime[k] = not is_prime[k]
            if x > y:
                k = 3 * x * x - y * y
                if k < limit and k % 12 == 11:
                    is_prime[k] = not is_prime[k]

    is_prime[2] = True
    is_prime[3] = True
    for n in range(5, sqlimit):
        if is_prime[n]:
            mult = n * n
            for k in range(mult, limit, mult):
                is_prime[k] = False

    for n in range(2, limit):
        if is_prime[n]:
            yield n


if __name__ == "__main__":
    import doctest
    doctest.testmod()
