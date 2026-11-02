students = [
    {"name": "Alice", "scores": [80, 90, 85]},
    {"name": "Charlie", "scores": [95, 90, 100]},
    {"name": "Bob", "scores": [60, 70, 65]}
]
# AVG score
def avg_score(students):
    for student in students:
        total = 0
        count = 0
        for score in student["scores"]:
            total += score
            count += 1
            avg = total / count
            student["average"] = avg

    return students

# Grade assign
def grade_assign(students):
    for student in students:
        if student["average"] >= 90:
            student["assigned"] = "A"
        elif student["average"] >= 80:
            student["assigned"] = "B"
        elif student["average"] >= 70:
            student["assigned"] = "C"
        else:
            student["assigned"] = "D"

    return students


# Top student
def top_student(students):
    top_score = 0
    top_stu = {}
    name = 0
    for student in students:
        if student["average"] < top_score:
            continue
        elif student["average"] > top_score:
            name = student["name"]
            top_score = student["average"]
    top_stu[name] = top_score
    return top_stu

# Report
print(grade_assign(avg_score(students)))
print("Top Student:", top_student(avg_score(students)))