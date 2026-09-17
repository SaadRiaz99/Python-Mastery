import numpy as np 
temperature = np.array([50.2, 72.5, 51.7, 41.0, 36.5])
name = np.array(["Saad Riaz", "Talha Riaz", "Jane Smith", "Umar Riaz", "Sumaiya Rani"])

print("Data type of the temperature array:", temperature.dtype)
print("Data type of the name array:", name.dtype)
typechange = temperature.astype(int)
print("Data type of the temperature array after conversion:", typechange.dtype)
print(typechange.dtype)