import pandas as pd
import numpy as np

data = {
    "Name": ["Ali", "Sara", None, "Ayesha", "Saad",
             "Hina", "Bilal", "Noor", None, "Iqra"],
    "Age": [20, None, 19, 21, np.nan, 20, 24, None, 22, 21],
    "Marks": [75, 88, np.nan, 92, 85, None, 55, 95, 68, np.nan]
}

df = pd.DataFrame(data)
print(df)