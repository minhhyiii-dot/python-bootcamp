def safe_divide(a, b):
    try:
        divided = a / b
        return divided
    except ZeroDivisionError:
        return("Cannot divide by zero")
        

print(safe_divide(10, 2))  
print(safe_divide(10, 0))  
print(safe_divide(9, 3))   

