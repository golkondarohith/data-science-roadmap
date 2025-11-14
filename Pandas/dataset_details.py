import pandas as pd 

data = {
    "Name":['Alice', 'John', 'koyes'],
    "Age": [10, 20, 30],
    "City": ['Nagpur', 'Mumbai', 'Delhi']
}
df = pd.DataFrame(data)

print(df)
print(df.shape)
print(df.columns)