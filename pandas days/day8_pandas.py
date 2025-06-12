import pandas as pd  # Import pandas for data manipulation

# Step 1: Load the CSV file into a pandas DataFrame
qa = pd.read_csv(r"D:\for_my_portfolio\Bibek_Subedi\Bibek_Subedi\rainfall_time_series.csv")

# Step 2: Display the first few rows of the DataFrame
print("First 5 rows of the DataFrame:")
print(qa.head())

# Step 3: Display information about the DataFrame
print("\nDetailed info about the DataFrame:")
print(qa.info())  # Shows column names, non-null counts, and data types

# Step 4: Filter rows where "Precipitation" > 20.4
print("\nRows where 'Precipitation' > 20.4:")
print(qa.loc[qa["Precipitation"] > 20.4])  # Filters rows where "Precipitation" exceeds 20.4

# Display only the "Precipitation" column for rows where the condition is met
print("\n'Precipitation' values > 20.4:")
print(qa.loc[qa["Precipitation"] > 20.4, ["Precipitation"]])

# Step 5: Filter rows where "name" contains "Bibek"
print("\nRows where 'name' contains 'Bibek':")
print(qa[qa["name"].str.contains("Bibek", na=False)])  # Avoids errors if "name" contains NaN

# Step 6: Filter rows where "name" contains "Bibek" or "Raj"
print("\nRows where 'name' contains 'Bibek' or 'Raj':")
print(qa[qa["name"].str.contains("Bibek|Raj", na=False)])  # Regular expression for "Bibek" or "Raj"

# Step 7: Case-insensitive filtering for "name" containing "bibek" or "raj"
print("\nRows where 'name' contains 'bibek' or 'raj' (case-insensitive):")
print(qa[qa["name"].str.contains("bibek|raj", case=False, na=False)])

# Step 8: Filter rows where "name" contains "Bibek" or "Raj" (literal match, regex disabled)
print("\nRows where 'name' contains 'Bibek' or 'Raj' (regex disabled):")
print(qa[qa["name"].str.contains("Bibek|Raj", regex=False, na=False)])

# Step 9: Filter rows where "Category" is "Heavy" or "Light" AND "name" starts with 'Bibek'
print("\nRows where 'Category' is 'Heavy' or 'Light' and 'name' starts with 'Bibek':")
print(qa[(qa["Category"].isin(["Heavy", "Light"])) & (qa["name"].str.startswith("Bibek", na=False))])

# Step 10: Using `query` for filtering
print("\nRows where 'Humidity' == 65 and 'Category' == 'Light':")
print(qa.query('Humidity == 65 and Category == "Light"'))
