"""Day 8: Each bank account must keep its own transaction list."""

class BankAccount:
    transactions = []

    def __init__(self, owner):
        self.owner = owner
        self.transactions = []

    def deposit(self, amount):
        self.transactions.append(amount)

saad = BankAccount("Saad")
ali = BankAccount("Ali")
saad.deposit(500)
ali.deposit(2300)

assert saad.transactions == [500]
assert ali.transactions == [2300]
print("Day 8 passed")
