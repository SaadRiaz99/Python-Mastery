import numpy as np

arr = np.array([1, 2, 3, 4, 5 , np.nan , np.inf])

na = np.isnan(arr)
print("Is NaN: ", na)