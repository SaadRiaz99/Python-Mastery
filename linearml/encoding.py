from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.read_csv("data.csv")
# print(df.head())
# print(df.shape)
# print(df.info())
# print(df.isnull().sum())

df_label = df.copy()

# gender_encoder = LabelEncoder()
# session_encoder = LabelEncoder()

# df_label["Gender_Encoded"] = gender_encoder.fit_transform(df_label["Gender"])
# df_label["Session_Encoded"] = session_encoder.fit_transform(df_label["Session"])
gender_map = {
    "Male" :0,
    "Female" :1
}
session_map = {
    "Morning": 0,
    "Evening": 1
}

department_map = {
    "IT": 0,
    "HR": 1,
    "Sales": 2
}

df_label["Gender_encoded"] = df_label["Gender"].map(gender_map) 
df_label["Session_encoded"] = df_label["Session"].map(session_map) 
df_label["Department_encoded"] = df_label["Department"].map(department_map) 
print("\nENCODED DATA")
print(df_label.head())