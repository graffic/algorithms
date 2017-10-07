def filter_multiples(numbers):
    for number in numbers:
        if number % 3 == 0:
            yield number
        elif number % 5 == 0:
            yield number

if __name__ == "__main__":
    print(sum(filter_multiples(range(1000))))
