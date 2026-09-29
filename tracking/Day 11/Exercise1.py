for id in range(500, 516):
    if id == 511:
        print("Breach detected at 511")
        break
    elif id % 3 == 0:
        continue
    else:
        print("Scanned ID:", id)