import numpy as np

arra1D = np.array([1, 2])


arra2D = np.array([[1, 2, 3 ],
                   [6, 7, 8]])
res = arra1D.reshape(2,1,3)
vector = res + arra2D
print(vector)
