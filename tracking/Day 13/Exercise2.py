risk_score = 0
processed = 0

for transaction_id in range(1001, 1011):
    if transaction_id == 1008:
            break

    if transaction_id % 5 == 0:
        continue

    processed += 1

    if transaction_id % 2 == 0:
        risk_score += 2
    else:
        risk_score -= 1
    
print(risk_score)
print(processed)