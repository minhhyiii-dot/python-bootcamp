credits = 26
rounds = 0
while credits >= 5:
    rounds += 1
    if credits % 4 == 0:
        credits -= 7
    else:
        credits -= 5
print(rounds)
print(credits)