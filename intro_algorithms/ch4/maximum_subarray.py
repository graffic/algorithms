"""
Find the maximum subarray
"""
from math import inf


def sub_max(items):
    """
    find the maximum sum sequentially for an iterable

    >>> sub_max([1, 2, 3])
    (6, 2)
    >>> sub_max([1, 2, -5])
    (3, 1)
    """
    maximum = -inf
    current_sum = 0
    maximum_index = None
    for index, value in enumerate(items):
        current_sum += value
        if current_sum > maximum:
            maximum = current_sum
            maximum_index = index

    return maximum, maximum_index


def find_maximum_cross(left, right, mid):
    """
    find the maximum sum in a subarray that crosses the middle

    >>> find_maximum_cross([1], [2], 1)
    (3, 0, 1)
    >>> find_maximum_cross([-1, 2, 5], [6, -7], 3)
    (13, 1, 3)
    >>> find_maximum_cross([-1, 2], [5, 6, -7], 2)
    (13, 1, 3)
    """
    left_sum, left_index = sub_max(left[::-1])
    right_sum, right_index = sub_max(right)
    left_index = mid - 1 - left_index
    right_index = mid + right_index

    return (left_sum + right_sum, left_index, right_index)


def find_maximum_subarray(items):
    """
    >>> find_maximum_subarray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7])
    (43, 7, 10)
    """
    mid = len(items) // 2
    if mid == 0:
        return items[0], 0, 0

    left = items[:mid]
    right = items[mid:]

    max_left, left_start, left_end = find_maximum_subarray(left)
    max_right, right_start, right_end =find_maximum_subarray(right)
    max_cross, cross_start, cross_end = find_maximum_cross(left, right, mid)

    if max_left >= max_right and max_left >= max_cross:
        return max_left, left_start, left_end
    elif max_right >= max_left and max_right >= max_cross:
        return max_right, right_start, right_end

    return max_cross, cross_start, cross_end


if __name__ == "__main__":
    import sys

    print(find_maximum_subarray([int(x) for x in sys.argv[1:]]))
