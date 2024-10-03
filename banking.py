# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200

# REFACTORED

def banking(transaction_list: list[str]) -> int:
    """its like banking except not"""
    total_balance = 0

    for item in transaction_list:
        transaction = item.split(" ")
        if len(transaction) != 2:
            return "Invalid transaction format"

        action, amount = transaction[0], int(transaction[1])
        if action == "D":
            total_balance += amount
        elif action == "W":
            total_balance -= amount
        else:
            return "Ohhhh noooooo"

    return total_balance


transactions = ["D 500", "D 500", "W 200", "W 200", "D 1000"]
balance = banking(transactions)
print(balance)
