score = 0

for n in range(1, 5):
    if n % 2 == 0:
        score += n
    else:
        score -= 1
    print("n =",n, "score =",score)
