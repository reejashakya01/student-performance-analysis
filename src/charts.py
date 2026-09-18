import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Student Performance Charts")

data = pd.read_csv("data/students.csv")

data["Total"] = data["Math"] + data["Science"] + data["English"]
data["Average"] = data["Total"] / 3

plt.figure(figsize=(10, 6))

plt.bar(data["Name"], data["Average"], color="skyblue")

plt.title("Student Average Marks")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.ylim(0, 100)

plt.tight_layout()
plt.show()
plt.savefig("charts/student_average_marks.png")
plt.show()

plt.figure(figsize=(7, 5))

sns.barplot(data=data, x="Gender", y="Average", hue="Gender", legend=False)

plt.title("Average Student Performance by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Marks")
plt.ylim(0, 100)

plt.tight_layout()
plt.savefig("charts/average_marks_by_gender.png")
plt.show()
