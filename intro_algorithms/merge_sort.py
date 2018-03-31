"""
Merge sort

Divide an conquer strategy: divide the list in two till we have the two
smallest lists of one item, then merge sorted arrays

Merging sorted is TH(n) and we do that log(n). So it is TH(n log())

Sorting is in place, but the code returns the array given.
"""
from math import inf


def merge(items, p, q, r):
    """
    merges two sorted sub arrays from items in place
    - items[p..q]  items[q+1..r]
    - p<=q<r

    >>> merge([1, 3, 2, 4], 0, 1, 3)
    [1, 2, 3, 4]
    >>> merge([2, 1], 0, 0, 1)
    [1, 2]
    >>> merge([1, 5, 3], 0, 1, 2)
    [1, 3, 5]
    """
    left = items[p:q+1] + [inf]
    right = items[q+1:r+1] + [inf]

    l_index = 0
    r_index = 0
    for i in range(p, r+1):
        if left[l_index] < right[r_index]:
            items[i] = left[l_index]
            l_index += 1
        else:
            items[i] = right[r_index]
            r_index += 1

    return items


def merge_sort(items):
    """
    Easy access function to merge sort

    >>> merge_sort([1])
    [1]
    """
    if len(items) < 2:
        return items
    return recursive_merge_sort(items, 0, len(items) - 1)

def recursive_merge_sort(items, p, r):
    """
    Recursive merge sort

    >>> recursive_merge_sort([3, 2, 1, 0], 0, 3)
    [0, 1, 2, 3]
    """
    if p >= r:
        return items

    middle = (r + p) // 2
    recursive_merge_sort(items, p, middle)
    recursive_merge_sort(items, middle + 1, r)
    merge(items, p, middle, r)

    return items


if __name__ == "__main__":
    import sys
    print(merge_sort([int(x) for x in sys.argv[1:]]))
