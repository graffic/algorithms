def problem():
    """
    >>> problem()
    25164150
    """
    n = 100
    res = (n * (n + 1) * (3*n + 2) * (n -1) ) // 12
    print(res)
