def place_order(stock, history, item, quantity):
    if item not in stock:
        return False
    if quantity > stock[item]:
        return False

    stock[item] -= quantity
    history.append({"item": item, "quantity": quantity})
    return True

stock = {"pen": 5, "notebook": 2}
history = []

place_order(stock, history, "calculator", 1)

print(stock)
print(history)