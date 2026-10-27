def calculate_trade_result(buy_price, sell_price, quantity):
    total_profit = (sell_price - buy_price) * quantity
    print(total_profit)

calculate_trade_result(100, 130, 5)
calculate_trade_result(200, 180, 3)
calculate_trade_result(150, 150, 10)