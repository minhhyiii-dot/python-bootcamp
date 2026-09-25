#You are writing a basic ATM withdrawal script.
#Ask the user for their starting balance (float) and a withdrawal amount (float).
#If the withdrawal is greater than the balance, print "Denied" and subtract a 30.0 penalty fee from the balance.
#If the withdrawal is less than or equal to the balance, subtract the withdrawal amount from the balance and print "Approved".
#Always print the final balance at the very end of the program.
#Constraints:
#Use only if. Do not use else or elif.
starting_balance = float(input("Starting Balance: "))
withdrawal_amount = float(input("Withdrawal amount: "))
if starting_balance < withdrawal_amount:
    print("Denied")
    starting_balance = starting_balance - 30
if starting_balance >= withdrawal_amount:
    starting_balance = starting_balance - withdrawal_amount
    print("Approved")
print(starting_balance)