score = 0
processed = 0
for id in range(20,36):
    if id == 33:
        break
    if id % 4 == 0:
        continue
    processed += 1
    if id % 3 == 0:
        score += 3
    else:
        score -= 1
print(score)
print(processed)