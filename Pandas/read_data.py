import pandas as pd

df = pd.read_json("sample_Data.json")

#Retrieving the first 10rows
print("Display first 10 rows: \n")
print(df.head(10))

#Retrieving the last 10 rows 
print("Display last 10 rows: \n")
print(df.tail(10))