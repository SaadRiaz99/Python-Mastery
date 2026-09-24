import numpy as np

products = np.array(["laptop", "mouse", "keyboard", "headphones"])


sales = np.array([
    [2, 1, 3, 0, 2, 4, 1],       # Laptop
    [5, 8, 6, 4, 10, 12, 7],     # Mouse
    [3, 2, 4, 1, 5, 6, 3],       # Keyboard
    [4, 3, 2, 5, 6, 8, 4]        # Headphones
])
prices = np.array([1000, 50, 75, 150])  # Prices for Laptop, Mouse, Keyboard, Headphones

sales = np.array([
    [2, 1, 3, 0, 2, 4, 1],       # Laptop
    [5, 8, 6, 4, 10, 12, 7],     # Mouse
    [3, 2, 4, 1, 5, 6, 3],       # Keyboard
    [4, 3, 2, 5, 6, 8, 4]        # Headphones
])
print("Sales Data:", sales)
