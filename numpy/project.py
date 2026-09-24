import numpy as np

products = np.array(["laptop", "mouse", "keyboard", "headphones"])

prices = np.array([1000, 50, 75, 150])  # Prices for Laptop, Mouse, Keyboard, Headphones

days = np.array(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

sales = np.array([
    [2, 1, 3, 0, 2, 4, 1],       # Laptop
    [5, 8, 6, 4, 10, 12, 7],     # Mouse
    [3, 2, 4, 1, 5, 6, 3],       # Keyboard
    [4, 3, 2, 5, 6, 8, 4]        # Headphones
])


print("Sales Data:", sales)



print("Products:", products)
print("Days:", days)

print("Array Imformation")
print("Sales:\n", sales)
print("Shape:", sales.shape)
print("Dimensions:", sales.ndim)
print("Total elements:", sales.size)
print("Data type:", sales.dtype)


print("Indexing")

print(f"Sales of laptop in Week {sales[0]}")

weekend = sales[: ,5:]
print(weekend)
