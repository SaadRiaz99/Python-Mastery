import numpy as np
import pandas as pd



data = {
    'Name': ['Ali', 'Ayesha', 'Hamza', 'Sara', 'Zainab' ,"Saad Bin Riaz"],
    'Department': ['IT', 'HR', 'IT', 'Sales', 'HR' , "IT"],
    'Salary': [85000, 60000, np.nan, 45000, 70000 , np.nan],
    'Experience_Years': [5, 3, 7, np.nan, 4 , np.nan]
}

df = pd.DataFrame(data)
print(df)
df["Name"] = df["Name"].str.upper()
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df.loc[df[3,"Experience_Years",5]]
print("Data")
print(df.to_string(index=False))
print(df.isnull().sum())
