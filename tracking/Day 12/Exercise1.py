score = 0
for num in range(1,21):
    if num > 15:
        break
    elif num % 3 == 0:
        continue
    elif num % 2 == 0:
        score += num
    else:
        score -= 1
print(score)