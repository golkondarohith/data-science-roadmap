import pandas as pd

df = pd.read_json("sample_Data.json")

print("Display first 10 rows: \n")
print(df.head(10))

print("Display last 10 rows: \n")
print(df.tail(10))