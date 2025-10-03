import numpy as np

student_marks = np.random.randint(39, 101, size=12)
print("Student Marks:\n", student_marks)

print("Students who scored above 75 marks:\n", student_marks[student_marks > 75])