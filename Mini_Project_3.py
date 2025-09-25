
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    student_name = input(f"Enter the name of the student{i+1}: ")
    marks = int(input(f"Enter the marks for student{i+1}: "))
    students.append([student_name, marks])

for name, marks in students:
    print(f"Student {name} scored {marks}")

with open("student.txt", "w") as f:
    for name, marks in students:
        f.write(f"Student {name} scored {marks}\n")

#Average Marks of the class
total_marks = sum([student[1] for student in students])
avg_marks = total_marks/len(students)
highest_marks = max(student[1] for student in students)



print(f"The average of the class is {avg_marks} and highest marks are {highest_marks}")

