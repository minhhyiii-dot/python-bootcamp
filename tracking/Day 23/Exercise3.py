portfolio = {
    "AAPL": 180,
    "MSFT": 420,
    "GOOG": 175,
    "TSLA": 250
}

remove_price = portfolio.pop("TSLA")
portfolio["AAPL"] = 195
portfolio["NVDA"] = 140

print(remove_price)
print("TSLA" in portfolio)
for key, value in portfolio.items():
    print(key, value)
print(len(portfolio))