from datetime import datetime

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

#Allocating grade
    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "F"
    
# Function to calculate average marks
def average_marks(students):
    return sum(student.marks for student in students) / len(students) if students else 0

# Function to find highest marks and top scorer(s)
def highest_marks(students):
    if not students:
        return 0, []
    high_marks = max(student.marks for student in students)
    top_students = [student.name for student in students if student.marks == high_marks]
    return high_marks, top_students

# Function to find lowest marks and bottom scorer(s)
def lowest_marks(students):
    if not students:
        return 0, []
    low_marks = min(student.marks for student in students)
    bottom_students = [student.name for student in students if student.marks == low_marks]
    return low_marks, bottom_students

# Main program
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    student_name = input(f"Enter the name of student {i+1}: ")

    # keep asking until valid marks
    while True:
        try:
            marks = int(input(f"Enter the marks for student {i+1}: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    students.append(Student(student_name, marks))

# Print student scores
for student in students:
    print(f"Student {student.name} scored {student.marks}")

# Write student scores to file
with open("student.txt", "a") as f:
    f.write("Report generated on: " + str(datetime.now()) + "\n\n")
    for student in students:
        f.write(f"Student {student.name} scored {student.marks} (Grade {student.grade()})\n")

# Calculate statistics
avg = average_marks(students)
high_marks, top_students = highest_marks(students)
low_marks, bottom_students = lowest_marks(students)

# Display statistics
print(f"\nClass Average: {avg:.2f}")
print(f"Highest Marks: {high_marks} by {', '.join(top_students)}")
print(f"Lowest Marks: {low_marks} by {', '.join(bottom_students)}")
print("\nFinal Student Grades:")
for student in students:
    print(f"Student {student.name} scored {student.marks} → Grade {student.grade()}")


