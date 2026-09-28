history = "W-W-L-W-L-L-W"
score = 0
for char in history:
    if char == "W":
        score += 3
    elif char == "L":
        score -= 1
    else:
        score = score
print("Final Score = ", score)