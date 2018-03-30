def filter_multiples(numbers):
    """
    >>> sum(filter_multiples(range(1000)))
    233168
    """
    for number in numbers:
        if number % 3 == 0:
            yield number
        elif number % 5 == 0:
            yield number
