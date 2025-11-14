import pandas as pd 

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance_score": [85, 90, 78, 92, 88, 95, 80, 89]
}


df = pd.DataFrame(data)
print("Display Original data: \n", df)

#Removing a single row from the dataset(Performance_score)
#syntax - df.drop(columns = ["Column_Name"], inplace = True)

# df.drop(columns = ["Performance_score"], inplace = True)
# print(df)

#Removing a multiple rows from the dataset(Performance_score, Age)
#syntax - df.drop(columns = ["Column_Name1", "Column_Name2"], inplace = True)

df.drop(columns = ["Performance_score", "Age"], inplace = True)
print("Modified dataset: \n", df)