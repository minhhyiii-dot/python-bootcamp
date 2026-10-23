entries = [
    {"Gate": "North", "Badge": "T21", "Type": "Guest"},
    {"Gate": "South", "Badge": "T22", "Type": "Staff"},
    {"Gate": "North", "Badge": "T23", "Type": "Guest"},
    {"Gate": "East", "Badge": "T21", "Type": "Guest"},
    {"Gate": "South", "Badge": "T24", "Type": "Guest"},
    {"Gate": "North", "Badge": "T22", "Type": "Staff"},
    {"Gate": "East", "Badge": "T25", "Type": "Staff"},
    {"Gate": "East", "Badge": "T26", "Type": "Guest"},
    {"Gate": "South", "Badge": "T24", "Type": "Guest"},
    {"Gate": "North", "Badge": "T27", "Type": "Guest"}
]

while True:
    print("\n---Museum Entry Audit Program---")
    print("1. Gate Activity")
    print("2. Duplicate Detection")
    print("3. Grouped Information")
    print("4. Visitor Type Frequency")
    print("5. Exit")

    menu_choice = int(input("Enter your choice: "))

    if menu_choice == 5:
        print("Exiting Program...")
        break

    elif menu_choice == 1:
        count = {}  
        for entry in entries:
            count[entry["Gate"]] = count.get(entry["Gate"], 0) + 1
        print(count)

    elif menu_choice == 2:
        count = {}
        duplicate = {}
        for entry in entries:
            count[entry["Badge"]] = count.get(entry["Badge"], 0) + 1
            if count[entry["Badge"]] > 1:
                duplicate[entry["Badge"]] = count[entry["Badge"]]
            print(duplicate)

    elif menu_choice == 3:
        group = {}
        for entry in entries:
            if entry["Gate"] in group:
                group[entry["Gate"]].add(entry["Badge"])
            else:
                group[entry["Gate"]] = set()
                group[entry["Gate"]].add(entry["Badge"])   
        print(group)

    elif menu_choice == 4:
        count = {}
        for entry in entries:
            count[entry["Type"]] = count.get(entry["Type"], 0) + 1
        print(count)

    else:
        print("Unknown choice")