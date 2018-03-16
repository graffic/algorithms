def test_cases():
    amount = int(input())
    while amount > 0:
        yield input()
        amount -= 1

for test in test_cases():
    print(test[::2] + " " + test[1::2])