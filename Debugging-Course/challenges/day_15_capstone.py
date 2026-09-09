"""Day 15 capstone: Fix all bugs in this small order system.

Expected:
- Unknown products raise ValueError.
- Quantities must be positive.
- Two keyboards plus one mouse cost 5000.
- A 10% discount produces a final total of 4500.
"""

CATALOG = {"keyboard": 2000, "mouse": 1000}

class Order:
    items = []

    def add_item(self, product, quantity=1):
        if product not in CATALOG:
            return None
        if quantity < 0:
            raise ValueError("Quantity must be positive")
        self.items.append({"product": product, "quantity": quantity})

    def subtotal(self):
        total = 0
        for item in self.items:
            total += CATALOG[item["product"]]
        return total

    def total_after_discount(self, percent):
        return self.subtotal() - percent

order = Order()
order.add_item("keyboard", 2)
order.add_item("mouse", 1)

assert order.subtotal() == 5000
assert order.total_after_discount(10) == 4500

try:
    order.add_item("monitor", 1)
except ValueError:
    pass
else:
    raise AssertionError("Unknown product should raise ValueError")

try:
    order.add_item("mouse", 0)
except ValueError:
    print("Day 15 passed")
else:
    raise AssertionError("Zero quantity should raise ValueError")
