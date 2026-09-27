import pandas as pd

df = pd.DataFrame({'Naam': ['Ali', 'Sana'], 'Salary': [50000, 60000]})


df["Salary"] = df['Salary'].apply(lambda x :x*0.10)
print(df)