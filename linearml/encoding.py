from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.read_csv("data.csv")
print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())

df_label = df.copy()
le = LabelEncoder()

df_label["Gender_Encoded"] = le.fit_transform(df_label["Gender"]) 
df_label["Passed_Encoded"] = le.fit_transform(df_label["Passed_Gender"])
print(df_label) 