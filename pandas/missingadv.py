import numpy as np
import pandas as pd

data = {
    'Product': ['Mobile', 'Laptop', 'Tablet', 'Watch'],
    'Stock': [15, np.nan, 30, np.nan],       # Missing numbers
    'Brand': ['Samsung', 'Dell', None, 'Apple'] # Missing text
}
df = pd.DataFrame(data)
ind = {
    "Stock" : 60,
    "Brand" : "Aiee"
}

df["Stock"] = df['Stock'].fillna(1)
df['Brand'] = df['Brand'].fillna(value=ind)
print(df)