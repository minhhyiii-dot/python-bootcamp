stock_price = 100
while stock_price < 125:
    print(stock_price)
    if stock_price < 110:
        stock_price += 10
    else:
        stock_price += 5
print("Target reached!")