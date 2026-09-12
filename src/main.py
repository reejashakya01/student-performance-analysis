import csv 

print("Student Performance Analysis System")
print("-----------------------------------")
print("Loading student data...")

students = [
    {
        "name": "Salwin",
        "age": 19,
        "gender": "Male",
        "math": 78,
        "science": 82,
        "english": 75
    },
    {
        "name": "Sita",
        "age": 20,
        "gender": "Female",
        "math": 88,
        "science": 91,
        "english": 85
    },
    {
        "name": "Rohan",
        "age": 19,
        "gender": "Male",
        "math": 65,
        "science": 72,
        "english": 68
    }
]

for student in students:
    print(student)
    
print("\nStudent Total Marks")
print("-------------------")

for student in students:
    total = (student["math"]+ student["science"]+ student["english"])
    print(student["name"], ":", total)
    
print("\nStudent Average Marks")
print("---------------------")

for student in students:
    total = student["math"] + student["science"] + student["english"]
    average = total / 3
    print(student["name"], ":", average)
    
print("\nPerformance Result")
print("------------------")

for student in students:
    total = student["math"] + student["science"] + student["english"]
    average = total / 3

    if average >= 80:
        result = "Excellent"
    elif average >= 60:
        result = "Good"
    else:
        result = "Needs Improvement"

    print(student["name"], ":", result)
    

print("\nReading data from students.csv")
print("------------------------------")

with open("data/students.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Columns:", header)

    for row in reader:
        name = row[0]
        math = int(row[3])
        science = int(row[4])
        english = int(row[5])

        total = math + science + english
        average = total / 3
        
        if average >= 80:
            result = "Excellent"
        elif average >= 60:
            result = "Good"
        else:
            result = "Needs Improvement"

        print(name)
        print("Total:", total)
        print("Average:", average)
        print("Performance:", result)
        print()