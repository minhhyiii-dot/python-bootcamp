def final_price(price, discount = 0):
    final_price = price - (price * discount / 100)
    return final_price

print(final_price(100))
print(final_price(100, 20))
print(final_price(discount = 20, price = 100))