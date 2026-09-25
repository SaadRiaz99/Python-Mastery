import pandas as pd


#csv read data
print("CSV Data")
df = pd.read_csv("pandas/data.csv" , encoding="utf-8")
print(df)

#json read data
print("JSON Data")
js = pd.read_json("pandas/data.json")
print(js) 

print("HTml")
py = pd