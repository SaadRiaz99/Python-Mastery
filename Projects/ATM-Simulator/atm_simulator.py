import csv
import os

File_name = "AtmData_user.csv"
Trancs_name = "Transaction.csv"

# === FILE CREATION ===
if not os.path.exists(File_name):
    with open(File_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["username", "Name", "Email", "Phone", "Age", "Cnic", "Password", "Balance"])

if not os.path.exists(Trancs_name):
    with open(Trancs_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Email", "TransactionType", "Amount"])


# === ACCOUNT CREATION ===
def create_account():
    print("\n===== Create Bank Account =====")
    username = input("Enter Username: ")
    Name = input("Enter Full Name: ")
    Email = input("Enter Email: ")
    Phone = input("Enter Phone Number: ")
    Age = int(input("Enter Age (18 or above): "))
    Cnic = input("Enter National ID Number: ")
    Password = input("Enter Password: ")
    RePassword = input("Re-enter Password: ")

    if Password != RePassword:
        print("Passwords do not match! Try again.")
        return

    if Age < 18:
        print("Sorry, you must be 18 or older to create an account.")
        return

    # --- Safe Header Skip ---
    with open(File_name, "r") as f:
        reader = csv.reader(f)
        try:
            next(reader)
        except StopIteration:
            pass

        for row in reader:
            if row and row[2] == Email:
                print("Account with this email already exists.")
                return

    # --- Add new account ---
    balance = 0
    with open(File_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, Name, Email, Phone, Age, Cnic, Password, balance])
        print(f"Account created successfully! Welcome, {username}.")


# === LOGIN ===
def login():
    print("\n===== Login =====")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    with open(File_name, "r", newline="") as f:
        reader = csv.reader(f)
        try:
            next(reader)
        except StopIteration:
            pass

        for row in reader:
            if row and row[2] == email and row[6] == password:
                print(f"Welcome back, {row[1]} ({row[0]})!")
                user_dashboard(email)
                return

    print("Invalid email or password.")


# === DASHBOARD ===
def user_dashboard(email):
    while True:
        print("\n===== BANK DASHBOARD =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Logout")

        choice = input("Choose option: ")

        if choice == "1":
            check_balance(email)
        elif choice == "2":
            deposit(email)
        elif choice == "3":
            withdraw(email)
        elif choice == "4":
            show_transactions(email)
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice, try again!")


# === CHECK BALANCE ===
def check_balance(email):
    with open(File_name, "r") as f:
        reader = csv.reader(f)
        try:
            next(reader)
        except StopIteration:
            pass

        for row in reader:
            if row and row[2] == email:
                print(f"Your current balance is: Rs {row[7]}")
                return


# === DEPOSIT ===
def deposit(email):
    amount = int(input("Enter amount to deposit: "))
    data = []

    with open(File_name, "r") as f:
        reader = csv.reader(f)
        data = list(reader)

    for row in data:
        if row and row[2] == email:
            balance = int(row[7]) + amount
            row[7] = str(balance)

            with open(Trancs_name, "a", newline="") as t:
                writer = csv.writer(t)
                writer.writerow([email, "Deposit", amount])

            print(f"Rs {amount} deposited successfully. New balance: Rs {balance}")
            break

    with open(File_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)


# === WITHDRAW ===
def withdraw(email):
    amount = int(input("Enter amount to withdraw: "))
    data = []

    with open(File_name, "r") as f:
        reader = csv.reader(f)
        data = list(reader)

    for row in data:
        if row and row[2] == email:
            balance = int(row[7])
            if amount > balance:
                print("Insufficient balance!")
                return

            balance -= amount
            row[7] = str(balance)

            with open(Trancs_name, "a", newline="") as t:
                writer = csv.writer(t)
                writer.writerow([email, "Withdraw", amount])

            print(f"Rs {amount} withdrawn successfully. Remaining balance: Rs {balance}")
            break

    with open(File_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)


# === SHOW TRANSACTIONS ===
def show_transactions(email):
    print("\n===== TRANSACTION HISTORY =====")
    with open(Trancs_name, "r") as f:
        reader = csv.reader(f)
        try:
            next(reader)
        except StopIteration:
            pass

        found = False
        for row in reader:
            if row and row[0] == email:
                print(f"{row[1]} - Rs {row[2]}")
                found = True
        if not found:
            print("No transactions found.")


# === MAIN MENU ===
while True:
    print("\n===== ATM USER PORTAL =====")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        create_account()
    elif ch == "2":
        login()
    elif ch == "3":
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice! Try again.")
