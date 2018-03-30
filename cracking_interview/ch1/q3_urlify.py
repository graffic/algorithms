"""
Replace spaces with %20 (in place)
"""

def urlify(source):
    """
    >>> urlify('ab c  ')
    'ab%20c'
    >>> urlify(' b  a      ')
    '%20b%20%20a'
    """
    source = list(source)
    read = write = len(source) - 1

    # Find last letter
    while source[read] == ' ':
        read -= 1
    
    while read >= 0:
        item = source[read]
        if item != ' ':
            source[write] = item
            write -= 1
        else:
            source[write] = '0'
            source[write - 1] = '2'
            source[write - 2] = '%'
            write -= 3
        read -= 1

    return ''.join(source)