def calculate_bonus(salary, rate):
    return salary * rate

def process_employee(employee):
    salary = employee["salary"]
    rate = employee["bonus_rate"]
    return calculate_bonus(salary, rate)

employee = {"salary": 5000}
print(process_employee(employee))