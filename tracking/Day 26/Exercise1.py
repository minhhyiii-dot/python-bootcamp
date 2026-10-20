products = [
    {"name": "Laptop", "prices": [900, 950]},
    {"name": "Mouse", "prices": [20, 25, 30]}
]

for product in products:
    for price in product["prices"]:
        print(price)