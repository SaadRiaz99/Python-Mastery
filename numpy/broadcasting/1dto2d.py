import numpy as np

arra1D = np.array([1, 2, 3])

arra2D = np.array([[1, 2, 3 ],
                   [6, 7, 8]])

vector = arra1D + arra2D
print("1D array: ", arra1D)
print("2D array: ", arra2D) 
print("Result of broadcasting: ", vector)

