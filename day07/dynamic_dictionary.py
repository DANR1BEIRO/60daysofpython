# dynamic dictionary

student = {}

student["Name"] = input("Enter the student name: ")
student["Age"] = int(input("Enter the student age: "))
student["Course"] = input("Enter the student course: ")
student["Enrollment number"] = int(input("Enter the student enrollment number: "))

for k, v in student.items():
    print(f"{k}: {v}")