"""
Knuth-Morris-Pratt with a DFSM
"""


def debug_dfsm(dfsm):
    for char in sorted(dfsm.keys()):
        print(f"'{char}': {dfsm[char]}")

def build_dfsm(pattern):
    """
    Build a dfsm to match the pattern.
    - State 0 is the beginning when no char has been matched
    - State len(pattern) is a match

    As you match the chars in the pattern, you move from one state to the 
    next. Mismatches are as if we had to backup and match from the next
    character: BABAC[miss] -> ABAC[???]

    We build the table and simulate a mismatch at the same time so this
    part is O(len(pattern))

    >>> dfsm = build_dfsm("potato")
    >>> debug_dfsm(dfsm)
    'a': [0, 0, 0, 4, 0, 0]
    'o': [0, 2, 0, 0, 0, 6]
    'p': [1, 1, 1, 1, 1, 1]
    't': [0, 0, 3, 0, 5, 0]
    """
    unique_chars = set(pattern)
    dfsm = dict((x,[None]*len(pattern)) for x in unique_chars)
    
    # First loop
    # All zeros except for the first character that goes to state 1
    for c in unique_chars:
        dfsm[c][0] = 0
    dfsm[pattern[0]][0] = 1

    x = 0  # Keeps the current state in the simulation after a backup
    j = 1
    while j < len(pattern):
        current_char = pattern[j]
        # Simulate a backup part I
        # On a mismatch we use the states as we had backup one char. In the 
        # beggining this means for j=1 and x=0
        # But while j increments, x follows the simulation of a backup
        for c in unique_chars:
            dfsm[c][j] = dfsm[c][x]
        # Fix the previous copy by setting the right char to the next state
        dfsm[current_char][j] = j + 1

        # Simulate a backup part II
        # Set the next state in our simulation
        x = dfsm[current_char][x]
        j += 1
    return dfsm


def search(string, pattern):
    """
    >>> search("abcdefghi", "cde")
    2
    >>> search("abcdefghi", "potato")
    -1
    """
    dfsm = build_dfsm(pattern)

    state = 0
    for index, c in enumerate(string):
        if c in dfsm:
            state = dfsm[c][state]
        else:
            state = 0
        if state == len(pattern):
            return index - len(pattern) + 1
    return -1


if __name__ == "__main__":
    import doctest
    doctest.testmod()