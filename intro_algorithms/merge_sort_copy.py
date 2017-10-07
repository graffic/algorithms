"""
Merge sort in a new tuple

Instead of doing it in place, we create new tuples
"""
from math import inf


def merge(first, second):
    """
    merges two sorted iterables from items in place

    >>> merge((1, 3), (2, 4))
    (1, 2, 3, 4)
    >>> merge((2,), (1,))
    (1, 2)
    >>> merge((1, 5), (3,))
    (1, 3, 5)
    """
    left = first + (inf,)
    right = second + (inf,)

    l_index = 0
    r_index = 0
    # We could use tuples, here a mutable list fits better
    result = []
    for i in range(len(first) + len(right) - 1):
        if left[l_index] < right[r_index]:
            result.append(left[l_index])
            l_index += 1
        else:
            result.append(right[r_index])
            r_index += 1

    return tuple(result)


def merge_sort(items):
    """
    Non recursive merge sort.

    >>> merge_sort([4, 3, 2, 1, 0])
    (0, 1, 2, 3, 4)
    >>> merge_sort([5, 1, 2, 4])
    (1, 2, 4, 5)
    """
    length = len(items)
    if length < 2:
        return items

    tuples = ((i,) for i in items)
    while length != 1:
        new_result = []
        skip = True
        previous = None
        for i in tuples:
            if skip:
                skip = False
                previous = i
            else:
                new_result.append(merge(previous, i))
                skip = True
        if not skip:
            new_result.append(previous)
        length = len(new_result)
        tuples = new_result

    return tuples[0]
