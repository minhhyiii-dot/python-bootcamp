battery = 23
minutes = 0
while battery > 0:
    if battery == 0:
        break
    minutes += 1
    if battery % 5 == 0:
        battery -= 4
    else:
        battery -= 3
print(minutes)
print(battery)