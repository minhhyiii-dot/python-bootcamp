
def calculate_total(prices, discount):
    if not prices:
        raise ValueError("Prices cannot be empty")

    if discount < 0 or discount > 100:
        raise ValueError("Invalid discount")

    total = 0

    for price in prices:
        total += price

    return total * (1 - discount / 100)

print(calculate_total([100, 50], 10))
print(calculate_total([80], 25))
print(calculate_total([10, 20, 30], 0))