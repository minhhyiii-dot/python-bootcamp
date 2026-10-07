portfolio = ["VCB", 120, False, 2025, 88.5]
old_value = portfolio[1]
portfolio[0] = "MBB"
portfolio[1] = 150
portfolio[2] = portfolio[1] > 100
portfolio[3] = portfolio[3] + 1
portfolio[4] = portfolio[4] + 1.5

print(portfolio)
print(old_value)
print(portfolio[0])
print(portfolio[-1])
print(len(portfolio))
print(type(portfolio[3]))