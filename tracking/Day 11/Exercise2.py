#The Task: Transaction Auditor
#Write a script that scans transaction IDs.
for id in range(80, 91):
    if id == 88:
        print("Audit triggered at 88")
        break
    elif id % 5 == 0:
        continue
    else:
        print("Valid ID:", id)