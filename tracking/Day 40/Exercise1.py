
def error(prices):
    if not prices:
        raise ValueError("Prices cannot be empty")

def calculate_total(prices, threshold, discount_rate):
    subtotal = sum(prices)

    if subtotal >= threshold:
        subtotal = subtotal * (1 - discount_rate)
    return subtotal

def retail_total(prices):
    error(prices)   

    subtotal = calculate_total(prices, 100, 0.1)

    return round(subtotal, 2)


def wholesale_total(prices):
    error(prices)

    subtotal = calculate_total(prices, 500, 0.2)

    return round(subtotal, 2)

print(retail_total([60, 50]))
print(retail_total([30, 40]))
print(wholesale_total([300, 250]))
print(wholesale_total([200, 100]))
