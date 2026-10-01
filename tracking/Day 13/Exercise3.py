risk_score = 0
processed = 0
for id in range(301, 316):
    if id == 313:
        break
    if id % 5 == 0:
        continue
    processed += 1
    if id % 4 == 0:
        risk_score += 3
    elif id % 3 == 0:
        risk_score += 2
    else:
        risk_score -= 1
print(risk_score)
print(processed)