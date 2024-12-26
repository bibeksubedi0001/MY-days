import pandas as pd  # Importing the pandas library

# Step 1: Load the first CSV file into the DataFrame 'aa'
aa = pd.read_csv(r"D:\for_my_portfolio\Bibek_Subedi\Bibek_Subedi\rainfall_time_series.csv")

# Step 2: Load the second CSV file into the DataFrame 'a'
a = pd.read_csv(r"D:\for_my_portfolio\Bibek_Subedi\Bibek_Subedi\updated_rainfall_data.csv")

# Step 3: Display the first few rows of DataFrame 'aa'
print("First few rows of 'aa':")
print(aa.head())

# Step 4: Display the last few rows of DataFrame 'a'
print("\nLast few rows of 'a':")
print(a.tail())

# Step 5: Merge the two DataFrames 'aa' and 'a' based on a common column
# 'name' from 'aa' and 'Customer Name' from 'a'
lm = pd.merge(aa, a, left_on="name", right_on="Customer Name", how="left")

# Step 6: Display the merged DataFrame 'lm'
print("\nMerged DataFrame 'lm':")
print(lm)

# Step 7: Rename the "Condition" column in the merged DataFrame 'lm' to "Unknown_Parameter"
lm.rename(columns={"Condition": "Unknown_Parameter"}, inplace=True)

# Step 8: Display the selected columns 'Fuel Type' and 'Condition' from DataFrame 'a'
print("\n'Fuel Type' and 'Condition' columns from 'a':")
print(a[["Fuel Type", "Condition"]])

# Step 9: Create a DataFrame 'good' which contains rows where 'Condition' is 'Good'
good = a[a['Condition'] == 'Good'].copy()

# Step 10: Create a DataFrame 'Fair' which contains rows where 'Condition' is 'Fair'
Fair = a[a['Condition'] == 'Fair'].copy()

# Step 11: Concatenate the 'good' and 'Fair' DataFrames vertically into 'aaa'
aaa = pd.concat([good, Fair])

# Step 12: Display the concatenated DataFrame 'aaa'
print("\nConcatenated DataFrame 'aaa' (Good + Fair conditions):")
print(aaa)
