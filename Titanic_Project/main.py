import pandas as pd

df = pd.read_csv("tested.csv")

print(df.head())

print(df.info())
print(df.isnull().sum())
# Age ki missing values average se fill karo
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fare ki missing value average se fill karo
df["Fare"] = df["Fare"].fillna(df["Fare"].mean())

# Cabin ki missing values Unknown se fill karo
df["Cabin"] = df["Cabin"].fillna("Unknown")

# Dobara check karo
print(df.isnull().sum())
print("\nTotal Passengers:", len(df))

print("\nSurvived Count:")
print(df["Survived"].value_counts())

print("\nGender Count:")
print(df["Sex"].value_counts())

print("\nPassenger Class Count:")
print(df["Pclass"].value_counts())
import matplotlib.pyplot as plt

df["Pclass"].value_counts().plot(kind="bar")

plt.title("Passengers by Class")
plt.xlabel("Class")
plt.ylabel("Number of Passengers")

plt.show()
# Pie Chart
df["Sex"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Male vs Female Passengers")
plt.ylabel("")
plt.show()
# Dataset Statistics
print("\nDataset Statistics:")
print(df.describe())