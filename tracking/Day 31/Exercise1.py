def apply_discount(price, discount_percent):
    discounted_price = price - price * (discount_percent / 100)
    return discounted_price
final_price = apply_discount(200, 15)

print(final_price)