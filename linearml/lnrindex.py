from sklearn.linear_model import LinearRegression
# Inputs: har inner list ek student ka data hai
X = [[1], [2], [3], [4], [5]]

# Outputs: un students ke marks
y = [30, 40, 50, 60, 70]

model = LinearRegression()
model.fit(X, y)


# 3. Naye input ke liye prediction
prediction = model.predict([[6]])

print("Weight:", round(model.coef_[0], 2))
print("Intercept:", round(model.intercept_, 2))
print("6 hours ke predicted marks:", round(prediction[0], 2))