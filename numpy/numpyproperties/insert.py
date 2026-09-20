import numpy as np


tempreatures = np.array([30, 25, 20, 15, 10 ,11 , 12, 13, 14])

numer = np.array([15, 30, 25, 20, 15, 10 ,11 , 12, 13, 14, 15, 69, 748, 5468, 9481356, 5468, 48, 5468, 481, 0])

names = np.array(["Saad Riaz", "Talha Riaz", "Jane Smith", "Umar Riaz", "Sumaiya Rani"])
inse = np.insert(numer , 0 , 00)
insei = np.insert(names , -1 , "Sumaiya ")
appendi = np.append(names , "Sumaiya Rani")
deletei = np.delete(names , 0)

#insert in 02d
tempreatures = np.array([[30, 25, 20,],[ 10 ,11 , 12]])
isneri2d = np.insert(tempreatures , 1 , [25, 30, 40] , axis = 0)
print(inse)
print(appendi)
print(deletei)
print(isneri2d)