from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

years = np.array([2021, 2022, 2023, 2024, 2025]).reshape(-1, 1)

prices = np.array([110, 150, 250, 280, 260])
print("The Year is " ,years , "and Price is" ,prices)
model = LinearRegression()

df = pd.DataFrame(
   {"Years" : years.flatten(),
    "Prcies" :prices}
)
x = years
y = prices
predict = model.fit(x,y)


future_years = np.array([[2026]])
predicted_price = model.predict(future_years)

print(f"\nPredicted petrol price for 2026: Rs. {predicted_price[0]:.2f}")

# Step 6: Visualize the result
plt.scatter(x.flatten(), y, label="Sample data")
plt.plot(x.flatten(), model.predict(x), label="Model prediction")
plt.xlabel("Year")
plt.ylabel("Petrol price (Rs./litre)")
plt.title("Petrol Price Prediction - Learning Project")
plt.legend()
plt.show()