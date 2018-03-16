from sys import stdin

def build_book():
    entries = int(input())
    book = {}
    while entries > 0:
        #print(input().split(" "))
        key, value = input().split(" ")
        book[key] = value
        entries -= 1
    return book

book = build_book()

for line in stdin:
    key = line.strip()
    if key in book:
        print("{0}={1}".format(key, book[key]))
    else:
        print("Not found")