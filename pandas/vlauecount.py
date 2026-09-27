import pandas as pd

# Sample dataset
df = pd.DataFrame({
    'Name': ['Ali', 'Sana', 'Zain', 'Kiran', 'Asif', 'Ayesha'],
    'City': ['Karachi', 'Lahore', 'Karachi', 'Islamabad', 'Karachi', 'Lahore']
})

pt = df["Name"].value_counts()
ps = df["City"].value_counts()
print(pt)
print(ps)