stock = {"A1": 5, "B2": 3, "C3": 0}

transactions = [
    ("TX1", "A1", "OUT", 2),
    ("TX2", "B2", "IN", 4),
    ("TX3", "A1", "OUT", 4),
    ("TX4", "C3", "IN", 3),
    ("TX2", "B2", "IN", 4),
    ("TX5", "C3", "OUT", 1),
    ("TX6", "B2", "OUT", 6),
    ("TX7", "A1", "IN", 1),
    ("TX8", "Z9", "IN", 5),
    ("TX9", "A1", "OUT", 4)
]

existed_transactions = set()
rejected_transactions = {}
successful_transactions_by_product = set()
successful_IN_transaction = 0
successful_OUT_transaction = 0
for transaction in transactions:
    if transaction[0] in existed_transactions:
        rejected_transactions[transaction] = "ID already existed"
        continue
    if transaction[1] not in stock:
        rejected_transactions[transaction] = "Unknown product ID"
        continue
    if transaction[2] == "IN":
        stock[transaction[1]] += transaction[3]
        successful_IN_transaction += 1
        existed_transactions.add(transaction[0])
        successful_transactions_by_product.add(transaction[0])
    elif transaction[2] == "OUT":
        if stock[transaction[1]] >= transaction[3]:
            stock[transaction[1]] -= transaction[3]
            successful_OUT_transaction += 1
            successful_transactions_by_product.add(transaction[0])
        else:
            rejected_transactions[transaction] = "Not enough product stock"
            continue
        existed_transactions.add(transaction[0])

print(f"Final Inventory:\n{stock}")
print(f"Rejected Transaction:\n{rejected_transactions}")
print(f"Successful Transactions by Product:\n{successful_transactions_by_product}")
print(f"Operation Frequency:\nIN: {successful_IN_transaction}\nOUT:{successful_OUT_transaction}")
    
    

