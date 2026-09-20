import numpy as np

prices = np.array([300 , 250 , 600 , 700 ,800])

discount = 0.10
final_price = []
after_discount = (prices * (1 - discount))

print("Prices after discount: ", after_discount)
for price in after_discount:
    total_price = price + (price * 0.05)
    final_price.append(price)
print("Final prices: ", final_price)
