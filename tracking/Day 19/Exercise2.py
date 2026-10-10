numbers = [14, 21, 8, 35, 18, 42, 11, 27]
new_numbers = []
for nums in numbers:
    if nums >= 20 and nums % 3 == 0:
        new_numbers.append(nums)
print(new_numbers)