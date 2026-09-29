#Viết chương trình:
#Có một list:
#numbers = [12, 5, 8, 21, 3, 17]
#In ra số lớn nhất trong list.
#Không dùng max().
number =  [12, 5, 8, 21, 3, 17]
max_num = 0
for num in number:
    if max_num <= num:
        max_num = num
    elif max_num > num:
        continue
print(max_num)