"""Day 8: Each bank account must keep its own transaction list."""

class BankAccount:
    transactions = []

    def __init__(self, owner):
        self.owner = owner

    def deposit(self, amount):
        self.transactions.append(amount)

saad = BankAccount("Saad")
ali = BankAccount("Ali")
saad.deposit(500)

assert saad.transactions == [500]
assert ali.transactions == []
print("Day 8 passed")
