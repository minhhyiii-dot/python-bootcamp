values = [4, -2, 7, 0, -5, 3, 8]
new_values = []
total = 0
for i in values:
    if i % 2 != 0 and i > 0:
        new_values.append(i**2)
        total += i**2
print(new_values)
print(total)