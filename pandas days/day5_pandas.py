import pandas as pd  # Importing the pandas library for data manipulation

# Step 1: Read the CSV file into a pandas DataFrame
# Replace the path with the correct file location on your system
hi = pd.read_csv(r"D:\for_my_portfolio\Bibek_Subedi\Bibek_Subedi\rainfall_time_series.csv")

# Step 2: Display the first 5 rows of the DataFrame to understand its structure
print("First 5 rows of the original DataFrame:")
print(hi.head())

# Step 3: Update specific rows and a column
# Set the "Precipitation" column values for rows with index 1 and 2 to 2.3
hi.loc[1:2, "Precipitation"] = 2.3

# Step 4: Display the updated rows to confirm changes
print("\nFirst 4 rows of the updated DataFrame:")
print(hi.head(4))
