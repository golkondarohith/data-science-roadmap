#Writing into a file

#Open a file in write mode
f = open("student.txt", "w")
f.write("Rohith - Grade 10\n")
f.write("Alice - Grade 4\n")
f.write("Jhon - Grade 7\n")
f.close



#Reading from the file
f = open("student.txt", "r")
content = f.read()
print(content)
f.close


#Using with

with open("student.txt", "a") as f:
    f.write("Maria - Grade 6\n")
