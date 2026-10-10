numbers = [12, 7, 18, 5, 20, 9]
count = 0
sum = 0
for nums in numbers:
    if nums % 2 == 0:
        count += 1
        sum += nums 
print(count)
print(sum)
