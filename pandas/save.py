import pandas as pd

data = {
   "Name": ["Saad Bin Riaz" , "Su" , "Talha Riaz"],
   "Age" : [19 ,25 ,9] ,
   "City" : ["Jhang" , "Jhang" ,"Jhang"]
}
sv = pd.DataFrame(data)
print(sv)


sv.to_excel("Pandas/Filesave.xlsx")
sv.to_csv("Pandas/Filesave.csv" ,index =False )