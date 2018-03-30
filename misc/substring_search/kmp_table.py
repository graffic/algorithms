"""
Knuth-Morris-Pratt without dfa

When using a DFA/DFSM  we take into account the character that we just mismatched, so we know the specific next state.

In this version, we only care about a mismatch and not the character of the mismatch itself. If there is a mismatch on the i th We know that at least we matched [0..i-1] characters. The useful information here is if there is another partial match (smaller) in that sequence so we can continue matching, or perhaps there is no partial match and we can continue from 0, but in both cases without backing up


Examples:
Pattern: abcabd
If after we match ... how much can we reuse:
"" -> 0
a -> 0
ab -> 0
abc -> 0
abca -> 1 I can restart matching at pattern[1] (match the mismatched character again)
abcab -> 2 I can restart matching at pattern[2]

How to build this table:

"""


def build_table(pattern):
    """
    >>> build_table("abcabdabcaf")
    [0, 0, 0, 1, 2, 0, 1, 2, 3, 4, 0]
    """
    table = [0] * len(pattern)
    i = 1
    j = 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
        else:
            j = 0
        i+=1
    return table

def search(string, pattern):
    """
    >>> search("abcdefghi", "cde")
    2
    >>> search("abcdefghi", "potato")
    -1
    >>> search("abcdefghi", "i")
    8
    >>> search("abcdefghi", "abc")
    0
    """
    table = build_table(pattern)
    s = 0
    p = 0
    while s < len(string):
        if string[s] == pattern[p]:
            p += 1
            s += 1
            if p == len(pattern):
                return s - p
        elif p > 0:
            p = table[p-1]
        else:
            s += 1
    return -1
