import numpy as np
import pandas as pd
from pathlib import Path


# sales_data = pd.read_csv("../data/data.csv")
BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(BASE_DIR / "data" / "data.csv")
# df = pd.DataFrame(sales_data)

print(df.head(10))
print(df.Shape())
print(df.dtypes())
print(df.isnull().sum())
print(df.duplicated())