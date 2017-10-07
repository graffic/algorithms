from euler import prime_factorization, primes_limit


def num_divisors(factors):
    res = 1
    for factor in factors:
        res *= factor[1] + 1
    return res


if __name__ == "__main__":
    limit = 20000
    primes = tuple(primes_limit(limit))
    amount_prev = 1
    for x in range(2, limit):
        if x % 2 == 0:
            factors = prime_factorization(x + 1, primes)
        else:
            factors = prime_factorization((x + 1) // 2, primes)
        amount = num_divisors(factors)
        total = amount_prev * amount
        if total > 500:
            break
        amount_prev = amount
    number = x*(x+1)//2
    print("%d th is %d" %(x, number))
