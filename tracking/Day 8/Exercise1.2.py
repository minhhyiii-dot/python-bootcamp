bank_balance = float(input("Bank Balance: "))
if bank_balance >= 1000000000:
    print("VIP")
elif bank_balance >= 500000000:
    print("Premium")
elif bank_balance >= 100000000: 
    print("Standard")
else:
    print("Basic")
