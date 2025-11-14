import pandas as pd 

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance_score": [85, 90, 78, 92, 88, 95, 80, 89]
}


df = pd.DataFrame(data)
print("Display Original data: \n", df)

#Adding a bonus column to the extsting data
df["Bonus"] = df["Salary"] * 0.1
print("Displaying the Modified data: \n", df)


#Adding column using insert method
#syntax - df.insert(loc, "Column_Name", data)
df.insert(0, "Employee_ID", [501, 502, 503, 504, 505, 506, 507, 508] )
print(df)