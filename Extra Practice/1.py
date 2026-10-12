class Student:
    def __init__(self, student_id, name, class_name, GPA):
        self.student_id = student_id
        self.name = name
        self.class_name = class_name
        self.GPA = GPA
        self.next = None
        
head = None

Student1 = Student("001", "Minh", "MIS", 2.7)
head = Student1
Student2 = Student("002", "An", "CS", 3.8)
Student1.next = Student2

current = head
count = 0
while current is not None:
    count += 1
    current = current.next
print(count)

current = head
id = input("Enter Student ID: ")
while current is not None:
    if id == current.student_id:
        print(current.student_id)
        print(current.name)
        print(current.class_name)
        print(current.GPA)
        break

    current = current.next
if current is None:
    print("Student not found!")

choice = "y"
while choice == "y":
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    class_name = input("Enter Class: ")
    GPA = float(input("Enter GPA: "))
    new_student = Student(student_id, name, class_name, GPA)
    if head is None:
        head = new_student
    else:
        current = head
        while current.next is not None:
            current = current.next
        current.next = new_student
    choice = input("Continue? (y/n)")

    