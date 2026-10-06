market_trend = input("Market Trend: ")
market_trend = market_trend.strip()
market_trend = market_trend.lower()
if market_trend == "bullish":
    print("Buy")
elif market_trend == "bearish":
    print("Sell")
else:
    print("Unknown trend")
    