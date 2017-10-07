import sys


def insert_sort(items):
    length = len(items)
    if length < 2:
        return items

    for i in range(1, length):
        key = items[i]
        k = i - 1
        while k >=0 and key < items[k]:
            items[k + 1] = items[k]
            k -= 1
        items[k + 1] = key
    return items


if __name__ == "__main__":
    print(insert_sort([int(x) for x in sys.argv[1:]]))
