def search(string, substring):
    """
    Brute force substring search

    >>> search("abcdefghi", "cde")
    2
    >>> search("abcdefghi", "potato")
    -1
    """
    for s in range(len(string)):
        for ss in range(len(substring)):
            if string[s+ss] != substring[ss]:
                break
        else:
            return s
    return -1

if __name__ == "__main__":
    import doctest
    doctest.testmod()