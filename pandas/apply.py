import pandas as pd

df = pd.DataFrame({'Naam': ['Ali', 'Sana', "Saad"], 'Salary': [50000, 60000 , 40000]})


df["Salary"] = df['Salary'].apply(lambda x :x * 1.100)
print(df)