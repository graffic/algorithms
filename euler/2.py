from itertools import takewhile


def fibonacci():
    """
    >>> sum(x for x in takewhile(lambda x: x <= 4000000, fibonacci()) if not x % 2)
    4613732
    """
    n2 = 0
    n1 = 1
    while True:
        res = n2 + n1
        yield res
        n2 = n1
        n1 = res
