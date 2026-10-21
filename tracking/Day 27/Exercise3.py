orders = ["A12", "B05", "A12", "C30", "B05", "A12", "D10"]
count = {}

for order in orders:
    count[order] = count.get(order, 0) + 1

print(count)
id = input("Enter product ID: ")

count[id] = count.get(id, 0)
print(count[id])
