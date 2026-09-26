import pandas as pd
data = {
   "Name": ["Saad Bin Riaz" , "Sumaiya Rani" , "Talha Riaz"],
   "Age" : [19 ,25 ,9] ,
   "City" : ["Jhang" , "Jhang" ,"Jhang"],
   "Salary":[1000 , 5000 ,6000],
   "performance":[10,90,58]

}
frm = pd.DataFrame(data)
print("Save Data Frame")
print(frm)

print("Descriptive Statics")
print(frm.describe())
