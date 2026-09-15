import pandas as pd

print("Student Performance Analysis with Pandas")

data = pd.read_csv("data/students.csv")
print(data)

print("\nNumber of Rows and Columns")
print(data.shape)

print("\nColumn Names")
print(data.columns)

print("\nDataset Information")
print("-------------------")
data.info()

print("\nStatistics Summary")
print("------------------")
print(data.describe())

print("\nMissing Values")
print("--------------")
print(data.isnull().sum())

data["Total"] = data["Math"] + data["Science"] + data["English"]
data["Average"] = data["Total"] / 3

print("\nStudent Totals and Averages")
print("---------------------------")
print(data[["Name", "Total", "Average"]])

print("\nAverage Marks by Gender")
print("-----------------------")

gender_averages = data.groupby("Gender")[["Math", "Science", "English", "Average"]].mean()

print(gender_averages)

print("\nAverage Marks by Subject")
print("------------------------")

subject_averages = data[["Math", "Science", "English"]].mean()
print(subject_averages)

best_subject = subject_averages.idxmax()
best_subject_average = subject_averages.max()

print("\nBest Performing Subject")
print("-----------------------")
print("Subject:", best_subject)
print("Average Mark:", best_subject_average)

print("\nStudent Ranking")
print("---------------")

ranking = data.sort_values(by="Average", ascending=False)

print(ranking[["Name", "Average"]])