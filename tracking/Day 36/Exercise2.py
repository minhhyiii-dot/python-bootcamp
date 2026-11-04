def calculate_ratio(a, b):
    try:
        number1 = int(a)
        number2 = int(b)
        divide = number1 / number2
        return divide
    except ValueError:
        return("Invalid number")
    except ZeroDivisionError:
        return("Cannot divide by zero")

print(calculate_ratio("10", "2"))
print(calculate_ratio("abc", "2"))
print(calculate_ratio("10", "0"))
print(calculate_ratio("9", "3"))
