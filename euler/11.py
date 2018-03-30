from os.path import dirname, join

def load_grid(filename):
    grid = []
    with open(filename, 'r') as infile:
        while True:
            line = infile.readline().strip()
            if not line:
                break
            grid.append([int(x) for x in line.split(' ')])
    return grid

def take_items(grid, x, y, incx, incy, num):
    items = 0
    res = []
    while items < num:
        res.append(grid[y][x])
        y += incy
        x += incx
        items += 1
    return res

def split_tuples(num, grid):
    directions = [(1, 0), (1, 1), (0, 1), (-1, 1)]
    max_x = len(grid[0])
    max_y = len(grid)
    x = y = 0
    while y < max_y:
        res = []
        for inc_x, inc_y in directions:
            # Can do it?
            dest_x = x + inc_x * num
            dest_y = y + inc_y * num
            if dest_x > max_x or dest_x < 0:
                continue
            if dest_y > max_y or dest_y < 0:
                continue
            # Do it and yield
            yield take_items(grid, x, y, inc_x, inc_y, num)
        x += 1
        if x == max_x:
            x = 0
            y += 1


def problem():
    """
    >>> problem()
    70600674
    """
    grid = load_grid(join(dirname(__file__), '11.grid'))
    biggest = 0
    for pack in split_tuples(4, grid):
        res = 1
        for number in pack:
            res *= number
        if res > biggest:
            biggest = res
    print(biggest)
