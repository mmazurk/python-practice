# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200

def banking(transaction_list):
    """its like banking except not"""
    total_balance = 0

    for item in transaction_list:
        amount = int(item[2::1])
        if item[0] == "D":
            total_balance += amount
        elif item[0] == "W":
            total_balance -= amount
        else:
            return "error code 32"

    return total_balance


transactions = ["D 500", "D 500", "W 200", "W 200", "D 1000"]
balance = banking(transactions)

if isinstance(balance, str):
    print("OH NO! ERROR CODE 32")
else:
    print(f"Your balance sir, is ${balance}")
