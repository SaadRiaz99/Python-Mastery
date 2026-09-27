import numpy as np
import pandas as pd

data = {
    'Product': ['Mobile', 'Laptop', 'Tablet', 'Watch'],
    'Stock': [15, np.nan, 30, np.nan],
    'Brand': ['Samsung', 'Dell', None, 'Apple']
}

df = pd.DataFrame(data)

fill_values = {
    'Stock': 60,
    'Brand': 'Aiee'
}

df = df.fillna(value=fill_values)
print(df)