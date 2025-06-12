import pandas as pd  # Importing pandas for data manipulation

# Step 1: Read the CSV file into a pandas DataFrame
# Replace the path with the correct location of your file
hi = pd.read_csv(r"C:\Users\Bibek\Documents\project\p2\rainfall_time_series.csv")

# Step 2: Display basic previews of the DataFrame
# Display the first 5 rows of the DataFrame
print("First 5 rows of the DataFrame:")
print(hi.head())

# Display the last 5 rows of the DataFrame
print("\nLast 5 rows of the DataFrame:")
print(hi.tail())

# Step 3: Random sampling
# Randomly select 8 rows from the DataFrame
print("\nRandom sample of 8 rows:")
print(hi.sample(8))

# Select 8 rows with a fixed random state for reproducibility
print("\nRandom sample of 8 rows with fixed random state (random_state=1):")
print(hi.sample(8, random_state=1))

# Step 4: Accessing specific rows and slices
# Select specific rows by index using `loc`
print("\nRows with index 17779, 1, and 2:")
print(hi.loc[[17779, 1, 2]])

# Slice rows from index 2 to 4 (inclusive) using `loc`
print("\nRows from index 2 to 4 (inclusive):")
print(hi.loc[2:4])

# Slice rows from index 35000 onwards using `loc`
print("\nRows from index 35000 onwards:")
print(hi.loc[35000:])

# Step 5: Accessing specific columns
# Select rows 3 to 7 for the column "Date"
print("\nRows 3 to 7 for the column 'Date':")
print(hi.loc[3:7, ["Date"]])

# Select all rows for the column "Date"
print("\nAll rows for the column 'Date':")
print(hi.loc[:, ["Date"]])

# Step 6: Access rows and columns by position using `iloc`
# Select rows 4 to 8 for the second column (index 1)
print("\nRows 4 to 8 for the second column (using `iloc`):")
print(hi.iloc[4:8, [1]])

# Step 7: Setting a new index
# Set the "Date" column as the index of the DataFrame
hi.index = hi['Date']
print("\nDataFrame with 'Date' set as the index:")
print(hi.head())

# Step 8: Access rows using the new DateTime index
# Select rows between specific dates/times
print("\nRows between '1/1/2019 0:00' and '1/1/2019 1:00':")
print(hi.loc["1/1/2019 0:00":"1/1/2019 1:00"])
