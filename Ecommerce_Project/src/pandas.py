import pandas as pd
import analysis
print(analysis.df.head(10))
print(analysis.df.shape)
print(analysis.df.dtypes)
print(analysis.df.isnull().sum())
print(analysis.df.duplicated())

analysis.df["Time"]= pd.to_datetime(analysis.df["Time"])