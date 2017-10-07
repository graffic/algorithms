def find_missing(numbers):
    """
    >>> find_missing([1,2,3,4,5,6,7,8])
    9
    >>> find_missing([2,3,4,5,6,7,8,9])
    1
    >>> find_missing([1,2,3,4,5,6,7,9])
    8
    >>> find_missing([1,3,4,5,6,7,8,9])
    2
    >>> find_missing([1,2,4,5,6,7,8,9])
    3
    >>> find_missing([1,3,4,5,6])
    2
    >>> find_missing([1,2,3,4,6])
    5
    >>> find_missing([1,2,4,5,6])
    3
    """
    left = 0
    right = len(numbers) - 1

    while left < right:
        middle = (left + right) // 2
        if numbers[middle] != middle + 1:
            if right == middle:
                return middle + 1
            right = middle
        else:
            if left == middle:
                if numbers[right] == right + 1:
                    return right + 2
                return right + 1
            left = middle
    return 1
