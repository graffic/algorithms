from os.path import dirname, join

def read_numbers(filename):
    with open(filename, 'r') as infile:
        while True:
            line = infile.readline().strip()
            if not line:
                break
            yield int(line)


def problem():
    """
    >>> problem()
    5537376230390876637302048746832985971773659831892672
    """
    print(sum(read_numbers(join(dirname(__file__), '13.numbers'))))

