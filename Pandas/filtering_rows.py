import pandas as pd 

data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'Jagdish', 'Raj', 'Simran'],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance_score": [85, 90, 78, 92, 88, 95, 80, 89]
}


df = pd.DataFrame(data)

#Displaying employee details whose salary is more than 50000
high_salary = df[df["Salary"] > 50000 ]
print(high_salary)


##Filtering employees with salary > 50000 and age > 30
filtered_rows = df[(df["Salary"] > 50000) & (df["Age"] > 30)]
print(filtered_rows)