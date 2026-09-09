"""Day 6: Invalid input should return None, but programming errors must not be hidden."""

def safe_divide(first :int, second :int) -> float | None:
    try:
        return int(first) / int(second)
    except:
        return None

assert safe_divide(1, 2) == 0.5
assert safe_divide(10, 0) is None
# Make zero division visible instead of silently hiding it.
try:
    safe_divide(10, 8)
except ZeroDivisionError:
    print("Day 6 passed")
else:
    raise AssertionError("ZeroDivisionError was incorrectly hidden")
