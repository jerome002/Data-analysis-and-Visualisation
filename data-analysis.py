# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set Seaborn style
sns.set(style="whitegrid")

# Task 1: Load and Explore the Dataset

# Load the Iris dataset
try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    print("Dataset loaded successfully!")
except Exception as e:
    print("Error loading dataset:", e)

# Display the first few rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Check data types and missing values
print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

# No missing values in this dataset, so no cleaning needed

# Task 2: Basic Data Analysis

# Basic statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Group by species and compute mean
grouped_means = df.groupby('species').mean()
print("\nMean values grouped by species:")
print(grouped_means)

# Interesting finding
print("\nObservation:")
print("Setosa has noticeably smaller petal length and width compared to other species.")

# Task 3: Data Visualization

# 1. Line Chart - Trend over index (not time-based, so this is just an example)
plt.figure(figsize=(10, 5))
df[['sepal length (cm)', 'sepal width (cm)']].plot()
plt.title("Sepal Length and Width Trend")
plt.xlabel("Index")
plt.ylabel("Value (cm)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# 2. Bar Chart - Average petal length by species
plt.figure(figsize=(6, 4))
sns.barplot(x=grouped_means.index, y=grouped_means['petal length (cm)'])
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.show()

# 3. Histogram - Distribution of sepal length
plt.figure(figsize=(6, 4))
sns.histplot(df['sepal length (cm)'], bins=15, kde=True)
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.tight_layout()
plt.show()

# 4. Scatter Plot - Sepal Length vs Petal Length
plt.figure(figsize=(6, 4))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.tight_layout()
plt.show()
