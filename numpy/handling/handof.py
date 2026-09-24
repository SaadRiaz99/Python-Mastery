import numpy as np

arr = np.array([1, 2, 3, 4, 5 , np.nan , np.nan])
num_cler = np.nan_to_num(arr, nan=12)
na = np.isnan(arr)
print("Is NaN: ", na)
print(num_cler)
 