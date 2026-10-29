balance = 1000

def preview_withdrawal(amount):
    new_balance = balance - amount
    return new_balance

new_balance = preview_withdrawal(300)
print(new_balance)
print(balance)