import pandas as pd

df = pd.DataFrame({'Naam': ['Ali', 'Sana', 'Zain'], 'Gender': ['M', 'F', 'M']})

changing = {"M" : "Male" , "F" :"Female"}
df["Gender"] = df["Gender"].map(changing)
print(df)