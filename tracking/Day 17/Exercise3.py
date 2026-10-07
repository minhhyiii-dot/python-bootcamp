left = ["VCB", 100, False]
right = ["MBB", 250, True]

old_left = left[0]
left[0] = right[0]
right[0] = old_left
left[1] = left[1] + right[1]
right[1] = left[1] - 50
left[2] = right[1] > 200
right[2] = not left[2]

print(left)
print(right)
print(old_left)
print(left[-1])
print(right[1])
print(type(left[1]))