from itertools import takewhile
from euler import primes_limit

def factors(number, possible_factors):
    holders = []
    for factor in possible_factors:
        amount = 0
        while number % factor == 0:
            amount += 1
            number = number // factor
        holders.append(amount)
        if number < factor:
            break
    return holders


if __name__ == "__main__":
    number = 20
    primes = tuple(primes_limit(number))
    result = [0] * len(primes)
    for n in range(2, number + 1):
        n_factors = factors(n, primes)
        for i, amount in enumerate(n_factors):
            if result[i] < amount:
                result[i] = amount

    # Build the final number
    number = 1
    for index, factor in enumerate(primes):
        times = result[index]
        while times:
            number *= factor
            times -= 1
    print(number)
