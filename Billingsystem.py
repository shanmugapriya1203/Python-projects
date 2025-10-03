# Simple Billing System (Very Simple Version)

bill_items = []
total = 0

print("=== Welcome to Simple Billing System ===")

while True:
    item = input("Enter item name (or 'done' to finish): ")
    if item.lower() == "done":
        break

    price = float(input(f"Enter price of {item}: "))
    qty = int(input(f"Enter quantity of {item}: "))

    cost = price * qty
    bill_items.append([item, price, qty, cost])
    total += cost

print("\n===== BILL RECEIPT =====")
for b in bill_items:
    print(b[0], "-", b[1], "x", b[2], "=", b[3])

print("===================")
print("Grand Total:", total)
print("Thank you! Visit again.")
