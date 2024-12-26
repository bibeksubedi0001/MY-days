import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# 1. Creating a DataFrame
data = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'James'],
    'Age': [29, 34, 28, 40, 50],
    'Position': ['Manager', 'Developer', 'Designer', 'Developer', 'Manager'],
    'Department': ['HR', 'Engineering', 'Design', 'Engineering', 'HR'],
    'Salary': [60000, 80000, 55000, 75000, 70000]
}
df_employees = pd.DataFrame(data)

# 2. Handling Missing Data
df_employees.loc[2, 'Salary'] = np.nan  # Set a NaN value for Salary of Employee 3
print("Data with Missing Salary Value:")
print(df_employees)

# Fill missing Salary data with the mean value
df_employees['Salary'].fillna(df_employees['Salary'].mean(), inplace=True)
print("\nData after Filling Missing Salary Value with Mean:")
print(df_employees)

# 3. Data Transformation: Using apply and map
df_employees['Age Group'] = df_employees['Age'].map(lambda x: 'Senior' if x > 35 else 'Junior')
print("\nData after Creating 'Age Group' Column:")
print(df_employees)

# 4. Merging DataFrames
df_departments = pd.DataFrame({
    'Department': ['HR', 'Engineering', 'Design'],
    'Manager': ['Alice', 'Bob', 'Charlie']
})

df_employees = pd.merge(df_employees, df_departments, on='Department', how='left')
print("\nData after Merging with Department Info:")
print(df_employees)

# 5. Data Filtering with Boolean Indexing
junior_employees = df_employees[df_employees['Age Group'] == 'Junior']
print("\nJunior Employees:")
print(junior_employees)

# 6. GroupBy Operations
department_salary = df_employees.groupby('Department')['Salary'].mean()
print("\nAverage Salary by Department:")
print(department_salary)

# 7. Time Series: Creating a time-indexed DataFrame
date_range = pd.date_range(start='2023-01-01', periods=5, freq='D')
stock_data = {
    'Date': date_range,
    'Open': [150, 152, 153, 155, 157],
    'Close': [151, 153, 154, 156, 158]
}
df_stock = pd.DataFrame(stock_data)
df_stock.set_index('Date', inplace=True)

print("\nStock Data with Date Index:")
print(df_stock)

# Resampling the stock data to get weekly average
df_stock_resampled = df_stock.resample('W').mean()
print("\nWeekly Resampled Stock Data (Average):")
print(df_stock_resampled)

# 8. Using Scikit-learn for Machine Learning (Iris Dataset)
iris = load_iris()
X = iris.data
y = iris.target
df_iris = pd.DataFrame(X, columns=iris.feature_names)
df_iris['Species'] = iris.target_names[y]

# Splitting the data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a Logistic Regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train_scaled, y_train)

# Evaluate the model
accuracy = model.score(X_test_scaled, y_test)
print(f"\nLogistic Regression Model Accuracy: {accuracy * 100:.2f}%")

# 9. Data Visualization
df_employees['Salary'].plot(kind='bar', title='Employee Salaries')
plt.xlabel('Employee')
plt.ylabel('Salary')
plt.show()

# Plotting stock data (Open and Close prices)
df_stock[['Open', 'Close']].plot(title='Stock Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

# 10. Advanced Data Analysis: Using Categorical Data for Aggregation
df_iris['Species'] = df_iris['Species'].astype('category')
species_group = df_iris.groupby('Species')['sepal length (cm)'].mean()
print("\nAverage Sepal Length by Species:")
print(species_group)

# 11. Optimizing DataFrames: Changing data types
df_employees['Age'] = df_employees['Age'].astype('int8')
df_employees['Salary'] = df_employees['Salary'].astype('float32')

print("\nOptimized Data Types:")
print(df_employees.dtypes)

# 12. Working with Large Datasets (Simulated)
large_data = {
    'CustomerID': [f'C{str(i).zfill(5)}' for i in range(1, 100001)],
    'PurchaseAmount': np.random.uniform(50, 500, 100000),
    'PurchaseDate': pd.date_range('2023-01-01', periods=100000, freq='min')
}
df_large = pd.DataFrame(large_data)

# Processing in Chunks to Handle Large Data
chunk_size = 10000
chunks = pd.read_csv('large_dataset.csv', chunksize=chunk_size)
for chunk in chunks:
    # Example operation: Calculate mean purchase amount in each chunk
    print(f"\nProcessing Chunk: {chunk}")
    print("Mean Purchase Amount:", chunk['PurchaseAmount'].mean())

# 13. Handling Categorical Data and GroupBy
df_large['CustomerSegment'] = pd.cut(df_large['PurchaseAmount'], bins=[0, 100, 200, 300, 400, 500], labels=['Low', 'Medium', 'High', 'Very High', 'Premium'])
grouped_data = df_large.groupby('CustomerSegment').agg({
    'PurchaseAmount': 'mean',
    'CustomerID': 'count'
})
print("\nAggregated Data by Customer Segment:")
print(grouped_data)

# 14. Data Preprocessing for Machine Learning: Feature Engineering
df_iris['SepalArea'] = df_iris['sepal length (cm)'] * df_iris['sepal width (cm)']
df_iris['PetalArea'] = df_iris['petal length (cm)'] * df_iris['petal width (cm)']

# Feature selection for model
X_iris = df_iris[['SepalArea', 'PetalArea']]
y_iris = df_iris['Species']

# Split data for training and testing
X_train_iris, X_test_iris, y_train_iris, y_test_iris = train_test_split(X_iris, y_iris, test_size=0.3, random_state=42)

# Train Logistic Regression model
model_iris = LogisticRegression(max_iter=200)
model_iris.fit(X_train_iris, y_train_iris)

# Evaluate the model
accuracy_iris = model_iris.score(X_test_iris, y_test_iris)
print(f"\nLogistic Regression Model on Iris Dataset Accuracy: {accuracy_iris * 100:.2f}%")
