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

math_total = 0
science_total = 0
english_total = 0
student_count = 0
highest_name = ""
highest_total = 0
lowest_name = ""
lowest_total = 1000
excellent_count = 0
good_count = 0
improvement_count = 0

with open("data/students.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("Columns:", header)

    for row in reader:
        name = row[0]
        math = int(row[3])
        science = int(row[4])
        english = int(row[5])
        student_count = student_count + 1
        math_total = math_total + math
        science_total = science_total + science
        english_total = english_total + english

        total = math + science + english
        average = total / 3
        if total > highest_total:
            highest_total = total
            highest_name = name
        if total < lowest_total:
            lowest_total = total
            lowest_name = name
        
        if average >= 80:
            result = "Excellent"
            excellent_count = excellent_count + 1

        elif average >= 60:
            result = "Good"
            good_count = good_count + 1
        else:
            result = "Needs Improvement"
            improvement_count = improvement_count + 1
            
            
        print(name)
        print("Total:", total)
        print("Average:", average)
        print("Performance:", result)
        print()
        
print("\nClass Subject Averages")
print("----------------------")

print("Math:", math_total / student_count)
print("Science:", science_total / student_count)
print("English:", english_total / student_count)

print("\nHighest Performer")
print("-----------------")
print("Name:", highest_name)
print("Total Marks:", highest_total)

print("\nLowest Performer")
print("-----------------")
print("Name:", lowest_name)
print("Total Marks:", lowest_total)

print("\nPerformance Summary")
print("-------------------")
print("Excellent:", excellent_count)
print("Good:", good_count)
print("Needs Improvement:", improvement_count)