import numpy as np
Salary = np.array([30000 , 25000 , 20000 , 15000 , 10000 ,11000 , 12000 , 13000 , 14000])

print("Salary of the company is : " , Salary)
print("Total Salary of the company is : " , Salary.sum())
print("Average Salary of the company is : " , Salary.mean())
print("Maximum Salary of the company is : " , Salary.max())
print("Minimum Salary of the company is : " , Salary.min())

print(Salary[Salary > 200000])
# print("Salary of the company is : " , Salary)
