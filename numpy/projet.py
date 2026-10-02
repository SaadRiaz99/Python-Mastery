import numpy as np
import pandas as pd

df = pd.read_csv("numpy/employees_dirty.csv")
print(df.head(10))


print("missing values in each column:")
print(df.isnull().sum())
print("missing values in each row:")
print(df.isnull().sum(axis=1))
print(df)