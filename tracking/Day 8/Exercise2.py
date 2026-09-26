#Mandatory Blank-Screen Task: Trading Bot Logic
#You need to build the decision logic for a basic trading bot. The bot prioritizes emergency limits (profit taking / stop losses) over general market trends.
#Requirements:
#Take two user inputs:
#daily_return (as a float, e.g., 12.5 or -9.0)
#market_trend (as a str, e.g., "Bullish", "Bearish", or "Neutral")
#Use a single if/elif/else chain to determine the bot's action based on these rules, in this exact priority order:
#If the return is 10.0 or higher, action is "Take Profit".
#If the return is -8.0 or lower, action is "Stop Loss".
#If neither limit is hit but the trend is "Bullish", action is "Hold".
#If neither limit is hit but the trend is "Bearish", action is "Reduce Position".
#For all other situations, action is "Wait".
#Print the assigned action at the very end using exactly one print() statement.

daily_return = float(input("Daily Return: "))
market_trend = input("Market Trend: ")
if daily_return >= 10:
    action = "Take Profit"
elif daily_return <= -8:
    action = "Stop Loss"
elif market_trend == "Bullish":
    action = "Hold"
elif market_trend == "Bearish":
    action = "Reduce Posistion"
else:
    action = "Wait"
print(action)  