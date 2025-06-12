import pandas as pd  # Importing the pandas library

# Create a simple DataFrame without specifying column names
df = pd.DataFrame([[1, 2, 4], [11, 10, 21], [111, 212, 313]])
# Print the first few rows of the DataFrame (default is 5 rows)
print("Initial DataFrame without column names:")
print(df.head())  # Displays the first 5 rows (if the DataFrame has more than 5 rows)

# Create another DataFrame with specified column names
df = pd.DataFrame([[1, 2, 4], [11, 10, 21], [111, 212, 313]], columns=["A", "B", "C"])
# Print the entire DataFrame to show the column names
print("\nDataFrame with specified column names:")
print(df.head())  # Displays the first 5 rows of the DataFrame

# Display only the first two rows of the DataFrame
print("\nFirst 2 rows of the DataFrame:")
print(df.head(2))

# Display only the last row of the DataFrame
print("\nLast row of the DataFrame:")
print(df.tail(1))

# Display the column names of the DataFrame
print("\nColumn names of the DataFrame:")
print(df.columns)

# Display the index of the DataFrame as a list
print("\nIndex of the DataFrame:")
print(df.index.tolist())

# Create another DataFrame with specified columns and a custom index
df = pd.DataFrame([[1, 2, 4], [11, 10, 21], [111, 212, 313]], 
                  columns=["A", "B", "C"], 
                  index=["B", 1, 2])
# Print the updated DataFrame with a custom index
print("\nDataFrame with custom index:")
print(df)

# Display detailed information about the DataFrame, such as column names, data types, and memory usage
print("\nDetailed information about the DataFrame:")
print(df.info())

# Display a summary of statistical measures (only for numerical columns)
print("\nStatistical summary of the DataFrame:")
print(df.describe())

# Count the number of unique values in each column
print("\nNumber of unique values in each column:")
print(df.nunique())

# Display the unique values in column "A"
print("\nUnique values in column 'A':")
print(df["A"].unique())

# Display the shape of the DataFrame (rows, columns)
print("\nShape of the DataFrame (rows, columns):")
print(df.shape)
