from itertools import combinations_with_replacement


def is_pal(number):
    number = str(number)
    half = len(number) // 2
    return number.endswith(number[:half][::-1])


if __name__ == "__main__":
    items = tuple(range(999, 100, -1))
    res = 0
    prev = (0, 0)
    for a, b in combinations_with_replacement(items, 2):
        if a < prev[0] and b < prev[1]:
            continue
        mult = a * b
        if is_pal(mult) and mult > res:
            res = mult
            prev = (a, b)
    print(res)
