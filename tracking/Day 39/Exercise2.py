
def count_increases(prices):
    if len(prices) < 2:
        return 0

    count = 0
    previous = prices[0]

    for price in prices[1:]:
        if price > previous:
            count += 1
        previous = price

    return count

print(count_increases([100, 120, 110, 115]))
print(count_increases([10, 20, 30]))
print(count_increases([30, 20, 10]))
print(count_increases([100]))