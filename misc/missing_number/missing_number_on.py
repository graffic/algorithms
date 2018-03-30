def find_missing(items):
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
    for index, number in enumerate(items):
        if index + 1 != number:
            return index + 1
    # We assume that there is always one number missing, so 
    # if we cannot find one, is the last one
    return index + 2
