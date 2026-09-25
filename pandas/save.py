import pandas as pd

data = {
   "Name": ["Saad Bin Riaz" , "Sumaiya Rani" , "Talha Riaz"],
   "Age" : [19 ,25 ,9] ,
   "City" : ["Jhang" , "Jhang" ,"Jhang"]
}
sv = pd.DataFrame(data)
print(sv)


sv.to_csv("Pandas/Filesave.csv" ,index =True )