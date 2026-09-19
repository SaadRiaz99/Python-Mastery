import numpy as np

tempreatures = np.array([30, 25, 20, 15, 10 ,11 , 12, 13, 14])
num = np.array([15, 30, 25, 20, 15, 10 ,11 , 12, 13, 14, 15, 69, 748, 5468, 9481356, 5468, 48, 5468, 481, 0])
reshap = tempreatures.reshape((3, 3))
reshape = num.reshape((4, 5))
print(reshap)