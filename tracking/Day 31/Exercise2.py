def process_withdrawal(balance, amount):
    if amount <= 0:
        return("INVALID AMOUNT")
    elif balance < amount + 5:
        return("INSUFFICIENT FUNDS")
    new_balance = balance - amount - 5
    return new_balance

print(process_withdrawal(200, 50))
print(process_withdrawal(100, 100))
print(process_withdrawal(500, -20))
print(process_withdrawal(50, 45))
print(process_withdrawal(100, 96))
