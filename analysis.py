import pandas as pd
import matplotlib.pyplot as plt

# Load the student performance dataset
df = pd.read_csv("student-mat.csv", sep=";")

# Display basic information
print("First five rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

print("\nStatistical summary:")
print(df.describe())

# Explore study time and final grades
print("\nStudy time and final grades:")
print(df.groupby("studytime")["G3"].mean())

# Create a graph
df.groupby("studytime")["G3"].mean().plot(kind="bar")
plt.title("Average Final Grade by Study Time")
plt.xlabel("Study Time")
plt.ylabel("Average Final Grade")
plt.tight_layout()
plt.show()
