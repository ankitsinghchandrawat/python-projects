import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
data = pd.read_csv('C:/Users/achan/Desktop/pythonworkshop/data.csv')  # Replace with the correct path to your CSV file

# Display the first few rows of the data
print("Data Overview:")
print(data.head())

# Calculate the average of a selected column (e.g., 'Salary')
average_salary = data['Salary'].mean()
print("\nAverage Salary:", average_salary)

# Check basic statistical summary for numeric columns
print("\nStatistical Summary:")
print(data.describe())

# Visualizations using Matplotlib and Seaborn
sns.set_style("whitegrid")

# Bar Chart - Number of Employees in Each Department
plt.figure(figsize=(10, 6))
data['Department'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Number of Employees in Each Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.show()

# Scatter Plot - Age vs Salary
plt.figure(figsize=(10, 6))
plt.scatter(data['Age'], data['Salary'], color='red')
plt.title('Scatter Plot of Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()

# Heatmap - Correlation Matrix
plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Heatmap of Correlations')
plt.show()
