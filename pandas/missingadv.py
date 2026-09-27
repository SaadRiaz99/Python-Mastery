import numpy as np
import pandas as pd

data = {
    'Product': ['Mobile', 'Laptop', 'Tablet', 'Watch'],
    'Stock': [15, np.nan, 30, np.nan],
    'Brand': ['Samsung', 'Dell', None, 'Apple']
}

df = pd.DataFrame(data)
spc = pd.Series([10 , 65 ], index = [1,3]) 
fill_values = {
    'Stock': 60,
    'Brand': 'Aiee'
}
df["Stock"] = df["Stock"].fillna(spc)
df = df.fillna(value=fill_values)
print(df)