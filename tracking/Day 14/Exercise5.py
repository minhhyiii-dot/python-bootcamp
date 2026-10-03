signal = "A-BB-XA-BX"
score = 0
processed = 0
for char in signal:
    if char == "X":
        break
    if char == "-":
        continue
    processed += 1
    if char == "A":
        score += 3
    if char == "B":
        score -= 1
print(score)
print(processed)