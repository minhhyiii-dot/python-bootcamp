#Final Challenge — Fraud Detection Queue
risk_score = 0
reviewed = 0
for id in range(700,735):
    if id == 729:
        break
    if id % 10 == 0:
        continue
    reviewed += 1
    if id % 2 == 0 and id > 720:
        risk_score += 5
    elif id % 2 == 0:
        risk_score += 2
    elif id % 7 == 0:
        risk_score += 3
    else:
        risk_score -= 1
print(risk_score)
print(reviewed)