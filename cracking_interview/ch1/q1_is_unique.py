"""
Implement an algorithm to determine if a string has all unique characters
"""

def is_unique(string):
    """
    Using a list with markers.

    >>> is_unique("abcd")
    True
    >>> is_unique("abcda")
    False
    """
    index = [True] * 128
    for char in string:
        index[ord(char)] ^= True
        if index[ord(char)]:
            return False
    return True

def is_unique_2(string):
    """
    Using bits as markers.

    >>> is_unique_2("abcd")
    True
    >>> is_unique_2("abcda")
    False
    """
    bits = 0
    for char in string:
        position = 1 << ord(char)
        bits ^= position
        if bits & position == 0:
            return False
    return True

def is_unique_3(string):
    """
    Using no markers
    >>> is_unique_3("abcd")
    True
    >>> is_unique_3("abcda")
    False
    """
    prev = None
    for char in sorted(string):
        if prev == char:
            return False
        prev = char
    return True