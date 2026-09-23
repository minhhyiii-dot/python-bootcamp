#Create these variables:

#price = 75
#quantity = 4
#discount = 30

#Then create exactly these five new variables using operators and expressions:

#subtotal
#final_price
#average_price
#remainder
#label

#Requirements:

#subtotal = price × quantity
#final_price = subtotal − discount
#average_price = final_price ÷ quantity using normal /
#remainder = final_price modulo quantity
#label must produce exactly:
#SALESALESALE

#using:

#"SALE"

#and an operator.

#Then print exactly these five variables, in this exact order:

#subtotal
#final_price
#average_price
#remainder
#label


price = 75
quantity = 4
discount = 30
subtotal = price * quantity
final_price = subtotal - discount
average_price = final_price / quantity
remainder = final_price % quantity
label = "SALE" * 3

print(subtotal)
print(final_price)
print(average_price)
print(remainder)
print(label)