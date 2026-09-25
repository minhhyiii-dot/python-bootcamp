#Ask the user for the cart total and convert it to an integer.
#Use an if statement: If cart_total is 1000 or greater, subtract 100 from the current value of cart_total. (Reassign the existing variable; do not create a new one).
#Unindent and print the final value of cart_total.
cart_total = int(input("Your cart total: "))
if cart_total >= 1000:
    cart_total = cart_total - 100
print(cart_total)