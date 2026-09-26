#Write a Python script from a blank editor that does the following:
#Takes a customer's bank balance as a float input.
#Uses an if/elif/else chain to determine their account_tier based on these rules:
#1,000,000,000 or more → "VIP"
#500,000,000 or more → "Premium"
#100,000,000 or more → "Standard"
#Anything strictly below 100,000,000 → "Basic"
#Prints the assigned tier at the very end.

bank_balance = float(input("Bank Balance: "))
if bank_balance >= 1000000000:
    account_tier = "VIP"
elif bank_balance >= 500000000:
    account_tier = "Premium"
elif bank_balance >= 100000000: 
    account_tier = "Standard"
else:
    account_tier = "Basic"
print(account_tier)
