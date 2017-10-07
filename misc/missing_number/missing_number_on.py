def find_missing(items):
    for index, number in enumerate(items):
        if index + 1 != number:
            return index + 1

if __name__ == "__main__":
    import sys

    print(find_missing([int(x) for x in sys.argv[1:]]))
