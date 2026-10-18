import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,r2_score

data = {
    'Name': ['Ali', 'Ayesha', 'Hamza', 'Sara', 'Zainab', 'Saad Bin Riaz'],
    'Attendance_Percentage': [90, 85, 75, 95, 80, 88],
    'Study_Hours': [3, 2, 4, 5, 3, 4],
    'Practice_Hours': [2, 1.5, 3, 4, 2.5, 3.5]
}

df = pd.DataFrame(data)
X = df[['Study_Hours', 'Attendance_Percentage']]
y = df['Practice_Hours']

model = LinearRegression()
dt = model.fit(X, y)
# new_data = pd.DataFrame([[4, 90]], columns=['Study_Hours', 'Attendance_Percentage'])
# prediction = dt.predict(
#     new_data
# )
# print(prediction)
# print(df)
# df["Name"] = df["Name"].str.upper()
# print("Data")
# print(df.to_string(index=False))
# print(df.isnull().sum())
y_pred = dt.predict(X)

# 4. Calculate metrics
mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"Mean Absolute Error: {mae:.2f} hours")
print(f"R-squared Score: {r2:.2f}")