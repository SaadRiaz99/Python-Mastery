import numpy as np
import pandas as pd

df = pd.read_csv("numpy/employees_dirty.csv")
print(df.head(10))


print("missing values in each column:")
print(df.isnull().sum())
print("missing values in each row:")
print(df.isnull().sum(axis=1))
print(df)

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Department"] = df["Department"].fillna("Unknown")
df["Department"] = df["Department"].replace("HR", "Human Resources")
df["Department"] = df["Department"].replace("IT", "Information Technology")

df["performance-score"] = df["performance-score"].apply(lambda x: x * 0.35)
print(df)