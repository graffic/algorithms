
#!/bin/python3

import sys

def get_price(meal, tip_percent, tax_percent):
    tip = meal * tip_percent / 100
    tax = meal * tax_percent / 100
    return round(meal + tip + tax)

if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())
    
    price = get_price(meal_cost, tip_percent, tax_percent)
    print("The total meal cost is {0} dollar{1}.".format(price, "s" if price > 1 else ""))

