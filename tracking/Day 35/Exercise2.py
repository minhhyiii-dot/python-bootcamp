def shipping_total(price, quantity = 1, shipping_fee = 10):
    total = price * quantity + shipping_fee
    return total

print(shipping_total(100))
print(shipping_total(100, 2))
print(shipping_total(shipping_fee = 3, quantity = 2, price = 100))
print(shipping_total(100,shipping_fee = 3))