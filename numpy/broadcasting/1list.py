import numpy as np

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = [x+y for x,y in zip(list1, list2)]
print("Result of addition: ", result)

# isi ko vectorized approcah karte hain 

lst1 = np.array([1, 2, 3])
lst2 = np.array([4, 5, 6])

result = lst1 + lst2
print("Result of addition using numpy: ", result)