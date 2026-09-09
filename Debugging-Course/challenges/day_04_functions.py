"""Day 4: Calculate price after percentage discount. Expected: 800."""

def discounted_price(price :int , discount_percent :float) -> float:
    discount = price * discount_percent / 100
    print("DEBUG discount:", discount)
    # A function should give its result back to the caller.
    final_price = price - discount
    return final_price

result = discounted_price(1000, 20)
assert result == 800
print("Day 4 passed")
