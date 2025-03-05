import csv
import os
from datetime import datetime

DATA_FILE = 'atm_data.csv'

def initialize_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['account_number', 'pin', 'name', 'balance', 'created_at'])

def create_account():
    name = input('Enter your name: ')
    account_number = input('Enter account number: ')
    pin = input('Set your 4-digit PIN: ')
    initialize_data()
    with open(DATA_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([account_number, pin, name, 0, datetime.now().isoformat()])
    print('Account created successfully!')

def login():
    account_number = input('Account Number: ')
    pin = input('PIN: ')
    initialize_data()
    with open(DATA_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['account_number'] == account_number and row['pin'] == pin:
                return row
    print('Invalid credentials!')
    return None

def check_balance(account):
    print(f'Current Balance: ')

def deposit(account):
    amount = float(input('Enter amount to deposit: $'))
    if amount <= 0:
        print('Invalid amount!')
        return
    new_balance = float(account['balance']) + amount
    update_balance(account['account_number'], new_balance)
    print(f'Deposited . New balance: ')

def withdraw(account):
    amount = float(input('Enter amount to withdraw: $'))
    if amount <= 0 or amount > float(account['balance']):
        print('Invalid amount or insufficient funds!')
        return
    new_balance = float(account['balance']) - amount
    update_balance(account['account_number'], new_balance)
    print(f'Withdrew . New balance: ')

def update_balance(account_number, new_balance):
    accounts = []
    with open(DATA_FILE, 'r') as f:
        accounts = list(csv.DictReader(f))
    with open(DATA_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['account_number', 'pin', 'name', 'balance', 'created_at'])
        writer.writeheader()
        for account in accounts:
            if account['account_number'] == account_number:
                account['balance'] = str(new_balance)
            writer.writerow(account)

def main():
    while True:
        print('1. Create Account')
        print('2. Login')
        print('3. Exit')
        choice = input('Select option: ')
        if choice == '1':
            create_account()
        elif choice == '2':
            account = login()
            if account:
                print(f'Welcome, {account[\
