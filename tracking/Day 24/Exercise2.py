portfolio_a = {"AAPL", "MSFT", "NVDA", "TSLA"}
portfolio_b = {"NVDA", "TSLA", "AMZN", "GOOG"}

shared_stocks = portfolio_a & portfolio_b
all_stocks = portfolio_a \ portfolio_b
only_a = portfolio_a - portfolio_b

print(shared_stocks)
print(all_stocks)
print(only_a)