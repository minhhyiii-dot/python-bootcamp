
thread_score = 0
for id in range(410,439):
    if id == 426:
        break
    elif id % 6 == 0:
        continue
    elif id % 2 == 0 and id > 420:
        thread_score += 5
    elif id % 2 == 0:
        thread_score += 2
    else:
        thread_score -= 1
print(thread_score)