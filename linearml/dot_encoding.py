from pathlib import Path
import pandas as pd

base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "data.csv"
df = pd.read_csv(csv_path)
# print(df.head())
# print(df.shape)
# print(df.info())
# print(df.isnull().sum())

df_label = df.copy()
df.columns = df.columns.str.strip()
dfa =pd.get_dummies(df, columns=["Session"])
# print(dfa)

df_departm4ent_encoding = pd.get_dummies(
    df,columns=["Department"],
    dtype=int
)
# print(df_departm4ent_encoding)

X = df[["Age", "Attendance_Percent", "Experience_Years"]]
y = df["Marks"]

print("Features (X):")
print(X.head())

print("\nTarget (y):")
print(y.head())