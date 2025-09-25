
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    student_name = input(f"Enter the name of the student{i+1}:")
    marks = int(input(f"Enter the marks for student{i+1}"))
    students.append([student_name, marks])

for name, marks in students:
    print(f"Student {name} scored {marks}")

