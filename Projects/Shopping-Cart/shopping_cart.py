import os
import csv
import random

print("-----------=4% Discount on Shopping of Rs.10000=-----------")

name = input("Enter Your Good Name: ")
print("-----------=Welcome to Our Shop=-----------", name)

# ================= ITEMS =================
items = {
    "flour": {
        "white": {
            "maida": {"small": 140, "medium": 280, "large": 550},
            "fine_aata": {"small": 130, "medium": 260, "large": 520}
        },
        "chaki": {
            "aata": {"small": 120, "medium": 240, "large": 480},
            "multigrain": {"small": 160, "medium": 310, "large": 600}
        },
        "gram": {
            "besan": {"small": 150, "medium": 300, "large": 580},
            "sugar free besan": {"small": 170, "medium": 330, "large": 620}
        }
    },
    "milk": {
        "fresh": {
            "cow": {"small": 60, "medium": 110, "large": 160},
            "buffalo": {"small": 70, "medium": 130, "large": 180}
        },
        "powder": {
            "olpers": {"small": 80, "medium": 150, "large": 250},
            "nestle nido": {"small": 100, "medium": 180, "large": 300}
        }
    },
    "bread": {
        "white": {
            "dawn": {"small": 40, "medium": 70, "large": 100},
            "british": {"small": 45, "medium": 75, "large": 105}
        },
        "brown": {
            "dawn brown": {"small": 50, "medium": 80, "large": 120},
            "british brown": {"small": 52, "medium": 85, "large": 125}
        }
    },
    "rice": {
        "basmati": {
            "super karachi": {"small": 120, "medium": 230, "large": 350},
            "trophy": {"small": 140, "medium": 250, "large": 380}
        },
        "sela": {
            "guard sela": {"small": 130, "medium": 220, "large": 360},
            "shahenshah": {"small": 135, "medium": 230, "large": 370}
        }
    },
    "oil": {
        "cooking_oil": {
            "dalda": {"small": 380, "medium": 820, "large": 1490},
            "habib": {"small": 370, "medium": 780, "large": 1420}
        },
        "ghee": {
            "dalda ghee": {"small": 380, "medium": 750, "large": 1350},
            "eva ghee": {"small": 350, "medium": 700, "large": 1300}
        }
    }
}

DEFAULT_STOCK = 50
STOCK_FILE = "stock.csv"
BILL_FILE = "bills.csv"

# ================= STOCK FUNCTIONS =================
def load_stock(filename=STOCK_FILE):
    stock = {}
    if os.path.exists(filename):
        with open(filename, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                key = (row['item'], row['sub'], row['child'], row['size'])
                stock[key] = int(row['stock'])
    return stock

def update_stock(stock, filename=STOCK_FILE):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["item", "sub", "child", "size", "stock"])
        for key, qty in stock.items():
            writer.writerow([*key, qty])

# ================= BILL ID =================
def generate_bill_id():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    bill_id = ""
    for _ in range(3):
        bill_id += random.choice(letters)
    for _ in range(3):
        bill_id += random.choice(numbers)
    return bill_id

# ================= CART FUNCTIONS =================
stock_data = load_stock()

def show_items(items):
    print("\nAvailable Main Items:")
    for item in items:
        print(" -", item.title())

def add_to_cart(items, cart):
    while True:
        a = input("\nEnter item name (or 'done' to finish): ").lower()
        if a == "done":
            break
        if a not in items:
            print(" Item not found!")
            continue

        print("\nSub Categories:")
        for sub in items[a]:
            print(" -", sub.title())
        sub = input("Enter sub-category: ").lower()
        if sub not in items[a]:
            print(" Invalid sub-category!")
            continue

        print("\nCompanies:")
        for child in items[a][sub]:
            print(" -", child.title())
        child = input("Enter company: ").lower()
        if child not in items[a][sub]:
            print(" Invalid company!")
            continue

        print("\nSizes:")
        for sz, pr in items[a][sub][child].items():
            print(f" {sz} : Rs.{pr}")
        size = input("Enter size: ").lower()
        if size not in items[a][sub][child]:
            print(" Invalid size!")
            continue

        key = (a, sub, child, size)
        if key not in stock_data:
            stock_data[key] = DEFAULT_STOCK

        available = stock_data[key]
        if available <= 0:
            print(" Out of Stock!")
            continue

        try:
            qty = int(input(f"Enter quantity (Available {available}): "))
        except:
            print(" Quantity must be a number!")
            continue

        if qty > available:
            print(" Not enough stock!")
            continue

        stock_data[key] -= qty
        price = items[a][sub][child][size] * qty

        cart.append({
            "item": a,
            "sub": sub,
            "child": child,
            "size": size,
            "quantity": qty,
            "price": price
        })

        print(f" Added {qty} x {size} {child.title()} = Rs.{price}")

# ================= SAVE BILL =================
def save_bill(bill_id, name, cart, total, discount, tax, grand_total, filename=BILL_FILE):
    file_exists = os.path.exists(filename)
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Bill ID", "Customer", "Item", "Sub-category", "Company", "Size", "Quantity", "Price", "Total", "Discount", "Tax", "Grand Total"])
        for item in cart:
            writer.writerow([
                bill_id,
                name,
                item["item"],
                item["sub"],
                item["child"],
                item["size"],
                item["quantity"],
                item["price"],
                total,
                discount,
                tax,
                grand_total
            ])

# ================= SEARCH BILL =================
def search_bill(bill_id, filename=BILL_FILE):
    if not os.path.exists(filename):
        print("No bills found.")
        return

    found = False
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        print(f"\n=========== BILL DETAILS FOR ID {bill_id} ===========")
        for row in reader:
            if row['Bill ID'] == bill_id:
                print(f"{row['Quantity']} x {row['Size']} {row['Company'].title()} ({row['Item'].title()}) = Rs.{row['Price']}")
                found = True
                total = row['Total']
                discount = row['Discount']
                tax = row['Tax']
                grand_total = row['Grand Total']
        if found:
            print(f"Total = Rs.{total}")
            print(f"Discount = Rs.{discount}")
            print(f"Tax = Rs.{tax}")
            print(f"Grand Total = Rs.{grand_total}")
        else:
            print("Bill ID not found!")

# ================= MAIN =================
cart = []
show_items(items)
add_to_cart(items, cart)

bill_id = generate_bill_id()
total = sum(item['price'] for item in cart)
discount = total * 0.04 if total >= 10000 else 0
final_total = total - discount
tax = final_total * 0.06 if final_total > 200 else 0
grand_total = final_total + tax

# Print bill
print("\n=========== BILL RECEIPT ===========")
print(f"Bill ID : {bill_id}")
print(f"Customer: {name}")
print("----------------------------------")
for i in cart:
    print(f"{i['quantity']} x {i['size']} {i['child'].title()} ({i['item'].title()}) = Rs.{i['price']}")
print("----------------------------------")
print(f"Total = Rs.{total}")
print(f"Discount = Rs.{discount}")
print(f"Sub Total = Rs.{final_total}")
print(f"Tax = Rs.{tax}")
print("----------------------------")
print(f"Total Bill = Rs.{grand_total}")
print("Thank You", name, "For Your Shopping!")


save_bill(bill_id, name, cart, total, discount, tax, grand_total)
update_stock(stock_data)
print("Stock Updated Successfully!")


search = input("\nDo you want to search a bill by Bill ID? (yes/no): ").lower()
if search == "yes":
    search_id = input("Enter Bill ID to search: ")
    search_bill(search_id)
