import numpy as np
import pandas as pd

data = {
    'Name': ['Ali', 'Ayesha', 'Hamza', 'Sara', 'Zainab'],
    'Department': ['IT', 'HR', 'IT', 'Sales', 'HR'],
    'Salary': [85000, 60000, 95000, 45000, 70000],
    'Experience_Years': [5, 3, 7, 1, 4]
}

df = pd.DataFrame(data)
print("--- ORIGINAL DATAFRAME ---")
print(df)
print("\n" + "="*50 + "\n")