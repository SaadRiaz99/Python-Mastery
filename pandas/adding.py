import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Hamza", "Ayesha", "Saad", "Hina", "Bilal", "Noor", "Zain", "Iqra"],
    "Age": [20, 22, 19, 21, 23, 20, 24, 18, 22, 21],
    "Marks": [75, 88, 60, 92, 85, 70, 55, 95, 68, 80]
}

df = pd.DataFrame(data)
print(df)


df["Bonus_Marks"] = df["Marks"] * 0.10
print(df) 