students = [
    {"name": "Alice", "scores": [85, 90, 95]},
    {"name": "Bob", "scores": [70, 85, 75]},
    {"name": "Charlie", "scores": [92, 88, 96]}
]

for student in students:
    for score in student["scores"]:
        print(student["name"] + ":", score)
  