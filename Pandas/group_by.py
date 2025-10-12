import pandas as pd


data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, 19, 22, 30, 19, 40, 22, 28],
    "Salary": [50000, 45000, 40000, 52000, 49000, 70000, 48000, 58000],
    "Performance_score": [85, None, 78, 92, 88, 95, 80, 89]
}


df = pd.DataFrame(data)
print("Display Original data: \n", df)


grouped = df.groupby("Age")["Salary"].sum()
print("Sum of Salaries by age: \n", grouped)

#grouping by multiple columns
grouped_mul = df.groupby(["Age", "Name"])["Salary"].sum()
print("Sum of Salaries by age: \n", grouped_mul)