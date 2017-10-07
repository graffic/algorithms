def read_numbers(filename):
    with open(filename, 'r') as infile:
        while True:
            line = infile.readline().strip()
            if not line:
                break
            yield int(line)


if __name__ == "__main__":
    print(sum(read_numbers('13.numbers')))

