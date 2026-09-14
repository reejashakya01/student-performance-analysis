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