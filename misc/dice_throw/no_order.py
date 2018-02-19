from typing import List

def count(n: int) -> int:
    """
    >>> count(2)
    2
    >>> count(10)
    35
    """
    def count(n: int, dots: List[int]) -> int:
        if n == 0:
            return 1
        if len(dots) > 0 and n > 0:
            return count(n - dots[0], dots) + count(n, dots[1:])
        return 0
    
    return count(n, [1, 2, 3, 4, 5, 6])
