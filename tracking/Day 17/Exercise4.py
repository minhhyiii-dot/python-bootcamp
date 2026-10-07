position = ["VCB", 100, 120.0, False]

new_price = float(input("New Price: "))
action = input("Action: ")
if action == "buy" or action == "sell":
    quantity = int(input("Quantity: "))
if action == "hold":
    position[1] = position[1]
elif action == "sell":
    if position[1] >= quantity:
        position[1] = position[1] - quantity
    else:
        print("You dont have enough shares")
elif action == "buy":
    position[1] = position[1] + quantity
else:
    print("Unknown Action")

if new_price > position[2]:
    statuses = "PROFIT"
elif new_price == position[2]:
    statuses = "BREAK-EVEN"
else:
    statuses = "LOSS"

position[3] = new_price > position[2]
position[2] = new_price

print(position)
print(statuses) 