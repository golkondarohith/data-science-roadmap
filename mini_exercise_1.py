#Creating a class student with names and grades

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def show(self):
        print(f"Student {self.name} has grade {self.grade}")

#Dynamically writing student names into a file

#Enter the number of students
students = []
n = int(input("Enter the number of students: "))

for i in range(n):
    name = input(f"Enter student{i+1} name:")
    grade = input(f"Enter student{i+1} grade: ")
    students.append(Student(name, grade))


#Write the student details into the file 
with open("student.txt", "w") as f:
    for s in students:
        f.write(f"{s.name}, {s.grade}\n")

#Unload the student details from the file
loaded_students = []

with open("student.txt", "r") as f:
    for line in f:
        name, grade = line.strip().split(",")
        loaded_students.append(Student(name, grade))

print("\nLoaded students from file:")
for s in loaded_students:
    s.show()

 