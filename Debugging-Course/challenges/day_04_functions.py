"""Day 4: Calculate price after percentage discount. Expected: 800."""

def discounted_price(price, discount_percent):
    discount = price * discount_percent
    print("DEBUG discount:", discount)
    # A function should give its result back to the caller.
    final_price = price - discount

result = discounted_price(1000, 20)
assert result == 800
print("Day 4 passed")
