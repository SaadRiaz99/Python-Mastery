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

high_salary_mask = df["Salary"] > 650000
print("Step 1: The Boolean Mask (True/False values):")
print(high_salary_mask)
print("\nStep 2: Final Filtered Data:")
print(df[high_salary_mask])
print("\n" + "="*50 + "\n")