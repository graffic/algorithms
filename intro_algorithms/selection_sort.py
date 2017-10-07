"""
Selection sort

Find the smallest item and put it first, exchanging it for the element that
wast first. Repeat for the rest of the array.

Worst case: O(n2)
"""
import sys


def selection_sort(items):
    length = len(items)
    if length < 2:
        return items

    current_index = 0
    while current_index < length:
        smaller = items[current_index]
        smaller_index = current_index

        for i in range(current_index, length):
            if items[i] < smaller:
                smaller = items[i]
                smaller_index = i
        items[smaller_index] = items[current_index]
        items[current_index] = smaller

        current_index += 1
    return items


if __name__ == "__main__":
    print(selection_sort([int(x) for x in sys.argv[1:]]))
