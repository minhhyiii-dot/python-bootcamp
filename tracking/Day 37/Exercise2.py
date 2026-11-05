def withdraw(balance, amount):
    if balance < 0:
        raise ValueError("Invalid balance")
    elif amount <= 0:
        raise ValueError("Amount must be positive")
    elif amount > balance:
        raise ValueError("Insufficient funds")
    new_balance = balance - amount
    return new_balance

print(withdraw(1000, 1500))