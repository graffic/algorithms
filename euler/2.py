from itertools import takewhile


def fibonacci():
    n2 = 0
    n1 = 1
    while True:
        res = n2 + n1
        yield res
        n2 = n1
        n1 = res


if __name__ == "__main__":
    print(sum(
        x for x in takewhile(lambda x: x <= 4000000, fibonacci()) \
        if not x % 2))

