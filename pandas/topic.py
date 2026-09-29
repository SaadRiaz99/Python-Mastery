import pandas as pd


data = {
   "Name": ["Saad Bin Riaz" , "Sumaiya" , "Talha Riaz"],
   "Age" : [19 ,25 ,9] ,
   "City" : ["Jhang" , "Jhang" ,"Jhang"]
}
sv = pd.DataFrame(data)
print(sv)

#see column
# 
se = sv.columns
clm = sv.shape
print(f"The Shape is {se}") 
print(f"The Column is {clm}") 