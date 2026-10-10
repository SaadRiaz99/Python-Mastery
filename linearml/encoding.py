from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.read_csv("linearml/data.csv")
print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())

df[""]