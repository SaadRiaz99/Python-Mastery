import numpy as np
import pandas as pd
from pathlib import Path


# sales_data = pd.read_csv("../data/data.csv")
BASE_DIR = Path(__file__).resolve().parent.parent

sales_data = pd.read_csv("data/data.csv")

df = pd.DataFrame(sales_data)


# df = pd.DataFrame(sales_data)

