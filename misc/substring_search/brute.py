def search(string, substring):
    """
    Brute force substring search

    >>> search("abcdefghi", "cde")
    2
    >>> search("abcdefghi", "potato")
    -1
    >>> search("abcdefghi", "i")
    8
    >>> search("abcdefghi", "abc")
    0
    """
    for s in range(len(string)):
        for ss in range(len(substring)):
            if string[s+ss] != substring[ss]:
                break
        else:
            return s
    return -1