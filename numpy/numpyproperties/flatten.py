import numpy as np
#.ravel() -> view
#.flatten -> copy
multidire = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
ravel = multidire.ravel()
flatten = multidire.flatten()
print(ravel)
print(flatten)
