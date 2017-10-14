"""
Check if a string is a permutation of a palindome
"""
def is_pp(string):
    """
    >>> is_pp("Tact Coa")
    True
    >>> is_pp("Tact Coaa")
    False
    """
    odd = dict()
    no_spaces = (x.lower() for x in string if x != " ")
    for char in no_spaces:
        odd[char] = not odd.get(char, False)
    count = 0
    for item in odd.values():
        count = count + (1 if item else 0)
    return count <= 1

def is_pp2(string):
    """
    Using bits and only for a-zA-Z
    >>> is_pp2("Tact Coa")
    True
    >>> is_pp2("Tact Coaa")
    False
    """
    odd = 0
    no_spaces = [ord(x.lower()) - 97 for x in string if x != " "]
    for item in no_spaces:
        odd ^= 1 << item
    return bin(odd).count("1") < 2

if __name__ == "__main__":
    import doctest
    doctest.testmod()
