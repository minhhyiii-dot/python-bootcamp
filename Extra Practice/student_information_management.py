class Student:
    def __init__(self, student_id, name, class_name, GPA):
        self.student_id = student_id
        self.name = name
        self.class_name = class_name
        self.GPA = GPA
        self.next = None

head = None
while True:
    print("\n---STUDENT MANAGEMENT---")
    print("1. Insert Student")
    print("2. Count Student")
    print("3. Find Student")
    print("4. Delete Student")
    print("5. Exit")

    menu_choice = int(input("Your Choice: "))

    if menu_choice == 5:
        print("Exiting program...")
        break

    elif menu_choice == 1:
        current = head
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

    elif menu_choice == 2:
        current = head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        print(count)

    elif menu_choice == 3:
        current = head
        find_id = input("Enter Student ID: ")
        while current is not None:
            if find_id == current.student_id:
                print(current.student_id)
                print(current.name)
                print(current.class_name)
                print(current.GPA)
                break
            current = current.next
        if current is None:
            print("ID Not Existed")

    elif menu_choice == 4:
        del_id = input("Enter Student ID: ")

        current = head
        previous = None

        while current is not None:
            if current.student_id == del_id:
                if previous is None:
                    head = current.next
                else:
                    previous.next = current.next

                print("Deleted")
                break
            previous = current
            current = current.next

        if current is None:
            print("ID not Existed")
            
                
                


