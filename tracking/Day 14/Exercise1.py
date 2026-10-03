score = 0 
processed = 0
for id in range(101,111):
    if id == 105:
        break
    if id % 5 == 0:
        continue
    processed += 1
    print(score)
    print(processed)
    print(id)
    if id % 2 == 0:
        score += 2
    else:
        id -= 1
