authorized_employee_IDs = {"E01", "E02", "E03", "E04"}
entry_scan_history = ["E01", "E03", "X99", "E01", "E04", "X99", "E02"]
IDs_already_appear = set()
distinct_authorized_employees = 0
successful_scans = 0

for id in entry_scan_history:
    if id not in authorized_employee_IDs:
        print("ACCESS DENIED:", id)
        continue
    successful_scans += 1
    if id in IDs_already_appear:
        print("ACCESS GRANTED:", id)
    else:
        distinct_authorized_employees += 1
        print("ACCESS GRANTED:", id)
        IDs_already_appear.add(id)

print("Successful scans:", successful_scans)
print("Unique_employee:", distinct_authorized_employees)