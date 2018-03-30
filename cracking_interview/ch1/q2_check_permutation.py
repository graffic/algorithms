"""
Given two string, check if one is permutation of the other
"""

def check(one, other):
    """
    Using sorting ((a+b)log(a*b))

    >>> check("abcda", "aadcb")
    True
    >>> check("abc", "bcd")
    False
    >>> check("a", "bc")
    False
    """
    if len(one) == len(other):
        return sorted(one) == sorted(other)
    return False

def count(string, max_char):
    """
    Count occurrences

    >>> count("\x02\x03\x02", 5)
    [0, 0, 2, 1, 0]
    """
    state = [0] * max_char
    for char in string:
        state[ord(char)] += 1
    return state


def check2(one, other):
    """
    Counting occurrences. 3(a+b) + c -> O(N)

    >>> check2("abcda", "aadcb")
    True
    >>> check2("abc", "abd")
    False
    >>> check2("abc", "bc")
    False
    """
    if len(one) != len(other):
        return False
    size = max(ord(x) for x in one + other) + 1

    res_one = count(one, size)
    res_other = count(other, size)

    for i in range(size):
        if res_one[i] != res_other[i]:
            return False
    return True
