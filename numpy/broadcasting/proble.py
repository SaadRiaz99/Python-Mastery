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


# solution form numpy
# faster than for loop
rakam = np.array([319 , 279 , 650 , 560 ,1000])


discount = 0.02

total_pricesx = rakam - (rakam * discount)

print("Prices after discount: ", total_pricesx)