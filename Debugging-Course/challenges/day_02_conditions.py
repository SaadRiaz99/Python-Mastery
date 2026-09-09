"""Day 2: Ages 18 and above are eligible. Fix the boundary bug."""

def can_apply(age):
    if age > 18:
        return True
    return False

assert can_apply(18) is True
assert can_apply(17) is False
print("Day 2 passed")
