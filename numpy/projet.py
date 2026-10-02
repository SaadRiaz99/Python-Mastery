import numpy as np
import pandas as pd


df = pd.read_csv("numpy/employees_dirty.csv")
print(df.head(10))

print("missing values in each column:")
print(df.isnull().sum())
print("missing values in each row:")
print(df.isnull().sum(axis=1))

# Standardize column names to match the CSV file used in this project.
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Fill missing numeric columns with their mean values.
for col in ["age", "salary_pkr", "experience_years", "hours_per_week", "attendance_percent", "performance_score"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(df[col].mean())

# Clean categorical fields.
df["department"] = df["department"].fillna("Unknown")
df["department"] = df["department"].str.replace("HR", "Human Resources", case=False)
df["department"] = df["department"].str.replace("IT", "Information Technology", case=False)
df["city"] = df["city"].fillna("Unknown")

# Scale the performance score.
df["performance_score"] = df["performance_score"].apply(lambda x: x * 5.35)
print(df)

# Drop fake attendance values above 100% and show which rows are removed.
fake_attendance = df["attendance_percent"] > 100
if fake_attendance.any():
    print("Dropped fake attendance rows:")
    print(df.loc[fake_attendance, ["employee_id", "name", "department", "attendance_percent"]].to_string(index=False))
    df = df.loc[~fake_attendance].copy()
else:
    print("No employees with attendance percentage greater than 100%.")

attend = df["attendance_percent"].mean()
print(f"Average attendance percentage after dropping invalid rows: {attend:.2f}")
print(df.head())


df['performance_score']=df["performance_score"].apply(lambda x: float(x) * 2)
df['performance_score']=df["performance_score"].round(2)

print(df)
