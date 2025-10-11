import pandas as pd 

data = {
    "Name": ['Ram', None, 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, None, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, None, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance_score": [85, None, 78, 92, 88, 95, 80, 89]
}


df = pd.DataFrame(data)
print("Display Original data: \n", df)

#Droping allnull values
#dropna()

df.dropna(inplace = True)
print(df)