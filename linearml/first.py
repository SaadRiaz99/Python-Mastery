from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as mp

years = np.array([2021, 2022, 2023, 2024, 2025]).reshape(-1, 1)

prices = np.array([110, 150, 250, 280, 260])
print("The Year is " ,years , "and Price is" ,prices)
