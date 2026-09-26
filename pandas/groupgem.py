import numpy as np
import pandas as pd
# ...existing code...
data = {
    "Name": ["Saad Bin Riaz", "Umar Bin Riaz", "Arsalan Mustafa", "Riaz", "Ayesha Khan", "Ali Hassan"],
    "Shop Branch": ["Gulshan", "Clifton", "Defence", "Nazimabad", "Johar", "Saddar"],
    "Branch Code": ["BR-101", "BR-205", "BR-310", "BR-118", "BR-402", "BR-515"],
    "City": ["Karachi", "Karachi", "Lahore", "Karachi", "Islamabad", "Rawalpindi"],
    "Manager": ["Hassan", "Naveed", "Mariam", "Bilal", "Sana", "Usman"],
    "Sales": [12000, 15000, 9800, 22000, 17000, 19000],
    "Customers": [180, 210, 140, 260, 190, 230],
    "Status": ["Active", "Active", "Inactive", "Active", "Active", "Active"]
}

dt = pd.DataFrame(data)
print(dt)
print("\n" + "="*50 + "\n")

total_sales_of_group = dt.groupby("Shop Branch")["Customers"].sum()
print(total_sales_of_group)